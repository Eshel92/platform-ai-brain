<!-- Converted from reference/command/setIndexCommitQuorum.txt (reStructuredText). Includes are inlined. -->

# setIndexCommitQuorum

**`setIndexCommitQuorum`**

Changes the minimum number of data-bearing members (i.e commit
quorum), including the primary, that must complete an in-progress
simultaneous index build
before the primary marks those indexes as ready.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
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

    Starting in MongoDB v5.0, it's possible to resume some
    interrupted index builds
    when the commit quorum is set to `"votingMembers"`. 

    Replica set nodes in a commit quorum must have `members[n].buildIndexes` 
    set to `true`. If any voting nodes have `members[n].buildIndexes` 
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

Issuing `setIndexCommitQuorum` has no effect on index builds
started with commitQuorum of
`0`. 

**Important:**

Replica set nodes with buildIndexes 
set to `false` can't be included in a commit quorum.

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
