<!-- Converted from reference/read-concern-majority.txt (reStructuredText). Includes are inlined. -->

# Read Concern `"majority"`

**`"majority"`**

For read operations not associated with multi-document
transactions, read concern `"majority"`
guarantees that the data read has been acknowledged by a majority of
the replica set members. The documents read are durable and
guaranteed to not roll back.

For operations in multi-document transactions, read concern `"majority"` provides its
guarantees only if the transaction commits with write concern
"majority". Otherwise, the
`"majority"` read concern provides no guarantees about the
data read in transactions.

Regardless of the read concern level, the most recent data on a
node may not reflect the most recent version of the data in the system.

For more information about what happens if a primary fails, see
replication-auto-failover.

## Performance

Each replica set member maintains, in memory, a view of the data at the
majority-commit point; the majority-commit point is calculated by the
primary. To fulfill read concern `"majority"`, the node returns data
from this view and is comparable in performance to other read
concerns.

## Availability

Read concern `"majority"` is available for use with or
without causally consistent sessions and transactions.

**Warning:**

If you are using a three-member primary-secondary-arbiter (PSA) 
architecture, consider the following:

- The write concern `"majority"` can cause
  performance issues if a secondary is unavailable or lagging. For 
  advice on how to mitigate these issues, see 
  performance-issues-psa.

- If you are using a global default `"majority"` 
  and the write concern is less than the size of the majority,
  your queries may return stale (not fully replicated) data.

## Example

Consider the following timeline of a write operation Write`0` to
a three member replica set:

**Note:**

For simplification, the example assumes:

- All writes prior to Write`0` have been successfully
  replicated to all members.

- Write`prev` is the previous write before Write`0`.

- No other writes have occured after Write`0`. 

(Figure: /images/read-concern-write-timeline.svg)

| Time | Event | Most Recent Write | Most Recent w: "majority" write |
|---|---|---|---|
| t`0` | Primary applies Write`0` | \| **Primary**: Write`0` \| **Secondary**`1`: Write`prev` \| **Secondary**`2`: Write`prev` | \| **Primary**: Write`prev` \| **Secondary**`1`: Write`prev` \| **Secondary**`2`: Write`prev` |
| t`1` | Secondary`1` applies write`0` | \| **Primary**: Write`0` \| **Secondary**`1`: Write`0` \| **Secondary**`2`: Write`prev` | \| **Primary**: Write`prev` \| **Secondary**`1`: Write`prev` \| **Secondary**`2`: Write`prev` |
| t`2` | Secondary`2` applies write`0` | \| **Primary**: Write`0` \| **Secondary**`1`: Write`0` \| **Secondary**`2`: Write`0` | \| **Primary**: Write`prev` \| **Secondary**`1`: Write`prev` \| **Secondary**`2`: Write`prev` |
| t`3` | Primary is aware of successful replication to Secondary`1` and sends acknowledgment to client | \| **Primary**: Write`0` \| **Secondary**`1`: Write`0` \| **Secondary**`2`: Write`0` | \| **Primary**: Write`0` \| **Secondary**`1`: Write`prev` \| **Secondary**`2`: Write`prev` |
| t`4` | Primary is aware of successful replication to Secondary`2` | \| **Primary**: Write`0` \| **Secondary**`1`: Write`0` \| **Secondary**`2`: Write`0` | \| **Primary**: Write`0` \| **Secondary**`1`: Write`prev` \| **Secondary**`2`: Write`prev` |
| t`5` | Secondary`1` receives notice (through regular replication mechanism) to update its snapshot of its most recent w: "majority" write | \| **Primary**: Write`0` \| **Secondary**`1`: Write`0` \| **Secondary**`2`: Write`0` | \| **Primary**: Write`0` \| **Secondary**`1`: Write`0` \| **Secondary**`2`: Write`prev` |
| t`6` | Secondary`2` receives notice (through regular replication mechanism) to update its snapshot of its most recent w: "majority" write | \| **Primary**: Write`0` \| **Secondary**`1`: Write`0` \| **Secondary**`2`: Write`0` | \| **Primary**: Write`0` \| **Secondary**`1`: Write`0` \| **Secondary**`2`: Write`0` |

Then, the following tables summarizes the state of the data that a read
operation with `"majority"` read concern would see at
time `T`.

(Figure: /images/read-concern-write-timeline.svg)

| Read Target | Time `T` | State of Data |
|---|---|---|
| Primary | Before t`3` | Data reflects Write`prev` |
| Primary | After t`3` | Data reflects Write`0` |
| Secondary`1` | Before t`5` | Data reflects Write`prev` |
| Secondary`1` | After t`5` | Data reflects Write`0` |
| Secondary`2` | Before or at t`6` | Data reflects Write`prev` |
| Secondary`2` | After t`6` | Data reflects Write`0` |

## Storage Engine Support

Read concern `"majority"` is available for the
WiredTiger storage engine.

**Tip:**

The `serverStatus` command returns the
`storageEngine.supportsCommittedReads` field, which
indicates whether the storage engine supports `"majority"` read
concern.

## Read Concern `"majority"` and Transactions

**Note:**

You set the read concern at the transaction level, not at the
individual operation level. To set the read concern for
transactions, see transactions-read-concern.

For operations in multi-document transactions, read concern `"majority"` provides its
guarantees only if the transaction commits with write concern
"majority". Otherwise, the
`"majority"` read concern provides no guarantees about the
data read in transactions.

## Read Concern `"majority"` and Aggregation

You can specify read concern level 
`"majority"` for an aggregation that includes an `$out` 
stage.

## Read Your Own Writes

You can use causally consistent sessions to read your own 
writes, if the writes request acknowledgment.

## Primary-Secondary-Arbiter Replica Sets

Starting in MongoDB 5.0,
`enableMajorityReadConcern` and 
`--enableMajorityReadConcern` cannot be changed 
and are always set to `true` due to storage engine improvements. 

In earlier versions of MongoDB, 
`enableMajorityReadConcern` and 
`--enableMajorityReadConcern` are configurable and can be set 
to `false` to prevent storage cache pressure from immobilizing a 
deployment with a three-member primary-secondary-arbiter (PSA) 
architecture.

If you are using a three-member primary-secondary-arbiter (PSA) 
architecture, consider the following:

- The write concern `"majority"` can cause
  performance issues if a secondary is unavailable or lagging. For 
  advice on how to mitigate these issues, see 
  performance-issues-psa.

- If you are using a global default `"majority"` 
  and the write concern is less than the size of the majority,
  your queries may return stale (not fully replicated) data.
