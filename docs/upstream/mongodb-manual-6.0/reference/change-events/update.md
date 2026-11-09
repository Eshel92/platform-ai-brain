<!-- Converted from reference/change-events/update.txt (reStructuredText). Includes are inlined. -->

# `update` Event

## Summary

**`update`**

An `update` event occurs when an operation updates a document
in a collection.

**Note:** Disambiguation

To learn more about events that occur when collection options are
modified, see the `modify` event.

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

* - `documentKey`
  - document
  - .. include:: /includes/change-stream/documentKey

* - `fullDocument`
  - document
  - .. include:: /includes/change-stream/fullDocument

    This field only appears if you configured the change stream with 
    `fullDocument` set to `updateLookup`. When you configure the change stream
    with `updateLookup`, the field represents the current 
    majority-committed version of the document modified by the update operation.
    The document may differ from the changes described in 
    updateDescription if any other 
    majority-committed operations have modified the document between the original 
    update operation and the full document lookup.

    For more information, see Lookup Full Document for Update Operations.

    **Changed in version:** 6.0

    Starting in MongoDB 6.0, if you set the `changeStreamPreAndPostImages` option
    using `db.createCollection()`, `create`, or
    `collMod`, then the `fullDocument` field shows the document after
    it was inserted, replaced, or updated (the document post-image). 
    `fullDocument` is always included for `insert` events.

* - `fullDocumentBeforeChange`
  - document
  - .. include:: /includes/change-stream/fullDocumentBeforeChange

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

    Returns a value of `update` for these change events.

* - `updateDescription`
  - document
  - .. include:: /includes/change-stream/updateDescription

* - | `updateDescription.`
    | `removedFields`
  - array
  - .. include:: /includes/change-stream/ud-removedFields

* - | `updateDescription.`
    | `truncatedArrays`
  - array 
  - .. include:: /includes/change-stream/ud-truncatedArrays

* - | `updateDescription.`
    | `truncatedArrays.`
    | `field`
  - string
  - .. include:: /includes/change-stream/ud-ta-field

* - | `updateDescription.`
    | `truncatedArrays.`
    | `newSize`
  - integer
  - .. include:: /includes/change-stream/ud-ta-newSize

* - | `updateDescription.`
    | `updatedFields`
  - document
  - .. include:: /includes/change-stream/ud-updatedFields

* - `txnNumber`
  - NumberLong
  - .. include:: /includes/change-stream/txnNumber

* - `wallTime`
  - ISODate
  - .. include:: /includes/change-stream/wallTime

## Behavior

### Document Pre- and Post-Images

Starting in MongoDB 6.0, you see a `fullDocumentBeforeChange`
document with the fields before the document was changed (or deleted)
if you perform these steps:

#. Enable the new `changeStreamPreAndPostImages` field for a
   collection using `db.createCollection()`,
   `create`, or `collMod`.

#. Set `fullDocumentBeforeChange` to `"required"` or
   `"whenAvailable"` in `db.collection.watch()`.

Example `fullDocumentBeforeChange` document in the change stream
output:

```json
"fullDocumentBeforeChange" : {
   "_id" : ObjectId("599af247bb69cd89961c986d"), 
   "userName" : "alice123",
   "name" : "Alice Smith"
}
```

For complete examples with the change stream output, see
db.collection.watch-change-streams-pre-and-post-images-example.

Pre- and post-images are not available for a change stream event if the images were:

- Not enabled on the collection at the time of a document update or
  delete operation.

- Removed after the pre- and post-image retention time set in
  `expireAfterSeconds`.

  - The following example sets `expireAfterSeconds` to `100`
    seconds on an entire cluster:

    ```javascript
    use admin
    db.runCommand( {
       setClusterParameter:
          { changeStreamOptions: {
             preAndPostImages: { expireAfterSeconds: 100 }
          } }
    } )
    ```

  - The following example returns the current `changeStreamOptions`
    settings, including `expireAfterSeconds`:

    ```javascript
    db.adminCommand( { getClusterParameter: "changeStreamOptions" } )
    ```

  - Setting `expireAfterSeconds` to `off` uses the default retention
    policy: pre- and post-images are retained until the corresponding
    change stream events are removed from the oplog.

  - If a change stream event is removed from the oplog, then the
    corresponding pre- and post-images are also deleted regardless of
    the `expireAfterSeconds` pre- and post-image retention time.

Additional considerations:

- Enabling pre- and post-images consumes storage space and adds
  processing time. Only enable pre- and post-images if you need them.

- Limit the change stream event size to less than 16 mebibytes. To limit
  the event size, you can:

  - Limit the document size to 8 megabytes. You can request pre- and
    post-images simultaneously in the change stream output if other change stream event fields like
    `updateDescription` are not large.

  - Request only post-images in the change stream output for documents
    up to 16 mebibytes if other change stream event fields like
    `updateDescription` are not large.

  - Request only pre-images in the change stream output for documents up
    to 16 mebibytes if:

    - document updates affect only a small fraction of the document
      structure or content, *and*

    - do not cause a `replace` change event. A `replace` event
      always includes the post-image.

- To request a pre-image, you set `fullDocumentBeforeChange` to
  `required` or `whenAvailable` in `db.collection.watch()`.
  To request a post-image, you set `fullDocument` using the same
  method.

- Pre-images are written to the `config.system.preimages` collection.

  - The `config.system.preimages` collection may become large. To
    limit the collection size, you can set `expireAfterSeconds`
    time for the pre-images as shown earlier.

  - Pre-images are removed asynchronously by a background process.

**Important:** Backward-Incompatible Feature

Starting in MongoDB 6.0, if you are using document pre- and post-images
for change streams, you must disable
changeStreamPreAndPostImages for each collection using
the `collMod` command before you can downgrade to an earlier
MongoDB version.

**See also:**

- For change stream events and output, see
  change-stream-output.

- To watch a collection for changes, see
  `db.collection.watch`.

- For complete examples with the change stream output, see
  db.collection.watch-change-streams-pre-and-post-images-example.

## Example

The following example illustrates an `update` event:

```json
{
   "_id": { <Resume Token> },
   "operationType": "update",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>,
   "ns": {
      "db": "engineering",
      "coll": "users"
   },
   "documentKey": {
      "_id": ObjectId("58a4eb4a30c75625e00d2820")
   },
   "updateDescription": {
      "updatedFields": {
         "email": "alice@10gen.com"
      },
      "removedFields": ["phoneNumber"],
      "truncatedArrays": [ {
         "field" : "vacation_time",
         "newSize" : 36
      } ]
   }
}
```

The following example illustrates an `update` event for change streams
opened with the `fullDocument : updateLookup` option:

```json
{
   "_id": { <Resume Token> },
   "operationType": "update",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>,
   "ns": {
      "db": "engineering",
      "coll": "users"
   },
   "documentKey": {
      "_id": ObjectId("58a4eb4a30c75625e00d2820")
   },
   "updateDescription": {
      "updatedFields": {
         "email": "alice@10gen.com"
      },
      "removedFields": ["phoneNumber"],
      "truncatedArrays": [ {
         "field" : "vacation_time",
         "newSize" : 36
      } ]
   },
   "fullDocument": {
      "_id": ObjectId("58a4eb4a30c75625e00d2820"),
      "name": "Alice",
      "userName": "alice123",
      "email": "alice@10gen.com",
      "team": "replication"
   }
}
```

The `fullDocument` document represents the most current majority-committed
version of the updated document. The `fullDocument` document may vary from
the document at the time of the update operation depending on the number of
interleaving majority-committed operations that occur between the update
operation and the document lookup.
