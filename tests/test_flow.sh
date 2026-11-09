#!/usr/bin/env bash
# Regression test for the brain's save and sync flow.
# A local bare repo plays GitLab; two clones play two engineers. Nothing outside a temp folder is touched.
#
#   bash tests/test_flow.sh        # run after changing scripts/ or plugin/scripts/
#
# Needs git, bash and Python 3.9+ (python3, python or py). Works on Linux, macOS and Git Bash on Windows.
# Exits non-zero if any check fails.
set -u
PY=""
for p in python3 python py; do if "$p" -c '' </dev/null >/dev/null 2>&1; then PY="$p"; break; fi; done
[ -n "$PY" ] || { echo "no working Python found (python3, python, py)"; exit 1; }
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
T="$(mktemp -d)"
trap 'rm -rf "$T"' EXIT
HOOK="$ROOT/plugin/scripts/session_start.py"
NUDGE="$ROOT/plugin/scripts/stop_nudge.py"
export CLAUDE_PLUGIN_DATA="$T/nudge-state"
PASS=0
FAIL=0

check() {  # check "<description>" <command...>
  local name="$1"; shift
  if "$@" >/dev/null 2>&1; then PASS=$((PASS + 1)); echo "ok    $name"; else FAIL=$((FAIL + 1)); echo "FAIL  $name"; fi
}
contains() { grep -qF -- "$2" <<<"$1"; }
edit() { sed -i.bak "$1" "$2" && rm -f "$2.bak"; }
brief() {
  BRAIN_DIR="$1" BRAIN_TEAM="${2:-}" "$PY" -B "$HOOK" </dev/null |
    "$PY" -c 'import json,sys; print(json.load(sys.stdin)["hookSpecificOutput"]["additionalContext"])'
}
save() {  # save <clone> <args...>; output goes to $T/out, returns the exit code
  local clone="$1"; shift
  "$PY" -B "$clone/scripts/brain_save.py" "$@" >"$T/out" 2>&1
}
page() {  # page <file> <type> <title> <body line>
  mkdir -p "$(dirname "$1")"
  cat >"$1" <<EOF
---
title: $3
type: $2
tags: [test]
applies_to: []
confidence: observed
last_verified: 2026-01-01
owners: [test]
source: test
rule: $3 → do the test thing
---

# $3

$4
EOF
}
nudge() {  # nudge <session> <transcript> <stop_hook_active> [cwd]
  printf '{"session_id":"%s","transcript_path":"%s","cwd":"%s","stop_hook_active":%s}' \
    "$1" "$T/tx/$2" "${4:-$T}" "$3" | BRAIN_DIR="$A" "$PY" -B "$NUDGE"
}

echo "== setup: fake GitLab + two clones (alice, bob)"
git init -q --bare "$T/origin.git"
git -C "$T/origin.git" symbolic-ref HEAD refs/heads/main
mkdir "$T/seed"
(cd "$ROOT" && tar --exclude=.git --exclude=INDEX.md --exclude=__pycache__ --exclude=./docs/upstream -cf - .) | tar -xf - -C "$T/seed"
git -C "$T/seed" init -q && git -C "$T/seed" checkout -q -b main
git -C "$T/seed" add -A
git -C "$T/seed" -c user.name=seed -c user.email=seed@test commit -qm "bootstrap"
git -C "$T/seed" remote add origin "$T/origin.git"
git -C "$T/seed" push -q origin main
for who in alice bob; do
  git clone -q "$T/origin.git" "$T/$who"
  git -C "$T/$who" config user.name "$who"
  git -C "$T/$who" config user.email "$who@test"
done
A="$T/alice"; B="$T/bob"
origin_log() { git -C "$T/origin.git" log --pretty=%s main; }

echo "== checks"
check "all real pages pass validation" "$PY" -B "$ROOT/scripts/brain.py" validate

out="$(brief "$A" team1-mongodb-cassandra)"
check "session start: up to date and Quick Rules present" contains "$out" "up to date with GitLab"
check "session start: has a Quick rules section" contains "$out" "Quick rules"

