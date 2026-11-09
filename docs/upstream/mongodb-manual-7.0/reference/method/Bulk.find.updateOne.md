<!-- Converted from reference/method/Bulk.find.updateOne.txt (reStructuredText). Includes are inlined. -->

# Bulk.find.updateOne() (mongosh method)

**Tip:**

MongoDB also provides the `db.collection.bulkWrite()` method for 
performing bulk write operations.

## Description

**`Bulk.find.updateOne(<update>)`**

Adds a single document update operation to a bulk operations list.

Use the `Bulk.find()` method to specify the condition that
determines which document to update. The
`Bulk.find.updateOne()` method limits the update to a single
document. To update multiple documents, see
`Bulk.find.update()`.

`Bulk.find.updateOne()` accepts the following parameter:

* - Parameter

  - Type

  - Description

* - update

  - document or pipeline

  - .. _bulk-find-updateOne-parameter:

    The modifications to apply. Can be one of the following:

    - A replacement document:

      Contains only field and value pairs.

      See also `Bulk.find.replaceOne()`.

    - Update document:

      Contains only update operator expressions.

    - Aggregation pipeline:

      Contains only the following aggregation stages:

      - `$addFields` and its alias `$set`

      - `$project` and its alias `$unset`

      - `$replaceRoot` and its alias `$replaceWith`

    For more information on the update modification parameter, see the
    `db.collection.updateOne` reference page.

    The sum of the associated `<query>` document from the
    `Bulk.find()` and the update document must be
    less than or equal to the `maximum BSON document size`.

- To specify an upsert: true for this operation,
  use with `Bulk.find.upsert()`.

- To specify `arrayFilters` to update specific array
  elements, use with `Bulk.find.arrayFilters()`.

- To specify the index to use for the associated
  `Bulk.find()`, see `Bulk.find.hint()`.

- To replace a document wholesale, see also
  `Bulk.find.replaceOne()`.

## Compatibility

This command is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

## Behavior

If the `<update>` document contains only update operator expressions, as in:

```javascript
{
  $set: { status: "D" },
  $inc: { points: 2 }
}
```

Then, `Bulk.find.updateOne()` updates only the corresponding
fields, `status` and `points`, in the document.

## Example

The following example initializes a `Bulk()` operations builder
for the `items` collection, and adds various
`updateOne` operations to the list of operations.

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( { status: "D" } ).updateOne( { $set: { status: "I", points: "0" } } );
bulk.execute();
```

### Update with Aggregation Pipeline

Update methods can accept an aggregation pipeline. For
example, the following uses:

- the `$set` stage which can provide similar
  behavior to the `$set` update operator expression,

- the aggregation variable `NOW`, which resolves to the
  current datetime and can provide similar behavior to a
  `$currentDate` update operator expression. To access
  aggregation variables, prefix the variable with double dollar signs
  `$$` and enclose in quotes.

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( {  status: "P" } ).updateOne(
   [  
      { $set: { points: 0, lastModified: "$$NOW" } }
   ]
);
bulk.execute();
```

**See also:**

- `db.collection.initializeUnorderedBulkOp()`
- `db.collection.initializeOrderedBulkOp()`
- `Bulk.find()`
- `Bulk.find.update()`
- `Bulk.find.replaceOne()`
- `Bulk.execute()`
- All Bulk Methods
