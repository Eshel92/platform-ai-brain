# Upstream docs (offline)

Text-only copies of the vendor and open-source docs we depend on, so Claude can read them inside
the air gap. One folder per product and version.

- **What's here and which folder answers what:** `commons/knowledge/upstream-docs.md`
- **Exact source, commit, size and license per folder:** `VERSIONS.md` (generated)
- **The list of sources:** `sources.json`

Each folder has a `.upstream` file (where it came from) and the project's `LICENSE` when it has one.

Almost everything is Markdown. MongoDB (reStructuredText) and Cassandra (AsciiDoc) are converted
while syncing by `scripts/upstream_convert.py`: one self-contained `.md` per page, with includes,
generated steps and placeholders filled in.

## Don't edit by hand

These folders are replaced on every refresh. Corrections and our own findings belong in brain pages
(`<team>/knowledge/`), not here.

## Refreshing

On a machine that can reach GitHub (not in the air gap), with PyYAML installed for the MongoDB
conversion (`pip3 install pyyaml`):

```bash
python3 scripts/sync_upstream_docs.py                   # all sources
python3 scripts/sync_upstream_docs.py mck-1.7           # just one
```

On macOS with the python.org Python, add `SSL_CERT_FILE=/etc/ssl/cert.pem` if downloads fail with a
certificate error. Then bring `docs/upstream/` into the air gap and save it:

```bash
bash scripts/run.sh brain_save.py -m "docs(upstream): refresh" docs/upstream
```

To pin another version, change `ref` (and the folder `name`) in `sources.json`, then refresh.
Full steps: `docs/ADMIN.md`.
