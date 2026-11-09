<!-- Converted from release-notes/dbtools-100.13.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.13.0 Changelogs

## 100.13.0 Changelog

*Released 2025-08-13*

The highlight for this release is Server 8.2.0 support. Starting
with 8.2.0, when restoring collections with `mongorestore`,
the `autoIndexId` collection creation option will be ignored,
since this is no longer supported with 8.2.0+.

This release also addresses a few reported security
vulnerabilities. Previous releases incorrectly included
development-only library dependencies in the SBOM, which
accounts for the `aws-sdk-go` vulnerability report. This package
is still included in the released SBOM because of a bug in our
SSDLC tooling. However, it has never been included in the actual
tools code. In addition, this release was built with Go 1.23.11,
which includes a fix for CVE-2025-22874, present in Go 1.23.8
and earlier. However, this particular vulnerability did not
impact the tools, because they do not use the impacted API.

Investigation:

- TOOLS-3825 - Investigate changes in SERVER-103887:
  Introduce QueryRecord IDL type Vulnerability

- TOOLS-3907 - Security Finding: Update package `aws-sdk-go@v1.53.11`

Bug:

- TOOLS-3920 - MacOS binaries are not notarized properly starting from release 100.12.1

- TOOLS-3931 - Goroutine may leak in `DumpIntents` function

- TOOLS-3934 - CVE-2025-22874 in mongoexport and mongoimport

Epic:

- TOOLS-3454 - `mongodump`/`mongorestore` passthrough tests

Task:

- TOOLS-3571 - Add support for RHEL9 on zSeries/s390x
  and PowerPC

- TOOLS-3610 - Add build.go targets for adding/updating
  deps

- TOOLS-3903 - Our SBOM file should only include deps
  for the tools binaries and be OS-insensitive

- TOOLS-3911 - Add a CODEOWNERS file

- TOOLS-3927 - Add tests with Server 8.2

- TOOLS-3928 - Fix failing CI tasks

- TOOLS-3933 - Add the gosec report to our release artifacts
