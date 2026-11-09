<!-- Converted from release-notes/dbtools-100.6.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.6.0 Changelogs

## 100.6.1 Changelog

*Released 2022-11-03*

This release fixes an issue where users without permissions 
to read `config.system.preimages` could not run 
`mongodump`. 
This release also fixes issues with installing the Database Tools on 
Amazon Linux 2 aarch64 and RHEL 8.3 s390x. The Database Tools 
are now available on RHEL 9.0 x86. We also made several 
improvements to our testing and release infrastructure.

### Bug

- TOOLS-3176 - Ignore config.system.preimages namespace
- TOOLS-3179 - Mongo Tools Enterprise Z series package is being published to Community repo
- TOOLS-3204 - Tools should not be packaged as arm64 on aarch64 platforms

### Task

- TOOLS-2956 - Use the new notary service to notarize MacOS builds
- TOOLS-3056 - Add RHEL9 x86 to Tools
- TOOLS-3185 - Fix TestMongorestoreTxns failure on all platforms when run against latest Server
- TOOLS-3201 - Add a .snyk file to exclude tests from snyk code analysis

## 100.6.0 Changelog

*Released 2022-08-19*

This release introduces a security enhancement. The tools will
interactively prompt for a SSL key password if the corresponding SSL key
is encrypted and no password is provided on the command line.

### New Feature

- TOOLS-2913 - Prompt for SSL key password when key is
  encrypted
