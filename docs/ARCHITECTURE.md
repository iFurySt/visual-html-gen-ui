# Architecture

This repository packages a Codex skill for standalone visual HTML chart
examples. The skill is source-controlled inside the repo instead of installed
globally so agents can review, extend, validate, and commit it in small slices.

## Repository Shape

- `skills/visual-html-gen-ui/`: the skill consumed by agents.
- `skills/visual-html-gen-ui/SKILL.md`: compact table of contents and usage
  entry point.
- `skills/visual-html-gen-ui/catalog.json`: source catalog for domains and
  charts.
- `skills/visual-html-gen-ui/<domain>/<chart>/index.html`: generated,
  standalone chart examples.
- `skills/visual-html-gen-ui/scripts/`: generation and validation utilities.
- `docs/`: collaboration guides, execution plans, histories, and quality notes.

## Boundary Rules

- Keep `SKILL.md` as navigation only; detailed examples belong in individual
  chart HTML files.
- Edit `catalog.json` for domain and chart changes, then regenerate outputs
  with `scripts/build_charts.py`.
- Generated chart examples should remain dependency-free HTML/CSS/SVG and
  follow the visual baseline from `~/projects/github/html-effectiveness`.
- Validation belongs in executable scripts so future agents can detect catalog,
  link, and output drift.

## Data Flow

1. Maintainer edits `skills/visual-html-gen-ui/catalog.json`.
2. `scripts/build_charts.py` generates `SKILL.md` and every chart
   `index.html`.
3. `scripts/validate_skill.py` checks frontmatter, catalog uniqueness, chart
   files, links, standalone HTML shape, and title coverage.
4. `make ci` runs repository-level checks, including skill validation.
