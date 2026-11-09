<!-- Converted from reference/command/nav-sharding.txt (reStructuredText). Includes are inlined. -->

# Sharding Commands

**Note:**

For details on a specific command, including syntax and examples,
click on the link to the command's reference page.

* - Name

  - Description

* - `abortReshardCollection`

  - Aborts a resharding operation.

    **New in version:** 5.0

* - `addShard`

  - Adds a shard to a sharded cluster.

* - `addShardToZone`

  - Associates a shard with a zone. Supports configuring zones in sharded clusters.

* - `balancerCollectionStatus`

  - Returns information on whether the chunks of a sharded
    collection are balanced.

* - `balancerStart`

  - Starts a balancer thread.

* - `balancerStatus`

  - Returns information on the balancer status.

* - `balancerStop`

  - Stops the balancer thread.

* - `clearJumboFlag`

  - Clears the `jumbo` flag for a chunk.

* - `cleanupOrphaned`

  - Removes orphaned data with shard key values outside of the ranges of the chunks owned by a shard.

* - `cleanupReshardCollection`

  - Cleans up a failed resharding operation.

    **New in version:** 5.0

* - `commitReshardCollection`

  - Forces a resharding operation to
    block writes and complete.

    **New in version:** 5.0

* - `configureCollectionBalancing`

  - Configures balancer settings on a sharded collection.

    **New in version:** 5.3

* - `enableSharding`

  - Creates a database.

* - `flushRouterConfig`

  - Forces a `mongod` / `mongos` instance to update its cached routing metadata.

* - `getShardMap`

  - Returns the hostnames and connection strings for shards in the
    cluster and the config servers for your cluster.

* - `isdbgrid`

  - Verifies that a process is a `mongos`.

* - `listShards`

  - Returns a list of configured shards.

* - `moveChunk`

  - Internal command that migrates chunks between shards.

* - `movePrimary`

  - Reassigns the primary shard when removing a shard from a sharded cluster.

* - `moveRange`

  - Migrates ranges between shards.

* - `mergeChunks`

  - Provides the ability to combine chunks on a single shard.

* - `refineCollectionShardKey`

  - Refines a collection's shard key by adding a suffix to the
    existing key.

* - `removeShard`

  - Starts the process of removing a shard from a sharded cluster.

* - `removeShardFromZone`

  - Removes the association between a shard and a zone. Supports configuring zones in sharded clusters.

* - `reshardCollection`

  - Initiates a resharding operation to change the
    shard key for a collection, changing the distribution of your data.

    **New in version:** 5.0

* - `setAllowMigrations`

  - Prevents the start of new automatic migrations on a 
    collection, prevents in-flight manual migrations from 
    committing, and excludes the collection from new balancer rounds.

* - `shardCollection`

  - Enables the sharding functionality for a collection, allowing the collection to be sharded.

* - `shardingState`

  - Reports whether the `mongod` is a member of a sharded cluster.

* - `split`

  - Creates a new chunk.

* - `unsetSharding`

  - *Removed in MongoDB 5.0.* Internal command that affects
    connections between instances in a MongoDB deployment.

* - `updateZoneKeyRange`

  - Adds or removes the association between a range of sharded data and a zone. Supports configuring zones in sharded clusters.
