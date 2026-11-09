<!-- Converted from tutorial/model-tree-structures-with-ancestors-array.txt (reStructuredText). Includes are inlined. -->

# Model Tree Structures with an Array of Ancestors

## Overview

This page describes a data model that describes a tree-like
structure in MongoDB documents using references to parent nodes and an array that stores
all ancestors.

## Pattern

The *Array of Ancestors* pattern stores each tree node in a document;
in addition to the tree node, document stores in an array the id(s) of
the node's ancestors or path.

Consider the following hierarchy of categories:

(Figure: /images/data-model-tree.bakedsvg.svg)

The following example models the tree using *Array of Ancestors*. In
addition to the `ancestors` field, these documents also store the
reference to the immediate parent category in the `parent` field:

```javascript
db.categories.insertMany( [
  { _id: "MongoDB", ancestors: [ "Books", "Programming", "Databases" ], parent: "Databases" },
  { _id: "dbm", ancestors: [ "Books", "Programming", "Databases" ], parent: "Databases" },
  { _id: "Databases", ancestors: [ "Books", "Programming" ], parent: "Programming" },
  { _id: "Languages", ancestors: [ "Books", "Programming" ], parent: "Programming" },
  { _id: "Programming", ancestors: [ "Books" ], parent: "Books" },
  { _id: "Books", ancestors: [ ], parent: null }
] )
```

- The query to retrieve the ancestors or path of a node is fast and
  straightforward:

  ```javascript
  db.categories.findOne( { _id: "MongoDB" } ).ancestors
  ```

- You can create an index on the field `ancestors` to enable fast
  search by the ancestors nodes:

  ```javascript
  db.categories.createIndex( { ancestors: 1 } )
  ```

- You can query by the field `ancestors` to find all its descendants:

  ```javascript
  db.categories.find( { ancestors: "Programming" } )
  ```

The *Array of Ancestors* pattern provides a fast and efficient solution
to find the descendants and the ancestors of a node by creating an
index on the elements of the ancestors field. This makes *Array of
Ancestors* a good choice for working with subtrees.

The *Array of Ancestors* pattern is slightly slower than the
Materialized Paths pattern but
is more straightforward to use.
