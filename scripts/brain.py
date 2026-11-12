#!/usr/bin/env python3
"""Brain maintenance: check pages, build the index, list Quick Rules and stale pages.

Standard library only, so it runs on any workstation without pip.

    python3 scripts/brain.py validate [FILE ...]      # all pages when no file is given
    python3 scripts/brain.py index                    # writes INDEX.md files (not committed)
    python3 scripts/brain.py rules [--team T] [--limit N]
    python3 scripts/brain.py stale [--days N]
    python3 scripts/brain.py search <words> [--folder F ...] [--brain | --docs | --everything] [--limit N]
    python3 scripts/brain.py show <file> [<section>] [--from LINE] [--lines N]
"""
from __future__ import annotations

import argparse
import json
import math
import os
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


# ---------- search & show ----------

UPSTREAM = ROOT / "docs" / "upstream"
SYNONYMS = ROOT / "docs" / "search-synonyms.txt"
STOP = set("a an and are as at be by can do does for from how i if in into is it its of on or that the "
           "this to was we what when where which why will with you your".split())
WORD = re.compile(r"[a-z0-9_][a-z0-9_.\-]*[a-z0-9_]|[a-z0-9_]")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*\s*$")
HTML_HEADING = re.compile(r"^<h([1-6])\b[^>]*>\s*([^<\n]*)", re.I)


def words(text: str) -> list[str]:
    return [w for w in WORD.findall(text.lower()) if len(w) > 1 and w not in STOP]


def term_pattern(term: str) -> re.Pattern:
    """A word or phrase, as a whole word, plural allowed (snapshot = snapshots)."""
    body = r"\s+".join(re.escape(part) for part in term.split())
    return re.compile(rf"(?<![a-z0-9_]){body}(?:s|es)?(?![a-z0-9_])")


def count_word(low: str, word: str) -> int:
    return len(term_pattern(word).findall(low))


def outline(lines: list[str]) -> list[tuple[int, int, str]]:
    """(line number, level, title) of every Markdown heading outside code fences."""
    found, fenced = [], False
    for number, line in enumerate(lines, start=1):
        if line.lstrip().startswith("```"):
            fenced = not fenced
        elif not fenced and (m := HEADING.match(line)):
            found.append((number, len(m.group(1)), m.group(2)))
        elif not fenced and (m := HTML_HEADING.match(line)):
            found.append((number, int(m.group(1)), m.group(2).strip() or f"section at line {number}"))
    return found


def page_title(text: str, path: Path) -> str:
    meta = parse(text) or {}
    for key in ("title", "Title", "linkTitle"):  # Redis docs use Title
        if isinstance(meta.get(key), str) and meta[key]:
            return meta[key]
    heads = outline(text.split("\n"))
    return heads[0][2] if heads else path.stem


def synonym_groups() -> list[list[str]]:
    groups = []
    if SYNONYMS.is_file():
        for line in SYNONYMS.read_text(encoding="utf-8").splitlines():
            line = line.split("#", 1)[0].strip()
            group = [" ".join(term.lower().split()) for term in line.split(",") if term.strip()]
            if len(group) > 1:
                groups.append(group)
    return groups


def concepts(query: str) -> list[tuple[str, list[str]]]:
    """What to look for: (query word or phrase, all its alternatives). A synonym phrase in the query
    ("replica set") stays one concept; every other word becomes its own."""
    groups = synonym_groups()
    rest = " " + " ".join(query.lower().split()) + " "
    found = []
    for group in groups:
        for alt in sorted(group, key=len, reverse=True):
            if " " in alt and f" {alt} " in rest:
                found.append((alt, group))
                rest = rest.replace(f" {alt} ", " ")
                break
    for word in dict.fromkeys(words(rest)):
        alts = [word] + [a for g in groups if word in g for a in g if a != word]
        if len(word) > 3 and word.endswith("s") and not word.endswith("ss"):  # snapshots -> snapshot
            singulars = {word[:-1]} | ({word[:-2]} if word.endswith("es") and len(word) > 4 else set())
            alts = [a for a in alts if a != word] + sorted(singulars)  # a singular also matches its plural
        found.append((word, list(dict.fromkeys(alts))))
    return found


def upstream_team(folder: Path) -> str:
    try:
        return json.loads((folder / ".upstream").read_text(encoding="utf-8")).get("team", "")
    except (OSError, ValueError):
        return ""


