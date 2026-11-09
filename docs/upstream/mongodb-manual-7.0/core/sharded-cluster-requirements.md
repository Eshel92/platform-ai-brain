<!-- Converted from core/sharded-cluster-requirements.txt (reStructuredText). Includes are inlined. -->

# Operational Restrictions in Sharded Clusters

## Sharding Operational Restrictions

### Operations Unavailable in Sharded Environments

`$where` does not permit references to the `db` object
from the `$where` function. This is uncommon in
un-sharded collections.

### Single Document Modification Operations in Sharded Collections

   and `deleteOne()`

To use `updateOne()` operations for a sharded
collection that specify the `multi: false` or `justOne` option: 

- If you only target one shard, you can use a partial shard key in the query specification or,

- You can provide the shard key or the `_id` field in the query
  specification.

To use `findOneAndUpdate()` with a sharded
collection, your query filter must include an equality condition on the
shard key to compare the key and value in either of these
formats:

```javascript
{ key: value }
{ key: { $eq: value } }
```

### Unique Indexes in Sharded Collections

MongoDB does not support unique indexes across shards, except when
the unique index contains the full shard key as a prefix of the
index. In these situations MongoDB will enforce uniqueness across
the full key, not a single field.

To learn more, see manual-maintain-uniqueness-sharded.

### Consistent Indexes

MongoDB does not guarantee consistent indexes across shards.  Index creation
during `addShard` operations or chunk migrations may not propagate
to new shards.

To check a sharded cluster for consistent indexes, use the
`checkMetadataConsistency` command:

```javascript
db.runCommand( {
   checkMetadataConsistency: 1,
   checkIndexes: true
} )
```

### Write Concern for DDL Operations

On a sharded cluster, DDL (Data Definition Language) operations run with write concern `"majority"`. If
you specify a different write concern, the operation overrides the
provided write concern with `"majority"`.
