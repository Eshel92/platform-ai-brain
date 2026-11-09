<!-- Converted from core/defragment-sharded-collections/stop-defragmenting-sharded-collection.txt (reStructuredText). Includes are inlined. -->

# Stop Defragmenting a Sharded Collection

Typically, you should use a shard balancing window to specify when the balancer runs
instead of manually starting and stopping defragmentation.

To manually stop defragmenting a sharded collection, use the
`configureCollectionBalancing` command with the
`defragmentCollection` option set to `false`.

## About this Task

The procedure in this task uses an example sharded collection named
`ordersShardedCollection` in a database named `test`.

You can use your own sharded collection and database in the procedure.

If you stop defragmenting a collection before defragmentation is
complete, the collection is in a partially defragmented state and
operates as usual. To resume defragmentation, restart the process.

## Before you Begin

- Start defragmenting a sharded collection. For details, see
  start-defragmenting-sharded-collection.
- Connect to `mongos`.

## Procedure

**Step 1: Stop defragmenting the collection**

Run:

```javascript
db.adminCommand(
   {
      configureCollectionBalancing: "test.ordersShardedCollection",
      defragmentCollection: false
   }
)
```

**Step 2: Ensure defragmentation stopped**

When defragmentation stops, the command output returns `ok: 1`:

```javascript
{
   ok: 1,
   '$clusterTime': {
      clusterTime: Timestamp({ t: 1678834337, i: 1 }),
      signature: {
         hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
         keyId: Long("0")
      }
   },
   operationTime: Timestamp({ t: 1678834337, i: 1 })
}
```

## Next Steps

You can start defragmentation again at any time. For details, see
start-defragmenting-sharded-collection.

## Learn More

- Start defragmenting a sharded collection
- Monitor defragmentation of a sharded collection

- Print shard status, see `db.printShardingStatus()`
- Retrieve shard status details, see `sh.status()` 
- View shard status collection fields, see
  sharding-status-collection-fields
- See active mongos instances, see sharding-status-mongoses
- Monitor shards using MongoDB Atlas, see [Review Sharded Clusters](https://www.mongodb.com/docs/atlas/review-sharded-cluster-metrics/#review-sharded-clusters/)
