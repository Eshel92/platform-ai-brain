#!/usr/bin/env python3
"""Brain maintenance: check pages, build the index, list Quick Rules and stale pages.

Standard library only, so it runs on any workstation without pip.

    python3 scripts/brain.py validate [FILE ...]      # all pages when no file is given
    python3 scripts/brain.py index                    # writes INDEX.md files (not committed)
    python3 scripts/brain.py rules [--team T] [--limit N]
    python3 scripts/brain.py stale [--days N]
"""
from __future__ import annotations

import argparse
import datetime as dt
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
TEAMS = ["commons", "team1-mongodb-cassandra", "team2-elastic", "team3-redis", "team4-placeholder"]
FOLDERS = {"knowledge": "knowledge", "runbooks": "runbook", "decisions": "decision"}
INBOX = "inbox"
SKIP = {"README.md", "INDEX.md"}

REQUIRED = ["title", "type", "tags", "applies_to", "last_verified", "owners"]
LIST_FIELDS = {"tags", "applies_to", "owners"}
CONFIDENCE = ["verified", "observed", "hypothesis"]
DECISION_STATUS = ["accepted", "proposed", "superseded"]
RULE_MAX = 220

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---\n", re.S)
DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
ALLOW_SECRET = "brain:allow-secret"
SECRETS = [
    ("private key", r"-----BEGIN [A-Z ]*PRIVATE KEY-----"),
    ("password", r"(?i)\b(password|passwd|pwd)\b\s*[:=]\s*(?![<$*])\S+"),
    ("S3 / access key", r"(?i)\b(secret[_-]?access[_-]?key|access[_-]?key[_-]?id|secret[_-]?key)\b\s*[:=]\s*(?![<$*])\S+"),
    ("connection string with password", r"mongodb(\+srv)?://[^/\s:@]+:(?![<$*])[^@\s]+@"),
    ("bearer token", r"(?i)\bbearer\s+[a-z0-9._\-]{20,}"),
    ("JWT", r"\beyJ[A-Za-z0-9_\-]{10,}\.eyJ[A-Za-z0-9_\-]{10,}\."),
    ("GitLab token", r"\bglpat-[A-Za-z0-9_\-]{20,}"),
    ("AWS-style access key", r"\bAKIA[0-9A-Z]{16}\b"),
    ("OpenShift token", r"\bsha256~[A-Za-z0-9_\-]{20,}"),
    ("kubeconfig credential", r"\b(client-key-data|client-certificate-data|token):\s*[A-Za-z0-9+/=._\-]{20,}"),
]
IP_ADDRESS = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")


# ---------- reading pages ----------

def read(rel: str) -> str:
    """Page text with Unix line endings, even if git checked it out with Windows (CRLF) endings."""
    return (ROOT / rel).read_text(encoding="utf-8").replace("\r\n", "\n")


def parse(text: str) -> dict | None:
    """Read the flat frontmatter block: `key: value` lines and `[a, b]` lists."""
    match = FRONTMATTER.match(text.replace("\r\n", "\n"))
    if not match:
        return None
    meta: dict = {}
    for line in match.group(1).splitlines():
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        key, sep, value = line.partition(":")
        if not sep:
            continue
        value = re.sub(r"\s+#\s.*$", "", value).strip()
        if value.startswith("[") and value.endswith("]"):
            meta[key.strip()] = [v.strip().strip("\"'") for v in value[1:-1].split(",") if v.strip()]
        else:
            meta[key.strip()] = value.strip("\"'")
    return meta


def kind_of(rel: str) -> str | None:
    """Expected `type` for a page path, or None if the path isn't a brain page."""
    parts = rel.split("/")
    if not rel.endswith(".md") or parts[-1] in SKIP:
        return None
    if len(parts) == 2 and parts[0] == INBOX:
        return "inbox"
    if len(parts) == 3 and parts[0] in TEAMS and parts[1] in FOLDERS:
        return FOLDERS[parts[1]]
    return None


