<!-- Converted from reference/method/Bulk.find.hint.txt (reStructuredText). Includes are inlined. -->

# Bulk.find.hint()

**Tip:**

MongoDB also provides the `db.collection.bulkWrite()` method for 
performing bulk write operations.

## Description

**`Bulk.find.hint()`**

Sets the `hint` option that specifies the index
to support the `Bulk.find()` for:

- `Bulk.find.replaceOne()`
- `Bulk.find.update()`
- `Bulk.find.updateOne()`.

The option can take an index specification document or the index
name string.

If you specify an index that does not exist, the operation
errors.

`Bulk.find.hint()` has no effect on `Bulk.find.removeOne()`

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

Create an example collection `orders`:

```javascript
db.orders.insertMany( [
   { "_id" : 1, "item" : "abc", "price" : NumberDecimal("12"), "quantity" : 2, "type": "apparel" },
   { "_id" : 2, "item" : "jkl", "price" : NumberDecimal("20"), "quantity" : 1, "type": "electronics" },
   { "_id" : 3, "item" : "abc", "price" : NumberDecimal("10"), "quantity" : 5, "type": "apparel" },
   { "_id" : 4, "item" : "abc", "price" : NumberDecimal("8"), "quantity" : 10, "type": "apparel" },
   { "_id" : 5, "item" : "jkl", "price" : NumberDecimal("15"), "quantity" : 15, "type": "electronics" }
] )
```

Create the following indexes on the example collection:

```javascript
db.orders.createIndex( { item: 1 } );
db.orders.createIndex( { item: 1, quantity: 1 } );
db.orders.createIndex( { item: 1, price: 1 } );
```

The following bulk operations specify different index to use for the
various update/replace document operations:

```javascript
var bulk = db.orders.initializeUnorderedBulkOp();
bulk.find({ item: "abc", price: { $gte: NumberDecimal("10") }, quantity: { $lte: 10 } }).hint({item: 1, quantity: 1}).replaceOne( { item: "abc123", status: "P", points: 100 } );
bulk.find({ item: "abc", price: { $gte: NumberDecimal("10") }, quantity: { $lte: 10 } }).hint({item: 1, price: 1}).updateOne( { $inc: { points: 10 } } );
bulk.execute();
```

To view the indexes used, you can use the `$indexStats` pipeline:

```javascript
db.orders.aggregate( [ { $indexStats: { } }, { $sort: { name: 1 } } ] )
```

**See also:**

- `db.collection.initializeUnorderedBulkOp()`
- `db.collection.initializeOrderedBulkOp()`
- `Bulk.find()`
- `Bulk.execute()`
- All Bulk Methods
