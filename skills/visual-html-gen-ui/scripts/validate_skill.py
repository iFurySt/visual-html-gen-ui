#!/usr/bin/env python3
"""Validate the generated visual-html-gen-ui skill."""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    catalog = json.loads((ROOT / "catalog.json").read_text(encoding="utf-8"))
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    failures: list[str] = []

    if not skill.startswith("---\nname: visual-html-gen-ui\n"):
        failures.append("SKILL.md frontmatter is missing or malformed")

    seen_domains: set[str] = set()
    seen_charts: set[tuple[str, str]] = set()

    for domain in catalog["domains"]:
        domain_slug = domain["slug"]
        if domain_slug in seen_domains:
            failures.append(f"duplicate domain slug: {domain_slug}")
        seen_domains.add(domain_slug)
        if f"### {domain['name']}" not in skill:
            failures.append(f"domain missing from SKILL.md: {domain_slug}")

        for chart in domain["charts"]:
            key = (domain_slug, chart["slug"])
            if key in seen_charts:
                failures.append(f"duplicate chart slug: {domain_slug}/{chart['slug']}")
            seen_charts.add(key)

            path = ROOT / domain_slug / f"{chart['slug']}.html"
            link = f"{domain_slug}/{chart['slug']}.html"
            if not path.is_file():
                failures.append(f"missing chart file: {link}")
                continue
            content = path.read_text(encoding="utf-8")
            if "<!doctype html>" not in content.lower():
                failures.append(f"chart is not standalone HTML: {link}")
            if "<script" in content.lower():
                failures.append(f"chart should not depend on inline JavaScript: {link}")
            if link not in skill:
                failures.append(f"chart link missing from SKILL.md: {link}")
            if chart["title"] not in content:
                failures.append(f"chart title missing in HTML: {link}")

    linked = set(re.findall(r"\(([^)]+\.html)\)", skill))
    expected = {
        f"{domain['slug']}/{chart['slug']}.html"
        for domain in catalog["domains"]
        for chart in domain["charts"]
    }
    for extra in sorted(linked - expected):
        failures.append(f"SKILL.md contains unknown chart link: {extra}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}", file=sys.stderr)
        return 1

    chart_count = sum(len(domain["charts"]) for domain in catalog["domains"])
    print(f"validated {len(catalog['domains'])} domains and {chart_count} charts")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
