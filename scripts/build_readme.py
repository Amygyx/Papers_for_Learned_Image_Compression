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
    "other-tasks-encryption",
]

SECTIONS = {
    "surveys-benchmarks-standards": (
        "Surveys, Benchmarks & Standards",
        "Surveys, evaluation resources, and standardization milestones for neural image compression.",
    ),
    "lossless-near-lossless": (
        "Lossless & Near-lossless Compression",
        "",
    ),
    "distortion-oriented": (
        "Lossy — Distortion-oriented Coding",
        "Methods primarily optimized for rate-distortion performance using pixel-domain fidelity metrics.",
    ),
    "perception-oriented": (
        "Lossy — Perception-oriented Coding",
        "Methods primarily optimized for perceptual quality or the rate-distortion-perception trade-off.",
    ),
    "other-tasks-encryption": (
        "Other tasks",
        None,
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

# Approximate annual main-conference chronology.  This only breaks ties within
# a year; journals follow the conference venues and use title order as a tie-breaker.
CONFERENCE_RECENCY = {
    "NeurIPS": 1200,
    "ACCV": 1100,
    "ICCV": 1000,
    "ACM MM": 950,
    "ECCV": 900,
    "BMVC": 850,
    "ICML": 700,
    "CVPR": 600,
    "ICLR": 450,
    "WACV": 200,
    "AAAI": 100,
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

SHORT_NAMES = {
    "fnlic-2025": "FNLIC",
    "lossless-inr-2025": "LosslessINR",
    "bit-plane-lossless-2024": "--",
    "dlpr-2024": "DLPR",
    "lc-fdnet-2022": "LC-FDNet",
    "pilc-2022": "PILC",
    "idf-plus-plus-2021": "IDF++",
    "iflow-2021": "iFlow",
    "osoa-2021": "OSOA",
    "ivpf-2021": "iVPF",
    "l3c-2019": "L3C",
    "deephq-2026": "DeepHQ",
    "causal-contextual-prediction-2022": "--",
    "diffeic-2025": "DiffEIC",
    "rdeic-2025": "RDEIC",
    "glc-2024": "GLC",
    "segpic-2024": "SegPIC",
    "perco-2024": "PerCo",
    "sga-plus-2024": "SGA+",
    "olvq-2024": "OLVQ",
    "glic-2026": "GLIC",
    "cmic-2026": "CMIC",
    "nefic-2026": "NeFIC",
    "kdic-2025": "KDiC",
    "hpcm-2025": "HPCM",
    "cassic-2025": "Cassic",
    "dcae-2025": "DCAE",
    "lalic-2025": "LALIC",
    "adaptive-lvq-2025": "ALVQ",
    "cca-2024": "CCA",
    "weconvene-2024": "WeConvene",
    "basic-2024": "BaSIC",
    "wclic-2024": "WCLIC",
    "tcm-2023": "TCM",
    "nvtc-2023": "NVTC",
    "elic-2022": "ELIC",
    "contextformer-2022": "Contextformer",
    "cod-2026": "CoD",
    "cadc-2026": "CADC",
    "dit-ic-2026": "DiT-IC",
    "cdc-2023": "CDC",
    "hific-2020": "HiFiC",
    "bit-swap-2019": "Bit-Swap",
    "bb-ans-2019": "BB-ANS",
    "local-bits-back-2019": "LBB",
    "diffc-2025": "DiffC",
    "ddcm-2025": "DDCM",
    "cod-lite-2026": "CoD-Lite",
    "turbo-ddcm-2026": "Turbo-DDCM",
    "ms-illm-2023": "MS-ILLM",
    "taco-2024": "TACO",
    "oscar-2025": "OSCAR",
    "onedc-2025": "OneDC",
    "stablecodec-2025": "StableCodec",
    "relic-uq-2025": "--",
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
        if "workshop" in paper["venue"].casefold():
            raise ValidationError(f"{paper_id}: workshop papers are retained in DEFERRED.md, not the main index")

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
        if paper["section"] == "other-tasks-encryption":
            if objective is not None:
                raise ValidationError(f"{paper_id}: encryption records must use objective: null")
            if not isinstance(paper.get("method"), str) or not paper["method"].strip():
                raise ValidationError(f"{paper_id}: encryption records require a method")
            if not isinstance(paper.get("legacy_order"), int):
                raise ValidationError(f"{paper_id}: encryption records require legacy_order")
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


def _model_cell(paper: dict) -> str:
    return SHORT_NAMES.get(paper["id"], "--")


def _venue_cell(paper: dict) -> str:
    venue = _escape(paper["venue"]).removeprefix("IEEE ")
    return f"{venue}{paper['year']}"


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
        "## Contents",
        "",
    ]

    for section in SECTION_ORDER:
        title = SECTIONS[section][0]
        # Match GitHub's heading-slug behavior: remove punctuation first, then
        # replace every remaining space.  Do not collapse adjacent hyphens.
        anchor = re.sub(r"[^a-z0-9 -]", "", title.lower()).replace(" ", "-")
        lines.append(f"- [{title}](#{anchor})")

    # Tag vocabulary remains validated in the data schema, but is intentionally
    # hidden from the README while the tables do not display per-paper tags.
    lines.append("")

    for section in SECTION_ORDER:
        title, description = SECTIONS[section]
        section_papers = (paper for paper in papers if paper["section"] == section)
        if section == "other-tasks-encryption":
            section_papers = sorted(section_papers, key=lambda paper: paper["legacy_order"])
        else:
            section_papers = sorted(
                section_papers,
                key=lambda paper: (
                    -paper["year"],
                    -CONFERENCE_RECENCY.get(paper["venue"].removeprefix("IEEE "), 0),
                    paper["title"].casefold(),
                ),
            )
        if section == "other-tasks-encryption":
            lines.extend(
                [
                    f"## {title}",
                    "",
                    "### Encryption",
                    "",
                    "| Methods | Paper | First Author | Venue |",
                    "| :--: | :---: | :--: | :--: |",
                ]
            )
        else:
            lines.extend(
                [
                    f"## {title}",
                    "",
                    description,
                    "",
                    "| Models | Paper | First Author | Venue | Project |",
                    "| :--: | :---: | :--: | :--: | :--: |",
                ]
            )
        for paper in section_papers:
            if section == "other-tasks-encryption":
                lines.append(
                    f"| {_escape(paper['method'])} | {_paper_cell(paper)} | "
                    f"{_escape(paper['first_author'])} | {_escape(paper['venue'])} |"
                )
                continue
            project = _project_cell(paper["project_url"])
            lines.append(
                f"| {_model_cell(paper)} | {_paper_cell(paper)} | {_escape(paper['first_author'])} | "
                f"{_venue_cell(paper)} | {project} |"
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
