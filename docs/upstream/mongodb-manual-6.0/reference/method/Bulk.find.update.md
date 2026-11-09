<!-- Converted from reference/method/Bulk.find.update.txt (reStructuredText). Includes are inlined. -->

# Bulk.find.update()

**Tip:**

MongoDB also provides the `db.collection.bulkWrite()` method for 
performing bulk write operations.

## Description

**`Bulk.find.update(<update>)`**

Adds a `multi` update operation to a bulk operations list. The
method updates specific fields in existing documents.

Use the `Bulk.find()` method to specify the condition that
determines which documents to update. The
`Bulk.find.update()` method updates all matching documents.
To specify a single document update, see
`Bulk.find.updateOne()`.

`Bulk.find.update()` accepts the following parameter:

* - Parameter

  - Type

  - Description

* - update

  - document or pipeline

  - .. _bulk-find-update-parameter:

    The modifications to apply. Can be one of the following:

    * - Update document

      - Contains only update operator expressions.

    * - Aggregation pipeline

      - Contains only the following aggregation stages:

        - `$addFields` and its alias `$set`

        - `$project` and its alias `$unset`

        - `$replaceRoot` and its alias `$replaceWith`

    For more information on the update modification parameter, see the
    `db.collection.updateMany` reference page.

    The sum of the associated `<query>` document from the
    `Bulk.find()` and the update document must be less than or
    equal to the `maximum BSON document size`.

- To specify an upsert: true for this operation,
  use with `Bulk.find.upsert()`. With
  `Bulk.find.upsert()`, if no documents match the
  `Bulk.find()` query condition, the update operation
  inserts only a single document.

- To specify `arrayFilters` to update specific array
  elements, use with `Bulk.find.arrayFilters()`.

- To specify the index to use for the associated
  `Bulk.find()`, see `Bulk.find.hint()`.

- To replace a document wholesale, see
  `Bulk.find.replaceOne()`.

## Compatibility

This command is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

## Example

The following example initializes a `Bulk()` operations builder
for the `items` collection, and adds various `multi` update
operations to the list of operations.

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( { status: "D" } ).update( { $set: { status: "I", points: "0" } } );
bulk.find( { item: null } ).update( { $set: { item: "TBD" } } );
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
bulk.find( { status: "P" } ).update(
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
- `Bulk.find.updateOne()`
- `Bulk.execute()`
- All Bulk Methods
