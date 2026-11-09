<!-- Converted from release-notes/dbtools-100.9.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.9.0 Changelogs

## 100.9.5 Changelog

*Released 2024-06-18*

For this release, we have updated many of our third-party dependencies, 
as well as adding third-party dependency vulnerability scanning, static 
analysis, and other tooling to comply with MongoDB's Software Security 
Development Lifecycle initiative. Notably, all releases now ship with 
a Software Bill of Materials (SBOM). Look for a file ending with 
`.cdx.json` in the archive. For OS packages, this file should be 
installed in an appropriate location for each package, such as 
`/usr/share/docs` for deb packages.

### Investigation

- TOOLS-3486 - Investigate changes in SERVER-81378 
  Change classic behavior: equality to null should not match undefined
- TOOLS-3498 - Investigate changes in SERVER-86928 
  Local Privilege Escalation via Untrusted Directory | mongodbldap.exe
- TOOLS-3500 - Investigate changes in SERVER-88071 
  Deprecate filemd5 with the intent of eventual removal

### Bug

- TOOLS-3519 - mongodump/mongoreplay docs don't include a 
  disclaimer against using --oplog/--oplogReplay in sharded clusters
- TOOLS-3554 - Security Vulnerability in mongodb db tools 
  packages

### Task

- TOOLS-3499 - Clean up release code to remove unused tags and 
  remove libsasl.dll from MSI
- TOOLS-3526 - Artifact: Authorized publication on distribution 
  channels for DB Tools 7.0.x
- TOOLS-3527 - Artifact: Third Party Dependencies Report for 
  DB Tools 7.0.x
- TOOLS-3528 - Prep for Silk Onboarding: Add DB Tools to 
  Silk Inventory
- TOOLS-3532 - Onboard DB Tools to Papertrail Service for 
  SSDLC Compliance
- TOOLS-3534 - Integrate this project with Snyk for third-party 
  vulnerability scanning
- TOOLS-3535 - Add gosec as a linter and add minimal precious 
  config
- TOOLS-3550 - Create augmented SBOM file and add it to the 
  release artifacts
- TOOLS-3551 - Fix integration test failures with MongoDB 8.0 
  RC release
- TOOLS-3555 - Remove support for Debian 8
- TOOLS-3559 - Include the Augmented SBOM in all release 
  artifacts
- TOOLS-3565 - Artifact: Static Code Analysis Report for 
  DB Tools 7.0.x

## 100.9.4 Changelog

*Released 2023-12-07*

This version updates the Go version used to build the tools to 
[1.20.12](https://go.dev/doc/devel/release#go1.20.minor) .

### Release

- TOOLS-3438 Release Database Tools 100.9.4 and update go 
  version to 1.20.12

## 100.9.3 Changelog

*Released 2023-11-17*

### Bug

- TOOLS-3429 - Add support for  Debian 11 (Bullseye) 

## 100.9.2 Changelog

*Released 2023-11-16*

### Task

- TOOLS-3302 - Add support for Debian 12

## 100.9.1 Changelog

*Released 2023-11-09*

This version updates external dependencies and fixes an issue where mongodump 
could change the ordering of fields in a view definition (TOOLS-3411). 
View pipelines and schema validation are the only collection options sensitive 
to field ordering. Depending on the contents of the view or validator options, 
the following can change:

- The set of results returned by a view, or
- The criteria that determines which documents are accepted by a validator.

Not all view pipelines or schema validations are affected by key reordering. 

### Bug

- TOOLS-3367 Building fails: failed to detect local platform from kernel name
- TOOLS-3388 mongodb/mongo-tools master :go.mod - Denial of Service DoS in golang.org/x/net
- TOOLS-3411 MongoDump does not maintain field-order for sort and match in Views.

## 100.9.0 Changelog

*Released 2023-10-20*

- This version adds support for 
  MongoDB Server 7.0. 

- This version updates the Go version used to build the tools to 
  [1.20.10](https://go.dev/doc/devel/release#go1.20.minor) .

### Epic

- TOOLS-3278 Tools 7.0 Support
