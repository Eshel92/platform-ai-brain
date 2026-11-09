<!-- Converted from reference/change-events.txt (reStructuredText). Includes are inlined. -->

# Change Stream Events

Change streams watch collections, databases, or deployments for changes.

When a change occurs on a watched resource, the change stream returns a
change event notification document, with information on the operation and
the changes it makes.

## Operation Types

* - Event
  - Description

* - `create`
  - Occurs on the creation of a collection.

    Requires that you set the showExpandedEvents option to `true`.

    **New in version:** 6.0

* - `createIndexes`
  - Occurs on the creation of indexes on the collection.

    Requires that you set the showExpandedEvents option to `true`.

    **New in version:** 6.0

* - `delete`
  - Occurs when a document is removed from the collection. 

* - `drop`
  - Occurs when a collection is dropped from a database. 

* - `dropDatabase`
  - Occurs when a database is dropped. 

* - `dropIndexes`
  - Occurs when an index is dropped from the collection.

    Requires that you set the showExpandedEvents option to `true`.

    **New in version:** 6.0

* - `insert`
  - Occurs when an operation adds documents to a collection.

* - `invalidate`
  - Occurs when an operation renders the change stream
    invalid.

* - `modify`
  - Occurs when a collection is modified.

    Requires that you set the showExpandedEvents option to `true`.

    **New in version:** 6.0

* - `refineCollectionShardKey` 
  - Occurs when a shard key is modified.

    **New in version:** 6.1

* - `rename`
  - Occurs when a collection is renamed.

* - `replace`
  - Occurs when an update operation removes a document from 
    a collection and replaces it with a new document.

* - `reshardCollection` 
  - Occurs when the shard key for a collection and the distribution
    of data changes.

    Requires that you set the showExpandedEvents option to `true`.

    **New in version:** 6.1 *(Also available in 6.0.14)*

* - `shardCollection`
  - Occurs when a collection is sharded.

    Requires that you set the showExpandedEvents option to `true`.

    **New in version:** 6.0

* - `update`
  - Occurs when an operation updates a document in a collection.

**Note:**

The server might return update operations as replace events when
the replace representation is more concise. If you listen for
update operations, also listen for replace operations.

## Resume Token

Each change event includes an `_id` field, which is a BSON
object that serves as an identifier for the change stream event. For an
example of resuming a change stream by `resumeToken`, see
change-stream-resume.

## Expanded Events

**New in version:** 6.0

Change streams support data definition language (DDL) event
notifications, such as
createIndexes and
dropIndexes. To include expanded
events, open a change stream cursor with the
`showExpandedEvents` option.

For example:

**mongosh:**

```javascript
let cur = db.names.watch( [ ], {
   showExpandedEvents: true
} )

cur.next()
```

**agg-stage:**

```javascript
let cur = db.names.aggregate( [ { 
   $changeStream: { 
       showExpandedEvents: true 
     } 
   }
 ] )

cur.next()
```
