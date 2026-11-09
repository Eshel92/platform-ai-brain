<!-- Converted from tutorial/analyze-sharded-data-distribution.txt (reStructuredText). Includes are inlined. -->

# Analyze Sharded Data Distribution

Use this procedure to analyze sharded data distribution. You can use this information to determine
if there is going to be a large amount of balancing on your cluster. 

## About This Task

This procedure shows how you can:

- Upgrade your cluster from 5.0 to 6.0.
- Determine your sharded data's distribution across the cluster using 
  the `$shardedDataDistribution` stage.
- Update your balancer settings, if needed.

## Before You Begin

Keep the balancer off through the upgrade process and throughout 
this procedure. Once you have an understanding of the evenness of 
your collections under the new balancing policy, you can turn the
balancer back on.

## Steps

**Step 1: Upgrade your cluster from 5.0 to 6.0.**

To upgrade your cluster from 5.0 to 6.0, see 
6.0-upgrade-sharded-cluster.

**Step 2: Connect to mongos using mongosh.**

You can connect to any `mongos` in the cluster.

**Step 3: Analyze the data distribution on your cluster.**

To understand how the data distribution of your collections will 
impact balancing, use the 
`$shardedDataDistribution` aggregation stage.

To return all sharded data distribution metrics, run the following:

```javascript
db.aggregate([
   { $shardedDataDistribution: { } }
])
```

Example output:

```json
[
  {
    "ns": "test.names",
    "shards": [
      {
        "shardName": "shard-1",
        "numOrphanedDocs": 0,
        "numOwnedDocuments": 6,
        "ownedSizeBytes": 366,
        "orphanedSizeBytes": 0
      },
      {
        "shardName": "shard-2",
        "numOrphanedDocs": 0,
        "numOwnedDocuments": 6,
        "ownedSizeBytes": 366,
        "orphanedSizeBytes": 0
      }
    ]
  }
]
```

If the difference between the shard with the greatest 
`ownedSizeBytes` and the shard with the fewest 
`ownedSizeBytes` is within the migration threshold, the collection is considered 
balanced. When the balancer is enabled for these collections, it 
does not issue migrations.

**Step 4: (*Optional*) Configure the balancer on 6.0.**

If your collection is unbalanced and you wish to control the 
balancer behavior, you can use one or both of the following
methods:

- Configure the balancer to be only be active at certain times by 
  modifying the balancing window.
- Restrict balancing operations to specific collections by 
  disabling the balancer on collections.

**Modify the Balancing Window**

1. Switch to the config database.

   Issue the following command to switch to the `config` 
   database.

   ```javascript
   use config 
   ```

#. Set the balancing window start and end times.

   To set the active window, use the `updateOne()`
   method:

   ```javascript
   db.settings.updateOne(
      { _id: "balancer" },
      { $set: { activeWindow : { start : "<start-time>", stop : "<stop-time>" } } },
      { upsert: true }
   )
   ```

   Replace `<start-time>` and `<end-time>` with time values using
   two-digit hour and minute values (that is, `HH:MM`) that specify the
   beginning and end boundaries of the balancing window.

   - For `HH` values, use hour values ranging from `00` - `23`.
   - For `MM` value, use minute values ranging from `00` - `59`.

   For self-managed sharded clusters, MongoDB evaluates the start 
   and stop times relative to the time zone of the primary member 
   in the config server replica set.

   For Atlas clusters, MongoDB evaluates the start and stop times 
   relative to the UTC timezone. 

   **Note:**

   The balancer window must be sufficient to *complete* the
   migration of all data inserted during the day.

   As data insert rates can change based on activity and usage
   patterns, ensure that the balancing window you select will 
   be sufficient to support the needs of your deployment.

#. (*Optional*) Ensure range deletion is synchronous.

   Only use this step if you want to constrain range deletion to 
   the balancing window. 

   By default, the balancer does not wait for the in-progress 
   migration's delete phase to complete before starting the 
   next chunk migration. To have the delete phase **block** the 
   start of the next chunk migration, you can set
   `_waitForDelete` to true.

   Update the `_waitForDelete` value in the `settings` 
   collection of the `config` database. For example:

   ```javascript
   use config

   db.settings.updateOne(
      { "_id" : "balancer" },
      { $set : { "_waitForDelete" : true } },
      { upsert : true }
   )
   ```

**Disable Balancing for Specific Collections**

By default, every collection has balancing enabled.

To disable balancing for a specific collection, connect to a 
`mongos` with the `mongosh` shell and call the
`sh.disableBalancing()` method.

This example disables balancing on the `students.grades`
collection:

```javascript
sh.disableBalancing("students.grades")
```

The `sh.disableBalancing()` method accepts the full namespace
of the collection as its parameter.

**Step 5: Re-enable the balancer on your cluster.**

Use this procedure if you have disabled the balancer and are ready to
re-enable it:

#. Connect to any `mongos` in the cluster using the
   `mongosh` shell.

#. Issue one of the following operations to enable the balancer:

   From the `mongosh` shell, run:

   ```javascript
   sh.startBalancer()
   ```

   **Note:**

   To enable the balancer from a driver, use the `balancerStart`
   command against the `admin` database, as in the following:

   ```javascript
   db.adminCommand( { balancerStart: 1 } )
   ```

   Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
   This is because of balancing policy improvements. Auto-splitting commands 
   still exist, but do not perform an operation. For details, see
   release-notes-6.0-balancing-policy-changes.

   In MongoDB versions earlier than 6.0.3, `sh.startBalancer()`
   also enables auto-splitting for the sharded cluster.

## Learn More

- sharded-cluster-balancer
- sharding-balancing-enable
- sharding-balancing-disable-temporarily
- sharding-schedule-balancing-window
- `$shardedDataDistribution`
