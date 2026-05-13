# visual-html-gen-ui

`visual-html-gen-ui` is a repository-local Codex skill for generating and
adapting standalone, domain-specific HTML chart examples.

## Intro

The skill lives at `skills/visual-html-gen-ui`. Its `SKILL.md` stays compact
and works as a table of contents. Agents should open only the domain/chart
example they need, then adapt that standalone HTML file into the target
project.

## Quick Start

Regenerate and validate the skill after editing the catalog:

```sh
python3 skills/visual-html-gen-ui/scripts/build_charts.py
python3 skills/visual-html-gen-ui/scripts/validate_skill.py
```

Run repository checks:

```sh
make ci
```

## Current Catalog

- Finance: 30 chart examples.
- Office: 10 chart examples.

## License

[MIT](LICENSE)
