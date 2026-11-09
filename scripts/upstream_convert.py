"""Turn upstream docs into self-contained Markdown pages while syncing.

- MongoDB docs (reStructuredText, "snooty"): includes, generated steps/extracts (YAML) and
  substitutions are inlined, so one .md file is one complete page.
- Cassandra docs (AsciiDoc, Antora): includes inlined, headings, code blocks and notes converted.

Unknown markup is kept as text rather than dropped: the goal is pages Claude can read in one go,
not perfect rendering. Used by sync_upstream_docs.py. PyYAML is needed for MongoDB's generated
steps and extracts (pip3 install pyyaml); without it those spots get a short note instead.
"""
from __future__ import annotations

import re
import textwrap
from pathlib import Path

try:
    import yaml
except ImportError:  # only the machine that refreshes docs needs it
    yaml = None

try:
    import tomllib
except ImportError:  # Python < 3.11
    tomllib = None


def indent_of(line: str) -> int:
    return len(line) - len(line.lstrip(" "))


def take_block(lines: list[str], start: int, base: int) -> tuple[list[str], int]:
    """Lines after `start` that are blank or indented deeper than `base`; trailing blanks stay outside."""
    end = start
    while end < len(lines) and (not lines[end].strip() or indent_of(lines[end]) > base):
        end += 1
    while end > start and not lines[end - 1].strip():
        end -= 1
    return lines[start:end], end


def dedent(lines: list[str]) -> list[str]:
    return textwrap.dedent("\n".join(lines)).split("\n") if lines else []


def split_options(body: list[str]) -> tuple[dict, list[str]]:
    """Leading `:key: value` lines of a directive body."""
    options, i = {}, 0
    while i < len(body):
        m = re.match(r"^:([\w-]+):\s*(.*)$", body[i])
        if not m:
            break
        options[m.group(1)] = m.group(2).strip()
        i += 1
    return options, body[i:]


# ---------------------------------------------------------------- MongoDB reStructuredText

INCLUDE = re.compile(r"^(?P<ind>[ \t]*)\.\. (?P<kind>include|sharedinclude|literalinclude)::[ \t]*(?P<arg>\S+)[ \t]*$")
DIRECTIVE = re.compile(r"^(?P<ind>\s*)\.\. (?P<name>[\w:-]+)::(?:[ \t]+(?P<arg>.*?))?\s*$")
SUBST_DEF = re.compile(r"^\s*\.\. \|(?P<name>[^|]+)\| replace::\s*(?P<value>.*)$")
ADORN = re.compile(r"^([=\-~^\"`'*+#])\1{2,}\s*$")
PLAIN_ROLES = {"ref", "doc", "term", "abbr", "guilabel", "manual", "atlas", "products", "github", "issue",
               "website", "wikipedia", "rfc", "dl", "gold", "red", "green", "blue", "icon", "icon-fa5"}
ADMONITIONS = {"note": "Note", "warning": "Warning", "important": "Important", "tip": "Tip",
               "caution": "Caution", "danger": "Danger", "seealso": "See also", "see": "See also",
               "example": "Example", "versionadded": "New in version", "versionchanged": "Changed in version",
               "deprecated": "Deprecated since version", "admonition": "", "optional": "Optional"}
DROP = {"meta", "facet", "contents", "default-domain", "toctree", "index", "raw", "banner", "class",
        "cssclass", "rst-class", "replacement", "kicker", "instruqt", "video", "youtube", "card-group",
        "landing:card-group", "landing:introduction", "include"}
CONTAINERS = {"io-code-block", "procedure", "tabs", "tabs-drivers", "tabs-platforms", "tabs-selector",
              "tabs-pillstrip", "tabs-cloud", "tabs-deployments", "container", "only", "cond", "hlist",
              "selected-content", "collapsible", "wayfinding", "composable-tutorial", "blockquote",
              "list-table-wrapper", "topic", "sidebar", "step-wrapper"}
CODE = {"code-block", "code", "sourcecode", "input", "output"}


