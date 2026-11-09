<!-- Converted from tutorial/remove-shards-from-cluster.txt (reStructuredText). Includes are inlined. -->

# Remove Shards from an Existing Sharded Cluster

To remove a shard you must ensure the shard's data is migrated
to the remaining shards in the cluster. This procedure describes how to
safely migrate data and how to remove a shard.

When you remove a shard in a cluster with an uneven chunk
distribution, the balancer first removes the chunks from the draining
shard and then balances the remaining uneven chunk distribution.

This procedure describes how to remove a shard from a cluster.
*Do not* use this procedure to migrate an entire cluster to new
hardware. To migrate, see
/tutorial/migrate-sharded-cluster-to-new-hardware instead.

To remove a shard, first connect to one of the cluster's
`mongos` instances using `mongosh`. Then use
the sequence of tasks in this document to remove a shard from the
cluster.

## Considerations

- .. include:: /includes/extracts/changestream-remove-shard-with-link.rst

- You can safely restart a cluster during a shard removal process. If
  you restart a cluster during an ongoing draining process,
  draining continues automatically after the cluster components restart.
  MongoDB records the shard draining status in the `config.shards`
  collection.

## Ensure the Balancer Process is Enabled

To successfully migrate data from a shard, the balancer process
**must** be enabled. Check the balancer state using the
`sh.getBalancerState()` helper in `mongosh`.
For more information, see the section on balancer operations.

## Determine the Name of the Shard to Remove

To determine the name of the shard, connect to a `mongos`
instance with `mongosh` and either:

- Use the `listShards` command, as in the following:

  ```javascript
  db.adminCommand( { listShards: 1 } )
  ```

- Run either the `sh.status()` or the
  `db.printShardingStatus()` method.

The `shards._id` field lists the name of each shard.

## Remove Chunks from the Shard

From the `admin` database, run the `removeShard` command.
This begins "draining" chunks
from the shard you are removing to other shards in the cluster. For
example, for a shard named `mongodb0`, run:

```javascript
db.adminCommand( { removeShard: "mongodb0" } )
```

`mongos` converts the
write concern of the
`removeShard` command to `"majority"`.

This operation returns with the following response:

```javascript
{
   "msg" : "draining started successfully",
   "state" : "started",
   "shard" : "mongodb0",
   "note" : "you need to drop or movePrimary these databases", 
   "dbsToMove" : [
      "fiz",
      "buzz"
   ],
   "ok" : 1,
   "operationTime" : Timestamp(1575398919, 2),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1575398919, 2),
      "signature" : {
         "hash" : BinData(0,"Oi68poWCFCA7b9kyhIcg+TzaGiA="),
         "keyId" : Long("6766255701040824328")
      }
   }
}
```

The balancer begins migrating chunks from the shard named `mongodb0`
to other shards in the cluster. These migrations happens slowly to
avoid placing undue load on the overall cluster.
Depending on your network capacity and the amount of data, this
operation can take from a few minutes to several days to complete.

**Note:**

The output includes the field `dbsToMove` indicating the
databases, if any, for which the shard is the primary shard. After all chunks have been drained from the shard,
you must either `movePrimary` for the database(s) or
alternatively, drop the databases (which deletes the associated data
files).

## Check the Status of the Migration

To check the progress of the migration at any stage in the process, run
`removeShard` from the `admin` database again. For example,
for a shard named `mongodb0`, run:

```javascript
db.adminCommand( { removeShard: "mongodb0" } )
```

`mongos` converts the
write concern of the
`removeShard` command to `"majority"`.

The command returns output similar to the following:

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
| `jumboChunks` | Of the total number of `chunks`, the number that are jumbo. If the `jumboChunks` is greater than 0, wait until only the `jumboChunks` remain on the shard. Once only the `jumbo` chunks remain, you must manually clear the jumbo flag before the draining can complete. See /tutorial/clear-jumbo-flag. After the `jumbo` flag clears, the balancer can migrate these chunks. For details on the migration procedure, see chunk-migration-procedure. |

Continue checking the status of the `removeShard` command until the
number of chunks remaining is `0`. 

```javascript
db.adminCommand( { removeShard: "mongodb0" } )
```

## Move Databases to Another Primary Shard

If the shard is the primary shard for one or more databases in
the cluster, then you must make that database use a different shard
as its primary shard. `removeShard` lists any databases
that you need to move in the `dbsToMove` field in the command output.
If the shard is
not the primary shard for any databases, skip to the next task,
remove-shard-finalize-migration.

To move a database to another shard, use the `movePrimary`
command. 

**Important:**

To ensure a smooth migration, refer to the considerations in the `movePrimary` command
documentation before running `movePrimary`.

To migrate the `fizz` database from
`mongodb0` to `mongodb1`, issue the following command:

```javascript
db.adminCommand( { movePrimary: "fizz", to: "mongodb1" })
```

`mongos` uses `"majority"` write concern for
`movePrimary`.

This command does not return until MongoDB completes moving all data. 
The response from this command will
resemble the following:

```javascript
{
   "ok" : 1,
   "operationTime" : Timestamp(1575400369, 9),
   "$clusterTime" : {
   "clusterTime" : Timestamp(1575400369, 9),
   "signature" : {
      "hash" : BinData(0,"2Nz8QCcVXB0LJLm1hsXfpTCaM0M="),
      "keyId" : NumberLong("6766255701040824328")
   }
}
}
```

## Finalize the Migration

To clean up all metadata information and finalize the removal, run
`removeShard` again. For example, for a shard named
`mongodb0`, run:

```javascript
db.adminCommand( { removeShard: "mongodb0" } )
```

`mongos` converts the
write concern of the
`removeShard` command to `"majority"`.

A success message appears at completion:

```javascript
{
    "msg" : "removeshard completed successfully",
    "state" : "completed",
    "shard" : "mongodb0",
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

Once the value of the `state` field is "completed", you may safely
stop the instances comprising the `mongodb0` shard.
