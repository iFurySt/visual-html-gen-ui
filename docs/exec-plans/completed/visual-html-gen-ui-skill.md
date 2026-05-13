# Visual HTML Gen UI Skill

## Goal

Build `skills/visual-html-gen-ui` as a Codex skill containing a compact
`SKILL.md` table of contents and many standalone domain chart HTML examples.
Each chart should be discoverable by domain, readable independently, and
maintained manually one chart or domain at a time.

## Scope

- In scope:
  - Create the skill under `skills/visual-html-gen-ui`.
  - Use the visual language and standalone HTML approach from the local
    `html-effectiveness` examples.
  - Add domains one at a time and commit after each finished domain.
  - Keep `SKILL.md` as a navigation surface, not the full chart library.
  - Validate that chart files, `SKILL.md`, and the gallery stay synchronized.
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
  - Keep chart content under the skill directory.
  - Avoid loading every chart into `SKILL.md`.

## Risks

- Risk: A large chart library could make `SKILL.md` noisy.
  - Mitigation: `SKILL.md` lists only domain/chart links and short usage
    guidance.
- Risk: Chart examples, `SKILL.md`, and the gallery could drift.
  - Mitigation: Update the matching chart files, `SKILL.md`, and gallery cards
    in the same commit, then run CI and manual structure/browser checks.
- Risk: Similar layouts could make domains feel generic.
  - Mitigation: Use varied chart types, copy, data labels, and visual
    treatments per domain.

## Milestones

1. Create the skill scaffold and first domain.
2. Add each requested domain in a separate commit.
3. Run a final completion audit against all requested domains.

## Validation

- Commands:
  - `make ci`
- Manual checks:
  - Confirm every requested domain appears in `SKILL.md`.
  - Confirm each chart link points to a standalone HTML file.
  - Confirm the history entry records the finished change.

## Progress Log

- [x] Confirm repository conventions and required docs.
- [x] Implement the first domain slice: finance.
- [x] Commit the first domain slice.
- [x] Add remaining requested domains one domain per commit.
- [x] Run final validation and completion audit.

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
- [x] Biotech
- [x] Legal
- [x] Government
- [x] Manufacturing
- [x] Energy
- [x] Retail
- [x] Crypto
- [x] Fashion
- [x] Sports
- [x] Pets

## Decision Log

- 2026-05-13: Use standalone HTML under
  `skills/visual-html-gen-ui/<domain>/<chart>.html` so the chart tree
  matches the requested skill shape while keeping each chart reviewable on its
  own.
- 2026-05-13: Treat `~/projects/github/html-effectiveness` as the strict visual
  baseline: ivory paper background, restrained serif headings, mono metadata,
  1.5px rules, low-saturation clay/olive/oat/slate palette, and dependency-free
  static HTML/SVG examples.

## Completion Audit

- 2026-05-13: `skills/visual-html-gen-ui/SKILL.md` lists every domain
  and chart link as a compact table of contents.
- 2026-05-13: Every chart listed in `SKILL.md` has a standalone
  `<domain>/<chart>.html` file.
- 2026-05-13: Git history contains one commit for each requested domain slice.
- 2026-05-13: Catalog-driven generation was later removed; maintenance is now
  manual by chart/domain, with `make ci`, parser checks, and browser checks as
  validation.
