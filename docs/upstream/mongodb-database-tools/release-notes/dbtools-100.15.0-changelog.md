<!-- Converted from release-notes/dbtools-100.15.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.15.0 Changelogs

## 100.15.0 Changelog

*Released 2026-03-11*

We are pleased to announce version 100.15.0 of the MongoDB Database Tools.

This release includes dependency and Golang updates for security fixes and
bug fixes.

This version upgrades the Go driver to 2.5.0. As a result, the Database
Tools no longer support MongoDB Server versions earlier than 4.2.
Attempts to connect to an earlier Server version fail.

Bug:

- TOOLS-4105 - `mongorestore` crashes when applying a `collMod` 
  `oplog` event with `forceNonUnique`.
- TOOLS-4068 - QA test fails with MongoDB Server 7.0.28, but passed with 7.0.26.
- TOOLS-4070 - `mongorestore` `--bypassDocumentValidation` does not 
  bypass document validation during oplog restore.
- TOOLS-4071 - `mongorestore` crashes when applying a `collMod` 
  `oplog` event which does not specify `expireAfterSeconds` or `hidden`.
- TOOLS-4075 - `mongorestore` crashes when applying a `collMod` 
  `oplog` event that converts an index to a TTL index.

Task:

- TOOLS-3968 - Update tools to driver v2.
- TOOLS-4073 - Add `mongorestore` support for restoring dumps from 
  clusters with `recordIdsReplicated` enabled into clusters without this feature enabled.
- TOOLS-4074 - Add a manual test program to test dump or restore between 
  clusters with and without replicated record IDs.
- TOOLS-4091 - Fix unsafe file extraction in the release code.
- TOOLS-4118 - Update to Go 1.25.7 to address some CVEs in 1.25.0.
