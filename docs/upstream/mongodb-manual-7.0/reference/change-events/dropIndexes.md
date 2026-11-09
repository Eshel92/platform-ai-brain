<!-- Converted from reference/change-events/dropIndexes.txt (reStructuredText). Includes are inlined. -->

# dropIndexes Event

## Synopsis

**`dropIndexes`**

**New in version:** 6.0

A `dropIndexes` event occurs when an index is dropped from the collection and
the change stream has the showExpandedEvents
option set to `true`.

## Descriptions

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
  - .. include:: /includes/change-stream/ns.db

* - `ns.coll`
  - string
  - .. include:: /includes/change-stream/ns.coll

* - `operationDescription`
  - document
  - .. include:: /includes/change-stream/operationDescription

* - | `operationDescription.`
    | `indexes`
  - array
  - An array of documents listing the indexes that were dropped
    by the operation.

    **New in version:** 6.0

* - `operationType`
  - string
  - .. include:: /includes/change-stream/operationType

    Returns a value of `dropIndexes` for these change events.

* - `txnNumber`
  - NumberLong
  - .. include:: /includes/change-stream/txnNumber

* - `wallTime`
  - ISODate
  - .. include:: /includes/change-stream/wallTime

## Example

The following example shows a `dropIndexes` event:

```json
{
   "_id": { <ResumeToken> },
   "operationType": "dropIndexes",
   "clusterTime": <Timestamp>
   "collectionUUID": <uuid>,
   "wallTime": <isodate>,
   "ns": {
      "db": "test",
      "coll": "authors" },
   "operationDescription": {
      "indexes": [
         { "v": 2, "key": { "name": 1 }, "name": "name_1" }
      ]
   }
}
```
