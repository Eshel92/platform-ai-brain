#!/usr/bin/env python3
"""Carry the brain between a connected machine and the air gap as one zip.

On the connected machine (where the tool and the vendor docs are built):

    python3 scripts/transfer.py export [--out FILE]

In the air gap, inside your clone of the GitLab repo:

    bash scripts/run.sh transfer.py import <zip>              # shows what would change; changes nothing
    bash scripts/run.sh transfer.py import <zip> --apply      # applies it, checks pages, pushes to main

First time (the clone doesn't have this script yet): unzip the zip anywhere and run its copy against
the clone:  python3 <unzipped>/platform-ai-brain/scripts/transfer.py import <zip> --into ~/platform-ai-brain

Export packs everything except .git, generated INDEX.md files and caches, plus TRANSFER.json: every
file with its fingerprint, what changed since the last export, and every file an earlier export had
that this one doesn't. A local record of past exports is kept in .transfer/ (ignored by git).

Import takes tool files from the zip, mirrors docs/upstream exactly, updates team pages only where
nobody in the air gap changed them, deletes only files an earlier export had (and only if unchanged),
and never touches pages that exist only in the air gap. Standard library only.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import json
import os
import subprocess
import sys
import zipfile
from pathlib import Path

sys.dont_write_bytecode = True
import brain  # noqa: E402  (same folder)

ROOT = brain.ROOT
TOP = "platform-ai-brain"
MANIFEST = "TRANSFER.json"
STATE = ROOT / ".transfer"
LEDGER = STATE / "ledger.json"  # every fingerprint ever exported, per file
LAST = STATE / "last-export.json"  # the files of the last export
INCOMING = STATE / "incoming"  # the export's version of pages that were kept as they are
SKIP_DIRS = {".git", "__pycache__", ".transfer"}
SKIP_FILES = {".DS_Store", MANIFEST}


def use_root(path: Path) -> None:
    """Work on another brain folder (import --into)."""
    global ROOT, STATE, LEDGER, LAST, INCOMING
    ROOT = brain.ROOT = path.expanduser().resolve()
    STATE = ROOT / ".transfer"
    LEDGER, LAST, INCOMING = STATE / "ledger.json", STATE / "last-export.json", STATE / "incoming"


def fingerprint(data: bytes) -> str:
    return hashlib.sha256(data.replace(b"\r\n", b"\n")).hexdigest()[:20]


def tree(root: Path) -> dict[str, Path]:
    """Every file to carry, by path relative to root."""
    found = {}
    for folder, dirs, names in os.walk(root):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for name in names:
            if name in SKIP_FILES or name.endswith((".pyc", ".zip")):
                continue
            path = Path(folder) / name
            rel = path.relative_to(root).as_posix()
            if name == "INDEX.md" and rel.count("/") <= 1:  # generated indexes (root and team folders)
                continue
            found[rel] = path
    return found


def ours(rel: str) -> bool:
    """Team pages and the inbox: written in the air gap, protected on import."""
    return rel.split("/")[0] in brain.TEAMS + [brain.INBOX]


def area(rel: str) -> str:
    parts = rel.split("/")
    return "/".join(parts[:3]) if rel.startswith("docs/upstream/") else parts[0] if len(parts) > 1 else "(top level)"


def load(path: Path, default):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return default


def summarize(label: str, paths: list[str], full: bool = False, limit: int = 12) -> None:
    if not paths:
        return
    print(f"  {label}: {len(paths)}")
    if full:
        for rel in paths[:limit]:
            print(f"    {rel}")
        if len(paths) > limit:
            print(f"    … {len(paths) - limit} more")
    else:
        groups: dict[str, int] = {}
        for rel in paths:
            groups[area(rel)] = groups.get(area(rel), 0) + 1
        for name, count in sorted(groups.items(), key=lambda g: -g[1])[:limit]:
            print(f"    {count:5d}  {name}")


# ---------------------------------------------------------------- export

def export(out: Path, remember: list[str]) -> int:
    files = tree(ROOT)
    current = {rel: fingerprint(p.read_bytes()) for rel, p in files.items()}
    ledger = load(LEDGER, {"exported": {}})
    for old in remember:  # an older copy of the brain: count its files as exported before
        for rel, p in tree(Path(old).expanduser().resolve()).items():
            hashes = ledger["exported"].setdefault(rel, [])
            if (h := fingerprint(p.read_bytes())) not in hashes:
                hashes.append(h)
    last = load(LAST, {})
    for rel, h in current.items():
        hashes = ledger["exported"].setdefault(rel, [])
        if h not in hashes:
            hashes.append(h)

    stamp = dt.datetime.now(dt.timezone.utc)
    plugin = load(ROOT / "plugin" / ".claude-plugin" / "plugin.json", {})
    changes = {
        "added": sorted(set(current) - set(last)),
        "changed": sorted(r for r in current if r in last and last[r] != current[r]),
        "removed": sorted(set(last) - set(current)),
    }
    manifest = {
        "format": 1,
        "id": stamp.strftime("%Y%m%d-%H%M%S"),
        "exported_at": stamp.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "plugin_version": plugin.get("version", "?"),
        "files": current,
        "removed": {rel: hashes for rel, hashes in ledger["exported"].items() if rel not in current},
        "history": {rel: ledger["exported"][rel] for rel in current if ours(rel)},
        "changes": changes,
    }

    out = out.expanduser().resolve()
    partial = out.with_suffix(out.suffix + ".partial")
    with zipfile.ZipFile(partial, "w", zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
        for rel in sorted(files):
            zf.write(files[rel], f"{TOP}/{rel}")
        zf.writestr(f"{TOP}/{MANIFEST}", json.dumps(manifest, indent=1) + "\n")
    partial.replace(out)
    STATE.mkdir(exist_ok=True)
    LEDGER.write_text(json.dumps(ledger) + "\n", encoding="utf-8")
    LAST.write_text(json.dumps(current) + "\n", encoding="utf-8")

    print(f"Exported {len(current)} files to {out} ({out.stat().st_size / 1e6:.1f} MB), id {manifest['id']}")
    if last:
        print("Since the last export:")
        summarize("added", changes["added"])
        summarize("changed", changes["changed"])
        summarize("removed", changes["removed"], full=True)
        if not any(changes.values()):
            print("  nothing changed")
    else:
        print("First export from this machine: no earlier export to compare with.")
    print(f"In the air gap: bash scripts/run.sh transfer.py import {out.name}")
    return 0


# ---------------------------------------------------------------- import

def git(*args: str, check: bool = True) -> str:
    env = {**os.environ, "GIT_TERMINAL_PROMPT": "0"}
    result = subprocess.run(["git", "-C", str(ROOT), *args], capture_output=True, encoding="utf-8",
                            errors="replace", env=env)
    if check and result.returncode != 0:
        sys.exit(f"git {' '.join(args)} failed:\n{(result.stderr or result.stdout).strip()}")
    return result.stdout.strip()


def import_(zip_path: Path, apply: bool, overwrite_pages: bool) -> int:
    if not (ROOT / ".git").exists():
        sys.exit(f"{ROOT} is not a git clone: import runs inside your clone of the brain repo")
    if git("rev-parse", "--abbrev-ref", "HEAD") != "main":
        sys.exit("the clone isn't on main: switch to main first")
    pending = [l for l in git("status", "--porcelain").splitlines() if not (l.startswith("??") and l.endswith(".zip"))]
    if pending:
        sys.exit("the clone has uncommitted changes: save or discard them first (git status)\n" + "\n".join(pending[:10]))
    if apply:
        git("pull", "--ff-only", "--quiet", "origin", "main")

    zf = zipfile.ZipFile(zip_path)
    try:
        manifest = json.loads(zf.read(f"{TOP}/{MANIFEST}"))
    except KeyError:
        sys.exit(f"{zip_path} has no {MANIFEST}: make it with `transfer.py export`")
    incoming = manifest["files"]
    history = manifest.get("history", {})
    removed = manifest.get("removed", {})
    clone = {rel: fingerprint(p.read_bytes()) for rel, p in tree(ROOT).items()}

    plan: dict[str, list[str]] = {k: [] for k in
                                  ("add", "update", "update_page", "keep_page", "kept_quiet", "delete", "keep_changed")}
    changed_in_export = set(manifest.get("changes", {}).get("changed", [])) | set(manifest.get("changes", {}).get("added", []))
    for rel, h in incoming.items():
        if rel not in clone:
            plan["add"].append(rel)
        elif clone[rel] == h:
            continue
        elif not ours(rel):
            plan["update"].append(rel)
        elif clone[rel] in history.get(rel, []) or overwrite_pages:
            plan["update_page"].append(rel)  # nobody changed it here: take the new version
        elif rel in changed_in_export:
            plan["keep_page"].append(rel)  # changed on both sides: keep ours, set the export's version aside
        else:
            plan["kept_quiet"].append(rel)  # changed here only: nothing to bring in
    for rel, h in clone.items():
        if rel in incoming:
            continue
        if rel.startswith("docs/upstream/"):
            plan["delete"].append(rel)  # vendor docs mirror the export exactly
        elif rel in removed:
            (plan["delete"] if h in removed[rel] else plan["keep_changed"]).append(rel)
    air_gap_only = [r for r in clone if r not in incoming and r not in removed and not r.startswith("docs/upstream/")]
    for key in plan:
        plan[key].sort()

    print(f"Import {zip_path.name}: export {manifest['id']} from {manifest['exported_at']}, plugin {manifest['plugin_version']}")
    changes = manifest.get("changes", {})
    if any(changes.values()):
        print(f"The export's own notes (vs its previous export): {len(changes.get('added', []))} added, "
              f"{len(changes.get('changed', []))} changed, {len(changes.get('removed', []))} removed")
    print("Plan for this clone:")
    summarize("add", plan["add"])
    summarize("update (tool files, vendor docs)", plan["update"])
    summarize("update team pages nobody changed here", plan["update_page"], full=True)
    summarize("delete (old files an earlier export had, or vendor docs no longer exported)", plan["delete"], full=True)
    summarize("CONFLICT: team pages changed here AND in this export. Kept yours; the export's version "
              "goes to .transfer/incoming/ to merge by hand", plan["keep_page"], full=True)
    summarize("KEEP old files that were changed here", plan["keep_changed"], full=True)
    print(f"  untouched: {len(air_gap_only)} file(s) that exist only here, {len(plan['kept_quiet'])} team page(s) "
          f"changed here (the export didn't change them)")
    work = plan["add"] + plan["update"] + plan["update_page"] + plan["delete"]
    if not work and not plan["keep_page"]:
        print("Nothing to do: this clone already matches the export.")
        return 0
    if not apply:
        print("Nothing changed yet. To apply: add --apply")
        return 0

    for rel in plan["add"] + plan["update"] + plan["update_page"]:
        target = ROOT / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(zf.read(f"{TOP}/{rel}"))
    for rel in plan["keep_page"]:
        target = INCOMING / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(zf.read(f"{TOP}/{rel}"))
    for rel in plan["delete"]:
        (ROOT / rel).unlink(missing_ok=True)
        folder = (ROOT / rel).parent
        while folder != ROOT and folder.is_dir() and not any(folder.iterdir()):
            folder.rmdir()
            folder = folder.parent

    if brain.validate() != 0:
        print("Pages failed the check (above). Nothing was committed: fix them, or undo with "
              "`git checkout -- . && git clean -fd`.")
        return 1
    if not git("status", "--porcelain"):
        print("Applied: no file content changed.")
        return 0
    result = subprocess.run([sys.executable, str(ROOT / "scripts" / "brain_save.py"),
                             "-m", f"brain(meta): import export {manifest['id']}", str(ROOT)])
    if plan["keep_page"]:
        print(f"Kept {len(plan['keep_page'])} page(s) changed here; the export's versions are in "
              f"{INCOMING} to compare (not committed).")
    return result.returncode


def main() -> int:
    for stream in (sys.stdout, sys.stderr):
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    p_export = sub.add_parser("export", help="pack the brain into a zip for the air gap")
    p_export.add_argument("--out", default=str(ROOT.parent / f"{TOP}.zip"), help="zip to write")
    p_export.add_argument("--remember", action="append", default=[], metavar="OLD_COPY",
                          help="an older copy of the brain whose files count as exported before")
    p_import = sub.add_parser("import", help="bring an exported zip into this clone")
    p_import.add_argument("zip")
    p_import.add_argument("--apply", action="store_true", help="make the changes and save them")
    p_import.add_argument("--overwrite-pages", action="store_true",
                          help="also replace team pages that were changed here (careful)")
    p_import.add_argument("--into", help="the clone to import into (default: the brain this script is in)")
    args = parser.parse_args()
    if args.command == "import" and args.into:
        use_root(Path(args.into))
    if args.command == "export":
        return export(Path(args.out), args.remember)
    return import_(Path(args.zip).expanduser(), args.apply, args.overwrite_pages)


if __name__ == "__main__":
    sys.exit(main())
