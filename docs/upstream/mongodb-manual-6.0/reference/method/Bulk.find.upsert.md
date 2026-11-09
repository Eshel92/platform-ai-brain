<!-- Converted from reference/method/Bulk.find.upsert.txt (reStructuredText). Includes are inlined. -->

# Bulk.find.upsert()

**Tip:**

MongoDB also provides the `db.collection.bulkWrite()` method for 
performing bulk write operations.

## Description

**`Bulk.find.upsert()`**

Sets the upsert option to true for an update or a
replacement operation and has the following syntax:

```javascript
Bulk.find(<query>).upsert().update(<update>);
Bulk.find(<query>).upsert().updateOne(<update>);
Bulk.find(<query>).upsert().replaceOne(<replacement>);
```

With the `upsert` option set to `true`, if no matching documents
exist for the `Bulk.find()` condition, then the update or
the replacement operation performs an insert. If a matching document
does exist, then the update or replacement operation performs the
specified update or replacement.

Use `Bulk.find.upsert()` with the following write operations:

- `Bulk.find.replaceOne()`

- `Bulk.find.updateOne()`

- `Bulk.find.update()`

## Compatibility

This command is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

## Behavior

The following describe the insert behavior of various write operations
when used in conjunction with `Bulk.find.upsert()`.

### Insert for `Bulk.find.replaceOne()`

The `Bulk.find.replaceOne()` method accepts, as its parameter,
a replacement document that only contains field and value pairs:

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( { item: "abc123" } ).upsert().replaceOne(
   {
     item: "abc123",
     status: "P",
     points: 100,
   }
);
bulk.execute();
```

If the replacement operation with the `Bulk.find.upsert()`
option performs an insert, the inserted document is the replacement
document. If neither the replacement document nor the query document
specifies an `_id` field, MongoDB adds the `_id` field:

```javascript
{
  "_id" : ObjectId("52ded3b398ca567f5c97ac9e"),
  "item" : "abc123",
  "status" : "P",
  "points" : 100
}
```

### Insert for `Bulk.find.updateOne()`

The `Bulk.find.updateOne()` method accepts as its
parameter either:

- a replacement document that contains only field and value pairs (same
  as `Bulk.find.replaceOne()`),

- an update document that contains only update operator expressions, or

- an aggregation pipeline.

#### Field and Value Pairs

If the parameter is a
replacement document that contains only field and value pairs:

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( { status: "P" } ).upsert().updateOne(
   {
     item: "TBD",
     points: 0,
     inStock: true,
     status: "I"
   }
);
bulk.execute();
```

Then, if the update operation with the `Bulk.find.upsert()`
option performs an insert, the inserted document is the replacement
document. If neither the replacement document nor the query document
specifies an `_id` field, MongoDB adds the `_id` field:

```javascript
{
  "_id" : ObjectId("52ded5a898ca567f5c97ac9f"),
  "item" : "TBD",
  "points" : 0,
  "inStock" : true,
  "status" : "I"
}
```

#### Update Operator Expressions

If the parameter is an update
document that contains only update operator
expressions:

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( { status: "P", item: null } ).upsert().updateOne(
   {
     $setOnInsert: { qty: 0, inStock: true },
     $set: { points: 0 }
   }
);
bulk.execute();
```

Then, if the update operation with the `Bulk.find.upsert()`
option performs an insert, the update operation inserts a document with
field and values from the query document of the
`Bulk.find()` method and then applies the specified updates from
the update document. If neither the update document nor the query document
specifies an `_id` field, MongoDB adds the `_id` field:

```javascript
{
   "_id" : ObjectId("5e28d1a1500153bc2872dadd"),
   "item" : null,
   "status" : "P",
   "inStock" : true,
   "points" : 0,
   "qty" : 0
}
```

#### Aggregation Pipeline

Update methods can accept an aggregation pipeline. For example, the following 
uses:

- the `$replaceRoot` stage which can provide
  somewhat similar behavior to a `$setOnInsert`
  update operator expression,

- the `$set` stage which can provide similar
  behavior to the `$set` update operator expression,

- the aggregation variable `NOW`, which resolves to
  the current datetime and can provide similar behavior to a
  `$currentDate` update operator expression.

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( { item: "Not Found", status: "P" } ).upsert().updateOne(
   [  
      { $replaceRoot: { newRoot: { $mergeObjects: [ { qty: 0, inStock: true }, "$$ROOT"  ] } } },
      { $set: { points: 0, lastModified: "$$NOW" } }
   ]
);
bulk.execute();
```

