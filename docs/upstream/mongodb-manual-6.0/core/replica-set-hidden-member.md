<!-- Converted from core/replica-set-hidden-member.txt (reStructuredText). Includes are inlined. -->

# Hidden Replica Set Members

A hidden member maintains a copy of the primary's
data set but is **invisible** to client applications. Hidden members
are good for workloads with different usage patterns from the other
members in the replica set. Hidden members must always be
priority 0 members and
so **cannot become primary**. The `db.hello()` method does not
display hidden members. Hidden members, however, **may vote** in
elections.

In the following five-member replica set, all four secondary members
have copies of the primary's data set, but one of the secondary members
is hidden.

(Figure: /images/replica-set-hidden-member.bakedsvg.svg)

## Behavior

### Read Operations

You can only read from a hidden member if you directly connect to the
node. If you connect to a cluster without directly connecting to the hidden 
node, you cannot run queries on the hidden node. As a result, these
members receive no traffic other than basic replication. Use hidden
members for dedicated tasks such as reporting and
backups.

**Important:**

If your replica set contains delayed members ensure that the delayed
members are hidden and non-voting. 

Hiding delayed replica set members prevents applications from seeing 
and querying delayed data without a direct connection to that member.
Making delayed replica set members non-voting means they will not 
count towards acknowledging write operations with write concern 
`"majority"`.

If you do not hide delayed members and one or more nodes 
become unavailable, the replica set has to wait for the delayed 
member and the commit point lags. A lagged commit point can lead to
performance issues.

For example, consider a Primary-Secondary-Delayed replica set
configuration where the delayed secondary is voting with a 10
minute delay.

With one non-delayed secondary unavailable, the degraded configuration
of Primary-Delayed must wait at least 10 minutes to acknowledge a write
operation with `"majority"`.The majority commit point 
will take longer to advance, leading to cache pressure similar 
performance issues with a
Primary with a Secondary and an Arbiter
(PSA) replica set.

For more information on the majority commit point, see 
Causal Consistency and Read and Write Concerns. For additional 
details on resolving performance issues see the
replica set maintenance tutorial.

In a sharded cluster, `mongos` do not interact with hidden
members.

### Voting

Hidden members *may* vote in replica set elections. If you stop a
voting hidden member, ensure that the set has an active majority or the
primary will step down. 

For the purposes of backups,

- .. include:: /includes/extracts/wt-fsync-lock-compatibility.rst

### Write Concern

Hidden replica set members can acknowledge write operations issued
with `w: <number> <`. For write operations
issued with `w : "majority"`, however,
hidden members must also be voting members (i.e. `members[n].votes`
greater than `0`) to acknowledge the `"majority"` write operation.
Non-voting replica set members (i.e. `members[n].votes` 
is `0`) cannot contribute to acknowledging write operations with 
`majority` write concern.

## Further Reading

For more information about backing up MongoDB databases,
see /core/backups. To configure a hidden member, see
/tutorial/configure-a-hidden-replica-set-member.
