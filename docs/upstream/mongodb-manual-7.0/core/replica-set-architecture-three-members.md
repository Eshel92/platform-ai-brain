<!-- Converted from core/replica-set-architecture-three-members.txt (reStructuredText). Includes are inlined. -->

# Three Member Replica Sets

The minimum number of replica set members needed to obtain the benefits
of a replica set is three members. A three member replica set can have
either three data-bearing members (Primary-Secondary-Secondary)
(*Recommended*) or if circumstances (such as cost) prohibit adding a
third data bearing member, two data-bearing members and an arbiter
(Primary-Secondary-Arbiter). [#arbiter-considerations]_

## Primary with Two Secondary Members (P-S-S)

A replica set with three members that store data has:

- One primary.

- Two secondary members. Both
  secondaries can become the primary in an election.

(Figure: /images/replica-set-primary-with-two-secondaries.bakedsvg.svg)

These deployments provide two complete copies of the data set at all
times in addition to the primary. These replica sets provide
additional fault tolerance and high availability. If the primary is unavailable, the replica
set elects a secondary to be primary and continues normal
operation. The old primary rejoins the set when available.

(Figure: /images/replica-set-trigger-election.bakedsvg.svg)

## Primary with a Secondary and an Arbiter (PSA)

**Note:**

For considerations when using an arbiter, see
/core/replica-set-arbiter.

   

A three member replica set with a two members that store data has:

- One primary.

- One secondary member. The
  secondary can become primary in an election.

- One arbiter. The arbiter only
  votes in elections.

(Figure: /images/replica-set-primary-with-secondary-and-arbiter.bakedsvg.svg)

Since the arbiter does not hold a copy of the data, these deployments
provides only one complete copy of the data. Arbiters require fewer
resources, but at the expense of more limited redundancy and fault
tolerance.

However, a deployment with a primary, secondary, and an arbiter
ensures that a replica set remains available if the primary *or* the
secondary is unavailable. If the primary is unavailable, the replica
set will elect the secondary to be primary.

(Figure: /images/replica-set-w-arbiter-trigger-election.bakedsvg.svg)

**See also:**

/tutorial/deploy-replica-set
