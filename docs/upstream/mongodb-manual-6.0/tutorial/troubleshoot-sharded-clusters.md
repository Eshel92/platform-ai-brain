<!-- Converted from tutorial/troubleshoot-sharded-clusters.txt (reStructuredText). Includes are inlined. -->

# Troubleshoot Sharded Clusters

This page describes common strategies for troubleshooting
sharded cluster deployments.

## Application Servers or `mongos` Instances Become Unavailable

If each application server has its own `mongos` instance, other
application servers can continue to access the database. Furthermore,
`mongos` instances do not maintain persistent state, and they
can restart and become unavailable without losing any state or data.
When a `mongos` instance starts, it retrieves a copy of the
config database and can begin routing queries.

## A Single Member Becomes Unavailable in a Shard Replica Set

Replica sets provide high availability for
shards. If the unavailable `mongod` is a primary,
then the replica set will elect a new
primary. If the unavailable `mongod` is a
secondary, and it disconnects the primary and secondary will
continue to hold all data. In a three member replica set, even if a
single member of the set experiences catastrophic failure, two other
members have full copies of the data. [#recovery-window]_

Always investigate availability interruptions and failures. If a system
is unrecoverable, replace it and create a new member of the replica set
as soon as possible to replace the lost redundancy.

## All Members of a Shard Become Unavailable

In a sharded cluster, `mongod` and `mongos` instances
monitor the replica sets in the sharded cluster (e.g. shard replica
sets, config server replica set).

If all members of a replica set shard are unavailable, all data held in
that shard is unavailable. However, the data on all other shards will
remain available, and it is possible to read and write data to the
other shards. However, your application must be able to deal with
partial results, and you should investigate the cause of the
interruption and attempt to recover the shard as soon as possible.

## A Config Server Replica Set Member Become Unavailable

Replica sets provide high availability for
the config servers. If an unavailable config server is a
primary, then the replica set will 
elect a new primary.

If the replica set config server loses its primary and cannot elect a
primary, the cluster's metadata becomes *read only*. You can still read
and write data from the shards, but no chunk migration or chunk splits will occur until a primary
is available.

**Note:**

For production deployments, we recommend deplying config server and shard replica
sets on at least three data centers. This configuration provides high availability in case
a single data center goes down.

**Note:**

All config servers must be running and available when you first initiate
a sharded cluster.

## Cursor Fails Because of Stale Config Data

A query returns the following warning when one or more of the
`mongos` instances has not yet updated its cache of the
cluster's metadata from the config database:

```none
could not initialize cursor across all shards because : stale config detected
```

This warning *should* not propagate back to your application. The
warning will repeat until all the `mongos` instances refresh
their caches. To force an instance to refresh its cache, run the
`flushRouterConfig` command.

## Shard Keys

To troubleshoot a shard key, see
shardkey-troubleshoot-shard-keys.

## Cluster Availability

To ensure cluster availability:

- Each shard should be a replica set, if a specific
  `mongod` instance fails, the replica set members will elect
  another to be primary and continue operation. However, if an
  entire shard is unreachable or fails for some reason, that data will
  be unavailable.

- The shard key should allow the `mongos` to isolate most
  operations to a single shard. If operations can be processed by a
  single shard, the failure of a single shard will only render *some*
  data unavailable. If operations need to access all shards for queries,
  the failure of a single shard will render the entire cluster
  unavailable.

## Config Database String Error

Config servers must be deployed as replica
sets. The `mongos` instances for the sharded cluster must
specify the same config server replica set name but can specify
hostname and port of different members of the replica set.

With earlier versions of MongoDB sharded clusters that use the topology
of three mirrored `mongod` instances for config servers,
`mongos` instances in a sharded cluster must specify identical
`configDB` string.

## Avoid Downtime when Moving Config Servers

Use CNAMEs to identify your config servers to the cluster so
that you can rename and renumber your config servers without downtime.

## `moveChunk commit failed` Error

At the end of a chunk migration, the
shard must connect to the config database to update the
chunk's record in the cluster metadata. If the shard fails to
connect to the config database, MongoDB reports the following
error:

```none
ERROR: moveChunk commit failed: version is at <n>|<nn> instead of
<N>|<NN>" and "ERROR: TERMINATING"
```

When this happens, the primary member of the shard's replica
set then terminates to protect data consistency. If a secondary
member can access the config database, data on the shard becomes
accessible again after an election.

The user will need to resolve the chunk migration failure
independently. If you encounter this issue, ask the [MongoDB Community](https://community.mongodb.com/?tck=docs_server) or
MongoDB Support to address this issue.