page "$A/commons/knowledge/test-one.md" knowledge "Test one" "Body."
save "$A" -m "brain(test): one" commons/knowledge/test-one.md
check "save: new page pushed to main" contains "$(cat "$T/out")" "[brain-saved]"
check "save: commit is on GitLab" contains "$(origin_log)" "brain(test): one"

out="$(brief "$B")"
check "next session pulls the new commit" contains "$out" "pulled 1 new commit"
check "next session lists the new page as recent" contains "$out" "commons/knowledge/test-one.md"

page "$A/commons/knowledge/test-a.md" knowledge "Test A" "Body."
save "$A" -m "brain(test): a" commons/knowledge/test-a.md
page "$B/commons/knowledge/test-b.md" knowledge "Test B" "Body."
save "$B" -m "brain(test): b" commons/knowledge/test-b.md
check "two engineers saving at once: second save still succeeds" contains "$(cat "$T/out")" "[brain-saved]"
check "two engineers saving at once: alice's commit on GitLab" contains "$(origin_log)" "brain(test): a"
check "two engineers saving at once: bob's commit on GitLab" contains "$(origin_log)" "brain(test): b"

page "$A/commons/knowledge/test-shared.md" knowledge "Test shared" "- value: base"
save "$A" -m "brain(test): shared" commons/knowledge/test-shared.md
git -C "$B" pull -q --ff-only
edit 's/- value: base/- value: alice/' "$A/commons/knowledge/test-shared.md"
edit 's/- value: base/- value: bob/' "$B/commons/knowledge/test-shared.md"
save "$A" -m "brain(test): alice edit" commons/knowledge/test-shared.md
save "$B" -m "brain(test): bob edit" commons/knowledge/test-shared.md; code=$?
check "same line edited twice: exit code 2" test "$code" -eq 2
check "same line edited twice: clone left clean (no rebase in progress)" test ! -d "$B/.git/rebase-merge"
check "same line edited twice: bob's commit kept locally" test "$(git -C "$B" rev-list --count origin/main..HEAD)" -eq 1
check "next session warns about the unpushed commit" contains "$(brief "$B")" "not pushed yet"
git -C "$B" rebase -q origin/main >/dev/null 2>&1
"$PY" - "$B/commons/knowledge/test-shared.md" <<'EOF'
import re, sys
path = sys.argv[1]
text = open(path).read()
text = re.sub(r"<<<<<<< [^\n]*\n(.*?)=======\n(.*?)>>>>>>> [^\n]*\n", lambda m: m.group(1) + m.group(2), text, flags=re.S)
open(path, "w").write(text)
EOF
git -C "$B" add commons/knowledge/test-shared.md
GIT_EDITOR=true git -C "$B" rebase --continue >/dev/null 2>&1
save "$B" --push
check "after merging both versions, --push succeeds" contains "$(cat "$T/out")" "[brain-saved]"
check "GitLab has both people's lines" test "$(git -C "$T/origin.git" show main:commons/knowledge/test-shared.md | grep -cE 'value: (alice|bob)')" -eq 2

before="$(git -C "$B" rev-parse HEAD)"
page "$B/inbox/2026-01-01-leaky.md" inbox "Leaky" 'mongosh "mongodb://admin:S3cret@db:27017" and password: hunter2'
save "$B" -m "brain(test): leaky" inbox/2026-01-01-leaky.md; code=$?
check "secret: save refused (exit 1)" test "$code" -eq 1
check "secret: connection string flagged" contains "$(cat "$T/out")" "connection string with password"
check "secret: nothing committed" test "$before" = "$(git -C "$B" rev-parse HEAD)"
rm -f "$B/inbox/2026-01-01-leaky.md"

cp "$ROOT/templates/knowledge.md" "$B/commons/runbooks/bad.md"
out="$("$PY" -B "$B/scripts/brain.py" validate commons/runbooks/bad.md 2>&1)"
check "validate: template placeholder caught" contains "$out" "template placeholder"
check "validate: wrong type for the folder caught" contains "$out" "must be 'runbook'"
rm -f "$B/commons/runbooks/bad.md"

