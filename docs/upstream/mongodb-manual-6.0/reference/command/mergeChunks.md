<!-- Converted from reference/command/mergeChunks.txt (reStructuredText). Includes are inlined. -->

# mergeChunks

## Definition

**`mergeChunks`**

For a sharded collection, `mergeChunks` combines
contiguous chunk ranges on a shard into a single
chunk. Issue the `mergeChunks` command on the `admin` database from a
`mongos` instance.

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
     mergeChunks: <namespace>,
     bounds : [ 
       { <shardKeyField>: <minFieldValue> },
       { <shardKeyField>: <maxFieldValue> } 
     ] 
   } 
)
```

For compound shard keys, you must include the full shard key in the
`bounds` specification. For example, if the shard key is ``{ x: 1, y:
1 }``, `mergeChunks` has the following form:

```javascript
db.adminCommand( 
   { 
     mergeChunks: <namespace>,
     bounds: [ 
       { x: <minValue>, y: <minValue> },
       { x: <maxValue>, y: <maxValue> } 
     ] 
   } 
 )
```

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `mergeChunks` | namespace | The fully qualified namespace of the collection where both chunks exist. Namespaces take form of `<database>.<collection>`. |
| `bounds` | array | An array that contains the minimum and maximum key values of the new chunk. |

       

## Access Control

On deployments running with `authorization`, the
built-in role `clusterManager` provides the required
privileges.

## Behavior

**Note:**

Use the `mergeChunks` only in special circumstances. For
instance, when cleaning up your sharded cluster after removing
many documents.

In order to successfully merge chunks, the following *must* be true:

- In the `bounds` field, `<minkey>` and `<maxkey>` must correspond to
  the lower and upper bounds of the chunks to merge.

- The chunks must reside on the same shard.

- The chunks must be contiguous.

`mergeChunks` returns an error if these conditions are not
satisfied.

## Return Messages

On success, `mergeChunks` returns this document:

```javascript
{
  "ok" : 1,
  "$clusterTime" : {
     "clusterTime" : Timestamp(1510767081, 1),
     "signature" : {
         "hash" : BinData(0,"okKHD0QuzcpbVQg7mP2YFw6lM04="),
         "keyId" : NumberLong("6488693018630029321")
      }
  },
  "operationTime" : Timestamp(1510767081, 1)
}
```

### Another Operation in Progress

`mergeChunks` returns the following error message if another
metadata operation is in progress on the `chunks` collection:

```none
errmsg: "The collection's metadata lock is already taken."
```

If another process, such as balancer process, changes metadata while
`mergeChunks` is running, you may see this error. You can
retry the `mergeChunks` operation without side effects.

### Chunks on Different Shards

If the input chunks are not on the same shard,
`mergeChunks` returns an error similar to the following:

```javascript
{
  "ok" : 0,
  "errmsg" : "could not merge chunks, collection test.users does not contain a chunk ending at { username: \"user63169\" }",
  "$clusterTime" : {
     "clusterTime" : Timestamp(1510767081, 1),
     "signature" : {
         "hash" : BinData(0,"okKHD0QuzcpbVQg7mP2YFw6lM04="),
         "keyId" : NumberLong("6488693018630029321")
      }
  },
  "operationTime" : Timestamp(1510767081, 1)
}
```

### Noncontiguous Chunks

If the input chunks are not contiguous,
`mergeChunks` returns an error similar to the following:

```javascript
{
  "ok" : 0,
  "errmsg" : "could not merge chunks, collection test.users has more than 2 chunks between [{ username: \"user29937\" }, { username: \"user49877\" })"
  "$clusterTime" : {
     "clusterTime" : Timestamp(1510767081, 1),
     "signature" : {
         "hash" : BinData(0,"okKHD0QuzcpbVQg7mP2YFw6lM04="),
         "keyId" : NumberLong("6488693018630029321")
      }
  },
  "operationTime" : Timestamp(1510767081, 1)

}
```
