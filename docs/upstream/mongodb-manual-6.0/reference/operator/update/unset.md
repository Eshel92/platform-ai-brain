<!-- Converted from reference/operator/update/unset.txt (reStructuredText). Includes are inlined. -->

# $unset

## Definition

**Note:** Disambiguation

The following page refers to the update operator `$unset`.
For the aggregation stage, see `$unset`.

**`$unset`**

The `$unset` operator deletes a particular field. 
   

## Compatibility

You can use `$unset` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

Consider the following syntax:

```javascript
{ $unset: { <field1>: "", ... } }
```

The specified value in the `$unset` expression (i.e. `""`)
does not impact the operation.

To specify a `<field>` in an embedded document or in an array, use
dot notation.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

If the field does not exist, then `$unset` does nothing (i.e.
no operation).

When used with `$` to match an array element, `$unset`
replaces the matching element with `null` rather than removing the
matching element from the array. This behavior keeps consistent the
array size and element positions.

Starting in MongoDB 5.0, `mongod` no longer raises an
error when you use an update operator like `$unset`
with an empty operand expression ( `{ }` ). An empty update results
in no changes and no oplog entry is created (meaning that the
operation is a no-op).

## Example

Create the `products` collection:

```javascript
db.products.insertMany( [
   { "item": "chisel", "sku": "C001", "quantity": 4, "instock": true },
   { "item": "hammer", "sku": "unknown", "quantity": 3, "instock": true },
   { "item": "nails", "sku": "unknown", "quantity": 100, "instock": true }
] )
```

Update the *first* document in the `products` collection where the
value of `sku` is `unknown`:

```javascript
db.products.updateOne(
   { sku: "unknown" },
   { $unset: { quantity: "", instock: "" } }
)
```

`updateOne()` uses the `$unset` operator to:

- remove the `quantity` field
- remove the `instock` field

```javascript
{
  item: 'chisel',
  sku: 'C001',
  quantity: 4,
  instock: true
},
{
  item: 'hammer',
  sku: 'unknown'
},
{
  item: 'nails',
  sku: 'unknown',
  quantity: 100,
  instock: true
}
```

**See also:**

`db.collection.updateMany()`
`db.collection.findAndModify()`
