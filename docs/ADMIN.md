# Running the brain (for maintainers)

## Commands

```bash
bash scripts/run.sh brain.py validate                        # check every page
bash scripts/run.sh brain.py index                           # rebuild INDEX.md (also done at session start)
bash scripts/run.sh brain.py rules --team team1-mongodb-cassandra
bash scripts/run.sh brain.py stale --days 180                # pages nobody re-checked lately
bash scripts/run.sh brain.py search <words> [--folder F]      # ranked search: our pages first, then vendor docs
python3 scripts/sync_upstream_docs.py --resplit                # split big vendor pages already downloaded
python3 scripts/transfer.py export                             # zip for the air gap (connected machine)
bash scripts/run.sh transfer.py import <zip> [--apply]         # bring it in (air gap)
bash scripts/run.sh brain.py show <file> ["<section>"]        # outline of a page, or one section
bash scripts/run.sh brain_save.py -m "brain(<team>): ..." <files>
bash scripts/run.sh brain_save.py --push                     # push commits that are waiting
bash tests/test_flow.sh                                  # after changing scripts/ or plugin/scripts/
claude plugin validate .                                 # after changing plugin/ or .claude-plugin/
python3 scripts/sync_upstream_docs.py --list             # vendor-doc sources (refresh: see below)
```

## Rolling out

- **Per engineer:** `AIRGAP_SETUP_GUIDE.md`, step 3. This is the tested path: Claude Code reads the
  plugin straight from the clone, so every session pull also updates it.
- **Many workstations at once (not tested here):** Claude Code managed settings can pre-register the
  marketplace and enable the plugin (`extraKnownMarketplaces`, `enabledPlugins`). Check the keys
  against your Claude Code version's settings docs, then run `claude plugin list` and look at "Read
  from". A marketplace added from a git URL is a separate copy that only changes after
  `claude plugin marketplace update platform-ai-brain`.

## Recipes

| Task | How |
|---|---|
| Add a team | Create `<team>/knowledge`, `runbooks` and `decisions`, each with a file (`.gitkeep`). Add the folder name to `TEAMS` in `scripts/brain.py`, and to the team lists in `CLAUDE.md`, `README.md`, `plugin/skills/lookup/SKILL.md` and `plugin/skills/learn/SKILL.md`. Bump the plugin version. Save. |
| Rename `team4-placeholder` | `git mv` the folder, then make the same edits as "Add a team". |
| Change hooks or skills | Edit `plugin/`, run the test, bump `version` in `plugin/.claude-plugin/plugin.json`, save as `brain(meta): …`. Everyone gets it at their next session start. |
| Change the scripts | Edit `scripts/`, run `bash tests/test_flow.sh`, save as `brain(meta): …`. |
| Add a secret pattern | Add it to `SECRETS` in `scripts/brain.py` and a case to the secret check in `tests/test_flow.sh`. |
| A version changed | Update `commons/knowledge/platform-versions.md` and the component's own page in one save. |
| Undo a bad save | In the clone: `git revert <commit>`, then `bash scripts/run.sh brain_save.py --push`. |
| A secret got pushed | 1. Rotate the secret now: it's already in every clone. 2. Revert the commit. 3. Only if policy requires removing it from history: allow force push on `main` temporarily, rewrite history, and have every engineer re-clone. |
| Weekly review | `/brain:curate`, run by one person. |
| Smaller briefing | `BRAIN_TEAM` and `BRAIN_RULES_LIMIT`; hard cap `MAX_CHARS` in `plugin/scripts/session_start.py`. |
| Turn on CI | Set the CI/CD variable `BRAIN_CI_IMAGE` to a Python image in your internal registry (see `.gitlab-ci.yml`). Add a weekly pipeline schedule for the stale report. |
| Switch to merge requests | Protect `main` (Maintainers only) and change `push()` in `scripts/brain_save.py` to push a branch and open an MR. Background: `commons/decisions/brain-saves-push-straight-to-main.md`. |
| Refresh the vendor docs | On a connected machine with PyYAML (`pip3 install pyyaml`): `python3 scripts/sync_upstream_docs.py` (or name one source), then export and import (README, "Moving it into the air gap"). |
| Pin a vendor-doc version | Change `ref` and `name` of that source in `docs/upstream/sources.json` (e.g. `release-3.2` → `release-3.1` for Argo CD), refresh it, delete the old folder, update `commons/knowledge/upstream-docs.md`. |
| Bring a new version into the air gap | `python3 scripts/transfer.py export` on the connected machine, then `transfer.py import` in the air gap: README, "Moving it into the air gap". |
| Add a search synonym | Add a line to `docs/search-synonyms.txt`: equivalent terms, comma-separated (e.g. `pvc, persistent volume claim`). It's pushed to GitHub, so generic terms only. |
| Add vendor docs | Step by step in `docs/upstream/README.md`, section "Adding new vendor docs". |
| Phase 2: shared search | Only if needed: wrap `brain.py search` in a small MCP server run once on OpenShift, so every engineer gets ranked search as a tool. |
