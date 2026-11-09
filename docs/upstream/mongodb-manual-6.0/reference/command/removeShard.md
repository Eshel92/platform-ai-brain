<!-- Converted from reference/command/removeShard.txt (reStructuredText). Includes are inlined. -->

# removeShard

## Definition

**`removeShard`**

Removes a shard from a sharded cluster. When you run
`removeShard`, MongoDB drains the shard by using the balancer to
move the shard's chunks to other shards in the cluster. Once the shard is
drained, MongoDB removes the shard from the cluster.

**Note:**

If you want to re-add a removed shard to your sharded cluster, you
must clear the `storage.dbPath` of all the nodes of the
shard to remove the shard's files of before you can re-add it. 

## Compatibility

This command is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**Note:**

This command is not supported in [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server). See [Modify your Atlas Sharded Cluster](https://www.mongodb.com/docs/atlas/scale-cluster/#modify-the-number-of-shards)
to add or remove shards from your Atlas cluster.

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     removeShard : <shardToRemove> 
   } 
)
```

## Behavior

### No Cluster Back Ups During Shard Removal

You cannot back up the cluster data during shard removal.

### Concurrent `removeShard` Operations

You can have more than one `removeShard` operation in progress.

### Access Requirements

If you have `authorization` enabled, you must have the
`clusterManager` role or any role that
includes the `removeShard` action.

### Database Migration Requirements

Each database in a sharded cluster has a primary shard. If the shard you
want to remove is also the primary of one of the cluster's databases, then
you must manually move the databases to a new shard after migrating
all data from the shard. See the `movePrimary` command and
the /tutorial/remove-shards-from-cluster for more information.

### Chunk Balancing

When you remove a shard in a cluster with an uneven chunk
distribution, the balancer first removes the chunks from the draining
shard and then balances the remaining uneven chunk distribution.

**See also:**

`balancerCollectionStatus`

### Write Concern

`mongos` converts the
write concern of the
`removeShard` command to `"majority"`.

### Change Streams

A shard removal may cause an open change stream cursor to close, and the closed change stream cursor may
not be fully resumable.

## Example

From `mongosh`, the `removeShard`
operation resembles the following:

```javascript
db.adminCommand( { removeShard : "bristol01" } )
```

Replace `bristol01` with the name of the shard to remove. When you
run `removeShard`, the command returns with a message that
resembles the following:

```javascript
{
   "msg" : "draining started successfully",
   "state" : "started",
   "shard" : "bristol01",
   "note" : "you need to drop or movePrimary these databases", 
   "dbsToMove" : [
      "fizz",
      "buzz"
   ],
   "ok" : 1,
   "operationTime" : Timestamp(1575398919, 2),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1575398919, 2),
      "signature" : {
         "hash" : BinData(0,"Oi68poWCFCA7b9kyhIcg+TzaGiA="),
         "keyId" : NumberLong("6766255701040824328")
      }
   }
}
```

The balancer begins migrating ("draining") chunks from the shard named
`bristol01` to other shards in the cluster. These migrations happen
slowly in order to avoid placing undue load on the cluster.

The output includes the field `dbsToMove` indicating the databases
for which `bristol01` is the primary shard.
After all chunks have been drained from the shard, you must either
`movePrimary` for the database(s) or alternatively, drop
these databases.

**Note:**

If the shard you are removing is not the primary shard for any
database, the `dbsToMove` array will be empty and
`removeShard` can complete the migration without
intervention.

If you run the command again, `removeShard` returns the
current status of the process. For example, if the operaton is in an
`ongoing` state, the command returns an output that resembles the
following:

```javascript
{
   "msg" : "draining ongoing",
   "state" : "ongoing",
   "remaining" : {
      "chunks" : NumberLong(2),
      "dbs" : NumberLong(2),
      "jumboChunks" : NumberLong(0)
   },
   "note" : "you need to drop or movePrimary these databases",
   "dbsToMove" : [
      "fizz",
      "buzz"
   ],
   "ok" : 1,
   "operationTime" : Timestamp(1575399086, 1655),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1575399086, 1655),
      "signature" : {
         "hash" : BinData(0,"XBrTmjMMe82fUtVLRm13GBVtRE8="),
         "keyId" : NumberLong("6766255701040824328")
      }
   }
}
```

In the output, the `remaining` field includes the following fields:

| Field | Description |
|---|---|
| `chunks` | Total number of chunks currently remaining on the shard. |
| `dbs` | Total number of databases whose primary shard is the shard. These databases are specified in the `dbsToMove` output field. |
| `jumboChunks` | Of the total number of `chunks`, the number that are jumbo. If the `jumboChunks` is greater than 0, wait until only the `jumboChunks` remain on the shard. Once only the jumbo chunks remain, you must manually clear the jumbo flag before the draining can complete. See /tutorial/clear-jumbo-flag. After the `jumbo` flag clears, the balancer can migrate these chunks. For details on the migration procedure, see range-migration-procedure. |

Continue checking the status of the `removeShard` command
(i.e. rerun the command) until the number of chunks remaining is `0`.

```javascript
{
   "msg" : "draining ongoing",
   "state" : "ongoing",
   "remaining" : {
      "chunks" : NumberLong(0),             // All chunks have moved
      "dbs" : NumberLong(2),
      "jumboChunks" : NumberLong(0)         
   },
   "note" : "you need to drop or movePrimary these databases",
   "dbsToMove" : [
      "fizz",
      "buzz"
   ],
   "ok" : 1,
   "operationTime" : Timestamp(1575400343, 1),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1575400343, 1),
      "signature" : {
         "hash" : BinData(0,"9plu5B/hw4uWAgEmjjBP3syw1Zk="),
         "keyId" : NumberLong("6766255701040824328")
      }
   }
}
```

After all chunks have been drained from the shard, if you have
`dbsToMove`, you can either `movePrimary` for those
databases or alternatively, drop the databases (which deletes the
associated data files).

After the balancer completes moving all chunks off the shard and you
have handled the `dbsToMove`, `removeShard` can finish.
Running `removeShard` again returns output that resembles
the following:

```javascript
{
   "msg" : "removeshard completed successfully",
   "state" : "completed",
   "shard" : "bristol01",
   "ok" : 1,
   "operationTime" : Timestamp(1575400370, 2),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1575400370, 2),
      "signature" : {
         "hash" : BinData(0,"JjSRciHECXDBXo0e5nJv9mdRG8M="),
         "keyId" : NumberLong("6766255701040824328")
      }
   }
}
```
