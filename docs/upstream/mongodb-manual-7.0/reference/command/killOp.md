<!-- Converted from reference/command/killOp.txt (reStructuredText). Includes are inlined. -->

# killOp (database command)

## Definition

**`killOp`**

Terminates an operation as specified by the operation ID.
`mongosh` provides the 
`db.killOp()` helper.
To find operations and their corresponding IDs,
see `$currentOp` or `db.currentOp()`.

The `killOp` command must be run against the `admin` database.

To run killOp, use the `db.runCommand( { <command> } )` method.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command has limited support in all MongoDB Atlas clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following form:

```javascript
db.adminCommand(
   { 
     killOp: 1, 
     op: <opid>, 
     comment: <any> 
   }
)
```

## Command Fields

| Parameter | Type | Description |
|---|---|---|
| `op` | number | An operation ID. |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

**Warning:**

Terminate running operations with extreme caution. Only use
`killOp` to terminate operations initiated by clients
and *do not* terminate internal database operations.

## Behavior

Do *not* use `killOp` to terminate an in-progress index
builds in replica sets or sharded clusters. Use `dropIndexes`
on the primary to drop the index. See 
dropIndexes-cmd-index-builds.

### Access Control

On systems running with `authorization`, to kill
operations not owned by the user, the user must have access that
includes the `killop` privilege action.

On `mongod` instances, users can kill their own operations
even without the `killop` privilege action.

### Sharded Cluster

The `killOp` command can be run on
a `mongos` and can kill queries (i.e. read operations)
that span shards in a cluster. The `killOp` command from the
`mongos` does not propagate to the shards when the
operation to be killed is a write operation.

For information on how to list sharding operations that are active on a
`mongos`, see the `localOps` parameter in
`$currentOp`.

For more information and examples on killing operations on a sharded
cluster, see:

- kill-read-ops-sharded-cluster

- kill-write-ops-sharded-cluster

## Example

The following example uses `killOp` to target
the running operation with opid `3478`.

```javascript
db.adminCommand( { "killOp": 1, "op": 3478 } )
```

The operation returns the following result:

```javascript
{ "info" : "attempting to kill op", "ok" : 1 }
```

`killOp` reports success if it succeeded in marking the
specified operation for termination. Operations may not actually be
terminated until they reach an appropriate interruption point. Use
`$currentOp` or `db.currentOp()` to confirm the
target operation was terminated.
