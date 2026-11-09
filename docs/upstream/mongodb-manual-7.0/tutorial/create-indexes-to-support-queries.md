<!-- Converted from tutorial/create-indexes-to-support-queries.txt (reStructuredText). Includes are inlined. -->

# Create Indexes to Support Your Queries

An index supports a query when the index contains all the fields scanned
by the query. The query scans the index and not the collection. Creating indexes
that support queries results in greatly increased query performance.

This document describes strategies for creating indexes that support queries.

## Create a Single-Key Index if All Queries Use the Same, Single Key

If you only ever query on a single key in a given collection, then you need
to create just one single-key index for that collection. For example, you
might create an index on `category` in the `product` collection:

```javascript
db.products.createIndex( { "category": 1 } )
```

## Create Compound Indexes to Support Several Different Queries

If you sometimes query on only one key and at other times query on that
key combined with a second key, then creating a compound index is more
efficient than creating a single-key index. MongoDB will use the
compound index for both queries. For example, you might create an index
on both `category` and `item`.

```javascript
db.products.createIndex( { "category": 1, "item": 1 } )
```

This allows you both options. You can query on just `category`, and
you also can query on `category` combined with `item`.
A single compound index on multiple fields
can support all the queries that search a "prefix" subset of those fields.

**Example:**

The following index on a collection:

```javascript
{ x: 1, y: 1, z: 1 }
```

Can support queries that the following indexes support:

```javascript
{ x: 1 }
{ x: 1, y: 1 }
```

There are some situations where the prefix indexes may offer better
query performance: for example if `z` is a large array.

The `{ x: 1, y: 1, z: 1 }` index can also support many of the same
queries as the following index:

```javascript
{ x: 1, z: 1 }
```

Also, `{ x: 1, z: 1 }` has an additional use. Given the following
query:

```javascript
db.collection.find( { x: 5 } ).sort( { z: 1} )
```

The `{ x: 1, z: 1 }` index supports both the query and the sort
operation, while the `{ x: 1, y: 1, z: 1 }` index only supports
the query. For more information on sorting, see
sorting-with-indexes.

## Create Indexes to Support Text Search

For data hosted on MongoDB Atlas, you can support full-text search with
Atlas Search indexes. To learn more, see Create an Atlas Search
Index.

For self-managed (non-Atlas) deployments, MongoDB provides a `text`
index type that supports searching for string content in a collection.
To learn more about self-managed text indexes, see
index-feature-text.

## Index Use and Collation

To use an index for string comparisons, an operation must also
specify the same collation. That is, an index with a collation
cannot support an operation that performs string comparisons on the
indexed fields if the operation specifies a different collation.

**Warning:**

Collation-aware index keys might be larger than index keys for indexes 
without collation because indexes that are configured with collation use 
ICU collation keys to achieve sort order.
