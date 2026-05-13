#!/usr/bin/env python3
"""Validate the generated GitHub Pages gallery."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
CATALOG_PATH = REPO_ROOT / "skills" / "visual-html-gen-ui" / "catalog.json"
INDEX_PATH = REPO_ROOT / "index.html"


def main() -> int:
    failures: list[str] = []
    if not INDEX_PATH.is_file():
        failures.append("missing root index.html")
        return report(failures)

    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    index = INDEX_PATH.read_text(encoding="utf-8")

    if "Visual HTML Gen UI" not in index:
        failures.append("index.html is missing the gallery title")

    expected_links = {
        f"skills/visual-html-gen-ui/{domain['slug']}/{chart['slug']}.html"
        for domain in catalog["domains"]
        for chart in domain["charts"]
    }
    actual_links = set(re.findall(r'href="(skills/visual-html-gen-ui/[^"]+\.html)"', index))

    for link in sorted(expected_links - actual_links):
        failures.append(f"missing gallery link: {link}")
    for link in sorted(actual_links - expected_links):
        failures.append(f"unknown gallery link: {link}")
    for link in sorted(actual_links):
        if not (REPO_ROOT / link).is_file():
            failures.append(f"gallery link target does not exist: {link}")

    for domain in catalog["domains"]:
        if f'id="{domain["slug"]}"' not in index:
            failures.append(f"missing domain section: {domain['slug']}")

    return report(failures)


def report(failures: list[str]) -> int:
    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1
    print("gallery index validated")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
