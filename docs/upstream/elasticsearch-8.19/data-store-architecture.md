<!-- Converted from data-store-architecture.asciidoc (AsciiDoc). Includes are inlined. -->

# Data store architecture

Elasticsearch is a distributed document store. Instead of storing information as rows of columnar data, Elasticsearch stores complex data structures that have been serialized as JSON documents. When you have multiple Elasticsearch nodes in a cluster, stored documents are distributed across the cluster and can be accessed immediately
from any node.

The topics in this section provides information about the architecture of Elasticsearch and how it stores and retrieves data: 

* Nodes and shards: Learn about the basic building blocks of an Elasticsearch cluster, including nodes, shards, primaries, and replicas.
* Node roles: Learn about the different roles that nodes can have in an Elasticsearch cluster.
* Reading and writing documents: Learn how Elasticsearch replicates read and write operations across shards and shard copies.
* Shard allocation, relocation, and recovery: Learn how Elasticsearch allocates and balances shards across nodes.
** Shard allocation awareness: Learn how to use custom node attributes to distribute shards across different racks or availability zones.
* Shard request cache: Learn how Elasticsearch caches search requests to improve performance.

(See `nodes-shards.md`)
(See `node-roles.md`)
(See `docs/data-replication.md`)
(See `modules/shard-ops.md`)
(See `modules/cluster/allocation_awareness.md`)
(See `shard-request-cache.md`)
