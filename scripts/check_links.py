#!/usr/bin/env python3
"""Check paper and project links without making transient publisher errors CI-fatal."""

from __future__ import annotations

import argparse
import concurrent.futures
import socket
import sys
import urllib.error
import urllib.request
from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.yml"
USER_AGENT = "Mozilla/5.0 neural-image-compression-index-link-check/1.0"


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


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--timeout", type=float, default=15.0)
    parser.add_argument("--workers", type=int, default=8)
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
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
