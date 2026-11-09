<!-- Converted from core/sharded-cluster-requirements.txt (reStructuredText). Includes are inlined. -->

# Operational Restrictions in Sharded Clusters

## Sharding Operational Restrictions

### Operations Unavailable in Sharded Environments

`$where` does not permit references to the `db` object
from the `$where` function. This is uncommon in
un-sharded collections.

The `geoSearch` command is not supported in sharded
environments.

In MongoDB 5.0 and earlier, you cannot specify sharded collections in the `from` parameter of `$lookup` stages.

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

**See also:**

shard-key-arbitrary-uniqueness for an alternate approach.

### Write Concern for DDL Operations

On a sharded cluster, DDL (Data Definition Language) operations run with write concern `"majority"`. If
you specify a different write concern, the operation overrides the
provided write concern with `"majority"`.
