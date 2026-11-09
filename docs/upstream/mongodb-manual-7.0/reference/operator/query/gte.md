<!-- Converted from reference/operator/query/gte.txt (reStructuredText). Includes are inlined. -->

# $gte (query predicate operator)

   

   

## Definition

**`$gte`**

`$gte` selects documents where the value of the specified
field is greater than or equal (`>=`) to the specified value.

## Compatibility

You can use `$gte` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$gte` operator has the following form:

```javascript
{ field: { $gte: value } }
```

## Behavior

Inequality comparison operators use type bracketing: a comparison on a given BSON type filters out
values of a different type.

## Examples

To create the `inventory` collection used in the examples, run:

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
`quantity` is greater than or equal to `20`:

```javascript
db.inventory.find( { quantity: { $gte: 20 } } )
```

Example output:

```javascript
 {
   _id: ObjectId("61bb51211b83c864e3bbe037"),
   item: 'nuts',
   quantity: 30,
   carrier: { name: 'Shipit', fee: 3 }
 },
 {
   _id: ObjectId("61bb51211b83c864e3bbe038"),
   item: 'bolts',
   quantity: 50,
   carrier: { name: 'Shipit', fee: 4 }
}
```

### Perform an Update Based on Embedded Document Fields

This example sets the `price` field based on a `$gte`
comparison on a field in an embedded document:

```javascript
db.inventory.updateMany(
   { "carrier.fee": { $gte: 2 } }, { $set: { "price": 9.99 } }
)
```

Example output:

```javascript
{
  _id: ObjectId("61bb51211b83c864e3bbe037"),
  item: 'nuts',
  quantity: 30,
  carrier: { name: 'Shipit', fee: 3 },
  price: 9.99
},
{
  _id: ObjectId("61bb51211b83c864e3bbe038"),
  item: 'bolts',
  quantity: 50,
  carrier: { name: 'Shipit', fee: 4 },
  price: 9.99
}
```

The `updateMany()` operation matches an embedded
document named `carrier`, with a subfield named `fee`. It sets
`{ price: 9.99 }` in each document where `fee` is greater than
or equal to `2`.

To set the `price` field in only the first document where
`carrier.fee` is greater than `2`, use
`updateOne()`.

## Learn More

- `find()`
- `$set`
