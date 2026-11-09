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

    The `collectionUUID` field is only included if the change stream is
    created with the `showExpandedEvents` field set to `true`. For
    details, see showExpandedEvents.

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
    | `disambiguatedPaths`
  - document
  - .. include:: /includes/change-stream/ud-disambiguatedPaths

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

### Path Disambiguation

**New in version:** 6.1

The `updateDescription` field notes changes made to specific fields in 
documents by an operation.  These field descriptors use dots (`.`) as
path separators and numbers as array indexes, which leads to some
ambiguity when it contains field names that use dots or numbers.

When an `update` event reports changes involving ambiguous fields,
the `disambiguatedPaths` document provides the path key with an array 
listing each path component.

**Note:**

The `disambiguatedPaths` field is only available on change streams
started with the showExpandedEvents option 

For example, consider a document that lists people and the towns in which they 
live:

```json
{
   "name": "Anthony Trollope",
   "home.town": "Oxford",
   "residences": [
      {"0": "Oxford"},
      {"1": "Sunbury"}
   ]
}
```

* When an update modifies the `home.town` field from `Oxford` to
  `London`, it produces an update description that looks like this:

  ```json
  "updateDescription": {
     "updatedFields": {
        "home.town": "London"
     },
     "disambiguatedPaths": {
        "home.town": [ "home.town" ]
     }
  }
  ```

  
  Because the field `home.town` contains a period, the `disambiguatedPaths` 
  field shows an array with one value, to indicate that `town` is not a
  sub-field of `home`.

* When an update modifies a value in the `residences` array to make the same 
  change, it produces an update description that looks like this:
  

  ```json
  "updateDescription": {
     "updatedFields": {
        "residences.0.0": "London"
     },
     "disambiguatedPaths": { "residences.0.0": [ "residences", 0, "0" ] }
  }
  ```

  The disambiguated paths include an integer `0` to indicate the array index
  and the string `"0"` to indicate the field name within the nested document.
  
There are two cases where `disambiguatedPath` does **not** include a 
numeric field:

* When the first field in the path is a numeric string (i.e. `0.name`).
  This is not ambiguous since the first field cannot be an array index.

* When the numeric string field has leading zeroes (i.e., `0001`).  
  This is not ambiguous since an integer cannot have leading zeroes.

### Update Operations

The `update` command can produce different change
events (not just `update`) depending on the actual
changes it makes to the collection. 

| Change Event | Description |
|---|---|
| `update` | The update operation modified an existing document. |
| `replace` | The update operation replaced the document or produced a diff that was more verbose than the original document, causing MongoDB to replace it. |
| `insert` | The update operation attempted to update a document that doesn't exist and instead added the document to the collection. This only occurs when the update runs with the `upsert` option enabled. |

### Comparison of Standard Updates and Pipeline Updates

In some scenarios, standard updates and pipeline updates produce different change events for the same
logical change. If you switch between standard and pipeline update
syntax, you may observe unexpected change events in your application.

The following example shows how the different update syntaxes produce
different change events when removing subfields from embedded documents.
This is only one of many scenarios where change events differ based on
the update syntax used.

- **Standard Updates:** When subfields of an embedded object are removed,
  the removed paths are always in the `removedFields` array.

- **Pipeline Updates:** When subfields of an embedded object are
  removed, the resulting change event shows the most concise description
  of the update. For example:
  
  - If a small number of subfields are removed (for example, removing 1 out
    of 3 subfields), the change is shown in the `removedFields` array.
    
  - If most subfields are removed (for example, removing 2 out of 3
    subfields), the change is shown in the `updatedFields` array, and
    the parent object reflects the new state.

The following example script shows the different change events generated
by standard updates and pipeline updates that remove subfields of an
object:

```javascript
// 1. Setup collection and insert documents for test cases

let contactMethods = {
   email: "user@example.com",
   phone: "555-0100",
   mobile: "555-0101"
};

db.cstest.drop();
db.cstest.insertMany([

   // Case 1: Remove 1 of 3 subfields
   { _id: "standard_remove_1_of_3", contactMethods: contactMethods },
   { _id: "pipeline_remove_1_of_3", contactMethods: contactMethods },

   // Case 2: Remove 2 of 3 subfields
   { _id: "standard_remove_2_of_3", contactMethods: contactMethods },
   { _id: "pipeline_remove_2_of_3", contactMethods: contactMethods }
]);

// 2. Open a Change Stream
const csCursor = db.cstest.watch();

// --- CASE 1: Remove 1 out of 3 subfields ---
db.cstest.updateOne({ _id: "standard_remove_1_of_3" }, { $unset: { "contactMethods.email": "" } });
db.cstest.updateOne({ _id: "pipeline_remove_1_of_3" }, [{ $unset: "contactMethods.email" }]);

// --- CASE 2: Remove 2 out of 3 subfields ---
db.cstest.updateOne({ _id: "standard_remove_2_of_3" }, { $unset: { "contactMethods.email": "", "contactMethods.phone": "" } });
db.cstest.updateOne({ _id: "pipeline_remove_2_of_3" }, [{ $unset: ["contactMethods.email", "contactMethods.phone"] }]);

// 3. Print the change stream updateDescriptions
print("\n--- Change Stream Results ---");
for (let i = 0; i < 4; i++) {
   if (csCursor.hasNext()) {
      let event = csCursor.next();
      print(`\nOperation: ${event.documentKey._id}`);
      print(JSON.stringify(event.updateDescription));
   }
}
csCursor.close(); 
```

