<!-- Converted from core/index-compound.txt (reStructuredText). Includes are inlined. -->

# Compound Indexes

MongoDB supports *compound indexes*, where a single index structure
holds references to multiple fields [#compound-index-field-limit]_
within a collection's documents. The following diagram illustrates an
example of a compound index on two fields:

(Figure: /images/index-compound-key.bakedsvg.svg)

Compound indexes can support queries that match on multiple fields.

## Compatibility

You can use compound indexes for deployments hosted in [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server).
To learn more about managing indexes for deployments hosted in MongoDB
Atlas, see Create, View, Drop, and Hide Indexes.

## Create a Compound Index

To create a compound index use an
operation that resembles the following prototype:

```javascript
db.collection.createIndex( { <field1>: <type>, <field2>: <type2>, ... } )
```

The order of the indexed fields has a strong impact on the
effectiveness of a particular index for a given query. For most
compound indexes, following the ESR (Equality, Sort, Range) rule helps to create efficient indexes.

**Important:**

Starting in MongoDB 4.4: 

- Compound indexes may contain **a single** hashed index field. 
- You will receive an error if you attempt to create a compound index 
  that contains more than one hashed index field.

In MongoDB 4.2 or earlier: 

- Compound indexes may **not** contain a hashed index field. 
- You will receive an error if you attempt to create a compound index
  that contains a hashed index field.

Consider a collection named `products` that holds documents that
resemble the following document:

```javascript
{
 "_id": ObjectId(...),
 "item": "Banana",
 "category": ["food", "produce", "grocery"],
 "location": "4th Street Store",
 "stock": 4,
 "type": "cases"
}
```

The following operation creates an ascending index on the `item` and
`stock` fields:

```javascript
db.products.createIndex( { "item": 1, "stock": 1 } )
```

The order of the fields listed in a compound index is important. The
index will contain references to documents sorted first by the values
of the `item` field and, within each value of the `item` field, sorted by
values of the stock field. See index-ascending-and-descending
for more information.

In addition to supporting queries that match on all the index fields,
compound indexes can support queries that match on the prefix of the
index fields. That is, the index supports queries on the `item` field
as well as both `item` and `stock` fields:

```javascript
db.products.find( { item: "Banana" } )
db.products.find( { item: "Banana", stock: { $gt: 5 } } )
```

For details, see compound-index-prefix.

## Sort Order

Indexes store references to fields in either ascending (`1`) or
descending (`-1`) sort order. For single-field indexes, the sort
order of keys doesn't matter because MongoDB can traverse the index in
either direction. However, for compound indexes, sort order can matter in determining whether
the index can support a sort operation.

Consider a collection `events` that contains documents with the
fields `username` and `date`. Applications can issue queries that
return results sorted first by ascending `username` values and then
by descending (i.e. more recent to last) `date` values, such as:

```javascript
db.events.find().sort( { username: 1, date: -1 } )
```

or queries that return results sorted first by descending `username`
values and then by ascending `date` values, such as:

```javascript
db.events.find().sort( { username: -1, date: 1 } )
```

The following index can support both these sort operations:

```javascript
db.events.createIndex( { "username" : 1, "date" : -1 } )
```

However, the above index **cannot** support sorting by ascending
`username` values and then by ascending `date` values, such as the
following:

```javascript
db.events.find().sort( { username: 1, date: 1 } )
```

For more information on sort order and compound indexes, see
/tutorial/sort-results-with-indexes.

## Prefixes

Index prefixes are the *beginning* subsets of indexed fields. For
example, consider the following compound index:

```javascript
{ "item": 1, "location": 1, "stock": 1 }
```

The index has the following index prefixes:

- `{ item: 1 }`

- `{ item: 1, location: 1 }`

For a compound index, MongoDB can use the index to support queries on
the index prefixes. As such, MongoDB can use the index for queries on
the following fields:

- the `item` field,
- the `item` field *and* the `location` field,
- the `item` field *and* the `location` field *and* the `stock` field.

MongoDB can also use the index to support a query on the `item` and
`stock` fields, since the `item` field corresponds to a prefix.
However, in this case the index would not be as efficient in supporting
the query as it would be if the index were on only `item` and
`stock`.

Since a query on `item` and `stock` omits the `location` index
prefix, it cannot use the `stock` index field which follows
`location`.  Only the `item` field in the index can support this
query. See create-indexes-to-support-queries for more
information. The index: 

1. Matches keys for `item`.
2. Performs a filter within the `IXSCAN` stage on the `stock` field.
3. Returns the filtered result. 

For example, consider a query for ``"item":
"saccharomyces cerevisiae"` and `"stock": 60``. If the collection
contains 10000 documents matching ``"item":
"saccharomyces cerevisiae"`` and only 100 of those documents matching 
`"stock": 60`, the query examines 10000 keys. In the `IXSCAN`
stage, the query filters those keys by the `stock` field and only
returns 100 results to the next stage.   

MongoDB cannot use the index to support queries that include the
following fields since without the `item` field, none of the listed
fields correspond to a prefix index:

- the `location` field,

- the `stock` field, or

- the `location` and `stock` fields.

If you have a collection that has both a compound index and an index on
its prefix (e.g. `{ a: 1, b: 1 }` and `{ a: 1 }`), if neither index
has a sparse or unique constraint, then you can remove the index on the
prefix (e.g. `{ a: 1 }`). MongoDB will use the compound index in all
of the situations that it would have used the prefix index.

## Index Intersection

Starting in version 2.6, MongoDB can use index
intersection to fulfill queries. The choice
between creating compound indexes that support your queries or relying
on index intersection depends on the specifics of your system. See
index-intersection-compound-indexes for more details.

## Sparse Compound Indexes

Compound indexes can contain different types of sparse indexes. The
combination of index types determines how the compound index matches
documents. 

This table summarizes the behavior of a compound index that contains
different types of sparse indexes:

| Compound Index Components | Compound Index Behavior |
|---|---|
| \| Ascending indexes \| Descending indexes | Only indexes documents that contain a value for at least one of the keys. |
| \| Ascending indexes \| Descending indexes \| Geospatial indexes | Only indexes a document when it contains a value for one of the `geospatial` fields. Does not index documents in the ascending or descending indexes. |
| \| Ascending indexes \| Descending indexes \| Text indexes | Only indexes a document when it matches one of the `text` fields. Does not index documents in the ascending or descending indexes. |

## Additional Considerations

During index builds, applications may encounter reduced performance or
limited read/write access to the collection being indexed.

For more information on the index build process, see
index-operations, especially the
index-operations-replicated-build section.

Some drivers use `NumberLong(1)` instead of `1` to specify the index
order. The resulting indexes are the same.
