<!-- Converted from reference/method/sh.balancerCollectionStatus.txt (reStructuredText). Includes are inlined. -->

# sh.balancerCollectionStatus() (mongosh method)

## Definition

**`sh.balancerCollectionStatus(namespace)`**

Returns a document that contains information about whether the
chunks of a sharded collection are balanced (i.e. do not need to be
moved) as of the time the command is run or need to be moved because
of draining shards, zone violation or imbalance of chunks across
shards. 

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `balancerCollectionStatus` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

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

The `sh.balancerCollectionStatus` has the following form:

```javascript
sh.balancerCollectionStatus( <namespace> )
```

### Parameter

The `sh.balancerCollectionStatus()` method takes the following parameter:

| Parameter | Type | Description |
|---|---|---|
| namespace | String | .. _method-balancercollectionstatus-namespace: The namespace of the collection to shard in the form `"<database>.<collection>"`. |

## Access Control

When running with access control, the user must have the
`enableSharding` privilege actions on database
and/or collection to run the
method. That is, a user must have a role that grants the
following privilege:

```javascript
{ resource: { db: <database>, collection: <collection> }, actions: [ "enableSharding" ] }
```

The built-in `clusterManager` role provides the appropriate
privileges.

## Examples

To check whether the chunks of a sharded collection `test.contacts`
is currently in balance, connect to a `mongos` instance
and issue the following:

```javascript
sh.balancerCollectionStatus("test.contacts")
```

If the chunks for the collection do not need to be moved, the method
returns an output similar to the following:

```javascript
{
   "balancerCompliant" : true,
   "ok" : 1,
   "operationTime" : Timestamp(1583193238, 1),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1583193238, 1),
      "signature" : {
         "hash" : BinData(0,"AAAAAAAAAAAAAAAAAAAAAAAAAAA="),
         "keyId" : Long(0)
      }
   }
}
```

### Ongoing Defragmentation Process

If the queried namespace is going through chunk defragmentation, the
`sh.balancerCollectionStatus` method returns output similar to the following:

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

For the description of the output, see balancerCollectionStatus
Output.
