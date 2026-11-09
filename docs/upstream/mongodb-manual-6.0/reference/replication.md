<!-- Converted from reference/replication.txt (reStructuredText). Includes are inlined. -->

# Self-Managed Replication Reference

## Replication Methods in `mongosh`

| Name | Description |
|---|---|
| `rs.add()` | Adds a member to a replica set. |
| `rs.addArb()` | Adds an arbiter to a replica set. |
| `rs.conf()` | Returns the replica set configuration document. |
| `rs.freeze()` | Prevents the current member from seeking election as primary for a period of time. |
| `rs.help()` | Returns basic help text for replica set functions. |
| `rs.initiate()` | Initializes a new replica set. |
| `rs.printReplicationInfo()` | Prints a formatted report of the replica set status from the perspective of the primary. |
| `rs.printSecondaryReplicationInfo()` | Prints a formatted report of the replica set status from the perspective of the secondaries. |
| `rs.reconfig()` | Re-configures a replica set by applying a new replica set configuration object. |
| `rs.remove()` | Remove a member from a replica set. |
| `rs.status()` | Returns a document with information about the state of the replica set. |
| `rs.stepDown()` | Causes the current primary to become a secondary which forces an election. |
| `rs.syncFrom()` | Sets the member that this replica set member will sync from, overriding the default sync target selection logic. |

## Replication Database Commands

| Name | Description |
|---|---|
| `applyOps` | Internal command that applies oplog entries to the current data set. |
| `hello` | Displays information about this member's role in the replica set, including whether it is the primary. |
| `replSetAbortPrimaryCatchUp` | Forces the elected primary to abort sync (catch up) then complete the transition to primary. |
| `replSetFreeze` | Prevents the current member from seeking election as primary for a period of time. |
| `replSetGetConfig` | Returns the replica set's configuration object. |
| `replSetGetStatus` | Returns a document that reports on the status of the replica set. |
| `replSetInitiate` | Initializes a new replica set. |
| `replSetMaintenance` | Enables or disables a maintenance mode, which puts a secondary node in a `RECOVERING` state. |
| `replSetReconfig` | Applies a new configuration to an existing replica set. |
| `replSetResizeOplog` | Dynamically resizes the oplog for a replica set member.  Available for WiredTiger storage engine only. |
| `replSetStepDown` | Forces the current primary to *step down* and become a secondary, forcing an election. |
| `replSetSyncFrom` | Explicitly override the default logic for selecting a member to replicate from. |

## Replica Set Reference Documentation

/reference/replica-configuration
   Complete documentation of the replica set configuration
   object returned by `rs.conf()`.

/reference/replica-set-protocol-versions
   Reference on the replica set protocol version.

/tutorial/troubleshoot-replica-sets
   Replica set trouble shooting guide.

/reference/local-database
   Complete documentation of the content of the `local` database
   that `mongod` instances use to support replication.

/reference/replica-states
   Reference for the replica set member states.
