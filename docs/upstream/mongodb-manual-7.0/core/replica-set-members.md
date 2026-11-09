<!-- Converted from core/replica-set-members.txt (reStructuredText). Includes are inlined. -->

# Replica Set Members

A *replica set* in MongoDB is a group of `mongod` processes
that provide redundancy and high availability. The members of a
replica set are:

replica-set-primary-member
   The primary receives all write operations.

replica-set-secondary-members
   Secondaries replicate operations from the primary to maintain an
   identical data set. Secondaries may have additional configurations
   for special usage profiles. For example, secondaries may be
   non-voting or
   priority 0.

The minimum recommended configuration for a replica set is a three
member replica set with three data-bearing members: one primary and two secondary members. In some circumstances (such
as you have a primary and a secondary but cost constraints prohibit
adding another secondary), you may choose to include an arbiter. An arbiter participates in elections but does not hold data (i.e. does not provide
data redundancy).

A replica set can have up to 50 members but only 7 voting members.

**See also:**

- `replSetGetStatus.votingMembersCount`

- `replSetGetStatus.writableVotingMembersCount`

## Primary

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

## Secondaries

# Replica Set Secondary Members

A secondary maintains a copy of the primary's data
set. To replicate data, a secondary applies operations from the
primary's oplog to its own data set
in an asynchronous process. [#slow-oplogs]_ A replica set can have one or more
secondaries.

The following three-member replica set has two secondary
members. The secondaries replicate the primary's oplog and apply
the operations to their data sets.

(Figure: /images/replica-set-primary-with-two-secondaries.bakedsvg.svg)

Although clients cannot write data to secondaries, clients can read
data from secondary members. See /core/read-preference for more
information on how clients direct read operations to replica sets.

A secondary can become a primary.
If the current primary becomes unavailable, the replica set
holds an election to choose which of the secondaries
becomes the new primary.

In the following three-member replica set, the primary becomes unavailable.
This triggers an election where one of the remaining
secondaries becomes the new primary.

(Figure: /images/replica-set-trigger-election.bakedsvg.svg)

See
/core/replica-set-elections for more details.

You can configure a secondary member for a specific purpose. You can
configure a secondary to:

- Prevent it from becoming a primary in an election, which allows it to
  reside in a secondary data center or to serve as a cold standby. See
  /core/replica-set-priority-0-member.

- Prevent applications from reading from it, which allows it to run applications
  that require separation from normal traffic. See
  /core/replica-set-hidden-member.

- Keep a running "historical" snapshot for use in recovery from
  certain errors, such as unintentionally deleted databases. See
  /core/replica-set-delayed-member.

# Replica Set Secondary Members

A secondary maintains a copy of the primary's data
set. To replicate data, a secondary applies operations from the
primary's oplog to its own data set
in an asynchronous process. [#slow-oplogs]_ A replica set can have one or more
secondaries.

The following three-member replica set has two secondary
members. The secondaries replicate the primary's oplog and apply
the operations to their data sets.

(Figure: /images/replica-set-primary-with-two-secondaries.bakedsvg.svg)

Although clients cannot write data to secondaries, clients can read
data from secondary members. See /core/read-preference for more
information on how clients direct read operations to replica sets.

A secondary can become a primary.
If the current primary becomes unavailable, the replica set
holds an election to choose which of the secondaries
becomes the new primary.

In the following three-member replica set, the primary becomes unavailable.
This triggers an election where one of the remaining
secondaries becomes the new primary.

(Figure: /images/replica-set-trigger-election.bakedsvg.svg)

See
/core/replica-set-elections for more details.

You can configure a secondary member for a specific purpose. You can
configure a secondary to:

- Prevent it from becoming a primary in an election, which allows it to
  reside in a secondary data center or to serve as a cold standby. See
  /core/replica-set-priority-0-member.

- Prevent applications from reading from it, which allows it to run applications
  that require separation from normal traffic. See
  /core/replica-set-hidden-member.

- Keep a running "historical" snapshot for use in recovery from
  certain errors, such as unintentionally deleted databases. See
  /core/replica-set-delayed-member.

## Arbiter

# Replica Set Arbiter

In some circumstances (such as when you have a primary and a secondary,
but cost constraints prohibit adding another secondary), you may choose
to add an arbiter to your replica set. An arbiter participates in
elections for primary but an arbiter does
**not** have a copy of the data set and **cannot** become a primary.

An arbiter has exactly `1` election vote. By default an arbiter has
priority `0`.

**Important:**

Do not run an arbiter on systems that also host the primary or the
secondary members of the replica set.

**Warning:**

Using a primary-secondary-arbiter (PSA)
architecture for shards in a sharded cluster can cause a loss of
availability if a data-bearing secondary is unavailable. A PSA
cluster differs from a typical replica set: In a sharded cluster,
shards perform `w: majority` write concern operations that cannot complete if the remaining
cluster members required to confirm an operation have an arbiter.

To add an arbiter, see /tutorial/add-replica-set-arbiter.

## Release Version Considerations

Arbiters are not supported with
quarterly rapid releases. If
your deployment includes arbiters, only use
LTS (Long Term Support) releases.

## Performance Issues with PSA replica sets

If you are using a three-member primary-secondary-arbiter (PSA) 
architecture, consider the following:

- The write concern `"majority"` can cause
  performance issues if a secondary is unavailable or lagging. For 
  advice on how to mitigate these issues, see 
  performance-issues-psa.

- If you are using a global default `"majority"` 
  and the write concern is less than the size of the majority,
  your queries may return stale (not fully replicated) data.

## Shard Keys, Transactions, and Arbiters

You cannot change a shard key using a transaction
if the replica set has an arbiter. Arbiters cannot participate in the
data operations required for multi-shard transactions.

Transactions whose write operations span multiple shards will error
and abort if any transaction operation reads from or writes to a
shard that contains an arbiter.

## Concerns with Multiple Arbiters

Use a single arbiter to avoid problems with data consistency. Multiple
arbiters prevent the reliable use of the majority write concern.

To ensure that a write will persist after the failure of a primary node,
the majority write concern requires a majority of nodes to acknowledge
a write operation. Arbiters do not store any data, but they do
contribute to the number of nodes in a replica set. When a replica set
has multiple arbiters it is less likely that a majority of data bearing
nodes will be available after a node failure.

**Warning:**

If a secondary node falls behind the primary, and the cluster is
`reconfigured`, votes from multiple arbiters
can elect the node that had fallen behind. The new primary will not
have the unreplicated writes even though the writes could have been
majority committed by the old configuration. The result is data
loss.

To avoid this scenario, use at most a single arbiter.

**New in version:** 5.3

Starting in MongoDB 5.3, support for multiple arbiters in a replica set is
disabled by default. If you attempt to add multiple arbiters to a
replica set, the server returns an error:

```text
MongoServerError: Multiple arbiters are not allowed unless all nodes
were started with --setParameter 'allowMultipleArbiters=true'
```

To add multiple arbiters to a replica set using MongoDB 5.3 or later, start
each node with the `allowMultipleArbiters` parameter set to `true`:

```bash
mongod --setParameter allowMultipleArbiters=true
```

## Security

### Authentication

When running with `authorization`, arbiters exchange credentials with
other members of the set to authenticate. MongoDB encrypts the
authentication process, and the MongoDB authentication exchange is
cryptographically secure.

Because arbiters do not store data, they do not possess the internal table of user and role mappings
used for authentication.  Thus, the only way to log on to an arbiter with authorization active is to
use the localhost exception.

### Communication

The only communication between arbiters and other set members are:
votes during elections, heartbeats, and configuration data. These
exchanges are not encrypted.

**However**, if your MongoDB deployment uses TLS/SSL, MongoDB will encrypt
*all* communication between replica set members. See
/tutorial/configure-ssl for more information.

As with all MongoDB components, run arbiters in trusted network
environments.

## Example

For example, in the following replica set with 2 data-bearing members
(the primary and a secondary), an arbiter allows the set to have an odd
number of votes to break a tie:

(Figure: /images/replica-set-primary-with-secondary-and-arbiter.bakedsvg.svg)

For considerations when using an arbiter, see /core/replica-set-arbiter.