Output:

```javascript
--- Change Stream Results ---

Operation: standard_remove_1_of_3
{"updatedFields":{},"removedFields":["contactMethods.email"],"truncatedArrays":[]}

Operation: pipeline_remove_1_of_3
{"updatedFields":{},"removedFields":["contactMethods.email"],"truncatedArrays":[]}

Operation: standard_remove_2_of_3
{"updatedFields":{},"removedFields":["contactMethods.email","contactMethods.phone"],"truncatedArrays":[]}

Operation: pipeline_remove_2_of_3
{"updatedFields":{"contactMethods":{"mobile":"555-0101"}},"removedFields":[],"truncatedArrays":[]}
```

### Array Updates

Updates to arrays produce `update` change events, but the
`updateDescription.updateFields` can show different values.

For example, consider the following document and updates:

```javascript
db.students.insertOne( { student_id: 1, scores: [ ] } )

db.students.updateOne( 
   { student_id: 1 }, 
   { $push: { scores: 0.85 } }
)

db.students.updateOne( 
   { student_id: 1 }, 
   { $push: { scores: 0.94 } } 
)

db.students.updateOne( 
   { student_id: 1 }, 
   { $pull: { scores: 0.94 } } 
)
```

The first update operates on an empty array. Here, the
`$push` produces an `update` change event where the
field is replaced by single-entry array with the given value:

```javascript
{
   _id: { _data: '82642AD66B000000012B022C0100296E5A10045DC4B11BEA5F4319A8E7CAF46816ED71461E5F6964002B060004' },
   operationType: 'update',
   clusterTime: Timestamp({ t: 1680529003, i: 1 }),
   ns: { db: 'communication_chat', coll: 'students' },
   documentKey: { student_id: 1 },
   updateDescription: {
      updatedFields: { scores: [ 0.85 ] },
      removedFields: [],
      truncatedArrays: []
   }
}
```

In the second update operation, the array now contains values.
The `$push` adds a new entry in the array. The
`update` change event then shows it as a change on the new
position in the array (that is, `scores.1`):

```javascript
{
  _id: { _data: '82642AD673000000012B022C0100296E5A10045DC4B11BEA5F4319A8E7CAF46816ED71461E5F6964002B060004' },
  operationType: 'update',
  clusterTime: Timestamp({ t: 1680529011, i: 1 }),
  ns: { db: 'communication_chat', coll: 'students' },
  documentKey: { student_id: 1 },
  updateDescription: {
    updatedFields: { 'scores.1': 0.94 },    
    removedFields: [],
    truncatedArrays: []
  }
}
```

If you run the update operation again to add a third score to
the student's record, it would produce an `update` change
event that modifies `scores.2`.

Removal of array items with the `$pull` operator
produces a change event that shows the new array:

```javascript
{
  _id: { _data: '82642AD673000000012B022C0100296E5A10045DC4B11BEA5F4319A8E7CAF46816ED71461E5F6964002B060004' },
  operationType: 'update',
  clusterTime: Timestamp({ t: 1680529011, i: 1 }),
  ns: { db: 'communication_chat', coll: 'students' },
  documentKey: { student_id: 1 },
  updateDescription: {
    updatedFields: { scores: [ 0.85 ] },
    removedFields: [],
    truncatedArrays: []
  }
}
```

### Array Truncation

Update operations that reduce the number of elements in arrays
through the pipeline updates, such
as with the `$addFields` or `$set`
aggregation stages, show the updated array and new size in the
`truncatedArrays` field.

```javascript
db.students.insertOne( { student_id: 2, scores: [ 0.85, 0.94, 0.78 ] } )

db.students.updateOne( 
   { student_id: 2 }, 
   [ { $addFields: { scores: [ 0.85, 0.94 ] } } ]
)

db.students.updateOne( 
   { student_id: 2 }, 
   [ { $addFields: { scores: [ 0.85, 0.94, 0.78 ] } } ]
)
```

The change event from the first update, which used the
`$addFields` stage to remove a value from the
`scores` field shows the change in the `truncatedArrays`
field:

```javascript
{
  _id: { _data: '82642AD673000000012B022C0100296E5A10045DC4B11BEA5F4319A8E7CAF46816ED71461E5F6964002B060004' },
  operationType: 'update',
  clusterTime: Timestamp({ t: 1680529011, i: 1 }),
  ns: { db: 'communication_chat', coll: 'students' },
  documentKey: { student_id: 2 },
  updateDescription: {
    updatedFields: {},
    removedFields: [],
    truncatedArrays: [ { fields: "scores", newSize: 2 } ]
  }
}
```

The change event from the second update, which used the
`$addFields` stage to add a value back to the
`scores` field, shows the update in the `updatedFields`
field:

```javascript
{
  _id: { _data: '82642AD673000000012B022C0100296E5A10045DC4B11BEA5F4319A8E7CAF46816ED71461E5F6964002B060004' },
  operationType: 'update',
  clusterTime: Timestamp({ t: 1680529011, i: 1 }),
  ns: { db: 'communication_chat', coll: 'students' },
  documentKey: { student_id: 2 },
  updateDescription: {
    updatedFields: { scores.2: 0.78 },
    removedFields: [],
    truncatedArrays: []
  }
}
```

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
      } ],
      "disambiguatedPaths": { }
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
