<!-- Converted from reference/method/Bulk.find.txt (reStructuredText). Includes are inlined. -->

# Bulk.find() (mongosh method)

**Tip:**

MongoDB also provides the `db.collection.bulkWrite()` method for 
performing bulk write operations.

## Description

**`Bulk.find(<query>)`**

Specifies a query condition for an update or a remove operation.

`Bulk.find()` accepts the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `query` | document | Specifies a query condition using query-selectors to select documents for an update or a remove operation. To specify all documents, use an empty document `{}`. With update operations, the sum of the query document and the update document must be less than or equal to the `maximum BSON document size`. With remove operations, the query document must be less than or equal to the `maximum BSON document size`. |

Use `Bulk.find()` with the following write operations:

- `Bulk.find.removeOne()`

- `Bulk.find.remove()`

- `Bulk.find.replaceOne()`

- `Bulk.find.updateOne()`

- `Bulk.find.update()`

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
for the `items` collection and adds a remove operation and an update
operation to the list of operations. The remove operation and the
update operation use the `Bulk.find()` method to specify a
condition for their respective actions:

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( { status: "D" } ).delete();
bulk.find( { status: "P" } ).update( { $set: { points: 0 } } )
bulk.execute();
```

**See also:**

- `db.collection.initializeUnorderedBulkOp()`
- `db.collection.initializeOrderedBulkOp()`
- `Bulk.execute()`
