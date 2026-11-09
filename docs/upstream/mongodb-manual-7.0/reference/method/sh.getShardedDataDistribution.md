<!-- Converted from reference/method/sh.getShardedDataDistribution.txt (reStructuredText). Includes are inlined. -->

# sh.getShardedDataDistribution() (mongosh method)

## Definition

**`sh.getShardedDataDistribution()`**

**New in version:** 6.0.3

Returns data distribution information for sharded collections.
`sh.getShardedDataDistribution()` is a shell helper method for the
`$shardedDataDistribution` aggregation pipeline stage.

You can only run the method from a `mongosh` session
connected to a `mongos` instance.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The method has the following syntax:

```javascript
sh.getShardedDataDistribution()
```

## Example

The following example runs the method:

```javascript
sh.getShardedDataDistribution()
```

The method returns an array of documents for each sharded collection.
For example:

```javascript
[
   {
      ns: 'config.system.sessions',
      shards: [
         {
            shardName: 'shard1',
            numOrphanedDocs: 0,
            numOwnedDocuments: 18,
            ownedSizeBytes: 1782,
            orphanedSizeBytes: 0
         }
      ]
   },
   {
      ns: 'records.people',
      shards: [
         {
            shardName: 'shard1',
            numOrphanedDocs: 0,
            numOwnedDocuments: 21,
            ownedSizeBytes: 134,
            orphanedSizeBytes: 0
         }
      ]
   }
]
```

The following table describes the output fields:

| Field Name | Data Type | Description |
|---|---|---|
| `ns` | string | Namespace of the sharded collection. |
| `shards` | array | Shards in the collection with the data distribution information for each shard. |
| `shards.numOrphanedDocs` | integer | Number of orphaned documents in the shard. |
| `shards.numOwnedDocuments` | integer | Number of documents owned by the shard. |
| `shards.ownedSizeBytes` | integer | Size in bytes of documents owned by the shard when uncompressed. |
| `shards.orphanedSizeBytes` | integer | Size in bytes of orphaned documents in the shard when uncompressed. |

## Learn More

- `$shardedDataDistribution`
- `sh.enableSharding()`
- `sh.addShard()`
- `sh.shardCollection()`
- `sh.reshardCollection()`
