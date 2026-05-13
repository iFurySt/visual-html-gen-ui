# visual-html-gen-ui

`visual-html-gen-ui` is a repository-local Codex skill for generating and
adapting standalone, domain-specific HTML chart examples.

## Intro

The skill lives at `skills/visual-html-gen-ui`. Its `SKILL.md` stays compact
and works as a table of contents. Agents should open only the domain/chart
example they need, then adapt that standalone HTML file into the target
project.

The public gallery is generated at the repository root as `index.html` for
GitHub Pages.

## Quick Start

Regenerate and validate the skill and gallery after editing the catalog:

```sh
python3 skills/visual-html-gen-ui/scripts/build_charts.py
python3 scripts/build-gallery.py
python3 skills/visual-html-gen-ui/scripts/validate_skill.py
python3 scripts/validate-gallery.py
```

Run repository checks:

```sh
make ci
```

## Gallery

- GitHub Pages: <https://ifuryst.com/visual-html-gen-ui/>
- Source: `index.html`
- Generator: `scripts/build-gallery.py`

## Current Catalog

- Finance: 30 chart examples.
- Office: 10 chart examples.
- Education: 10 chart examples.
- Health: 10 chart examples.
- Ecommerce: 10 chart examples.
- Social: 10 chart examples.
- Entertainment: 10 chart examples.
- Gaming: 10 chart examples.
- Content Creation: 10 chart examples.
- Enterprise Services: 10 chart examples.
- Cybersecurity: 10 chart examples.
- AI Agent: 10 chart examples.
- Real Estate: 10 chart examples.
- HR: 10 chart examples.
- Mobility: 10 chart examples.
- Travel: 10 chart examples.
- Biotech: 10 chart examples.
- Legal: 10 chart examples.
- Government: 10 chart examples.
- Manufacturing: 10 chart examples.
- Energy: 10 chart examples.
- Retail: 10 chart examples.
- Crypto: 10 chart examples.
- Fashion: 10 chart examples.
- Sports: 10 chart examples.
- Pets: 10 chart examples.

## License

[MIT](LICENSE)
