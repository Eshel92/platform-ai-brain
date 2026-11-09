#!/usr/bin/env python3
"""Save brain pages straight to main: check → commit → rebase onto origin/main → push.

Run it only after the engineer said yes.

    python3 scripts/brain_save.py -m "brain(team1): what was learned" FILE [FILE ...]
    python3 scripts/brain_save.py --push      # retry commits a previous run couldn't push

Files may be new, edited or deleted (pass both paths when moving a page).
Exit codes: 0 saved, 1 error (nothing pushed), 2 conflict (commit kept locally).
Standard library only.
"""
from __future__ import annotations

import argparse
import os
import subprocess
import sys

sys.dont_write_bytecode = True
import brain  # noqa: E402  (same folder)

ROOT = brain.ROOT
RUN = f'bash "{(ROOT / "scripts" / "run.sh").as_posix()}"'  # works on Linux, macOS and Git Bash on Windows
TRAILER = "Captured-By: Claude Code (platform brain)"
ATTEMPTS = 3
NETWORK_TIMEOUT = 60
SAVED_MARK = "[brain-saved]"  # the Stop hook looks for this to know a save happened


class SaveError(Exception):
    def __init__(self, message: str, code: int = 1):
        super().__init__(message)
        self.code = code


def git(*args: str, timeout: int | None = None, check: bool = True) -> subprocess.CompletedProcess:
    env = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}  # no one can answer a password prompt here: fail fast
    result = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, encoding="utf-8",
                            errors="replace", timeout=timeout, env=env)
    if check and result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise SaveError(f"git {' '.join(args)} failed:\n{detail}")
    return result


def ensure_ready() -> None:
    branch = git("rev-parse", "--abbrev-ref", "HEAD").stdout.strip()
    if branch != "main":
        raise SaveError(f"the brain clone is on branch '{branch}'. Switch it back to main first.")
    git_dir = ROOT / git("rev-parse", "--git-dir").stdout.strip()
    if (git_dir / "rebase-merge").exists() or (git_dir / "rebase-apply").exists():
        raise SaveError("a rebase is in progress in the brain clone. Finish it or run: git rebase --abort")


def commit(message: str, paths: list[str]) -> None:
    errors = [e for p in paths if (ROOT / p).exists() and brain.kind_of(p) for e in brain.check_page(p)[0]]
    if errors:
        raise SaveError("not saved: fix these first\n" + "\n".join(f"  {e}" for e in errors))
    if not git("status", "--porcelain", "--", *paths).stdout.strip():
        raise SaveError("nothing to save: those files have no changes")
    git("add", "-A", "--", *paths)
    git("commit", "--quiet", "-m", message, "-m", TRAILER, "--", *paths)


def rebase_onto_main() -> None:
    result = git("rebase", "--autostash", "origin/main", check=False)
    if result.returncode == 0:
        return
    conflicted = git("diff", "--name-only", "--diff-filter=U", check=False).stdout.split()
    git("rebase", "--abort", check=False)
    files = ", ".join(conflicted) or "(see git output)"
    raise SaveError(
        f"conflict: someone else changed the same lines in {files}.\n"
        "Your commit is kept locally on main. To finish:\n"
        f'  1. git -C "{ROOT.as_posix()}" rebase origin/main\n'
        "  2. merge both versions in the file(s) above, then: git add <file>; git rebase --continue\n"
        f"  3. {RUN} brain_save.py --push",
        code=2,
    )


def push() -> str:
    for _ in range(ATTEMPTS):
        fetched = git("fetch", "--quiet", "origin", "main", timeout=NETWORK_TIMEOUT, check=False)
        if fetched.returncode != 0:
            raise SaveError(
                "couldn't reach GitLab; your commit is kept locally. Retry later with: "
                f"{RUN} brain_save.py --push\n{fetched.stderr.strip()}"
            )
        if git("rev-list", "--count", "origin/main..HEAD").stdout.strip() == "0":
            raise SaveError("nothing to push: main has no local commits")
        rebase_onto_main()
        result = git("push", "--quiet", "origin", "HEAD:main", timeout=NETWORK_TIMEOUT, check=False)
        if result.returncode == 0:
            return git("log", "-1", "--pretty=%h %s").stdout.strip()
        if "rejected" not in result.stderr and "fetch first" not in result.stderr:
            raise SaveError(
                "push failed; your commit is kept locally. Retry with: "
                f"{RUN} brain_save.py --push\n{result.stderr.strip()}"
            )
    raise SaveError(f"main kept moving during {ATTEMPTS} attempts. Retry with --push in a minute.")


def main() -> int:
    for stream in (sys.stdout, sys.stderr):  # Windows consoles and pipes default to a non-UTF-8 code page
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("-m", "--message", help='commit message, e.g. "brain(team1): what was learned"')
    parser.add_argument("--push", action="store_true", help="only push commits that are waiting")
    parser.add_argument("files", nargs="*")
    args = parser.parse_args()
    if not args.push and (not args.message or not args.files):
        parser.error("give -m MESSAGE and at least one FILE (or use --push)")

    try:
        ensure_ready()
        if not args.push:
            commit(args.message, [brain.to_rel(f) for f in args.files])
        pushed = push()
    except subprocess.TimeoutExpired:
        print(f"GitLab didn't answer in time; any commit is kept locally. Retry: "
              f"{RUN} brain_save.py --push", file=sys.stderr)
        return 1
    except SaveError as error:
        print(error, file=sys.stderr)
        return error.code

    brain.write_index()
    print(f"{SAVED_MARK} pushed to main: {pushed}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
