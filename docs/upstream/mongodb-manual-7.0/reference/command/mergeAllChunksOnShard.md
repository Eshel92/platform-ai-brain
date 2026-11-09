<!-- Converted from reference/command/mergeAllChunksOnShard.txt (reStructuredText). Includes are inlined. -->

# mergeAllChunksOnShard (database command)

## Definition

**`mergeAllChunksOnShard`**

`mergeAllChunksOnShard` finds and merges all mergeable 
chunks that a shard owns for a given collection.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
  { 
    mergeAllChunksOnShard: <name of the collection>,
    shard: <name of the shard>,
    maxNumberOfChunksToMerge: <maximum number of chunks to merge> /* optional */
  } 
)
```

## Command Fields

The command takes the following fields:

| Field | Type | Necessity | Description |
|---|---|---|---|
| `mergeAllChunksOnShard` | string | Required | Name of the collection. |
| `shard` | string | Required | Name of the shard. |
| `maxNumberOfChunksToMerge` | integer | Optional | Maximum number of chunks to merge. |

## Behavior

`mergeAllChunksOnShard` finds and merges all mergeable chunks for a 
collection on the same shard. Two or more contiguous chunks in the same 
collection are **mergeable** when they meet all of these conditions: 

- They are owned by the same shard.
- They are not jumbo chunks. `jumbo` chunks are 
  not mergeable because they cannot participate in migrations.
- Their history can be purged safely, without breaking transactions and 
  snapshot reads:

  - The last migration involving the chunk happened at least as many
    seconds ago as the value of 
    `minSnapshotHistoryWindowInSeconds`.
  - The last migration involving the chunk happened at least as many 
    seconds ago as the value of 
    `transactionLifetimeLimitSeconds`.

## Example

This example assumes that history is empty for all chunks and all chunks 
are non-jumbo. Since both conditions are true, all contiguous intervals 
on the same shard are mergeable.

## Setup

These chunks belong to a collection named `coll` with shard key `x`.
There are nine chunks in total.

| Chunk ID | Min | Max | Shard |
|---|---|---|---|
| A | `x: 0` | `x: 10` | Shard0 |
| B | `x: 10` | `x: 20` | Shard0 |
| C | `x: 20` | `x: 30` | Shard0 |
| D | `x: 30` | `x: 40` | Shard0 |
| E | `x: 40` | `x: 50` | Shard1 |
| F | `x: 50` | `x: 60` | Shard1 |
| G | `x: 60` | `x: 70` | Shard0 |
| H | `x: 70` | `x: 80` | Shard0 |
| I | `x: 80` | `x: 90` | Shard1 |

## Steps

**Step 1: Merge All Mergeable Chunks on Shard0**

```javascript
db.adminCommand( { mergeAllChunksOnShard: "db.coll", shard: "Shard0" } )
```

This command merges the contiguous sequences of chunks:

- A-B-C-D
- G-H

**Step 2: Merge All Mergeable Chunks on Shard1**

```javascript
db.adminCommand( { mergeAllChunksOnShard: "db.coll", shard: "Shard1" } )
```

This command merges the contiguous sequences of chunks E-F.

## Result

After these commands have completed, the contiguous chunks have been 
merged. There are four total chunks instead of the original nine.

| Chunk ID | Min | Max | Shard |
|---|---|---|---|
| A-B-C-D | `x: 0` | `x: 40` | Shard0 |
| E-F | `x: 40` | `x: 60` | Shard1 |
| G-H | `x: 60` | `x: 80` | Shard0 |
| I | `x: 80` | `x: 90` | Shard1 |
