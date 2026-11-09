<!-- Converted from applications/data-models.txt (reStructuredText). Includes are inlined. -->

# Data Model Examples and Patterns

**See also:**

For additional patterns and use cases, see also: [Building with Patterns](https://www.mongodb.com/blog/post/building-with-patterns-a-summary)

The following documents provide overviews of various data modeling
patterns and common schema design considerations:

/applications/data-models-relationships
   Examples for modeling relationships between documents.

   /tutorial/model-embedded-one-to-one-relationships-between-documents
      Presents a data model that uses embedded documents to describe one-to-one relationships
      between connected data.

   /tutorial/model-embedded-one-to-many-relationships-between-documents
      Presents a data model that uses embedded documents to describe one-to-many
      relationships between connected data.

   /tutorial/model-referenced-one-to-many-relationships-between-documents
      Presents a data model that uses references to describe one-to-many
      relationships between documents.

/applications/data-models-tree-structures
   Examples for modeling tree structures.

   /tutorial/model-tree-structures-with-parent-references
      Presents a data model that organizes documents in a tree-like
      structure by storing references to "parent" nodes in "child"
      nodes.

   /tutorial/model-tree-structures-with-child-references
      Presents a data model that organizes documents in a tree-like
      structure by storing references to "child" nodes in "parent"
      nodes.

   See /applications/data-models-tree-structures for additional
   examples of data models for tree structures.

/applications/data-models-applications
   Examples for models for specific application contexts.

   /tutorial/model-data-for-atomic-operations
      Illustrates how embedding fields related to an atomic update
      within the same document ensures that the fields are in sync.

   /tutorial/model-data-for-keyword-search
      Describes one method for supporting keyword search by storing
      keywords in an array in the same document as the text field.
      Combined with a multi-key index, this pattern can support
      application's keyword search operations.
