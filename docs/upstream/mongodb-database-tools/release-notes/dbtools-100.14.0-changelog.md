<!-- Converted from release-notes/dbtools-100.14.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.14.0 Changelogs

## 100.14.1 Changelog

*Released 2026-01-29*

We are pleased to announce version 100.14.1 of the MongoDB Database Tools.

This release updates dependencies with the latest security fixes.

Bug

- TOOLS-4037 - Update to latest versions of dependencies

## 100.14.0 Changelog

*Released 2025-12-16*

We are pleased to announce version 100.14.0 of the MongoDB Database Tools.

This version adds important fixes to upstream dependencies.
It also adds new safety restrictions to `mongofiles` that help protect your data.

Vulnerability

- TOOLS-4010 - Security Finding: Update package crypto@v0.38.0

Bug

- TOOLS-4019 - Fix path traversal in mongofiles

Task

- TOOLS-3983 - Make `mongorestore` warn when restoring archive from a 
  different server version
