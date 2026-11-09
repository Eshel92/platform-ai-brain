<!-- Converted from core/replica-set-secondary.txt (reStructuredText). Includes are inlined. -->

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
