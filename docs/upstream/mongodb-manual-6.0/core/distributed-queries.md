<!-- Converted from core/distributed-queries.txt (reStructuredText). Includes are inlined. -->

# Distributed Queries

## Read Operations to Replica Sets

By default, clients reads from a replica set's primary;
however, clients can specify a read preference to direct read operations to other members.
For example, clients can configure read preferences to read from
secondaries or from nearest member to:

- reduce latency in multi-data-center deployments,

- improve read throughput by distributing high read-volumes (relative
  to write volume),

- perform backup operations, and/or

- allow reads until a new primary is elected.

(Figure: /images/replica-set-read-preference.bakedsvg.svg)

Read operations from secondary members of replica sets may not reflect
the current state of the primary. Read preferences that direct read
operations to different servers may result in non-monotonic reads.

Clients can use causally consistent
sessions, which provides various guarantees including monotonic reads.

You can configure the read preference on a per-connection or
per-operation basis. For more information on read preference or on the
read preference modes, see /core/read-preference and
replica-set-read-preference-modes.

## Write Operations on Replica Sets

In replica sets, all write operations go to the
set's primary. The primary applies the write operation and
records the operations on the primary's operation log or oplog.
The oplog is a reproducible sequence of operations to the data set.
secondary members of the set continuously replicate the oplog
and apply the operations to themselves in an asynchronous process.

(Figure: /images/replica-set-read-write-operations-primary.bakedsvg.svg)

For more information on replica sets and write operations, see
/replication and
/reference/write-concern.

## Read Operations to Sharded Clusters

Sharded clusters allow you to partition a data
set among a cluster of `mongod` instances in a way that is
nearly transparent to the application. For an overview of sharded
clusters, see the /sharding section of this manual.

For a sharded cluster, applications issue operations to one of the
`mongos` instances associated with the cluster.

(Figure: /images/sharded-cluster.bakedsvg.svg)

Read operations on sharded clusters are most efficient when directed to
a specific shard. Queries to sharded collections should include the
collection's shard key. When a query
includes a shard key, the `mongos` can use cluster metadata
from the config database to route the
queries to shards.

(Figure: /images/sharded-cluster-targeted-query.bakedsvg.svg)

If a query does not include the shard key, the `mongos` must
direct the query to *all* shards in the cluster. These *scatter
gather* queries can be inefficient. On larger clusters, scatter gather
queries are unfeasible for routine operations.

(Figure: /images/sharded-cluster-scatter-gather-query.bakedsvg.svg)

For replica set shards, read operations from secondary members of
replica sets may not reflect the current state of the primary. Read
preferences that direct read operations to different servers may result
in non-monotonic reads.

**Note:**

- Clients can use causally consistent
  sessions, which provides various guarantees, including monotonic
  reads.

- All members of a shard replica set, not just the primary, maintain
  the metadata regarding chunk metadata. This prevents reads from
  the secondaries from returning orphaned data if not using read concern `"available"`.
  In earlier versions, reads from secondaries, regardless of the
  read concern, could return orphaned documents.

For more information on read operations in sharded clusters, see the
/core/sharded-cluster-query-router and sharding-shard-key
sections.

## Write Operations on Sharded Clusters

For sharded collections in a sharded cluster, the
`mongos` directs write operations from applications to the
shards that are responsible for the specific *portion* of the data
set. The `mongos` uses the cluster metadata from the
config database to route the write
operation to the appropriate shards.

(Figure: /images/sharded-cluster.bakedsvg.svg)

MongoDB partitions data in a sharded collection into *ranges* based on
the values of the shard key. Then, MongoDB distributes these
chunks to shards. The shard key determines the distribution of chunks to
shards. This can affect the performance of write operations in the
cluster.

(Figure: /images/sharding-range-based.bakedsvg.svg)

**Important:** Update operations that affect a *single* document

**must** include the shard key or the `_id`
field. Updates that affect multiple documents are more efficient in
some situations if they have the shard key, but can be
broadcast to all shards.

If the value of the shard key increases or decreases with every
insert, all insert operations target a single shard. As a result, the
capacity of a single shard becomes the limit for the insert capacity
of the sharded cluster.

For more information, see /sharding and
/core/bulk-write-operations.

**See also:**

retryable-writes

## Change Streams and Orphan Documents

Starting in MongoDB 5.3, during range migration, change stream
events are not generated for updates to orphaned documents.
