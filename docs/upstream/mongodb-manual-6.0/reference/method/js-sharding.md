<!-- Converted from reference/method/js-sharding.txt (reStructuredText). Includes are inlined. -->

# Sharding Methods

**Note:**

For details on a specific method, including syntax and examples,
click on the link to the method's reference page.

* - Name

  - Description

* - `sh.abortReshardCollection()`

  - Aborts a resharding operation.

    **New in version:** 5.0

* - `sh.addShard()`

  - Adds a shard to a sharded cluster.

* - `sh.addShardTag()`

  - This method aliases to `sh.addShardToZone()`.

* - `sh.addShardToZone()`

  - Associates a shard to a zone. Supports configuring zones in sharded clusters.

* - `sh.addTagRange()`

  - This method aliases to `sh.updateZoneKeyRange()`.

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

  - This method aliases to `sh.removeRangeFromZone()`.

* - `sh.removeRangeFromZone()`

  - Removes an association between a range of shard keys and a zone. Supports configuring zones in sharded clusters.

* - `sh.help()`

  - Returns help text for the `sh` methods.

* - `sh.isBalancerRunning()`

  - Returns a document describing the status of the balancer.

* - `sh.moveChunk()`

  - Migrates a chunk in a sharded cluster.

* - `sh.moveRange()`

  - Move ranges between shards.

* - `sh.removeShardTag()`

  - This method aliases to `sh.removeShardFromZone()`.

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