page "$A/commons/knowledge/test-later.md" knowledge "Test later" "Body."
save "$A" -m "brain(test): later" commons/knowledge/test-later.md
echo "local note" >>"$B/README.md"   # bob is now behind GitLab and has an unrelated local edit
page "$B/commons/knowledge/test-bob-later.md" knowledge "Test bob later" "Body."
save "$B" -m "brain(test): bob later" commons/knowledge/test-bob-later.md
check "unrelated local edit: save succeeds" contains "$(cat "$T/out")" "[brain-saved]"
check "unrelated local edit: still there, not committed" test "$(git -C "$B" status --porcelain README.md)" = " M README.md"
git -C "$B" checkout -q -- README.md

git -C "$B" checkout -q -b side
page "$B/commons/knowledge/test-side.md" knowledge "Test side" "Body."
save "$B" -m "brain(test): side" commons/knowledge/test-side.md; code=$?
check "refuses to save when the clone isn't on main" test "$code" -eq 1
rm -f "$B/commons/knowledge/test-side.md"; git -C "$B" checkout -q main; git -C "$B" branch -q -D side

page "$B/inbox/2026-01-01-maybe.md" inbox "Maybe" "Body."
save "$B" -m "brain(test): maybe" inbox/2026-01-01-maybe.md
mv "$B/inbox/2026-01-01-maybe.md" "$B/commons/knowledge/test-maybe.md"
edit 's/^type: inbox/type: knowledge/' "$B/commons/knowledge/test-maybe.md"
(cd "$T" && "$PY" -B "$B/scripts/brain_save.py" -m "brain(test): promote" inbox/2026-01-01-maybe.md commons/knowledge/test-maybe.md >"$T/out" 2>&1)
check "curate move (relative paths from another folder): pushed" contains "$(cat "$T/out")" "[brain-saved]"
check "curate move: inbox file gone on GitLab" test -z "$(git -C "$T/origin.git" ls-tree --name-only main inbox/2026-01-01-maybe.md)"

git -C "$A" pull -q --ff-only
git -C "$A" remote set-url origin "$T/nowhere.git"
check "offline: session start says GitLab unreachable" contains "$(brief "$A")" "couldn't reach GitLab"
page "$A/commons/knowledge/test-offline.md" knowledge "Test offline" "Body."
save "$A" -m "brain(test): offline" commons/knowledge/test-offline.md; code=$?
check "offline: save fails with exit 1" test "$code" -eq 1
check "offline: commit kept locally" test "$(git -C "$A" rev-list --count origin/main..HEAD)" -eq 1
git -C "$A" remote set-url origin "$T/origin.git"
save "$A" --push
check "back online: --push succeeds" contains "$(cat "$T/out")" "[brain-saved]"

check "missing brain folder: briefing says so" contains "$(brief "$T/nowhere")" "not found at"

mkdir -p "$T/tx"
"$PY" - "$T/tx" <<'EOF'
import json, sys, pathlib
d = pathlib.Path(sys.argv[1])
use = json.dumps({"type": "assistant", "message": {"content": [{"type": "tool_use", "name": "Bash"}]}})
(d / "long.jsonl").write_text("\n".join([use] * 25))
(d / "short.jsonl").write_text("\n".join([use] * 5))
(d / "saved.jsonl").write_text("\n".join([use] * 25 + [json.dumps({"result": "[brain-saved] pushed to main: abc"})]))
EOF
check "nudge: long session with no save asks once" contains "$(nudge s1 long.jsonl false)" '"decision": "block"'
check "nudge: never twice in one session" test -z "$(nudge s1 long.jsonl false)"
check "nudge: no loop when already continuing" test -z "$(nudge s2 long.jsonl true)"
check "nudge: quiet for short sessions" test -z "$(nudge s3 short.jsonl false)"
check "nudge: quiet after a save" test -z "$(nudge s4 saved.jsonl false)"
check "nudge: quiet when working inside the brain" test -z "$(nudge s5 long.jsonl false "$A")"
check "nudge: survives garbage input" test -z "$(echo 'not json' | "$PY" -B "$NUDGE")"

echo
echo "$PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ]
