<!-- Converted from reference/operator/query/gt.txt (reStructuredText). Includes are inlined. -->

# $gt (query predicate operator)

## Definition

**`$gt`**

`$gt` selects documents where the value of the field is
greater than (`>`) the specified value.

## Compatibility

You can use `$gt` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$gt` operator has this form:

```javascript
{ field: { $gt: value } }
```

## Behavior

Inequality comparison operators use type bracketing: a comparison on a given BSON type filters out
values of a different type.

## Examples

To create the `inventory` collection used in the examples, run this
command:

```javascript
db.inventory.insertMany( [
   {
      item: "nuts", quantity: 30,
      carrier: { name: "Shipit", fee: 3 }
   },
   {
      item: "bolts", quantity: 50,
      carrier: { name: "Shipit", fee: 4 }
   },
   {
      item: "washers", quantity: 10,
      carrier: { name: "Shipit", fee: 1 }
   }
] )
```

### Match Document Fields

This example selects documents in the `inventory` collection where
`quantity` is greater than `20`:

```javascript
db.inventory.find( { quantity: { $gt: 20 } } )
```

Example output:

```javascript
{
  _id: ObjectId("61ba25cbfe687fce2f042414"),
  item: 'nuts',
  quantity: 30,
  carrier: { name: 'Shipit', fee: 3 }
},
{
  _id: ObjectId("61ba25cbfe687fce2f042415"),
  item: 'bolts',
  quantity: 50,
  carrier: { name: 'Shipit', fee: 4 }
}
```

### Perform an Update Based on Embedded Document Fields

This example sets the `price` field based on a `$gt`
comparison on a field in an embedded document:

```javascript
db.inventory.updateOne(
   { "carrier.fee": { $gt: 2 } }, { $set: { "price": 9.99 } }
)
```

Example output:

```javascript
{
  _id: ObjectId("61ba3ec9fe687fce2f042417"),
  item: 'nuts',
  quantity: 30,
  carrier: { name: 'Shipit', fee: 3 },
  price: 9.99
},
{
  _id: ObjectId("61ba3ec9fe687fce2f042418"),
  item: 'bolts',
  quantity: 50,
  carrier: { name: 'Shipit', fee: 4 }
},
{
  _id: ObjectId("61ba3ec9fe687fce2f042419"),
  item: 'washers',
  quantity: 10,
  carrier: { name: 'Shipit', fee: 1 }
}
```

The `updateOne()` operation matches an embedded
document named `carrier`, with a subfield named `fee`. The operation
sets `{ price: 9.99 }` in the first document where `fee` is greater
than `2`.

To set the `price` field in all documents where `carrier.fee` is
greater than `2`, use `updateMany()`.

## Learn More

- `find()`
- `$set`
