<!-- Converted from reference/sharding.txt (reStructuredText). Includes are inlined. -->

# Sharding Reference

## Sharding Methods in `mongosh`

* - Name

  - Description

* - `sh.abortReshardCollection()`

  - Aborts a resharding operation.

    **New in version:** 5.0

* - `sh.addShard()`

  - Adds a shard to a sharded cluster.

* - `sh.addShardTag()`

  - In MongoDB 3.4, this method aliases to `sh.addShardToZone()`.

* - `sh.addShardToZone()`

  - Associates a shard to a zone. Supports configuring zones in sharded clusters.

* - `sh.addTagRange()`

  - In MongoDB 3.4, this method aliases to `sh.updateZoneKeyRange()`.

* - `sh.balancerCollectionStatus()`

  - Returns information on whether the chunks of a sharded
    collection are balanced.

* - `sh.commitReshardCollection()`

  - Forces a resharding operation to
    block writes and complete.

    **New in version:** 5.0

* - `sh.disableBalancing()`

  - Disable balancing on a single collection in a sharded database. Does not affect balancing of other collections in a sharded cluster.

* - `sh.enableBalancing()`

  - Activates the sharded collection balancer process if previously disabled using `sh.disableBalancing()`.

* - `sh.disableAutoSplit()`

  - Disables auto-splitting for the sharded cluster.

    Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
    This is because of balancing policy improvements. Auto-splitting commands 
    still exist, but do not perform an operation. For details, see
    release-notes-6.0-balancing-policy-changes.

* - `sh.enableAutoSplit()`

  - Enables auto-splitting for the sharded cluster.

    Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
    This is because of balancing policy improvements. Auto-splitting commands 
    still exist, but do not perform an operation. For details, see
    release-notes-6.0-balancing-policy-changes.

* - `sh.enableSharding()`

  - Creates a database.

* - `sh.getBalancerState()`

  - Returns a boolean to report if the balancer is currently enabled.

* - `sh.getShardedDataDistribution()`

  - .. include:: /includes/sharding/getShardedDataDistribution-shell-helper-method-summary.rst

* - `sh.removeTagRange()`

  - In MongoDB 3.4, this method aliases to `sh.removeRangeFromZone()`.

* - `sh.removeRangeFromZone()`

  - Removes an association between a range of shard keys and a zone. Supports configuring zones in sharded clusters.

* - `sh.help()`

  - Returns help text for the `sh` methods.

* - `sh.isBalancerRunning()`

  - Returns a document describing the status of the balancer.

* - `sh.moveChunk()`

  - Migrates a chunk in a sharded cluster.

* - `sh.removeShardTag()`

  - In MongoDB 3.4, this method aliases to `sh.removeShardFromZone()`.

* - `sh.removeShardFromZone()`

  - Removes the association between a shard and a zone. Use to manage zone sharding.

* - `sh.reshardCollection()`

  - Initiates a resharding operation to change the
    shard key for a collection, changing the distribution of your data.

    **New in version:** 5.0

* - `sh.setBalancerState()`

  - Enables or disables the balancer which migrates chunks between shards.

* - `sh.shardCollection()`

  - Enables sharding for a collection.

* - `sh.splitAt()`

  - Divides an existing chunk into two chunks using a specific value of the shard key as the dividing point.

* - `sh.splitFind()`

  - Divides an existing chunk that contains a document matching a query into two approximately equal chunks.

* - `sh.startBalancer()`

  - Enables the balancer and waits for balancing to start.

* - `sh.status()`

  - Reports on the status of a sharded cluster, as `db.printShardingStatus()`.

* - `sh.stopBalancer()`

  - Disables the balancer and waits for any in progress balancing rounds to complete.

* - `sh.waitForBalancer()`

  - Internal. Waits for the balancer state to change.

* - `sh.waitForBalancerOff()`

  - Internal. Waits until the balancer stops running.

* - `sh.waitForPingChange()`

  - Internal. Waits for a change in ping state from one of the `mongos` in the sharded cluster.

* - `sh.updateZoneKeyRange()`

  - Associates a range of shard keys to a zone. Supports configuring zones in sharded clusters.

* - `convertShardKeyToHashed()`

  - Returns the hashed value for the input.

## Sharding Database Commands

The following database commands support sharded clusters.

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

* - `enableSharding`

  - Enables sharding on a specific database.

* - `flushRouterConfig`

  - Forces a `mongod` / `mongos` instance to update its cached routing metadata.

* - `getShardMap`

  - Internal command that reports on the state of a sharded cluster.

* - `isdbgrid`

  - Verifies that a process is a `mongos`.

* - `listShards`

  - Returns a list of configured shards.

* - `moveChunk`

  - Internal command that migrates chunks between shards.

* - `movePrimary`

  - Reassigns the primary shard when removing a shard from a sharded cluster.

* - `moveRange`

  - Command that migrates ranges between shards.

* - `mergeChunks`

  - Provides the ability to combine chunks on a single shard.

* - `removeShard`

  - Starts the process of removing a shard from a sharded cluster.

* - `removeShardFromZone`

  - Removes the association between a shard and a zone. Supports configuring zones in sharded clusters.

* - `reshardCollection`

  - Initiates a resharding operation to change the
    shard key for a collection, changing the distribution of your data.

    **New in version:** 5.0

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

## Reference Documentation

Operational Restrictions
   Requirement for deploying a sharded cluster

/tutorial/troubleshoot-sharded-clusters
   Common strategies for troubleshooting sharded cluster deployments.

/reference/config-database
   Complete documentation of the content of the `local` database
   that MongoDB uses to store sharded cluster metadata.
