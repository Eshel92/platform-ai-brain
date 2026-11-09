<!-- Converted from tutorial/add-shards-to-shard-cluster.txt (reStructuredText). Includes are inlined. -->

# Add Shards to a Cluster

You add shards to a sharded cluster after you create the cluster
or any time that you need to add capacity to the cluster. If you have not
created a sharded cluster, see sharding-procedure-setup.

All shards must be replica sets.

## Considerations

### Balancing

When you add a shard to a sharded cluster, you affect the balance of
chunks among the shards of a cluster for all existing sharded
collections. The balancer will begin migrating chunks so that the
cluster will achieve balance. See sharding-internals-balancing for
more information.

### Capacity Planning

When adding a shard to a cluster, always ensure that the cluster has
enough capacity to support the migration required for balancing the
cluster without affecting legitimate production traffic.

## Add a Shard to a Cluster

You interact with a sharded cluster by connecting to a `mongos`
instance.

1. In `mongosh`, connect to the `mongos`
   instance. For example, if a `mongos` is accessible at
   `mongos0.example.net` on port `27017`, issue the following
   command:

   ```bash
   mongosh --host mongos0.example.net --port 27017
   ```

#. Add a shard replica set to the cluster using the `sh.addShard()`
   method, as shown in the example below. Issue `sh.addShard()`
   separately for each shard. Specify the name of the replica set and a 
   member of the set.

   **Note:** Optional

   You can instead use the `addShard` database
   command, which lets you specify a name and maximum size for the
   shard. If you do not specify these, MongoDB automatically assigns
   a name and maximum size. To use the database command, see
   `addShard`.

   The following example illustrates adding a shard with
   `sh.addShard()`:

   To add a shard replica set named `rs1` with a member
   running on port `27018` on `mongodb0.example.net`, issue the
   following command:

   ```javascript
   sh.addShard( "rs1/mongodb0.example.net:27018" )
   ```

   **Note:** It might take some time for chunks to

   migrate to the new shard.
