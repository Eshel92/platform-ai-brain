<!-- Converted from core/timeseries/timeseries-limitations.txt (reStructuredText). Includes are inlined. -->

# Time Series Collection Limitations

This page describes limitations on using time series collections.

## Unsupported Features

The following features are not supported for time series collections:

* Atlas Search
* Change streams
* Client-Side Field Level Encryption
* `Database Triggers`
* Schema validation rules
* `reIndex`
* `renameCollection`

`Atlas Device Sync` support is limited to time
series collections that use `Atlas Data Ingest`.

## Aggregation $out and $merge

You cannot use the `$out` or `$merge` aggregation
pipeline stages to add data from another collection to a time series
collection.

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

## Document Size

The maximum size for documents within a time series collection is 4 MB.

## Updates and Deletes

Starting in MongoDB 5.1, you can perform some delete and update
operations.

Delete commands must meet the following requirements:

- You can only match on metaField field
  values.
- Your delete command must not limit the number of documents to be
  deleted. Set `justOne: false` or use the
  `deleteMany()` method.

If a time series collection contains documents with `timeField`
timestamps before `1970-01-01T00:00:00.000Z` or after
`2038-01-19T03:14:07.000Z`, no documents are deleted from the
collection by the TTL "time to live" feature.

For details on TTL deletes, see ttl-collections.

Update commands must meet the following requirements:

- You can only match on the `metaField` field value.
- You can only modify the `metaField` field value.
- Your update document can only contain update operator expressions.
- Your update command must not limit the number of documents to be
  updated. Set `multi: true` or use the
  `updateMany()` method. 
- Your update command must not set upsert: true.

In MongoDB 5.0, time series collections only support insert operations
and read queries. Updates and manual delete operations result in an
error.

To automatically delete old data, set up automatic removal (TTL).

To remove all documents from a collection, use the
`drop()` method to drop the collection.

## Time Series Secondary Indexes

There is improved support for secondary indexes in MongoDB 6.0.

### Time Series Secondary Indexes with MongoDB 6.0 and Later

Starting in MongoDB 6.0, you can add a secondary index to any field.

These index types are not supported:

- Text indexes
- Unique indexes

The TTL index property is not supported. For
TTL deletion, use expireAfterSeconds.

The following index types can only be created on the `metaField`:

- 2d indexes
- Multikey indexes
- Sparse indexes

For improvements to time series secondary indexes available starting in
MongoDB 6.0, see timeseries-add-secondary-index-mongodb-6.0.

If there are secondary indexes on time
series collections and you need to
downgrade the feature compatibility version (FCV), you must first drop
any secondary indexes that are incompatible with the downgraded FCV.
For more information, see `setFeatureCompatibilityVersion`.

### Time Series Secondary Indexes with MongoDB 5.0 and Earlier

In MongoDB 5.0 and earlier:

- The `metaField` can have secondary indexes.
- The `timeField`  can have secondary indexes.
- If the `metaField` is a document, you can add secondary indexes on
  fields inside the document.

**See also:**

indexes

## Capped Collections

You cannot create a time series collection as a capped collection.

## Modification of Collection Type

You can only set the collection type when you create a collection:

- An existing collection cannot be converted into a time series
  collection.
- A time series collection cannot be converted into a different
  collection type.

To move data from an existing collection to a time series collection,
migrate data into a time series collection.

## Modification of `timeField` and `metaField`

You can only set a collection's `timeField` and `metaField`
parameters when you create the collection. You cannot modify these
parameters later.

## Modification of `granularity`

After you set the `granularity`, you can only increase it one level at
a time. The `granularity` can change from `"seconds"` to
`"minutes"` or from `"minutes"` to `"hours"`. Other changes are
not allowed. 

To change the `granularity` from `"seconds"` to `"hours"`, first
increase the `granularity` to `"minutes"` and then to `"hours"`.

## Sharding

Starting in MongoDB 5.1 (and 5.0.6), you can create sharded time series
collections.

In versions earlier than MongoDB 5.0.6, you cannot shard time series
collections.

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
- [MongoDB Blog: On Selecting a Shard Key for MongoDB](https://www.mongodb.com/blog/post/on-selecting-a-shard-key-for-mongodb?tck=docs_server).

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

Reads from time series collections are supported in transactions.

## View Limitations

Time series collections are writable non-materialized views. Limitations
for views apply to time series collections.

- You cannot create a view from a time series bucket collection
  namespace (namely, a collection prefixed with `system.buckets`).

## Snapshot Isolation

Read operations on time series collections with read concern
`"snapshot"` guarantee snapshot isolation only in the absence of
concurrent drop or rename operations on collections in the read
operation. Re-creating a time series collection on the same namespace
with different granularity setting does not yield full snapshot
isolation.
