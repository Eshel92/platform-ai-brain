<!-- Converted from core/replica-set-primary.txt (reStructuredText). Includes are inlined. -->

:orphan:

# Replica Set Primary

The primary is the only member in the replica set that receives write
operations. MongoDB applies write operations on the primary and
then records the operations on the primary's oplog. Secondary members replicate this log and apply
the operations to their data sets.

In the following three-member replica set, the primary accepts all
write operations. Then the secondaries replicate the oplog to apply to
their data sets.

(Figure: /images/replica-set-read-write-operations-primary.bakedsvg.svg)

All members of the replica set can accept read operations. However, by
default, an application directs its read operations to the primary
member. See /core/read-preference for details on changing the
default read behavior.

The replica set can have at most one primary.
[#edge-cases-2-primaries]_ If the current primary becomes unavailable,
an election determines the new primary. See
/core/replica-set-elections for more details.

In the following 3-member replica set, the primary becomes unavailable.
This triggers an election which selects one of the remaining
secondaries as the new primary.

(Figure: /images/replica-set-trigger-election.bakedsvg.svg)