def all_pages() -> list[str]:
    pages = [p.relative_to(ROOT).as_posix() for p in ROOT.glob("*/*.md")]
    pages += [p.relative_to(ROOT).as_posix() for p in ROOT.glob("*/*/*.md")]
    return sorted(p for p in pages if kind_of(p))


def load(rel: str) -> tuple[dict, str]:
    text = read(rel)
    return parse(text) or {}, text


# ---------- validate ----------

def check_page(rel: str) -> tuple[list[str], list[str]]:
    errors: list[str] = []
    warnings: list[str] = []
    expected = kind_of(rel)
    text = read(rel)
    meta = parse(text)
    if meta is None:
        return [f"{rel}: missing the header block (--- ... ---) at the top"], []

    for key in REQUIRED:
        if key not in meta:
            errors.append(f"{rel}: missing field '{key}'")
    for key in LIST_FIELDS:
        if key in meta and not isinstance(meta[key], list):
            errors.append(f"{rel}: '{key}' must be a list like [a, b]")
    if not meta.get("owners"):
        errors.append(f"{rel}: 'owners' can't be empty")
    for key, value in meta.items():
        if isinstance(value, str) and value.startswith("<") and value.endswith(">"):
            errors.append(f"{rel}: '{key}' still has the template placeholder — fill it in or delete the line")

    if meta.get("type") and meta["type"] != expected:
        errors.append(f"{rel}: type is '{meta['type']}' but pages in this folder must be '{expected}'")
    if expected == "decision":
        if meta.get("status") not in DECISION_STATUS:
            errors.append(f"{rel}: decisions need status: {' | '.join(DECISION_STATUS)}")
    elif meta.get("confidence") not in CONFIDENCE:
        errors.append(f"{rel}: confidence must be one of: {' | '.join(CONFIDENCE)}")

    when = meta.get("last_verified", "")
    if when and not DATE.match(when):
        errors.append(f"{rel}: last_verified must be YYYY-MM-DD")
    elif when and dt.date.fromisoformat(when) > dt.date.today():
        errors.append(f"{rel}: last_verified is in the future")

    rule = meta.get("rule")
    if rule is not None and (not isinstance(rule, str) or not rule or len(rule) > RULE_MAX):
        errors.append(f"{rel}: 'rule' must be one non-empty line, at most {RULE_MAX} characters")

    name = rel.rsplit("/", 1)[-1]
    if not re.fullmatch(r"[a-z0-9][a-z0-9\-]*\.md", name):
        warnings.append(f"{rel}: use lowercase-with-dashes file names")

    for number, line in enumerate(text.splitlines(), start=1):
        if ALLOW_SECRET in line:
            continue
        for label, pattern in SECRETS:
            if re.search(pattern, line):
                errors.append(f"{rel}:{number}: looks like a {label} — replace it with <REDACTED>")
        if IP_ADDRESS.search(line):
            warnings.append(f"{rel}:{number}: IP address — make sure it's OK to store")
    return errors, warnings


def validate(files: list[str] | None = None) -> int:
    pages = [f for f in files if kind_of(f)] if files else all_pages()
    errors: list[str] = []
    warnings: list[str] = []
    for rel in pages:
        e, w = check_page(rel)
        errors += e
        warnings += w
    for line in errors:
        print(f"ERROR   {line}")
    for line in warnings:
        print(f"warning {line}")
    print(f"checked {len(pages)} page(s): {len(errors)} error(s), {len(warnings)} warning(s)")
    return 1 if errors else 0


# ---------- index & rules ----------

def describe(rel: str, meta: dict) -> str:
    level = meta.get("status") if meta.get("type") == "decision" else meta.get("confidence", "?")
    scope = ", ".join(meta.get("applies_to") or []) or "general"
    return f"- `{rel}` — {meta.get('title', rel)} · {level} · {scope} · {meta.get('last_verified', '?')}"


