<!-- Converted from core/replica-set-sync.txt (reStructuredText). Includes are inlined. -->

# Replica Set Data Synchronization

In order to maintain up-to-date copies of the shared data set,
secondary members of a replica set sync or replicate data from
other members. MongoDB uses two forms of data synchronization:
initial sync to populate new members
with the full data set, and replication to apply ongoing changes to the
entire data set.

## Initial Sync

Initial sync copies all the data from one member of the replica set to
another member. See replica-set-initial-sync-source-selection for
more information on initial sync source selection criteria.

The `local` database stores the oplog data that the initial
sync process uses. Ensure the destination member has enough space in the
`local` database to store the oplog data for the initial sync process
to complete.

**Note:**

During the initial sync, MongoDB truncates the oplog on the destination 
member. This oplog truncation can impact processes, such as 
change streams, that depend on oplog data.

You can specify the preferred initial sync source using the 
`initialSyncSourceReadPreference` parameter. This parameter can 
only be specified when starting the `mongod`.

Starting in MongoDB 5.2, initial syncs can be *logical* or *file copy 
based*. 

### Logical Initial Sync Process

When you perform a logical initial sync, MongoDB:

#. Clones all databases except the local database. To clone, the
   `mongod` scans every collection in each source database and
   inserts all data into its own copies of these collections.

#. Builds all collection indexes as the documents are copied for each 
   collection.
   
#. Pulls newly added oplog records during the data copy. Ensure that the 
   target member has enough disk space in the `local` database to 
   temporarily store these oplog records for the duration of this data 
   copy stage.

#. Applies all changes to the data set. Using the oplog from the
   source, the `mongod` updates its data set to reflect the
   current state of the replica set.

When the initial sync finishes, the member transitions from
`STARTUP2` to `SECONDARY`.

To perform an initial sync, see
/tutorial/resync-replica-set-member.

### File Copy Based Initial Sync

*Available in MongoDB Enterprise only.*

File copy based initial sync runs the initial sync process by copying
and moving files on the file system. This sync method can be faster than
logical initial sync.

**Important:** File copy based initial sync may cause inaccurate counts

After file copy based initial sync completes, if you run the
`count()` method without a query predicate, the
count of documents returned may be inaccurate.

A `count` method without a query predicate looks like this:
`db.<collection>.count()`.

To learn more, see count-method-behavior-query-predicate.

#### Enable File Copy Based Initial Sync

To enable file copy based initial sync, set the
`initialSyncMethod` parameter to `fileCopyBased` on the
destination member for the initial sync. This parameter can only be set
at startup.

#### Behavior

File copy based initial sync replaces the `local` database of the
target member with the `local` database of the source member when 
syncing.

#### Limitations

- During a file copy based initial sync:

  - You cannot run a backup on the member that is being *synced to* or
    the member that is being *synced from*.

  - You cannot write to the `local` database on the member that is
    being *synced to*.

- You can only run an initial sync from one given member at a time. 

- When using the encrypted storage engine, MongoDB uses the source
  key to encrypt the destination.

### Initial Sync on NVMe Clusters

You must perform an initial sync on clusters that use the local
Non-Volatile Memory Express (NVMe) SSD storage option, including
if you're using Atlas auto-scaling. Atlas
NVMe clusters auto-scale to the next higher tier when 90% of the storage
space is full. An initial sync takes longer to complete compared to
subsequent syncs, and reduces the performance of the primary
from which the data is read.

### Fault Tolerance

If a secondary performing initial sync encounters a *non-transient*
(i.e. persistent) network error during the sync process, the secondary
restarts the initial sync process from the beginning. 

A secondary performing initial sync can attempt to resume the sync process if 
interrupted by a *transient* (i.e. temporary) network error, collection drop, or
collection rename.

By default, the secondary tries to resume initial sync for 24 hours.
You can use the `initialSyncTransientErrorRetryPeriodSeconds` server
parameter to control the amount of time the secondary attempts to
resume initial sync. If the secondary cannot successfully resume the
initial sync process during the configured time period, it selects a new
healthy source from the replica set and restarts the initial
synchronization process from the beginning. 

The secondary attempts to restart the initial sync up to `10` times
before returning a fatal error.

### Initial Sync Source Selection

Initial sync source selection depends on the value of the
`mongod` startup parameter
`initialSyncSourceReadPreference`:

- For `initialSyncSourceReadPreference` set to
  `primary` (default if `chaining` is disabled), select the primary
  as the sync source. If the primary is unavailable or unreachable, log
  an error and periodically check for primary availability.

- For `initialSyncSourceReadPreference` set to
  `primaryPreferred` (default for voting replica set
  members), attempt to select the primary as the sync source. If
  the primary is unavailable or unreachable, perform sync source
  selection from the remaining replica set members.

- For all other supported read modes, perform sync source selection 
  from the replica set members.

Members performing initial sync source selection make two passes through 
the list of all replica set members:

**firstpass:**

The member applies the following criteria to each replica 
set member when making the first pass for selecting a
initial sync source:

- The sync source *must* be in the `PRIMARY` or
  `SECONDARY` replication state.

- The sync source *must* be online and reachable.

- If `initialSyncSourceReadPreference` is
  `secondary` or `secondaryPreferred`, 
  the sync source *must* be a secondary.

- The sync source *must* be `visible`.

- The sync source *must* be within `30` seconds of the newest 
  oplog entry on the primary.

- If the member `builds indexes`, the sync source *must*
  build indexes.

- If the member `votes` in 
  replica set elections, the sync source *must* also vote.

- If the member is *not* a `delayed member`, the sync source *must not* be delayed.

- If the member *is* a `delayed member`, the sync source must have a shorter 
  configured delay.

- The sync source *must* be faster (i.e. lower latency) than 
  the current best sync source.

