<!-- Converted from faq/sharding.txt (reStructuredText). Includes are inlined. -->

# FAQ: Sharding with MongoDB

This document answers common questions about /sharding. See also
the /sharding section in the manual, which provides an
overview of sharding, including details on:

- Shard Keys and Considerations for Shard Key Selection

- Query Routing

- sharding-availability

- /core/sharding-data-partitioning and
  Chunk Migration Process

- /tutorial/troubleshoot-sharded-clusters

## Is sharding appropriate for a new deployment?

Sometimes. However, if your data set fits on a single server, you
should begin with an unsharded deployment as sharding while your data
set is small provides *little advantage* .

## Can I select a different shard key after sharding a collection?

Your options for changing a shard key depend on the version of MongoDB
that you are running:

- Starting in MongoDB 5.0, you can reshard a collection by changing a document's shard key.
- You can refine a shard key by adding a suffix field 
  or fields to the existing shard key.

**See also:**

/core/sharding-shard-key

## Why are my documents not distributed across the shards?

The balancer starts distributing data across the shards once the
distribution of chunks has reached certain thresholds. See
sharding-migration-thresholds.

In addition, MongoDB cannot move a chunk if the number of documents in
the chunk exceeds a certain number. See
migration-chunk-size-limit and jumbo-chunk.

## How does `mongos` detect changes in the sharded cluster configuration?

`mongos` instances maintain a cache of the config
database that holds the metadata for the sharded cluster.

`mongos` updates its cache lazily by issuing a request to a
shard and discovering that its metadata is out of date. To force the
`mongos` to reload its cache, you can run the
`flushRouterConfig` command against each `mongos`
directly.

## What does `writebacklisten` in the log mean?

The writeback listener is a process that opens a long poll to relay
writes back from a `mongod` or `mongos` after
migrations to make sure they have not gone to the wrong server.  The
writeback listener sends writes back to the correct server if
necessary.

These messages are a key part of the sharding infrastructure and should
not cause concern.

## How does `mongos` use connections?

Each `mongos` instance maintains a pool of connections to the
members of the sharded cluster. Client requests use these connections
one at a time; i.e. requests are not multiplexed or pipelined.

When client requests complete, the `mongos` returns the
connection to the pool. These pools do not shrink when the number of
clients decreases. This can lead to an unused `mongos` with a
large number of open connections. If the `mongos` is no longer
in use, it is safe to restart the process to close existing connections.

To return aggregated statistics related to all of the outgoing
connection pools used by the `mongos`, connect
`mongosh` to the `mongos`, and run the
`connPoolStats` command:

```bash
db.adminCommand("connPoolStats");
```

See the System Resource Utilization section of the /reference/ulimit
document.
