<!-- Converted from reference/command/compact.txt (reStructuredText). Includes are inlined. -->

# compact

## Definition

**`compact`**

Rewrites and defragments all data and indexes in a collection. On
WiredTiger databases, this command will release
unneeded disk space to the operating system.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
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

**Note:** Starting in MongoDB 4.2

MongoDB removes the MMAPv1 storage engine and the MMAPv1 specific
options `paddingFactor`, `paddingBytes`, `preservePadding`
for `compact`.

| Field | Type | Description |
|---|---|---|
| `compact` | string | The name of the collection. |
| `force` | flag | .. _compact-force-option: Optional. Starting in v4.4, if specified, forces `compact` to run on the primary in a replica set. Before v4.4, this boolean field enabled `compact` to run on the primary in a replica set if the value was `true` and returned an error when run on a primary if the value was `false`, because the command blocked all other operations. Starting in v4.4, `compact` does not block crud on the database it is compacting. |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

## `compact` Required Privileges

For clusters enforcing authentication,
you must authenticate as a user with the `compact` privilege
action on the target collection. The `dbAdmin` role provides 
the required privileges for running `compact` against
non-system collections. 

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

If you terminate `compact` with the `db.killOp()` method or restart the server before the operation  
finishes, `compact` ends and may fail its attempt to release 
disk space back to the operating system.

### Disk Space

The `compact` command attempts to reduce the disk space consumed for data and
indexes in a collection by releasing obsolete blocks back to the operating system.
The effectiveness of `compact` is relative to how many blocks are available to be 
released and where in the data file the blocks are. 

To see how the storage space changes for the collection, run the
`collStats` command before and after compaction. You can use the output 
metric `collStats.freeStorageSize` to view the amount of storage available 
for reuse. 

The operation is iterative and operates on segments of the data file in each pass. 
To view an estimate of how much space `compact` will release, use the `dryRun` 
flag. Calling `compact` on a collection will compact both the collection and its 
associated indexes. 

`compact` may require additional disk space to run.

### Replica Sets

You can use `compact` on collections and indexes that are stored in a
replica set, however there are some important considerations:

- The primary node does not replicate the `compact` command to the
  secondaries.
- You should run `compact` on secondary nodes whenever possible. If
  you cannot run `compact` on secondaries, see the force option.
- Starting in MongoDB 6.0.2 (and 5.0.12):

  - A secondary node can replicate while `compact` is running.
  - Reads are permitted.

To run `compact` on a cluster

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

#### Version Specific Considerations for Secondary Nodes

Blocking behavior on secondary nodes is version specific.

* - Version
  - Blocking Behavior

* - 4.4
  - - No replication is possible.
    - Reads are not permitted.

* - Post 4.4.17, 5.0.12, and 6.0.2
  - - A secondary node can replicate while `compact` is running.
    - Reads permitted.  

While the `compact` command is running, the replica set remains in a 
`SECONDARY` status.

For more information about replica set member states, see
See replica-set-member-states.

For replica set maintenance and availability, see
perform-maint-on-replica-set.

### Sharded Clusters

`compact` only applies to `mongod` instances. In a
sharded environment, run `compact` on each shard separately
as a maintenance operation.

You cannot issue `compact` against a `mongos` instance.

### Index Building

`mongod` rebuilds all indexes in parallel following the
`compact` operation.