def search_scope(folders: list[str] | None, mode: str) -> tuple[list[Path], list[Path]]:
    """(our folders, vendor-doc folders) to search."""
    vendors_all = sorted(p for p in UPSTREAM.iterdir() if p.is_dir()) if UPSTREAM.is_dir() else []
    if folders:
        ours, vendors = [], []
        for name in folders:
            name = name.rstrip("/").removeprefix("docs/upstream/")
            if (ROOT / name).is_dir() and name in TEAMS + [INBOX]:
                ours.append(ROOT / name)
            elif (UPSTREAM / name).is_dir():
                vendors.append(UPSTREAM / name)
            else:
                sys.exit(f"no folder '{name}'. Our folders: {', '.join(TEAMS)}. "
                         f"Vendor docs: {', '.join(p.name for p in vendors_all)}")
        return ours, vendors
    ours = [ROOT / t for t in TEAMS if (ROOT / t).is_dir()] + [ROOT / INBOX]
    team = os.environ.get("BRAIN_TEAM", "").strip()
    vendors = vendors_all
    if team and mode != "everything":  # commons + this team's vendor docs only
        vendors = [p for p in vendors_all if upstream_team(p) in ("commons", team, "")]
    if mode == "brain":
        vendors = []
    if mode == "docs":
        ours = []
    return ours, vendors


