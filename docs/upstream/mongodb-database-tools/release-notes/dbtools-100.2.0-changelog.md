<!-- Converted from release-notes/dbtools-100.2.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.2.0 Changelogs

## 100.2.1 Changelog

*Released 2020-11-13*

This release includes a `mongorestore` performance
improvement, a fix for a bug affecting highly parallel
`mongorestore` instances, and an observability improvement
to `mongodump` and `mongoexport`, in addition
to a number of internal build/release changes.

### Build Failure

- TOOLS-2767 Windows 64 dist task fails

### Release

- TOOLS-2741 Release Database Tools 100.2.1

### Bug

- TOOLS-2744 mongorestore not scaling due to unnecessary incremental sleep time

### New Feature

- TOOLS-2750 Log before getting collection counts

### Task

- TOOLS-1856 use a memory pool in mongorestore
- TOOLS-2651 Simplify build scripts
- TOOLS-2687 Add archived releases JSON feed for Database Tools
- TOOLS-2735 Move server vendoring instructions to a README in the repo
- TOOLS-2748 Add a String() to OpTime
- TOOLS-2758 Bump Go driver to 1.4.2

## 100.2.0 Changelog

*Released 2020-10-15*

This release deprecates the `--sslAllowInvalidHostnames` and
`--sslAllowInvalidCertificates` flags in favor of a new
`--tlsInsecure` flag. The `mongofiles` `put` and
`mongofiles` `get` commands can now accept a list of file
names. There is a new `mongofiles` `get_regex` command to
retrieve all files matching a regex pattern. The `100.2.0` release
also contains fixes for several bugs. It fixes a bug introduced in
version `100.1.0` that made it impossible to connect to clusters with
an SRV connection string (TOOLS-2711).

### Build Failure

- TOOLS-2693 Most tasks failing on race detector variant
- TOOLS-2737 Fix TLS tests on Mac and Windows
- TOOLS-2747 Git tag release process does not work

### Release

- TOOLS-2704 Release Database Tools 100.2.0

### Bug

- TOOLS-2587 sslAllowInvalidHostnames bypass ssl/tls server certification validation entirely
- TOOLS-2688 `mongodump` does not handle EOF when passing in the password as STDIN
- TOOLS-2706 tar: implausibly old time stamp error on Amazon Linux/RHEL
- TOOLS-2708 Atlas recommended connection string for `mongostat` doesn't work
- TOOLS-2710 Non-zero index key values are not preserved in ConvertLegacyIndexes
- TOOLS-2711 Tools fail with "a direct connection cannot be made if multiple hosts are specified" if mongodb+srv URI or a legacy uri containing multiple `mongos` is specified
- TOOLS-2716 `mongodb-database-tools` package should break older versions of `mongodb-*-tools`

### New Feature

- TOOLS-2667 Support list of files for `put` and `get` subcommands in `mongofiles`
- TOOLS-2668 Create regex interface for getting files from remote FS in `mongofiles`

### Task

- TOOLS-2674 Clarify contribution guidelines
- TOOLS-2700 Use git tags for triggering release versions
- TOOLS-2701 Log target linux repo in push task
