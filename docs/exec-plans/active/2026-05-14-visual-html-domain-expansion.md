# Visual HTML Domain Expansion

## Goal

Expand the visual HTML skill and gallery by reviewing each domain from a practical domain-expert perspective, then adding only common, high-value chart examples that are missing. Finance already has broader coverage; the other domains are not constrained to exactly ten examples.

## Scope

- In scope:
  - Hand-authored chart HTML files under `skills/visual-html-gen-ui/<domain>/`.
  - Manual updates to `skills/visual-html-gen-ui/SKILL.md`.
  - Manual updates to `index.html` gallery cards and domain counts.
  - Validation scripts or one-off checks that inspect the maintained files.
  - History entries for completed slices.
- Out of scope:
  - Reintroducing `catalog.json` or generator scripts.
  - Bulk-generating gallery or skill content from a catalog.
  - Adding external charting dependencies.

## Context

- Relevant docs:
  - `docs/REPO_COLLAB_GUIDE.md`
  - `docs/ARCHITECTURE.md`
  - `docs/design-docs/core-beliefs.md`
  - `docs/HISTORY_GUIDE.md`
  - `docs/QUALITY_SCORE.md`
- Relevant code paths:
  - `skills/visual-html-gen-ui/SKILL.md`
  - `skills/visual-html-gen-ui/*/*.html`
  - `index.html`
  - `docs/histories/2026-05/`
- Constraints:
  - Each chart remains a standalone HTML document with inline CSS and SVG.
  - Gallery and skill catalog are maintained manually.
  - Additions should be small, reviewable domain slices with validation before commit.

## Coverage Audit

Current baseline: Finance has 30 examples. All other domains currently have 10 examples.

Likely high-value gaps to consider by domain:

- Office: decision latency control, dependency risk matrix, work intake aging, stakeholder alignment.
- Education: chronic absenteeism, intervention response, enrollment funnel, resource equity.
- Health: wait-time throughput, staffing acuity, claims denial, care-gap closure.
- Ecommerce: replenishment forecast, LTV cohort, fulfillment SLA, returns reason analysis.
- Social: creator retention, moderation aging, community graph, ad yield.
- Entertainment: rights windowing, churn cohort, content ROI, ad fill waterfall.
- Gaming: economy inflation, matchmaking quality, churn return, crash/performance heatmap.
- Content Creation: revenue stack, subscriber cohort, content ROI scatter, sponsorship pipeline.
- Enterprise Services: SLA breach heatmap, renewal forecast, implementation milestones, backlog aging.
- Cybersecurity: incident timeline, vulnerability aging, attack path graph, control coverage.
- AI Agent: eval pass/fail matrix, tool trace, latency/cost distribution, fallback taxonomy.
- Real Estate: lease expiry ladder, rent roll waterfall, capex schedule, debt maturity.
- HR: compensation equity, attrition risk, hiring funnel capacity, workforce scenario.
- Mobility: fleet availability, charger utilization, safety incident heatmap, supply/demand imbalance.
- Travel: booking lead time, occupancy/revPAR, disruption recovery, route profitability.
- Biotech: trial enrollment forecast, adverse events, biomarker response, milestone runway.
- Legal: document review progress, outside counsel spend, litigation timeline, clause deviation.
- Government: service backlog aging, budget variance, resident satisfaction, grant pipeline.
- Manufacturing: process control, supplier OTIF, bottleneck capacity, shortage risk.
- Energy: load forecast error, battery dispatch, PPA revenue, outage restoration.
- Retail: inventory aging, labor productivity, price elasticity, loyalty LTV.
- Crypto: token unlock, bridge exposure, validator concentration, stablecoin peg monitor.
- Fashion: size availability, fit returns, trend lifecycle, supplier lead time.
- Sports: lineup combinations, ticket revenue, opponent scouting, tactical formation.
- Pets: lifetime care cost, appointment capacity, adoption geography, claims by condition.

## Risks

- Risk: Gallery, skill links, and file counts drift apart.
  - Mitigation: Run link/count checks after each slice.
- Risk: New examples look generic instead of domain-specific.
  - Mitigation: Each chart must name realistic domain signals, use cases, and labels.
- Risk: Direct manual edits introduce malformed HTML.
  - Mitigation: Parse touched files plus `index.html` after each slice and run `make ci`.

## Milestones

1. Document coverage strategy and validate current baseline.
2. Add small domain slices with chart files, skill links, gallery cards, and history entries.
3. Commit each validated slice.
4. Run full final audit across all domains.
5. Push the completed branch.

## Validation

- Commands:
  - `make ci`
  - HTML parser checks for `index.html` and all chart files.
  - Link and count checks comparing file system, `SKILL.md`, and gallery cards.
  - `git diff --check`
- Manual checks:
  - Browser smoke check for touched gallery sections and at least one standalone chart page per slice.
  - Confirm no `catalog.json` or generator script workflow is reintroduced.
- Observability checks:
  - Not applicable; this is a static skill/gallery content change.

## Progress Log

- [x] Confirmed current baseline: Finance 30, all other domains 10.
- [x] Removed catalog-driven generation workflow in the earlier cleanup.
- [x] Implement and validate the Office expansion slice.
- [x] Continue domain slices by priority.
- [x] Run full final validation.
- [x] Push completed branch.

## Validation Results

- 2026-05-14: `make ci` passed.
- 2026-05-14: Parsed `index.html` and all 308 chart pages successfully.
- 2026-05-14: Verified every chart page includes `id="chart-preview"`.
- 2026-05-14: Verified file counts match `SKILL.md` links and gallery cards for every domain.
- 2026-05-14: Verified no non-finance domain remains at exactly 10 chart examples.
- 2026-05-14: Verified no `catalog.json`, `build_charts.py`, `build-gallery.py`, `validate_skill.py`, or `validate-gallery.py` files exist.
- 2026-05-14: Browser audit confirmed gallery section card counts match labels and final added cards are present; standalone `pets/appointment-capacity-calendar.html` rendered a non-empty SVG.
- 2026-05-14: Pushed `main` to `origin`.

## Decision Log

- 2026-05-14: Add examples based on common domain workflows instead of fixed per-domain counts, because the skill should reflect useful coverage rather than catalog symmetry.
- 2026-05-14: Keep gallery and skill updates manual, because the user explicitly rejected catalog-generated maintenance.
