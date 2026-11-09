<!-- Converted from core/sharding-reshard-a-collection.txt (reStructuredText). Includes are inlined. -->

# Reshard a Collection

**New in version:** 5.0

The ideal shard key allows MongoDB to distribute documents evenly
throughout the cluster while facilitating common query patterns. A
suboptimal shard key can lead to performance or scaling issues due to
uneven data distribution. Starting in MongoDB 5.0, you can change the
shard key for a collection to change the distribution of your data
across a cluster.

**Note:**

Before resharding your collection, read
shardkey-troubleshoot-shard-keys for information on common
performance and scaling issues and advice on how to fix them.

## About this Task

- Only one collection can be resharded at a time.
- `writeConcernMajorityJournalDefault` must be `true`.
- To reshard a collection that has a uniqueness constraint, the new shard key must satisfy
  the unique index requirements for 
  any existing unique indexes.
- The following commands and corresponding shell methods are not
  supported on the collection that is being resharded while the
  resharding operation is in progress:

  - `collMod`
  - `convertToCapped`
  - `createIndexes`
  - `createIndex()`
  - `drop`
  - `drop()`
  - `dropIndexes`
  - `dropIndex()`
  - `renameCollection`
  - `renameCollection()`

- The following commands and methods are not supported on the cluster
  while the resharding operation is in progress:

  - `addShard`
  - `removeShard`
  - `db.createCollection()`
  - `dropDatabase`

  **Warning:**

  Using any of the preceding commands during a resharding
  operation causes the resharding operation to fail.

- If the collection to be resharded uses Atlas Search, the search index will become unavailable when the
  resharding operation completes. You need to manually rebuild the
  search index once the resharding operation completes.

- You can't reshard a sharded time series collection.

## Before you Begin

Before you reshard your collection, ensure that you meet the following
requirements:

- Your application can tolerate a period of **two seconds** where the
  collection that is being resharded blocks writes. During the time
  period where writes are blocked your application experiences an
  increase in latency. If your workload cannot tolerate this
  requirement, consider refining your shard key instead.
- Your database meets these resource requirements:

  - Available storage space: Ensure that the available storage
    space on each shard the collection will be distributed
    across is at least twice the size of the collection
    that you want to reshard and its total index size, divided
    by the number of shards. 

    ```none
    storage_req = ( ( collection_size + index_size ) * 2 ) / shard_count
    ```

    For example, consider a collection that contains 2 TB of
    data and has a 400 GB index distributed across four shards.
    To perform a resharding operation on this collection, each
    shard would require 1.2 TB of available storage.

    ```none
    1.2 TB storage = ( ( 2 TB collection + 0.4 TB index ) * 2 ) / 4 shards
    ```

    To meet storage requirements, you may need to upgrade to
    the next tier of storage during the resharding operation.
    You can scale down once the operation completes.

  -  I/O: Ensure that your I/O capacity is below 50%.
  -  CPU load: Ensure that your CPU load is below 80%.

  **Important:**

  These requirements are not enforced by the database. A failure to
  allocate enough resources can result in:

  - the database running out of space and shutting down
  - decreased performance
  - the resharding operation taking longer than expected

  If your application has time periods with less traffic, reshard your
  collection during that time if possible.

- You must rewrite your application's queries to use **both** the
  current shard key and the new shard key.

  **Tip:**

  If your application can tolerate downtime, you can perform these
  steps to avoid rewriting your application's queries to use both the
  current and new shard keys:

  #. Stop your application.

  #. Rewrite your application to use the **new** shard key.

  #. Wait until resharding completes. To monitor the resharding
     process, use the `$currentOp` pipeline stage.

  #. Deploy your rewritten application.

  Before resharding completes, the following queries return an error if
  the query filter does not include either the current shard key or a
  unique field (like `_id`):

  - `deleteOne()`
  - `findAndModify()`
  - `findOneAndDelete()`
  - `findOneAndReplace()`
  - `findOneAndUpdate()`
  - `replaceOne()`
  - `updateOne()`

  These operations also return an error after the resharding
  operation completes if the query filter does not include the new
  shard key or a unique field (like `_id`).

  For optimal performance, we recommend that you also rewrite other
  queries to include the new shard key.

  Once the resharding operation completes, you can remove the old shard
  key from the queries.

