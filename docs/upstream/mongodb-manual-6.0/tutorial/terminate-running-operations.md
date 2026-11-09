<!-- Converted from tutorial/terminate-running-operations.txt (reStructuredText). Includes are inlined. -->

# Terminate Running Operations

## Overview

MongoDB provides two facilitates to terminate running operations:
`maxTimeMS()` and `db.killOp()`. Use these
operations as needed to control the behavior of operations in a
MongoDB deployment.

## Available Procedures

### `maxTimeMS`

The `maxTimeMS()` method sets a time limit for an
operation. When the operation reaches the specified time limit,
MongoDB interrupts the operation at the next interrupt point.

#### Terminate a Query

From `mongosh`, use the following method to set a
time limit of 30 milliseconds for this query:

```javascript
db.location.find( { "town": { "$regex": "(Pine Lumber)",
                              "$options": 'i' } } ).maxTimeMS(30)
```

#### Terminate a Command

Consider a potentially long running operation using
`distinct` to return each distinct `collection` field that
has a `city` key:

```javascript
db.runCommand( { distinct: "collection",
                 key: "city" } )
```

You can add the `maxTimeMS`  field to the command document to set a
time limit of 45 milliseconds for the operation:

```javascript
db.runCommand( { distinct: "collection",
                 key: "city",
                 maxTimeMS: 45 } )
```

Operations that reach `maxTimeMS` will return a `MaxTimeMSExpired`
error.

### `killOp`

The `db.killOp()` method interrupts a running operation at
the next interrupt point. `db.killOp()` identifies
the target operation by operation ID.

```javascript
db.killOp(<opId>)
```

**Warning:**

Terminate running operations with extreme caution. Only use
`db.killOp()` to terminate operations initiated by clients
and *do not* terminate internal database operations.

#### Sharded Cluster

The `killOp` command can be run on a `mongos` and can 
kill queries (i.e. read operations) that span shards in a cluster. The 
`killOp` command from the `mongos` does not propagate to 
the shards when the operation to be killed is a write operation.

For more information on killing operations on a sharded cluster, see:

- kill-read-ops-sharded-cluster

- kill-write-ops-sharded-cluster

For information on how to list sharding operations that are active on a
`mongos`, see the `localOps` parameter in
`$currentOp`.