class RstConverter:
    """Converts one MongoDB `source/` folder (a sparse checkout, so code examples are present too)."""

    def __init__(self, source: Path):
        self.src = source
        self.subs: dict[str, str] = {}
        self.consts: dict[str, str] = {}
        self.yaml_files: dict[str, dict] = {}
        self.extracts: dict[str, tuple[str, dict]] = {}
        self.steps: dict[str, tuple[str, list]] = {}
        self.levels: list[tuple[str, bool]] = []
        self.step_number = 0
        self.notes: set[str] = set()
        self._load_settings()
        self._load_yaml()

    def _load_settings(self) -> None:
        toml = self.src.parent / "snooty.toml"
        if tomllib and toml.is_file():
            try:
                data = tomllib.loads(toml.read_text(encoding="utf-8"))
            except (tomllib.TOMLDecodeError, UnicodeDecodeError):
                return
            self.consts = {k: str(v) for k, v in (data.get("constants") or {}).items()}
            self.subs = {k: str(v) for k, v in (data.get("substitutions") or {}).items()}

    def _load_yaml(self) -> None:
        if yaml is None:
            self.notes.add("PyYAML not installed: generated steps and extracts were skipped")
            return
        for f in sorted((self.src / "includes").rglob("*.yaml")):
            try:
                docs = [d for d in yaml.safe_load_all(f.read_text(encoding="utf-8")) if isinstance(d, dict)]
            except Exception:  # a broken upstream YAML file shouldn't stop the sync
                continue
            self.yaml_files[f.name] = {d["ref"]: d for d in docs if isinstance(d.get("ref"), str)}
            if f.name.startswith("steps-"):
                self.steps[f.stem[len("steps-"):]] = (f.name, docs)
            elif f.name.startswith("extracts-"):
                for d in docs:
                    if isinstance(d.get("ref"), str):
                        self.extracts[d["ref"]] = (f.name, d)

    # ---- pages

    def pages(self) -> list[Path]:
        return sorted(p for p in self.src.rglob("*.txt") if "includes" not in p.relative_to(self.src).parts)

    def convert_page(self, page: Path) -> str:
        self.levels, self.step_number = [], 0
        text = self.expand(page.read_text(encoding="utf-8", errors="replace"), page, 0)
        text = self.substitute(text)
        body = "\n".join(self.block(text.split("\n")))
        body = self.inline(body)
        body = re.sub(r"\n{3,}", "\n\n", body).strip()
        rel = page.relative_to(self.src).as_posix()
        return f"<!-- Converted from {rel} (reStructuredText). Includes are inlined. -->\n\n{body}\n"

    # ---- includes

    def resolve(self, arg: str, current: Path) -> Path | None:
        rel = arg.lstrip("/")
        # Absolute paths start at source/; shared folders such as content/code-examples sit a few levels up.
        bases = [self.src, *list(self.src.parents)[:3]] if arg.startswith("/") else [current.parent]
        for base in bases:
            for candidate in (base / rel, base / f"{rel}.rst", base / f"{rel}.txt"):
                if candidate.is_file():
                    return candidate
        return None

    def expand(self, text: str, current: Path, depth: int) -> str:
        lines, out, i = text.split("\n"), [], 0
        while i < len(lines):
            m = INCLUDE.match(lines[i])
            if not m:
                out.append(lines[i])
                i += 1
                continue
            ind = m.group("ind")
            body, i = take_block(lines, i + 1, len(ind))
            options, rest = split_options(dedent(body))
            content = self.include_text(m.group("kind"), m.group("arg"), current, options, depth)
            for name, value in self.replacements(rest).items():
                content = content.replace(f"|{name}|", value)
            out.extend(ind + l if l.strip() else "" for l in content.split("\n"))
        return "\n".join(out)

    @staticmethod
    def replacements(lines: list[str]) -> dict[str, str]:
        found, i = {}, 0
        while i < len(lines):
            m = re.match(r"^\s*\.\. replacement::\s*(\S+)", lines[i])
            if m:
                block, i = take_block(lines, i + 1, indent_of(lines[i]))
                found[m.group(1)] = "\n".join(dedent(block)).strip()
            else:
                i += 1
        return found

    def include_text(self, kind: str, arg: str, current: Path, options: dict, depth: int) -> str:
        if kind == "sharedinclude":
            return f"(Text shared from another MongoDB docs repo, not available offline: {arg})"
        path = self.resolve(arg, current)
        if kind == "literalinclude":
            if not path:
                return f"(Code example not available offline: {arg})"
            code = self.cut(path.read_text(encoding="utf-8", errors="replace"), options)
            lang = options.get("language", "")
            return f".. code-block:: {lang}\n\n" + textwrap.indent(code, "   ")
        if depth > 8:
            return f"(Include nested too deep: {arg})"
        if path:
            return self.expand(path.read_text(encoding="utf-8", errors="replace"), path, depth + 1)
        generated = self.generated(arg)
        if generated is not None:
            return self.expand(generated, self.src / "includes" / "generated.rst", depth + 1)
        return f"(Include not available offline: {arg})"

    @staticmethod
    def cut(code: str, options: dict) -> str:
        if options.get("start-after") and options["start-after"] in code:
            code = code.split(options["start-after"], 1)[1].split("\n", 1)[-1]
        if options.get("end-before") and options["end-before"] in code:
            code = code.split(options["end-before"], 1)[0].rsplit("\n", 1)[0]
        if options.get("lines"):
            keep, lines = set(), code.split("\n")
            for part in options["lines"].split(","):
                a, _, b = part.strip().partition("-")
                if a.isdigit():
                    keep.update(range(int(a), (int(b) if b.isdigit() else len(lines)) + 1))
            code = "\n".join(l for n, l in enumerate(lines, 1) if n in keep)
        return textwrap.dedent(code).strip("\n")

    # ---- generated includes (YAML)

    def generated(self, arg: str) -> str | None:
        m = re.match(r"^/?includes/extracts/(.+?)\.rst$", arg)
        if m:
            entry = self.extracts.get(m.group(1))
            return self.render_extract(*entry) if entry else None
        m = re.match(r"^/?includes/steps/(.+?)\.rst$", arg)
        if m:
            entry = self.steps.get(m.group(1))
            return self.render_steps(*entry) if entry else None
        return None

    def merged(self, doc: dict, filename: str, depth: int = 0) -> dict:
        parent = doc.get("inherit") or doc.get("source")
        if isinstance(parent, dict) and depth < 6:
            base_file = parent.get("file", filename)
            base = self.yaml_files.get(base_file, {}).get(parent.get("ref"))
            if base:
                result = dict(self.merged(base, base_file, depth + 1))
                replacement = dict(result.get("replacement") or {})
                replacement.update(doc.get("replacement") or {})
                result.update({k: v for k, v in doc.items() if k not in ("inherit", "source")})
                result["replacement"] = replacement
                return result
        return doc

    @staticmethod
    def fill(text, replacement: dict) -> str:
        text = "" if text is None else str(text)
        for key, value in (replacement or {}).items():
            text = text.replace("{{" + str(key) + "}}", str(value))
        return text

    def render_extract(self, filename: str, doc: dict) -> str:
        d = self.merged(doc, filename)
        return self.fill(d.get("content"), d.get("replacement"))

    def render_steps(self, filename: str, docs: list) -> str:
        parts = []
        for number, doc in enumerate(docs, 1):
            d = self.merged(doc, filename)
            rep = d.get("replacement")
            title = d.get("title")
            title = title.get("text", "") if isinstance(title, dict) else title
            parts.append(f"**Step {d.get('stepnum', number)}: {self.fill(title, rep)}**\n")
            for key in ("pre", "content"):
                if d.get(key):
                    parts.append(self.fill(d[key], rep) + "\n")
            actions = d.get("action") or []
            for action in actions if isinstance(actions, list) else [actions]:
                if not isinstance(action, dict):
                    continue
                if action.get("pre"):
                    parts.append(self.fill(action["pre"], rep) + "\n")
                if action.get("code"):
                    code = textwrap.indent(self.fill(action["code"], rep).rstrip(), "   ")
                    parts.append(f".. code-block:: {action.get('language', '')}\n\n{code}\n")
                if action.get("post"):
                    parts.append(self.fill(action["post"], rep) + "\n")
            if d.get("post"):
                parts.append(self.fill(d["post"], rep) + "\n")
        return "\n".join(parts)

    # ---- substitutions

    ICONS = {"arrow": "→", "checkmark": "✓", "xmark": "✗", "check": "✓", "x": "✗"}

    def substitute(self, text: str) -> str:
        local = {**self.ICONS, **self.subs}
        kept = []
        for line in text.split("\n"):
            m = SUBST_DEF.match(line)
            if m:
                local[m.group("name")] = m.group("value").strip()
            else:
                kept.append(line)
        text = "\n".join(kept)
        for _ in range(3):  # values can refer to other substitutions
            text = re.sub(r"\|([\w.\-]+(?: [\w.\-]+)*)\|", lambda m: local.get(m.group(1), m.group(0)), text)
        return re.sub(r"\{\+([\w.\-]+)\+\}", lambda m: self.consts.get(m.group(1), m.group(0)), text)

    # ---- blocks

    def heading(self, char: str, overline: bool, title: str) -> list[str]:
        style = (char, overline)
        if style not in self.levels:
            self.levels.append(style)
        level = min(self.levels.index(style) + 1, 6)
        return ["", "#" * level + " " + title.strip(), ""]

    def block(self, lines: list[str]) -> list[str]:
        out, i = [], 0
        while i < len(lines):
            line = lines[i]
            nxt = lines[i + 1] if i + 1 < len(lines) else ""
            if ADORN.match(line) and i + 2 < len(lines) and nxt.strip() and ADORN.match(lines[i + 2]) \
                    and lines[i + 2].strip()[0] == line.strip()[0]:
                out += self.heading(line.strip()[0], True, nxt)
                i += 3
                continue
            if line.strip() and not line[0].isspace() and ADORN.match(nxt) and not ADORN.match(line) \
                    and len(nxt.strip()) >= min(len(line.strip()), 3):
                out += self.heading(nxt.strip()[0], False, line)
                i += 2
                continue
            m = DIRECTIVE.match(line)
            if m:
                ind = m.group("ind")
                body, i = take_block(lines, i + 1, len(ind))
                options, body = split_options(dedent(body))
                converted = self.directive(m.group("name"), (m.group("arg") or "").strip(), options, body)
                out += [ind + l if l.strip() else "" for l in converted]
                continue
            if line.lstrip().startswith(".. "):  # comment or link target: drop it and its block
                _, i = take_block(lines, i + 1, indent_of(line))
                continue
            if line.rstrip().endswith("::") and not line.lstrip().startswith(".."):
                body, end = take_block(lines, i + 1, indent_of(line))
                if any(l.strip() for l in body):
                    text = line.rstrip()[:-2].rstrip()
                    if text.strip():
                        out.append(text + ":")
                    out += self.fence("", dedent(body), line[: indent_of(line)])
                    i = end
                    continue
            out.append(line)
            i += 1
        return out

    @staticmethod
    def fence(lang: str, body: list[str], ind: str = "") -> list[str]:
        while body and not body[0].strip():
            body = body[1:]
        return ["", f"{ind}```{lang}", *[ind + l if l.strip() else "" for l in body], f"{ind}```", ""]

    def directive(self, name: str, arg: str, options: dict, body: list[str]) -> list[str]:
        short = name.split(":")[-1]
        if short in CODE:
            lang = arg if short in ("code-block", "code", "sourcecode") else options.get("language", "")
            label = ["Output:"] if short == "output" else []
            return label + self.fence(lang or options.get("language", ""), body)
        if short in DROP:
            return []
        if short == "procedure":
            self.step_number = 0
            return self.block(body)
        if short == "step":
            self.step_number += 1
            return ["", f"**Step {self.step_number}: {arg}**", ""] + self.block(body)
        if short == "tab":
            return ["", f"**{options.get('tabid', arg) or 'Tab'}:**", ""] + self.block(body)
        if short in CONTAINERS:
            return self.block(body)
        if short in ADMONITIONS:
            label = ADMONITIONS[short] or arg
            head = f"**{label}:** {arg}".rstrip() if ADMONITIONS[short] else f"**{label}**"
            return ["", head, ""] + self.block(body) + [""]
        if short == "list-table":
            return self.table(body, options)
        if short in ("figure", "image"):
            return [f"(Figure: {arg})"] + self.block(body)
        if short == "rubric":
            return ["", f"**{arg}**", ""]
        if short in ("literalinclude", "sharedinclude"):
            return [f"(Not available offline: {arg})"]
        if arg:  # API objects (data, method, setting, parameter, dbcommand, ...) and anything unknown
            return ["", f"**`{arg}`**" if short not in ("card", "button") else f"**{arg}**", ""] + self.block(body)
        return self.block(body)

    def table(self, body: list[str], options: dict) -> list[str]:
        rows, cell = [], None
        for line in body:
            m = re.match(r"^\*\s+-\s?(.*)$", line)
            n = re.match(r"^\s{2}-\s?(.*)$", line)
            if m:
                rows.append([[m.group(1)]])
            elif n and rows:
                rows[-1].append([n.group(1)])
            elif rows:
                rows[-1][-1].append(line[4:] if line.startswith("    ") else line.strip())
        simple = rows and all(
            all(not any(l.lstrip().startswith(("..", "* ", "- ")) for l in c[1:]) for c in r) for r in rows)
        if not simple:
            return self.block(body)
        flat = [[" ".join(l.strip() for l in c if l.strip()).replace("|", "\\|") for c in r] for r in rows]
        width = max(len(r) for r in flat)
        flat = [r + [""] * (width - len(r)) for r in flat]
        header = flat[0] if options.get("header-rows", "0").strip() not in ("", "0") else [""] * width
        data = flat[1:] if header != [""] * width else flat
        out = ["", "| " + " | ".join(header) + " |", "|" + "---|" * width]
        out += ["| " + " | ".join(r) + " |" for r in data]
        return out + [""]

    # ---- inline markup

    @staticmethod
    def inline(text: str) -> str:
        parts = re.split(r"(^\s*```.*?^\s*```\s*$)", text, flags=re.S | re.M)
        for k in range(0, len(parts), 2):  # outside code fences only
            t = parts[k]
            t = re.sub(r"``(.+?)``", r"`\1`", t)

            def role(m: re.Match) -> str:
                kind, value = m.group(1).split(":")[-1], m.group(2)
                if value.endswith(">") and "<" in value:
                    shown = value[: value.rfind("<")].strip()
                    value = shown or value[value.rfind("<") + 1:-1]
                elif value.startswith("~"):
                    value = value[1:].split(".")[-1]
                value = value.replace("\\", "")
                return value if kind in PLAIN_ROLES else f"`{value}`"

            t = re.sub(r":((?:[\w-]+:)*[\w-]+):`([^`]+)`", role, t)
            t = re.sub(r"`([^`<]+?)\s*<([^`>\s]+)>`__?", lambda m: f"[{' '.join(m.group(1).split())}]({m.group(2)})", t)
            t = re.sub(r"`([^`\n]+)`_\b_?", r"\1", t)
            t = t.replace("\\ ", "")
            parts[k] = t
        return "".join(parts)


