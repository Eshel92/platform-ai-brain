<!-- Converted from reference/read-concern-available.txt (reStructuredText). Includes are inlined. -->

# Read Concern `"available"`

A query with read concern `"available"` returns data from the instance
with no guarantee that the data has been written to a majority of the
replica set members (i.e. may be rolled back).

- **For a sharded cluster**, `"available"` read concern
  provides greater tolerance for partitions.

  Queries with the `"available"` read concern don't require a
  check to ensure that the correct shard received the query.

  In the event of network partitions, these queries route to the shard 
  considered appropriate before the network partition occurred.  They do not
  wait for consistency guarantees from servers that may be unavailable.  If
  the shard was undergoing chunk migration, queries with 
  `"available"` can return orphaned documents.

  **Warning:**

  `mongos` does not guarantee that queries with read concern
  `"available"` route to the correct shards.  The shard that
  receives the query returns data, but this shard may not be the
  authoritative owner of the requested data.

  This can cause queries to return incorrect or unexpected results.

- **For unsharded collections** (including collections in a standalone
  deployment or a replica set deployment), `"local"` and
  `"available"` read concerns behave identically.

Regardless of the read concern level, the most recent data on a
node may not reflect the most recent version of the data in the system.

**See also:**

`orphanCleanupDelaySecs`

## Availability

Read concern `"available"` is unavailable for use
with causally consistent sessions and transactions.

       

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
operation with `"available"` read concern would see at
time `T`.

(Figure: /images/read-concern-write-timeline.svg)

| Read Target | Time `T` | State of Data |
|---|---|---|
| Primary | After t`0` | Data reflects Write`0`. |
| Secondary`1` | Before t`1` | Data reflects Write`prev` |
| Secondary`1` | After t`1` | Data reflects Write`0` |
| Secondary`2` | Before t`2` | Data reflects Write`prev` |
| Secondary`2` | After t`2` | Data reflects Write`0` |
