<!-- Converted from release-notes/dbtools-100.3.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.3.0 Changelogs

## 100.3.1 Changelog

*Released 2021-03-17*

This release includes various bug fixes. Particularly notable is
TOOLS-2783, where we reverted a change from 100.2.1
(TOOLS-1856: use a memory pool in `mongorestore`)
after discovering that it was causing memory usage issues.

### Build Failure

- TOOLS-2796 mongotop_sharded.js failing on all versions of the qa-tests
- TOOLS-2815 Development build artifacts accidentally uploaded for versioned release

### Release

- TOOLS-2791 Release Database Tools 100.3.1

### Bug

- TOOLS-2584 Restoring single BSON file should use db set in URI
- TOOLS-2783 Mongorestore uses huge amount of RAM

### Task

- TOOLS-704 Remove system.indexes collection dumping from mongodump
- TOOLS-2801 Migrate from dep to Go modules and update README
- TOOLS-2802 Make mongo-tools-common a subpackage of mongo-tools
- TOOLS-2805 Add mod tidy static analysis check for Go modules
- TOOLS-2806 Migrate mongo-tools-common unit tests to mongo-tools
- TOOLS-2807 Migrate mongo-tools-common integration tests to mongo-tools
- TOOLS-2808 Migrate mongo-tools-common IAM auth tests to mongo-tools

## 100.3.0 Changelog

*Released 2021-02-04*

This release includes support for PKCS8-encrypted client private keys,
support for providing secrets in a config file instead of on the command
line, and a few small bug fixes.

### Build Failure

- TOOLS-2795 Tools failing to build on SUSE15-sp2
- TOOLS-2800 RPM creation failing on amazon linux 1

### Release

- TOOLS-2790 Release Database Tools 100.3.0

### Investigation

- TOOLS-2771 SSL connection problems mongodump

### Bug

- TOOLS-2751 Deferred query EstimatedDocumentCount helper incorrect with filter
- TOOLS-2760 rpm package should not obsolete itself
- TOOLS-2775 --local does not work with multi-file get or get_regex

### New Feature

- TOOLS-2779 Add --config option for password values

### Task

- TOOLS-2013 Support PKCS8 encrypted client private keys
- TOOLS-2707 Build mongo-tools and mongo-tools-common with go 1.15
- TOOLS-2780 Add warning when password value appears on command line
- TOOLS-2798 Add Amazon Linux 2 Arm64 to Tools
