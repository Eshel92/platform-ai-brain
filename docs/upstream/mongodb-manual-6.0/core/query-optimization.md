<!-- Converted from core/query-optimization.txt (reStructuredText). Includes are inlined. -->

# Query Optimization

Indexes improve the efficiency of read operations by reducing the
amount of data that query operations need to process. This simplifies
the work associated with fulfilling queries within MongoDB.

## Create an Index to Support Read Operations

If your application queries a collection on a particular field or set
of fields, then an index on the queried field or a compound index on the set of fields can prevent the query from
scanning the whole collection to find and return the query results. For
more information about indexes, see the complete documentation of
indexes in MongoDB.

**Example:** An application queries the `inventory` collection on the

`type` field. The value of the `type` field is user-driven.

```javascript
var typeValue = <someUserInput>;
db.inventory.find( { type: typeValue } );
```

To improve the performance of this query, add an ascending or a
descending index to the `inventory` collection on the `type`
field. [#ensureIndexOrder]_ In `mongosh`, you can
create indexes using the `db.collection.createIndex()`
method:

```javascript
db.inventory.createIndex( { type: 1 } )
```

This index can prevent the above query on `type` from scanning the
whole collection to return the results.

To analyze the performance of the query with an index, see
/tutorial/analyze-query-plan.

In addition to optimizing read operations, indexes can support sort
operations and allow for a more efficient storage utilization. See
`db.collection.createIndex()` and
/indexes for more information about index
creation.

## Query Selectivity

Query selectivity refers to how well the query predicate excludes or
filters out documents in a collection. Query selectivity can determine
whether or not queries can use indexes effectively or even use indexes
at all.

More selective queries match a smaller percentage of documents. For
instance, an equality match on the unique `_id` field is highly
selective as it can match at most one document.

Less selective queries match a larger percentage of documents. Less
selective queries cannot use indexes effectively or even at all.

For instance, the inequality operators `$nin` and
`$ne` are *not* very selective since they often match a large
portion of the index. As a result, in many cases, a `$nin` or
`$ne` query with an index may perform no better than a
`$nin` or `$ne` query that must scan all documents in
a collection.

The selectivity of `regular expressions` depends on the
expressions themselves. For details, see regular expression and
index use.

## Covered Query

A covered query is a query that can be satisfied entirely using an 
index and does not have to examine any documents. An index covers a 
query when all of the following apply:

- All the fields in the query (both as specified by the application and
  as needed internally such as for sharding purposes) are part of an
  index.

- All the fields returned in the results are in the same index.

- No fields in the query are equal to `null`. For example, the
  following query predicates cannot result in covered queries:
  
  - `{ "field": null }`
  - `{ "field": { $eq: null } }`

### Example

An `inventory` collection has the following index on the `type` and
`item` fields:

```javascript
db.inventory.createIndex( { type: 1, item: 1 } )
```

The index covers the following operation which queries on the `type`
and `item` fields and returns only the `item` field:

```javascript
db.inventory.find(
   { type: "food", item:/^c/ },
   { item: 1, _id: 0 }
)
```

For the specified index to cover the query, the projection document
must explicitly specify `_id: 0` to exclude the `_id` field from
the result since the index does not include the `_id` field.

### Embedded Documents

An index can cover a query on fields within embedded documents.

For example, consider a `userdata` collection with documents of the
following form:

```javascript
db.userdata.insertOne(
   { _id: 1, user: { login: "tester" } }
)
```

The collection has the following index:

```javascript
db.userdata.createIndex(
   { "user.login": 1 }
)
```

The `{ "user.login": 1 }` index covers the following query:

```javascript
db.userdata.find(
   { "user.login": "tester" },
   { "user.login": 1, _id: 0 }
)
```

**Note:**

To index fields in embedded documents, use dot notation. See
index-embedded-fields.

### Multikey Covering

Multikey indexes can cover queries over the non-array fields
if the index tracks which field or fields cause the index to be multikey.

Multikey indexes cannot cover queries 
over array field(s).

For an example of a covered query with a multikey index, see
multikey-covered-queries on the multikey indexes page.

### Performance

Because the index contains all fields required by the query, MongoDB can both
match the query conditions
and return the results using only the index.

Querying *only* the index can be much faster than querying documents
outside of the index. Index keys are typically smaller than the
documents they catalog, and indexes are typically available in RAM or
located sequentially on disk.

### Limitations

#### Index Types

Not all index types can cover queries. For details
on covered index support, refer to the documentation page for the
corresponding index type.

#### Restrictions on Sharded Collection

When run on `mongos`, indexes can only cover queries on 
sharded collections if the index contains
the shard key.

### `explain`

To determine whether a query is a covered query, use the
`db.collection.explain()` or the `explain()`
method. See explain-output-covered-queries.
