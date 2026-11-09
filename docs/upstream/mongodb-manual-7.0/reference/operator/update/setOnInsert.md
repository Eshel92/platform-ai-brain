<!-- Converted from reference/operator/update/setOnInsert.txt (reStructuredText). Includes are inlined. -->

# $setOnInsert (update operator)

## Definition

**`$setOnInsert`**

If an update operation with upsert: true
results in an insert of a document, then `$setOnInsert`
assigns the specified values to the fields in the document. If the
update operation does not result in an insert,
`$setOnInsert` does nothing.

You can specify the `upsert` option for:

- `db.collection.updateOne()`
- `db.collection.updateMany()`
- `db.collection.findOneAndUpdate()`

```javascript
db.collection.updateOne(
   <query>,
   { $setOnInsert: { <field1>: <value1>, ... } },
   { upsert: true }
)
```

To specify a `<field>` in an embedded document or in an array, use
dot notation.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

Starting in MongoDB 5.0, `mongod` no longer raises an
error when you use an update operator like `$setOnInsert`
with an empty operand expression ( `{ }` ). An empty update results
in no changes and no oplog entry is created (meaning that the
operation is a no-op).

## Example

The `products` collection contains no documents.

Insert a new document using `db.collection.updateOne()` the upsert:
true parameter.

```javascript
db.products.updateOne(
  { _id: 1 },
  {
     $set: { item: "apple" },
     $setOnInsert: { defaultQty: 100 }
  },
  { upsert: true }
)
```

MongoDB uses `<query>` to create a new document with `_id: 1`.
`$setOnInsert` updates the document as specified.

The `products` collection contains the newly-inserted document:

```javascript
{ "_id" : 1, "item" : "apple", "defaultQty" : 100 }
```

When the upsert parameter is `true`
`db.collection.updateOne()`:

- creates a new document 
- applies the `$set` operation
- applies the `$setOnInsert` operation

If `db.collection.updateOne()` matches an existing document,
MongoDB only applies the `$set` operation.

**See also:**

- `db.collection.updateOne()`
- `db.collection.findOneAndUpdate()`
