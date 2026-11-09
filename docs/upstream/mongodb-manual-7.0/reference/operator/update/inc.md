<!-- Converted from reference/operator/update/inc.txt (reStructuredText). Includes are inlined. -->

# $inc (update operator)

## Definition

**`$inc`**

The `$inc` operator increments a field by a specified value.

## Compatibility

You can use `$inc` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$inc` operator has the following form:

```javascript
{ $inc: { <field1>: <amount1>, <field2>: <amount2>, ... } }
```

To specify a `<field>` in an embedded document or in an array, use
dot notation.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

The `$inc` operator accepts positive and negative values.

If the field does not exist, `$inc` creates the field and sets
the field to the specified value.

Using the `$inc` operator on a field with a null value
generates an error.

`$inc` is an atomic operation within a single document.

Starting in MongoDB 5.0, `mongod` no longer raises an
error when you use an update operator like `$inc`
with an empty operand expression ( `{ }` ). An empty update results
in no changes and no oplog entry is created (meaning that the
operation is a no-op).

## Example

Create the `products` collection:

```javascript
db.products.insertOne(
   {
     _id: 1,
     sku: "abc123",
     quantity: 10,
     metrics: { orders: 2, ratings: 3.5 }
   }
)
```

The following `updateOne()` operation uses the
`$inc` operator to:

- increase the `"metrics.orders"` field by 1
- increase the `quantity` field by -2 (which decreases `quantity`)

```javascript
db.products.updateOne(
   { sku: "abc123" },
   { $inc: { quantity: -2, "metrics.orders": 1 } }
)
```

The operation returns the following result:

```javascript
{
  _id: 1,
  sku: 'abc123',
  quantity: 8,
  metrics: { orders: 3, ratings: 3.5 }
}
```

**See also:**

- `db.collection.updateMany()`
- `db.collection.findAndModify()`
