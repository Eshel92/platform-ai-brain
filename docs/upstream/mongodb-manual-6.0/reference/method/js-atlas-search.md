<!-- Converted from reference/method/js-atlas-search.txt (reStructuredText). Includes are inlined. -->

# Atlas Search and Atlas Vector Search Index Methods

**Note:**

For details on a specific method, including syntax and examples,
click on the link to the method's reference page.

**New in version:** 6.0.7

Atlas Search indexes let you query data
in Atlas Search, while Atlas Vector Search indexes 
let you query data in Atlas Vector Search. Atlas Search and
Atlas Vector Search indexes enable performant
text search queries by mapping search terms to the documents that
contain those terms.

Use the following methods to manage Atlas Search and Atlas Vector Search indexes.

**Important:**

The following methods can only be run on deployments hosted on
MongoDB Atlas, and require an Atlas cluster tier of at
least M10.

| Name | Description |
|---|---|
| `db.collection.createSearchIndex()` | .. include:: /includes/atlas-search-commands/command-descriptions/createSearchIndex-method.rst |
| `db.collection.dropSearchIndex()` | .. include:: /includes/atlas-search-commands/command-descriptions/dropSearchIndex-description.rst |
| `db.collection.getSearchIndexes()` | .. include:: /includes/atlas-search-commands/command-descriptions/getSearchIndexes-description.rst |
| `db.collection.updateSearchIndex()` | .. include:: /includes/atlas-search-commands/command-descriptions/updateSearchIndex-description.rst |
