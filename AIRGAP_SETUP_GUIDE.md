# Air-gap setup guide

## What you need

- **Claude Code 2.x** on each workstation (plugins). Check with `claude --version`; tested on 2.1.311.
- **git** and **Python 3.9+** (`python3`, or `python` / `py` on Windows). The scripts use only the
  standard library: nothing to pip install.
- **On Windows:** Git for Windows *with Git Bash* (Claude Code runs the brain's hooks in Git Bash) and
  Python from python.org. See "Windows" below.
- Each engineer's git name set (`git config --global user.name` / `user.email`); saves are committed as them.
- **Git access to GitLab without a password prompt**: an SSH key (loaded in ssh-agent if it has a
  passphrase) or HTTPS with a stored token / credential helper. The hooks run in the background and
  can't type a password. Check: `git -C ~/platform-ai-brain pull` must work without asking anything.

## 1. Bring it in

On the Mac: zip `~/Documents/platform-ai-brain`, transfer it the approved way, unzip it inside.
The zip is about 31 MB, mostly the offline vendor docs in `docs/upstream/`. A clone is about 130 MB
(about 98 MB of files plus the git history).

The vendor docs can't be refreshed inside the air gap: refresh them on a connected machine and
bring them in (`docs/upstream/README.md`).

## 2. GitLab project (once)

1. Create the project, e.g. `platform-engineering/platform-ai-brain`, default branch `main`.
2. **Settings → Repository → Protected branches → `main`:**
   - Allowed to merge: Developers + Maintainers
   - Allowed to push and merge: **Developers + Maintainers** (saves push straight to main)
   - Allowed to force push: off
   - Code owner approval: off (with it on, GitLab rejects direct pushes)
3. Push the content:

```bash
cd platform-ai-brain
git init -b main
git add -A
git commit -m "brain(meta): bootstrap"
git remote add origin <gitlab-url>/platform-engineering/platform-ai-brain.git
git push -u origin main
```

If you already pushed the earlier version: clone it, delete everything except `.git`, copy the new
files in, then `git add -A` (this records the deletions too), commit and push.

## 3. Each engineer (once)

```bash
git clone <gitlab-url>/platform-engineering/platform-ai-brain.git ~/platform-ai-brain
claude plugin marketplace add ~/platform-ai-brain
claude plugin install brain@platform-ai-brain
```

Optional, in your shell profile:

```bash
export BRAIN_TEAM=team1-mongodb-cassandra   # Quick Rules from commons + your team only
export BRAIN_DIR=/some/other/path            # only if you didn't clone to ~/platform-ai-brain
```

### Windows

Run these in PowerShell (`$HOME` is `C:\Users\<you>`):

```powershell
git clone <gitlab-url>/platform-engineering/platform-ai-brain.git "$HOME\platform-ai-brain"
claude plugin marketplace add "$HOME\platform-ai-brain"
claude plugin install brain@platform-ai-brain
[Environment]::SetEnvironmentVariable("BRAIN_TEAM", "team1-mongodb-cassandra", "User")   # optional
```

- The repo forces Unix line endings (`.gitattributes`), so it's fine even if git is set to convert
  them. A clone made **before** this file existed may have Windows line endings: delete it and clone again.
- The hooks and skills find Python by trying `python3`, then `python`, then `py`. The Windows Store
  "python3" shortcut that only opens the Store is skipped.
- To run brain commands yourself, use Git Bash: `bash ~/platform-ai-brain/scripts/run.sh brain.py validate`.

If you installed the first version, remove it:

```bash
rm -f ~/.claude/commands/brain.md ~/.claude/commands/learn.md
# and delete the "Platform AI Brain" section from ~/.claude/CLAUDE.md
```

## 4. Check it

```bash
claude plugin list                         # brain@platform-ai-brain  ✔ enabled
bash ~/platform-ai-brain/tests/test_flow.sh   # once per OS: 42 checks, runs in a temp folder (Git Bash on Windows)
bash ~/platform-ai-brain/scripts/run.sh ../plugin/scripts/session_start.py   # prints the session briefing
```

The test uses a fake GitLab in a temp folder, so it never touches the real one. It was run on macOS;
run it once on your Windows / Linux workstations.

The last command runs the session-start hook by hand. It should print JSON whose text starts with
`PLATFORM BRAIN: … up to date with GitLab` and lists the Quick Rules. If it doesn't, the hook can't
work either, and the error message says why.

Start `claude` and ask: *"What Quick Rules did the platform brain give you?"* Then try
`/brain:lookup mongodb versions`.

## 5. Optional: CI

`.gitlab-ci.yml` re-checks every push to `main` and can report stale pages weekly. It stays inactive
until you set the CI/CD variable `BRAIN_CI_IMAGE` to an image in your internal registry that has python3, git and
bash. Details: `docs/ADMIN.md`.

## Updates

Claude Code reads the plugin straight from your clone, and every session pulls the clone. Changes to
pages, hooks and skills reach everyone on their next session, with no reinstall.

## Settings

| Variable | Default | Effect |
|---|---|---|
| `BRAIN_DIR` | `~/platform-ai-brain` | Where the clone is |
| `BRAIN_TEAM` | (all) | Show Quick Rules from commons + this team only |
| `BRAIN_RULES_LIMIT` | 25 | Max Quick Rules in the session briefing |
| `BRAIN_NUDGE_MIN_TOOLS` | 20 | Tool calls before the "anything worth saving?" question |
| `BRAIN_NUDGE_DISABLE` | unset | `1` turns that question off |

## Troubleshooting

| Briefing or error says | Fix |
|---|---|
| `not found at …` | Clone to `~/platform-ai-brain`, or set `BRAIN_DIR` |
| `couldn't reach GitLab` | Offline: the local copy is used. Saves wait locally; push later with `brain_save.py --push` |
| `N local commit(s) not pushed` | `bash ~/platform-ai-brain/scripts/run.sh brain_save.py --push` |
| `local edits … clash` | In `~/platform-ai-brain`: `git status`, then save or discard those edits |
| Push rejected: protected branch | Developers aren't allowed to push to `main` (step 2) |
| `conflict` (exit code 2) | Follow the printed steps; Claude can merge the two versions |
| `/brain:…` commands missing | `claude plugin list`; install again (step 3) |

More maintenance tasks (adding a team, undoing a save, a leaked secret): `docs/ADMIN.md`.

Claude Code older than 2.x has no plugins. Upgrade, or add the two hooks from
`plugin/hooks/hooks.json` to `~/.claude/settings.json` by hand, replacing `${CLAUDE_PLUGIN_ROOT}`
with `~/platform-ai-brain/plugin`.
