<!-- Converted from reference/command/balancerCollectionStatus.txt (reStructuredText). Includes are inlined. -->

# balancerCollectionStatus

## Definition

**`balancerCollectionStatus`**

Returns a document that contains information about whether the
chunks of a sharded collection are balanced (i.e. do not need to be
moved) as of the time the command is run or need to be moved because
of draining shards, zone violation or imbalance of chunks across
shards.

You can only issue the `balancerCollectionStatus` against the
`admin` database.

   helper method

**Tip:**

In `mongosh`, this command can also be run through the `sh.balancerCollectionStatus`.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in serverless instances.
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
     balancerCollectionStatus: "<db>.<collection>" 
   } 
)
```

Specify the full namespace (`"<db>.<collection>"`) of the sharded collection.

`mongosh` provides a wrapper method
`sh.balancerCollectionStatus()`.

## Access Control

When running with access control, the user must have the
`enableSharding` privilege actions on database
and/or collection to run the
command. That is, a user must have a role that grants
the following privilege:

```javascript
{ resource: { db: <database>, collection: <collection> }, actions: [ "enableSharding" ] }
```

The built-in `clusterManager` role provides the appropriate
privileges.

## Output Document

The following is an example of a document returned by the command:

```json
{
   "chunkSize": Long("128"),
   "balancerCompliant" : false,
   "firstComplianceViolation" : "chunksImbalance",
   "ok" : 1,
   "operationTime" : Timestamp(1583192967, 16),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1583192967, 16),
      "signature" : {
         "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
         "keyId" : NumberLong(0)
      }
   }
}
```

   

| Field | Description |
|---|---|
| `"chunkSize"` | .. versionadded:: 5.3 An integer that indicates the chunk size in megabytes. |
| `"balancerCompliant"` | A boolean that indicates whether the chunks do not need to be moved (`true`) or need to be moved (`false`). |
| `"firstComplianceViolation"` | A string that indicates the reason chunks for this namespace need to be moved. The field is only available if `"balancerCompliant"` is `false`. Possible values are: `"chunksImbalance"` The difference in the number of chunks between the shard with the most chunks for the collection and the shard with the fewest chunks for the collection exceed the migration threshold. `"defragmentingChunks"` The queried namespace is currently going through the chunk defragmentation process. Defragmentation can be triggered by the `configureCollectionBalancing` command. `"draining"` A remove shard operation is in progress and MongoDB must drain chunks off the removed shard to other shards. `"zoneViolation"` Chunks violate the defined zone ranges for a shard. This field only returns information on the *first* violation observed by MongoDB. There may be additional pending chunk migrations due to a different reason than the one reported in `firstComplianceViolation`. |
| `"details"` | An object containing information on the ongoing defragmentation process. This object indicates the current phase of the defragmentation and how many chunks are left to process in that phase. For example output, see balancer-collection-status-defrag-output-command. This field is only returned when `firstComplianceViolation` is `defragmentingChunks`. |

In addition to the command-specific return fields, the command also
returns the `ok` status field, the `operationTime` field, and the
`$clusterTime` field for the operation. For details on these fields,
see command-response.

## Examples

To check whether the chunks of a sharded collection `test.contacts`
is currently in balance, connect to a `mongos` instance
and issue the following command:

```javascript
db.adminCommand( { balancerCollectionStatus: "test.contacts" } )
```

If the chunks for the collection do not need to be moved, the command
returns an output similar to the following:

```javascript
{
   "chunkSize": Long("128"),
   "balancerCompliant" : true,
   "ok" : 1,
   "operationTime" : Timestamp(1583193238, 1),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1583193238, 1),
      "signature" : {
         "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
         "keyId" : NumberLong(0)
      }
   }
}
```

### Ongoing Defragmentation Process

If the queried namespace is going through chunk defragmentation, the
`balancerCollectionStatus` command returns output similar to the following:

```javascript
{
   "chunkSize": Long("128"),
   "balancerCompliant": false,
   "firstComplianceViolation": "defragmentingChunks",
   "details": {
      "currentPhase": "moveAndMergeChunks",
      "progress": { "remainingChunksToProcess": 1 }
   }
}
```

**Note:**

Chunk defragmentation occurs in multiple phases. The `progress` field
only pertains to the current phase.
