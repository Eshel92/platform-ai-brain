# Page header reference

Every `.md` file in `<team>/knowledge/`, `<team>/runbooks/`, `<team>/decisions/` and `inbox/` (except
`README.md` and `INDEX.md`) starts with this block. `scripts/brain.py validate` enforces it, and
`scripts/brain_save.py` refuses to push a page that fails.

```yaml
---
title: MongoDB member stuck in STARTUP2 after resync
type: knowledge
tags: [mongodb, resync]
applies_to: [mck-1.10, mongo-8.0, ocp-4.18]
confidence: observed
last_verified: 2026-11-08
owners: [team1]
source: claude-session
rule: Member stuck in STARTUP2 after resync → check the oplog window before restarting
---
```

## Fields

| Field | Required | Format | Notes |
|---|---|---|---|
| `title` | yes | text | What someone would search for during an incident |
| `type` | yes | `knowledge` · `runbook` · `decision` · `inbox` | Must match the folder |
| `tags` | yes | `[a, b]` | May be `[]` |
| `applies_to` | yes | `[a, b]` | `[]` = everywhere. Tokens like `ocp-4.18`, `mongo-8.0`, `mongo-6.0..8.0`, `mck-1.10`, `k8ssandra-1.20` |
| `confidence` | yes, except decisions | `verified` · `observed` · `hypothesis` | See below |
| `status` | decisions only | `accepted` · `proposed` · `superseded` | |
| `last_verified` | yes | `YYYY-MM-DD` | Not in the future |
| `owners` | yes | `[a, b]`, not empty | Who to ask |
| `source` | recommended | text | `claude-session`, an incident, a person, a ticket |
| `rule` | optional | one line, at most 220 characters | `<situation> → <what to do>`; becomes a Quick Rule |

| `confidence` | Means |
|---|---|
| `verified` | Confirmed by the owning team, or tested working |
| `observed` | Seen once, or read in docs or code |
| `hypothesis` | Believed but not confirmed |

## Format limits

- A flat block: one `key: value` per line, lists as `[a, b]`, no multi-line values.
- A value that still looks like a template placeholder (`<...>`) is an error: fill it in or delete the line.

## Also checked on every page

- **Errors (block the push):** private keys, `password:` / `password=`, S3 / access keys, MongoDB
  connection strings with a password, bearer tokens, JWTs, GitLab tokens (`glpat-`), AWS-style keys,
  OpenShift tokens (`sha256~`), kubeconfig credentials.
- **Warnings:** IP addresses; file names that aren't lowercase-with-dashes.
- A false positive: add `brain:allow-secret` at the end of that line.
- The scan catches common patterns only. Hostnames, customer names and credentials written in prose
  still need a human eye.
