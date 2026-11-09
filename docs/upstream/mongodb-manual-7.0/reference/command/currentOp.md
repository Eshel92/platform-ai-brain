<!-- Converted from reference/command/currentOp.txt (reStructuredText). Includes are inlined. -->

# currentOp (database command)

## Definition

**`currentOp`**

**Deprecated since version:** 6.2

In versions 6.2 and later use the `$currentOp` aggregation 
stage.

Returns a document that contains information on in-progress
operations for the `mongod` instance. 

The `currentOp` database command is deprecated 
since version 6.2. Use the `$currentOp` aggregation 
stage instead of the `currentOp` command and its 
`mongosh` helper method `db.currentOp()`.

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
db.adminCommand(
   { 
     currentOp: 1 
   }
)
```

**Note:**

Starting in MongoDB 5.0, the `$currentOp` aggregation 
stage is used when running the helper method `db.currentOp()` 
with `mongosh`.

Given this, in the 5.0 version of the shell and with mongosh,
`db.currentOp()` result sets are not subject to the
16MB BSON document return size 
document return size limit for documents of the previous legacy 
`mongo` versions.

## Behavior

`currentOp` must run against the `admin` database, and
it can accept several optional fields.

| Field | Description |
|---|---|
| `"$ownOps"` | Boolean. If set to `true`, returns information on the current user's operations only. On `mongod` instances, users are always authorized to run `currentOp` with `"$ownOps": true` to view their own operations. See access control. |
| `"$all"` | Boolean. If set to `true`, returns information on all operations, including operations on idle connections and system operations. `"$all": true` overrides any output field filters. |
| <filter> | Specify filter conditions on the currentOp-output-fields. See currentOp-examples. |
| `comment` | .. include:: /includes/extracts/comment-content.rst |

       
`currentOp` and the database profiler report
the same basic diagnostic information for CRUD operations, including
the following:
 
- `aggregate`
- `count`
- `delete`
- `distinct`
- `find` (OP_QUERY and
  `command`)
- `findAndModify`
- `getMore` (OP_GET_MORE and
  `command`)
- `insert`
- `mapReduce`
- `update`

These operations are also included in the logging of
slow queries. See `slowOpThresholdMs` for
more information about slow query logging.

### Redaction

When using Queryable Encryption,
`currentOp` operations with the `encryptionInformation` option
redact certain information:

* The output omits all fields after `"command"`.
* The output redacts `"command"` to include only the first element,
  `$comment`, and `$db`.

## Access Control

On systems running with `authorization`, the user
must have access that includes the `inprog` privilege
action.

Users can use
`$ownOps` on `mongod` instances to view their own
operations without the `inprog` privilege action.

```javascript
db.adminCommand( { currentOp: 1, "$ownOps": 1 } )
```

**See also:**

create-role-to-manage-ops

## Examples

The following examples use the `currentOp` command with
various query documents to filter the output.

### Display All Current Operations

```javascript
db.adminCommand(
   {
     currentOp: true,
     "$all": true
   }
)
```

### Write Operations Waiting for a Lock

The following example returns information on all write operations that
are waiting for a lock:

```javascript
db.adminCommand(
   {
     currentOp: true,
     "waitingForLock" : true,
     $or: [
        { "op" : { "$in" : [ "insert", "update", "remove" ] } },
        { "command.findandmodify": { $exists: true } }
    ]  
   }
)
```

### Active Operations with no Yields

The following example returns information on all active running
operations that have never yielded:

```javascript
db.adminCommand(
   {
     currentOp: true,
     "active" : true,
     "numYields" : 0,
     "waitingForLock" : false
   }
)
```

### Active Operations on a Specific Database

The following example returns information on all active operations for
database `db1` that have been running longer than 3 seconds:

```javascript
db.adminCommand(
   {
     currentOp: true,
     "active" : true,
     "secs_running" : { "$gt" : 3 },
     "ns" : /^db1\./
   }
)
```

### Active Indexing Operations

The following example returns information on index creation operations:

```javascript
db.getSiblingDB("admin").aggregate( [
   { $currentOp : { idleConnections: true } },
   { $match: {
         $or: [
            { "op": "command", "command.createIndexes": { $exists: true } },
            { "op": "none", "msg": /^Index Build/ }
         ]
     }
   }
] )
```

MongoDB marks index builds waiting on commit quorum to complete the operation as an 
idle connection by setting the `active` field to `false`. The `idleConnections: true`
setting includes these idle connections in the `$currentOp` output. 

## Output Example

tabs:

   - id: standalone
     name: Standalone
     content: |

         The following is a prototype of the `currentOp`
         output when run on a standalone:

         ```javascript
         {
           "inprog": [
                {
                  "type" : <string>,
                  "host" : <string>,
                  "desc" : <string>,
                  "connectionId" : <number>,
                  "client" : <string>,
                  "appName" : <string>,
                  "clientMetadata" : <document>,
                  "active" : <boolean>,
                  "currentOpTime" : <string>,
                  "effectiveUsers" : [
                     {
                        "user" : <string>,
                        "db" : <string>
                     }
                  ],
                  "opid" : <number>,
                  "lsid" : {
                     "id" : <UUID>,
                     "uid" : <BinData>
                  },
                  "secs_running" : <Long()>,
                  "microsecs_running" : <number>,
                  "op" : <string>,
                  "ns" : <string>,
                  "command" : <document>,
                  "queryFramework" : <string>,
                  "planSummary": <string>,
                  "cursor" : {                              // only for getMore operations
                     "cursorId" : <Long()>,
                     "createdDate" : <ISODate()>,
                     "lastAccessDate" : <ISODate()>,
                     "nDocsReturned" : <Long()>,
                     "nBatchesReturned" : <Long()>,
                     "noCursorTimeout" : <boolean>,
                     "tailable" : <boolean>,
                     "awaitData" : <boolean>,
                     "originatingCommand" : <document>,
                     "planSummary" : <string>,
                     "operationUsingCursorId" : <Long()>
                  },
                  "msg": <string>,
                  "progress" : {
                      "done" : <number>,
                      "total" : <number>
                  },
                  "killPending" : <boolean>,
                  "numYields" : <number>,
                  "dataThroughputLastSecond" : <number>, 
                  "dataThroughputAverage" : <number>, 
                  "waitingForLatch" : { 
                      "timestamp" : <ISODate()>,
                      "captureName" : <string>
                  },
                  "locks" : {
                      "ParallelBatchWriterMode" : <string>,
                      "ReplicationStateTransition" : <string>,
                      "Global" : <string>,
                      "Database" : <string>,
                      "Collection" : <string>,
                      "Metadata" : <string>,
                      "oplog" : <string>
                  },
                  "waitingForLock" : <boolean>,
                  "lockStats" : {
                      "ParallelBatchWriterMode" : {
                         "acquireCount": {
                            "r": <NumberLong>,
                            "w": <NumberLong>,
                            "R": <NumberLong>,
                            "W": <NumberLong>
                         },
                         "acquireWaitCount": {
                            "r": <NumberLong>,
                            "w": <NumberLong>,
                            "R": <NumberLong>,
                            "W": <NumberLong>
                         },
                         "timeAcquiringMicros" : {
                            "r" : Long(0),
                            "w" : Long(0),
                            "R" : Long(0),
                            "W" : Long(0)
                         },
                         "deadlockCount" : {
                            "r" : Long(0),
                            "w" : Long(0),
                            "R" : Long(0),
                            "W" : Long(0)
                         }
                      },
                      "ReplicationStateTransition" : {
                         ...
                      },
                      "Global": {
                         ...
                      },
                      "Database" : {
                         ...
                      },
                      ...
                  }
                },
                ...
            ],
            "fsyncLock": <boolean>,
            "info": <string>,
             "ok": <num>
         }
         ```

   - id: repl
     name: Replica Set (Primary)
     content: |

         The following is a prototype of the `currentOp`
         output when run on a primary of a replica set:

         ```javascript
         {
           "inprog": [
                {
                  "type" : <string>,
                  "host" : <string>,
                  "desc" : <string>,
                  "connectionId" : <number>,
                  "client" : <string>,
                  "appName" : <string>,
                  "clientMetadata" : <document>,
                  "lsid" : {
                     "id" : <UUID>,
                     "uid" : <BinData>
                  },
                  "transaction" : {
                     "parameters" : {
                        "txnNumber" : <Long()>,
                        "autocommit" : <boolean>,
                        "readConcern" : {
                           "level" : <string>
                        }
                     },
                     "readTimestamp" : <Timestamp>,
                     "startWallClockTime" : <string>,
                     "timeOpenMicros" : <Long()>,
                     "timeActiveMicros" : <Long()>,
                     "timeInactiveMicros" : <Long()>,
                     "expiryTime" : <string>,
                  },
                  "active" : <boolean>,
                  "currentOpTime" : <string>,
                  "effectiveUsers" : [
                     {
                        "user" : <string>,
                        "db" : <string>
                     }
                  ],
                  "opid" : <number>,
                  "secs_running" : <Long()>,
                  "microsecs_running" : <number>,
                  "op" : <string>,
                  "ns" : <string>,
                  "command" : <document>,
                  "originatingCommand" : <document>,
                  "queryFramework" : <string>,
                  "planSummary": <string>,
                  "prepareReadConflicts" : <Long()>,
                  "writeConflicts" : <Long()>,
                  "cursor" : {                              // only for getMore operations
                     "cursorId" : <Long()>,
                     "createdDate" : <ISODate()>,
                     "lastAccessDate" : <ISODate()>,
                     "nDocsReturned" : <Long()>,
                     "nBatchesReturned" : <Long()>,
                     "noCursorTimeout" : <boolean>,
                     "tailable" : <boolean>,
                     "awaitData" : <boolean>,
                     "originatingCommand" : <document>,
                     "planSummary" : <string>,
                     "operationUsingCursorId" : <Long()>
                  },
                  "msg": <string>,
                  "progress" : {
                      "done" : <number>,
                      "total" : <number>
                  },
                  "killPending" : <boolean>,
                  "numYields" : <number>,
                  "dataThroughputLastSecond" : <number>, 
                  "dataThroughputAverage" : <number>, 
                  "waitingForLatch" : {
                       "timestamp" : <ISODate()>,
                       "captureName" : <string>
                   },
                  "locks" : {
                      "ParallelBatchWriterMode" : <string>,
                      "ReplicationStateTransition" : <string>,
                      "Global" : <string>,
                      "Database" : <string>,
                      "Collection" : <string>,
                      "Metadata" : <string>,
                      "oplog" : <string>
                  },
                  "waitingForLock" : <boolean>,
                  "lockStats" : {
                      "ParallelBatchWriterMode" : {
                         "acquireCount": {
                            "r": <NumberLong>,
                            "w": <NumberLong>,
                            "R": <NumberLong>,
                            "W": <NumberLong>
                         },
                         "acquireWaitCount": {
                            "r": <NumberLong>,
                            "w": <NumberLong>,
                            "R": <NumberLong>,
                            "W": <NumberLong>
                         },
                         "timeAcquiringMicros" : {
                            "r" : Long(0),
                            "w" : Long(0),
                            "R" : Long(0),
                            "W" : Long(0)
                         },
                         "deadlockCount" : {
                            "r" : Long(0),
                            "w" : Long(0),
                            "R" : Long(0),
                            "W" : Long(0)
                         }
                      },
                      "ReplicationStateTransition" : { 
                         ...
                      },
                      "Global" : {
                         ...
                      },
                      "Database" : {
                         ...
                      },
                      ...
                  }
                },
                ...
            ],
            "fsyncLock": <boolean>,
            "info": <string>,
            "ok": <num>,
            "operationTime": <timestamp>,
            "$clusterTime": <document>
         }
         ```

   - id: shardedcluster
     name: Sharded Cluster (mongos)
     content: |

         The following is an example of the `currentOp`
         output when run on a `mongos` of a sharded
         cluster (Fields may vary depending on the operation being
         reported):

         ```javascript
         {
           "inprog": [
                {
                  "shard": <string>,
                  "type" : <string>,
                  "host" : <string>,
                  "desc" : <string>,
                  "connectionId" : <number>,
                  "client_s" : <string>,
                  "appName" : <string>,
                  "clientMetadata" : <document>,
                  "lsid" : {
                     "id" : <UUID>,
                     "uid" : <BinData>
                  },
                  "transaction" : {
                     "parameters" : {
                        "txnNumber" : <Long()>,
                        "autocommit" : <boolean>,
                        "readConcern" : {
                           "level" : <string>
                        }
                     },
                     "readTimestamp" : <Timestamp>,
                     "startWallClockTime" : <string>,
                     "timeOpenMicros" : <Long()>,
                     "timeActiveMicros" : <Long()>,
                     "timeInactiveMicros" : <Long()>,
                     "expiryTime" : <string>,
                  },
                  "active" : <boolean>,
                  "currentOpTime" : <string>,
                  "effectiveUsers" : [
                     {
                        "user" : <string>,
                        "db" : <string>
                     }
                  ],
                  "runBy" : [
                     {
                        "user" : <string>,
                        "db" : <string>
                     }
                  ],
                  "twoPhaseCommitCoordinator" : {
                     "lsid" : {
                        "id" : <UUID>,
                        "uid" : <BinData>
                     },
                     "txnNumber" : <NumberLong>,
                     "numParticipants" : <NumberLong>,
                     "state" : <string>,
                     "commitStartTime" : <ISODate>,
                     "hasRecoveredFromFailover" : <boolean>,
                     "stepDurations" : <document>,
                     "decision" : <document>,
                     "deadline" : <ISODate>
                  }
                  "opid" : <string>,
                  "secs_running" : <Long()>,
                  "microsecs_running" : <number>,
                  "op" : <string>,
                  "ns" : <string>,
                  "command" : <document>,
                  "configTime" : <Timestamp>,           // Starting in 5.0
                  "topologyTime" : <Timestamp>,           // Starting in 5.0
                  "queryFramework" : <string>,            // Starting in 6.2       
                  "planSummary": <string>,
                  "prepareReadConflicts" : <Long()>,
                  "writeConflicts" : <Long()>,
                  "cursor" : {                              // only for getMore operations
                     "cursorId" : <Long()>,
                     "createdDate" : <ISODate()>,
                     "lastAccessDate" : <ISODate()>,
                     "nDocsReturned" : <Long()>,
                     "nBatchesReturned" : <Long()>,
                     "noCursorTimeout" : <boolean>,
                     "tailable" : <boolean>,
                     "awaitData" : <boolean>,
                     "originatingCommand" : <document>,
                     "planSummary" : <string>,
                     "operationUsingCursorId" : <Long()>
                  },
                  "msg": <string>,
                  "progress" : {
                      "done" : <number>,
                      "total" : <number>
                  },
                  "killPending" : <boolean>,
                  "numYields" : <number>,
                  "dataThroughputLastSecond" : <number>, 
                  "dataThroughputAverage" : <number>, 
                  "waitingForLatch" : { 
                      "timestamp" : <ISODate()>,
                      "captureName" : <string>
                  },
                  "locks" : {
                      "ParallelBatchWriterMode" : <string>,
                      "ReplicationStateTransition" : <string>,
                      "Global" : <string>,
                      "Database" : <string>,
                      "Collection" : <string>,
                      "Metadata" : <string>,
                      "oplog" : <string>
                  },
                  "waitingForLock" : <boolean>,
                  "lockStats" : {
                      "ParallelBatchWriterMode": {
                         "acquireCount": {
                            "r": <NumberLong>,
                            "w": <NumberLong>,
                            "R": <NumberLong>,
                            "W": <NumberLong>
                         },
                         "acquireWaitCount": {
                            "r": <NumberLong>,
                            "w": <NumberLong>,
                            "R": <NumberLong>,
                            "W": <NumberLong>
                         },
                         "timeAcquiringMicros" : {
                            "r" : Long(0),
                            "w" : Long(0),
                            "R" : Long(0),
                            "W" : Long(0)
                         },
                         "deadlockCount" : {
                            "r" : Long(0),
                            "w" : Long(0),
                            "R" : Long(0),
                            "W" : Long(0)
                         }
                      },
                      "ReplicationStateTransition" : {
                         ...
                      },
                      "Global" : {
                         ...
                      },
                      "Database" : {
                         ...
                      },
                      ...
                  }
                },
                ...
            ],
           "ok": <num>,
           "operationTime": <timestamp>,
           "$clusterTime": <document>
         }
         ```

## Specific Output Examples

These output samples illustrate `currentOp` output for particular
operations. The fields that make up the actual output vary depending on
the server's role. 

### Resharding Output Example

```javascript
{    
    type: "op",
    desc: "Resharding{Donor, Recipient, Coordinator}Service <reshardingUUID>",
    op: "command",
    ns: "<database>.<collection>",
    originatingCommand: {
        reshardCollection: "<database>.<collection>",
        key: <shardkey>,
        unique: <boolean>,
        collation: {locale: "simple"},
        // Other options to the reshardCollection command are omitted
        // to decrease the likelihood the output is truncated.
   },
   {donor, coordinator, recipient}State : "<service state>",
   approxDocumentsToCopy: NumberLong(<count>),
   approxBytesToCopy: NumberLong(<count>),
   bytesCopied: NumberLong(<count>),
   countWritesToStashCollections: NumberLong(<count>),
   countWritesDuringCriticalSection : NumberLong(<count>),
   countReadsDuringCriticalSection: NumberLong(<count>),
   deletesApplied: NumberLong(<count>),
   documentsCopied: NumberLong(<count>),
   insertsApplied: NumberLong(<count>),
   oplogEntriesFetched: NumberLong(<count>),
   oplogEntriesApplied: NumberLong(<count>),
   remainingOperationTimeEstimatedSecs: NumberLong(<count>),
   allShardsLowestRemainingOperationTimeEstimatedSecs: NumberLong(<estimate>),
   allShardsHighestRemainingOperationTimeEstimatedSecs: NumberLong(<estimate>),
   totalApplyTimeElapsedSecs: NumberLong(<count>),
   totalCopyTimeElapsedSecs: NumberLong(<count>),
   totalCriticalSectionTimeElapsedSecs : NumberLong(<count>),
   totalOperationTimeElapsedSecs: NumberLong(<count>),
   updatesApplied: NumberLong(<count>),
}
```

### Global Index Example

```javascript
{
    type: "op",
    desc: "GlobalIndex{Donor, Recipient, Coordinator}Service <globalIndexUUID}",
    op: "command",
    ns: "<database>.<collection>",
    originatingCommand: {
        createIndexes: "<database>.<collection>",
        key: <indexkeypattern>,
        unique: <boolean>,
        <Additional createIndexes options>
    },
   {donor, coordinator, recipient}State : "<service state>",
   approxDocumentsToScan: Long(<count>),
   approxBytesToScan: Long(<count>),
   bytesWrittenFromScan: Long(<count>),
   countWritesToStashCollections: Long(<count>),
   countWritesDuringCriticalSection : Long(<count>),
   countReadsDuringCriticalSection: Long(<count>),
   keysWrittenFromScan: Long(<count>),
   remainingOperationTimeEstimatedSecs: Long(<count>),
   allShardsLowestRemainingOperationTimeEstimatedSecs: Long(<estimate>),
   allShardsHighestRemainingOperationTimeEstimatedSecs: Long(<estimate>),
   totalCopyTimeElapsedSecs: Long(<count>),
   totalCriticalSectionTimeElapsedSecs : Long(<count>),
   totalOperationTimeElapsedSecs: Long(<count>),
}
```

## Output Fields

**`currentOp.type`**

The type of operation. Values are either:

- `op`
- `idleSession`
- `idleCursor`

If the `currentOp.type` is `op`, `currentOp.op`
provides details on the specific operation.

**`currentOp.host`**

The name of the host against which the operation is run.

**`currentOp.desc`**

A description of the client. This string includes the
`connectionId`.

**`currentOp.connectionId`**

An identifier for the connection where the operation originated.

**`currentOp.client`**

A string with information about where the operation originated.

For multi-document transactions, `client` stores
information about the most recent client to run an operation inside
the transaction.

**`currentOp.appName`**

The identifier of the client application which ran the operation. Use
the `appName` connection string option to set a custom value
for the `appName` field.

**`currentOp.clientMetadata`**

Additional information on the client.

For multi-document transactions, `client` stores
information about the most recent client to run an operation inside
the transaction.

**`currentOp.currentOpTime`**

The start time of the operation.

**`currentOp.effectiveUsers`**

An array that contains a document for each user associated with the
operation. Each user document contains the `user` name and the
authentication `db`.

**See also:**

`currentOp.runBy`

**`currentOp.runBy`**

An array that contains a document for each user who is impersonating
the `effectiveUser(s)` for the
operation. The runBy document contains the `user` name
and the authentication `db`. In general, the runBy user is
the `__system` user; e.g.

```javascript
"runBy" : [
   {
      "user" : "__system",
      "db" : "local"
   }
]
```

*Only available on sharded clusters*

**`currentOp.lsid`**

The session identifier.

Only present if the operation is associated with a
session.

**`currentOp.transaction`**

A document that contains multi-document transaction information.

Only present if the operation is part of a multi-document transaction.

**`currentOp.transaction.parameters`**

A document that contains information on multi-document
transaction.

Only present if the operation is part of a multi-document
transaction.

**`currentOp.transaction.parameters.txnNumber`**

The transaction number.

Only present if the operation is part of a multi-document transaction.

**`currentOp.transaction.parameters.autocommit`**

A boolean flag that indicates if autocommit is on for the
transaction.

Only present if the operation is part of a multi-document transaction.

**`currentOp.transaction.parameters.readConcern`**

The read concern for the
transaction.

Multi-document transactions support read concern
`"snapshot"`, `"local"`, and
`"majority"`.

Only present if the operation is part of a multi-document transaction.

**`currentOp.transaction.readTimestamp`**

The timestamp of the snapshot being read by the operations in
the transaction.

Only present if the operation is part of a multi-document transaction.

**`currentOp.transaction.startWallClockTime`**

The date and time (with time zone) of the transaction start.

Only present if the operation is part of a multi-document transaction.

**`currentOp.transaction.timeOpenMicros`**

The duration of the transaction in microseconds.

The `timeActiveMicros`
value added to the
`timeInactiveMicros`
should equal the
`timeOpenMicros`.

Only present if the operation is part of a multi-document transaction.

**`currentOp.transaction.timeActiveMicros`**

The total amount of time that the transaction has been active;
i.e. when the transaction had operations running.

The
`timeActiveMicros`
value added to the
`timeInactiveMicros`
should equal the
`timeOpenMicros`.

Only present if the operation is part of a multi-document transaction.

**`currentOp.transaction.timeInactiveMicros`**

The total amount of time that the transaction has been
inactive; i.e. when the transaction had no operations running.

The
`timeInactiveMicros`
value added to the
`timeActiveMicros`
should equal the
`timeOpenMicros`.

Only present if the operation is part of a multi-document transaction.

**`currentOp.transaction.expiryTime`**

The date and time (with time zone) when the transaction will
time out and abort.

The `currentOp.transaction.expiryTime` equals the
`currentOp.transaction.startWallClockTime` + the
`transactionLifetimeLimitSeconds`.

For more information, see transaction-limit for
transactions.

Only present if the operation is part of a multi-document transaction.

**`currentOp.twoPhaseCommitCoordinator`**

Information on either:

- .. _current-op-cmd-commit-coord-metrics:

  The commit coordination metrics for a transaction whose
  write operations span multiple shards.

  Commit coordination is handled by a shard, and
  `currentOp` (run either on a `mongos` or a
  shard member) returns a shard's coordination information only for
  those transactions currently being coordinated by that shard.

  To filter for just the commit coordination metrics:

  ```javascript
  db.currentOp( { desc:  "transaction coordinator" })
  ```

- .. _current-op-cmd-commit-coord-operation:

  A specific commit coordination operation (i.e.
  `currentOp.type` is `op` and `currentOp.desc` is
  `"TransactionCoordinator"`) spawned by the transaction
  coordinator.

**`currentOp.twoPhaseCommitCoordinator.lsid`**

The session identifier for the multi-shard transaction.

The combination of the
`lsid` and
`txnNumber` identifies
the transaction.

Available for both the commit coordination metrics and for specific
coordination operation.

**`currentOp.twoPhaseCommitCoordinator.txnNumber`**

The transaction number for the multi-shard transaction.

The combination of the
`txnNumber` and
`lsid` identifies the
transaction.

Available for both the commit coordination metrics and for specific
coordination operation.

**`currentOp.twoPhaseCommitCoordinator.action`**

The specific commit coordination operation spawned by the
transaction coordinator:

- `"sendingPrepare"`
- `"sendingCommit"`
- `"sendingAbort"`
- `"writingParticipantList"`
- `"writingDecision"`
- `"deletingCoordinatorDoc"`

Only available for specific coordination operation.

**`currentOp.twoPhaseCommitCoordinator.startTime`**

The start date and time of the
`action`.

Only available for specific coordination operation.

**`currentOp.twoPhaseCommitCoordinator.numParticipants`**

Number of shards participating in this commit.

Only available for the commit coordination metrics.

**`currentOp.twoPhaseCommitCoordinator.state`**

The current step/state of the commit coordination process.

| Step/stage | Description |
|---|---|
| `inactive` | Not actively part of a commit. |
| `writingParticipantList` | Writing a local record of the list of shards that are part of this multi-shard transaction. |
| `waitingForVotes` | Waiting for the participants to respond with vote to commit or abort. |
| `writingDecision` | Writing a local record of the coordinator's decision to commit or abort based on votes. |
| `waitingForDecisionAck` | Waiting for participants to acknowledge the coordinator's decision to commit or abort. |
| `deletingCoordinatorDoc` | Deleting the local record of commit decision. |

Only available for the commit coordination metrics.

See also
`currentOp.twoPhaseCommitCoordinator.stepDurations`.

**`currentOp.twoPhaseCommitCoordinator.commitStartTime`**

The date and time when the commit started.

Only available for the commit coordination metrics.

**`currentOp.twoPhaseCommitCoordinator.hasRecoveredFromFailover`**

A boolean that indicates whether the commit coordination was
restarted due to failover on the shard that is coordinating the
commit.

If
`hasRecoveredFromFailover`
is true, then the times specified in
`currentOp.twoPhaseCommitCoordinator.stepDurations` may not
be accurate for all steps.

Only available for the commit coordination metrics.

**`currentOp.twoPhaseCommitCoordinator.stepDurations`**

A document that contains the duration, in microseconds, of the
commit coordination `steps/state` completed or in
progress:

```javascript
"stepDurations" : {
   "writingParticipantListMicros" : Long(17801),
   "totalCommitDurationMicros" : Long(42488463),
   "waitingForVotesMicros" : Long(30378502),
   "writingDecisionMicros" : Long(15015),
   "waitingForDecisionAcksMicros" : Long(12077145),
   "deletingCoordinatorDocMicros" : Long(6009)
},
```

If
`currentOp.twoPhaseCommitCoordinator.hasRecoveredFromFailover`
is true, then the times specified in
`stepDurations` may not
be accurate for all steps.

For a coordinator in an `inactive` state, the document is empty:

```javascript
"stepDurations" : {
}
```

Only available for the commit coordination metrics.

See `currentOp.twoPhaseCommitCoordinator.state`.

**`currentOp.twoPhaseCommitCoordinator.decision`**

A document that contains the commit/abort decision, for example:

- For a commit decision:

  ```javascript
  "decision" : {
     "decision" : "commit",
     "commitTimestamp" : Timestamp(1572034669, 3)
  }
  ```

- For an abort decision:

  ```javascript
  "decision" : {
     "decision" : "abort",
     "abortStatus" : {
        "code" : 282,
        "codeName" : "TransactionCoordinatorReachedAbortDecision",
        "errmsg" : "Transaction exceeded deadline"
     }
  }
  ```

Only available for the commit coordination metrics.

**`currentOp.twoPhaseCommitCoordinator.deadline`**

The date and time by which the commit must finish.

Only available for the commit coordination metrics.

**`currentOp.opid`**

The identifier for the operation. You can pass this value to
`db.killOp()` in `mongosh` to terminate the
operation.

**Warning:**

Terminate running operations with extreme caution. Only use
`db.killOp()` to terminate operations initiated by clients
and *do not* terminate internal database operations.

**`currentOp.active`**

A boolean value specifying whether the operation has started. Value
is `true` if the operation has started or `false` if the
operation is idle, such as an idle connection or an internal thread
that is currently idle. An operation can be active even if the
operation has yielded to another operation. For some inactive
background threads, such as an inactive `signalProcessingThread`,
MongoDB suppresses various empty fields.

**`currentOp.secs_running`**

The duration of the operation in seconds. MongoDB calculates this
value by subtracting the current time from the start time of the
operation.

Only appears if the operation is running; i.e. if
`active` is `true`.

**`currentOp.microsecs_running`**

The duration of the operation in microseconds. MongoDB calculates this
value by subtracting the current time from the start time of the
operation.

Only appears if the operation is running; i.e. if
`active` is `true`.

**`currentOp.op`**

A string that identifies the specific operation type. Only present
if `currentOp.type` is `op`.

The possible values are:

- `"none"`
- `"update"`
- `"insert"`
- `"query"`
- `"command"`
- `"getmore"`
- `"remove"`
- `"killcursors"`

`"query"` operations include read operations.

`"command"` operations include most 
commands such as the
`createIndexes` and `findAndModify`.

**`currentOp.ns`**

The namespace the operation targets. A namespace consists of
the database name and the collection name
concatenated with a dot (`.`); that is,
`"<database>.<collection>"`.

**`currentOp.command`**

A document containing the full command object associated with this
operation. 

For example, the following output contains the command object for a
`find` operation on a collection named `items` in a
database named `test`:

```javascript
"command" : {
  "find" : "items",
  "filter" : {
    "sku" : 1403978
  },
  ...
  "$db" : "test"
}
```

The following example output contains the command object for a
`getMore` operation generated by
a command with cursor ID `19234103609` on a collection named
`items` in a database named `test`:

```javascript
"command" : {
    "getMore" : Long("19234103609"),
    "collection" : "items",
    "batchSize" : 10,
    ...
    "$db" : "test"
},
```

If the command document exceeds 1 kilobyte, the
document has the following form:

```javascript
"command" : {
  "$truncated": <string>,
  "comment": <string>
}
```

The `$truncated` field contains a string summary of the document excluding
the document's `comment` field if present. If the summary still exceeds
1 kilobyte then it is further truncated, denoted by an ellipsis
(...) at the end of the string.

The `comment` field is present if a comment was passed to the operation.
A comment may be attached to any database command.

**`currentOp.planSummary`**

Specifies whether the cursor uses a collection scan
(`COLLSCAN`) or an index scan (`IXSCAN { ... }`).

The `IXSCAN` also includes the specification document of the index
used.

**`currentOp.prepareReadConflicts`**

The number of times the current operation had to wait for a
prepared transaction with a write to commit or abort.

While waiting, the current operation continues to hold any necessary
locks and storage engine resources.

**`currentOp.writeConflicts`**

The number of times the current operation conflicted with
another write operation on the same document.

**`currentOp.cursor`**

A document that contains the cursor information for `getmore`
operations; i.e. where `op` is `getmore`.

If reporting on a `getmore` operation before the `getmore` has
accessed its cursor information, the `cursor` field
is not available.

**`currentOp.cursor.cursorId`**

The ID of the cursor.

**`currentOp.cursor.createdDate`**

The date and time when the cursor was created.

**`currentOp.cursor.lastAccessDate`**

The date and time when the cursor was last used.

**`currentOp.cursor.nDocsReturned`**

The cumulative number of documents returned by the cursor.

**`currentOp.cursor.nBatchesReturned`**

The cumulative number of batches returned by the cursor.

**`currentOp.cursor.noCursorTimeout`**

The flag that indicates that the cursor will not timeout when idle;
i.e. if the cursor has the `noTimeout` option set.

- If true, the cursor does not time out when idle.

- If false, the cursor times out when idle.

**See also:**

`cursor.addOption()`

**`currentOp.cursor.tailable`**

The flag that indicates if the cursor is a tailable cursor for a capped collection. Tailable cursors
remain open after the client exhausts the results in the initial
cursor.

**See also:**

- `find`
- `cursor.tailable()`
- `cursor.addOption()`

**`currentOp.cursor.awaitData`**

The flag that indicates whether the tailable cursor should temporarily block a
`getMore` command on the cursor while waiting for new
data rather than returning no data.

For non-tailable cursors, the value is always false.

**See also:**

- `find`
- `cursor.tailable()`
- `cursor.addOption()`

**`currentOp.cursor.originatingCommand`**

The `originatingCommand` field contains the full command object
(e.g. `find` or `aggregate`) which originally created the
cursor.

**`currentOp.cursor.planSummary`**

Specifies whether the cursor uses a collection scan
(`COLLSCAN`) or an index scan (`IXSCAN { ... }`).

The `IXSCAN` also includes the specification document of the index
used.

**`currentOp.cursor.operationUsingCursorId`**

The `opid` of the operation using the cursor.

Only present if the cursor is not idle.

**`currentOp.waitingForLatch`**

The `waitingForLatch` document is only
available if the operation is waiting to acquire an internal locking
primitive (a.k.a. a latch) or for an internal condition to be met.

For example,

```javascript
"waitingForLatch" : {
   "timestamp" : ISODate("2020-03-19T23:25:58.412Z"),
   "captureName" : "FutureResolution",
},
```

| Output Field | Description |
|---|---|
| timestamp | The date and time at which the operation started to wait. |
| captureName | The internal name of the section where the operation is currently blocked. |

**New in version:** 4.2.2

**`currentOp.locks`**

The `locks` document reports the type and mode of
locks the operation currently holds. The possible lock types are as
follows:

| Lock Type | Description |
|---|---|
| `ParallelBatchWriterMode` | Represents a lock for parallel batch writer mode. In earlier versions, PBWM information was reported as part of the `Global` lock information. |
| `ReplicationStateTransition` | Represents lock taken for replica set member state transitions. |
| `Global` | Represents global lock. |
| `Database` | Represents database lock. |
| `Collection` | Represents collection lock. |
| `Mutex` | Represents mutex. |
| `Metadata` | Represents metadata lock. |
| `oplog` | Represents lock on the oplog. |

The possible modes are as follows:

| Lock Mode | Description |
|---|---|
| `R` | Represents Shared (S) lock. |
| `W` | Represents Exclusive (X) lock. |
| `r` | Represents Intent Shared (IS) lock. |
| `w` | Represents Intent Exclusive (IX) lock. |

**`currentOp.waitingForLock`**

Returns a boolean value. `waitingForLock` is `true` if the
operation is waiting for a lock and `false` if the operation has
the required lock.

**`currentOp.msg`**

The `msg` provides a message that describes the status and
progress of the operation. In the case of indexing or mapReduce
operations, the field reports the completion percentage.

**`currentOp.progress`**

Reports on the progress of mapReduce or indexing operations. The
`progress` fields corresponds to the completion percentage in
the `msg` field. The `progress` specifies the following
information:

**`currentOp.progress.done`**

Reports the number completed.

**`currentOp.progress.total`**

Reports the total number.

**`currentOp.killPending`**

Returns `true` if the operation is currently flagged for
termination.  When the operation encounters its next safe termination point, the
operation will terminate.

**`currentOp.numYields`**

`numYields` is a counter that reports the number of times the
operation has yielded to allow other operations to complete.

Typically, operations yield when they need access to data that
MongoDB has not yet fully read into memory. This allows
other operations that have data in memory to complete quickly
while MongoDB reads in data for the yielding operation.

**`currentOp.dataThroughputLastSecond`**

Amount of data (in MiB) processed by the `validate`
operation in the last second. Only available for a
`validate` operation that is currently scanning
documents. For example:

```json
"msg" : "Validate: scanning documents Validate: scanning documents: 7258/24000 30%",
"progress" : {
   "done" : 7258,
   "total" : 24000
},
"numYields" : 0,
"dataThroughputLastSecond" : 15.576952934265137,
"dataThroughputAverage" : 15.375944137573242,
```

**`currentOp.dataThroughputAverage`**

The average amount of data (in MiB) processed by the
`validate` operation. Only available for a
`validate` operation that is currently scanning
documents. For example:

```json
"msg" : "Validate: scanning documents Validate: scanning documents: 7258/24000 30%",
"progress" : {
   "done" : 7258,
   "total" : 24000
},
"numYields" : 0,
"dataThroughputLastSecond" : 15.576952934265137,
"dataThroughputAverage" : 15.375944137573242,
```

**`currentOp.fsyncLock`**

Specifies if database is currently locked for `fsync
write/snapshot`.

Only appears if locked; i.e. if `fsyncLock` is
`true`.

**`currentOp.info`**

Information regarding how to unlock database from
`db.fsyncLock()`. Only appears if
`fsyncLock` is `true`.

**`currentOp.lockStats`**

For each lock type and mode (see `currentOp.locks` for
descriptions of lock types and modes), returns the following
information:

**`currentOp.lockStats.acquireCount`**

Number of times the operation acquired the lock in the specified
mode.

**`currentOp.lockStats.acquireWaitCount`**

Number of times the operation had to wait for the
`acquireCount` lock acquisitions
because the locks were held in a conflicting mode.
`acquireWaitCount` is less than or
equal to `acquireCount`.

**`currentOp.lockStats.timeAcquiringMicros`**

Cumulative time in microseconds that the operation had to wait to
acquire the locks.

`timeAcquiringMicros` divided by
`acquireWaitCount` gives an
approximate average wait time for the particular lock mode.

**`currentOp.lockStats.deadlockCount`**

Number of times the operation encountered deadlocks while waiting
for lock acquisitions.

**`currentOp.waitingForFlowControl`**

A boolean that indicates if the operation is in the process of waiting for
flow control.

**`currentOp.flowControlStats`**

The flow control statistics for this operation.

**`currentOp.flowControlStats.acquireCount`**

The number of times this operation acquired a ticket.

**`currentOp.flowControlStats.acquireWaitCount`**

The number of times this operation waited to acquire a ticket.

**`currentOp.flowControlStats.timeAcquiringMicros`**

The total time this operation has waited to acquire a ticket.

**`currentOp.totalOperationTimeElapsedSecs`**

The total time elapsed, in seconds, for the current resharding
operation. The time is set to 0 when a new
resharding operation starts.

Only present if a resharding operation is taking place.

**New in version:** 5.0

Starting in MongoDB 6.1, this metric is also available on the
coordinator during resharding.

**`currentOp.updatesApplied`**

The number of updates applied.

Only present on a recipient shard when a resharding operation is
taking place.

**New in version:** 6.1

**`currentOp.remainingOperationTimeEstimatedSecs`**

`remainingOperationTimeEstimatedSecs`: estimated time remaining in
seconds for the current resharding operation. It is returned as `-1` when a new resharding
operation starts.

Starting in:

- MongoDB 5.0, but before MongoDB 6.1,
  `remainingOperationTimeEstimatedSecs` is only available on a
  recipient shard during a
  resharding operation.
- MongoDB 6.1, `remainingOperationTimeEstimatedSecs` is also available
  on the coordinator during a resharding operation.

The resharding operation performs these phases in order:

#. The clone phase duplicates the current collection data.
#. The catch-up phase applies any pending write operations to the
   resharded collection.

`remainingOperationTimeEstimatedSecs` is set to a pessimistic time
estimate:

- The catch-up phase time estimate is set to the clone phase time, which
  is a relatively long time.
- In practice, if there are only a few pending write operations, the
  actual catch-up phase time is relatively short.

**New in version:** 5.0

**`currentOp.allShardsLowestRemainingOperationTimeEstimatedSecs`**

Calculated across all shards, the lowest estimate of the number of
seconds remaining. 

Only present on a coordinator when a resharding operation is
taking place.

**New in version:** 6.1

**`currentOp.allShardsHighestRemainingOperationTimeEstimatedSecs`**

Calculated across all shards, the highest estimate of the number of
seconds remaining. 

Only present on a coordinator when a resharding operation is
taking place.

**New in version:** 6.1

**`currentOp.approxDocumentsToCopy`**

The approximate number of documents to be copied from the donor
shards to the recipient shards during the resharding operation. This number is an estimate that is set at the
beginning of the resharding operation and does not change after it
has been set. The number is set to 0 when a new resharding operation
starts. It is possible for `$currentOp.documentsCopied` and
`$currentOp.bytesCopied` to end up exceeding
`$currentOp.approxDocumentsToCopy` and
`$currentOp.approxBytesToCopy`, respectively, if
the post-resharding data distribution is not perfectly uniform.

Only present on a recipient shard when a resharding operation is
taking place.

**New in version:** 5.0

**`currentOp.documentsCopied`**

The number of documents copied form donor shards to recipient shards
during the resharding operation. The
number is set to 0 when a new resharding operation starts.

Only present on a recipient shard when a resharding operation is
taking place.

**New in version:** 5.0

**`currentOp.approxBytesToCopy`**

The approximate number of bytes to be copied from the donor shards to
the recipient shards during the resharding operation. This number is an estimate that is set at the
beginning of the resharding operation and does not change after it
has been set. The number is set to 0 when a new resharding operation
starts. It is possible for `$currentOp.documentsCopied` and
`$currentOp.bytesCopied` to end up exceeding
`$currentOp.approxDocumentsToCopy` and
`$currentOp.approxBytesToCopy`, respectively, if the
post-resharding data distribution is not perfectly uniform.

Only present on a recipient shard when a resharding operation is
taking place.

**New in version:** 5.0

**`currentOp.bytesCopied`**

The number of bytes copied from donor shards to recipient shards
during the resharding operation. The
number is set to 0 when a new resharding operation starts.

Only present on a recipient shard when a resharding operation is
taking place.

**New in version:** 5.0

**`currentOp.countWritesToStashCollections`**

The number of writes to the recipient stash collections.

Only present on a recipient shard when a resharding operation is
taking place.

**New in version:** 6.1

**`currentOp.countWritesDuringCriticalSection`**

The number of writes attempted during the donor's critical
section.

Only present on a donor shard when a resharding operation is
taking place.

**New in version:** 6.1

**`currentOp.countReadsDuringCriticalSection`**

The number of reads attempted during the donor's critical
section.

Only present on a donor shard when a resharding operation is
taking place.

**New in version:** 6.1

**`currentOp.deletesApplied`**

The number of deletes applied to the temporary resharding collection.
Each oplog entry that involves a delete increments the counter by 1.

Only present on a recipient shard when a resharding operation is
taking place.

**New in version:** 6.1

**`currentOp.insertsApplied`**

The number of inserts applied to the temporary resharding collection.
Each oplog entry that involves an insert increments the counter by 1.

Only present on a recipient shard when a resharding operation is
taking place.

**New in version:** 6.1

**`currentOp.totalCopyTimeElapsedSecs`**

The total elapsed time, in seconds, for ongoing data copy tasks from
donor shards to recipient shards for the current resharding
operation. The time is set to 0 when a new
resharding operation starts.

Only present on a recipient shard when a resharding operation is
taking place.

**New in version:** 5.0

Starting in MongoDB 6.1, this metric is also available on the
coordinator during resharding.

**`currentOp.oplogEntriesFetched`**

The number of entries fetched from the oplog for the current
resharding operation. The number is set
to 0 when a new resharding operation starts.

Only present on a recipient shard when a resharding operation is
taking place.

**New in version:** 5.0

**`currentOp.oplogEntriesApplied`**

The number of entries applied to the oplog for the current
resharding operation. The number is set
to 0 when a new resharding operation starts.

Only present on a recipient shard when a resharding operation is
taking place.

**New in version:** 5.0

**`currentOp.totalApplyTimeElapsedSecs`**

The total elapsed time, in seconds, for the apply step of the
current resharding operation. In the
apply step, recipient shards apply oplog entries to modify
their data based on new incoming writes from donor shards. The time
is set to 0 when a new resharding operation starts.

Only present on a recipient shard when a resharding operation is
taking place.

**New in version:** 5.0

Starting in MongoDB 6.1, this metric is also available on the
coordinator during resharding.

**`currentOp.countWritesDuringCriticalSection`**

The number of writes performed in the critical section for the current
resharding operation. The critical
section prevents new incoming writes to the collection currently
being resharded. The number is set to 0 when a new resharding
operation starts.

Only present on a donor shard when a resharding operation is taking
place.

**New in version:** 5.0

**`currentOp.totalCriticalSectionTimeElapsedSecs`**

The total elapsed time, in seconds, for the critical section of the
current resharding operation. The
critical section prevents new incoming writes to the collection
currently being resharded. The time is set to 0 when a new
resharding operation starts.

Only present on a donor shard when a resharding operation is taking
place.

**New in version:** 5.0

Starting in MongoDB 6.1, this metric is also available on the
coordinator during resharding.

**`currentOp.donorState`**

The current state of a donor shard for the resharding operation. The state is set to `unused` when a new
resharding operation starts.

Only present on a donor shard when a resharding operation is taking
place.

| State | Description |
|---|---|
| `unused` | The resharding operation is about to start or recovering from a primary failover. |
| `preparing-to-donate` | The donor shard is preparing to donate data to the recipient shards. |
| `donating-initial-data` | The donor shard is donating data to the recipient shards. |
| `donating-oplog-entries` | The donor shard is donating oplog entries to the recipient shards. |
| `preparing-to-block-writes` | The donor shard is about to prevent new incoming write operations to the collection that is being resharded. |
| `error` | An error occurred during the resharding operation. |
| `blocking-writes` | The donor shard is preventing new incoming write operations and the donor shard has notified all recipient shards that new incoming writes are prevented. |
| `done` | The donor shard has dropped the old sharded collection and the resharding operation is complete. |

**New in version:** 5.0

**`currentOp.recipientState`**

The current state of a recipient shard for a resharding
operation. The state is set to `unused` when
a new resharding operation starts.

Only present on a donor shard when a resharding operation is taking
place.

| State | Description |
|---|---|
| `unused` | The resharding operation is about to start or recovering from a primary failover. |
| `awaiting-fetch-timestamp` | The recipient shard is waiting for the donor shards to be prepared to donate their data. |
| `creating-collection` | The recipient shard is creating the new sharded collection. |
| `cloning` | The recipient shard is receiving data from the donor shards. |
| `applying` | The recipient shard is applying oplog entries to modify its copy of the data based on the new incoming writes from donor shards. |
| `error` | An error occurred during the resharding operation. |
| `strict-consistency` | The recipient shard has all data changes stored in a temporary collection. |
| `done` | The resharding operation is complete. |

**New in version:** 5.0

**`currentOp.coordinatorState`**

The state of the resharding coordinator for the current
resharding operation. The resharding
coordinator is an operation that runs on the config server primary. The state is set to
`unused` when a new resharding operation starts.

Only present on the coordinating config server.

* - State
  - Description

* - `unused`
  - The resharding operation is about to start or recovering from
    a primary failover.

* - `initializing`
  - The resharding coordinator has inserted the coordinator
    document into `config.reshardingOperations` and has added
    the `reshardingFields` to the `config.collections` entry
    for the original collection.

* - `preparing-to-donate`
  - The resharding coordinator

    - has created a `config.collections` entry for the temporary
      resharding collection.
    - has inserted entries into `config.chunks` for ranges based
      on the new shard key.
    - has inserted entries into `config.tags` for any zones
      associated with the new shard key.

    The coordinator informs participant shards to begin the
    resharding operation. The coordinator then waits until all
    donor shards have picked a `minFetchTimestamp` and are ready
    to donate.

* - `cloning`
  - The resharding coordinator informs donor shards to donate data
    to recipient shards. The coordinator waits for all recipients
    to finish cloning the data from the donor.

* - `applying`
  - The resharding coordinator informs recipient shards to modify
    their copies of data based on new incoming writes from donor
    shards. The coordinator waits for all recipients to finish
    applying oplog entries.

* - `blocking-writes`
  - The resharding coordinator informs donor shards to prevent new
    incoming write operations to the collection being resharded.
    The coordinator then waits for all recipients to have all data
    changes.

* - `aborting`
  - An unrecoverable error occurred during the resharding
    operation or the `abortReshardCollection` command
    (or the `sh.abortReshardCollection()` method) was run.

* - `committing`
  - The resharding coordinator removes the `config.collections`
    entry for the temporary resharding collection. The coordinator
    then adds the `recipientFields` to the source collection's
    entry.

**New in version:** 5.0

**`currentOp.opStatus`**

This metric is removed in version 6.1. 

**Changed in version:** 6.1

**`currentOp.collUuid`**

The UUID of the sampled collection.

This field only appears on documents related to query sampling.
For details, see sampled-queries-currentOp-stage.

**New in version:** 7.0

**`currentOp.startTime`**

The time at which query sampling began.

This field only appears on documents related to query sampling.
For details, see sampled-queries-currentOp-stage.

**New in version:** 7.0

**`currentOp.samplesPerSecond`**

The maximum number of queries to sample per second.

On a sharded cluster, this is reported on `mongos` instead of 
`mongod`. On a replica set, this is reported on `mongod`.

This field only appears on documents related to query sampling.
For details, see sampled-queries-currentOp-stage.

**New in version:** 7.0

   

**`currentOp.sampledReadsCount`**

The number of sampled read queries.

This field only appears on documents related to query sampling.
For details, see sampled-queries-currentOp-stage.

**New in version:** 7.0

**`currentOp.sampledWritesCount`**

The number of sampled write queries.

This field only appears on documents related to query sampling.
For details, see sampled-queries-currentOp-stage.

**New in version:** 7.0

**`currentOp.sampledReadsBytes`**

The size of the sampled read queries, in bytes.

On a replica set, this is reported on every `mongod`.

On a sharded cluster, this only reported on `mongod` with 
`--shardsvr`.

This field only appears on documents related to query sampling.
For details, see sampled-queries-currentOp-stage.

**New in version:** 7.0

**`currentOp.sampledWritesBytes`**

The size of the sampled write queries, in bytes.

On a replica set, this is reported on every `mongod`.

On a sharded cluster, this only reported on `mongod` with 
`--shardsvr`.

This field only appears on documents related to query sampling.
For details, see sampled-queries-currentOp-stage.

**New in version:** 7.0
