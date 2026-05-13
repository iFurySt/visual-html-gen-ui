# Quality Score

Track quality by product area and architectural layer so agents can prioritize the weakest parts of the system.

## Suggested Scale

- `A`: strong coverage, stable behavior, clear docs, low operational risk.
- `B`: acceptable but still has known gaps.
- `C`: works but needs targeted hardening.
- `D`: fragile or underspecified.

## Initial Template

| Area | Score | Why | Next Step |
| --- | --- | --- | --- |
| Product surface | B | Skill surface covers all requested domains with 280 standalone chart examples. | Add targeted visual smoke checks for representative chart families. |
| Architecture docs | B | Architecture documents the hand-maintained skill index, gallery, and flat chart HTML outputs. | Keep this updated as the skill structure evolves. |
| Testing | C | Repository checks cover docs, hygiene, action pinning, and shell syntax; chart/gallery review is manual. | Add targeted checks only if they support the manual review workflow instead of replacing it. |
| Observability | D | No local stack or conventions yet. | Document logs, metrics, traces, and local access. |
| Security | C | Defaults are documented, implementation is pending. | Add real auth, secret, and dependency rules. |
