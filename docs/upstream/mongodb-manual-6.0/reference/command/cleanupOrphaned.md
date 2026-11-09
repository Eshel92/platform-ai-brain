<!-- Converted from reference/command/cleanupOrphaned.txt (reStructuredText). Includes are inlined. -->

# cleanupOrphaned

**Important:**

Starting in MongoDB 6.0.3, you should run an aggregation using the 
`$shardedDataDistribution` stage to confirm no orphaned 
documents remain. For details, 
see shardedDataDistribution-no-orphaned-docs.

## Definition

**`cleanupOrphaned`**

Use this command to wait for orphaned documents in a chunk
range from a shard key's `MinKey` to its
`MaxKey` for a specified namespace to be
cleaned up from a majority of a shard's members.

To run, issue `cleanupOrphaned` in the `admin` database
directly on the `mongod` instance that is the primary
replica set member of the shard. You do not need to disable the
balancer before running `cleanupOrphaned`.

**Note:**

Do not run `cleanupOrphaned` on a
`mongos` instance.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

              

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   {
     cleanupOrphaned: "<database>.<collection>",
     startingFromKey: <minimumShardKeyValue>, // deprecated
     secondaryThrottle: <boolean>, // deprecated
     writeConcern: <document> // deprecated
   } 
)
```

### Command Fields

`cleanupOrphaned` has the following fields:

| Field | Type | Description |
|---|---|---|
| `cleanupOrphaned` | string | The namespace, i.e. both the database and the collection name, of the sharded collection for which to wait for cleanup of the orphaned data. |

 

## Behavior

### Determine Range

The value of this field is not used to determine the bounds of the cleanup 
range. The `cleanupOrphaned` command waits until all orphaned 
documents in all ranges in the namespace are cleaned up from the shard before
completing, regardless of the presence of or value of
`startingFromKey`. 

## Required Access

On systems running with `authorization`, you must have
`clusterAdmin` privileges to run `cleanupOrphaned`.

## Output

### Return Document

Each `cleanupOrphaned` command returns a document containing
a subset of the following fields:

**`cleanupOrphaned.ok`**

Equal to `1` on success.

A value of `1` indicates that either:

- No orphaned documents remain in the `cleanupOrphaned` namespace
  on the shard, or
- The collection referenced in the `cleanupOrphaned` namespace is
  not sharded.

A value of `0` indicates that an error has occurred.
