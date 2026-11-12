<!-- Converted from tutorial/query-array-of-documents.txt (reStructuredText). Includes are inlined. -->

# Query an Array of Embedded Documents

   
   

You can query documents in MongoDB by using the following
methods:

- Your programming language's driver.
- The MongoDB Atlas UI. To learn more, see 
  query-array-documents-atlas-ui.
- `MongoDB Compass`.

This page provides examples of query operations on an array of nested documents using the
`db.collection.find()` method in `mongosh`.

```javascript
db.inventory.insertMany( [
   { item: "journal", instock: [ { warehouse: "A", qty: 5 }, { warehouse: "C", qty: 15 } ] },
   { item: "notebook", instock: [ { warehouse: "C", qty: 5 } ] },
   { item: "paper", instock: [ { warehouse: "A", qty: 60 }, { warehouse: "B", qty: 15 } ] },
   { item: "planner", instock: [ { warehouse: "A", qty: 40 }, { warehouse: "B", qty: 5 } ] },
   { item: "postcard", instock: [ { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ] }
]);
```

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `query-array-of-documents.parts/`)

- `001-query-for-a-document-nested-in-an-array-specify-a-.md`: Query for a Document Nested in an Array … Specify a Query Condition on a Field in an Array of Documents
- `002-specify-multiple-conditions-for-array-of-documents.md`: Specify Multiple Conditions for Array of Documents … Specify Multiple Conditions for Array of Documents
- `003-query-for-a-document-nested-in-an-array-query-for-.md`: Query for a Document Nested in an Array … Query for a Document Nested in an Array
- `004-specify-a-query-condition-on-a-field-in-an-array-o.md`: Specify a Query Condition on a Field in an Array of Documents … Additional Query Tutorials
