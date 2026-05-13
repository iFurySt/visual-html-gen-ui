## [2026-05-13 12:55] | Task: Fix gallery back scroll

### Execution Context

- Agent ID: `codex`
- Base Model: `GPT-5`
- Runtime: `Codex CLI`

### User Query

> Fix the bug where returning to the GitHub Pages gallery makes the page keep
> scrolling downward.

### Changes Overview

- Area: GitHub Pages gallery
- Key actions:
  - Replaced navigated preview iframes with `srcdoc` previews extracted from
    each generated chart page.
  - Updated gallery validation to reject preview iframes that use a `src`
    attribute and require the expected `srcdoc` preview count.
  - Regenerated the root gallery.

### Design Intent

The gallery should preview the real inner chart without causing each card to
perform a fragment navigation such as `#chart-preview`. Using `srcdoc` keeps the
preview isolated and avoids polluting browser history or scroll restoration
when the user returns from a chart page.

### Files Modified

- `index.html`
- `scripts/build-gallery.py`
- `scripts/validate-gallery.py`
