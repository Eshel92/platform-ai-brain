# Writing pages for the brain

## Where things go

| You learned… | Folder | Template |
|---|---|---|
| A problem: symptom, cause, fix, a wrong first guess | `<team>/knowledge/` | `templates/knowledge.md` |
| How a system is built here | `<team>/knowledge/` | `templates/overview.md` |
| A repeatable procedure | `<team>/runbooks/` | `templates/runbook.md` |
| A decision and its reasons | `<team>/decisions/` | `templates/decision.md` |
| Something unsure or partial | `inbox/` (`type: inbox`) | `templates/knowledge.md` |

`<team>` is `commons` for shared topics (OpenShift, Argo CD, Helm, GitLab, storage, monitoring,
Python), otherwise the team folder. File names: lowercase-with-dashes, named after the symptom or
topic, e.g. `mongodb-startup2-after-resync.md`.

### What each folder is for

- **knowledge/**: how things really behave here. Architecture overviews, quirks, root causes,
  version-specific behaviour, and Claude's lessons from its own mistakes ("What we assumed first").
- **runbooks/**: approved step-by-step procedures with checks, verification and rollback.
- **decisions/**: why we chose X over Y, with alternatives and consequences.
- **inbox/**: anything not yet trustworthy. Sessions treat it as a lead; `/brain:curate` sorts it.

## The header

```yaml
---
title: MongoDB member stuck in STARTUP2 after resync   # what someone would search for
type: knowledge            # knowledge | runbook | decision | inbox (must match the folder)
tags: [mongodb, resync]
applies_to: [mck-1.10, mongo-8.0, ocp-4.18]   # [] = applies everywhere
confidence: observed       # verified | observed | hypothesis   (decisions: status)
last_verified: 2026-11-08  # last time someone confirmed it's still true
owners: [team1]            # who to ask
source: claude-session     # where it came from: session, incident, person, ticket
rule: Member stuck in STARTUP2 after resync → check the oplog window before restarting
---
```

| `confidence` | Means |
|---|---|
| `verified` | Confirmed by the owning team, or tested working |
| `observed` | Seen once, or read in docs or code |
| `hypothesis` | Believed but not confirmed |

Decisions use `status: proposed | accepted | superseded` instead of `confidence`.
Every field and check in detail: `docs/FRONTMATTER.md`.

**`rule`** is optional: one line, `<situation> → <what to do>`. All rules are collected into the
Quick Rules that every Claude session sees at start, so keep them short and only add clear ones.

## Writing rules

- Search first; update an existing page rather than adding a near-duplicate.
- Paste exact error text so search finds it.
- Write version ranges ("since 6.0", "up to 5.0"), never "the current version".
- When a version changes, update `commons/knowledge/platform-versions.md` too.
- Mark gaps as `[UNKNOWN]`.
- Never store passwords, tokens, keys, certificates, connection strings with credentials or
  customer data. Use `<REDACTED>`.
- Link related pages by path in backticks.

## Saving

Claude saves with `/brain:learn`: it shows you the page and asks, and only after your yes runs
`scripts/brain_save.py`. That script checks the page, commits it under your git name, rebases onto
the latest main and pushes. To save a page you wrote yourself:

```bash
bash ~/platform-ai-brain/scripts/run.sh brain_save.py -m "brain(team1): what you learned" <file>
```

Undo a save with `git revert <commit>`, then save the revert the same way (`--push`).

## Weekly curation

One person runs `/brain:curate`: inbox items get promoted, merged or discarded, unconfirmed pages get
confirmed or downgraded, and stale pages (`brain.py stale`) go to their owners to re-check.
