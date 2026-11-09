<!-- Converted from tutorial/model-tree-structures-with-parent-references.txt (reStructuredText). Includes are inlined. -->

# Model Tree Structures with Parent References

## Overview

This page describes a data model that describes a tree-like
structure in MongoDB documents by storing
references to "parent" nodes in
children nodes.

## Pattern

The *Parent References* pattern stores each tree node in a document; in
addition to the tree node, the document stores the ID of the node's
parent.

Consider the following hierarchy of categories:

(Figure: /images/data-model-tree.bakedsvg.svg)

The following example models the tree using *Parent References*,
storing the reference to the parent category in the field `parent`:

```javascript
db.categories.insertMany( [
   { _id: "MongoDB", parent: "Databases" },
   { _id: "dbm", parent: "Databases" },
   { _id: "Databases", parent: "Programming" },
   { _id: "Languages", parent: "Programming" },
   { _id: "Programming", parent: "Books" },
   { _id: "Books", parent: null }
] )
```

- The query to retrieve the parent of a node is fast and
  straightforward:

  ```javascript
  db.categories.findOne( { _id: "MongoDB" } ).parent
  ```

- You can create an index on the field `parent` to enable fast search
  by the parent node:

  ```javascript
  db.categories.createIndex( { parent: 1 } )
  ```

- You can query by the `parent` field to find its immediate children
  nodes:

  ```javascript
  db.categories.find( { parent: "Databases" } )
  ```

- To retrieve subtrees, see `$graphLookup`.
