<!-- Converted from reference/change-events/replace.txt (reStructuredText). Includes are inlined. -->

# `replace` Event

## Summary

**`replace`**

A `replace` event occurs when an operation replaces all fields in a
document with new values, such as when `replaceOne` is called or when an `update`
command performs a document replacement.

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
  - The new document created by the operation. 

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

    Returns a value of `replace` for these change events.

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

    **Note:**

    The `setClusterParameter` command is not supported in MongoDB 
    Atlas clusters. For information on Atlas support for all commands, see 
    unsupported-commands.

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

  - To monitor the size of `config.system.preimages`, connect to a
    shard node on a sharded cluster or a `mongod` node
    on a replica set. Then, run the following commands:

    ```javascript
    use config
    db.system.preimages.totalSize()
    db.system.preimages.stats()
    ```

    **Note:**

    You must have the `collStats` privilege action on the
    `config.system.preimages` collection to run these commands.

    To run these commands on an MongoDB Atlas deployment, you must have
    the `atlasAdmin` role.

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

#### Update Operations

The `update` command can produce different change
events (not just `update`) depending on the actual
changes it makes to the collection. 

| Change Event | Description |
|---|---|
| `update` | The update operation modified an existing document. |
| `replace` | The update operation replaced the document or produced a diff that was more verbose than the original document, causing MongoDB to replace it. |
| `insert` | The update operation attempted to update a document that doesn't exist and instead added the document to the collection. This only occurs when the update runs with the `upsert` option enabled. |

## Examples

The following example illustrates a `replace` event:

```json
{
   "_id": { <Resume Token> },
   "operationType": "replace",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>,
   "ns": {
      "db": "engineering",
      "coll": "users"
   },
   "documentKey": {
      "_id": ObjectId("599af247bb69cd89961c986d")
   },
   "fullDocument": {
      "_id": ObjectId("599af247bb69cd89961c986d"),
      "userName": "alice123",
      "name": "Alice"
   }
}
```

A `replace` event can result from `replaceOne()` or from an `update`
command that performs a full-document replacement.

The `fullDocument` of a `replace` event represents the replacement
document after the operation completes.
