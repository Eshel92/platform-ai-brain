<!-- Converted from reference/command/nav-atlas-search.txt (reStructuredText). Includes are inlined. -->

# Atlas Search Database Commands

**Note:**

For details on a specific command, including syntax and examples,
click on the link to the command's reference page.

**New in version:** 6.0.7

Atlas Search indexes let you query data
in Atlas Search. Atlas Search indexes enable performant
text search queries by mapping search terms to the documents that
contain those terms.

Use the following database commands to manage Atlas Search indexes.

**Important:**

The following commands can only be run on deployments hosted on
MongoDB Atlas, and require an Atlas cluster tier of at
least M10.

| Name | Description |
|---|---|
| `createSearchIndexes` | .. include:: /includes/atlas-search-commands/command-descriptions/createSearchIndexes-description.rst |
| `dropSearchIndex` | .. include:: /includes/atlas-search-commands/command-descriptions/dropSearchIndex-description.rst |
| `updateSearchIndex` | .. include:: /includes/atlas-search-commands/command-descriptions/updateSearchIndex-description.rst |
