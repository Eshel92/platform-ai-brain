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

Starting in version 2.6, MongoDB can use index
intersection to fulfill queries. The choice
between creating compound indexes that support your queries or relying
on index intersection depends on the specifics of your system. See
index-intersection-compound-indexes for more details.

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

Because indexes that are configured with collation use ICU
collation keys to achieve sort order, collation-aware index keys
may be larger than index keys for indexes without collation. 

A `restaurants` collection has the following documents:

```javascript
db.restaurants.insertMany( [
   { _id: 1, category: "café", status: "Open" },
   { _id: 2, category: "cafe", status: "open" },
   { _id: 3, category: "cafE", status: "open" }
] )
```

The `restaurants` collection has an index on a string field
`category` with the collation locale `"fr"`.

```javascript
db.restaurants.createIndex( { category: 1 }, { collation: { locale: "fr" } } )
```

The following query, which specifies the same collation as the index,
can use the index:

```javascript
db.restaurants.find( { category: "cafe" } ).collation( { locale: "fr" } )
```

However, the following query operation, which by default uses the
"simple" binary collator, cannot use the index:

```javascript
db.restaurants.find( { category: "cafe" } )
```

For a compound index where the index prefix keys are not strings,
arrays, and embedded documents, an operation that specifies a
different collation can still use the index to support comparisons
on the index prefix keys.

For example, the collection `restaurants` has a compound index on the
numeric fields `score` and `price` and the string field
`category`; the index is created with the  collation locale
`"fr"` for string comparisons:

```javascript
db.restaurants.createIndex(
   { score: 1, price: 1, category: 1 },
   { collation: { locale: "fr" } } )
```

The following operations, which use `"simple"` binary collation
for string comparisons, can use the index:

```javascript
db.restaurants.find( { score: 5 } ).sort( { price: 1 } )
db.restaurants.find( { score: 5, price: { $gt: NumberDecimal( "10" ) } } ).sort( { price: 1 } )
```

The following operation, which uses `"simple"` binary collation
for string comparisons on the indexed `category` field, can use
the index to fulfill only the `score: 5` portion of the query:

```javascript
db.restaurants.find( { score: 5, category: "cafe" } )
```

To confirm whether a query used an index, run the query with the
`explain()` option.

**Important:**

Matches against document keys, including embedded document keys, 
use simple binary comparison. This means that a query for a key  
like "type.café" will not match the key "type.cafe", regardless of
the value you set for the strength parameter.
