<!-- Converted from tutorial/optimize-query-performance-with-indexes-and-projections.txt (reStructuredText). Includes are inlined. -->

# Optimize Query Performance

## Create Indexes to Support Queries

For commonly issued queries, create indexes. If a
query searches multiple fields, create a compound index. Scanning an index is much faster than scanning a
collection. The indexes structures are smaller than the documents
reference, and store references in order.

**Example:** If you have a `posts` collection containing blog posts,

and if you regularly issue a query that sorts on the `author_name`
field, then you can optimize the query by creating an index on the
`author_name` field:

```javascript
db.posts.createIndex( { author_name : 1 } )
```

Indexes also improve efficiency on queries that routinely sort on a
given field.

**Example:** If you regularly issue a query that sorts on the

`timestamp` field, then you can optimize the query by creating an
index on the `timestamp` field:

Creating this index:

```javascript
db.posts.createIndex( { timestamp : 1 } )
```

Optimizes this query:

```javascript
db.posts.find().sort( { timestamp : -1 } )
```

Because MongoDB can read indexes in both ascending and descending
order, the direction of a single-key index does not matter.

Indexes support queries, update operations, and some phases of the
aggregation pipeline.

Index keys that are of the `BinData` type are more efficiently stored
in the index if:

- the binary subtype value is in the range of 0-7 or 128-135, and

- the length of the byte array is: 0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 12,
  14, 16, 20, 24, or 32.

## Limit the Number of Query Results to Reduce Network Demand

MongoDB cursors return results in groups of multiple
documents. If you know the number of results you want, you can reduce
the demand on network resources by issuing the `limit()`
method.

This is typically used in conjunction with sort operations. For example,
if you need only 10 results from your query to the `posts`
collection, you would issue the following command:

```javascript
db.posts.find().sort( { timestamp : -1 } ).limit(10)
```

For more information on limiting results, see `limit()`

## Use Projections to Return Only Necessary Data

When you need only a subset of fields from documents, you can achieve better
performance by returning only the fields you need:

For example, if in your query to the `posts` collection, you need only
the `timestamp`, `title`, `author`, and `abstract` fields, you
would issue the following command:

```javascript
db.posts.find( {}, { timestamp : 1 , title : 1 , author : 1 , abstract : 1} ).sort( { timestamp : -1 } )
```

For more information on using projections, see
read-operations-projection.

## Use `$hint` to Select a Particular Index

In most cases the query optimizer selects the optimal index for a
specific operation; however, you can force MongoDB to use a specific
index using the `hint()` method. Use
`hint()` to support performance testing, or on
some queries where you must select a field or field included in
several indexes.

## Use the Increment Operator to Perform Operations Server-Side

Use MongoDB's `$inc` operator to increment or decrement
values in documents. The operator increments the value of the field on
the server side, as an alternative to selecting a document, making
simple modifications in the client and then writing the entire
document to the server.  The `$inc` operator can also help
avoid race conditions, which would result when two application
instances queried for a document, manually incremented a field, and
saved the entire document back at the same time.
