<!-- Converted from tutorial/upgrade-revision.txt (reStructuredText). Includes are inlined. -->

# Upgrade to the Latest Self-Managed Patch Release of MongoDB

For general guidance on MongoDB version numbering, patch release
policy, and upgrade paths, see versions-and-upgrade-paths.

## About this Task

This page describes upgrade procedures for the MongoDB
7.0 release series. To upgrade a different release
series, refer to the corresponding version of the manual.

## Before You Begin

Review the following sections to ensure that your deployment is ready to
be upgraded.

### Backup

Ensure you have an up-to-date backup of your data set. See
backup-methods.

### Compatibility Considerations

Consult the following documents for any special considerations or
compatibility issues specific to your MongoDB release:

- Release notes

- `Driver documentation`

### Maintenance Window

If your installation includes replica sets, set
the upgrade to occur during a predefined maintenance window.

### Staging Environment Check

Before you upgrade a production environment, use the procedures in this
document to upgrade a *staging* environment that reproduces your
production environment. Ensure that your production configuration is
compatible with all changes before upgrading.

## Steps

Upgrade each `mongod` and `mongos` binary
separately:

#. For deployments that use authentication, first upgrade all of your
   MongoDB Drivers. To upgrade, see the
   `documentation for your driver`.

#. Upgrade any standalone instances. See
   upgrade-mongodb-instance.

#. Upgrade any replica sets that are not part of a sharded cluster, as
   described in upgrade-replica-set.

#. Upgrade sharded clusters, as described in
   upgrade-sharded-cluster.

### Upgrade a MongoDB Instance

To upgrade a 7.0 `mongod` or
`mongos` instance, use one of these approaches:

- Upgrade the instance using the operating system's package management
  tool and the official MongoDB packages. This is the preferred
  approach. See 7.0 Upgrade Procedures.

- Upgrade the instance by replacing the existing binaries with new
  binaries. See upgrade-replace-binaries.

#### Replace the Existing Binaries

This section describes how to upgrade MongoDB by replacing the existing
binaries. The preferred approach to an upgrade is to use the operating
system's package management tool and the official MongoDB packages, as
described in 7.0 Upgrade Procedures.

To upgrade a `mongod` or `mongos` instance by
replacing the existing binaries:

1. Download the binaries for the latest MongoDB patch release from the
   MongoDB Download Page and store the binaries in a temporary
   location. The binaries download as compressed files that uncompress
   to the directory structure used by the MongoDB installation.

#. Shutdown the instance.

#. Replace the existing MongoDB binaries with the downloaded binaries.

#. Make any required configuration file changes.

#. Restart the instance.

### Upgrade Replica Sets

To upgrade a 7.0 replica set, upgrade each member
individually, starting with the secondaries and
finishing with the primary. Plan the upgrade during a predefined
maintenance window.

**Important:**

Before you upgrade or downgrade a replica set, ensure all replica set
members are running. If you do not, the upgrade or downgrade will not
complete until all members are started.

#### Upgrade Secondaries

Upgrade each secondary separately as follows:

1. Upgrade the secondary's `mongod` binary by following the
   instructions in upgrade-mongodb-instance.

#. After upgrading a secondary, wait for the secondary to recover to
   the `SECONDARY` state before upgrading the next instance. To
   check the member's state, issue `rs.status()` in
   `mongosh`.

   The secondary may briefly go into `STARTUP2` or `RECOVERING`.
   This is normal. Make sure to wait for the secondary to fully recover
   to `SECONDARY` before you continue the upgrade.

#### Upgrade the Primary

1. Step down the primary to initiate the normal failover procedure. Using one of the following:

   - The `rs.stepDown()` helper in `mongosh`.

   - The `replSetStepDown` database command.

   During failover, the set cannot accept writes. Typically this takes
   10-20 seconds. Plan the upgrade during a predefined maintenance
   window.

   **Note:** Stepping down the primary is preferable to directly

   *shutting down* the primary. Stepping down expedites the
   failover procedure.

#. Once the primary has stepped down, call the `rs.status()`
   method from `mongosh` until you see that another
   member has assumed the `PRIMARY` state.

#. Shut down the original primary and upgrade its instance by
   following the instructions in upgrade-mongodb-instance.

### Upgrade Sharded Clusters

To upgrade a 7.0 sharded cluster:

1. Disable the cluster's balancer as described in
   sharding-balancing-disable-temporarily.

#. Upgrade the config servers.

   To upgrade the config server replica set, use the procedures in
   upgrade-replica-set.

#. Upgrade each shard.

   - If a shard is a replica set, upgrade the shard using the
     procedure titled upgrade-replica-set.

   - If a shard is a standalone instance, upgrade the shard using the
     procedure titled
     upgrade-mongodb-instance.

#. Once the config servers and the shards have been upgraded, upgrade
   each `mongos` instance by following the instructions in
   upgrade-mongodb-instance. You can upgrade the
   `mongos` instances in any order.

#. Re-enable the balancer, as described in sharding-balancing-re-enable.

## Learn More

- production-notes

- sharding-manage-shards

- replica-set-sync
