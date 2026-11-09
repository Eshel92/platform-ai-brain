<!-- Converted from reference/replica-set-protocol-versions.txt (reStructuredText). Includes are inlined. -->

# Self-Managed Replica Set Protocol Version

MongoDB only supports replica set protocol version 1 
(`pv1`). `pv1` is the default for all new replica 
sets.

## Preservation of Writes

### `w:1` Writes

With `pv1`, you can use
`catchUpTimeoutMillis` to prioritize between faster
failovers and preservation of `w:1 <` writes.

### `w: "majority"` Writes

`pv1` guarantees the preservation of confirmed `w:
"majority"` writes.

## Availability

`pv1` is available in MongoDB version 3.2 or later and is the default
for all new replica sets.

## Vetoes

`pv1` does not use vetoes. Individual members can vote for or against
a candidate in a particular election, but cannot individually veto (abort)
an election unilaterally.

## Detection of Simultaneous Primaries

In some circumstances, two nodes in a replica set
may *transiently* believe that they are the primary, but at most, one
of them will be able to complete writes with `{ w:
"majority" }` write concern. The node that can complete
`{ w: "majority" }` writes is the current
primary, and the other node is a former primary that has not yet
recognized its demotion, typically due to a network partition.
When this occurs, clients that connect to the former primary may
observe stale data despite having requested read preference
`primary`, and new writes to the former primary will
eventually roll back.

`pv1` uses the concept of term. This allows for a faster
detection of simultaneous primaries and for multiple successful
elections in a short period of time.

## Back to Back Elections

`pv1` makes a "best-effort" attempt to have the secondary with the
highest `priority` available call an election. This
could lead to back-to-back elections as eligible members with
higher priority can call an election.

However, for `pv1`:

- Priority elections have been limited to occur only if the higher
  priority node is within 10 seconds of the current primary. 

- Arbiters will vote no in elections if they detect a healthy primary
  of equal or greater priority to the candidate.

## Double Voting

`pv1` prevents double voting in one member's call for election. This
is achieved through its use of terms.
