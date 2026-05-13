# Architecture

This repository packages a Codex skill for standalone visual HTML chart
examples. The skill is source-controlled inside the repo instead of installed
globally so agents can review, extend, validate, and commit it in small slices.

## Repository Shape

- `skills/visual-html-gen-ui/`: the skill consumed by agents.
- `skills/visual-html-gen-ui/SKILL.md`: compact table of contents and usage
  entry point.
- `skills/visual-html-gen-ui/<domain>/<chart>.html`: hand-maintained,
  standalone chart examples.
- `index.html`: hand-maintained GitHub Pages gallery, grouped by domain.
- `docs/`: collaboration guides, execution plans, histories, and quality notes.

## Boundary Rules

- Keep `SKILL.md` as the hand-maintained navigation index; detailed examples
  belong in individual chart HTML files.
- Add and revise chart HTML files one at a time, then update `SKILL.md` and
  `index.html` with the matching domain section and link.
- Chart examples should remain dependency-free HTML/CSS/SVG and follow the
  visual baseline from `~/projects/github/html-effectiveness`.
- Review belongs at the artifact level: inspect the touched chart HTML, the
  skill index entry, and the gallery card together before committing.

## Data Flow

1. Maintainer creates or edits one chart HTML file under
   `skills/visual-html-gen-ui/<domain>/`.
2. Maintainer updates `skills/visual-html-gen-ui/SKILL.md` by hand with the
   domain summary and chart link.
3. Maintainer updates `index.html` by hand so the public gallery matches the
   same chart set.
4. Maintainer reviews the changed domain in the browser or by inspecting the
   standalone HTML and gallery snippet.
5. `make ci` runs repository-level checks for docs, hygiene, action pinning,
   and shell syntax.
