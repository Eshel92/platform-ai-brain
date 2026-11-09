<!-- Converted from reference/change-events/dropDatabase.txt (reStructuredText). Includes are inlined. -->

# dropDatabase Event

## Synopsis

**`dropDatabase`**

A `dropDatabase` event occurs when a database is dropped. 

## Description

| Field | Type | Description |
|---|---|---|
| `_id` | Document | .. include:: /includes/change-stream/id |
| `clusterTime` | Timestamp | .. include:: /includes/change-stream/clusterTime |
| `lsid` | document | .. include:: /includes/change-stream/lsid |
| `ns` | document | .. include:: /includes/change-stream/ns |
| `ns.db` | string | .. include:: /includes/change-stream/ns.db |
| `operationType` | string | .. include:: /includes/change-stream/operationType Returns a value of `dropDatabase` for these change events. |
| `txnNumber` | NumberLong | .. include:: /includes/change-stream/txnNumber |
| `wallTime` | ISODate | .. include:: /includes/change-stream/wallTime |

## Example

The following example illustrates a `dropDatabase` event:

```json
{
   "_id": { <Resume Token> },
   "operationType": "dropDatabase",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>,
   "ns": {
      "db": "engineering"
   }
}
```

A `dropDatabase` command generates a
drop event for each collection in
the database before generating a `dropDatabase` event for the database.

A `dropDatabase` event leads to an `invalidate` event for 
change streams opened against its own `ns.db` database.
