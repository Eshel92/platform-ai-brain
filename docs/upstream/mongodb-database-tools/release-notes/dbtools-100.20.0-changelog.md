<!-- Converted from release-notes/dbtools-100.20.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.20.0 Changelogs

## 100.20.1 Changelog

*Released 2026-11-02*

We are pleased to announce version 100.20.1 of the MongoDB Database
Tools.

This release hardens how the tools handle untrusted input and fixes
several security concerns, including path traversal and query-operator
injection. This release also prevents secrets from leaking into error
messages and corrects the `uri` field in generated SARIF reports.

Bug:

- TOOLS-4352 - `mongorestore` should reject crafted
  collection names that resolve to `$admin.system.` auth collections
- TOOLS-4417 - `mongorestore` should not unescape real
  collection names if filenames are truncated
- TOOLS-4448 - `mongoimport` allows query-operator injection
  into the selector

Task:

- TOOLS-4222 - Fix path traversal bypass in
  `mongofiles get <filename>`
- TOOLS-4415 - `mongofiles`: treat server-returned `-` as a
  filename rather than stdout
- TOOLS-4422 - `mongodump`: validate server-returned
  collection names to prevent path traversal
- TOOLS-4429 - Replace all uses of `gopkg.in/yaml.v3` with
  `github.com/goccy/go-yaml`
- TOOLS-4439 - The `uri` field for SARIF entries shows only a
  filename, not the path to the file from the repo root
- TOOLS-4446 - Redact secrets from connection strings in error
  messages

## 100.20.0 Changelog

*Released 2026-10-26*

We are pleased to announce version 100.20.0 of the MongoDB Database
Tools.

This release removes support for MongoDB Server versions before 4.2.
The target server and any dump files must now be from MongoDB 4.2 or
later. This release also fixes two `mongorestore` bugs. The release
includes Go 1.27.3 and Go driver upgrades.

Bug:

- TOOLS-4176 - `mongorestore` crash when namespace without
  active consumer is used
- TOOLS-4373 - `mongorestore --oplogReplay` aborts with
  `Location7667503` when a time series collection was written during
  `mongodump --oplog`

Task:

- TOOLS-4350 - Remove support for pre-4.2 Server versions and
  dump files
- TOOLS-4401 - Upgrade to the latest Go driver version
- TOOLS-4404 - Remove Amazon 2018 from CI
- TOOLS-4414 - Upgrade our `github.com/deckarep/golang-set`
  dependency to v3
- TOOLS-4432 - Upgrade to Go 1.27.3
