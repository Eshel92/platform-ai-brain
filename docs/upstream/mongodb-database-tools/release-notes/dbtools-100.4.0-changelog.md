<!-- Converted from release-notes/dbtools-100.4.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.4.0 Changelogs

## 100.4.1 Changelog

*Released 2021-07-23*

This patch fixes a bug (TOOLS-2931) that was introduced in
version `100.4.0` which causes `mongodump` to skip any
document that contains an empty field name (e.g. `{ "": "foo" }`).
Documents with empty field names were not skipped by default if the
`--query` or `--queryFile` options were specified. No tools other
than `mongodump` were affected. It is highly recommended to
upgrade to `100.4.1` if it is possible that your database contains
documents with empty field names.

### Build Failure

- TOOLS-2927 Clean up the platforms list inside platform.go

### Release

- TOOLS-2929 Release Database Tools 100.4.1

### Bug

- TOOLS-2931 mongodump skips documents with empty field names

### Task

- TOOLS-2926 Run release on 'test' and 'development' linux repo separately.

## 100.4.0 Changelog

*Released 2021-07-19*

This release includes MongoDB Server 5.0
support, including dump/restoring of timeseries collections.

### Build Failure

- TOOLS-2892 aws-auth tests failing on all variants
- TOOLS-2893 legacy-js-tests 4.4 and 5.0 failing on all variants

### Release

- TOOLS-2845 Release Database Tools 100.4.0

### Bug

- TOOLS-2041 Mongorestore should handle duplicate key errors during oplog replay
- TOOLS-2833 Creating an index with partialFilterExpression during oplogReplay fails
- TOOLS-2925 RPM packages are only signed with the 4.4 auth token

### New Feature

- TOOLS-2857 Dump timeseries collections
- TOOLS-2858 Mongodump can query timeseries collections by metadata
- TOOLS-2859 Restore timeseries collections
- TOOLS-2860 Include/Exclude/Rename timeseries collections in mongorestore

### Task

- TOOLS-2719 Add Enterprise RHEL 8 zSeries to Tools
- TOOLS-2721 Add RHEL8 ARM to Tools
- TOOLS-2777 Generate Full JSON variant should not be running on every commit
- TOOLS-2823 Build with go 1.16
- TOOLS-2824 Add static analysis task that runs "evergreen validate"
- TOOLS-2849 Mongodump should fail during resharding
- TOOLS-2850 Mongorestore should fail when restoring geoHaystack indexes to 4.9.0
- TOOLS-2851 importCollection command should cause mongodump to fail
- TOOLS-2853 Hide deprecated --slaveOk option
- TOOLS-2866 Drop support for zSeries platforms
- TOOLS-2873 Run full test suite on all supported distros in evergreen
- TOOLS-2881 Push tools releases to 4.9+ linux repos
- TOOLS-2921 Upgrade to Go Driver 1.6
