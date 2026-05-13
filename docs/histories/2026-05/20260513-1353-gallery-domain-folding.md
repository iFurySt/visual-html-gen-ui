## [2026-05-13 13:53] | Task: Gallery domain folding

### Execution Context

- Agent ID: `codex`
- Base Model: `GPT-5`
- Runtime: `Codex CLI`

### User Query

> Make each domain collapsible because there are too many charts per domain.
> Keep the domain tag links sticky after scrolling, keep "Visual HTML Gen UI"
> on one line, and remove the unclear runtime deps summary item.

### Changes Overview

- Area: GitHub Pages gallery
- Key actions:
  - Converted each domain group into a default-open collapsible `details`
    section.
  - Moved domain tags into a full-page sticky navigation bar with compact
    sticky styling, active state, and click-to-scroll behavior.
  - Kept the gallery title on one line with responsive fixed breakpoints.
  - Removed the `runtime deps` summary stat from the hero summary.
  - Expanded gallery validation to check the new generated structure.

### Design Intent

The gallery should still open as a browsable full catalog, but users can fold
large domain groups when scanning. The domain tag row becomes the persistent
navigation control once the hero scrolls away, while the hero summary stays
focused on useful catalog scale metrics.

### Files Modified

- `index.html`
- `scripts/build-gallery.py`
- `scripts/validate-gallery.py`
