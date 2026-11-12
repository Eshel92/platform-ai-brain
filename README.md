# Platform AI Brain

The shared memory of the platform teams: what we know about our OpenShift, MongoDB, Cassandra,
Elasticsearch and Redis platforms, plus a Claude Code plugin that reads it before work and saves
what Claude learns after.

## How it works

```
every Claude Code session
  │
  ├─ starts   → hook pulls this repo from GitLab, rebuilds the index and gives Claude
  │             the Quick Rules + pages changed in the last 14 days
  ├─ works    → /brain:lookup searches the brain before troubleshooting
  ├─ learns   → /brain:learn drafts a page, the engineer says yes,
  │             brain_save.py checks it and pushes straight to main
  └─ long session, nothing saved → Claude asks once: "anything worth saving?"

weekly → /brain:curate: a person reviews inbox/ and unconfirmed pages
```

There are no merge requests. Each learning is its own file and the index is generated on each
laptop, so two engineers saving at the same time don't collide. The save script blocks common
secret patterns and rebases onto the latest main before pushing.

## Layout

| Path | What lives there |
|---|---|
| `commons/` | Shared by all teams: OpenShift, Argo CD, Helm, GitLab, storage, monitoring, Python |
| `team1-mongodb-cassandra/`, `team2-elastic/`, `team3-redis/`, `team4-placeholder/` | Each team's own pages |
| `<team>/knowledge/` | How things work, gotchas, root causes, lessons |
| `<team>/runbooks/` | Step-by-step procedures |
| `<team>/decisions/` | Decisions and why |
| `inbox/` | Claude's unsure saves, reviewed weekly |
| `templates/` | Starting points for new pages |
| `scripts/` | `brain.py` (checks, index, search), `brain_save.py` (push to main), `transfer.py` (export / import) |
| `plugin/` | The Claude Code plugin (hooks + skills) |
| `docs/` | Design, page header reference, maintainer guide |
| `docs/upstream/` | Offline vendor docs (MongoDB, Ops Manager, MCK, Cassandra, K8ssandra, Elasticsearch, Kibana, Redis Enterprise, Kubernetes, Argo CD, monitoring), as Markdown |
| `tests/` | `test_flow.sh`: end-to-end test of saving and syncing |
| `.gitlab-ci.yml` | Optional CI check, inactive until configured |

## Daily use

| Command | When |
|---|---|
| `/brain:lookup <topic>` | Before an investigation (Claude also does it on its own) |
| `/brain:learn` | After solving or discovering something |
| `/brain:curate` | Weekly, by one person |

## Moving it into the air gap: export and import

The tool and the vendor docs are built on a connected machine; the team's pages live in the air gap.
`scripts/transfer.py` carries a new version across as one zip, without touching what the team saved.

### 1. Export (connected machine)

```bash
python3 scripts/transfer.py export        # writes ../platform-ai-brain.zip next to the brain folder
```

It packs everything except git history, generated `INDEX.md` files and caches, and prints what
changed since the last export. Carry the zip across the approved way.

The export keeps a small record of past exports in `.transfer/` (ignored by git). Keep it: it's how
the next export knows which files were removed.

### 2. Import (air gap, inside your clone)

```bash
bash scripts/run.sh transfer.py import ~/platform-ai-brain.zip            # shows the plan, changes nothing
bash scripts/run.sh transfer.py import ~/platform-ai-brain.zip --apply    # applies it and pushes to main
```

**First time**, when the clone doesn't have `transfer.py` yet, run the zip's own copy against your clone:

```bash
unzip platform-ai-brain.zip -d ~/brain-new
python3 ~/brain-new/platform-ai-brain/scripts/transfer.py import platform-ai-brain.zip --into ~/platform-ai-brain
python3 ~/brain-new/platform-ai-brain/scripts/transfer.py import platform-ai-brain.zip --into ~/platform-ai-brain --apply
```

On Windows use `py` instead of `python3` (in Git Bash), or `bash scripts/run.sh …` as above.

What import does to each kind of file:

| Files | What happens |
|---|---|
| Tool files (scripts, plugin, docs, templates, README) | Replaced by the zip's version |
| Vendor docs (`docs/upstream/`) | Mirrored exactly: added, updated, removed |
| Team pages and inbox nobody changed in the air gap | Updated to the zip's version |
| Team pages changed in the air gap | **Kept.** If the zip changed the same page too, import reports a conflict and puts the zip's version in `.transfer/incoming/` to merge by hand |
| Pages that exist only in the air gap | **Never touched** |
| Files an earlier export had that this one doesn't | Deleted, but only if unchanged in the air gap |

Before applying, the clone must be on `main` with no uncommitted changes, and GitLab must be
reachable. Import pulls first, checks every page, then commits and pushes everything as one save.
Teammates get the new version at their next session start.

Rule of thumb: **edit team pages in the air gap; change tool files and vendor docs on the connected
machine.** To take the zip's version of pages that were changed in the air gap anyway, add
`--overwrite-pages` (careful: it replaces teammates' edits).

## Rules

1. Every page has a header with scope (`applies_to`) and honesty (`confidence`).
2. Unknown is written as `[UNKNOWN]`, never guessed.
3. No secrets, ever.
4. Claude pushes only after the engineer says yes.
5. A runbook in the brain doesn't authorize running it.

## Docs

| File | Read it when |
|---|---|
| `AIRGAP_SETUP_GUIDE.md` | Setting up GitLab or a workstation |
| `CONTRIBUTING.md` | Writing or editing pages |
| `docs/FRONTMATTER.md` | You need the exact page header rules |
| `docs/DESIGN.md` | You want to know how it works, why, and what's been tested |
| `docs/ADMIN.md` | Maintaining it: adding a team, changing the plugin, undoing a save, a leaked secret |
| `CLAUDE.md` | (For Claude) rules when working inside this repo |
| `commons/decisions/brain-*.md` | Why it was built this way |
| `commons/knowledge/upstream-docs.md` | Which vendor-docs folder answers what, and its version vs ours |
| `docs/upstream/README.md` | Refreshing the vendor docs |
| `NOTICE` | Licenses of the vendor docs |

Start pages: `commons/knowledge/platform-versions.md` (what runs where) and each team's `knowledge/`.

## Glossary

| Term | Meaning |
|---|---|
| commons | Topics shared by all teams |
| Quick Rules | One-line lessons (`rule:` in a page header) shown to every Claude session at start |
| inbox | Claude's unsure saves, waiting for the weekly review |
| curate | The weekly review: promote, merge or discard inbox pages; confirm unproven ones |
| `confidence` | `verified` (team-confirmed or tested), `observed` (seen once), `hypothesis` (unconfirmed) |
| MCK | MongoDB Controllers for Kubernetes, the MongoDB operator |

## Next (phase 2)

A shared search server, only if local search turns out too slow or the models don't use it, and an
automatic lookup on every message if the pilot shows they don't search on their own. See `docs/ADMIN.md`.
