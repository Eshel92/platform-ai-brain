<!-- Converted from reference/change-events/drop.txt (reStructuredText). Includes are inlined. -->

# drop Event

## Synopsis

**`drop`**

A `drop` event occurs when a collection is dropped from a database. 

## Description

| Field | Type | Description |
|---|---|---|
| `_id` | Document | .. include:: /includes/change-stream/id |
| `clusterTime` | Timestamp | .. include:: /includes/change-stream/clusterTime |
| `collectionUUID` | UUID | .. include:: /includes/change-stream/collectionUUID-views |
| `lsid` | document | .. include:: /includes/change-stream/lsid |
| `ns` | document | .. include:: /includes/change-stream/ns |
| `ns.coll` | string | .. include:: /includes/change-stream/ns.coll |
| `ns.db` | string | .. include:: /includes/change-stream/ns.db |
| `operationType` | string | .. include:: /includes/change-stream/operationType Returns a value of `drop` for these change events. |
| `txnNumber` | NumberLong | .. include:: /includes/change-stream/txnNumber |
| `wallTime` | ISODate | .. include:: /includes/change-stream/wallTime |

## Example

The following example illustrates a `drop` event:

```json
{
   "_id": { <Resume Token> },
   "operationType": "drop",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>,
   "ns": {
      "db": "engineering",
      "coll": "users"
   }
}
```

A `drop` event leads to an `invalidate` event for change streams opened 
against its own `ns` collection.
