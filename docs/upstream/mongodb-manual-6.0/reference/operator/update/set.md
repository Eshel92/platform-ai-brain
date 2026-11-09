<!-- Converted from reference/operator/update/set.txt (reStructuredText). Includes are inlined. -->

# $set

## Definition

**Note:** Disambiguation

The following page refers to the update operator `$set`.
For the aggregation stage, see `$set`.

**`$set`**

The `$set` operator replaces the value of a field with the
specified value.

## Compatibility

You can use `$set` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$set` operator expression has the following form:

```javascript
{ $set: { <field1>: <value1>, ... } }
```

To specify a `<field>` in an embedded document or in an array, use
dot notation.

## Behavior

Starting in MongoDB 5.0, update operators process document fields with
string-based names in lexicographic order. Fields with numeric names are
processed in numeric order. See Update Operators Behavior for details.

If the field does not exist, `$set` will add a new field with the
specified value, provided that the new field does not violate a type
constraint.
If you specify a dotted path for a non-existent field,
`$set` will create the embedded documents *as needed* to
fulfill the dotted path to the field.

If you specify multiple field-value pairs, `$set` will update
or create each field.

Starting in MongoDB 5.0, `mongod` no longer raises an
error when you use an update operator like `$set`
with an empty operand expression ( `{ }` ). An empty update results
in no changes and no oplog entry is created (meaning that the
operation is a no-op).

## Examples

Create the `products` collection:

```javascript
db.products.insertOne(
   {
     _id: 100,
     quantity: 250,
     instock: true,
     reorder: false,
     details: { model: "14QQ", make: "Clothes Corp" },
     tags: [ "apparel", "clothing" ],
     ratings: [ { by: "Customer007", rating: 4 } ]
   }
)
```

### Set Top-Level Fields

For the document matching the criteria `_id` equal to `100`, the
following operation uses the `$set` operator to update the
value of the `quantity` field, `details` field, and the `tags`
field.

```javascript
db.products.updateOne(
   { _id: 100 },
   { $set:
      {
        quantity: 500,
        details: { model: "2600", make: "Fashionaires" },
        tags: [ "coats", "outerwear", "clothing" ]
      }
   }
)
```

The operation updates the:

- value of `quantity` to `500`
- `details` field with new embedded document
- `tags` field with new array

```javascript
{
  _id: 100,
  quantity: 500,
  instock: true,
  reorder: false,
  details: { model: '2600', make: 'Fashionaires' },
  tags: [ 'coats', 'outerwear', 'clothing' ],
  ratings: [ { by: 'Customer007', rating: 4 } ]
}
```

### Set Fields in Embedded Documents

To specify a `<field>` in an embedded document or in an array, use
dot notation.

For the document matching the criteria `_id` equal to `100`, the
following operation updates the `make` field in the `details`
document:

```javascript
db.products.updateOne(
   { _id: 100 },
   { $set: { "details.make": "Kustom Kidz" } }
)
```

After updating, the document has the following values:

```javascript
{
   _id: 100,
   quantity: 500,
   instock: true,
   reorder: false,
   details: { model: '2600', make: 'Kustom Kidz' },
   tags: [ 'coats', 'outerwear', 'clothing' ],
   ratings: [ { by: 'Customer007', rating: 4 } ]
}
```

**Important:**

The above code uses `dot notation` to update the `make` field of the 
embedded `details` document. The code format looks similar to the following 
code example, which instead *replaces the entire embedded document*, removing 
all other fields in the embedded `details` document:

```javascript
db.products.updateOne(
   { _id: 100 },
   { $set: { details:
      {make: "Kustom Kidz"}
      }
   })
```

### Set Elements in Arrays

To specify a `<field>` in an embedded document or in an array, use
dot notation.

For the document matching the criteria `_id` equal to `100`, the
following operation updates the value second element (array index of
`1`) in the `tags` field and the `rating` field in the first
element (array index of `0`) of the `ratings` array.

```javascript
db.products.updateOne(
   { _id: 100 },
   { $set:
      {
        "tags.1": "rain gear",
        "ratings.0.rating": 2
      }
   }
)
```

After updating, the document has the following values:

```javascript
{
  _id: 100,
  quantity: 500,
  instock: true,
  reorder: false,
  details: { model: '2600', make: 'Kustom Kidz' },
  tags: [ 'coats', 'rain gear', 'clothing' ],
  ratings: [ { by: 'Customer007', rating: 2 } ]
}
```

For additional update operators for arrays, see
/reference/operator/update-array.

**See also:**

- `db.collection.updateMany()`
- `db.collection.findAndModify()`
