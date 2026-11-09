<!-- Converted from reference/method/db.killOp.txt (reStructuredText). Includes are inlined. -->

# db.killOp()

## Description

**`db.killOp(opid)`**

Terminates an operation as specified by the operation ID. To find
operations and their corresponding IDs, see `$currentOp`
or `db.currentOp()`.

The `db.killOp()` method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `op` | number | An operation ID. |

**Warning:**

Terminate running operations with extreme caution. Only use
`db.killOp()` to terminate operations initiated by clients
and *do not* terminate internal database operations.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

MongoDB Atlas limits the use of this method to the MongoDB user who ran the 
operation. For information on Atlas support for all commands,
see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Sharded Cluster

### Kill Read Operations

The `db.killOp()` method can be run on a
`mongos` and can kill queries (read operations) that are running 
on more than one shard in a cluster.

For example, to kill a query operation on a sharded cluster:

tabs:

   - id: mongos
     name: From the mongos Instance
     content: |

         #. On the **same** `mongos` where the client issued the
            query, find the opid of the query operation to kill by running the
            aggregation pipeline `$currentOp` with the ``localOps:
            true``:

            ```javascript
            use admin
            db.aggregate( [
               { $currentOp : { allUsers: true, localOps: true } },
               { $match : <filter condition> } // Optional.  Specify the condition to find the op.
                                               // e.g. { op: "getmore", "command.collection": "someCollection" }
            ] )
            ```

            **Important:**

            You must issue this aggregation operation on the **same**
            `mongos` where the client issued the query.

         #. Once you find the query operation to kill, issue
            `db.killOp()` with the opid on the `mongos`:

            ```javascript
            db.killOp(<opid of the query to kill>)
            ```

         **See also:**

         The `localOps` parameter in `$currentOp`.

   - id: mongod
     name: From a shard member
     content: |

         Alternatively, you can find and kill the read operation from a
         shard member where the operation is running. MongoDB
         propagates the kill operation to the other shards and
         `mongos` instances:

         #. On one of the shards where the operation is running, find the opid
            of the query operation to kill:

            ```javascript
            use admin
            db.aggregate( [
               { $currentOp : { allUsers: true } },
               { $match : <filter condition> } // Optional.  Specify the condition to find the op.
                                                // e.g. { op: "getmore", "command.collection": "someCollection" }
            ] )
            ```

         #. Once you find the query operation to kill, issue
            `db.killOp()` with the opid on the shard member:

            ```javascript
            db.killOp(<opid of the query to kill>)
            ```

            MongoDB propagates the kill operation to the
            other shards and `mongos` instances.

### Kill Write Operations

Within a Session
   MongoDB drivers associate all operations with a 
   server session, with the
   exception of unacknowledged writes.

   If the write operation is associated with a session, you can use the
   `killSessions` command on the `mongos` to
   kill the write operation across shards.

   #. Run the aggregation pipeline `$currentOp` on
      the `mongos` to find the
      `lsid` (logical session id).

      ```javascript
      use admin
      db.aggregate( [
         { $currentOp : { allUsers: true, localOps: true } },
         { $match : <filter condition> } // Optional.  Specify the condition to find the op.
                                         // e.g. { "op" : "update", "ns": "mydb.someCollection" }
      ] )
      ```

      #. Using the returned `lsid` information, issue the
         `killSessions` command on the
         `mongos` to kill the operation on the shards.
              

         ```javascript
         db.adminCommand( { killSessions: [
            { "id" : UUID("80e48c5a-f7fb-4541-8ac0-9e3a1ed224a4"), "uid" : BinData(0,"47DEQpj8HBSa+/TImW+5JCeuQeRkm5NMpJWZG3hSuFU=") }
         ] } )
         ```

Without a Session
   If the write operation is **not** associated with a session, you must find and kill the
   operation on all the shards associated with the write.

   #. From a `mongos`, run the aggregation pipeline
      `$currentOp` to find the opid(s) of the query operation on
      the shards:

      ```javascript
      use admin
      db.aggregate( [
         { $currentOp : { allUsers: true } },
         { $match : <filter condition> } // Optional.  Specify the condition to find the op.
      ] )
      ```

      When run on a `mongos`, `$currentOp`
      returns the opids in the format of ``"<shardName>:<opid on that
      shard>"``; e.g.

      ```javascript
      {
         "shard" : "shardB",
         ..
         "opid" : "shardB:79214",
         ...
      },
      {
         "shard" : "shardA",
         ..
         "opid" : "shardA:100913",
         ...
      },
      ```

   #. Using the opid information, issue `db.killOp()` on the
      `mongos` to kill the operation on the shards.

      ```javascript
      db.killOp("shardB:79014");
      db.killOp("shardA:100813");
      ```

## Access Control

On systems running with `authorization`, to kill
operations not owned by the user, the user must have access that
includes the `killop` privilege action.

On `mongod` instances, users can kill their own operations
even without the `killop` privilege action.

**See also:**

`$currentOp`
