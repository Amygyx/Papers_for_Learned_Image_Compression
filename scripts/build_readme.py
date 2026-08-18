#!/usr/bin/env python3
"""Validate data/papers.yml and generate the repository README."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

import yaml


ROOT = Path(__file__).resolve().parents[1]
DATA_PATH = ROOT / "data" / "papers.yml"
README_PATH = ROOT / "README.md"

SECTION_ORDER = [
    "surveys-benchmarks-standards",
    "lossless-near-lossless",
    "distortion-oriented",
    "perception-oriented",
]

SECTIONS = {
    "surveys-benchmarks-standards": (
        "Surveys, Benchmarks & Standards",
        "Surveys, evaluation resources, and standardization milestones for neural image compression.",
    ),
    "lossless-near-lossless": (
        "Lossless & Near-lossless Compression",
        "Neural lossless codecs and methods with explicit pointwise reconstruction-error constraints.",
    ),
    "distortion-oriented": (
        "Lossy — Distortion-oriented Coding",
        "Methods primarily optimized for rate-distortion performance using pixel-domain fidelity metrics.",
    ),
    "perception-oriented": (
        "Lossy — Perception-oriented Coding",
        "Methods primarily optimized for perceptual quality or the rate-distortion-perception trade-off.",
    ),
}

ALLOWED_OBJECTIVES = {"lossless", "near-lossless", "distortion", "perception"}
ALLOWED_PARADIGMS = {
    "autoregressive",
    "diffusion",
    "flow",
    "foundation-model",
    "gan",
    "inr",
    "overfitted",
    "transform",
    "vq",
}
ALLOWED_FOCUS = {
    "adaptation",
    "benchmark",
    "entropy-model",
    "optimization",
    "quantization",
    "standardization",
    "transform",
}
ALLOWED_CAPABILITIES = {
    "content-adaptive",
    "low-complexity",
    "practical",
    "progressive",
    "scalable",
    "variable-rate",
}
REQUIRED_FIELDS = {
    "id",
    "title",
    "first_author",
    "year",
    "venue",
    "status",
    "paper_url",
    "project_url",
    "section",
    "objective",
    "paradigm",
    "focus",
    "capability",
}


class ValidationError(ValueError):
    pass


def _validate_url(value: str | None, field: str, paper_id: str) -> None:
    if value is None:
        return
    parsed = urlparse(value)
    if parsed.scheme != "https" or not parsed.netloc:
        raise ValidationError(f"{paper_id}: {field} must be an absolute HTTPS URL")
    lowered = value.lower()
    if "x-amz-" in lowered or "sciencedirectassets.com" in lowered:
        raise ValidationError(f"{paper_id}: {field} uses an expiring signed URL")


def _validate_list(paper: dict, field: str, allowed: set[str]) -> None:
    value = paper[field]
    if not isinstance(value, list) or any(not isinstance(item, str) for item in value):
        raise ValidationError(f"{paper['id']}: {field} must be a list of strings")
    unknown = set(value) - allowed
    if unknown:
        raise ValidationError(f"{paper['id']}: unsupported {field}: {sorted(unknown)}")
    if len(value) != len(set(value)):
        raise ValidationError(f"{paper['id']}: duplicate value in {field}")


def validate(data: dict) -> list[dict]:
    if not isinstance(data, dict) or not isinstance(data.get("metadata"), dict):
        raise ValidationError("Top-level metadata mapping is required")
    papers = data.get("papers")
    if not isinstance(papers, list) or not papers:
        raise ValidationError("Top-level papers must be a non-empty list")

    last_curated = str(data["metadata"].get("last_curated", ""))
    if not re.fullmatch(r"20\d{2}-\d{2}-\d{2}", last_curated):
        raise ValidationError("metadata.last_curated must use YYYY-MM-DD")
    max_year = int(last_curated[:4])

    ids: set[str] = set()
    titles: set[str] = set()
    dois: set[str] = set()
    arxiv_ids: set[str] = set()

    for index, paper in enumerate(papers, start=1):
        if not isinstance(paper, dict):
            raise ValidationError(f"Paper #{index} must be a mapping")
        missing = REQUIRED_FIELDS - set(paper)
        if missing:
            raise ValidationError(f"Paper #{index} is missing fields: {sorted(missing)}")

        paper_id = paper["id"]
        if not isinstance(paper_id, str) or not re.fullmatch(r"[a-z0-9][a-z0-9-]*", paper_id):
            raise ValidationError(f"Paper #{index}: invalid id {paper_id!r}")
        if paper_id in ids:
            raise ValidationError(f"Duplicate id: {paper_id}")
        ids.add(paper_id)

        for field in ("title", "first_author", "venue", "status", "paper_url", "section"):
            if not isinstance(paper[field], str) or not paper[field].strip():
                raise ValidationError(f"{paper_id}: {field} must be a non-empty string")

        title_key = re.sub(r"\s+", " ", paper["title"].strip()).casefold()
        if title_key in titles:
            raise ValidationError(f"Duplicate title: {paper['title']}")
        titles.add(title_key)

        if not isinstance(paper["year"], int) or not 2010 <= paper["year"] <= max_year:
            raise ValidationError(f"{paper_id}: year is outside the supported range")
        if paper["section"] not in SECTIONS:
            raise ValidationError(f"{paper_id}: unsupported section {paper['section']}")
        if paper["status"] not in {"published", "preprint"}:
            raise ValidationError(f"{paper_id}: status must be published or preprint")

        objective = paper["objective"]
        if objective is not None and objective not in ALLOWED_OBJECTIVES:
            raise ValidationError(f"{paper_id}: unsupported objective {objective}")
        if paper["section"] == "surveys-benchmarks-standards" and objective is not None:
            raise ValidationError(f"{paper_id}: survey/standard records must use objective: null")
        if paper["section"] == "lossless-near-lossless" and objective not in {"lossless", "near-lossless"}:
            raise ValidationError(f"{paper_id}: lossless section requires a lossless objective")
        if paper["section"] == "distortion-oriented" and objective != "distortion":
            raise ValidationError(f"{paper_id}: distortion section requires objective: distortion")
        if paper["section"] == "perception-oriented" and objective != "perception":
            raise ValidationError(f"{paper_id}: perception section requires objective: perception")
        if paper["status"] == "preprint":
            raise ValidationError(f"{paper_id}: preprints are retained in DEFERRED.md, not the main index")

        _validate_list(paper, "paradigm", ALLOWED_PARADIGMS)
        _validate_list(paper, "focus", ALLOWED_FOCUS)
        _validate_list(paper, "capability", ALLOWED_CAPABILITIES)
        _validate_url(paper["paper_url"], "paper_url", paper_id)
        _validate_url(paper["project_url"], "project_url", paper_id)

        url = paper["paper_url"].lower()
        doi_match = re.search(r"doi\.org/(10\.[^?#]+)", url)
        if doi_match:
            doi = doi_match.group(1).rstrip("/")
            if doi in dois:
                raise ValidationError(f"Duplicate DOI: {doi}")
            dois.add(doi)
        arxiv_match = re.search(r"arxiv\.org/abs/(\d{4}\.\d{4,5})", url)
        if arxiv_match:
            arxiv_id = arxiv_match.group(1)
            if arxiv_id in arxiv_ids:
                raise ValidationError(f"Duplicate arXiv id: {arxiv_id}")
            arxiv_ids.add(arxiv_id)

    return papers


def _escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def _tag_list(paper: dict) -> str:
    tags: list[str] = []
    if paper["objective"]:
        tags.append(paper["objective"])
    tags.extend(paper["paradigm"])
    tags.extend(paper["focus"])
    tags.extend(paper["capability"])
    return " · ".join(f"`{tag}`" for tag in dict.fromkeys(tags))


def _paper_cell(paper: dict) -> str:
    return f"[{_escape(paper['title'])}]({paper['paper_url']})"


def _project_cell(project_url: str | None) -> str:
    if not project_url:
        return "—"

    parsed = urlparse(project_url)
    if parsed.netloc.lower() == "github.com":
        path_parts = [part for part in parsed.path.split("/") if part]
        if len(path_parts) >= 2:
            repository = "/".join(path_parts[:2])
            badge = f"https://img.shields.io/github/stars/{repository}.svg?style=social&label=Star"
            return f"[![Stars]({badge})]({project_url})"

    return f"[link]({project_url})"


def render(data: dict, papers: list[dict]) -> str:
    metadata = data["metadata"]
    counts = {section: 0 for section in SECTION_ORDER}
    for paper in papers:
        counts[paper["section"]] += 1

    lines = [
        "# Papers for Neural Image Compression",
        "**Purpose:** We aim to provide a summary of neural image compression. More papers will be summarized.",
        "",
        "University of Science and Technology of China (USTC), "
        "[Intelligent Media Computing Lab](https://faculty.ustc.edu.cn/chenzhibo).",
        "",
        "**📌 About new works.** If you want to incorporate your studies (e.g., the link of paper or project) "
        "on neural image compression in this repository. Welcome to raise an issue or email us. We will "
        "incorporate it into this repository and our survey report as soon as possible.",
        "",
        "<!-- Paper tables below are generated from data/papers.yml. -->",
        f"**Last curated:** {metadata['last_curated']}  ",
        f"**Coverage:** {len(papers)} selected publications and preprints.",
        "",
        "This first curation pass focuses on surveys and standards, lossless/near-lossless coding, "
        "distortion-oriented lossy coding, and perception-oriented lossy coding. Semantic or "
        "human-machine coding, special image domains, and broader visual compression are currently "
        "[deferred](DEFERRED.md).",
        "",
        "## Contents",
        "",
    ]

    for section in SECTION_ORDER:
        title = SECTIONS[section][0]
        anchor = title.lower().replace("—", "").replace("&", "").replace(" ", "-")
        anchor = re.sub(r"[^a-z0-9-]", "", anchor)
        anchor = re.sub(r"-+", "-", anchor).strip("-")
        lines.append(f"- [{title}](#{anchor})")

    lines.extend(["", "## Tag vocabulary", ""])
    lines.extend(
        [
            "- **Objective:** `lossless`, `near-lossless`, `distortion`, `perception`",
            "- **Paradigm:** `transform`, `flow`, `vq`, `inr`, `overfitted`, `gan`, `diffusion`, `foundation-model`",
            "- **Focus:** `transform`, `entropy-model`, `quantization`, `optimization`, `adaptation`",
            "- **Capability:** `variable-rate`, `progressive`, `scalable`, `content-adaptive`, `low-complexity`, `practical`",
            "",
        ]
    )

    for section in SECTION_ORDER:
        title, description = SECTIONS[section]
        section_papers = sorted(
            (paper for paper in papers if paper["section"] == section),
            key=lambda paper: (-paper["year"], paper["title"].casefold()),
        )
        lines.extend(
            [
                f"## {title}",
                "",
                description,
                "",
                "| Year | Paper | First author | Venue | Tags | Code / project |",
                "| :--: | --- | --- | --- | --- | :--: |",
            ]
        )
        for paper in section_papers:
            project = _project_cell(paper["project_url"])
            venue = _escape(paper["venue"])
            if paper["status"] == "preprint":
                venue += " (Preprint)"
            lines.append(
                f"| {paper['year']} | {_paper_cell(paper)} | {_escape(paper['first_author'])} | "
                f"{venue} | {_tag_list(paper)} | {project} |"
            )
        lines.append("")

    return "\n".join(lines)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--check", action="store_true", help="validate and verify README is current")
    args = parser.parse_args()

    try:
        with DATA_PATH.open("r", encoding="utf-8") as handle:
            data = yaml.safe_load(handle)
        papers = validate(data)
        rendered = render(data, papers)
    except (OSError, yaml.YAMLError, ValidationError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 1

    if args.check:
        try:
            current = README_PATH.read_text(encoding="utf-8")
        except OSError as exc:
            print(f"error: {exc}", file=sys.stderr)
            return 1
        if current != rendered:
            print("error: README.md is not synchronized with data/papers.yml", file=sys.stderr)
            return 1
        print(f"Validated {len(papers)} papers; README.md is up to date.")
        return 0

    README_PATH.write_text(rendered, encoding="utf-8", newline="\n")
    print(f"Generated README.md from {len(papers)} validated records.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
