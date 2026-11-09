<!-- Converted from reference/method/Bulk.toString.txt (reStructuredText). Includes are inlined. -->

# Bulk.toString() (mongosh method)

**`Bulk.toString()`**

Returns as a string a JSON document that contains the number of
operations and batches in the `Bulk()` object.

## Compatibility

This command is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

## Example

The following initializes a `Bulk()` operations builder on the
`items` collection, adds a series of write operations, and calls
`Bulk.toString()` on the `bulk` builder object.

```javascript
var bulk = db.items.initializeOrderedBulkOp();
bulk.insert( { item: "abc123", status: "A", defaultQty: 500, points: 5 } );
bulk.insert( { item: "ijk123", status: "A", defaultQty: 100, points: 10 } );
bulk.find( { status: "D" } ).deleteOne();
bulk.toString();
bulk.execute()
```

The `Bulk.toString()` returns the following JSON document

```javascript
{
  acknowledged: true,
  insertedCount: 2,
  insertedIds: [
    { index: 0, _id: ObjectId("627bf4f95e19ff3518448883") },
    { index: 1, _id: ObjectId("627bf4f95e19ff3518448884") }
  ],
  matchedCount: 0,
  modifiedCount: 0,
  deletedCount: 0,
  upsertedCount: 0,
  upsertedIds: []
}
```

**See also:**

`Bulk()`
