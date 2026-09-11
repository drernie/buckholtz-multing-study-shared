#!/usr/bin/env bash
# Regenerate the reviewer copy of this repository from scratch.
#
# WHY THIS EXISTS
#   Two repositories, one source of truth:
#     - this one  (buckholtz-idm-multing-mvp -> sergeeey/buckholtz-idm-multing-study)
#       is where ALL work happens. Its history contains private correspondence
#       and is never shared.
#     - the copy   (../buckholtz-multing-shared -> sergeeey/buckholtz-multing-study-shared)
#       is PURELY DERIVED. Never edit it by hand. Run this script instead.
#   If you ever find yourself editing a file in the copy, that is the bug.
#
# WHAT IT REMOVES (from EVERY commit, not just the tip)
#   correspondence/     private letters, both directions
#   .claude/            internal session state, incl. nested experiments/*/.claude/
#   three third-party email addresses
#
# WHAT IT KEEPS
#   Everything else, with all commit dates and messages intact -- the dated,
#   incremental trail is itself evidence that conclusions were not retrofitted.
#
# USAGE   bash scripts/refresh_shared_repo.sh          # rebuild, do not push
#         bash scripts/refresh_shared_repo.sh --push   # rebuild and force-push
#
set -euo pipefail

ORIG_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
COPY_DIR="$(dirname "$ORIG_DIR")/buckholtz-multing-shared"
REMOTE="https://github.com/sergeeey/buckholtz-multing-study-shared.git"
RULES="$(mktemp)"

cat > "$RULES" <<'EOF'
[private email redacted]==>[private email redacted]
[third-party email redacted]==>[third-party email redacted]
[third-party email redacted]==>[third-party email redacted]
EOF

if [ -e "$COPY_DIR" ]; then
  echo "ERROR: $COPY_DIR already exists."
  echo "Remove it yourself first -- this script will not delete directories."
  exit 1
fi

echo "==> cloning (tracked files only; data/source_material is git-ignored by design)"
git clone --no-local -q "$ORIG_DIR" "$COPY_DIR"
cd "$COPY_DIR"

echo "==> stripping correspondence/ and .claude/ from all history"
python -m git_filter_repo --invert-paths --path correspondence/ --path .claude/ --replace-text "$RULES"
# Second pass: --path-regex anchors at the start of the path, so nested
# experiments/*/.claude/ survives the first pass. Found the hard way, 2026-09-11.
python -m git_filter_repo --invert-paths --path-regex '.*\.claude/' --force

echo "==> applying the two copy-only README deltas"
# 1. the CI badge points at the private original -- a 404 for any reviewer
sed -i '/actions\/workflows\/ci.yml\/badge.svg/d' README.md
# 2. the clone directory name differs
sed -i 's/^cd buckholtz-idm-multing-mvp$/cd buckholtz-multing-study-shared/' README.md
git add README.md
git commit -q -m "chore: reviewer-copy README deltas (badge, clone dir) -- generated, do not hand-edit"

echo "==> verifying"
for p in "correspondence/" ".claude/"; do
  n=$(git rev-list --objects --all | grep -c "$p" || true)
  [ "$n" -eq 0 ] && echo "    OK: no '$p' anywhere in history" || { echo "    FAIL: $n objects still match '$p'"; exit 1; }
done
for e in [private email redacted] [third-party email redacted] [third-party email redacted]; do
  n=$(git log --all -S"$e" --oneline | wc -l)
  [ "$n" -eq 0 ] && echo "    OK: '$e' absent from history" || { echo "    FAIL: '$e' still in $n commits"; exit 1; }
done
echo "    commits preserved: $(git rev-list --count HEAD)"

if [ "${1:-}" = "--push" ]; then
  echo "==> force-pushing to $REMOTE (history is rewritten every run, so this must be forced)"
  git branch -M main
  git remote add origin "$REMOTE"
  git push --force -u origin main
else
  echo "==> NOT pushed. Re-run with --push when you have checked the result."
fi

rm -f "$RULES"
