<!-- Converted from release-notes/dbtools-100.19.0-changelog.txt (reStructuredText). Includes are inlined. -->

# Database Tools 100.19.0 Changelogs

## 100.19.1 Changelog

*Released 2026-09-30*

We are pleased to announce version 100.19.1 of the MongoDB Database
Tools.

This patch release adds support for Debian 13 for MongoDB Community.

Task:

- TOOLS-4393 - Add support for Debian 13 for MongoDB
  Community

## 100.19.0 Changelog

*Released 2026-09-22*

We are pleased to announce version 100.19.0 of the MongoDB Database
Tools.

The highlight for this release includes dependency and Golang upgrades
that address a variety of CVEs. This release also fixes
`mongorestore`, which can be tricked into using an unbounded amount of
memory with malicious input. Avoid using `mongorestore` with untrusted
input.

Bug:

- TOOLS-4355 - `mongorestore` could use unbounded memory
  through unbounded archive `concurrent_collections` settings
- TOOLS-4330 - Some tests use the wrong context in
  `t.Cleanup`

Task:

- TOOLS-4336 - The options handling of some timeout values
  treats them as milliseconds but documents them as seconds
- TOOLS-4338 - Error checking in the `MongoDump.Dump` func is
  backwards
- TOOLS-4346 - Upgrade to Golang 1.26.7
- TOOLS-4372 - Bump Go toolchain past 1.26.5 to fix 10 stdlib
  CVEs (fixed in 1.25.13 / 1.26.6 / 1.27.0-rc.3)
- TOOLS-4354 - Upgrade Go driver to 2.8.2
