<!-- Converted from reference/read-concern-local.txt (reStructuredText). Includes are inlined. -->

# Read Concern `"local"`

A query with read concern `"local"` returns data from the instance
with no guarantee that the data has been written to a majority of the
replica set members (i.e. may be rolled back).

Read concern `"local"` is the default for read operations against the
primary and secondaries.

Regardless of the read concern level, the most recent data on a
node may not reflect the most recent version of the data in the system.

## Availability

Read concern `"local"` is available for use with or without
causally consistent sessions and transactions.

## Read Concern local and Transactions

You set the read concern at the transaction level, not at the
individual operation level. To set the read concern for transactions,
see transactions-read-concern.

You can create collections and indexes inside a transaction. If
explicitly creating a
collection or an index, the transaction must use read concern
`"local"`. If you implicitly create a collection, you can
use any of the read concerns available for transactions.

On a replica set, even if a transaction uses read concern `local`, you
might observe stronger read isolation where the operation reads from a
snapshot at the point in time that the transaction was opened.

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
operation with `"local"` read concern would see at
time `T`.

(Figure: /images/read-concern-write-timeline.svg)

| Read Target | Time `T` | State of Data |
|---|---|---|
| Primary | After t`0` | Data reflects Write`0`. |
| Secondary`1` | Before t`1` | Data reflects Write`prev` |
| Secondary`1` | After t`1` | Data reflects Write`0` |
| Secondary`2` | Before t`2` | Data reflects Write`prev` |
| Secondary`2` | After t`2` | Data reflects Write`0` |
