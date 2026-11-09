<!-- Converted from reference/command/shardingState.txt (reStructuredText). Includes are inlined. -->

# shardingState

**`shardingState`**

`shardingState` is an admin command that reports if
`mongod` is a member of a sharded cluster. To
run the command, you must run against the `admin` database. See
`db.adminCommand()`.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

           

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
  { 
    shardingState: 1   
  }
)
```

## Behavior

For `shardingState` to detect that a `mongod` is a
member of a sharded cluster, the `mongod` must satisfy the
following conditions:

#. the `mongod` is a primary member of a replica set, and

#. the `mongod` instance is a member of a sharded
   cluster.

If `shardingState` detects that a `mongod` is a
member of a sharded cluster, `shardingState` returns a
document that resembles the following prototype:

```javascript
{
  "enabled" : true,
  "configServer" : "<configdb-string>",
  "shardName" : "<string>",
  "shardHost" : "string:",
  "versions" : {
       "<database>.<collection>" : Timestamp(<...>),
       "<database>.<collection>" : Timestamp(<...>)
  },
  "ok" : 1,
  "$clusterTime" : {
     "clusterTime" : Timestamp(1510716515, 1),
     "signature" : {
        "hash" : BinData(0,"B2ViX7XLzFLS5Fl9XEuFXbwKIM4="),
        "keyId" : NumberLong("6488045157173166092")
     }
  },
  "operationTime" : Timestamp(1510716515, 1)
}
```

Otherwise, `shardingState` will return the following document:

```javascript
{
  "enabled" : false,
  "ok" : 1,
  "$clusterTime" : {
     "clusterTime" : Timestamp(1510716515, 1),
     "signature" : {
        "hash" : BinData(0,"B2ViX7XLzFLS5Fl9XEuFXbwKIM4="),
        "keyId" : NumberLong("6488045157173166092")
     }
  },
  "operationTime" : Timestamp(1510716515, 1)
}
```

The response from `shardingState` when used with a
config server is:

```javascript
{
   "enabled" : false,
   "ok" : 1,
   "operationTime" : Timestamp(1510767613, 1),
   "$gleStats" : {
      "lastOpTime" : Timestamp(0, 0),
      "electionId" : ObjectId("7fffffff0000000000000001")
   },
   "$clusterTime" : {
      "clusterTime" : Timestamp(1510767613, 1),
      "signature" : {
         "hash" : BinData(0,"IwBZ4SZjIMI5NdM62NObV/R31GM="),
         "keyId" : NumberLong("6488693018630029321")
      }
   }
}
```

**Note:**

`mongos` instances do not provide the
`shardingState`.

**Warning:**

This command obtains a write lock on the affected database and
will block other operations until it has completed; however, the
operation is typically short lived.
