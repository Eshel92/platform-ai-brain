<!-- Converted from core/timeseries/timeseries-limitations.txt (reStructuredText). Includes are inlined. -->

# Time Series Collection Limitations

Time series collections generally
behave like regular collections with several limitations.

## Unsupported Features

MongoDB does not support the following features with time series collections:

* Atlas Search
* Change streams
* Client-Side Field Level Encryption
* Database Triggers
* Schema validation rules
* `reIndex`
* `renameCollection`

(Text shared from another MongoDB docs repo, not available offline: cet/atlas/asp-limitations.rst)

## Aggregation $merge

You cannot use the `$merge` aggregation stage to add data from
another collection to a time series collection. Use the `$out`
aggregation stage to write documents to a time series collection. 

You can use `$merge` to move data from a time series
collection to another collection.

## distinct Command

Due to the unique data structure of time series collections, MongoDB can't
efficiently index them for distinct values. Avoid using the
`distinct` command or `db.collection.distinct()` helper
method on time series collections. Instead, use a `$group` 
aggregation to group documents by distinct values. 

For example, to query for distinct `meta.type` values on documents
where `meta.project = 10`, instead of:

```javascript
db.foo.distinct("meta.type", {"meta.project": 10})
```

Use:

```javascript
db.foo.createIndex({"meta.project":1, "meta.type":1})
db.foo.aggregate([{$match: {"meta.project": 10}},
                  {$group: {_id: "$meta.type"}}])
```

This works as follows:

#. Creating a compound index on `meta.project`
   and `meta.type` and supports the aggregation. 

#. The `$match` stage filters for documents where `meta.project = 10`.

#. The `$group` stage uses `meta.type` as the group key to output
   one document per unique value.

## Geospatial Queries

Time series collections only support the `$geoNear`
aggregation stage for sorting geospatial data from queries against 2dsphere indexes. You can't use `$near` and
`$nearSphere` operators on time series collections.

### $geoNear

You can't use the `query` field for `$geoNear` on a 
time series collection.

You must specify the `key` field for `$geoNear` on a 
time series collection.

## Document Size

The maximum size for documents within a time series collection is 4 MB.

## Extended Date Range

If your time series collection contains  documents with `timeField`
timestamps before `1970-01-01T00:00:00.000Z` or after
`2038-01-19T03:14:07.000Z`, create an index on the `timeField` to
optimize queries.  

## Updates

Update commands must meet the following requirements:

- You can only match on the `metaField` field value.
- You can only modify the `metaField` field value.
- Your update document can only contain update operator expressions.
- Your update command must not limit the number of documents to be
  updated. Set `multi: true` or use the
  `updateMany()` method. 
- Your update command must not set upsert: true.

To automatically delete old data, set up automatic removal (TTL).

## Time Series Secondary Indexes

MongoDB partially supports the following indexes on time series collections:
 
- You can only create multikey indexes on
  the `metaField`.
- You can only create 2d indexes on the `metaField`. 
- You can only create sparse indexes on the `metaField`.

MongoDB doesn't support the following index types on time series collections:

- Text indexes
- Unique indexes

If there are secondary indexes on time
series collections and you need to
downgrade the feature compatibility version (FCV), you must first drop
any secondary indexes that are incompatible with the downgraded FCV.
For more information, see `setFeatureCompatibilityVersion`.

## Capped Collections

You cannot create a time series collection as a capped collection.

## Modification of Collection Type

You can only set the collection type when you create a collection:

- You cannot convert an existing collection into a time series
  collection.
- You cannot convert a time series collection into a different
  collection type.

To move data from an existing collection to a time series collection,
migrate data into a time series collection.

## Modification of `timeField` and `metaField`

You can only set a collection's `timeField` and `metaField`
parameters when you create the collection. You cannot modify these
parameters later.

## Granularity

### Bucket Size

For any configuration of granularity parameters, the maximum
size of a bucket is 1000 measurements or 125KB of data,
whichever is lower. MongoDB may also enforce a lower maximum size for 
high cardinality data with many unique values, so that the working set 
of buckets fits within the WiredTiger cache.

### Modifying Bucket Parameters

Once you set a collection's `granularity` or the custom bucketing
parameters `bucketMaxSpanSeconds` and `bucketRoundingSeconds`, you
can increase the time span covered by a bucket, but not decrease it.
Use the `collMod` command to modify the parameters. For example:

```javascript
db.runCommand({
   collMod: "timeseries",
   timeseries: { bucketMaxSpanSeconds: 3600, bucketRoundingSeconds: 3600 }
})
```

   

**Note:**

`bucketMaxSpanSeconds` and `bucketRoundingSeconds` must be
equal. If you modify one parameter, you must also set the other to
the same value.

## Sharding

Time series collections are subject to several sharding limitations. 

### Sharding Administration Commands

You cannot run sharding administration commands on sharded time series 
collections. 

### Shard Key Fields

When sharding time series collections, you can only specify
the following fields in the shard key:

- The `metaField`
- Sub-fields of `metaField`
- The `timeField`

You may specify combinations of these fields in the shard key. No other
fields, including `_id`, are allowed in the shard key pattern.

When you specify the shard key:

- `metaField` can be either a:

  - Hashed shard key
  - Ranged shard key

- `timeField` must be:

  - A ranged shard key
  - At the end of the shard key pattern

**Tip:**

Avoid specifying **only** the `timeField` as the shard key. Since
the `timeField` increases monotonically, it may result in all writes appearing on a
single chunk within the cluster. Ideally, data is evenly distributed
across chunks.

To learn how to best choose a shard key, see:

- sharding-shard-key-requirements
- [MongoDB Blog: On Selecting a Shard Key for MongoDB](https://www.mongodb.com/blog/post/on-selecting-a-shard-key-for-mongodb).

### Resharding

You cannot reshard a sharded time series collection. However, you can 
refine its shard key.

### Zone Sharding

Zone sharding does not support time series collections. The
balancer always distributes data in sharded time series
collections evenly across all shards in the cluster.

## Transactions

You cannot write to time series collections in transactions.

**Note:**

MongoDB supports reads from time series collections in transactions.

## Views

- Time series collections are writable non-materialized views. Limitations for views apply to time series
  collections.

- You cannot create a view from a time series bucket collection
  namespace (namely, a collection prefixed with `system.buckets`).

## Snapshot Isolation

Read operations on time series collections with read concern
`"snapshot"` guarantee snapshot isolation only in the absence of
concurrent drop or rename operations on collections in the read
operation. Re-creating a time series collection on the same namespace
with different granularity setting does not yield full snapshot
isolation.
