# Upstream docs (offline)

Text-only copies of the vendor and open-source docs we depend on, so Claude can read them inside
the air gap. One folder per product and version.

- **What's here and which folder answers what:** `commons/knowledge/upstream-docs.md`
- **Exact source, commit, size and license per folder:** `VERSIONS.md` (generated)
- **The list of sources:** `sources.json`

Each folder has a `.upstream` file (where it came from) and the project's `LICENSE` when it has one.

Almost everything is Markdown. MongoDB (reStructuredText), Cassandra and Elastic 8.x (AsciiDoc) are
converted while syncing by `scripts/upstream_convert.py`: one self-contained `.md` per page, with
includes, generated steps and placeholders filled in.

## Don't edit by hand

These folders are replaced on every refresh. Corrections and our own findings belong in brain pages
(`<team>/knowledge/`), not here.

## Adding new vendor docs

Everything except the last step runs on a machine that can reach GitHub (not in the air gap).

### 1. Find the docs

- **The repo and folder.** Most projects keep their docs in their main repo (`docs/`,
  `docs/reference/`, `content/…`). Some have a separate docs repo (`mongodb/docs`, `redis/docs`,
  `elastic/docs-content`).
- **The version.** Pick the branch or tag that matches what we run:
  ```bash
  git ls-remote --heads https://github.com/<org>/<repo> | grep -E 'release|[0-9]+\.[0-9]+'
  git ls-remote --tags  https://github.com/<org>/<repo> | tail -20
  ```
  Many docs repos keep older versions as folders on `main` instead (Redis: `rs/7.22/`).
- **The format.** Markdown is copied as is. reStructuredText and AsciiDoc get converted (step 3).
- **The license** (the repo's `LICENSE` or README). If it says **NoDerivatives** (as Elastic's 9.x
  guides do), don't convert: copy the files as they are. Non-commercial licenses are fine for
  internal use.

### 2. Check the size first

Keep each source light, ideally **under ~15 MB of text**. Leave out other products, generated
reference pages (thousands of tiny files) and archived versions you don't run. To measure a folder
without downloading the whole repo:

```bash
git clone --depth 1 --filter=blob:none --sparse -b <ref> https://github.com/<org>/<repo> /tmp/peek
git -C /tmp/peek sparse-checkout set <docs folder>
du -sh /tmp/peek/<docs folder>; find /tmp/peek/<docs folder> -name '*.md' | wc -l
du -sh /tmp/peek/<docs folder>/* | sort -h | tail       # the biggest subfolders, to decide what to leave out
rm -rf /tmp/peek
```

### 3. Add an entry to `sources.json`

```json
{
  "name": "redis-enterprise-software",
  "team": "team3-redis",
  "about": "Redis Enterprise Software: current docs, the 7.22 docs and release notes from 7.2 on",
  "repo": "redis/docs",
  "ref": "main",
  "paths": ["content/operate/rs"],
  "convert": "md",
  "checkout": ["content/embeds"],
  "exclude": ["7.4/*", "7.8/*", "release-notes/rs-6-*"]
}
```

| Field | Needed | What it is |
|---|---|---|
| `name` | yes | Folder name under `docs/upstream/`. Put the version in it when it's pinned (`mck-1.7`) |
| `team` | yes | `commons` or the team folder that owns it |
| `about` | yes | One line: what it covers. Shown in `VERSIONS.md` |
| `repo` | yes | `org/repo` (on GitHub, or the same path on `UPSTREAM_GIT_BASE`) |
| `ref` | yes | Branch or tag |
| `paths` | yes | Docs folder(s) in the repo. With several, each lands in its own subfolder |
| `include` / `exclude` | no | Patterns on paths inside those folders, e.g. `"esql/*"`, `"*powerflex*"` |
| `convert` | no | `rst` (MongoDB-style reStructuredText), `adoc` (Antora AsciiDoc, like Cassandra), `asciidoc` (plain AsciiDoc, like Elastic 8.x), `md` (Markdown with `{{placeholders}}` or shared snippets). Leave it out to copy files as they are |
| `checkout` | no | Extra repo folders needed only while converting (shared snippets, code examples) |
| `attrs` | no | Values for placeholders the converter doesn't know, e.g. `{"version.stack": "9.x"}` |
| `root_files` | no | Extra files from the repo root, e.g. `["README.md"]` |
| `extra_extensions` | no | File types beyond `.md .rst .adoc .txt .yaml`, e.g. `[".cue"]` |
| `license` | no | The license, when the repo has no `LICENSE` file |

### 4. Download and check it

```bash
pip3 install pyyaml                                   # once; needed for convert: rst and md
python3 scripts/sync_upstream_docs.py <name>          # prints files, size, license, commit
```

On macOS with the python.org Python, add `SSL_CERT_FILE=/etc/ssl/cert.pem` if it fails with a
certificate error. Then check the result:

- Open two or three pages: are they readable, with no big holes?
- Search it: `bash scripts/run.sh brain.py search <words you'd ask> --folder <name>`. The right page
  should be near the top.
- Leftover placeholders: `grep -rhoE '\{[a-z][a-z0-9.-]+\}' docs/upstream/<name> | sort | uniq -c | sort -rn | head`.
  Fill common ones with `attrs` and run the download again.
- Huge pages: `find docs/upstream/<name> -name '*.md' -size +200k`. These are fine (Claude reads them by
  section), but if most of the size is one kind of generated page, `exclude` it.

If a download fails, the old folder stays as it was. Fix `sources.json` and run it again.

### 5. Tell Claude about it

- Add a row to `commons/knowledge/upstream-docs.md`: which questions it answers, the docs version, and
  how that compares to what we run (`[UNKNOWN]` if you don't know).
- If the license isn't in a `LICENSE` file in the folder, add a line to `NOTICE`.

### 6. Bring it into the air gap and save it

Copy `docs/upstream/<name>/`, `docs/upstream/sources.json` and `docs/upstream/VERSIONS.md` into your
clone, along with the catalog page, then:

```bash
bash scripts/run.sh brain_save.py -m "docs(upstream): add <name>" docs/upstream commons/knowledge/upstream-docs.md
```

**To remove a source:** delete its entry in `sources.json` and its folder, run
`python3 scripts/sync_upstream_docs.py --versions`, remove its row from the catalog page, and save.

## Refreshing

```bash
python3 scripts/sync_upstream_docs.py                   # all sources
python3 scripts/sync_upstream_docs.py mck-1.7           # just one
```

Then bring `docs/upstream/` into the air gap and save it:

```bash
bash scripts/run.sh brain_save.py -m "docs(upstream): refresh" docs/upstream
```

To move to another version, change `ref` (and the folder `name`) in `sources.json`, refresh, delete
the old folder and update the catalog page.
