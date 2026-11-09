<!-- Converted from reference/change-events/invalidate.txt (reStructuredText). Includes are inlined. -->

# invalidate Event

## Summary

**`invalidate`**

An `invalidate` event occurs when an operation renders the change stream
invalid. For example, a change stream opened on a collection that was later 
dropped or renamed would cause an `invalidate` event.

## Description

| Field | Type | Description |
|---|---|---|
| `_id` | Document | .. include:: /includes/change-stream/id |
| `clusterTime` | Timestamp | .. include:: /includes/change-stream/clusterTime |
| `operationType` | string | .. include:: /includes/change-stream/operationType Returns a value of `invalidate` for these change events. |
| `wallTime` | ISODate | .. include:: /includes/change-stream/wallTime |

## Example

The following example illustrates an `invalidate` event:

```json
{
   "_id": { <Resume Token> },
   "operationType": "invalidate",
   "clusterTime": <Timestamp>,
   "wallTime": <ISODate>
}
```

Change streams opened on collections raise an `invalidate` event when a 
drop, rename, 
or dropDatabase operation occurs 
that affects the watched collection.

Change streams opened on databases raise an `invalidate` event when a
dropDatabase event occurs that affects
the watched database.

`invalidate` events close the change stream cursor.

You cannot use `resumeAfter` to resume a change stream after an
invalidate event (for example, a collection
drop or rename) closes the stream. Instead, you can use
startAfter to start a new change
stream after an invalidate event.
