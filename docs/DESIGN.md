# How the brain works

## Goals and constraints

- **Two jobs:** a knowledge base the teams trust, and a learning loop: Claude saves what it learned so
  the next session, anyone's, doesn't repeat the mistake.
- **Air-gapped:** no internet, nothing to `pip install`.
- **Models:** open-source models through Claude Code, with small context windows. We can't count on them
  following long instructions.
- **Four teams** with different technologies, plus shared topics in `commons/`.

## Parts

| Part | Started by | Job |
|---|---|---|
| SessionStart hook (`plugin/scripts/session_start.py`) | Claude Code, at every session start, resume, clear and compact | Pull `main` (fast-forward only), rebuild `INDEX.md`, brief Claude: Quick Rules, recent pages, how to use the brain |
| Stop hook (`plugin/scripts/stop_nudge.py`) | Claude Code, when Claude finishes a reply | Once per long session with no save: ask Claude to offer one |
| `/brain:lookup` | The model or the engineer | Search before work |
| `/brain:learn` | The model or the engineer | Draft a page, ask the engineer, then save |
| `/brain:curate` | The engineer only | Weekly review of the inbox and unconfirmed pages |
| `scripts/brain.py` | Anyone | `validate`, `index`, `rules`, `stale` |
| `scripts/brain_save.py` | The learn and curate skills | Check → commit → rebase → push to `main` |

## What's guaranteed, and what depends on the model

- **Guaranteed** (Claude Code runs it, whatever the model): the pull, the briefing, the nudge, and the
  checks inside `brain_save.py`.
- **Up to the model:** looking things up or offering a save on its own, writing a good page, asking
  before pushing. Engineers can always type `/brain:lookup` and `/brain:learn` themselves.

## Why saves don't collide

- Each learning is its own file with a unique name.
- Nobody edits a shared file by hand: `INDEX.md` and the Quick Rules are generated on each laptop and
  never committed.
- `brain_save.py` rebases onto the latest `main` before pushing, and retries up to 3 times.
- One case is left: two people editing the same lines of one page. The script stops (exit code 2),
  keeps the commit and prints how to merge.

## Safety without merge requests

| A merge request gave | Replaced by |
|---|---|
| A person reads it first | The engineer approves the page in the session before the push |
| Secrets caught | Secret-pattern check before every push (`docs/FRONTMATTER.md`) |
| Unproven claims caught | Claude's pages start as `observed` or `hypothesis`; weekly `/brain:curate` |
| A record of who changed what | The engineer's own git name, a `Captured-By: Claude Code` line, `git revert` |

Reasons and trade-offs: `commons/decisions/brain-saves-push-straight-to-main.md`.

## Context budget

- Skill descriptions: about 250 tokens in every session.
- Briefing: about 800 tokens today, capped near 1,500 (6,000 characters). `BRAIN_TEAM` and
  `BRAIN_RULES_LIMIT` make it smaller.
- Pages are read only when needed.
- The vendor docs in `docs/upstream/` cost nothing until Claude opens a page. Claude searches only
  the folder for the product and version it needs, so other teams' docs never show up in results.

## Tested, and not tested yet

Tested on macOS with Claude Code 2.1.311, git 2.52 and Python 3.11:

- `tests/test_flow.sh`, 42 checks: saving, pulling, two people saving at once, a real conflict, a blocked
  secret, unrelated local edits kept, a page moved out of the inbox, offline then retry, the nudge, search and section reading.
- `claude plugin validate`, then install and enable. A real session received the briefing and listed
  the skills.

Not tested yet:

- A real GitLab: protected-branch settings, authentication, push permissions.
- Linux workstations. The test is written for both; run it there once (`bash tests/test_flow.sh`).
- The air-gap models: whether they use the skills on their own and always ask before pushing.
- `.gitlab-ci.yml` on a real runner.
