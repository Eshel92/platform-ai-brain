#!/usr/bin/env python3
"""Refresh the offline upstream docs in docs/upstream/ from GitHub or an internal git mirror.

Run it on a machine that can reach the git host (not inside the air gap), then bring the
updated docs/upstream/ folder in and save it with brain_save.py. Needs git, and PyYAML for the
MongoDB conversion (pip3 install pyyaml). Sources marked "convert" become one Markdown file per page
(see upstream_convert.py).

    python3 scripts/sync_upstream_docs.py                  # every source in docs/upstream/sources.json
    python3 scripts/sync_upstream_docs.py mck-1.7 vector   # only these
    python3 scripts/sync_upstream_docs.py --list           # show the sources
    python3 scripts/sync_upstream_docs.py --versions       # only rebuild VERSIONS.md

Environment:
  UPSTREAM_GIT_BASE   git host to clone from (default https://github.com), e.g. https://gitlab.internal/mirrors
"""
from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import json
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

sys.dont_write_bytecode = True
from upstream_convert import convert_tree  # noqa: E402  (same folder)

ROOT = Path(__file__).resolve().parent.parent
UPSTREAM = ROOT / "docs" / "upstream"
SOURCES = UPSTREAM / "sources.json"
BASE = os.environ.get("UPSTREAM_GIT_BASE", "https://github.com").rstrip("/")
TEXT = {".md", ".markdown", ".txt", ".rst", ".adoc", ".yaml", ".yml"}
LICENSES = [
    ("Attribution-NonCommercial-NoDerivatives 4.0", "CC BY-NC-ND 4.0"),
    ("Attribution-NonCommercial-ShareAlike 4.0", "CC BY-NC-SA 4.0"),
    ("Apache License", "Apache-2.0"),
    ("Attribution-NonCommercial-ShareAlike 3.0", "CC BY-NC-SA 3.0"),
    ("Attribution 4.0 International", "CC BY 4.0"),
    ("GNU AFFERO GENERAL PUBLIC LICENSE", "AGPL-3.0"),
    ("Mozilla Public License", "MPL-2.0"),
    ("MIT License", "MIT"),
]


def git(*args: str, cwd: Path | None = None) -> str:
    result = subprocess.run(["git", *args], cwd=cwd, capture_output=True, text=True, timeout=900)
    if result.returncode != 0:
        raise RuntimeError(f"git {' '.join(args)}: {(result.stderr or result.stdout).strip()}")
    return result.stdout.strip()


def selected(rel: str, source: dict) -> bool:
    """The source's include / exclude patterns."""
    if source.get("include") and not any(fnmatch.fnmatch(rel, p) for p in source["include"]):
        return False
    return not any(fnmatch.fnmatch(rel, p) for p in source.get("exclude", []))


def wanted(rel: str, source: dict) -> bool:
    if Path(rel).suffix.lower() not in TEXT | set(source.get("extra_extensions", [])):
        return False
    return selected(rel, source)


def license_of(repo: Path) -> tuple[str, Path | None]:
    for name in ("LICENSE", "LICENSE.md", "LICENSE.txt", "COPYING", "license"):
        path = repo / name
        if path.is_file():
            head = path.read_text(encoding="utf-8", errors="ignore")[:3000]
            label = next((label for needle, label in LICENSES if needle.lower() in head.lower()), "see LICENSE")
            return label, path
    return "unknown", None


