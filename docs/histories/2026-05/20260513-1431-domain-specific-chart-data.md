## [2026-05-13 14:31] | Task: Domain-specific chart examples

### Execution Context

- Agent ID: `codex`
- Base Model: `GPT-5`
- Runtime: `local CLI`

### User Query

> Reduce repeated chart examples and make each domain's sample data fit that domain, even when chart types repeat.

### Changes Overview

- Area: `skills/visual-html-gen-ui`
- Key actions:
  - Added domain profiles and deterministic per-domain chart sample data in the chart generator.
  - Updated generated chart titles, metadata, labels, legends, and values so repeated chart types use domain-specific examples.
  - Renamed duplicate catalog titles that made generated pages feel interchangeable.
  - Expanded validation to reject duplicate chart titles, duplicate generated sample titles, and generic placeholder metadata.
  - Regenerated the skill documentation, all chart HTML pages, and the root gallery preview.

### Design Intent

The generated skill should feel usable as a reference library, not a toy catalog. The generator now keeps repeated visual patterns while varying the business vocabulary, dimensions, and sample values by domain. Validation protects that standard so future catalog additions do not drift back into generic examples.

### Files Modified

- `skills/visual-html-gen-ui/scripts/build_charts.py`
- `skills/visual-html-gen-ui/scripts/validate_skill.py`
- `skills/visual-html-gen-ui/catalog.json`
- `skills/visual-html-gen-ui/SKILL.md`
- `skills/visual-html-gen-ui/*/*.html`
- `index.html`
