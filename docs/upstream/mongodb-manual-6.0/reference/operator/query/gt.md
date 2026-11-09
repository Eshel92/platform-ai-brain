<!-- Converted from reference/operator/query/gt.txt (reStructuredText). Includes are inlined. -->

# $gt

## Definition

**`$gt`**

`$gt` selects those documents where the value of the
specified field is greater than (i.e. `>`) the specified value.

For most data types, comparison
operators only perform
comparisons on fields where the
BSON type matches the
query value's type. MongoDB supports limited cross-BSON comparison
through type-bracketing.

## Compatibility

You can use `$gt` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$gt` operator has the following form:

```javascript
{ field: { $gt: value } }
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
is greater than `20`:

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

The following example sets the `price` field based on a `$gt`
comparison against a field in an embedded document.

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

This `updateOne()` operation searches for an
embedded document, `carrier`, with a subfield named `fee`. It sets
`{ price: 9.99 }` in the first document it finds where `fee` has a
value greater than 2.

To set the value of the `price` field in *all* documents where
`carrier.fee` is greater than 2, use
`updateMany()`.

**See also:**

- `find()`
- `$set`
