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
| `scripts/` | `brain.py` (checks, index) and `brain_save.py` (push to main) |
| `plugin/` | The Claude Code plugin (hooks + skills) |
| `docs/` | Design, page header reference, maintainer guide |
| `docs/upstream/` | Offline vendor docs (MongoDB, Ops Manager, MCK, Cassandra, K8ssandra, Kubernetes, Argo CD, monitoring), as Markdown |
| `tests/` | `test_flow.sh`: end-to-end test of saving and syncing |
| `.gitlab-ci.yml` | Optional CI check, inactive until configured |

## Daily use

| Command | When |
|---|---|
| `/brain:lookup <topic>` | Before an investigation (Claude also does it on its own) |
| `/brain:learn` | After solving or discovering something |
| `/brain:curate` | Weekly, by one person |

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

A shared search server (keyword ranking over the brain and `docs/upstream/`), following the
team-redbull/redbull-brain example, and docs for Elasticsearch and Redis when those teams join.
See `docs/ADMIN.md`.