If no candidate sync sources remain after the first pass, 
the member performs a second pass with relaxed criteria. 
See Sync Source Selection (Second Pass).

**second pass:**

The member applies the following criteria to each replica 
set member when making the second pass for selecting a
initial sync source:

- The sync source *must* be in the 
  `PRIMARY` or `SECONDARY` replication 
  state.

- The sync source *must* be online and reachable.

- If `initialSyncSourceReadPreference` is
  `secondary`, the sync source *must* be a
  secondary.

- If the member `builds indexes`, the sync source must
  build indexes.

- The sync source *must* be faster (i.e. lower latency) than 
  the current best sync source.
       
If the member cannot select an initial sync source after two passes, it
logs an error and waits `1` second before restarting the selection
process. The secondary `mongod` can restart the initial
sync source selection process up to `10` times before exiting with an
error.

### Oplog Window

The oplog window must be long enough so that a secondary can fetch any
new oplog entries that occur between the start and end of 
the replica-set-initial-sync-logical.
If the window isn't long enough, there is a risk that some entries may 
fall off the `oplog` before the secondary can apply them.

It is recommended that you size the `oplog` for additional time to fetch any
new `oplog` entries.  This allows for changes that may occur during initial
syncs.

For more information, see replica-set-oplog-sizing.

## Replication

Secondary members replicate data continuously after the initial sync.
Secondary members copy the oplog from
their *sync from* source and apply these operations in an asynchronous
process. [#slow-oplogs]_ 

Secondaries may automatically change their *sync from* source as needed
based on changes in the ping time and state of other members'
replication. See replica-set-replication-sync-source-selection
for more information on sync source selection criteria.

### Streaming Replication

*Sync from* sources send a continuous stream 
of oplog entries to their syncing 
secondaries. Streaming replication mitigates replication lag in 
high-load and high-latency networks. It also: 

- Reduces staleness for reads from secondaries.
- Reduces risk of losing write operations with w: 1 due to 
  primary failover.
- Reduces latency on write operations with `w: "majority"` and w: >1 (that is, any write concern that 
  requires waiting for replication).

Use the `oplogFetcherUsesExhaust` startup parameter to disable 
streaming replication and using the older replication behavior. 
Set the `oplogFetcherUsesExhaust` parameter to `false` only if 
there are any resource constraints on the *sync from* source or if you wish 
to limit MongoDB's usage of network bandwidth for replication.

### Multithreaded Replication

MongoDB applies write operations in batches using multiple threads to
improve concurrency. MongoDB groups batches by document ID (WiredTiger) and simultaneously applies each group of
operations using a different thread. MongoDB always applies write
operations to a given document in their original write order.

Read operations that
target secondaries and are
configured with a read concern level of
`"local"` or  `"majority"` read from
a WiredTiger snapshot of the data if the read
takes place on a secondary where replication batches are being applied. 

Reading from a snapshot guarantees a consistent view of the
data, and allows the read to occur simultaneously with the ongoing
replication without the need for a lock. As a result, secondary reads
requiring these read concern levels no longer need to wait for
replication batches to be applied, and can be handled as they are
received.

### Flow Control

Starting in MongoDB 4.2, administrators can limit the rate at which
the primary applies its writes with the goal of keeping the `majority
committed` lag under
a configurable maximum value `flowControlTargetLagSeconds`.

By default, flow control is `enabled`.

For more information, see flow-control.

### Replication Sync Source Selection

Replication sync source selection depends on the replica set 
`chaining` setting:

- With chaining enabled (default), perform sync source selection from
  the replica set members.

- With chaining disabled, select the primary as the sync 
  source. If the primary is unavailable or unreachable, log an 
  error and periodically check for primary availability.

Members performing replication sync source selection make two passes
through the list of all replica set members:

**firstpass:**

The member applies the following criteria to each replica 
set member when making the first pass for selecting a
replication sync source:

- The sync source *must* be in the `PRIMARY` or
  `SECONDARY` replication state.

- The sync source *must* be online and reachable.

- The sync source *must* have newer oplog entries than the member
  (i.e. the sync source is *ahead* of the member).

- The sync source *must* be `visible`.

- The sync source *must* be within `30` seconds of the newest 
  oplog entry on the primary.

- If the member `builds indexes`, the sync source *must*
  build indexes.

- If the member `votes` in 
  replica set elections, the sync source *must* also vote.

- If the member is *not* a `delayed member`, the sync source *must not* be delayed.

- If the member *is* a `delayed member`, the sync source must have a shorter 
  configured delay.

- The sync source *must* be faster (i.e. lower latency) than 
  the current best sync source.

If no candidate sync sources remain after the first pass, 
the member performs a second pass with relaxed criteria. 
See the Sync Source Selection (Second Pass).

**second pass:**

The member applies the following criteria to each replica 
set member when making the second pass for selecting a
replication sync source:

- The sync source *must* be in the 
  `PRIMARY` or `SECONDARY` replication 
  state.

- The sync source *must* be online and reachable.

- If the member `builds indexes`, the sync source must
  build indexes.

- The sync source *must* be faster (i.e. lower latency) than 
  the current best sync source.

If the member cannot select a sync source after two passes, it logs an
error and waits `1` second before restarting the selection process.

The number of times a source can be changed per hour is
configurable by setting the `maxNumSyncSourceChangesPerHour`
parameter. 

**Note:**

The startup parameter `initialSyncSourceReadPreference` takes 
precedence over the replica set's `settings.chainingAllowed` setting 
when selecting an initial sync source. After a replica set member
successfully performs initial sync, it defers to the value of
`chainingAllowed` when selecting a replication sync
source.

See replica-set-initial-sync-source-selection for more
information on initial sync source selection.