# ---------------------------------------------------------------- Cassandra AsciiDoc (Antora)

class AdocConverter:
    """Converts an Antora `doc/` folder: modules/<module>/pages/**/*.adoc become <module>/<page>.md."""

    ADMON = {"NOTE": "Note", "TIP": "Tip", "IMPORTANT": "Important", "WARNING": "Warning", "CAUTION": "Caution"}

    def __init__(self, source: Path):
        self.src = source
        self.notes: set[str] = set()

    def pages(self) -> list[Path]:
        return sorted(p for p in self.src.glob("modules/*/pages/**/*.adoc"))

    def out_name(self, page: Path) -> str:
        rel = page.relative_to(self.src / "modules")
        return (Path(rel.parts[0]) / Path(*rel.parts[2:])).with_suffix(".md").as_posix()

    def resolve(self, target: str, page: Path) -> Path | None:
        module = page.relative_to(self.src / "modules").parts[0]
        m = re.match(r"^(?:[\w-]+:)?(?:([\w-]+):)?(partial|example|page|attachment)\$(.+)$", target)
        if m:
            folder = {"partial": "partials", "example": "examples", "page": "pages", "attachment": "attachments"}
            path = self.src / "modules" / (m.group(1) or module) / folder[m.group(2)] / m.group(3)
        else:
            path = page.parent / target
        return path if path.is_file() else None

    def expand(self, text: str, page: Path, depth: int = 0) -> str:
        def include(m: re.Match) -> str:
            path = self.resolve(m.group(1), page)
            if not path or depth > 6:
                return f"(Include not available offline: {m.group(1)})"
            body = path.read_text(encoding="utf-8", errors="replace")
            tags = re.search(r"tags?=([\w;,-]+)", m.group(2))
            if tags:
                picked = []
                for tag in re.split(r"[;,]", tags.group(1)):
                    found = re.search(rf"tag::{re.escape(tag)}\[\]\s*\n(.*?)\n.*?end::{re.escape(tag)}\[\]", body, re.S)
                    if found:
                        picked.append(found.group(1))
                body = "\n".join(picked) or body
            body = "\n".join(l for l in body.split("\n") if not re.search(r"(tag|end)::[\w-]+\[\]", l))
            return self.expand(body, path if path.suffix == ".adoc" else page, depth + 1)

        return re.sub(r"^include::([^\[]+)\[([^\]]*)\]\s*$", include, text, flags=re.M)

    def convert_page(self, page: Path) -> str:
        text = self.expand(page.read_text(encoding="utf-8", errors="replace"), page)
        attrs, out, fence, admon, lang = {}, [], None, None, ""
        for line in text.split("\n"):
            if fence:
                if line.strip() == fence:
                    out.append("```")
                    fence = None
                else:
                    out.append(line)
                continue
            m = re.match(r"^:([\w-]+):\s*(.*)$", line)
            if m:
                attrs[m.group(1)] = m.group(2)
                continue
            if re.match(r"^\[source,\s*([\w+-]+).*\]$", line.strip()):
                lang = re.match(r"^\[source,\s*([\w+-]+)", line.strip()).group(1)
                continue
            if line.strip() in ("----", "...."):
                out.append(f"```{lang}")
                fence, lang = line.strip(), ""
                continue
            m = re.match(r"^\[(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]$", line.strip())
            if m:
                admon = self.ADMON[m.group(1)]
                continue
            if line.strip() == "====":  # admonition or example block delimiter
                if admon == "open":
                    admon = None
                elif admon:
                    out += ["", f"**{admon}:**"]
                    admon = "open"
                continue
            if re.match(r"^\[[^\]]*\]$", line.strip()) or line.startswith("//") or re.match(r"^(ifdef|ifndef|endif)::", line):
                continue
            m = re.match(r"^(=+)\s+(.*)$", line)
            if m:
                out += ["", "#" * min(len(m.group(1)), 6) + " " + m.group(2), ""]
                continue
            m = re.match(r"^(NOTE|TIP|IMPORTANT|WARNING|CAUTION):\s*(.*)$", line)
            if m:
                out.append(f"**{self.ADMON[m.group(1)]}:** {m.group(2)}")
                continue
            if line.startswith("image::"):
                out.append(f"(Figure: {line[7:].split('[')[0]})")
                continue
            out.append(self.inline(line, attrs))
        body = re.sub(r"\n{3,}", "\n\n", "\n".join(out)).strip()
        rel = page.relative_to(self.src).as_posix()
        return f"<!-- Converted from {rel} (AsciiDoc). Includes are inlined. -->\n\n{body}\n"

    @staticmethod
    def inline(line: str, attrs: dict) -> str:
        line = re.sub(r"\{([\w-]+)\}", lambda m: attrs.get(m.group(1), m.group(0)), line)
        line = re.sub(r"xref:([^\[\s]+)\[([^\]]*)\]", lambda m: m.group(2) or m.group(1), line)
        line = re.sub(r"(?:link:)?(https?://[^\[\s]+)\[([^\]]*)\]", lambda m: f"[{m.group(2) or m.group(1)}]({m.group(1)})", line)
        line = re.sub(r"<<([^,>]+),\s*([^>]+)>>", r"\2", line)
        line = re.sub(r"<<([^>]+)>>", r"\1", line)
        return re.sub(r"\+\+?([^+\n]+?)\+\+?", r"\1", line)


def convert_tree(kind: str, source: Path, out: Path) -> tuple[int, set[str]]:
    """Convert every page under `source` into `out`. Returns (pages written, notes)."""
    converter = RstConverter(source) if kind == "rst" else AdocConverter(source)
    count = 0
    for page in converter.pages():
        if kind == "rst":
            target = out / page.relative_to(source).with_suffix(".md")
        else:
            target = out / converter.out_name(page)
        target.parent.mkdir(parents=True, exist_ok=True)
        try:
            target.write_text(converter.convert_page(page), encoding="utf-8")
        except Exception as error:  # one odd page shouldn't stop the sync; keep its raw text
            target.write_text(f"<!-- Conversion failed ({error}); raw source follows. -->\n\n"
                              + page.read_text(encoding="utf-8", errors="replace"), encoding="utf-8")
            converter.notes.add(f"raw fallback for {page.name}")
        count += 1
    return count, converter.notes
