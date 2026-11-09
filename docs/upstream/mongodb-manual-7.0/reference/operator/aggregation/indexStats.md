<!-- Converted from reference/operator/aggregation/indexStats.txt (reStructuredText). Includes are inlined. -->

# $indexStats (aggregation stage)

## Definition

**`$indexStats`**

Returns statistics regarding the use of each index for the
collection. If running with access control, 
authenticate as a user with at least the `clusterMonitor` role.

The `$indexStats` stage takes an empty document and has
the following syntax:

```javascript
{ $indexStats: { } }
```

For each index, the return document includes the following fields:

* - Output Field
  - Description

* - `name`
  - Index name.

* - key
  - .. _indexStats-output-key:

    Index key specification.

    See also: spec.

* - host

  - .. _indexStats-output-host:

    The hostname and port of the `mongod` process.

* - accesses

  - .. _indexStats-output-accesses:

    Index usage metrics for the associated host, including: 

    - `ops`: the number of user operations that used the index.
      This value excludes internal operations, such as deletion
      by TTL indexes or chunk split
      and migration operations. This exclusion also covers index
      access from replication, such as oplog application and
      index builds during initial sync.

    - `since`: the time from which MongoDB gathered the
      statistics

    WARNING: The `accesses` field reports index usage
    metrics only for the node where the query runs. For more
    comprehensive index usage statistics, run
    `$indexStats` on each node in the cluster.

* - shard

  - .. _indexStats-output-shard:

    The name of the shard associated with the host

    Only available for a sharded cluster.

* - spec

  - .. _indexStats-output-spec:

    The full specification document for the index, which includes
    the index key and index properties.

    The index option `hidden` is only included if the value is `true`.

* - building

  - .. _indexStats-output-building:

    Indicates if the index is currently being built.

    Only available if `true`.

## Behavior

### Accesses Field

The statistics reported by the accesses field only apply to the node where
the query is being run and only include index access driven
by user requests. The `accesses` field excludes the following
internal operations:

- Deletion by TTL indexes
- Chunk split and migration operations
- Index access from replication, such as oplog application and
  index builds during initial sync

### Restrictions

- `$indexStats` must be the first stage in an aggregation pipeline.

- `$indexStats` is not allowed in transactions.

### Index Statistics Reset Considerations

- Statistics for an index reset on `mongod`
  restart or index drop and recreation.
- Modification of an existing index (see `collMod`
  command) resets the statistics for that index.

## Examples

**shell:**

The following example uses the `movies` collection from the sample_mflix
sample dataset.  For details on how to load this dataset into
your deployment, see Load the sample dataset.

Create the following indexes on the `movies` collection:

```javascript
db.movies.createIndex( { year: 1, title: 1 } )
db.movies.createIndex( { rated: 1, year: 1 } )
db.movies.createIndex(
   { metacritic: 1 },
   { partialFilterExpression: { rated: "R" } }
)
```

Run some queries against the collection:

```javascript
db.movies.find( { rated: "R" } )
db.movies.find( { year: 1994 } ).sort( { title: 1 } )
db.movies.find( { metacritic: { $gt: 90 } } )
```

The following aggregation operation returns a document that contains
usage statistics for each index on the `movies` collection:

```javascript
```

Output:

```javascript
```

**nodejs:**

To use the MongoDB Node.js driver to add a `$indexStats` stage to an aggregation
pipeline, use the `$indexStats` operator in a pipeline object.

The following example creates a pipeline stage that returns a document that contains usage statistics for each index on
the collection. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [{ $indexStats: {} }];

const cursor = collection.aggregate(pipeline);
return cursor;
```
