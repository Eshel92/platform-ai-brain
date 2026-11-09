<!-- Converted from core/link-text-indexes.txt (reStructuredText). Includes are inlined. -->

# Perform a Text Search (Self-Managed Deployments)

**Note:**

This page describes text query capabilities for self-managed
(non-Atlas) deployments. For data hosted on MongoDB Atlas, MongoDB
offers an improved full-text query solution, Atlas Search and a vector search solution, Atlas Vector Search. 

To run text search queries on self-managed deployments, you must have a
text index on your collection. MongoDB
provides text indexes to support text search queries on string content.
Text indexes can include any field whose value is a string or an array
of string elements. A collection can only have **one** text search
index, but that index can cover multiple fields.

See the /core/index-text section for a full reference on text
indexes, including behavior, tokenization, and properties.

## Examples

This example demonstrates how to build a text index and use it to find
coffee shops, given only text fields.

### Create a Collection

Create a collection `stores` with the following documents:

```javascript
db.stores.insertMany(
   [
     { _id: 1, name: "Java Hut", description: "Coffee and cakes" },
     { _id: 2, name: "Burger Buns", description: "Gourmet hamburgers" },
     { _id: 3, name: "Coffee Shop", description: "Just coffee" },
     { _id: 4, name: "Clothes Clothes Clothes", description: "Discount clothing" },
     { _id: 5, name: "Java Shopping", description: "Indonesian goods" },
     { _id: 6, name: "NYC_Coffee Shop", description: "local NYC coffee" }
   ]
)
```

### Create a Text Index

Run the following in `mongosh` to allow text search over 
the `name` and `description` fields:

```javascript
db.stores.createIndex( { name: "text", description: "text" } )
```

### Search for an Exact String

You can search for exact multi-word strings by wrapping them in double-quotes.
Text search only matches documents that include the whole string.

For example, the following query finds all documents that contain the string
"coffee shop":

```javascript
db.stores.find( { $text: { $search: "\"coffee shop\"" } } )
```

This query returns the following documents:

```javascript
[
   { _id: 3, name: 'Coffee Shop', description: 'Just coffee' },
   { _id: 6, name: 'NYC_Coffee Shop', description: 'local NYC coffee' }
]
```

Unless specified, exact string search is not case sensitive or diacritic
sensitive. For example, the following query returns the same
results as the previous query:

```javascript
db.stores.find( { $text: { $search: "\"COFFEé SHOP\"" } } )
```

Exact string search does not handle stemming or stop words. 

### Exclude a Term

To exclude a word, you can prepend a "`-`" character. For example, to
find all stores containing "java" or "shop" but not "coffee", use the
following:

```javascript
db.stores.find( { $text: { $search: "java shop -coffee" } } )
```

### Sort the Results

MongoDB returns its results in unsorted order by default. However,
`$text` queries compute a relevance score for each document
that specifies how well a document matches the query.

To sort the results in order of relevance score, you must explicitly
project the `$meta` `textScore` field and sort on it:

```javascript
db.stores.find(
   { $text: { $search: "java coffee shop" } },
   { score: { $meta: "textScore" } }
).sort( { score: { $meta: "textScore" } } )
```

`$text` is also available in the aggregation pipeline.
