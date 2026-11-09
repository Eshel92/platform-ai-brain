<!-- Converted from reference/change-events/insert.txt (reStructuredText). Includes are inlined. -->

# insert Event

## Summary

**`insert`**

An `insert` event occurs when an operation adds documents to a collection.

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

    The `collectionUUID` field is only included if the change stream is
    created with the `showExpandedEvents` field set to `true`. For
    details, see showExpandedEvents.

* - `documentKey`
  - document
  - .. include:: /includes/change-stream/documentKey

* - `fullDocument`
  - document
  - The document created by the operation.

    **Changed in version:** 6.0

    Starting in MongoDB 6.0, if you set the `changeStreamPreAndPostImages` option
    using `db.createCollection()`, `create`, or
    `collMod`, then the `fullDocument` field shows the document after
    it was inserted, replaced, or updated (the document post-image). 
    `fullDocument` is always included for `insert` events.

* - `lsid`
  - document
  - .. include:: /includes/change-stream/lsid

* - `ns`
  - document
  - .. include:: /includes/change-stream/ns

* - `ns.coll`
  - string
  - .. include:: /includes/change-stream/ns.coll

* - `ns.db`
  - string
  - .. include:: /includes/change-stream/ns.db

* - `operationType`
  - string
  - .. include:: /includes/change-stream/operationType

    Returns a value of `insert` for these change events.

* - `txnNumber`
  - NumberLong
  - .. include:: /includes/change-stream/txnNumber

* - `wallTime`
  - ISODate
  - .. include:: /includes/change-stream/wallTime

## Behavior

### Update Operations

The `update` command can produce different change
events (not just `update`) depending on the actual
changes it makes to the collection. 

| Change Event | Description |
|---|---|
| `update` | The update operation modified an existing document. |
| `replace` | The update operation replaced the document or produced a diff that was more verbose than the original document, causing MongoDB to replace it. |
| `insert` | The update operation attempted to update a document that doesn't exist and instead added the document to the collection. This only occurs when the update runs with the `upsert` option enabled. |

## Example

The following example illustrates an `insert` event:

```json
{
   "_id": { <Resume Token> },
   "operationType": "insert",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>,
   "ns": {
      "db": "engineering",
      "coll": "users"
   },
   "documentKey": {
      "userName": "alice123",
      "_id": ObjectId("599af247bb69cd89961c986d")
   },
   "fullDocument": {
      "_id": ObjectId("599af247bb69cd89961c986d"),
      "userName": "alice123",
      "name": "Alice"
   }
}
```

The `documentKey` field includes both the `_id` and the `userName`
field. This indicates that the `engineering.users` collection is sharded,
with a shard key on `userName` and `_id`.

The `fullDocument` document represents the version of the document at the
time of the insert.