def search(query: str, folders: list[str] | None, mode: str, limit: int) -> int:
    wanted = concepts(query)
    if not wanted:
        sys.exit("give some search words")
    patterns = {alt: term_pattern(alt) for _, alts in wanted for alt in alts}
    ours, vendors = search_scope(folders, mode)
    files = [(p, True) for base in ours for p in sorted(base.rglob("*.md")) if p.name != "INDEX.md"]
    files += [(p, False) for base in vendors for p in sorted(base.rglob("*.md"))]
    first_words = {alt: alt.split()[0] for alt in patterns}
    hits, df = [], {label: 0 for label, _ in wanted}
    for path, own in files:
        text = path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n")
        low = text.lower()
        if not any(w in low for w in first_words.values()):
            continue
        counts = {label: sum(len(patterns[a].findall(low)) for a in alts if first_words[a] in low)
                  for label, alts in wanted}
        if not any(counts.values()):
            continue
        for label, c in counts.items():
            df[label] += 1 if c else 0
        hits.append((path, own, text, low, counts))
    total = len(files)
    if not hits:
        print(f'nothing found for "{query}" ({total} pages searched)')
        return 0

    avg = sum(len(h[3]) for h in hits) / len(hits)
    phrase = " ".join(query.lower().split())
    ranked = []
    for path, own, text, low, counts in hits:
        rel = path.relative_to(ROOT).as_posix()
        title = page_title(text, path)
        title_low, rel_low = title.lower(), rel.lower()
        score, matched = 0.0, 0
        for label, alts in wanted:
            idf = math.log(1 + (total - df[label] + 0.5) / (df[label] + 0.5))
            tf = counts[label]
            if tf:
                matched += 1
                score += idf * tf * 2.2 / (tf + 1.2 * (0.25 + 0.75 * len(low) / avg))
            if any(patterns[a].search(title_low) for a in alts):
                score += 2 * idf
            if any(a.replace(" ", "-") in rel_low for a in alts):
                score += idf
        score *= matched / len(wanted)
        if len(wanted) > 1 and phrase in low:
            score *= 1.5
        ranked.append((score, own, rel, title, text, matched))
    ranked.sort(key=lambda r: -r[0])

    alts_all = [a for _, alts in wanted for a in alts]
    expanded = [f"{label} = {', '.join(alts[1:4])}" for label, alts in wanted if len(alts) > 1]
    print(f'Search "{query}": {total} pages ({len(ours)} of our folders, {len(vendors)} vendor-doc folders)')
    if expanded:
        print(f"Also matching: {'; '.join(expanded)}")
    enough = max(1, (len(wanted) + 1) // 2)  # our pages must match at least half the search words
    own_hits = [r for r in ranked if r[1] and r[5] >= enough][: (limit if not vendors else min(3, limit))]
    vendor_hits = [r for r in ranked if not r[1]][: limit - len(own_hits)]
    number = 0
    for heading, group in (("Our pages", own_hits), ("Vendor docs", vendor_hits)):
        if not group:
            continue
        print(f"{heading}:")
        for score, own, rel, title, text, _ in group:
            number += 1
            print(f" {number}. {rel}  [{max(1, len(text) // 1000)} KB]")
            print(f"    {title[:110]}")
            line_no, line = best_line(text, title, alts_all)
            if line_no:
                print(f"    L{line_no}: {line[:130]}")
    print('Next: brain.py show <path> for the outline, show <path> "<section>" for one section.')
    return 0


def best_line(text: str, title: str, alts: list[str]) -> tuple[int, str]:
    best, found = -1.0, (0, "")
    body_start = text.find("\n---", 3) + 4 if text.startswith("---") else 0  # skip the header block
    offset = text.count("\n", 0, body_start)
    for line_no, line in enumerate(text[body_start:].split("\n"), start=offset + 1):
        if line.lstrip("# ").strip() == title or line.startswith("<!--"):  # title / converter note
            continue
        ll = line.lower()
        present = sum(1 for a in alts if a in ll) + (0.5 if line.startswith("#") else 0)
        if present >= 1 and present > best:
            best, found = present, (line_no, line.strip())
    return found


def show(file: str, section: str | None, start: int | None, count: int) -> int:
    path = Path(file)
    if not path.is_absolute():
        path = path if path.is_file() else ROOT / file
    if not path.is_file():
        sys.exit(f"no such file: {file}")
    lines = path.read_text(encoding="utf-8", errors="replace").replace("\r\n", "\n").split("\n")
    try:
        rel = path.resolve().relative_to(ROOT).as_posix()
    except ValueError:
        rel = str(path)
    heads = outline(lines)

    if start is None and section is None:  # outline only
        size = sum(len(l) + 1 for l in lines)
        print(f"{rel}: {len(lines)} lines, {max(1, size // 1000)} KB, {len(heads)} headings")
        for number, level, title in heads[:80]:
            print(f"  L{number:<6}{'  ' * (level - 1)}{title[:120]}")
        if len(heads) > 80:
            print(f'  … {len(heads) - 80} more headings: use show <path> "<words>" to jump to one')
        return 0

    if start is not None:
        first, last = max(start, 1), min(max(start, 1) + count - 1, len(lines))
    else:
        want = section.lower()
        match = next((h for h in heads if want in h[2].lower()), None)
        if match:
            first = match[0]
            nxt = next((h for h in heads if h[0] > first and h[1] <= match[1]), None)
            last = (nxt[0] - 1) if nxt else len(lines)
        else:
            hit = next((n for n, l in enumerate(lines, start=1) if want in l.lower()), None)
            if hit is None:
                print(f'"{section}" not found in {rel}. Run show {rel} for the outline.')
                return 1
            first, last = max(hit - 5, 1), len(lines)
        last = min(last, first + count - 1)
    print(f"{rel}: lines {first}-{last} of {len(lines)}")
    print("\n".join(lines[first - 1:last]))
    if last < len(lines):
        print(f"… more: show {rel} --from {last + 1}")
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
    p_search = sub.add_parser("search", help="rank pages by how well they match some words")
    p_search.add_argument("query", nargs="+")
    p_search.add_argument("--folder", action="append", help="a team folder or a docs/upstream folder (repeatable)")
    p_search.add_argument("--brain", dest="mode", action="store_const", const="brain", help="only our pages")
    p_search.add_argument("--docs", dest="mode", action="store_const", const="docs", help="only vendor docs")
    p_search.add_argument("--everything", dest="mode", action="store_const", const="everything",
                          help="ignore BRAIN_TEAM and search every vendor-doc folder")
    p_search.add_argument("--limit", type=int, default=10)
    p_show = sub.add_parser("show", help="print a page's outline, one section, or a range of lines")
    p_show.add_argument("file")
    p_show.add_argument("section", nargs="?")
    p_show.add_argument("--from", dest="start", type=int)
    p_show.add_argument("--lines", type=int, default=120)
    args = parser.parse_args()

    if args.command == "search":
        return search(" ".join(args.query), args.folder, args.mode or "all", args.limit)
    if args.command == "show":
        return show(args.file, args.section, args.start, args.lines)

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
