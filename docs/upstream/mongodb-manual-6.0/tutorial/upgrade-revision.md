<!-- Converted from tutorial/upgrade-revision.txt (reStructuredText). Includes are inlined. -->

# Upgrade to the Latest Self-Managed Patch Release of MongoDB

MongoDB versioning has the form
`X.Y.Z` where `Z` refers to the revision/patch number.
Revisions provide security patches, bug fixes, and new or changed
features that generally do not contain any backward breaking changes.
Always upgrade to the latest revision in your release series.

For more information on versioning, see release-version-numbers.

## Before Upgrading

### Backup

Ensure you have an up-to-date backup of your data set. See
/core/backups.

### Compatibility Considerations

- Consult the following documents for any special considerations or
  compatibility issues specific to your MongoDB release:

  - The release notes, located at /release-notes.

  - The `documentation for your driver`.

**Important:**

- Starting in MongODB 4.2, MongoDB removes support for Ubuntu 16.04
  PPCLE.

- Starting in MongoDB 3.6.13, MongoDB 3.6-series removes support for
  Ubuntu 16.04 PPCLE.

- Starting in MongoDB 3.4.21, MongoDB 3.4-series removes support for
  Ubuntu 16.04 PPCLE.

     

### Maintenance Window

If your installation includes replica sets, plan
the upgrade during a predefined maintenance window.

### Change Streams

Starting in MongoDB 4.0.7, change streams use a version 1 `v1` resume
tokens. MongoDB versions earlier than 4.0.7 use `v0` resume tokens.

When upgrading from MongoDB 4.0.6 or earlier to MongoDB 4.0.7 or later,
a client may try to resume change streams using the new `v1` resume
token when connected to a member that has not been updated (i.e. only
accepts `v0` or BinData token) and fail. In such cases, the client
must wait for the upgrade to complete before resuming change streams.

### Staging Environment Check

Before you upgrade a production environment, use the procedures in this
document to upgrade a *staging* environment that reproduces your
production environment, to ensure that your production configuration is
compatible with all changes.

## Upgrade Procedure

**Important:** Always backup all of your data before upgrading MongoDB.

Upgrade each `mongod` and `mongos` binary
separately, using the procedure described here. When upgrading a binary,
use the procedure upgrade-mongodb-instance.

Follow this upgrade procedure:

1. For deployments that use authentication, first upgrade all of your
   MongoDB Drivers. To upgrade, see the
   `documentation for your driver`.

#. Upgrade sharded clusters, as described in
   upgrade-sharded-cluster.

#. Upgrade any standalone instances. See
   upgrade-mongodb-instance.

#. Upgrade any replica sets that are not part of a sharded cluster, as
   described in upgrade-replica-set.

## Upgrade a MongoDB Instance

To upgrade a `mongod` or `mongos` instance,
use one of these approaches:

- Upgrade the instance using the operating system's package management
  tool and the official MongoDB packages. This is the preferred
  approach. See /installation.

- Upgrade the instance by replacing the existing binaries with new
  binaries. See upgrade-replace-binaries.

- Make any required configuration file changes before restarting the
  instance.

## Replace the Existing Binaries

**Important:** Always backup all of your data before upgrading MongoDB.

This section describes how to upgrade MongoDB by replacing the existing
binaries. The preferred approach to an upgrade is to use the operating
system's package management tool and the official MongoDB packages, as
described in /installation.

To upgrade a `mongod` or `mongos` instance by
replacing the existing binaries:

1. Download the binaries for the latest MongoDB revision from the
   MongoDB Download Page and store the binaries in a temporary
   location. The binaries download as compressed files that uncompress
   to the directory structure used by the MongoDB installation.

#. Shutdown the instance.

#. Replace the existing MongoDB binaries with the downloaded binaries.

#. Make any required configuration file changes.

#. Restart the instance.

## Upgrade Replica Sets

To upgrade a replica set, upgrade each member individually, starting with
the secondaries and finishing with the
primary. Plan the upgrade during a predefined maintenance window.

**Important:**

Before you upgrade or downgrade a replica set, ensure all replica set
members are running. If you do not, the upgrade or downgrade will not
complete until all members are started.

**Note:**

Starting in MongoDB 4.0.7, change streams use a version 1 `v1`
resume tokens. MongoDB versions
earlier than 4.0.7 use `v0` resume tokens or BinData resume tokens.

When upgrading from MongoDB 4.0.0-4.0.6 to MongoDB 4.0.7 or later,
a client may try to resume change streams using the new `v1`
resume token when connected to a member that has not been updated
(i.e. only accepts `v0` token or BinData) and fail. In such cases, the
client must wait for the upgrade to complete before resuming change
streams.

### Upgrade Secondaries

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

### Upgrade the Primary

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

## Upgrade Sharded Clusters

**Changed in version:** 3.4

The procedure applies to 6.0. To make revision 
upgrades for other versions of MongoDB sharded clusters, refer to 
the appropriate version of the manual.

**Note:**

Starting in MongoDB 4.0.7, change streams use a version 1 `v1`
resume tokens. MongoDB versions
earlier than 4.0.7 use `v0` resume tokens or BinData resume tokens.

When upgrading from MongoDB 4.0.6 or earlier to 4.0.7 or later, the
members of the sharded clusters will continue to produce `v0` or
BinData resume tokens until the `mongos` instance(s)
are updated. Upgraded `mongos` instances will begin
producing `v1` change stream resume tokens. These tokens cannot be
used to resume a stream on a `mongos` that has not yet
been upgraded to 4.0.7 or later.

To upgrade a 6.0 sharded cluster:

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
