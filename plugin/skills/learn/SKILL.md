---
name: learn
description: Save something durable to the platform brain — a root cause, a wrong assumption corrected, a version-specific quirk, a procedure that worked, a decision and its reason, or a fix to a wrong brain page. Use after solving or discovering something a teammate would otherwise rediscover. Shows the engineer the page first and pushes straight to main only after they say yes.
---

# Save a learning to the brain

```bash
BRAIN="${BRAIN_DIR:-$HOME/platform-ai-brain}"
```

## 0. Is it worth saving?

Save it if a teammate in the same situation in 3 months would save real time.
**Yes:** root causes, workarounds, "X only happens on version Y", commands that finally worked,
wrong assumptions corrected, decisions with their reasons, a brain page that was wrong.
**No:** generic facts from public docs, routine work with no surprises, anything you can't scope.
If it isn't worth saving, say so in one line and stop.

## 1. Search first: updating beats creating

```bash
grep -rilE '<key terms>|<exact error>' "$BRAIN" --include='*.md' --exclude-dir=upstream
```

If a page already covers it, **edit that page**: add the new case, adjust `applies_to` or
`confidence`, set `last_verified` to today and add a line under `## History`.

## 2. Pick the place

| What you learned | Where | Start from |
|---|---|---|
| A problem: symptom, cause, fix, wrong assumption | `<team>/knowledge/<topic>.md` | `$BRAIN/templates/knowledge.md` |
| How a system is built here | `<team>/knowledge/<component>.md` | `$BRAIN/templates/overview.md` |
| A step-by-step procedure | `<team>/runbooks/<task>.md` | `$BRAIN/templates/runbook.md` |
| A decision and why | `<team>/decisions/<topic>.md` | `$BRAIN/templates/decision.md` |
| Unsure, partial, or needs a person to judge | `inbox/<yyyy-mm-dd>-<topic>.md` with `type: inbox` | `$BRAIN/templates/knowledge.md` |

`<team>`: `commons` (OpenShift, Argo CD, Helm, GitLab, storage, monitoring, Python),
`team1-mongodb-cassandra`, `team2-elastic`, `team3-redis`. File names: lowercase-with-dashes,
named after the symptom or topic.

## 3. Write it

- Copy the template and fill every header field. `last_verified` is today; `source: claude-session`.
- **`confidence` is honest:** `verified` only if the engineer confirmed it or it was tested working in
  this session. Seen once = `observed`. Believed but unproven = `hypothesis`.
- **`rule:`** one line, `<situation> → <what to do>`. It's shown to every future session, so add it
  only when there's a clear rule, and delete the line otherwise.
- Body: exact error text (so grep finds it), what you assumed first if it was wrong, the cause,
  the fix, the scope, and how we know.
- **Never write secrets:** passwords, tokens, keys, certificates, connection strings with
  credentials, customer data. Use `<REDACTED>`.
- Cite related pages by path in backticks, e.g. `team1-mongodb-cassandra/knowledge/mongodb-overview.md`.
- If a version changed, also update `commons/knowledge/platform-versions.md` and save both files together.

## 4. Check it

```bash
bash "$BRAIN/scripts/run.sh" brain.py validate <file> [<file> ...]
```

Fix every ERROR. Warnings are worth a look.

## 5. Ask, then push

Show the engineer:
- the file path(s), and whether each is new or edited
- the `rule:` line, if any
- a 2-3 line summary

Ask: **"Save this to the brain? It pushes straight to main."** Wait for a clear yes, then:

```bash
bash "$BRAIN/scripts/run.sh" brain_save.py -m "brain(<team>): <what was learned>" <file> [<file> ...]
```

- **If the engineer says no:** delete new files; for edited pages run `git -C "$BRAIN" checkout -- <file>`.
- **On a conflict (exit code 2):** follow the steps it prints. Never force-push.
- **If GitLab is unreachable:** the commit stays local; `brain_save.py --push` retries later.

Finish with one line: what was saved, and the commit id that `brain_save.py` printed.