def sync(source: dict) -> str:
    name = source["name"]
    with tempfile.TemporaryDirectory() as tmp:
        repo = Path(tmp) / "repo"
        git("clone", "--quiet", "--depth", "1", "--filter=blob:none", "--sparse",
            "--branch", source["ref"], f"{BASE}/{source['repo']}", str(repo))
        git("sparse-checkout", "set", *source["paths"], *source.get("checkout", []), cwd=repo)
        commit = git("rev-parse", "HEAD", cwd=repo)

        build = Path(tmp) / "out"  # build here, swap in at the end: a failure never leaves half a snapshot
        build.mkdir()
        files, notes = 0, set()
        for folder in source["paths"]:
            base = repo / folder
            target = build / Path(folder).name if len(source["paths"]) > 1 else build
            if source.get("convert"):  # one self-contained Markdown file per page
                count, found = convert_tree(source["convert"], base, target,
                                            keep=lambda rel: selected(rel, source), attrs=source.get("attrs"))
                files, notes = files + count, notes | found
                if source["convert"] != "md":  # stray Markdown next to rst/AsciiDoc sources
                    for extra in base.glob("*.md"):
                        target.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(extra, target / extra.name)
                        files += 1
                continue
            for path in sorted(base.rglob("*")):
                rel = path.relative_to(base).as_posix()
                if path.is_file() and wanted(rel, source):
                    out = target / rel
                    out.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(path, out)
                    files += 1
        for extra in source.get("root_files", []):
            if (repo / extra).is_file():
                shutil.copy2(repo / extra, build / extra)
                files += 1
        if not files:
            raise RuntimeError(f"no doc files found under {source['paths']}: the upstream layout may have moved")
        label, license_file = license_of(repo)
        if license_file:
            shutil.copy2(license_file, build / "LICENSE")
        elif source.get("license"):  # no license file in the repo: use the one stated in sources.json
            label = source["license"]

        size = sum(p.stat().st_size for p in build.rglob("*") if p.is_file())
        meta = {
            "name": name, "team": source["team"], "about": source["about"],
            "repo": source["repo"], "ref": source["ref"], "commit": commit,
            "paths": source["paths"], "files": files, "bytes": size, "license": label,
            "format": {"rst": "Markdown, converted from reStructuredText (includes inlined)",
                       "adoc": "Markdown, converted from AsciiDoc (includes inlined)",
                       "asciidoc": "Markdown, converted from AsciiDoc (snippets inlined)",
                       "md": "Markdown (substitutions filled in, shared snippets inlined)"}.get(source.get("convert"), "as upstream"),
            "notes": sorted(notes),
            "synced": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        (build / ".upstream").write_text(json.dumps(meta, indent=2) + "\n", encoding="utf-8")
        dest = UPSTREAM / name
        if dest.exists():
            shutil.rmtree(dest)
        shutil.move(str(build), str(dest))
    return f"{name}: {files} files, {size / 1e6:.1f} MB, {label}, {source['ref']} @ {commit[:10]}"


def write_versions() -> None:
    rows = []
    for meta_file in sorted(UPSTREAM.glob("*/.upstream")):
        m = json.loads(meta_file.read_text(encoding="utf-8"))
        rows.append(f"| `{m['name']}` | {m['team']} | {m['repo']} | {m['ref']} | {m['commit'][:10]} | "
                    f"{m['files']} | {m['bytes'] / 1e6:.1f} MB | {m['license']} | {m['synced'][:10]} | {m['about']} |")
    text = [
        "# Upstream doc snapshots",
        "",
        "_Generated by `scripts/sync_upstream_docs.py`. Don't edit. Each folder also has a `.upstream` file and the project's `LICENSE`._",
        "",
        "| Folder | Team | Source | Ref | Commit | Files | Size | License | Synced | What it covers |",
        "|---|---|---|---|---|---|---|---|---|---|",
        *rows,
        "",
    ]
    (UPSTREAM / "VERSIONS.md").write_text("\n".join(text), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("names", nargs="*", help="source names (default: all)")
    parser.add_argument("--list", action="store_true", help="list the sources and exit")
    parser.add_argument("--versions", action="store_true", help="only rebuild VERSIONS.md")
    args = parser.parse_args()

    sources = json.loads(SOURCES.read_text(encoding="utf-8"))["sources"]
    if args.list:
        for s in sources:
            print(f"{s['name']:28s} {s['repo']} @ {s['ref']}")
        return 0
    if not args.versions:
        unknown = set(args.names) - {s["name"] for s in sources}
        if unknown:
            sys.exit(f"unknown source(s): {', '.join(sorted(unknown))}")
        failed = 0
        for source in sources:
            if args.names and source["name"] not in args.names:
                continue
            try:
                print(sync(source), flush=True)
            except Exception as error:  # keep the old snapshot and carry on
                failed += 1
                print(f"{source['name']}: FAILED, old snapshot kept. {error}", file=sys.stderr, flush=True)
    write_versions()
    return 1 if not args.versions and failed else 0


if __name__ == "__main__":
    sys.exit(main())
