<!-- Converted from reference/change-events/shardCollection.txt (reStructuredText). Includes are inlined. -->

# `shardCollection` Event

## Summary

**`shardCollection`**

**New in version:** 6.0

A `shardCollection` event occurs when a collection is sharded.

## Description

| Field | Type | Description |
|---|---|---|
| `_id` | Document | .. include:: /includes/change-stream/id |
| `clusterTime` | Timestamp | .. include:: /includes/change-stream/clusterTime |
| `collectionUUID` | UUID | .. include:: /includes/change-stream/collectionUUID |
| `lsid` | document | .. include:: /includes/change-stream/lsid |
| `ns` | document | .. include:: /includes/change-stream/ns |
| `ns.coll` | string | .. include:: /includes/change-stream/ns.coll |
| `ns.db` | string | .. include:: /includes/change-stream/ns.db |
| `operationDescription` | document | .. include:: /includes/change-stream/operationDescription |
| \| `operationDescription.` \| `numInitialChunks` | long | .. include:: /includes/change-stream/od-numInitialChunks |
| \| `operationDescription.` \| `presplitHashedZones` | boolean | .. include:: /includes/change-stream/od-presplitHashedZones |
| \| `operationDescription.` \| `shardKey` | document | .. include:: /includes/change-stream/od-shardKey |
| \| `operationDescription.` \| `unique` | boolean | .. include:: /includes/change-stream/od-unique |
| `operationType` | string | .. include:: /includes/change-stream/operationType Returns a value of `shardCollection` for these change events. |
| `txnNumber` | NumberLong | .. include:: /includes/change-stream/txnNumber |
| `wallTime` | ISODate | .. include:: /includes/change-stream/wallTime |

## Example

The following example shows a `shardCollection` event:

```json
{
   "_id": { <ResumeToken> },
   "operationType": "shardCollection",
   "clusterTime": Timestamp({ t: 1654894852, i: 52 }),
   "collectionUUID": UUID("98046a1a-b649-4e5b-9c75-67594221ce19"),
   "wallTime": ISODate("2022-06-10T21:00:52.854Z"),
   "ns": {
      "db": "test",
      "coll": "authors"
   },
   "operationDescription": {
      "shardKey": { "age": "hashed" },
      "unique": false,
      "numInitialChunks": Long("0"),
      "presplitHashedZones": false
   }
}
```
