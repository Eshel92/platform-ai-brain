<!-- Converted from reference/method/db.currentOp.txt (reStructuredText). Includes are inlined. -->

# db.currentOp() (mongosh method)

## Definition

**`db.currentOp()`**

**Important:**

The `currentOp` database command is deprecated 
since version 6.2. Use the `$currentOp` aggregation 
stage instead of the `currentOp` command and its 
`mongosh` helper method `db.currentOp()`.

Returns a document that contains information on in-progress
operations for the database instance. The `db.currentOp()`
method wraps the database command `currentOp`. 

**Note:**

Starting in MongoDB 5.0, the `$currentOp` aggregation 
stage is used when running the helper method `db.currentOp()` 
with `mongosh`.

Given this, in the 5.0 version of the shell and with mongosh,
`db.currentOp()` result sets are not subject to the
16MB BSON document return size 
document return size limit for documents of the previous legacy 
`mongo` versions.

## Compatibility

This method is available in deployments hosted in the following environments: 

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

`db.currentOp()` has the following form:

```javascript
db.currentOp(<operations>)
```

`db.currentOp()` can take the following *optional*
argument:

* - Parameter
  - Type
  - Description

* - operations
  - boolean or document
  - .. _method-currentop-operations:

    Optional. Specifies the operations to report on. Can pass either
    a boolean or a document:

    - Specify `true` to include operations on idle connections and
      system operations.
    - Specify a document with query conditions to report only on
      those operations that match the conditions. See
      currentOp-behavior for details.

## Behavior

`db.currentOp()` can accept a filter document or a boolean
parameter.

If you pass a filter document to `db.currentOp()`, the output
returns information only for the current operations that match the
filter. The filter document can contain:

| Field | Description |
|---|---|
| `"$ownOps"` | Boolean. If set to `true`, returns information on the current user's operations only. On `mongod` instances, users can always run `db.currentOp( { "$ownOps": true } )` to view their own operations. |
| `"$all"` | Boolean. If set to `true`, returns information on all operations, including operations on idle connections and system operations. For more information, see current-op-agg. If the document includes `"$all": true` along with db.currentOp-output-fields conditions, only the `"$all":true` applies. |
| <filter> | Specify filter conditions on the db.currentOp-output-fields. See currentOp-method-examples. If the document includes `"$all": true` along with db.currentOp-output-fields conditions, only the `"$all": true` applies. |

 
Passing in `true` to `db.currentOp()` is equivalent to
passing in a document of `{ "$all": true }`. The following operations
are equivalent:

```javascript
db.currentOp(true)
db.currentOp( { "$all": true } )
```

`db.currentOp` and the
database profiler report the same
basic diagnostic information for all CRUD operations, including the
following:

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

   

## Access Control

On systems running with `authorization`, the user
must have access that includes the `inprog` privilege
action. 

Users can run ``db.currentOp( { "$ownOps": true }
)`` on `mongod` instances to view their own operations
even without the `inprog` privilege action.

**See also:**

create-role-to-manage-ops

## Examples

The following examples use the `db.currentOp()` method with
various query documents to filter the output.

### Write Operations Waiting for a Lock

The following example returns information on all write operations that
are waiting for a lock:

```javascript
db.currentOp(
   {
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
db.currentOp(
   {
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
db.currentOp(
   {
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

**Note:**

Active Indexing Operations do not apply to rolling index builds. 

## Output Example

The following is a prototype of `db.currentOp()` output.

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

For a complete list of `db.currentOp()` output fields, see
currentOp.
