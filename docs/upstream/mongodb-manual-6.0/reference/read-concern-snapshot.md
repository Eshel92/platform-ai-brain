<!-- Converted from reference/read-concern-snapshot.txt (reStructuredText). Includes are inlined. -->

# Read Concern `"snapshot"`

   

**Changed in version:** 5.0

A query with read concern `"snapshot"` returns majority-committed data as it 
appears across shards from a specific single point in time in the recent past. 
Read concern `"snapshot"` provides its guarantees only if the transaction 
commits with write concern `"majority"`.

Read concern `"snapshot"` is available for multi-document
transactions, and starting in MongoDB 5.0, certain
read operations outside of multi-document transactions.

- If the transaction is not part of a causally consistent session, upon transaction commit with write concern
  `"majority"`, the transaction operations are guaranteed
  to have read from a snapshot of majority-committed data.

- If the transaction is part of a causally consistent session, upon transaction commit with write concern
  `"majority"`, the transaction operations are guaranteed
  to have read from a snapshot of majority-committed data that provides
  causal consistency with the operation immediately preceding the
  transaction start.

Outside of multi-document transactions, read concern
`"snapshot"` is available on primaries and secondaries for
the following read operations:

- `find`
- `aggregate`
- `distinct` (on unsharded collections)

All other read commands prohibit `"snapshot"`.

## Operations

For a list of all operations that accept read concerns, see
read-concern-operations.

## Snapshot Isolation Limitation

Read operations with read concern `"snapshot"` guarantee snapshot
isolation only in the absence of concurrent drop or rename operations on
collections in the read operation. In most cases, MongoDB detects when
an operation removes a collection ahead of the read snapshot and reports
a `SnapshotUnavailable` error. If this detection is not possible, the
read operation reflects the dropped or renamed collection even though
the collection existed during the time of the snapshot. This
limitation applies to all read concerns for
operations within and outside a multi-document transaction.

## Read Concern and Transactions

Multi-document transactions support read concern
`"snapshot"` as well as `"local"`, and
`"majority"`.

**Note:**

You set the read concern at the transaction level, not at the
individual operation level. To set the read concern for
transactions, see transactions-read-concern.

## Read Concern and `atClusterTime`

**New in version:** 5.0

Outside of multi-document transactions, reads with read concern
`"snapshot"` support the optional parameter
`atClusterTime`. The parameter `atClusterTime` allows you to specify
the timestamp for the read. To satisfy a read request with a specified
`atClusterTime` of T, the `mongod` performs the request
based on the data available at time T.

You can obtain the `operationTime` or `clusterTime` of an operation
from the response of db.runCommand() or from the `Session`
object.

The following command performs a find operation with read concern
`"snapshot"` and specifies that the operation should read
data from the snapshot at cluster time `Timestamp(1613577600, 1)`.

```javascript
db.runCommand( {
    find: "restaurants",
    filter: { _id: 5 },
    readConcern: {
        level: "snapshot",
        atClusterTime: Timestamp(1613577600, 1)
    },
} )
```

If the parameter `atClusterTime` is not supplied, the
`mongos`, or in single member replica sets the
`mongod`, selects the timestamp of the latest
majority-committed snapshot as the `atClusterTime` and returns it to
the client.

Outside of transactions, `"snapshot"` reads are
guaranteed to read from majority-committed data.

### `atClusterTime` Considerations and Behavior

- The allowed values for `atClusterTime` depend on the
  `minSnapshotHistoryWindowInSeconds` parameter.
  `minSnapshotHistoryWindowInSeconds` is the minimum time window in
  seconds for which the storage engine keeps the snapshot history. If
  you specify an atClusterTime value older than
  the oldest snapshot retained according to
  `minSnapshotHistoryWindowInSeconds`, `mongod` returns
  an error.

- If you perform a read operation with `"snapshot"`
  against a delayed replica set member, the returned majority-committed
  data could be stale.

- It is not possible to specify `atClusterTime` for
  `"snapshot"` inside of causally consistent
  sessions.

## Read Concern on Capped Collections

Starting in version 5.0, you cannot use read concern
`"snapshot"` when reading from a
capped collection.
