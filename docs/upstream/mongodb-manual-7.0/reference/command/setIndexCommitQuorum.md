<!-- Converted from reference/command/setIndexCommitQuorum.txt (reStructuredText). Includes are inlined. -->

# setIndexCommitQuorum (database command)

**`setIndexCommitQuorum`**

The `setIndexCommitQuorum` command sets minimum number of
data-bearing members that must be prepared to commit their local
index builds before the primary node will commit the index.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     setIndexCommitQuorum: <string>,
     indexNames: [ <document> ],
     commitQuorum: <int> | <string>,
     comment: <any>
   }     
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - setIndexCommitQuorum
  - `string`
  - .. _setIndexCommitQuorum-cmd-coll:

    The name of the collection for which the indexes are being 
    built.

* - indexNames
  - `array`
  - .. _setIndexCommitQuorum-cmd-indexNames:

    An array of in-progress index builds to modify. Each 
    element of the array must be the *name* of the index. 

    The indexes specified to `indexNames` must be the entire set
    of in-progress builds associated to a given index builder,
    i.e. the indexes built by a single `createIndexes`
    or `db.collection.createIndexes()` operation.

* - commitQuorum
  - `int` or `string`
  - .. _setIndexCommitQuorum-cmd-commitQuorum:

    The minimum number of data-bearing replica
    set members (i.e. commit quorum), including the primary, that
    must report a successful index build before the primary
    marks the `indexes` as ready.

    You can resume some
    interrupted index builds
    when the commit quorum is set to the default
    `"votingMembers"`.

    To update the commitQuorum, member replica set nodes must have
    `members[n].buildIndexes` set to `true`. If any voting
    nodes have `members[n].buildIndexes` 
    set to `false`, you can't use the default `"votingMembers"` commit 
    quorum. Either configure all nodes with `members[n].buildIndexes` 
    set to `true`, or select a different commit quorum. 

    Supports the following values:

    - `"votingMembers"` - all data-bearing voting replica set
      members (*Default*). A "voting" member is any replica set member 
      where `members[n].votes` is greater than `0`.

    - `"majority"` - a simple majority of data-bearing
      replica set members.

    - `<int>` - a specific number of data-bearing 
      replica set members. Specify an integer greater than 
      `0`.

    - A replica set tag name.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

## Behavior

**Note:** Requires `featureCompatibilityVersion` 4.4+

Each `mongod` in the replica set or sharded cluster
*must* have featureCompatibilityVersion set to at
least `4.4` to start index builds simultaneously across 
replica set members.

Index creation is a multistage process. 
The index creation process uses the `commit quorum` to minimize replication 
lag on secondary nodes.

When a secondary node receives a `commitIndexBuild` oplog entry, the 
node stops further oplog applications until the local index build can be
committed. Index builds can take anywhere from moments to days to
complete, so the replication lag can be significant if the secondary
node builds more slowly than the primary. 

To manage the replication lag, the commit quorum delays committing the
index build on the primary node until a minimum number of secondaries
are also ready to commit the index build. 

The commit quorum does not guarantee that indexes on secondaries are
ready for use when the command completes. To ensure that a specific
number of secondaries are ready for use, set an appropriate write
concern.

If a secondary node that is not included in the commit quorum receives
a `commitIndexBuild` oplog entry, the node may block replication until
its index build is complete.

Issuing `setIndexCommitQuorum` has no effect on index builds
started with commitQuorum of
`0`. 

**Important:**

Replica set nodes with buildIndexes 
set to `false` can't be included in a commit quorum.

### Commit Quorum Contrasted with Write Concern

There are important differences between commit quorums and write concerns:

- Index builds use **commit quorums**.
- Write operations use **write concerns**. 

Each data-bearing node in a cluster is a voting member.

The **commit quorum** specifies how many data-bearing voting members, or
which voting members, including the primary, must be prepared to commit
a simultaneous index build
before the primary will execute the commit.

The **write concern** is the level of acknowledgment that the write has
propagated to the specified number of instances.

The **commit quorum** specifies how many nodes must be *ready* to finish
the index build before the primary commits the index build. In contrast,
when the primary has committed the index build, the **write concern**
specifies how many nodes must *finish* the index build before the
command returns.

## Examples

Index builds on a replica set or sharded cluster build simultaneously across 
all data-bearing replica set members. For sharded clusters, the index build 
occurs only on shards containing data for the collection being indexed. 
The primary requires a minimum number of data-bearing `voting` members (i.e commit quorum), including itself,
that must complete the build before marking the index as ready for
use. See index-operations-replicated-build for more
information.

The following operation starts an index build of two indexes:

```javascript
db.getSiblingDB("examples").invoices.createIndexes(
  [
    { "invoices" : 1 },
    { "fulfillmentStatus" : 1 }
  ]
)
```

By default, index builds use `"votingMembers"` commit quorum, or all
data-bearing voting replica set members. The following operation
modifies the index build commit quorum to `"majority"`, or a 
simple majority of data-bearing voting members:. 

```javascript
db.getSiblingDB("examples").runCommand(
  {
    "setIndexCommitQuorum" : "invoices", 
    "indexNames" : ["invoices_1", "fullfillmentStatus_1"], 
    "commitQuorum" : "majority"
  }
)
```

- The indexes specified to `indexNames` must be the entire set
  of in-progress builds associated to a given index builder, 
  i.e. the `createIndexes()` operation. 

- The `indexNames` field specifies the *names* of the indexes. Since
  the indexes were created without an explicit name, MongoDB generated
  an index name by concatenating the names of the indexed fields and the
  sort order.
