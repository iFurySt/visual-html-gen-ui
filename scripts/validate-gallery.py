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
    if "runtime deps" in index:
        failures.append("index.html should not show the runtime deps summary stat")
    if "white-space: nowrap;" not in index:
        failures.append("index.html should keep the gallery title on one line")
    if 'class="toc-sentinel"' not in index or 'toc.classList.toggle("is-stuck"' not in index:
        failures.append("index.html is missing sticky domain tag behavior")
    if "border: 1.5px solid var(--g300);" not in index or "border-radius: 10px;" not in index:
        failures.append("index.html should render the sticky tag bar as a framed surface")
    if "history.pushState(null, \"\", link.hash)" not in index or "alignToHash();" not in index:
        failures.append("index.html should preserve hash navigation and refresh alignment")
    if "const getTocOffset = () =>" not in index or "const stickyOffset = getTocOffset() + 2" not in index:
        failures.append("index.html should share scroll and active tag offset logic")
    if ".toggle::before,\n  .toggle::after" not in index or "details[open] .toggle::after" not in index:
        failures.append("index.html should render the fold toggle with CSS line icons")

    expected_links = {
        f"skills/visual-html-gen-ui/{domain['slug']}/{chart['slug']}.html"
        for domain in catalog["domains"]
        for chart in domain["charts"]
    }
    actual_links = set(re.findall(r'href="(skills/visual-html-gen-ui/[^"]+\.html)"', index))
    preview_count = len(re.findall(r'<iframe class="preview-frame" srcdoc=', index))
    navigating_previews = re.findall(
        r'<iframe class="preview-frame"[^>]+src="([^"]+)"',
        index,
    )

    for link in sorted(expected_links - actual_links):
        failures.append(f"missing gallery link: {link}")
    for link in sorted(actual_links - expected_links):
        failures.append(f"unknown gallery link: {link}")
    if preview_count != len(expected_links):
        failures.append(
            f"gallery preview iframe count mismatch: expected {len(expected_links)}, got {preview_count}"
        )
    for src in navigating_previews:
        failures.append(f"gallery preview iframe must use srcdoc, not src: {src}")
    for link in sorted(actual_links):
        if not (REPO_ROOT / link).is_file():
            failures.append(f"gallery link target does not exist: {link}")

    for domain in catalog["domains"]:
        section_marker = f'<details class="domain-section" id="{domain["slug"]}" open>'
        if section_marker not in index:
            failures.append(f"missing collapsible domain section: {domain['slug']}")
        toc_marker = f'href="#{domain["slug"]}"'
        if toc_marker not in index:
            failures.append(f"missing sticky tag link: {domain['slug']}")

    missing_preview_anchor = []
    for link in sorted(expected_links):
        if 'id="chart-preview"' not in (REPO_ROOT / link).read_text(encoding="utf-8"):
            missing_preview_anchor.append(link)
    for link in missing_preview_anchor:
        failures.append(f"chart target missing #chart-preview anchor: {link}")

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
