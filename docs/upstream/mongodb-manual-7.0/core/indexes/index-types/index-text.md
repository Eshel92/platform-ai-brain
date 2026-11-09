<!-- Converted from core/indexes/index-types/index-text.txt (reStructuredText). Includes are inlined. -->

# Text Indexes on Self-Managed Deployments

**Note:**

This page describes text query capabilities for self-managed
(non-Atlas) deployments. For data hosted on MongoDB Atlas, MongoDB
offers an improved full-text query solution, Atlas Search and a vector search solution, Atlas Vector Search. 

Text indexes support text search queries on
fields with string content. Text indexes improve performance when
searching for specific words or strings. 

A collection can have only **one** text index, but that index may include
multiple fields.

To create a text index, use the following prototype:

```javascript
db.<collection>.createIndex(
   {
      <field1>: "text",
      <field2>: "text",
      ...
   }
)
```

## $text Query Support

Text indexes support `$text` queries on self-managed
deployments. You must create a text index to use `$text`.

## Use Cases

An online shop's `clothing` collection has a `description` field that 
contains a string of text describing each item. To find clothes made of 
`"silk"`, create a text index on `description` and run a
`$text` query for `"silk"`. The search returns all documents
mentioning `"silk"` in `description`.

## Get Started

To learn how to create and use text indexes, see:
  
- create-text-index
- create-wildcard-text-index
- specify-default-text-index-language
- limit-entries-scanned

## Details

This section describes text index details.

### Compound Text Indexes

In a compound index with a text index key and other key types,
only the text index field determines whether the index references
a document. Other keys do not affect document references.

### Covered Queries

Text indexes can't cover a query.

### `sparse` Property

Text indexes are always sparse.
MongoDB ignores the `sparse` option when creating text indexes.

MongoDB does not add a text index entry for documents that lack
the text index field, have null values, or have empty arrays.

### Storage Requirements and Performance Costs

Text indexes have these storage and performance characteristics:

- Text indexes can consume significant RAM. They contain one
  index entry for each unique stemmed word in each indexed field
  for each document.

- Building a text index is similar to building a large
  multikey index but takes longer
  than building an ordered (scalar) index on the same data.

- When building large text indexes, ensure sufficient file
  descriptor limits. See recommended settings.

- Text indexes impact write performance because MongoDB must add
  an index entry for each unique stemmed word in each indexed
  field of new documents.

- Text indexes store individual words, not multi-word strings or
  word proximity information. Queries with multiple words run
  faster when the entire collection fits in RAM.

## Learn More

- To learn more about text indexes, see: 
  
  - control-text-search-results
  - text-index-properties
  - text-index-restrictions
  - text-index-versions
  
- For text search examples, see the `$text reference page`.
  
- For sample `$text` operations in aggregation pipelines, see
  text-agg.