- You do not need to create an index on the new shard key before
  resharding. The resharding operation builds the required indexes
  automatically during the index phase.

- No index builds are in progress. To check for running index builds,
  use `$currentOp`:

  ```javascript
  db.getSiblingDB("admin").aggregate( [
     { $currentOp : { idleConnections: true } },
     { $match: {
           $or: [
               { "op": "command", "command.createIndexes": { $exists: true } },
               { "op": "none", "msg": /^Index Build/ }
           ]
        }
     }
  ] )
  ```

  In the result document, if the `inprog` field value is an empty
  array, there are no index builds in progress:

  ```javascript
  {
     inprog: [],
     ok: 1,
     '$clusterTime': { ... },
     operationTime: <timestamp>
  }
  ```

**Note:**

Resharding is a write-intensive process which can generate increased rates 
of oplog. You may wish to:

- set a fixed oplog size to prevent unbounded oplog growth.
- increase the oplog size to minimize the chance that one or more
  secondary nodes becomes stale.

See the replica-set-oplog documentation for more details.

## Steps

**Important:**

We strongly recommend that you check the
resharding-limitations and read the resharding_process
section in full before resharding your collection.

In a collection resharding operation, a shard can be a:

- **donor**, which currently stores chunks for the
  sharded collection.
- **recipient**, which stores new chunks for the sharded collection
  based on the shard keys and zones.

A shard can be donor and a recipient at the same time. The set of donor
shards is identical to the recipient shards, unless you use zones.

The config server primary is always the resharding coordinator and
starts each phase of the resharding operation.

**Step 1: Disable the Balancer**

You must turn off the balancer before you begin the process of resharding a collection. 
To disable the balancer, see [here](https://www.mongodb.com/docs/manual/tutorial/manage-sharded-cluster-balancer/#disable-the-balancer).

**Step 2: Start the resharding operation.**

While connected to the `mongos`, issue a
`reshardCollection` command that specifies the collection
to be resharded and the new shard key:

```javascript
db.adminCommand({
  reshardCollection: "<database>.<collection>",
  key: <shardkey>
})
```

MongoDB sets the max number of seconds to block writes to two seconds
and begins the resharding operation.

**Step 3: Monitor the resharding operation.**

To monitor the resharding operation, you can use the
`$currentOp` pipeline stage:

```javascript
db.getSiblingDB("admin").aggregate([
  { $currentOp: { allUsers: true, localOps: false } },
  {
    $match: {
      type: "op",
      "originatingCommand.reshardCollection": "<database>.<collection>"
    }
  }
])
```

**Note:**

To see updated values, you need to continuously run the
preceeding pipeline.

The `$currentOp` pipeline outputs:

- `totalOperationTimeElapsedSecs`: elapsed operation time in
  seconds
- .. include:: /includes/remainingOperationTimeEstimatedSecs-details.rst

```javascript
[
  {
    shard: '<shard>',
    type: 'op',
    desc: 'ReshardingRecipientService | ReshardingDonorService | ReshardingCoordinatorService <reshardingUUID>',
    op: 'command',
    ns: '<database>.<collection>',
    originatingCommand: {
      reshardCollection: '<database>.<collection>',
      key: <shardkey>,
      unique: <boolean>,
      collation: { locale: 'simple' }
    },
    totalOperationTimeElapsedSecs: <number>,
    remainingOperationTimeEstimatedSecs: <number>,
    ...
  },
  ...
]
```

**Step 4: Re-enable the Balancer.**

To enable the balancer, see [here](https://www.mongodb.com/docs/manual/tutorial/manage-sharded-cluster-balancer/#enable-the-balancer).

## Behavior

### Minimum Duration of a Resharding Operation

The minimum duration of a resharding operation is always 5 minutes.

### Retryable Writes

Retryable writes initiated before or during
resharding can be retried during and after the collection has been
resharded for up to 5 minutes. After 5 minutes you may be unable to find
the definitive result of the write and subsequent attempts to retry the
write fail with an `IncompleteTransactionHistory` error.

## Error Case

### Duplicate `_id` Values

The resharding operation fails if `_id` values are not globally unique
to avoid corrupting collection data. Duplicate `_id` values can also
prevent successful chunk migration. If you have documents with duplicate
`_id` values, copy the data from each into a new document, and then
delete the duplicate documents.
