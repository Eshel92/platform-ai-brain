<!-- Converted from release-notes/dbtools-100.11.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.11.0 Changelogs

## 100.11.0 Changelog

*Released 2025-02-02*

This version adds support for OIDC
for programmatic workloads. It also updates a few dependency
libraries to fix vulnerabilities, adds a check of metadata
consistency to accommodate `$`-prefixed fields, and fixes a
small race condition in logging.

Bug:

- TOOLS-3618 - Race condition in the
  `mongorestore.ParseOptions` and `log.Logvf`
- TOOLS-3637 - `mongodump` should check collection
  metadata consistency

Task:

- TOOLS-3537 - Create the SSDLC report template
- TOOLS-3736 - Add OIDC Support for Programmatic workloads
- TOOLS-3741 - Update `x/crypto` to address CVE-2024-45337
- TOOLS-3743 - Release new mongo-tools version.
