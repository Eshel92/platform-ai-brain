<!-- Converted from core/defragment-sharded-collections/monitor-defragmentation-sharded-collection.txt (reStructuredText). Includes are inlined. -->

# Monitor Defragmentation of a Sharded Collection

To monitor defragmentation of a sharded collection, use the
`balancerCollectionStatus` command.

You can see the current defragmentation state and the number of
remaining chunks to process. This shows you the defragmentation
progress.

## About this Task

Defragmentation uses the following phases to reduce the number of chunks
in a collection and improve performance:

1. Merge chunks on the same shard that can be merged.
#. Migrate smaller chunks to other shards. A small chunk is one that
   contains data less than 25% of the `chunkSize` setting.
#. Merge remaining chunks on the same shard that can be merged.

The procedure in this task uses an example sharded collection named
`ordersShardedCollection` in a database named `test`.

You can use your own sharded collection and database in the procedure.

In the procedure for this task, you monitor the phases and see the
defragmentation progress.

## Before you Begin

- Start defragmenting a sharded collection. For details, see
  start-defragmenting-sharded-collection.
- Connect to `mongos`.

## Procedure

**Step 1: Monitor defragmentation**

Run:

```javascript
db.adminCommand(
   {
      balancerCollectionStatus: "test.ordersShardedCollection"
   }
)
```

**Step 2: Examine output document**

The previous command returns a document with information about
defragmentation status, current phase, and the defragmentation
work remaining. For example:

```javascript
{
   "balancerCompliant": false,
   "firstComplianceViolation": "defragmentingChunks",
   "details": {
      "currentPhase": "moveAndMergeChunks",
      "progress": { "remainingChunksToProcess": 1 }
   }
}
```

The following table describes the document fields.

* - Field
  - Type
  - Description

* - `balancerCompliant`
  - Boolean
  - `false` if collection chunks must be moved. Otherwise,
    `true`.

* - `firstComplianceViolation`
  - String
  - Indicates the reason that chunks for the namespace must be
    moved or merged. Only returned if `balancerCompliant` is
    `false`.

* - `details`
  - Object
  - Addtional information about the current defragmentation
    state. Only returned if `firstComplianceViolation` is
    `defragmentingChunks`.

* - `currentPhase`
  - String
  - Current defragmentation phase:

    - For phase one, `currentPhase` is
      `mergeAndMeasureChunks`.

      Phase one merges contiguous chunks located on the same
      shard and calculates the data size for those chunks.

    - For phase two, `currentPhase` is
      `moveAndMergeChunks`.

      After phase one is complete, there might be some small
      chunks remaining. Phase two migrates those small chunks
      to other shards and merges the chunks on those shards.

* - `remainingChunksToProcess`
  - Integer
  - Number of remaining chunks to process in the current phase.

For additional information about the returned document fields, see
the balancer collection status output document.

**Step 3: Confirm that defragmentation is complete**

After defragmentation completes, the command returns either:

- `balancerCompliant: true` if your collection is balanced.
- `balancerCompliant: false` with `firstComplianceViolation`
  set to a string other than `defragmentingChunks` if
  your collection is not balanced.

Example output for a balanced collection after defragmentation
completes:

```javascript
{
   chunkSize: 0.2,
   balancerCompliant: true,
   ok: 1,
   '$clusterTime': {
      clusterTime: Timestamp({ t: 1677543079, i: 1 }),
      signature: {
         hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
         keyId: Long("0")
      }
   },
   operationTime: Timestamp({ t: 1677543079, i: 1 })
}
```

## Next Steps

If defragmentation has not yet completed, you can stop it. For details,
see stop-defragmenting-sharded-collection.

## Learn More

- Start defragmenting a sharded collection
- Stop defragmenting a sharded collection
- To view the balancer collection status output document, see
  Balancer collection status output document

- Print shard status, see `db.printShardingStatus()`
- Retrieve shard status details, see `sh.status()` 
- View shard status collection fields, see
  sharding-status-collection-fields
- See active mongos instances, see sharding-status-mongoses
- Monitor shards using MongoDB Atlas, see [Review Sharded Clusters](https://www.mongodb.com/docs/atlas/review-sharded-cluster-metrics/#review-sharded-clusters/)