def collect_rules(team: str = "") -> list[str]:
    ranked = []
    for rel in all_pages():
        meta, _ = load(rel)
        rule = meta.get("rule")
        if not isinstance(rule, str) or not rule:
            continue
        if team and rel.split("/")[0] not in ("commons", team, INBOX):
            continue
        level = meta.get("confidence", "")
        tags = []
        if rel.startswith(INBOX + "/"):
            tags.append("inbox, unreviewed")
        if level == "hypothesis":
            tags.append("hypothesis")
        suffix = f" [{'; '.join(tags)}]" if tags else ""
        rank = CONFIDENCE.index(level) if level in CONFIDENCE else 1
        ranked.append((rank, meta.get("last_verified", ""), f"- {rule} (`{rel}`){suffix}"))
    # Most trusted first; inside the same level, newest first (two stable sorts).
    ranked.sort(key=lambda r: r[1], reverse=True)
    ranked.sort(key=lambda r: r[0])
    return [line for _, _, line in ranked]


def write_index() -> None:
    note = "_Generated by `scripts/brain.py index` at every session start. Don't edit; not committed._"
    summary = []
    for team in TEAMS:
        if not (ROOT / team).is_dir():
            continue
        lines = [f"# {team}", "", note, ""]
        counts = []
        for folder in FOLDERS:
            pages = [p for p in all_pages() if p.startswith(f"{team}/{folder}/")]
            counts.append(str(len(pages)))
            lines.append(f"## {folder}")
            lines += [describe(p, load(p)[0]) for p in pages] or ["(none yet)"]
            lines.append("")
        (ROOT / team / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")
        summary.append(f"| {team} | {' | '.join(counts)} | `{team}/INDEX.md` |")

    inbox = [p for p in all_pages() if p.startswith(INBOX + "/")]
    lines = [
        "# Brain index", "", note, "",
        "## Quick rules", "",
        *(collect_rules() or ["(none yet)"]), "",
        "## Areas", "",
        "| Area | Knowledge | Runbooks | Decisions | Index |",
        "|---|---|---|---|---|",
        *summary, "",
        f"## Inbox ({len(inbox)} unreviewed)", "",
        *([describe(p, load(p)[0]) for p in inbox] or ["(empty)"]), "",
    ]
    (ROOT / "INDEX.md").write_text("\n".join(lines), encoding="utf-8")


def stale(days: int) -> int:
    cutoff = dt.date.today() - dt.timedelta(days=days)
    old = []
    for rel in all_pages():
        when = load(rel)[0].get("last_verified", "")
        if DATE.match(when) and dt.date.fromisoformat(when) < cutoff:
            old.append((when, rel))
    for when, rel in sorted(old):
        print(f"{when}  {rel}")
    print(f"{len(old)} page(s) not verified in the last {days} days")
    return 0


def main() -> int:
    for stream in (sys.stdout, sys.stderr):  # Windows consoles and pipes default to a non-UTF-8 code page
        if hasattr(stream, "reconfigure"):
            stream.reconfigure(encoding="utf-8", errors="replace")
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)
    p_validate = sub.add_parser("validate")
    p_validate.add_argument("files", nargs="*")
    sub.add_parser("index")
    p_rules = sub.add_parser("rules")
    p_rules.add_argument("--team", default="")
    p_rules.add_argument("--limit", type=int, default=0)
    p_stale = sub.add_parser("stale")
    p_stale.add_argument("--days", type=int, default=180)
    args = parser.parse_args()

    if args.command == "validate":
        files = [to_rel(f) for f in args.files]
        return validate(files or None)
    if args.command == "index":
        write_index()
        return 0
    if args.command == "rules":
        rules = collect_rules(args.team)
        shown = rules[: args.limit] if args.limit else rules
        print("\n".join(shown))
        if len(rules) > len(shown):
            print(f"- … {len(rules) - len(shown)} more in INDEX.md")
        return 0
    return stale(args.days)


def to_rel(path: str) -> str:
    """Accept absolute paths, paths relative to the current folder, or paths relative to the brain."""
    p = Path(path)
    if not p.is_absolute():
        here = (Path.cwd() / p).resolve()
        p = here if here.exists() and ROOT in here.parents else ROOT / p
    try:
        return p.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        sys.exit(f"{path} is not inside the brain ({ROOT})")


if __name__ == "__main__":
    sys.exit(main())
