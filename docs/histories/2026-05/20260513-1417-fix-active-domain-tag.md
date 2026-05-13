## [2026-05-13 14:17] | Task: Fix active domain tag

### Execution Context

- Agent ID: `codex`
- Base Model: `GPT-5`
- Runtime: `Codex CLI`

### User Query

> Fix the bug where clicking a domain tag scrolls to the right section but the
> active tag remains on the previous domain.

### Changes Overview

- Area: GitHub Pages gallery
- Key actions:
  - Added one shared `getTocOffset()` helper for hash scrolling, CSS
    `scroll-margin-top`, and active tag detection.
  - Changed active domain detection to use the same offset plus a small
    tolerance so the selected tag matches the scrolled-to section.
  - Expanded gallery validation to catch drift between scroll and active tag
    offset logic.

### Design Intent

The visible section and selected domain tag should be driven by the same sticky
navigation geometry. Keeping those calculations in sync prevents off-by-one
active states after clicking a tag or refreshing a hash URL.

### Files Modified

- `index.html`
- `scripts/build-gallery.py`
- `scripts/validate-gallery.py`
