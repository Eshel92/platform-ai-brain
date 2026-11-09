#!/usr/bin/env bash
# Run a brain script with whichever Python works here: python3 (Linux, macOS), python or py (Windows).
# Skips the Windows Store "python3" stub, which exists but doesn't run.
#
#   bash scripts/run.sh brain_save.py -m "brain(team1): ..." <files>
#   bash scripts/run.sh brain.py validate
here="$(cd "$(dirname "$0")" && pwd)"
script="$1"; shift
for p in python3 python py; do
  if "$p" -c '' </dev/null >/dev/null 2>&1; then
    exec "$p" "$here/$script" "$@"
  fi
done
echo "run.sh: no working Python found (tried python3, python, py)" >&2
exit 1
