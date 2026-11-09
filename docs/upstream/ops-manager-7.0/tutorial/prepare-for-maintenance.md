<!-- Converted from tutorial/prepare-for-maintenance.txt (reStructuredText). Includes are inlined. -->

# Prepare for Cluster Maintenance

Ops Manager performs a `rolling restart` when you perform maintenance
on nodes in a cluster. To maintain cluster availability during a 
maintenance period, Automation updates nodes in a cluster in the
following way:

- For three-member replica sets, Automation updates nodes one node at a
  time.
- For five-member replica sets, Automation updates two nodes at a time.

Before you perform maintenance on your clusters, review the following 
considerations and take action, if necessary, to maintain cluster
availability.

**Note:**

To learn about how Automation performs maintenance on your clusters,
see rolling-restart-faq.

## `oplog` Size

Each node in a cluster is restarted in standalone mode before 
maintenance starts. The node replays writes in the oplog to 
catch up to the other nodes when it is added back to the cluster after 
maintenance completes.
  
Make sure that the cluster's oplog is large enough to store all writes
that you application might make during the maintenance period. Use 
the `replication.oplogSizeMB` advanced deployment option
to adjust the oplog size.

## Priority

All client connections to a primary node are dropped when maintenance 
starts on that node. Connections are re-established to the newly elected 
primary node.

You may prefer a node in a specific data center to become the new primary 
node. Edit the cluster's configuration 
and adjust the priority of each node to indicate your preferred primary
node.

## Fault Tolerance

Nodes undergoing maintenance don't provide failover support to the 
cluster. For three-member and five-member replica sets, if an
additional node becomes unavailable during maintenance, the cluster
loses the majority of nodes. The primary node loses this status and 
steps down to become a secondary node. A new primary can't be elected
until a majority of the cluster's nodes become available.

For mission-critical applications with high uptime needs, consider 
adding a temporary arbiter to a 
three-member or five-member replica set before you perform maintenance.
The temporary arbiter can maintain cluster majority in case 
an additional cluster node becomes unavailable during a maintenance 
period.

## Unique Index Builds

Automation builds indexes on cluster nodes one at a time using identical 
but independent commands. To ensure that writes respect the `unique` 
quality of indexed fields in a unique indexe, 
all writes to the collection on the cluster must stop before you build 
the index.

You can't use Data Explorer or the 
Automation Config Resource in 
Ops Manager to create unique indexes in a rolling fashion because these 
methods don't stop writes to the cluster.

If your use case requires you to build new unique indexes: 

1. Stop all writes to the affected collection. For more information.
   see db.fsyncLock() in the
   MongoDB Manual.
2. See Build Indexes on Replica Sets in the MongoDB Manual 
   to build the unique index in a rolling fashion.

**See also:**

data-explorer-create-an-index
