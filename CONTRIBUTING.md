# Contributing

Thank you for helping keep this neural image compression map accurate and useful.

## Scope

The active list currently covers:

- surveys, benchmarks, and standards for neural still-image compression;
- lossless and near-lossless neural image compression;
- distortion-oriented lossy coding; and
- perception-oriented lossy coding.

Semantic or human-machine coding, special image domains, video, 3DGS, point clouds, and other broader visual compression topics are deferred for a later curation pass.

## Inclusion policy

Accepted conference and journal papers are preferred. A preprint is eligible only when it has public code and a clearly differentiated compression contribution. Use canonical HTTPS links such as DOI, CVF, OpenReview, arXiv abstract, or an official project page. Do not use temporary signed PDF URLs.

## Data schema

Add or update records in `data/papers.yml`. Required fields are:

- `id`: stable lowercase identifier using letters, digits, and hyphens;
- `title`, `first_author`, `year`, `venue`, and `status`;
- `paper_url` and optional `project_url` (`null` when unavailable);
- `section` and `objective`;
- list-valued `paradigm`, `focus`, and `capability`; and
- optional `summary` for landmark or recent core work.

The controlled vocabulary is enforced by `scripts/build_readme.py`. Survey and standards entries use `objective: null`. Preprints must use `section: emerging`, `venue: arXiv`, and include public code.

## Review checklist

1. Confirm the final publication status and year from an official source.
2. Search the YAML file for duplicate titles, DOI values, and arXiv identifiers.
3. Select one primary section and only applicable controlled tags.
4. Generate and validate the README:

   ```bash
   python -m pip install -r requirements.txt
   python scripts/build_readme.py
   python scripts/build_readme.py --check
   python scripts/check_links.py
   ```

5. Explain additions, migrations, merges, and removals in the pull request.

The live link checker fails only for confirmed `404` or `410` responses. Authentication failures, rate limits, and transient publisher/network errors are reported as warnings.
