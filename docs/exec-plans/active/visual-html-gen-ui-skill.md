# Visual HTML Gen UI Skill

## Goal

Build `skills/visual-html-gen-ui` as a Codex skill containing a compact
`SKILL.md` table of contents and many standalone domain chart HTML examples.
Each chart should be discoverable by domain, readable independently, and
generated from a repository-local catalog so future agents can extend it
without loading every example into context.

## Scope

- In scope:
  - Create the skill under `skills/visual-html-gen-ui`.
  - Use the visual language and standalone HTML approach from the local
    `html-effectiveness` examples.
  - Add domains one at a time and commit after each finished domain.
  - Keep `SKILL.md` as a navigation surface, not the full chart library.
  - Add validation that confirms catalog entries, generated files, and
    `SKILL.md` links stay synchronized.
- Out of scope:
  - Publishing the skill to a global Codex skill directory.
  - Adding external charting dependencies.
  - Building an application runtime or hosted gallery.

## Context

- Relevant docs:
  - `docs/REPO_COLLAB_GUIDE.md`
  - `docs/ARCHITECTURE.md`
  - `docs/design-docs/core-beliefs.md`
  - `docs/HISTORY_GUIDE.md`
  - `docs/QUALITY_SCORE.md`
- Relevant code paths:
  - `skills/visual-html-gen-ui/`
  - `docs/histories/`
- Constraints:
  - Chart files should be self-contained HTML.
  - Keep generated chart content under the skill directory.
  - Avoid loading every chart into `SKILL.md`.

## Risks

- Risk: A large catalog could make `SKILL.md` noisy.
  - Mitigation: `SKILL.md` lists only domain/chart links and short usage
    guidance.
- Risk: Generated examples could drift from the catalog.
  - Mitigation: Add a validator and run it before each domain commit.
- Risk: Similar layouts could make domains feel generic.
  - Mitigation: Use varied chart types, copy, data labels, and visual
    treatments per domain.

## Milestones

1. Create the skill scaffold, generator, validator, and first domain.
2. Add each requested domain in a separate commit.
3. Run a final completion audit against all requested domains.

## Validation

- Commands:
  - `python3 skills/visual-html-gen-ui/scripts/build_charts.py`
  - `python3 skills/visual-html-gen-ui/scripts/validate_skill.py`
  - `make ci`
- Manual checks:
  - Confirm every requested domain appears in `SKILL.md`.
  - Confirm each chart link points to a generated standalone HTML file.
  - Confirm the history entry records the finished change.

## Progress Log

- [x] Confirm repository conventions and required docs.
- [x] Implement the first domain slice: finance.
- [ ] Commit the first domain slice.
- [ ] Add remaining requested domains one domain per commit.
- [ ] Run final validation and completion audit.

## Domain Completion Log

- [x] Finance
- [x] Office
- [x] Education
- [x] Health
- [x] Ecommerce
- [x] Social
- [x] Entertainment
- [x] Gaming
- [x] Content Creation
- [x] Enterprise Services
- [x] Cybersecurity
- [x] AI Agent
- [x] Real Estate
- [x] HR
- [x] Mobility
- [x] Travel
- [ ] Biotech
- [ ] Legal
- [ ] Government
- [ ] Manufacturing
- [ ] Energy
- [ ] Retail
- [ ] Crypto
- [ ] Fashion
- [ ] Sports
- [ ] Pets

## Decision Log

- 2026-05-13: Use generated standalone HTML under
  `skills/visual-html-gen-ui/<domain>/<chart>/index.html` so the chart tree
  matches the requested skill shape while keeping maintenance centralized in a
  catalog.
- 2026-05-13: Treat `~/projects/github/html-effectiveness` as the strict visual
  baseline: ivory paper background, restrained serif headings, mono metadata,
  1.5px rules, low-saturation clay/olive/oat/slate palette, and dependency-free
  static HTML/SVG examples.
