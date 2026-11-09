<!-- Converted from release-notes/dbtools-100.16.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.16.0 Changelogs

## 100.16.1 Changelog

*Released 2026-04-24*

We are pleased to announce version 100.16.1 of the MongoDB Database
Tools.

This patch release includes a fix for a message size overflow in
`BufferedBulkInserter`, along with maintenance updates including
rewriting JavaScript tests in Go, improving `mongoexport` Extended
JSON marshalling, and upgrading to Go 1.25.9.

Bug:

- TOOLS-4142 - Fix OP_MSG size overflow in
  `BufferedBulkInserter`

Task:

- TOOLS-4148 - Rewrite JS tests in Go
- TOOLS-4184 - Use simple `MarshalExtJSON` in
  `mongoexport`
- TOOLS-4194 - Upgrade to Go 1.25.9

## 100.16.0 Changelog

*Released 2026-04-01*

We are pleased to announce version 100.16.0 of the MongoDB Database
Tools.

The highlight for this release is MongoDB Server 8.3 support, as well
as support for new server features. There are a few important changes
to note:

- When running against MongoDB 8.3, `mongoexport` no longer
  supports exporting collections in the `system.buckets.` namespace.
- When running against MongoDB 8.3 with authentication enabled,
  `mongodump` requires the `performRawDataOperations` permission in
  addition to `find`. The built-in `backup` role contains this
  permission.

Investigation:

- TOOLS-4039 - Explicitly replicate multikey writes in a 
  multi-doc transaction

Build Failure:

- TOOLS-4108 - Fix missing document in capped collection
  during `mongodump` testing
- TOOLS-4141 - Fix failing QA tests on Windows for MongoDB 8.2

Bug:

- TOOLS-4145 - `mongorestore` failure when batch size
  exceeds `maxMessageSizeBytes`
- TOOLS-4154 - `mongorestore` is not handling empty
  `partialFilterExpression` option correctly

Task:

- TOOLS-4120 - Ignore `"cu"` type oplog entries for
  dump/restore
- TOOLS-4127 - Add pre-release 8.3 version to testing matrix
- TOOLS-4130 - Run passthrough tests with 8.1 and 8.2
- TOOLS-4134 - Add basic time series tests for
  import/export
- TOOLS-4136 - Add passthrough tests for 8.3
- TOOLS-4146 - Add support for `rawData` CRUD API to 
  `mongodump/mongorestore` and `mongoimport/mongoexport`
- TOOLS-4147 - Remove workaround for `rawData` on `admin`
  database
- TOOLS-4150 - Ensure tools work with changes in SPM-4355
- TOOLS-4153 - Enable 8.3 in Linux package repos
- TOOLS-4158 - All tools should properly escape database
  and collection names in output
