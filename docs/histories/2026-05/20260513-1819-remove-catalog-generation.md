## [2026-05-13 18:19] | Task: Remove skill and gallery automation

### Execution Context

- Agent ID: `Codex`
- Base Model: `GPT-5`
- Runtime: `Codex CLI`

### User Query

> Remove the catalog-based generation flow and skill/gallery scripts; chart
> examples and gallery cards should be handled one at a time.

### Changes Overview

- Area: Skill maintenance, gallery maintenance, CI, documentation.
- Key actions:
  - Deleted the catalog file, chart batch generator, skill validator, gallery
    generator, and gallery validator.
  - Made `SKILL.md` and `index.html` hand-maintained artifacts.
  - Removed skill/gallery script targets from `Makefile` and CI.
  - Updated repository docs to describe one-chart-at-a-time manual maintenance.

### Design Intent

The skill should preserve each chart page and gallery card as individually
reviewed artifacts. Automation should not create the appearance that broad,
template-like domain coverage is complete before each domain has been designed
and inspected on its own merits.

### Files Modified

- `README.md`
- `docs/ARCHITECTURE.md`
- `docs/QUALITY_SCORE.md`
- `index.html`
- `Makefile`
- `scripts/ci.sh`
- `scripts/build-gallery.py`
- `scripts/skill_index.py`
- `scripts/validate-gallery.py`
- `skills/visual-html-gen-ui/SKILL.md`
- `skills/visual-html-gen-ui/catalog.json`
- `skills/visual-html-gen-ui/scripts/build_charts.py`
- `skills/visual-html-gen-ui/scripts/validate_skill.py`
