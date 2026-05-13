#!/usr/bin/env bash

set -euo pipefail

repo_root="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

"${repo_root}/scripts/check-docs.sh"
"${repo_root}/scripts/check-repo-hygiene.sh"
"${repo_root}/scripts/check-action-pinning.sh"
python3 "${repo_root}/skills/visual-html-gen-ui/scripts/validate_skill.py"

while IFS= read -r file; do
  bash -n "$file"
done < <(find "${repo_root}/scripts" -type f -name '*.sh' | sort)

echo "base CI checks passed"
