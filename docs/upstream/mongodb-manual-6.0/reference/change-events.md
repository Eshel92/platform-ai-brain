<!-- Converted from reference/change-events.txt (reStructuredText). Includes are inlined. -->

# Change Events

Change streams watch collections, databases, or deployments for changes.

When a change occurs on a watched resource, the change stream returns a
change event notification document, with information on the operation and
the changes it made.

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

## Resume Token

Each change event includes an `_id` field, which contain a document.  This
document can serve as the resume token when
starting a change stream.

## Expanded Events

**New in version:** 6.0

Starting in MongoDB 6.0, change streams support change notifications for DDL
events, like the createIndexes and
dropIndexes events. To include expanded
events in a change stream, create the change stream cursor using the
`showExpandedEvents` option.

For example:

```javascript
let cur = db.names.aggregate( [ { 
   $changeStream: { 
       showExpandedEvents: true 
     } 
   }
 ] )

cur.next()
```
