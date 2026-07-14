#!/usr/bin/env bash
set -euo pipefail

repo="hanax-ai/Project-ICE-HANA-X-Copilot"

if [[ "${CONFIRM_VISIBILITY_CHANGE:-}" != "YES" ]]; then
  echo "Refusing to change repository visibility."
  echo "Set CONFIRM_VISIBILITY_CHANGE=YES after reviewing the remediation guide."
  exit 2
fi

command -v gh >/dev/null 2>&1 || { echo "GitHub CLI (gh) is required."; exit 3; }
gh auth status >/dev/null

current="$(gh repo view "$repo" --json visibility --jq .visibility)"
if [[ "$current" == "PRIVATE" ]]; then
  echo "$repo is already private."
  exit 0
fi

gh repo edit "$repo" --visibility private --accept-visibility-change-consequences
new_visibility="$(gh repo view "$repo" --json visibility --jq .visibility)"

if [[ "$new_visibility" != "PRIVATE" ]]; then
  echo "Visibility verification failed: $new_visibility"
  exit 4
fi

echo "$repo is now private."
