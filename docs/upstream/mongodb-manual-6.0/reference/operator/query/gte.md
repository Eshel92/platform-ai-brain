<!-- Converted from reference/operator/query/gte.txt (reStructuredText). Includes are inlined. -->

# $gte

   

   

## Definition

**`$gte`**

`$gte` selects the documents where the value of the
specified field is greater than or equal to (i.e. `>=`) a specified
value (e.g. `value`.)

For most data types, comparison
operators only perform
comparisons on fields where the
BSON type matches the
query value's type. MongoDB supports limited cross-BSON comparison
through type-bracketing.

## Compatibility

You can use `$gte` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
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

## Examples

The following examples use the `inventory` collection. Create the
collection:

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

Select all documents in the `inventory` collection where `quantity`
is greater than or equal to `20`:

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

The following example sets the `price` field based on a `$gte`
comparison against a field in an embedded document.

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

This `updateOne()` operation searches for an
embedded document, `carrier`, with a subfield named `fee`. It sets
`{ price: 9.99 }` in each document where `fee` has a value greater
than or equal to 2.

To set the value of the `price` field in only the first document
where `carrier.fee` is greater than 2, use
`updateOne()`.

**See also:**

- `find()`
- `$set`
