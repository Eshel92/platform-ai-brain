<!-- Converted from release-notes/dbtools-100.1.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.1.0 Changelogs

## 100.1.1 Changelog

*Released 2020-07-31*

This release contains a fix for a linux packaging bug and a
`mongorestore` bug related to the
`--convertLegacyIndexes`
flag.

### Release

- TOOLS-2685 Release Database Tools 100.1.1

### Bug

- TOOLS-2645 Check for duplicate index keys after converting legacy index definitions
- TOOLS-2683 Ubuntu 16.04 DB Tools 100.1.0 DEB depends on `libcom-err2`, should be `libcomerr2`

## 100.1.0 Changelog

*Released 2020-07-24*

This release officially adds support for MongoDB 4.4. In addition to
various bug fixes, it adds support for MongoDB 4.4's new `MONGODB-AWS`
authentication mechanism.

The full list of changes is below:

### Build Failure

- TOOLS-2604 integration-4.4-cluster is failing on master
- TOOLS-2638 Test-case failure for mongorestore
- TOOLS-2643 New linux distros missing from repo-config.yaml

### Release

- TOOLS-2630 Release Database Tools 100.1.0

### Bug

- TOOLS-2287 URI parser incorrectly prints unsupported parameter warnings
- TOOLS-2337 nsInclude does not work with percent encoded namespaces
- TOOLS-2366 ^C isn't handled by mongodump
- TOOLS-2494 mongorestore thorw error "panic: close of closed channel"
- TOOLS-2531 mongorestore hung if restoring views with --preserveUUID --drop options
- TOOLS-2596 Database Tools --help links to old Manual doc pages
- TOOLS-2597 swallows errors from URI parsing
- TOOLS-2609 Detached signatures incorrectly appearing in download JSON
- TOOLS-2622 Tools do not build following README instructions
- TOOLS-2669 macOS zip archive structure incorrect
- TOOLS-2670 Troubleshoot IAM auth options errors

### New Feature

- TOOLS-2369 IAM Role-based authentication

### Task

- TOOLS-2363 Update warning message for "mongorestore"
- TOOLS-2476 Notarize builds for macOS catalina
- TOOLS-2505 Add missing 4.4 Platforms
- TOOLS-2534 Ignore startIndexBuild and abortIndexBuild oplog entries in oplog replay
- TOOLS-2535 commitIndexBuild and createIndexes oplog entries should build indexes with the createIndexes command during oplog replay
- TOOLS-2554 Remove ReplSetTest file dependencies from repo
- TOOLS-2569 Update tools to go driver 1.4.0
- TOOLS-2618 Refactor AWS IAM auth testing code
- TOOLS-2628 Add 3.4 tests to evg
- TOOLS-2644 Update barque authentication
- TOOLS-2650 Create changelog for tools releases
