<!-- Converted from core/transactions-sharded-clusters.txt (reStructuredText). Includes are inlined. -->

# Production Considerations (Sharded Clusters)

You can perform multi-document transactions on sharded clusters.

The following page lists concerns specific to running transactions on a
sharded cluster. These concerns are in addition to those listed in
/core/transactions-production-consideration.

## Performance

### Single Shard

Transactions that target a single shard should have the same
performance as replica-set transactions.

### Multiple Shards

Transactions that affect multiple shards incur a greater performance
cost.

**Note:**

On a sharded cluster, transactions that span multiple shards will
error and abort if any involved shard contains an arbiter.

### Time Limit

To specify a time limit, specify a `maxTimeMS` limit on
`commitTransaction`. 

If `maxTimeMS` is unspecified, MongoDB will use the
`transactionLifetimeLimitSeconds`.

If `maxTimeMS` is specified but would result in transaction that
exceeds `transactionLifetimeLimitSeconds`, MongoDB will use
the `transactionLifetimeLimitSeconds`.

To modify `transactionLifetimeLimitSeconds` for a sharded
cluster, the parameter must be modified for all shard replica set
members.

## Read Concerns

Multi-document transactions support `"local"`,
`"majority"`, and `"snapshot"` read concern
levels.

For transactions on a sharded cluster, only the
`"snapshot"` read concern provides a consistent snapshot
across multiple shards.

For more information on read concern and transactions, see
transactions-read-concern.

## Write Concerns

You cannot run transactions on a sharded cluster that has a shard
with `writeConcernMajorityJournalDefault` set to `false`
(such as a shard with a voting member that uses the in-memory
storage engine).

**Note:**

Regardless of the write concern specified for the
transaction, the commit operation for a
sharded cluster transaction includes some parts that use ``{w:
"majority", j: true}`` write concern.

## Arbiters

You cannot change a shard key using a transaction
if the replica set has an arbiter. Arbiters cannot participate in the
data operations required for multi-shard transactions.

Transactions whose write operations span multiple shards will error
and abort if any transaction operation reads from or writes to a
shard that contains an arbiter.

## Backups and Restores

**Warning:**

To use `mongodump` and `mongorestore` as a backup
strategy for sharded clusters, see backup-sharded-dumps.

Sharded clusters can also use one of the following coordinated backup
and restore processes, which maintain the atomicity guarantees of
transactions across shards:

- [MongoDB Atlas](https://www.mongodb.com/atlas/database?tck=docs_server)

- [MongoDB Cloud Manager](https://www.mongodb.com/cloud/cloud-manager?tck=docs_server)

- [MongoDB Ops Manager](https://www.mongodb.com/products/ops-manager?tck=docs_server)

## Chunk Migrations

Chunk migration acquires
exclusive collection locks during certain stages.

If an ongoing transaction has a lock on a collection and a chunk
migration that involves that collection starts, these migration stages
must wait for the transaction to release the locks on the collection,
thereby impacting the performance of chunk migrations.

If a chunk migration interleaves with a transaction (for instance, if a
transaction starts while a chunk migration is already in progress and
the migration completes before the transaction takes a lock on the
collection), the transaction errors during the commit and aborts.

Depending on how the two operations interleave, some sample errors
include (the error messages have been abbreviated):

- `an error from cluster data placement change ... migration commit in progress for <namespace>`

- `Cannot find shardId the chunk belonged to at cluster time ...`

**See also:**

`shardingStatistics.countDonorMoveChunkLockTimeout`

## Outside Reads During Commit

During the commit for a transaction, outside read operations may try
to read the same documents that will be modified by the transaction.
If the transaction writes to multiple shards, then during the commit
attempt across the shards:

- Outside reads that use read concern `"snapshot"` or
  `"linearizable"` wait until all writes of a transaction 
  are visible.

- Outside reads that are part of causally consistent
  sessions (those that include 
  afterClusterTime) wait until all writes
  of a transaction are visible.

- Outside reads using other read concerns do not wait until all writes
  of a transaction are visible, but instead read the 
  before-transaction version of the documents.

**See also:**

transactions-atomicity

## Additional Information

See also /core/transactions-production-consideration.
