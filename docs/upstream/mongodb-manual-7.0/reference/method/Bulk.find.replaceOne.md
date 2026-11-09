<!-- Converted from reference/method/Bulk.find.replaceOne.txt (reStructuredText). Includes are inlined. -->

# Bulk.find.replaceOne() (mongosh method)

**Tip:**

MongoDB also provides the `db.collection.bulkWrite()` method for 
performing bulk write operations.

## Description

**`Bulk.find.replaceOne(<document>)`**

Adds a single document replacement operation to a bulk operations
list. Use the `Bulk.find()` method to specify the condition
that determines which document to replace. The
`Bulk.find.replaceOne()` method limits the replacement to a
single document.

`Bulk.find.replaceOne()` accepts the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `replacement` | document | A replacement document that completely replaces the existing document. Contains only field and value pairs. The sum of the associated `<query>` document from the `Bulk.find()` and the replacement document must be less than or equal to the `maximum BSON document size`. |

To specify an upsert for this operation, see
`Bulk.find.upsert()`.

To specify the index to use for the associated
`Bulk.find()`, see `Bulk.find.hint()`.

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

The following example initializes a `Bulk()` operations builder
for the `items` collection, and adds various
`replaceOne` operations to the list of operations.

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( { item: "abc123" } ).replaceOne( { item: "abc123", status: "P", points: 100 } );
bulk.execute();
```

**See also:**

- `db.collection.initializeUnorderedBulkOp()`
- `db.collection.initializeOrderedBulkOp()`
- `Bulk.find()`
- `Bulk.execute()`
- All Bulk Methods
