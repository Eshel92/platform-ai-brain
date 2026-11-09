<!-- Converted from reference/method/db.collection.renameCollection.txt (reStructuredText). Includes are inlined. -->

# db.collection.renameCollection() (mongosh method)

(Include not available offline: includes/wayfinding/mongosh-method-renameCollection.rst)

## Definition

**`db.collection.renameCollection(target, dropTarget)`**

Renames a collection. Provides a wrapper for the
`renameCollection` database command.

### Parameters

| Parameter | Type | Description |
|---|---|---|
| `target` | string | The new name of the collection. Enclose the string in quotes. See restrictions-on-db-names. |
| `dropTarget` | boolean | Optional. If `true`, `mongod` drops the `target` of `renameCollection` prior to renaming the collection. The default value is `false`. |

## Behavior

The `db.collection.renameCollection()` method operates within a
collection by changing the metadata associated with a given collection.

Refer to the documentation `renameCollection` for additional
warnings and messages.

**Warning:**

The `db.collection.renameCollection()` method and
`renameCollection` command will invalidate open cursors
which interrupts queries that are currently returning data.

For /changeStreams, the
`db.collection.renameCollection()` method and
`renameCollection` command create an
change-event-invalidate for any existing
/changeStreams opened on the source or target collection.

- The method has the following limitations:

  - `db.collection.renameCollection()` cannot move a collection
    between databases. Use `renameCollection` for these
    rename operations.

  - .. include:: /includes/extracts/views-unsupported-rename.rst

  - `db.collection.renameCollection()` is not supported on
    time series collections.

  - You cannot rename a collection to itself. If you try to rename a
    collection to itself an `IllegalOperation` error is thrown.

### Resource Locking in Sharded Clusters

**Changed in version:** 5.0

When renaming a sharded or unsharded collection in a sharded cluster,
the source and target collections are exclusively locked on every shard.
Subsequent operations on the source and target collections must wait
until the rename operation completes.

For more information on locking in MongoDB, see /faq/concurrency.

### Resource Locking in Replica Sets

`renameCollection()` obtains an exclusive lock on
the source and target collections for the duration of the operation. All
subsequent operations on the collections must wait until
`renameCollection()` completes. 

### Interaction with `mongodump`

A `mongodump` started with 
`--oplog` fails if a client issues
`db.collection.renameCollection()` during the dump process. See
`mongodump.--oplog` for more information.

## Example

Call the `db.collection.renameCollection()` method on a
collection object. For example:

```javascript
db.rrecord.renameCollection("record")
```

This operation will rename the `rrecord` collection to `record`. If
the target name (i.e. `record`) is the name of an existing collection,
then the operation will fail.
