---
name: curate
description: Curate the platform brain — review inbox items, promote or merge or discard them, confirm or downgrade unproven pages, list stale pages — then push one commit to main after the engineer approves. Use when the engineer asks to curate, clean up or review the brain.
disable-model-invocation: true
---

# Curate the brain (weekly, run by a person)

```bash
BRAIN="${BRAIN_DIR:-$HOME/platform-ai-brain}"
ls "$BRAIN/inbox"
grep -rlE '^confidence: (observed|hypothesis)' "$BRAIN"/*/knowledge "$BRAIN"/*/runbooks
bash "$BRAIN/scripts/run.sh" brain.py stale --days 180
```

## 1. Decide, item by item

For **each inbox item**, pick one:
- **promote:** move it to `<team>/knowledge|runbooks|decisions/`, set `type`, tidy the wording
- **merge:** fold it into an existing page (extend `applies_to`, add a `## History` line), delete the inbox file
- **keep:** still unclear; leave it and say what's missing
- **discard:** wrong, duplicate or not durable; delete it

For **observed / hypothesis pages**: ask the engineer whether they can confirm them now.
Raise `confidence` only on their word or on new evidence.

For **stale pages**: don't delete them. List them with their `owners` so someone re-checks them.

## 2. Show the plan, wait for approval

A table: item → decision → reason. Wait for the engineer's yes.

## 3. Apply and save as one commit

Make the moves and edits, then:

```bash
bash "$BRAIN/scripts/run.sh" brain.py validate
bash "$BRAIN/scripts/run.sh" brain_save.py -m "brain(curate): review $(date +%F)" <every changed, moved or deleted path>
```

For a moved page, pass both the old and the new path.
