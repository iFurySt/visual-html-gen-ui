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
| Product surface | C | Initial skill surface exists with a finance catalog and standalone chart examples. | Add the remaining requested domains one domain per commit. |
| Architecture docs | B | Architecture now documents the skill catalog, generated outputs, and validation flow. | Keep this updated as the skill structure evolves. |
| Testing | C | Skill validation checks catalog/link/output drift and is wired into CI. | Add visual smoke checks if generated HTML becomes more interactive. |
| Observability | D | No local stack or conventions yet. | Document logs, metrics, traces, and local access. |
| Security | C | Defaults are documented, implementation is pending. | Add real auth, secret, and dependency rules. |
