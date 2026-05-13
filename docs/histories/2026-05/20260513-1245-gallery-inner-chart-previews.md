## [2026-05-13 12:45] | Task: Gallery inner chart previews

### Execution Context

- Agent ID: `codex`
- Base Model: `GPT-5`
- Runtime: `Codex CLI`

### User Query

> The GitHub Pages gallery previews look too repetitive. Show the inner chart
> directly in the preview area instead of using repeated placeholder previews.

### Changes Overview

- Area: GitHub Pages gallery
- Key actions:
  - Added a stable `#chart-preview` anchor to each generated chart page.
  - Updated the gallery cards to lazy-load the corresponding chart page in an
    iframe preview.
  - Updated gallery validation to require one preview iframe per chart and a
    `#chart-preview` anchor in every chart target.
  - Regenerated all chart pages and the root gallery.

### Design Intent

The gallery should preview the actual inner chart artifact so cards no longer
look like repeated generic thumbnails. The iframe approach deliberately reuses
the inner chart HTML instead of duplicating chart rendering logic in the
gallery, so future richer chart examples can still be surfaced from the same
source page.

### Files Modified

- `index.html`
- `scripts/build-gallery.py`
- `scripts/validate-gallery.py`
- `skills/visual-html-gen-ui/scripts/build_charts.py`
- `skills/visual-html-gen-ui/<domain>/<chart>.html`
