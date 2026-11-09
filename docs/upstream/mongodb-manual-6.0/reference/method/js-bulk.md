<!-- Converted from reference/method/js-bulk.txt (reStructuredText). Includes are inlined. -->

# Bulk Operation Methods

**Note:**

For details on a specific method, including syntax and examples,
click on the link to the method's reference page.

**Tip:**

MongoDB also provides the `db.collection.bulkWrite()` method for 
performing bulk write operations.

| Name | Description |
|---|---|
| `db.collection.initializeOrderedBulkOp()` | Initializes a `Bulk()` operations builder for an ordered list of operations. |
| `db.collection.initializeUnorderedBulkOp()` | Initializes a `Bulk()` operations builder for an unordered list of operations. |
| `Bulk()` | Bulk operations builder. |
| `Bulk.execute()` | Executes a list of operations in bulk. |
| `Bulk.find()` | Specifies the query condition for an update or a remove operation. |
| `Bulk.find.arrayFilters()` | Specifies the filters that determine which elements of an array to update for an `update` or `updateOne` operation. |
| `Bulk.find.collation()` | Specifies the collation for the query condition. |
| `Bulk.find.delete()` | Adds a multiple document delete operation to a list of operations. |
| `Bulk.find.deleteOne()` | Adds a single document delete operation to a list of operations. |
| `Bulk.find.hint()` | Specifies the index to use for the update/replace operation. |
| `Bulk.find.remove()` | An alias for `Bulk.find.delete()`. |
| `Bulk.find.removeOne()` | An alias for `Bulk.find.deleteOne()`. |
| `Bulk.find.replaceOne()` | Adds a single document replacement operation to a list of operations. |
| `Bulk.find.updateOne()` | Adds a single document update operation to a list of operations. |
| `Bulk.find.update()` | Adds a `multi` update operation to a list of operations. |
| `Bulk.find.upsert()` | Specifies `upsert: true` for an update operation. |
| `Bulk.getOperations()` | Returns an array of write operations executed in the `Bulk()` operations object. |
| `Bulk.insert()` | Adds an insert operation to a list of operations. |
| `Bulk.toJSON()` | Returns a JSON document that contains the number of operations and batches in the `Bulk()` operations object. |
| `Bulk.toString()` | Returns the `Bulk.toJSON()` results as a string. |
