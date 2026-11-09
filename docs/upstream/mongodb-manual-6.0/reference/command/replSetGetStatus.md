<!-- Converted from reference/command/replSetGetStatus.txt (reStructuredText). Includes are inlined. -->

# replSetGetStatus

## Definition

**`replSetGetStatus`**

The `replSetGetStatus` command returns the status of the replica
set from the point of view of the server that processed the command.
`replSetGetStatus` must be run on the admin database.

The `mongod` instance must be a replica set member for
`replSetGetStatus` to return successfully.

Data provided by this command derives from data included in
heartbeats sent to the server by other members of the replica set.
Because of the frequency of heartbeats, these data can be several
seconds out of date.

**Tip:**

In `mongosh`, this command can also be run through the `rs.status` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

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
db.adminCommand( 
   { 
     replSetGetStatus: 1 
   } 
)
```

If you run `replSetGetStatus` or the `mongosh` helper 
`rs.status()` on a member during its initial sync (i.e. `STARTUP2` state), the command 
returns `replSetGetStatus.initialSyncStatus` metrics.
      
After the member completes the initial synchronization and transitions to 
another state, the `replSetGetStatus.initialSyncStatus` metrics are no 
longer available.

## Example

tabs:

   - id: primary
     name: Primary
     content: |

       The following example runs the `replSetGetStatus`
       command on the admin database of the replica set
       primary:

       ```javascript
       db.adminCommand( { replSetGetStatus: 1 } )
       ```

       The command returns the following output for an example
       replica set primary:

       ```javascript
       {
          "set" : "replset",
          "date" : ISODate("2024-08-15T23:06:13.978Z"),
          "myState" : 1,
          "term" : NumberLong(3),
          "syncSourceHost" : "",
          "syncSourceId" : -1,
          "heartbeatIntervalMillis" : NumberLong(2000),
          "majorityVoteCount" : 2,
          "writeMajorityCount" : 2,
          "votingMembersCount" : 3,           
          "writableVotingMembersCount" : 3,   
          "optimes" : {
             "lastCommittedOpTime" : {
                "ts" : Timestamp(1723763173, 1),
                "t" : NumberLong(3)
             },
             "lastCommittedWallTime" : ISODate("2024-08-15T23:06:13.978Z"),
             "readConcernMajorityOpTime" : {
                "ts" : Timestamp(1723763173, 1),
                "t" : NumberLong(3)
             },
             "readConcernMajorityWallTime" : ISODate("2024-08-15T23:06:13.978Z"),
             "appliedOpTime" : {
                "ts" : Timestamp(1723763173, 1),
                "t" : NumberLong(3)
             },
             "durableOpTime" : {
                "ts" : Timestamp(1723763173, 1),
                "t" : NumberLong(3)
             },
             "lastAppliedWallTime" : ISODate("2020-03-05T05:24:38.122Z"),
             "lastDurableWallTime" : ISODate("2020-03-05T05:24:38.122Z")
          },
          "lastStableRecoveryTimestamp" : Timestamp(1723763173, 1),
          "electionCandidateMetrics" : {
             "lastElectionReason" : "stepUpRequestSkipDryRun",
             "lastElectionDate" : ISODate("2024-08-15T23:06:13.978Z"),
             "electionTerm" : NumberLong(3),
             "lastCommittedOpTimeAtElection" : {
                "ts" : Timestamp(1723763173, 1),
                "t" : NumberLong(2)
             },
             "lastSeenOpTimeAtElection" : {
                "ts" : Timestamp(1723763173, 1),
                "t" : NumberLong(2)
             },
             "numVotesNeeded" : 2,
             "priorityAtElection" : 1,
             "electionTimeoutMillis" : NumberLong(10000),
             "priorPrimaryMemberId" : 1,
             "numCatchUpOps" : NumberLong(0),
             "newTermStartDate" : ISODate("2024-08-15T23:06:13.978Z"),
             "wMajorityWriteAvailabilityDate" : ISODate("2024-08-15T23:06:13.978Z")
          },
          "electionParticipantMetrics" : {
             "votedForCandidate" : true,
             "electionTerm" : NumberLong(2),
             "lastVoteDate" : ISODate("2024-08-15T23:06:13.978Z"),
             "electionCandidateMemberId" : 1,
             "voteReason" : "",
             "lastAppliedOpTimeAtElection" : {
                "ts" : Timestamp(1723763173, 1),
                "t" : NumberLong(1)
             },
             "maxAppliedOpTimeInSet" : {
                "ts" : Timestamp(1723763173, 1),
                "t" : NumberLong(1)
             },
             "priorityAtElection" : 1
          },
          "members" : [
             {
                "_id" : 0,
                "name" : "m1.example.net:27017",
                "health" : 1,
                "state" : 1,
                "stateStr" : "PRIMARY",
                "uptime" : 269,
                "optime" : {
                   "ts" : Timestamp(1723763173, 1),
                   "t" : NumberLong(3)
                },
               "optimeDurable" : {
                   "ts" : Timestamp(1723763173, 1),
                   "t" : NumberLong(3)
                },
                "optimeDate" : ISODate("2024-08-15T23:06:13.978Z"),
                "optimeWrittenDate" : ISODate("2024-08-15T23:06:13.978Z"),
                "lastAppliedWallTime": ISODate("2024-08-15T23:06:13.978Z"),
                "lastDurableWallTime": ISODate("2024-08-15T23:06:13.978Z"),
                "syncSourceHost" : "",
                "syncSourceId" : -1,
                "infoMessage" : "",
                "electionTime" : Timestamp(1723763173, 1),
                "electionDate" : ISODate("2024-08-15T23:06:13.978Z"),
                "configVersion" : 1,
                "configTerm" : 0,
                "self" : true,
                "lastHeartbeatMessage" : ""
             },
             {
                "_id" : 1,
                "name" : "m2.example.net:27017",
                "health" : 1,
                "state" : 2,
                "stateStr" : "SECONDARY",
                "uptime" : 266,
                "optime" : {
                   "ts" : Timestamp(1723763173, 1),
                   "t" : NumberLong(3)
                },
                "optimeDurable" : {
                   "ts" : Timestamp(1723763173, 1),
                   "t" : NumberLong(3)
                },
                "optimeDate" : ISODate("2024-08-15T23:06:13.978Z"),
                "optimeDurableDate" : ISODate("2024-08-15T23:06:13.978Z"),
                "lastAppliedWallTime": ISODate("2024-08-15T23:06:13.978Z"),
                "lastDurableWallTime": ISODate("2024-08-15T23:06:13.978Z"),
                "lastHeartbeat" : ISODate("2024-08-15T23:06:13.978Z"),
                "lastHeartbeatRecv" : ISODate("2024-08-15T23:06:13.978Z"),
                "pingMs" : NumberLong(0),
                "lastHeartbeatMessage" : "",
                "syncSourceHost" : "m3.example.net:27017",
                "syncSourceId" : 2,
                "infoMessage" : "",
                "configVersion" : 1
             },
             {
                "_id" : 2,
                "name" : "m3.example.net:27017",
                "health" : 1,
                "state" : 2,
                "stateStr" : "SECONDARY",
                "uptime" : 266,
                "optime" : {
                   "ts" : Timestamp(1723763173, 1),
                   "t" : NumberLong(3)
                },
                "optimeDurable" : {
                   "ts" : Timestamp(1723763173, 1),
                   "t" : NumberLong(3)
                },
                "optimeDate" : ISODate("2024-08-15T23:06:13.978Z"),
                "optimeDurableDate" : ISODate("2024-08-15T23:06:13.978Z"),
                "lastAppliedWallTime": ISODate("2024-08-15T23:06:13.978Z"),
                "lastDurableWallTime": ISODate("2024-08-15T23:06:13.978Z"),
                "lastHeartbeat" : ISODate("2024-08-15T23:06:13.978Z"),
                "lastHeartbeatRecv" : ISODate("2024-08-15T23:06:13.978Z"),
                "pingMs" : NumberLong(0),
                "lastHeartbeatMessage" : "",
                "syncSourceHost" : "m1.example.net:27017",
                "syncSourceId" : 0,
                "infoMessage" : "",
                "configVersion" : 1
             }
          ],
          "ok" : 1,
          "$clusterTime" : {
             "clusterTime" : Timestamp(1723763173, 1),
             "signature" : {
                "hash" : BinData(0,"9C2qcGVkipEGJW3iF90qxb/gIwc="),
                "keyId" : NumberLong("6800589497806356482")
             }
          },
          "operationTime" : Timestamp(1723763173, 1)
       }
       ```

   - id: secondary
     name: Secondary
     content: |

       The following example runs the `replSetGetStatus`
       command on the admin database of the replica set
       secondary:

       ```javascript
       db.adminCommand( { replSetGetStatus: 1 } )
       ```

       The command returns the following output for an example replica set secondary:

       ```javascript
       {
          "set" : "replset",
          "date" : ISODate("2024-08-15T23:06:13.978Z"),
          "myState" : 2,
          "term" : NumberLong(3),
          "syncSourceHost" : "m3.example.net:27017",
          "syncSourceId" : 2,
          "heartbeatIntervalMillis" : NumberLong(2000),
          "majorityVoteCount" : 2,
          "writeMajorityCount" : 2,
          "votingMembersCount" : 3,
          "writableVotingMembersCount" : 3,
          "optimes" : {
             "lastCommittedOpTime" : {
                "ts" : Timestamp(1723763173, 1),
                "t" : NumberLong(3)
             },
             "lastCommittedWallTime" : ISODate("2024-08-15T23:06:13.978Z"),
             "readConcernMajorityOpTime" : {
                "ts" : Timestamp(1723763173, 1),
                "t" : NumberLong(3)
             },
             "readConcernMajorityWallTime" : ISODate("2024-08-15T23:06:13.978Z"),
             "appliedOpTime" : {
                "ts" : Timestamp(1723763173, 1),
                "t" : NumberLong(3)
             },
             "durableOpTime" : {
                "ts" : Timestamp(1723763173, 1),
                "t" : NumberLong(3)
             },
             "lastAppliedWallTime" : ISODate("2024-08-15T23:06:13.978Z"),
             "lastDurableWallTime" : ISODate("2024-08-15T23:06:13.978Z")
          },
          "lastStableRecoveryTimestamp" : Timestamp(1723763173, 1),
          "electionParticipantMetrics" : {
             "votedForCandidate" : true,
             "electionTerm" : NumberLong(3),
             "lastVoteDate" : ISODate("2024-08-15T23:06:13.978Z"),
             "electionCandidateMemberId" : 0,
             "voteReason" : "",
             "lastAppliedOpTimeAtElection" : {
                "ts" : Timestamp(1723763173, 1),
                "t" : NumberLong(2)
             },
             "maxAppliedOpTimeInSet" : {
                "ts" : Timestamp(1723763173, 1),
                "t" : NumberLong(2)
             },
             "priorityAtElection" : 1,
             "newTermStartDate" : ISODate("2024-08-15T23:06:13.978Z"),
             "newTermAppliedDate" : ISODate("2024-08-15T23:06:13.978Z")
          },
          "members" : [
             {
                "_id" : 0,
                "name" : "m1.example.net:27017",
                "health" : 1,
                "state" : 1,
                "stateStr" : "PRIMARY",
                "uptime" : 407,
                "optime" : {
                   "ts" : Timestamp(1723763173, 1),
                   "t" : NumberLong(3)
                },
                "optimeDurable" : {
                   "ts" : Timestamp(1723763173, 1),
                   "t" : NumberLong(3)
                },
                "optimeDate" : ISODate("2024-08-15T23:06:13.978Z"),
                "optimeDurableDate" : ISODate("2024-08-15T23:06:13.978Z"),
                "lastAppliedWallTime": ISODate("2024-08-15T23:06:13.978Z"),
                "lastDurableWallTime": ISODate("2024-08-15T23:06:13.978Z"),
                "lastHeartbeat" : ISODate("2024-08-15T23:06:13.978Z"),
                "lastHeartbeatRecv" : ISODate("2024-08-15T23:06:13.978Z"),
                "pingMs" : NumberLong(0),
                "lastHeartbeatMessage" : "",
                "syncSourceHost" : "",
                "syncSourceId" : -1,
                "infoMessage" : "",
                "electionTime" : Timestamp(1723763173, 1),
                "electionDate" : ISODate("2024-08-15T23:06:13.978Z"),
                "configVersion" : 1
             },
             {
                "_id" : 1,
                "name" : "m2.example.net:27017",
                "health" : 1,
                "state" : 2,
                "stateStr" : "SECONDARY",
                "uptime" : 409,
                "optime" : {
                   "ts" : Timestamp(1723763173, 1),
                   "t" : NumberLong(3)
                },
                "optimeDurable" : {
                   "ts" : Timestamp(1723763173, 1),
                   "t" : NumberLong(3)
                },
                "optimeDate" : ISODate("2024-08-15T23:06:13.978Z"),
                "lastAppliedWallTime": ISODate("2024-08-15T23:06:13.978Z"),
                "lastDurableWallTime": ISODate("2024-08-15T23:06:13.978Z"),
                "syncSourceHost" : "m3.example.net:27017",
                "syncSourceId" : 2,
                "infoMessage" : "",
                "configVersion" : 1,
                "configTerm" : 0,
                "self" : true,
                "lastHeartbeatMessage" : ""
             },
             {
                "_id" : 2,
                "name" : "m3.example.net:27017",
                "health" : 1,
                "state" : 2,
                "stateStr" : "SECONDARY",
                "uptime" : 407,
                "optime" : {
                   "ts" : Timestamp(1723763173, 1),
                   "t" : NumberLong(3)
                },
                "optimeDurable" : {
                   "ts" : Timestamp(1723763173, 1),
                   "t" : NumberLong(3)
                },
                "optimeDate" : ISODate("2024-08-15T23:06:13.978Z"),
                "optimeDurableDate" : ISODate("2024-08-15T23:06:13.978Z"),
                "lastAppliedWallTime": ISODate("2024-08-15T23:06:13.978Z"),
                "lastDurableWallTime": ISODate("2024-08-15T23:06:13.978Z"),
                "lastHeartbeat" : ISODate("2024-08-15T23:06:13.978Z"),
                "lastHeartbeatRecv" : ISODate("2024-08-15T23:06:13.978Z"),
                "pingMs" : NumberLong(0),
                "lastHeartbeatMessage" : "",
                "syncSourceHost" : "m1.example.net:27017",
                "syncSourceId" : 0,
                "infoMessage" : "",
                "configVersion" : 1
             }
          ],
          "ok" : 1,
          "$clusterTime" : {
             "clusterTime" : Timestamp(1723763173, 1),
             "signature" : {
                "hash" : BinData(0,"kmhE5YARZlzn/DX4B/D0E5P6okY="),
                "keyId" : NumberLong("6800589497806356482")
             }
          },
          "operationTime" : Timestamp(1723763173, 1),
       }
       ```

       In earlier versions (3.6.x-4.2.0)
          You can include the optional `initialSync: 1` to include
          the `replSetGetStatus.initialSyncStatus` in the
          output (you can omit if you do not want to return the
          initial sync status):

          ```javascript
          db.adminCommand( { replSetGetStatus: 1, initialSync: 1 } )
          ```

   - id: startup2
     name: Include Initial Sync Metrics
     content: |

       Starting in MongoDB 5.2, 
          the `replSetGetStatus.initialSyncStatus` document
          contains additional fields when using a
          file copy based initial sync.

       If you run `replSetGetStatus` on a member during its 
       initial sync, the command returns 
       `replSetGetStatus.initialSyncStatus` metrics.

       ```javascript
       db.adminCommand( { replSetGetStatus: 1 } )
       ```

       After the member completes the initial synchronization and
       transitions to another state, the
       `replSetGetStatus.initialSyncStatus` metrics are no
       longer available.

       The following example runs the `replSetGetStatus`
       command on the admin database of the 4.4 replica
       set member during its initial sync:

       ```javascript
       {
          "set" : "replset",
          "date" : ISODate("2024-08-15T23:06:13.978Z")
          "myState" : 5,
          "term" : NumberLong(1),
          "syncSourceHost" : "m1.example.net:27017",
          "syncSourceId" : 0,
          "heartbeatIntervalMillis" : NumberLong(2000),
          "majorityVoteCount" : 2,
          "writeMajorityCount" : 2,
          "votingMembersCount" : 2,
          "writableVotingMembersCount" : 2,
          "optimes" : {
             "lastCommittedOpTime" : {
                "ts" : Timestamp(0, 0),
                "t" : NumberLong(-1)
             },
             "lastCommittedWallTime" : ISODate("1970-01-01T00:00:00Z"),
             "appliedOpTime" : {
                "ts" : Timestamp(0, 0),
                "t" : NumberLong(-1)
             },
             "durableOpTime" : {
                "ts" : Timestamp(0, 0),
                "t" : NumberLong(-1)
             },
             "lastAppliedWallTime" : ISODate("1970-01-01T00:00:00Z"),
             "lastDurableWallTime" : ISODate("1970-01-01T00:00:00Z")
          },
          "lastStableRecoveryTimestamp" : Timestamp(0, 0),
          "initialSyncStatus" : {
             "failedInitialSyncAttempts" : 0,
             "maxFailedInitialSyncAttempts" : 10,
             "initialSyncStart" : ISODate("2024-08-15T23:06:13.978Z"),
             "initialSyncAttempts" : [ ],
             "appliedOps" : 0,
             "initialSyncOplogStart" : Timestamp(1723763173, 1),
             "syncSourceUnreachableSince" : ISODate("2024-08-15T23:06:13.978Z"),
             "currentOutageDurationMillis" : NumberLong(8687),
             "totalTimeUnreachableMillis" : NumberLong(8687),
             "databases" : {
                "databasesCloned" : 3,
                "admin" : {
                   "collections" : 4,
                   "clonedCollections" : 4,
                   "start" : ISODate("2024-08-15T23:06:13.978Z"),
                   "end" : ISODate("2024-08-15T23:06:13.978Z"),
                   "elapsedMillis" : 429,
                   "admin.system.roles" : {
                      "documentsToCopy" : 22,
                      "documentsCopied" : 22,
                      "indexes" : 2,
                      "fetchedBatches" : 1,
                      "start" : ISODate("2024-08-15T23:06:13.978Z"),
                      "end" : ISODate("2024-08-15T23:06:13.978Z"),
                      "elapsedMillis" : 138,
                      "receivedBatches" : 1
                   },
                   "admin.system.users" : {
                      "documentsToCopy" : 32,
                      "documentsCopied" : 32,
                      "indexes" : 2,
                      "fetchedBatches" : 1,
                      "start" : ISODate("2024-08-15T23:06:13.978Z"),
                      "end" : ISODate("2024-08-15T23:06:13.978Z"),
                      "elapsedMillis" : 149,
                      "receivedBatches" : 1
                   },
                   "admin.system.keys" : {
                      "documentsToCopy" : 2,
                      "documentsCopied" : 2,
                      "indexes" : 1,
                      "fetchedBatches" : 1,
                      "start" : ISODate("2024-08-15T23:06:13.978Z"),
                      "end" : ISODate("2024-08-15T23:06:13.978Z"),
                      "elapsedMillis" : 76,
                      "receivedBatches" : 1
                   },
                   "admin.system.version" : {
                      "documentsToCopy" : 2,
                      "documentsCopied" : 2,
                      "indexes" : 1,
                      "fetchedBatches" : 1,
                      "start" : ISODate("2024-08-15T23:06:13.978Z"),
                      "end" : ISODate("2024-08-15T23:06:13.978Z"),
                      "elapsedMillis" : 66,
                      "receivedBatches" : 1
                   }
                },
                "config" : {
                   "collections" : 2,
                   "clonedCollections" : 2,
                   "start" : ISODate("2024-08-15T23:06:13.978Z"),
                   "end" : ISODate("2024-08-15T23:06:13.978Z"),
                   "elapsedMillis" : 198,
                   "config.transactions" : {
                      "documentsToCopy" : 0,
                      "documentsCopied" : 0,
                      "indexes" : 1,
                      "fetchedBatches" : 0,
                      "start" : ISODate("2024-08-15T23:06:13.978Z"),
                      "end" : ISODate("2024-08-15T23:06:13.978Z"),
                      "elapsedMillis" : 74,
                      "receivedBatches" : 0
                   },
                   "config.system.sessions" : {
                      "documentsToCopy" : 0,
                      "documentsCopied" : 0,
                      "indexes" : 2,
                      "fetchedBatches" : 0,
                      "start" : ISODate("2024-08-15T23:06:13.978Z"),
                      "end" : ISODate("2024-08-15T23:06:13.978Z"),
                      "elapsedMillis" : 124,
                      "receivedBatches" : 0
                   }
                },
                "test" : {
                   "collections" : 1,
                   "clonedCollections" : 1,
                   "start" : ISODate("2024-08-15T23:06:13.978Z"),
                   "end" : ISODate("2024-08-15T23:06:13.978Z"),
                   "elapsedMillis" : 47967,
                   "test.hugeindex" : {
                      "documentsToCopy" : 25000,
                      "documentsCopied" : 25000,
                      "indexes" : 2,
                      "fetchedBatches" : 21,
                      "start" : ISODate("2024-08-15T23:06:13.978Z"),
                      "end" : ISODate("2024-08-15T23:06:13.978Z"),
                      "elapsedMillis" : 47967,
                      "receivedBatches" : 21
                   }
                }
             }
          },
          "members" : [
             {
                "_id" : 0,
                "name" : "m1.example.net:27017",
                "health" : 0,
                "state" : 8,
                "stateStr" : "(not reachable/healthy)",
                "uptime" : 0,
                "optime" : {
                   "ts" : Timestamp(0, 0),
                   "t" : NumberLong(-1)
                },
                "optimeDurable" : {
                   "ts" : Timestamp(0, 0),
                   "t" : NumberLong(-1)
                },
                "optimeDate" : ISODate("1970-01-01T00:00:00Z"),
                "optimeDurableDate" : ISODate("1970-01-01T00:00:00Z"),
                "lastAppliedWallTime": ISODate("1970-01-01T00:00:00Z"),
                "lastDurableWallTime": ISODate("1970-01-01T00:00:00Z""),
                "lastHeartbeat" : ISODate("2024-08-15T23:06:13.978Z"),
                "lastHeartbeatRecv" : ISODate("2024-08-15T23:06:13.978Z"),
                "pingMs" : NumberLong(0),
                "lastHeartbeatMessage" : "Error connecting to m1.example.net:27017 (127.0.0.1:27018) :: caused by :: Connection refused",
                "syncSourceHost" : "",
                "syncSourceId" : -1,
                "infoMessage" : "",
                "configVersion" : 2
             },
             {
                "_id" : 1,
                "name" : "m2.example.net:27017",
                "health" : 1,
                "state" : 5,
                "stateStr" : "STARTUP2",
                "uptime" : 5297,
                "optime" : {
                   "ts" : Timestamp(0, 0),
                   "t" : NumberLong(-1)
                },
                "optimeDurable" : {
                   "ts" : Timestamp(0, 0),
                   "t" : NumberLong(-1)
                },
                "optimeDate" : ISODate("1970-01-01T00:00:00Z"),
                "lastAppliedWallTime": ISODate("1970-01-01T00:00:00Z"),
                "lastDurableWallTime": ISODate("1970-01-01T00:00:00Z"),
                "syncSourceHost" : "m1.example.net:27017",
                "syncSourceId" : 0,
                "infoMessage" : "",
                "configVersion" : 2,
                "configTerm" : 1,
                "self" : true,
                "lastHeartbeatMessage" : ""
             }
          ],
          "ok" : 1
       }
       ```

## Output

The `replSetGetStatus` command returns a document with the
following fields:

**`replSetGetStatus.set`**

The `set` value is the name of the replica set, configured in the
`replSetName` setting. This is the same value as
`_id` in `rs.conf()`.

**`replSetGetStatus.date`**

An ISODate formatted date and time that contains the current
time according to the server that processed the
`replSetGetStatus` command. Compare this to the values of
`replSetGetStatus.members[n].lastHeartbeat` to find the
operational latency between this server and the other members of the
replica set.

**`replSetGetStatus.myState`**

An integer between `0` and `10` that represents the replica
state of the current member.

**`replSetGetStatus.term`**

The election count for the replica set, as known to this replica set
member. The `term` is used by the
distributed consensus algorithm to ensure correctness.

**`replSetGetStatus.syncSourceHost`**

The `syncSourceHost` field holds the
hostname of the member from which this instance syncs.

If this instance is a primary,
`syncSourceHost` is an empty string and
the `syncSourceId` `-1`.

**`replSetGetStatus.syncSourceId`**

The `syncSourceId` field holds the
`replSetGetStatus.members[n]._id` of the member from which
this instance synchronizes.

If this instance is a primary,
`syncSourceHost` is an empty string and
the `syncSourceId` `-1`.

**`replSetGetStatus.heartbeatIntervalMillis`**

The frequency in milliseconds of the heartbeats.

**`replSetGetStatus.majorityVoteCount`**

The number of majority votes needed to elect a
new primary in an election.

**`replSetGetStatus.writeMajorityCount`**

The number of data-bearing voting members (i.e. not arbiters) needed
to fulfill write concern `"majority"`. Writes can only
be applied to data-bearing members.

For the calculation of `replSetGetStatus.writeMajorityCount`,
see calculating-majority-count.

**`replSetGetStatus.votingMembersCount`**

The number of members configured with `votes: 1`, including arbiters.

**`replSetGetStatus.writableVotingMembersCount`**

The number of *data-bearing* members configured with `votes:
1` (this does not include arbiters).

**`replSetGetStatus.optimes`**

The `optimes` field holds a document that contains optimes used to inspect replication progress. The `optimes` field 
includes the corresponding ISODate-formatted date strings for the various 
optimes.

Each optime value is a document that contains:

- `ts`, the Timestamp of
  the operation.

- `t`, the `term` in which the
  operation was originally generated on the primary.

**`replSetGetStatus.optimes.lastCommittedOpTime`**

Information, from the viewpoint of this member, regarding the
most recent operation that has been written to a majority of
replica set members.

**`replSetGetStatus.optimes.lastCommittedWallTime`**

The ISODate-formatted date string corresponding to
`lastCommittedOpTime`.

**`replSetGetStatus.optimes.readConcernMajorityOpTime`**

Information, from the viewpoint of this member, regarding the
most recent operation that can fulfill read concern
`"majority"` queries; i.e. the most recent
`lastCommittedOpTime` that can
fulfill `"majority"` queries.
`readConcernMajorityOpTime` is
either less than or equal to
`lastCommittedOpTime`.

**`replSetGetStatus.optimes.readConcernMajorityWallTime`**

The ISODate-formatted date string corresponding to
`readConcernMajorityOpTime`.

**`replSetGetStatus.optimes.appliedOpTime`**

Information, from the viewpoint of this member, regarding the
most recent operation that has been applied to this member of the
replica set.

**`replSetGetStatus.optimes.lastAppliedWallTime`**

The ISODate-formatted date string corresponding to
`appliedOpTime`.

**`replSetGetStatus.optimes.durableOpTime`**

Information, from the viewpoint of this member, regarding the
most recent operation that has been written to the journal of
this member of the replica set.

**`replSetGetStatus.optimes.lastDurableWallTime`**

The ISODate-formatted date string corresponding to
`durableOpTime`.

**`replSetGetStatus.lastStableRecoveryTimestamp`**

*For internal use only*

**`replSetGetStatus.electionCandidateMetrics`**

Metrics related to the election of the current primary.
`electionCandidateMetrics` is only available
on the primary or a candidate for election. For a candidate, the
metrics are unavailable after the candidate loses the election.

**`replSetGetStatus.electionCandidateMetrics.lastElectionReason`**

Reason the member called the election.

**`replSetGetStatus.electionCandidateMetrics.lastElectionDate`**

The date and time the member called the election.

**`replSetGetStatus.electionCandidateMetrics.electionTerm`**

The member's election count (i.e. `term`)
at the time it called the new election.

**`replSetGetStatus.electionCandidateMetrics.lastCommittedOpTimeAtElection`**

The most recent `majority-committed optime`, as seen by this
member, at the time it called the new election.

**`replSetGetStatus.electionCandidateMetrics.lastSeenOpTimeAtElection`**

The member's most recent `applied optime` at the time it called
the new election.

**`replSetGetStatus.electionCandidateMetrics.numVotesNeeded`**

The number of votes needed to win the election.

**`replSetGetStatus.electionCandidateMetrics.priorityAtElection`**

The member's `priority` at the time
it called the election.

**`replSetGetStatus.electionCandidateMetrics.electionTimeoutMillis`**

The replica set's configured
`electionTimeoutMillis` setting at the time of
the election.

**`replSetGetStatus.electionCandidateMetrics.priorPrimaryMemberId`**

The `members[n]._id` of the previous primary. If
there is no previous primary, then the field is not present.

**`replSetGetStatus.electionCandidateMetrics.targetCatchupOpTime`**

The newly-elected primary's target opTime for its catchup
process. Only when the newly-elected primary reaches the target
catchup opTime can it start accepting writes.

**`replSetGetStatus.electionCandidateMetrics.numCatchUpOps`**

The number of operations applied by the newly-elected primary as
it successfully concludes its catchup process.

**`replSetGetStatus.electionCandidateMetrics.newTermStartDate`**

The date and time at which the member's term as the primary
started (i.e. the date and time at which a `new term` entry was
written to the oplog).

**`replSetGetStatus.electionCandidateMetrics.wMajorityWriteAvailabilityDate`**

The date and time at which the write concern
`"majority"` became available after the election
for the replica set (the date and time when the ``new
term`` oplog entry was majority committed).

**`replSetGetStatus.electionParticipantMetrics`**

Metrics related to the latest election in which the member
participated.

**`replSetGetStatus.electionParticipantMetrics.votedForCandidate`**

A boolean which indicates whether the member voted for the
candidate calling the election.

**`replSetGetStatus.electionParticipantMetrics.electionTerm`**

The term of the election in which the member participated. The
term identifies the election associated with the participant
metrics.

**`replSetGetStatus.electionParticipantMetrics.lastVoteDate`**

An ISODate formatted date string that records when the
participant voted.

**`replSetGetStatus.electionParticipantMetrics.electionCandidateMemberId`**

The `members[n]._id` of the candidate calling the
election.

**`replSetGetStatus.electionParticipantMetrics.voteReason`**

The reason for the vote if the member did not vote for the candidate.
If the member voted for the candidate, the value is an empty string.

**`replSetGetStatus.electionParticipantMetrics.lastAppliedOpTimeAtElection`**

This member's latest applied optime at the time of the election.

The optime value is a document that contains the Timestamp (`ts`) and the term (`t`).

**`replSetGetStatus.electionParticipantMetrics.maxAppliedOpTimeInSet`**

The most recent applied optime for any member of this replica
set, as known by this member.

The optime value is a document that contains the Timestamp (`ts`) and the term (`t`).

**`replSetGetStatus.electionParticipantMetrics.priorityAtElection`**

The member's `priority` at the time of the election.

**`replSetGetStatus.electionParticipantMetrics.newTermStartDate`**

The date and time at which the elected primary's term started;
this corresponds to when the primary wrote the `new term` entry
to its oplog and not when the entry was added (i.e. replicated)
to the secondary's oplog.

The field is available for secondary members only. For the
primary, see
`replSetGetStatus.electionCandidateMetrics.newTermStartDate`
instead.

**`replSetGetStatus.electionParticipantMetrics.newTermAppliedDate`**

The date and time at which this secondary applied the ``new
term`` entry.

The field is available for secondary members only.

**`replSetGetStatus.initialSyncStatus`**

A document that provides information on the progress and status of
initial sync on this member.

**Important:** Availability

`replSetGetStatus.initialSyncStatus` metrics are only
available when run on a member during its initial sync (i.e.
`STARTUP2` state).

**`replSetGetStatus.initialSyncStatus.failedInitialSyncAttempts`**

The number of times the initial sync failed and had to restart on this
member.

**`replSetGetStatus.initialSyncStatus.maxFailedInitialSyncAttempts`**

The maximum number of times the initial sync can restart on this member before
the member shuts down.

**`replSetGetStatus.initialSyncStatus.initialSyncStart`**

The start timestamp of the initial sync for this member.

**`replSetGetStatus.initialSyncStatus.initialSyncEnd`**

The end timestamp of the initial sync for this member.

**`replSetGetStatus.initialSyncStatus.initialSyncElapsedMillis`**

The number of milliseconds between
`initialSyncStart` and
`initialSyncEnd`.

**`replSetGetStatus.initialSyncStatus.initialSyncAttempts`**

Array of documents where each document corresponds to a single
initial sync attempt. For example:

```javascript
"initialSyncAttempts" : [
   {
      "durationMillis" : 59539,
      "status" : "InvalidOptions: error fetching oplog during initial sync :: caused by :: Error while getting the next batch in the oplog fetcher :: caused by :: readConcern afterClusterTime value must not be greater than the current clusterTime. Requested clusterTime: { ts: Timestamp(0, 1) }; current clusterTime: { ts: Timestamp(0, 0) }",
      "syncSource" : "m1.example.net:27017",
      "rollBackId" : 1,                     
      "operationsRetried" : 120,            
      "totalTimeUnreachableMillis" : 52601  
   }
],
```

Each document contains the following information for the initial sync attempt:

| Field | Description |
|---|---|
| durationMillis | Duration in milliseconds of the initial sync attempt. |
| status | Exit status of the initial sync attempt. |
| syncSource | Sync source for the initial sync attempt. |
| rollBackId | The sync source's rollback identifier at the start of the initial sync attempt. `rollBackId` does not appear when using file copy based initial sync. |
| operationsRetried | Total number of all operation retry attempts. |
| totalTimeUnreachableMillis | Total time spent for retry operation attempts. |

See also
`failedInitialSyncAttempts`.

**`replSetGetStatus.initialSyncStatus.appliedOps`**

The number of ops that occurred after the initial sync started and were applied after cloning
the databases.

As part of the initial sync process, the member uses the oplog
to update its data set to reflect the current state of the
replica set.

**`replSetGetStatus.initialSyncStatus.initialSyncOplogStart`**

The start timestamp of the oplog application stage of the
initial sync where the
member applies changes that occurred after the initial sync
start.

As part of the initial sync process, the member uses the oplog
to update its data set to reflect the current state of the
replica set.

**`replSetGetStatus.initialSyncStatus.initialSyncOplogEnd`**

The end timestamp of the oplog application stage of the
initial sync where the
member applies changes that occurred after the initial sync
start.

As part of the initial sync process, the member uses the oplog
to update its data set to reflect the current state of the
replica set.

**`replSetGetStatus.initialSyncStatus.syncSourceUnreachableSince`**

The date and time at which the sync source became unreachable. 

Only present if the if sync source is unavailable during the
current initial sync.

**`replSetGetStatus.initialSyncStatus.currentOutageDurationMillis`**

The time in milliseconds that the sync source has been unavailable.

Only present if the if sync source is unavailable during the
current initial sync.

**`replSetGetStatus.initialSyncStatus.totalTimeUnreachableMillis`**

The total time in milliseconds that the member has been
unavailable during the current initial sync.

**`replSetGetStatus.initialSyncStatus.databases`**

Detail on the databases cloned during initial sync.

**`replSetGetStatus.initialSyncStatus.databases.databasesCloned`**

Number of databases cloned during initial sync.

**`replSetGetStatus.initialSyncStatus.databases.<dbname>`**

For each database, a document that returns information regarding
the progress of the cloning of that database.

```javascript
{
   "collections" : <number of collections to clone in the database>,
   "clonedCollections" : <number of collections cloned to date>,
   "start" : <start date and time for the database clone>,
   "end" : <end date and time for the database clone>,
   "elapsedMillis" : <duration of the database clone>,
   "<db>.<collection>" : {
      "documentsToCopy" : <number of documents to copy>,
      "documentsCopied" : <number of documents copied to date>,
      "indexes" :  <number of indexes>,
      "fetchedBatches" :  <number of batches of documents fetched to date>,
      "start" :  <start date and time for the collection clone>,
      "end" : <end date and time for the collection clone>,
      "elapsedMillis" : <duration of the collection clone>,
      "receivedBatches" : <number of batches of documents received to date> 
   }
}
```

**`replSetGetStatus.initialSyncStatus.method`**

**New in version:** 5.2

The method used for the initial sync.

If set to `logical`, the sync is a logical initial sync. If set to `fileCopyBased`, the
sync is a file copy based initial sync.  

**`replSetGetStatus.initialSyncStatus.approxTotalDataSize`**

The approximate size (in bytes) of all files to be synced during 
file copy based initial sync. 

This field only appears when using file copy based initial 
sync.
   

**`replSetGetStatus.initialSyncStatus.approxTotalBytesCopied`**

The total bytes already copied.

This field only appears when using file copy based initial 
sync.

**`replSetGetStatus.initialSyncStatus.totalInitialSyncElapsedMillis`**

The total time elapsed for the sync attempt in progress.

This field only appears when using file copy based initial 
sync.

**`replSetGetStatus.initialSyncStatus.remainingInitialSyncEstimatedMillis`**

The expected time remaining for the sync attempt in progress.

This field only appears when using file copy based initial 
sync.

**`replSetGetStatus.initialSyncStatus.initialBackupDataSize`**

The total size (in bytes) of the initial set of files to be synced.

This field only appears when using file copy based initial 
sync.

**`replSetGetStatus.initialSyncStatus.previousOplogEnd`**

The optime available in the previous backup cursor. 

This field only appears when using file copy based initial 
sync.

**`replSetGetStatus.initialSyncStatus.currentOplogEnd`**

The last optime guaranteed to be available in the current 
backup cursor. 

This field only appears when using file copy based initial 
sync.

**`replSetGetStatus.initialSyncStatus.syncSourceLastApplied`**

The optime of the last update applied at the sync source 
prior to the start of this backup cursor. 

This field only appears when using file copy based initial 
sync.

**`replSetGetStatus.initialSyncStatus.numExtensions`**

The number of times the sync has started a new backup cursor.

This field does not appear if a backup cursor has not started.

This field only appears when using file copy based initial 
sync.

**`replSetGetStatus.initialSyncStatus.extensionDataSize`**

The total bytes in the current extension. 

This field does not appear if there is no extension in progress.

This field only appears when using file copy based initial 
sync.
   

**`replSetGetStatus.initialSyncStatus.files`**

An array of files to be synced during file copy based initial 
sync.

This field only appears when using file copy based initial 
sync.

**`replSetGetStatus.initialSyncStatus.files[n].filePath`**

The path of the file relative to the root of the 
backup cursor.

This field only appears when using file copy based initial 
sync.

**`replSetGetStatus.initialSyncStatus.files[n].fileSize`**

The size of the file as reported by the backup cursor.

This field only appears when using file copy based initial 
sync.

**`replSetGetStatus.initialSyncStatus.files[n].bytesCopied`**

The number of bytes copied so far.

This field only appears when using file copy based initial 
sync.

**`replSetGetStatus.initialSyncStatus.files[n].extensionNumber`**

The number of the extension the file belongs 
to if this file is part of an extension.

This field only appears when using file copy based initial 
sync.

**`replSetGetStatus.members`**

The `members` field holds an array that contains a document for
every member in the replica set.

**`replSetGetStatus.members[n]._id`**

The identifier for the member.

**`replSetGetStatus.members[n].name`**

The name of the member.

**`replSetGetStatus.members[n].ip`**

The resolved IP address of the member. If the
`mongod` is unable to resolve the
`replSetGetStatus.members[n].name` to an IP address, the
return value is a BSON null. Otherwise, the returned value is a
string representation of the resolved IP address.

**`replSetGetStatus.members[n].self`**

A boolean that indicates if the member is the current
`mongod` instance.

The `self` field is only included in the document for the
current `mongod` instance, and as such, its value is always
`true`.

**`replSetGetStatus.members[n].health`**

A number that indicates if the member is up (`1`) or down
(`0`).

**`replSetGetStatus.members[n].state`**

An integer between `0` and `10` that represents the
replica state of the member.

**`replSetGetStatus.members[n].stateStr`**

A string that describes `state`.

**`replSetGetStatus.members[n].uptime`**

For the member on which the `replSetGetStatus` command
is run, `uptime` is the 
the number of seconds the member has been online.

For the other members, `uptime`
is the number of seconds the member has been in continuous
communication with the member on which the
`replSetGetStatus` command was run.

**`replSetGetStatus.members[n].optime`**

Information regarding the last operation from the operation log that
this member has applied.

`optime` returns a document that contains:

- `ts`, the Timestamp of
  the last operation applied to this member of the replica set
  from the oplog.

- `t`, the `term` in which the last
  applied operation was originally generated on the primary.

**`replSetGetStatus.members[n].optimeDurable`**

Information regarding the last operation from the operation log
that this member has applied to its journal.

`optimeDurable` returns a document that contains:

- `ts`, the Timestamp of
  the operation.

- `t`, the `term` in which this
  operation was originally generated on the primary.

**`replSetGetStatus.members[n].optimeDate`**

An ISODate formatted date string that contains the last
entry from the oplog that this member applied. If this
differs significantly from
`lastHeartbeat` this member is
either experiencing "replication lag" *or* there have not been any
new operations after the last update. Compare
`members.optimeDate` between all of the members of the set.

**`replSetGetStatus.members[n].optimeDurableDate`**

An ISODate formatted date string that contains the last
entry from the oplog that this member applied to its
journal.

**`replSetGetStatus.members[n].lastAppliedWallTime`**

An ISODate formatted date string reflecting the wall clock
time at which the last operation applied by this member of the 
replica set was applied on the primary node.

**`replSetGetStatus.members[n].lastDurableWallTime`**

An ISODate formatted date string reflecting the wall clock
time at which the last operation written to this member's journal 
was first applied on the primary node.

**`replSetGetStatus.members[n].electionTime`**

For the current primary, information regarding the election
Timestamp from the
operation log. See /core/replica-set-high-availability for more
information about elections.

**`replSetGetStatus.members[n].electionDate`**

For the current primary, an ISODate formatted date string
that contains the election date. See
/core/replica-set-high-availability for more information about
elections.

**`replSetGetStatus.members[n].lastHeartbeat`**

An ISODate formatted date and time that contains the last
time the server that processed the `replSetGetStatus`
command received a response from a heartbeat that it sent to this
member (`members[n]`).
Compare this value to the values of the `date` and
`lastHeartbeatRecv` fields to
track latency between these replica set members.

This value is only available for replica set members other than the server specified by `replSetGetStatus.members[n].self`.

**`replSetGetStatus.members[n].lastHeartbeatRecv`**

An ISODate formatted date and time that contains the last
time the server that processed the `replSetGetStatus`
command received a heartbeat request from this member
(`members[n]`).
Compare this value to the values of the
`date` and
`lastHeartbeat` fields to track
latency between these replica set members.

This value is only available for replica set members other than the server specified by `replSetGetStatus.members[n].self`.

**`replSetGetStatus.members[n].lastHeartbeatMessage`**

When the last heartbeat included an extra message, the
`lastHeartbeatMessage` contains
a string representation of that message.

**`replSetGetStatus.members[n].pingMs`**

The `pingMs` represents the number of milliseconds (ms) that a
round-trip packet takes to travel between the remote member and
the local instance.

This value does not appear for the member that returns the
`rs.status()` data.

**`replSetGetStatus.members[n].syncSourceHost`**

The `syncSourceHost` field
holds the hostname of the member from which this instance syncs.

If the `replSetGetStatus.members[n]` is a primary,
`syncSourceHost` is an empty
string and the `syncSourceId`
`-1`.

**`replSetGetStatus.members[n].syncSourceId`**

The `syncSourceId` field holds
the `replSetGetStatus.members[n]._id` value of the
`syncSourceHost`.

If the `replSetGetStatus.members[n]` is a primary,
`syncSourceHost` is an empty
string and the `syncSourceId`
`-1`.

**`replSetGetStatus.members[n].configVersion`**

The `configVersion` value is the `replica
set configuration version`.

**`replSetGetStatus.tooStale`**

A boolean which indicates that a replica set member has fallen
too far behind the primary's oplog and is stuck in
the `RECOVERING` state. This field is only included in the
`replSetGetStatus` output if its value is `true`.

See also command-response for details on the `ok` status
field, the `operationTime` field and the `$clusterTime` field.

**`replSetGetStatus.optime`**

Present after the removal of a member from the replica set. Provides the
optime of the last oplog entry applied by the removed member.

**`replSetGetStatus.optimeDate`**

Present after the removal of a member from the replica set. Provides the
ISODate formatted string of the optime of the last oplog entry applied
by the removed member.
