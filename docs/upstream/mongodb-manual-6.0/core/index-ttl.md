<!-- Converted from core/index-ttl.txt (reStructuredText). Includes are inlined. -->

# TTL Indexes

**Note:**

If you are removing documents to save on storage costs, consider
Online Archive in
[MongoDB Atlas](https://www.mongodb.com/cloud?tck=docs_server). Online
Archive automatically archives infrequently accessed data to
fully-managed S3 buckets for cost-effective data
tiering.

TTL indexes are special single-field indexes that MongoDB can use to
automatically remove documents from a collection after a certain amount
of time or at a specific clock time. Data expiration is useful for certain types of information
like machine generated event data, logs, and session information that
only need to persist in a database for a finite amount of time.

You can create and manage TTL indexes in the UI for deployments hosted in [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server).

## Create a TTL Index

**Warning:**

After you create a TTL index, it might have a very large number of 
qualifying documents to delete at once. This large workload might 
cause performance issues on the server. To avoid these issues, plan 
to create the index during off hours, or delete qualifying documents 
in batches before you create the index for future documents.

To create a TTL index, use `createIndex()`.
Specify an index field that is either a date type or an array that contains date type values. 
Use the `expireAfterSeconds` option to specify a TTL value in seconds.

(Include not available offline: includes/expireAfterSeconds-range.rst)

For example, to create a TTL index on the `lastModifiedDate` field of
the `eventlog` collection, with a TTL value of `3600` seconds, use
the following operation in `mongosh`:

```javascript
db.eventlog.createIndex( { "lastModifiedDate": 1 }, { expireAfterSeconds: 3600 } )
```

If a time series collection contains documents with `timeField`
timestamps before `1970-01-01T00:00:00.000Z` or after
`2038-01-19T03:14:07.000Z`, no documents are deleted from the
collection by the TTL "time to live" feature.

## Convert a non-TTL single-field Index into a TTL Index

Starting in MongoDB 5.1, you can add the `expireAfterSeconds` option
to an existing single-field index. To change a non-TTL single-field
index to a TTL index, use the `collMod` database command:

```javascript
db.runCommand({
  "collMod": <collName>,
  "index": {
    "keyPattern": <keyPattern>,
    "expireAfterSeconds": <number>
  }
})
```

The following example converts a non-TTL single-field index with the
pattern `{ "lastModifiedDate": 1 }` into a TTL index:

```javascript
db.runCommand({
  "collMod": "tickets",
  "index": {
    "keyPattern": { "lastModifiedDate": 1 },
    "expireAfterSeconds": 100
  }
})
```

## Change the `expireAfterSeconds` value for a TTL Index

To change the `expireAfterSeconds` value for a TTL Index, use the
`collMod` database command:

```javascript
db.runCommand({
  "collMod": <collName>,
  "index": {
    "keyPattern": <keyPattern>,
    "expireAfterSeconds": <number>
  }
})
```

The following example changes the `expireAfterSeconds` value for an
index with the pattern `{ "lastModifiedDate": 1 }` on the `tickets`
collection:

```javascript
db.runCommand({
  "collMod": "tickets",
  "index": {
    "keyPattern": { "lastModifiedDate": 1 },
    "expireAfterSeconds": 100
  }
})
```

**Important:**

Consider the following before updating the `expireAfterSeconds`
parameter of a TTL index:

- Changing the `expireAfterSeconds` parameter **does not** trigger a 
  complete index rebuild. However, reducing the `expireAfterSeconds` 
  value can make many documents eligible for immediate deletion, 
  potentially causing performance issues due to the increased delete 
  operations.

- The recommended approach is to manually delete documents in 
  small batches before updating the TTL index. This helps control 
  the impact on your cluster.

- Deleting many documents can fragment storage files, additionally 
  impacting performance. You may need to run the 
  compact command on your collection or 
  perform a replica-set-initial-sync to reclaim space and 
  optimize storage.

## Behavior

### Expiration of Data

TTL indexes expire documents after the specified number of seconds has
passed since the indexed field value. The expiration threshold is
the indexed field value plus the specified number of seconds. 

If the field is an array, and there are multiple date values in the
index, MongoDB uses *lowest* (earliest) date value in the array to
calculate the expiration threshold.

If the indexed field in a document is not a
date or an array that holds one or
more date values, the document will not expire.

If a document does not contain the indexed field, the document will not
expire.

### Delete Operations

A background thread in `mongod` reads the values in the index
and removes expired documents from the collection.

In progress delete operations performed by the TTL thread appear in
`db.currentOp()` output. As the TTL thread deletes documents,
the `metrics.ttl.deletedDocuments` server status metric is
incremented.

If a time series collection contains documents with `timeField`
timestamps before `1970-01-01T00:00:00.000Z` or after
`2038-01-19T03:14:07.000Z`, no documents are deleted from the
collection by the TTL "time to live" feature.

#### Timing of the Delete Operation

MongoDB begins removing expired documents as soon as the index
finishes building on the primary. For more information on the
index build process, see index-operations.

The TTL index does not guarantee that expired data will be deleted
immediately upon expiration. There may be a delay between the time that a
document expires and the time that MongoDB removes the document from
the database.

The background task that removes expired documents runs *every 60
seconds*. As a result, documents may remain in a collection during the
period between the expiration of the document and the running of the
background task. MongoDB starts deleting documents 0 to 60 seconds after
the index completes.

Because the duration of the removal operation depends on the workload
of your `mongod` instance, expired data may exist for some
time *beyond* the 60 second period between runs of the background task.

The delete operations initiated by the TTL task run in the foreground,
like other deletes.

#### Replica Sets

On replica set members, the TTL background thread *only*
deletes documents when a member is in state primary. The TTL background
thread is idle when a member is in state secondary. Secondary members replicate
deletion operations from the primary.

### Support for Queries

A TTL index supports queries in the same way non-TTL indexes do.

## Restrictions

- TTL indexes are single-field indexes. Compound indexes do not support TTL and ignore the
  `expireAfterSeconds` option.

- The `_id` field does not support TTL indexes.

- You cannot create a TTL index on a capped collection.

- You cannot create a TTL index on a time series collection. Similar functionality is provided
  through automatic removal on time series collections instead.

- You cannot use `createIndex()` to change the
  value of `expireAfterSeconds` of an existing index. Instead use the
  `collMod` database command. See
  change-ttl-expireafterseconds-value.

- If a non-TTL single-field index already exists for a field, you
  cannot create a TTL index on the same field since you cannot create
  indexes that have the same key specification and differ only by the
  options. To change a non-TTL single-field index to a TTL index, use the
  `collMod` database command.
