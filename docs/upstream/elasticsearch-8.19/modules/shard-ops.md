<!-- Converted from modules/shard-ops.asciidoc (AsciiDoc). Includes are inlined. -->

## Shard allocation, relocation, and recovery

Each index in Elasticsearch is divided into one or more shards. 
Each document in an index belongs to a single shard.

A cluster can contain multiple copies of a shard. Each shard has one distinguished shard copy called the _primary_, and zero or more non-primary copies called _replicas_. The primary shard copy serves as the main entry point for all indexing operations. The operations on the primary shard copy are then forwarded to its replicas.

Replicas maintain redundant copies of your data across the nodes in your cluster, protecting against hardware failure and increasing capacity to serve read requests like searching or retrieving a document. If the primary shard copy fails, then a replica is promoted to primary and takes over the primary's responsibilities.

Over the course of normal operation, Elasticsearch allocates shard copies to nodes, relocates shard copies across nodes to balance the cluster or satisfy new allocation constraints, and recovers shards to initialize new copies. In this topic, you'll learn how these operations work and how you can control them.

**Tip:** To learn about optimizing the number and size of shards in your cluster, refer to Size your shards. To learn about how read and write operations are replicated across shards and shard copies, refer to Reading and writing documents.

### Shard allocation

Shard allocation is the process of assigning shard copies to nodes. This can
happen during initial recovery, replica allocation, rebalancing, when nodes are added to or removed from the cluster, or when cluster or index settings that impact allocation are updated.
By default, the primary and replica shard copies for an index can be allocated to any node in the cluster, and may be relocated to rebalance the cluster. 

#### Adjust shard allocation settings

You can control how shard copies are allocated using the following settings:

- Cluster-level shard allocation settings: Use these settings to control how shard copies are allocated and balanced across the entire cluster. For example, you might want to allocate nodes availability zones, or prevent certain nodes from being used so you can perform maintenance.

- Index-level shard allocation settings: Use these settings to control how the shard copies for a specific index are allocated. For example, you might want to allocate an index to a node in a specific data tier, or to an node with specific attributes.

#### Monitor shard allocation

If a shard copy is unassigned, it means that the shard copy is not allocated to any node in the cluster. This can happen if there are not enough nodes in the cluster to allocate the shard copy, or if the shard copy can't be allocated to any node that satisfies the shard allocation filtering rules. When a shard copy is unassigned, your cluster is considered unhealthy and returns a yellow or red cluster health status.

You can use the following APIs to monitor shard allocation:

- Cluster allocation explain
- cat allocation
- cluster health

Learn more about troubleshooting unassigned shard copies and recovering your cluster health.

### Shard recovery

Shard recovery is the process of initializing a shard copy, such as restoring a
primary shard from a snapshot or creating a replica shard from a primary shard.
When a shard recovery completes, the recovered shard is available for search
and indexing.

Recovery automatically occurs during the following processes:

* When creating an index for the first time.
* When a node rejoins the cluster and starts up any missing primary shard copies using the data that it holds in its data path.
* Creation of new replica shard copies from the primary.
* Relocation of a shard copy to a different node in the same cluster.
* A snapshot restore operation.
* A clone, shrink, or
split operation.

You can determine the cause of a shard recovery using the recovery or  cat recovery APIs.

#### Adjust shard recovery settings

To control how shards are recovered, for example the resources that can be used by recovery operations, and which indices should be prioritized for recovery, you can adjust the following settings: 

- Index recovery settings
- Cluster-level shard allocation settings
- Index-level shard allocation settings, including delayed allocation and index recovery prioritization 

Shard recovery operations also respect general shard allocation settings. 

#### Monitor shard recovery

You can use the following APIs to monitor shard allocation:

 - View a list of in-progress and completed recoveries using the cat recovery API
 - View detailed information about a specific recovery using the index recovery API

### Shard relocation

Shard relocation is the process of moving shard copies from one node to another. This can happen when a node joins or leaves the cluster, or when the cluster is rebalancing.

When a shard copy is relocated, it is created as a new shard copy on the target node. When the shard copy is fully allocated and recovered, the old shard copy is deleted. If the shard copy being relocated is a primary, then the new shard copy is marked as primary before the old shard copy is deleted.

#### Adjust shard relocation settings

You can control how and when shard copies are relocated. For example, you can adjust the rebalancing settings that control when shard copies are relocated to balance the cluster, or the high watermark for disk-based shard allocation that can trigger relocation. These settings are part of the cluster-level shard allocation settings.

Shard relocation operations also respect shard allocation and recovery settings.