Then, if the update operation with the `Bulk.find.upsert()`
option performs an insert, the update operation inserts a document with
field and values from the query document of the `Bulk.find()`
method and then applies the specified aggregation pipeline. If neither
the update document nor the query document specifies an `_id` field,
MongoDB adds the `_id` field:

```javascript
{
   "_id" : ObjectId("5e28cf1e500153bc2872d49f"),
   "qty" : 0,
   "inStock" : true,
   "item" : "Not Found",
   "status" : "P",
   "points" : 0,
   "lastModified" : ISODate("2020-01-22T22:39:26.789Z")
}
```

### Insert for `Bulk.find.update()`

When using `upsert()` with the multiple document
update method `Bulk.find.update()`, if no documents match the
query condition, the update operation inserts a *single* document.

The `Bulk.find.update()` method accepts as its parameter either:

- an update document that contains only update operator expressions, or

- an aggregation pipeline.

#### Update Operator Expressions

If the parameter is an update
document that contains only update operator
expressions: 

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( { status: "P" } ).upsert().update(
   {
     $setOnInsert: { qty: 0, inStock: true },
     $set: { status: "I", points: "0" }
   }
);
bulk.execute();
```

Then, if the update operation with the `Bulk.find.upsert()`
option performs an insert, the update operation inserts a single
document with the fields and values from the query document of
the `Bulk.find()` method and then applies the specified update
from the update document. If neither the update document
nor the query document specifies an `_id` field, MongoDB adds
the `_id` field:

```javascript
{
   "_id": ObjectId("52ded81a98ca567f5c97aca1"),
   "status": "I",
   "qty": 0,
   "inStock": true,
   "points": "0"
}
```

#### Aggregation Pipeline

Update methods can accept an aggregation pipeline. For
example, the following uses:

- the `$replaceRoot` stage which can provide
  somewhat similar behavior to a `$setOnInsert`
  update operator expression,

- the `$set` stage which can provide similar
  behavior to the `$set` update operator expression,

- the aggregation variable `NOW`, which resolves to the
  current datetime and can provide similar behavior to the
  `$currentDate` update operator expression. The value of
  `NOW` remains the same throughout the pipeline. To access
  aggregation variables, prefix the variable with double dollar signs
  `$$` and enclose in quotes.

```javascript
var bulk = db.items.initializeUnorderedBulkOp();
bulk.find( { item: "New Item", status: "P" } ).upsert().update(
   [  
      { $replaceRoot: { newRoot: { $mergeObjects: [ { qty: 0, inStock: true }, "$$ROOT"  ] } } },
      { $set: { points: 0, lastModified: "$$NOW" } }
   ]
);
bulk.execute();
```

Then, if the update operation with the `Bulk.find.upsert()`
option performs an insert, the update operation inserts a single
document with the fields and values from the query document of the
`Bulk.find()` method and then applies the aggregation pipeline.
If neither the update document nor the query document specifies an
`_id` field, MongoDB adds the `_id` field:

```javascript
{
   "_id" : ObjectId("5e2920a5b4c550aad59d18a1"),
   "qty" : 0,
   "inStock" : true,
   "item" : "New Item",
   "status" : "P",
   "points" : 0,
   "lastModified" : ISODate("2020-01-23T04:27:17.780Z")
}
```

**See also:**

- `db.collection.initializeUnorderedBulkOp()`
- `db.collection.initializeOrderedBulkOp()`
- `Bulk.find()`
- `Bulk.execute()`
- All Bulk Methods
