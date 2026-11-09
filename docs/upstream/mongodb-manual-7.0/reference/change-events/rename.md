<!-- Converted from reference/change-events/rename.txt (reStructuredText). Includes are inlined. -->

# `rename` Event

## Summary

**`rename`**

A `rename` event occurs when a collection is renamed.

## Description

| Field | Type | Description |
|---|---|---|
| `_id` | Document | .. include:: /includes/change-stream/id |
| `clusterTime` | Timestamp | .. include:: /includes/change-stream/clusterTime |
| `collectionUUID` | UUID | .. include:: /includes/change-stream/collectionUUID |
| `lsid` | document | .. include:: /includes/change-stream/lsid |
| `ns` | document | .. include:: /includes/change-stream/ns |
| `ns.db` | string | .. include:: /includes/change-stream/ns.db |
| `ns.coll` | string | .. include:: /includes/change-stream/ns.coll |
| `operationDescription` | document | .. include:: /includes/change-stream/operationDescription |
| \| `operationDescription.` \| `dropTarget` | UUID | .. include:: /includes/change-stream/od-dropTarget |
| \| `operationDescription.` \| `to` | document | .. include:: /includes/change-stream/od-to |
| \| `operationDescription.` \| `to.coll` | document | .. include:: /includes/change-stream/od-to-coll |
| \| `operationDescription.` \| `to.db` | document | .. include:: /includes/change-stream/od-to-db |
| `operationType` | string | .. include:: /includes/change-stream/operationType Returns a value of `rename` for these change events. |
| `to` | document | .. include:: /includes/change-stream/to |
| `to.coll` | document | .. include:: /includes/change-stream/to.coll |
| `to.db` | document | .. include:: /includes/change-stream/to.db |
| `txnNumber` | NumberLong | .. include:: /includes/change-stream/txnNumber |
| `wallTime` | ISODate | .. include:: /includes/change-stream/wallTime |

## Behavior

### Expanded Event Information

**Changed in version:** 6.0

Starting in MongoDB 6.0, when the showExpandedEvents option is set to `true` for the change 
stream, the `rename` event includes an `operationDescription` document.
This document provides a `to` field showing the changed database and
collection and a `dropTarget` field indicating whether the `rename`
operation removed the collection before the rename.

## Example

The following example illustrates a `rename` event:

```json
{
   "_id": { <Resume Token> },
   "operationType": "rename",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>,
   "ns": {
      "db": "engineering",
      "coll": "users"
   },
   "to": {
      "db": "engineering",
      "coll": "people"
   },
   "operationDescription": {
      "to": {
         "db": "engineering",
         "coll": "people"
      }
   }
}
```

A `rename` event leads to an
invalidate event for change streams opened
against its `ns` collection or `to` collection.
