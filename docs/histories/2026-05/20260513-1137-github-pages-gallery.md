## [2026-05-13 11:37] | Task: GitHub Pages gallery

### Execution Context

- Agent ID: `codex`
- Base Model: `GPT-5`
- Runtime: `Codex CLI`

### User Query

> Add a GitHub Pages page for `visual-html-gen-ui`, with a root `index.html`
> similar to the `html-effectiveness` preview/index page but grouped by domain.

### Changes Overview

- Area: GitHub Pages gallery
- Key actions:
  - Added a generated root `index.html` gallery.
  - Added `scripts/build-gallery.py` to render the gallery from the skill
    catalog.
  - Added `scripts/validate-gallery.py` and wired it into CI.
  - Updated README and architecture docs with the gallery workflow.

### Design Intent

The gallery uses the same visual baseline as the local `html-effectiveness`
index: ivory background, restrained serif headings, mono metadata, compact
domain pills, thin rules, and card-based previews. It adds one level of
organization for domains, then links each card to its standalone chart HTML.

### Files Modified

- `index.html`
- `scripts/build-gallery.py`
- `scripts/validate-gallery.py`
- `scripts/ci.sh`
- `Makefile`
- `README.md`
- `docs/ARCHITECTURE.md`
