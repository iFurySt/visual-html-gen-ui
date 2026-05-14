## [2026-05-14 00:08] | Task: Final non-finance domain chart expansion

### Execution Context

- Agent ID: `Codex`
- Base Model: `GPT-5`
- Runtime: `Codex CLI`

### User Query

> Add missing common charts by field, one at a time, instead of stopping at ten
> non-finance examples.

### Changes Overview

- Area: energy, retail, crypto, fashion, sports, and pets chart examples.
- Key actions:
  - Added hand-authored examples for battery dispatch, inventory aging, token
    unlocks, size availability, lineup net rating, and appointment capacity.
  - Updated the relevant `SKILL.md` domain sections.
  - Updated gallery counts and cards manually.

### Design Intent

This final batch moves the remaining non-finance domains beyond fixed ten-chart
coverage with common expert workflows that were not represented in their
existing examples.

### Files Modified

- `index.html`
- `skills/visual-html-gen-ui/SKILL.md`
- `skills/visual-html-gen-ui/energy/battery-dispatch-profile.html`
- `skills/visual-html-gen-ui/retail/inventory-aging-buckets.html`
- `skills/visual-html-gen-ui/crypto/token-unlock-schedule.html`
- `skills/visual-html-gen-ui/fashion/size-availability-curve.html`
- `skills/visual-html-gen-ui/sports/lineup-net-rating-matrix.html`
- `skills/visual-html-gen-ui/pets/appointment-capacity-calendar.html`
