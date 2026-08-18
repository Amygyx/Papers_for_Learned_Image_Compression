#!/usr/bin/env python3
"""Check paper and project links without making transient publisher errors CI-fatal."""

from __future__ import annotations

import argparse
import concurrent.futures
import html
import json
import re
import socket
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.yml"
USER_AGENT = "Mozilla/5.0 neural-image-compression-index-link-check/1.0"
STOP_WORDS = {
    "a", "an", "and", "at", "based", "by", "for", "from", "in", "is", "of",
    "on", "the", "to", "via", "with",
}


def probe(url: str, timeout: float) -> tuple[str, str, int | None]:
    request = urllib.request.Request(url, method="HEAD", headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return "ok", url, response.status
    except urllib.error.HTTPError as exc:
        if exc.code == 405:
            request = urllib.request.Request(
                url,
                method="GET",
                headers={"User-Agent": USER_AGENT, "Range": "bytes=0-0"},
            )
            try:
                with urllib.request.urlopen(request, timeout=timeout) as response:
                    return "ok", url, response.status
            except urllib.error.HTTPError as get_exc:
                exc = get_exc
        if exc.code in {404, 410}:
            return "error", url, exc.code
        return "warn", url, exc.code
    except (urllib.error.URLError, TimeoutError, socket.timeout):
        return "warn", url, None


def normalize(text: str) -> str:
    return " ".join(re.findall(r"[a-z0-9]+", html.unescape(text).lower()))


def title_tokens(title: str) -> list[str]:
    return [
        token
        for token in normalize(title).split()
        if len(token) >= 4 and token not in STOP_WORDS
    ]


def compare_title(paper: dict[str, object], observed_title: str) -> tuple[str, str]:
    expected = normalize(str(paper["title"]))
    observed = normalize(observed_title)
    if expected in observed:
        return "MATCH", "full title found"

    expected_tokens = title_tokens(str(paper["title"]))
    matched_tokens = [token for token in expected_tokens if token in observed]
    required = min(len(expected_tokens), max(3, (len(expected_tokens) + 1) // 2))
    if len(matched_tokens) >= required:
        return "PARTIAL", f"{len(matched_tokens)}/{len(expected_tokens)} distinctive title terms found"
    return "MISMATCH", f"only {len(matched_tokens)}/{len(expected_tokens)} distinctive title terms found"


def inspect_doi(paper: dict[str, object], timeout: float) -> tuple[str, str, str]:
    doi = urllib.parse.urlparse(str(paper["paper_url"])).path.lstrip("/")
    metadata_url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="/")
    request = urllib.request.Request(metadata_url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            metadata = json.load(response)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, socket.timeout, json.JSONDecodeError) as exc:
        return "UNVERIFIED", str(paper["id"]), f"DOI metadata request failed ({getattr(exc, 'code', 'network')})"

    titles = metadata.get("message", {}).get("title", [])
    if not titles:
        return "UNVERIFIED", str(paper["id"]), "DOI metadata has no title"
    status, detail = compare_title(paper, str(titles[0]))
    return status, str(paper["id"]), f"Crossref: {detail}"


def inspect_paper(paper: dict[str, object], timeout: float) -> tuple[str, str, str]:
    """Check whether an HTML landing page mentions the indexed paper title.

    Publishers sometimes block automated content reads or serve PDFs. Those cases
    are deliberately reported as UNVERIFIED rather than false failures.
    """
    url = str(paper["paper_url"])
    host = urllib.parse.urlparse(url).netloc
    if host == "doi.org":
        return inspect_doi(paper, timeout)
    request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            content_type = response.headers.get_content_type()
            payload = response.read(1_500_000)
    except (urllib.error.HTTPError, urllib.error.URLError, TimeoutError, socket.timeout) as exc:
        return "UNVERIFIED", str(paper["id"]), f"request failed ({getattr(exc, 'code', 'network')})"

    if content_type not in {"text/html", "application/xhtml+xml"}:
        return "UNVERIFIED", str(paper["id"]), f"non-HTML landing page ({content_type})"

    status, detail = compare_title(paper, payload.decode("utf-8", errors="ignore"))
    if status == "MISMATCH" and host in {
        "openreview.net",
        "ieeexplore.ieee.org",
        "www.nature.com",
    }:
        # These sites render citation metadata client-side or behind bot checks.
        # A missing title in the raw response is not evidence of a wrong link.
        return "UNVERIFIED", str(paper["id"]), f"metadata not exposed in raw {host} response"
    return status, str(paper["id"]), detail


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--workers", type=int, default=8)
    parser.add_argument(
        "--verify-paper-metadata",
        action="store_true",
        help="also compare each paper URL landing page with its indexed title",
    )
    args = parser.parse_args()

    with DATA_PATH.open("r", encoding="utf-8") as handle:
        data = yaml.safe_load(handle)

    urls = sorted(
        {
            paper[field]
            for paper in data["papers"]
            for field in ("paper_url", "project_url")
            if paper.get(field)
        }
    )
    results: list[tuple[str, str, int | None]] = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(probe, url, args.timeout) for url in urls]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    errors = sorted(result for result in results if result[0] == "error")
    warnings = sorted(result for result in results if result[0] == "warn")
    ok_count = len(results) - len(errors) - len(warnings)
    print(f"Checked {len(results)} unique links: {ok_count} ok, {len(warnings)} warnings, {len(errors)} broken.")
    for _, url, status in warnings:
        detail = str(status) if status is not None else "network/timeout"
        print(f"WARN {detail}: {url}")
    for _, url, status in errors:
        print(f"ERROR {status}: {url}")

    if not args.verify_paper_metadata:
        return 1 if errors else 0

    print("\nPaper title verification:")
    paper_results: list[tuple[str, str, str]] = []
    papers = [paper for paper in data["papers"] if paper.get("paper_url")]
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(inspect_paper, paper, args.timeout) for paper in papers]
        for future in concurrent.futures.as_completed(futures):
            paper_results.append(future.result())

    for status, paper_id, detail in sorted(paper_results):
        print(f"{status:<11} {paper_id}: {detail}")
    mismatches = [result for result in paper_results if result[0] == "MISMATCH"]
    verified = sum(result[0] in {"MATCH", "PARTIAL"} for result in paper_results)
    unverified = sum(result[0] == "UNVERIFIED" for result in paper_results)
    print(
        f"Verified {verified}/{len(paper_results)} paper pages; "
        f"{unverified} need manual review; {len(mismatches)} mismatches."
    )
    return 1 if errors or mismatches else 0


if __name__ == "__main__":
    raise SystemExit(main())
