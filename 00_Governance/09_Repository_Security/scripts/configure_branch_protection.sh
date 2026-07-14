#!/usr/bin/env bash
set -euo pipefail

repo="hanax-ai/Project-ICE-HANA-X-Copilot"
branch="main"

if [[ "${CONFIRM_BRANCH_PROTECTION:-}" != "YES" ]]; then
  echo "Set CONFIRM_BRANCH_PROTECTION=YES after reviewing the protection policy."
  exit 2
fi

command -v gh >/dev/null 2>&1 || { echo "GitHub CLI (gh) is required."; exit 3; }
gh auth status >/dev/null

tmp="$(mktemp)"
trap 'rm -f "$tmp"' EXIT

cat > "$tmp" <<'EOF'
{
  "required_status_checks": {
    "strict": true,
    "contexts": [
      "Source integrity",
      "Register validation",
      "Artifact manifest validation",
      "Release integrity"
    ]
  },
  "enforce_admins": true,
  "required_pull_request_reviews": {
    "dismiss_stale_reviews": true,
    "require_code_owner_reviews": true,
    "required_approving_review_count": 1,
    "require_last_push_approval": true
  },
  "restrictions": null,
  "required_conversation_resolution": true,
  "allow_force_pushes": false,
  "allow_deletions": false,
  "block_creations": false,
  "required_linear_history": false,
  "lock_branch": false,
  "allow_fork_syncing": true
}
EOF

gh api --method PUT \
  -H "Accept: application/vnd.github+json" \
  -H "X-GitHub-Api-Version: 2026-03-10" \
  "repos/$repo/branches/$branch/protection" \
  --input "$tmp"

echo "Branch protection configured for $repo:$branch"
