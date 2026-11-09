<!-- Converted from release-notes/dbtools-100.10.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.10.0 Changelogs

## 100.10.0 Changelog

*Released 2024-07-24*

This version adds support for MongoDB Server 8.0, and support for 
Ubuntu 24.04 platforms. It also updates several packages and fixes a bug.

### Security

- TOOLS-3615 - Security Finding: Update package `golang.org/x/crypto` 
  to address [CVE-2022-30636](https://www.cve.org/CVERecord?id=CVE-2022-30636).

### Bug

- TOOLS-3611 - Mongodump and restore should not produce a 
  JSON format error on $-prefixed object keys

### Epic

- TOOLS-3413 - Tools 8.0 Support

### Task

- TOOLS-3546 - Support vectored insertion oplog format
- TOOLS-3572 - Fix file names for released deb packages
- TOOLS-3574 - Run integration tests against 8.0 and add ubuntu2404 variants
- TOOLS-3575 - Support dump and restore mixed-schema timeseries buckets
- TOOLS-3604 - Add platforms rhel8.8 (x86_64 and arm64) and rhel9.3 (x86_64 and arm64)
- TOOLS-3613 - Run qa and legacy tests against 8.0
- TOOLS-3616 - Update go driver version to v1.16.0
