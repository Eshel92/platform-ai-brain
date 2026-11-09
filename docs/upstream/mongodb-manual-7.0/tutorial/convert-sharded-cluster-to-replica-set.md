<!-- Converted from tutorial/convert-sharded-cluster-to-replica-set.txt (reStructuredText). Includes are inlined. -->

# Convert Self-Managed Sharded Cluster to Replica Set

This tutorial describes how to convert a sharded
cluster to a non-sharded replica set. To convert a replica
set into a sharded cluster, see
/tutorial/convert-replica-set-to-replicated-shard-cluster. See the
/sharding documentation for more information on sharded
clusters.

This tutorial guides you through the following tasks:

1. Disable the balancer.

#. Convert the cluster to a replica set.

#. Unlock the cluster (multi-shard clusters only).

## Before You Begin

### Version Compatibility

The steps in this tutorial require MongoDB 6.0 or later.

### Authorization

The `fsync` and `fsyncUnlock` commands require the
`fsync` authorization action, which can be assigned through
the `hostManager` role or a custom role.

### Users and Roles

In a sharded cluster, MongoDB stores user and role definitions in
the `admin` database of the config servers. These definitions don't transfer to the replica set when
you convert the cluster.

Before your applications connect to the replica set, create the
users and roles that your deployment requires on the replica set.
To learn more, see create-users and
manage-users-and-roles.

### Schedule the Cluster Conversion

Convert the cluster when chunk migrations, resharding, and schema
transformations aren't typically performed.

## Steps

**singleshardcluster:**

In the case of a sharded cluster with only one shard,
that shard contains the full data set. To convert that cluster
into a non-sharded replica set:

**Step 1: Disable the Balancer**

To disable the balancer:

a. Connect `mongosh` to a
   `mongos` instance in the sharded cluster.

#. To stop the balancer, run:

   ```javascript
   sh.stopBalancer()
   ```

#. To verify the balancer is disabled, run the following
   command and ensure the output is `false`:

   ```javascript
   sh.getBalancerState()
   ```

**Step 2: Convert the Cluster to a Replica Set**

a. Stop all `mongos` instances.

#. Reconfigure the application to connect directly to
   the replica set members of the shard that will
   become the new replica set.

#. Perform a rolling restart of the replica set
   members to remove the
   `--shardsvr` option
   from `mongod`.

   **Tip:** Changing the

   changes the port that `mongod`
   listens for incoming connections on.

The single-shard cluster is now a non-sharded
replica set that accepts read and write
operations on the data set. You can decommission
the config servers as needed.

**multishardcluster:**

Use the following procedure to transition from a
sharded cluster with more than one shard to an
entirely new replica set.

**Step 1: Disable the Balancer and Lock the Cluster**

To disable the balancer and lock the cluster:

a. Connect `mongosh` to a
   `mongos` instance in the sharded cluster.

#. To stop the balancer, run:

   ```javascript
   sh.stopBalancer()
   ```

#. To verify the balancer is disabled, run the following
   command and ensure the output is `false`:

   ```javascript
   sh.getBalancerState()
   ```

#. To lock the sharded cluster, which prevents database
   writes, run:

   ```javascript
   db.getSiblingDB( "admin" ).fsyncLock()
   ```

#. To confirm the lock, run:

   ```javascript
   db.getSiblingDB( "admin" ).aggregate( [
      { $currentOp: { } },
      { $facet: {
         "locked": [
            { $match: { $and: [
               { fsyncLock: { $exists: true } }
            ] } }
         ],
         "unlocked": [
            { $match: { fsyncLock: { $exists: false } } }
         ]
      } },
      { $project: {
         "fsyncLocked": { $gt: [ { $size: "$locked" }, 0 ] },
         "fsyncUnlocked": { $gt: [ { $size: "$unlocked" }, 0 ] }
      } }
   ] )
   ```

#. Ensure the output shows `fsyncLocked` is `true`,
   which means the cluster is locked:

   ```javascript
   [ { fsyncLocked: true }, { fsyncUnlocked: false } ]
   ```

**Step 2: Convert the Cluster to a Replica Set**

a. With the sharded cluster locked and the balancer
   disabled, deploy a new replica set in addition to your
   sharded cluster. The replica set must have sufficient
   capacity to hold all of the data files from all of
   the current shards combined. Do not configure the
   application to connect to the new replica set until
   the data transfer is complete.

#. Reconfigure your application or stop all
   `mongos` instances. If you stop all
   `mongos` instances, the applications
   cannot read from the database. If you stop all
   `mongos` instances, start a temporary
   `mongos` instance that applications
   cannot access for the data migration procedure.

#. Use mongodump and mongorestore to migrate
   the data from the `mongos` instance to
   the new replica set.

   Exclude the `config` database when you run
   `mongorestore`. Use the
   `--nsExclude`
   option as shown in this example:

   ```sh
   mongorestore --nsExclude="config.*" <connection-string> /data/backup
   ```

   **Note:** Not all collections on all databases are

   necessarily sharded. Do not solely migrate the
   sharded collections. Ensure that all databases
   and all collections migrate correctly.

#. Reconfigure the application to use the non-sharded
   replica set instead of the
   `mongos` instance.

   After you convert the sharded cluster to a replica
   set, update the
   connection string used by your
   applications to the connection string for your
   replica set. Then, restart your applications.

The application now uses the non-sharded replica
set for reads and writes. You may now decommission
the remaining unused sharded cluster infrastructure.

**Step 3: Unlock the Cluster**

After you convert the sharded cluster to a replica set,
unlock the cluster:

a. To unlock the cluster and allow database writes to
   resume, run:

   ```javascript
   db.getSiblingDB( "admin" ).fsyncUnlock()
   ```

#. To confirm the unlock, run:

   ```javascript
   db.getSiblingDB( "admin" ).aggregate( [
      { $currentOp: { } },
      { $facet: {
         "locked": [
            { $match: { $and: [
               { fsyncLock: { $exists: true } }
            ] } } ],
            "unlocked": [
            { $match: { fsyncLock: { $exists: false } } }
         ]
      } },
      { $project: {
         "fsyncLocked": { $gt: [ { $size: "$locked" }, 0 ] },
         "fsyncUnlocked": { $gt: [ { $size: "$unlocked" }, 0 ] }
      } }
   ] )
   ```

#. Ensure the output shows `fsyncLocked` is `false`,
   which means the cluster is unlocked:

   ```javascript
   [ { fsyncLocked: false }, { fsyncUnlocked: true } ]
   ```

## Learn More

sharded-cluster-balancer
