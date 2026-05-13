## [2026-05-13 11:20] | Task: Flatten chart HTML paths

### Execution Context

- Agent ID: `codex`
- Base Model: `GPT-5`
- Runtime: `Codex CLI`

### User Query

> Change chart files from
> `skills/visual-html-gen-ui/<domain>/<chart>/index.html` to
> `skills/visual-html-gen-ui/<domain>/<chart>.html`.

### Changes Overview

- Area: `skills/visual-html-gen-ui`
- Key actions:
  - Updated the chart generator to emit flat per-domain HTML files.
  - Updated the validator and `SKILL.md` links to use `<chart>.html`.
  - Regenerated all 280 chart examples into the new path structure.
  - Updated architecture, quality, completed plan, and prior history references.

### Design Intent

The flattened path keeps each chart as an independent HTML artifact while
removing one unnecessary directory level. The generator now removes stale chart
directories during rebuilds so old `index.html` paths cannot coexist with the
new structure.

### Files Modified

- `skills/visual-html-gen-ui/scripts/build_charts.py`
- `skills/visual-html-gen-ui/scripts/validate_skill.py`
- `skills/visual-html-gen-ui/SKILL.md`
- `skills/visual-html-gen-ui/<domain>/<chart>.html`
- `docs/ARCHITECTURE.md`
- `docs/QUALITY_SCORE.md`
- `docs/exec-plans/completed/visual-html-gen-ui-skill.md`
- `docs/histories/2026-05/20260513-1107-visual-html-finance-skill.md`
