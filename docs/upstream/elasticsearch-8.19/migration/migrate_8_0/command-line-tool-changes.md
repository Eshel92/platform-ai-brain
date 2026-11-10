<!-- Converted from migration/migrate_8_0/command-line-tool-changes.asciidoc (AsciiDoc). Includes are inlined. -->

#### Command line tool changes

**Tip:** {ess-skip-section}

**The `elasticsearch-migrate` tool has been removed.**
*Details* +
The `elasticsearch-migrate` tool provided a way to convert file
realm users and roles into the native realm. It has been deprecated
since Elasticsearch 7.2.0. Users and roles should now be created in the native
realm directly.

*Impact* +
Discontinue use of the `elasticsearch-migrate` tool. Attempts to use the
`elasticsearch-migrate` tool will result in an error.
