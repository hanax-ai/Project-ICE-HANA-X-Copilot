#!/usr/bin/env bash
set -euo pipefail

if [[ $# -ne 2 ]]; then
  echo "Usage: $0 <canonical-repository-path> <public-mirror-output-path>"
  exit 2
fi

src="$(cd "$1" && pwd)"
dst="$2"

if [[ -e "$dst" ]]; then
  echo "Output path already exists: $dst"
  exit 3
fi

mkdir -p "$dst"

for file in README.md PUBLICATION_GUIDE.md SECURITY.md CONTRIBUTING.md; do
  if [[ -f "$src/$file" ]]; then
    cp "$src/$file" "$dst/$file"
  fi
done

for directory in 11_Deliverables 12_Releases; do
  if [[ -d "$src/$directory" ]]; then
    mkdir -p "$dst/$directory"
    rsync -a "$src/$directory/" "$dst/$directory/"
  fi
done

approved_src="$src/04_White_Paper/00_Front_Matter/ICE-FM-001_Letter-from-the-Founder/04_Approved"
approved_dst="$dst/04_White_Paper/00_Front_Matter/ICE-FM-001_Letter-from-the-Founder/04_Approved"
if [[ -d "$approved_src" ]]; then
  mkdir -p "$approved_dst"
  rsync -a "$approved_src/" "$approved_dst/"
fi

cat > "$dst/PUBLIC_MIRROR_NOTICE.md" <<'EOF'
# Project ICE Public Mirror

This is a sanitized distribution mirror. It is not the canonical Project ICE evidence repository. Restricted source evidence, knowledge-base content, registers, private review records, requirements, and working files are intentionally excluded.
EOF

find "$dst" -type f -path '*/Originals/*' -print > "$dst/PUBLIC_MIRROR_ORIGINALS_REVIEW.txt"
if [[ -s "$dst/PUBLIC_MIRROR_ORIGINALS_REVIEW.txt" ]]; then
  echo "Unexpected Originals files were found in the mirror. Review before publication."
  exit 4
fi

echo "Sanitized working tree created at: $dst"
echo "Review the complete output before initializing or pushing a public repository."
