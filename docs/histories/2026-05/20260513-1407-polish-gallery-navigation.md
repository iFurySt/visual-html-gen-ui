## [2026-05-13 14:07] | Task: Polish gallery navigation

### Execution Context

- Agent ID: `codex`
- Base Model: `GPT-5`
- Runtime: `Codex CLI`

### User Query

> Restore the elegant hash scroll behavior for domain tags, make refresh with a
> domain hash scroll to that section, improve the sticky tag bar styling, and
> smooth out the fold toggle icon so it matches the html-effectiveness style.

### Changes Overview

- Area: GitHub Pages gallery
- Key actions:
  - Added hash-aware domain scrolling that opens the target domain, updates the
    URL hash, and re-aligns on refresh.
  - Restyled the sticky domain tag bar as a full framed surface with balanced
    side padding, rounded corners, and a softer sticky shadow.
  - Replaced the text `+` / `-` fold indicator with CSS line icons to avoid
    rough font rendering and heavy black outlines.
  - Expanded gallery validation to cover the navigation and visual structure.

### Design Intent

The domain tags should feel like the original html-effectiveness TOC pills while
still behaving as persistent page navigation. The fold control should read as a
small interface affordance rather than a separate heavy button.

### Files Modified

- `index.html`
- `scripts/build-gallery.py`
- `scripts/validate-gallery.py`
