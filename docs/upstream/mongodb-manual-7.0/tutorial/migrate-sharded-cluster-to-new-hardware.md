<!-- Converted from tutorial/migrate-sharded-cluster-to-new-hardware.txt (reStructuredText). Includes are inlined. -->

# Migrate a Self-Managed Sharded Cluster to Different Hardware

The tutorial is specific to MongoDB 7.0. For earlier 
versions of MongoDB, refer to the corresponding version of the MongoDB 
Manual.

Config servers for sharded clusters are 
deployed as a replica set. The
replica set config servers must run the WiredTiger storage engine.

This procedure moves the components of the sharded cluster to a
new hardware system without downtime for reads and writes.

**Important:** While the migration is in progress, do not attempt to change to the

any operation that modifies the cluster metadata *in any way*. For
example, do not create or drop databases, create or drop collections,
or use any sharding commands.

## Disable the Balancer

Disable the balancer to stop chunk migration and do not perform any metadata
write operations until the process finishes. If a migration is in
progress, the balancer will complete the in-progress migration before
stopping.

To disable the balancer, connect to one of the cluster's
`mongos` instances and issue the following method: [#autosplit-stop]_

```javascript
sh.stopBalancer()
```

To check the balancer state, issue the `sh.getBalancerState()`
method.

For more information, see sharding-balancing-disable-temporarily.

## Migrate Each Config Server Separately

Config servers for sharded clusters can be
deployed as a replica set (CSRS). 
Using a replica set for the config
servers improves consistency across the config servers, since MongoDB
can take advantage of the standard replica set read and write protocols
for the config data. In addition, using a replica set for config
servers allows a sharded cluster to have more than 3 config servers
since a replica set can have up to 50 members. To deploy config servers
as a replica set, the config servers must run the storage-wiredtiger. 

The following restrictions apply to a replica set configuration when used
for config servers:

- Must have zero arbiters.

- Must have no delayed members.

- Must build indexes (i.e. no member should have
  `members[n].buildIndexes` setting set to false).

For each member of the config server replica set:

**Important:** Replace the secondary members before replacing the primary.

**Step 1: Start the replacement config server.**

Start a `mongod` instance, specifying the `--configsvr`,
`--replSet`, `--bind_ip` options, and other options as
appropriate to your deployment.

**Warning:**

Before you bind your instance to a publicly-accessible IP address,
you must secure your cluster from unauthorized access. For a complete
list of security recommendations, see
security-checklist. At minimum, consider
enabling authentication and hardening
network infrastructure.

```sh
mongod --configsvr --replSet <replicaSetName> --bind_ip localhost,<hostname(s)|ip address(es)>
```

**Step 2: Add the new config server to the replica set.**

Connect `mongosh` to the primary of the config server
replica set and use `rs.add()` to add the new member.

**Warning:**

Before MongoDB 5.0, a newly added secondary still counts as a voting
member even though it can neither serve reads nor become primary until
its data is consistent. If you are running a MongoDB version earlier
than 5.0 and add a secondary with its `votes`
and `priority` settings greater than zero, this can
lead to a case where a majority of the voting members are
online but no primary can be elected. To avoid such situations,
consider adding the new secondary initially with
`priority :0` and `votes :0`. Then, run `rs.status()` to ensure the
member has transitioned into `SECONDARY` state. Finally, use
`rs.reconfig()` to update its priority and votes.

```javascript
rs.add( { host: "<hostnameNew>:<portNew>", priority: 0, votes: 0 } )
```

The initial sync process copies all the data from one member of the
config server replica set to the new member without restarting.

`mongos` instances automatically recognize the change in the
config server replica set members without restarting.

**Step 3: Update the newly added config server's votes and priority settings.**

a. Ensure that the new member has reached `SECONDARY`
   state. To check the state of the replica set members, run
   `rs.status()`:

   ```javascript
   rs.status()
   ```

#. Reconfigure the replica set to update the votes and priority of
   the new member:

   ```javascript
   var cfg = rs.conf();

   cfg.members[n].priority = 1;  // Substitute the correct array index for the new member
   cfg.members[n].votes = 1;     // Substitute the correct array index for the new member

   rs.reconfig(cfg)
   ```

   where `n` is the array index of the new member in the
   `members` array.

**Warning:**

- The `rs.reconfig()` shell method can force the current
  primary to step down, which causes an election. When the primary steps down, the
  `mongod` closes all client connections. While this
  typically takes 10-20 seconds, try to make these changes during
  scheduled maintenance periods.

- .. include:: /includes/warning-mixed-version-rs-config.rst

**Step 4: Shut down the member to replace.**

If replacing the primary member, step down the primary first before
shutting down.

**Step 5: Remove the member to replace from the config server replica set.**

Upon completion of initial sync of the replacement config server,
from a `mongosh` session that is connected to the
primary, use `rs.remove()` to remove the old member.

```javascript
rs.remove("<hostnameOld>:<portOld>")
```

`mongos` instances automatically recognize the change in the
config server replica set members without restarting.

**Step 6: If necessary, update `mongos` configuration or DNS entry.**

With replica set config servers, the `mongos` instances specify
in the `--configdb` or `sharding.configDB` setting the config
server replica set name and at least one of the replica set members. 

As such, if the `mongos` instance does not specify the
removed replica set member in the `--configdb` or
`sharding.configDB` setting, no further action is necessary.

If, however, a `mongos` instance specified the removed
member in the `--configdb` or `configDB`
setting, either:

- Update the setting for the next time you restart the
  `mongos`, or

- Modify the DNS entry that points to the system that provided the old
  config server, so that the *same* hostname points to the new
  config server.

## Restart the `mongos` Instances

With replica set config servers, the `mongos` instances
specify in the `--configdb` or `sharding.configDB`
setting the config server replica set name and at least one of the
replica set members. The `mongos` instances for the sharded
cluster must specify the same config server replica set name but can
specify different members of the replica set. 

If a `mongos` instance specifies a migrated replica set member in
the `--configdb` or `sharding.configDB` setting, update
the config server setting for the next time you restart the
`mongos` instance.

For more information, see sharding-setup-start-mongos.

## Migrate the Shards

Migrate the shards one at a time. For each shard, follow the appropriate
procedure in this section.

### Migrate a Replica Set Shard

To migrate a sharded cluster, migrate each member separately. First
migrate the non-primary members, and then migrate the primary
last.

If the replica set has two voting members, add an arbiter to the replica set to ensure the set
keeps a majority of its votes available during the migration. You can
remove the arbiter after completing the migration.

#### Migrate a Member of a Replica Set Shard

1. Shut down the `mongod` process. To ensure a
   clean shutdown, use the `shutdown` command.

#. Move the data directory (i.e., the `dbPath`)
   to the new machine.

#. Restart the `mongod` process at the new
   location.

#. Connect to the replica set's current primary.

#. If the hostname of the member has changed, use
   `rs.reconfig()` to update the replica set configuration
   document with the new hostname.

   For example, the following sequence of commands updates the
   hostname for the instance at position `2` in the `members`
   array:

   ```javascript
   cfg = rs.conf()
   cfg.members[2].host = "pocatello.example.net:27018"
   rs.reconfig(cfg)
   ```

   For more information on updating the configuration document, see
   replica-set-reconfiguration-usage.

#. To confirm the new configuration, issue `rs.conf()`.

#. Wait for the member to recover. To check the member's state, issue
   `rs.status()`.

#### Migrate the Primary in a Replica Set Shard

While migrating the replica set's primary, the set must elect a new
primary. This failover process which renders the replica set
unavailable to perform reads or accept writes for the duration of the
election, which typically completes quickly. If possible, plan the
migration during a maintenance window.

1. Step down the primary to allow the normal failover process. To step down the primary, connect
   to the primary and issue the either the
   `replSetStepDown` command or the `rs.stepDown()`
   method. The following example shows the `rs.stepDown()`
   method:

   ```javascript
   rs.stepDown()
   ```

#. Once the primary has stepped down and another member has become
   `PRIMARY` state. To migrate the stepped-down primary,
   follow the migrate-replica-set-shard-member procedure

   You can check the output of `rs.status()` to confirm the
   change in status.

## Re-Enable the Balancer

To complete the migration, re-enable the balancer to resume
chunk migrations.

Connect to one of the cluster's `mongos` instances and pass
`true` to the `sh.startBalancer()` method: [#autosplit-start]_

```javascript
sh.startBalancer()
```

To check the balancer state, issue the `sh.getBalancerState()`
method.

For more information, see sharding-balancing-enable.
