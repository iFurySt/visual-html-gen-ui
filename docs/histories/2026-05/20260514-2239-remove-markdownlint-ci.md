## [2026-05-14 22:39] | Task: Remove markdownlint from CI

### Execution Context

- Agent ID: `Codex`
- Base Model: `GPT-5`
- Runtime: `Codex CLI`

### User Query

> Remove markdownlint from CI because this repository does not need that check.

### Changes Overview

- Area: CI workflow
- Key actions: removed the GitHub Actions markdownlint step while leaving the repository base CI checks intact.

### Design Intent

Keep CI aligned with the repository's preferred checks and avoid blocking documentation edits on markdownlint formatting rules that are not part of the local validation workflow.

### Files Modified

- `.github/workflows/ci.yml`
