<!-- Converted from reference/command/compact.txt (reStructuredText). Includes are inlined. -->

# compact (database command)

## Definition

**`compact`**

Rewrites and defragments all data and indexes in a collection. On
WiredTiger databases, this command
releases unneeded disk space to the operating system.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
   

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     compact: <collection name> 
   }
)
```

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `compact` | string | The name of the collection. |
| `force` | flag | .. _compact-force-option: Optional. If specified, forces `compact` to run on the primary in a replica set. `compact` does not block crud on the database it is compacting. |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

## `compact` Required Privileges

For clusters enforcing authentication,
you must authenticate as a user with the `compact` privilege
action on the target collection. The `dbAdmin` role provides 
the required privileges for running `compact` against
non-system collections. 

For system collections, you must: 

1. Create a custom role that grants the `compact` action on 
   the system collection.
2. Grant that role to a new or existing user. 
3. Authenticate as that user to perform the `compact` 
   command.

For example, the following operations create a custom role that grants
the `compact` action against the specified database and
collection:

```javascript
use admin
db.createRole(
  {
    role: "myCustomCompactRole",
    privileges: [
      {
        resource: { "db" : "<database>" , "collection" : "<collection>" },
        actions: [ "compact" ]
      }
    ],
    roles: []
  }
)
```

For more information on configuring the `resource` document, see 
resource-document.

To add the `dbAdmin` or the custom role to an existing
user, use `db.grantRolesToUser` or `db.updateUser()`.
The following operation grants the custom `compact` role to the 
`myCompactUser` on the `admin` database:

```javascript
use admin
db.grantRolesToUser("myCompactUser", [ "dbAdmin" | "myCustomCompactRole" ] )
```

To add the `dbAdmin` or the custom role to a new user,
specify the role to the `roles` array of the
`db.createUser()` method when creating the user.

```javascript
use admin
db.createUser(
  { 
     user: "myCompactUser",
     pwd: "myCompactUserPassword",
     roles: [
       { role: "dbAdmin", db: "<database>" } | "myCustomCompactRole"
     ]
   }
)
```

## Behavior

### Monitoring Progress

To check the `compact` operation's progress, monitor the
`mongod` log file or run `db.currentOp()`
from another shell instance.

### Operation Termination

If you restart the server before `compact` finishes, the operation terminates 
and may fail its attempt to release disk space back to the operating system.

### Disk Space

The `compact` command attempts to reduce disk space for data and
indexes in a collection by releasing obsolete blocks to the operating
system.
Effectiveness depends on how many blocks are available to release and
their location in the data file.

To see how the storage space changes for the collection, run the
`collStats` command before and after compaction. You can use the output 
metric `collStats.freeStorageSize` to view the amount of storage available for 
reuse. 

The operation is iterative and operates on segments of the data file in each pass. 
Calling `compact` on a collection compacts both the collection and its 
associated indexes. 

`compact` may require additional disk space to run.

### Backups

Compaction regularly checkpoints the database, which can lead to
synchronization overhead. On high-traffic databases, this can potentially
delay or prevent operational tasks such as taking backups. To avoid unexpected
disruptions, disable compaction before taking a backup.

#### Multi-Shard Transactions

**Note:**

If your deployment uses secondary reads and multi-shard transactions,
consider running an initial sync instead of 
`compact`.

When `compact` runs, WiredTiger temporarily adjusts its block-manager strategy 
to accommodate the compact workload. This adjustment can slow checkpoint 
operations and increase the time that a member takes to commit a transaction. 
Delayed transaction commits can cause significant read latency, replication lag, 
and operational queuing.

### Replica Sets

You can use `compact` on collections and indexes in a replica set;
however, consider the following:

- The primary node does not replicate the `compact` command to the
  secondaries.
- You should run `compact` on secondary nodes whenever possible. If
  you cannot run `compact` on secondaries, see the force option.
- Starting in MongoDB 6.1.0 (and 6.0.2):

  - A secondary node can replicate while `compact` is running.
  - Reads are permitted.

To run `compact` on a self-managed cluster:

**Step 1: Compact the secondary nodes.**

Run `compact` on one of the secondary nodes. When `compact`
finishes, repeat the operation on each of the remaining
secondaries in turn.

**Step 2: Reassign the primary node.**

To step down the current primary and trigger an election, use the
`rs.stepDown()` method. To nominate a particular secondary
node, adjust the member priority.

**Step 3: Compact the old primary.**

After stepping down, the old primary node becomes a secondary
node. Run `compact` on the old primary node.

#### Considerations for MongoDB Atlas Clusters

MongoDB Atlas does not support the `rs.stepDown()` method or
changes to member priority, so you cannot reassign the primary node as
you do in the self-managed `compact` procedure. Instead, on
MongoDB Atlas, run `compact` on each node. To run `compact` on the
current primary node, use the force
option. To learn about the performance impact of running `compact`
on a node that serves reads and writes, see
compact-multi-shard-transactions.

#### Version Specific Considerations for Secondary Nodes

- A secondary node can replicate while `compact` is running.

- Reads are permitted.  

While the `compact` command is running, the replica set remains in a 
`SECONDARY` status.

For more information about replica set member states, see
See replica-set-member-states.

For replica set maintenance and availability, see
perform-maint-on-replica-set.

### Index Size Differences Across Members

Each node applies writes to its indexes independently. Index storage
size can differ across the members of a replica set, even when the
members hold identical data. A primary node applies writes directly
from client operations. A secondary node applies the same writes from
the oplog, often in different batches and order. These write pattern
differences change how the storage engine packs and compresses index
pages. As a result, an index on one member can grow larger on disk
than the same index on another member.

To bring an affected index back in line with the same index on other
members, use one of the following remediation options:

- Run `compact` on the affected node.
- Perform an initial sync of the
  affected node.
- Drop and recreate the affected index.

When you plan storage capacity for a replica set, account for this
variation in index size across members.

### Sharded Clusters

`compact` only applies to `mongod` instances. In a
sharded environment, run `compact` on each shard separately
as a maintenance operation.

You cannot issue `compact` against a `mongos` instance.

### Index Building

`mongod` rebuilds all indexes in parallel following the
`compact` operation.

## Example

The following operation runs the `compact` command on the
`movies` collection:

```javascript
db.runCommand( { compact: "movies" } )
```

Running `compact` returns output similar to the following:

```javascript
{ bytesFreed: 27859, ok: 1 }
```
