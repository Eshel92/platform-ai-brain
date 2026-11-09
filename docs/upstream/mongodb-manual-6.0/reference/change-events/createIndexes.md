<!-- Converted from reference/change-events/createIndexes.txt (reStructuredText). Includes are inlined. -->

# createIndexes Event

## Summary

**`createIndexes`**

**New in version:** 6.0

A `createIndexes` event occurs when an index is created on the collection 
and the change stream has the showExpandedEvents option set to `true`.

## Description

* - Field
  - Type
  - Description

* - `_id`
  - Document
  - .. include:: /includes/change-stream/id

* - `clusterTime`
  - Timestamp
  - .. include:: /includes/change-stream/clusterTime

* - `collectionUUID`
  - UUID
  - .. include:: /includes/change-stream/collectionUUID

* - `lsid`
  - document
  - .. include:: /includes/change-stream/lsid

* - `ns`
  -  document
  - .. include:: /includes/change-stream/ns

* - `ns.db`
  - string
  - .. include:: /includes/change-stream/ns.db.rst

* - `ns.coll`
  - string
  - .. include:: /includes/change-stream/ns.coll.rst

* - `operationDescription`
  - document
  - .. include:: /includes/change-stream/operationDescription

* - | `operationDescription.`
    | `indexes`
  - array
  - An array of documents listing the indexes that were created 
    by the operation.

    **New in version:** 6.0

* - `operationType`
  - string
  - .. include:: /includes/change-stream/operationType

    Returns a value of `createIndexes` for these change events.

* - `txnNumber`
  - NumberLong
  - .. include:: /includes/change-stream/txnNumber

* - `wallTime`
  - ISODate
  - .. include:: /includes/change-stream/wallTime

## Example

The following example shows a `createIndexes` event:

```json
{
   "_id": { <ResumeToken> },
   "operationType": "createIndexes",
   "clusterTime": Timestamp({ t: 1651257835, i: 1 }),
   "collectionUUID": UUID("06bced37-7cc8-4267-96aa-a58a422153d8"),
   "wallTime": ISODate("2022-04-29T18:43:55.160Z"),
   "ns": {
      "db": "test",
      "coll": "authors"
   },
   "operationDescription": {
      "indexes": [
         { "v": 2, "key": { "name": 1 }, "name": "name_1" }
      ]
   }
}
```
