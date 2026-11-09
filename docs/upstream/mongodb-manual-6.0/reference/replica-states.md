<!-- Converted from reference/replica-states.txt (reStructuredText). Includes are inlined. -->

# Replica Set Member States

Each member of a replica set has a state.

| Number | Name | State Description |
|---|---|---|
| 0 | `STARTUP` | Not yet an active member of any set. All members start up in this state. The `mongod` parses the replica set configuration document while in `STARTUP`. |
| 1 | `PRIMARY` | The member in state primary is the only member that can accept write operations. Eligible to vote. |
| 2 | `SECONDARY` | A member in state secondary is replicating the data store. Eligible to vote. |
| 3 | `RECOVERING` | Members either perform startup self-checks, or transition from completing a rollback or resync. Data is not available for reads from this member. Eligible to vote. |
| 5 | `STARTUP2` | The member is running an initial sync. Eligible to vote, except when newly added to the replica set. |
| 6 | `UNKNOWN` | The member's state, as seen from another member of the set, is not yet known. |
| 7 | `ARBITER` | Arbiters do not replicate data and exist solely to participate in elections. Eligible to vote. |
| 8 | `DOWN` | The member, as seen from another member of the set, is unreachable. |
| 9 | `ROLLBACK` | This member is actively performing a rollback.  Eligible to vote. Data is not available for reads from this member. Starting in version 4.2, MongoDB kills all in-progress user operations when a member enters the `ROLLBACK` state. |
| 10 | `REMOVED` | This member was once in a replica set but was subsequently removed. |

## States

### Core States

**`PRIMARY`**

Members in `PRIMARY` state accept write operations. A replica set has at most
one primary at a time. [#edge-cases-2-primaries]_ A `SECONDARY` member becomes primary
after an election. Members in the `PRIMARY`
state are eligible to vote.

**`SECONDARY`**

Members in `SECONDARY` state replicate the primary's data set
and can be configured to accept read operations. Secondaries are eligible to vote in
elections, and may be elected to the `PRIMARY` state if the
primary becomes unavailable.

**`ARBITER`**

Members in `ARBITER` state do not replicate data or accept write operations.
They are eligible to vote, and exist solely to break a tie during
elections. Replica sets should only have a member in the `ARBITER` state
if the set would otherwise have an even number of voting members, and could suffer
from tied elections. There should only be at most one arbiter configured
in any replica set. For considerations when using an arbiter, see
/core/replica-set-arbiter.

See /core/replica-set-members for more information on core states.

### Other States

**`STARTUP`**

Each member of a replica set starts up in `STARTUP`
state. `mongod` then loads that member's replica set configuration,
and transitions the member's state to `STARTUP2` or `ARBITER`. Members in
`STARTUP` are not eligible to vote, as they are not yet a recognized member of any replica set.

**`STARTUP2`**

**Changed in version:** 5.0

Each data-bearing member of a replica set enters the
`STARTUP2` state as soon as `mongod` finishes
loading that member's configuration. 

The member then decides whether or not to undertake an initial sync.
If a member begins an initial sync, the member remains in
`STARTUP2` until all data is copied and all indexes are
built. Afterwards, the member transitions to `RECOVERING`.

Newly-added members in `STARTUP2` are not eligible to vote and 
cannot be elected during the initial sync process. Prior to MongoDB 5.0, 
members in `STARTUP2` were eligible to vote. 

**`RECOVERING`**

A member of a replica set enters `RECOVERING` state when
it is not ready to accept reads. The `RECOVERING` state
can occur during normal operation, and doesn't necessarily reflect
an error condition.  Members in the `RECOVERING` state
are eligible to vote in elections, but are not eligible to enter the
`PRIMARY` state.

A member transitions from `RECOVERING` to `SECONDARY`
after replicating enough data to guarantee a consistent view of the data for
client reads.  The only difference between `RECOVERING`
and `SECONDARY` states is that `RECOVERING`
prohibits client reads and `SECONDARY` permits them.
`SECONDARY` state does not guarantee anything about the
staleness of the data with respect to the primary.

Due to overload, a secondary may fall far enough behind the
other members of the replica set such that it may need to resync with the
rest of the set. When this happens, the member enters the
`RECOVERING` state and requires manual intervention.

**`ROLLBACK`**

Whenever the replica set replaces a primary in an
election, the old primary may contain documents
that did not replicate to the secondary
members. In this case, the old primary member reverts those writes. During
rollback, the member will have
`ROLLBACK` state. Members in the `ROLLBACK` state
are eligible to vote in elections.

Starting in version 4.2, MongoDB kills all in-progress user
operations when a member enters the `ROLLBACK` state.

### Error States

Members in any error state can't vote.

**`UNKNOWN`**

Members that have never communicated status information to the replica
set are in the `UNKNOWN` state.

**`DOWN`**

Members that lose their connection to the replica set are seen as `DOWN` by the remaining members of the set.

**`REMOVED`**

Members that are removed from the replica set enter the `REMOVED`
state.
When members enter the `REMOVED` state, the logs will
mark this event with a `replSet REMOVED` message entry.
