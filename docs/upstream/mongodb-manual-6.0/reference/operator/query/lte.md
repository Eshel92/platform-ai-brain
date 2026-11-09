<!-- Converted from reference/operator/query/lte.txt (reStructuredText). Includes are inlined. -->

# $lte

## Definition

**`$lte`**

*Syntax*: `{ field: { $lte: value } }`

`$lte` selects the documents where the value of the
`field` is less than or equal to (i.e. `<=`) the specified
`value`.

For most data types, comparison
operators only perform
comparisons on fields where the
BSON type matches the
query value's type. MongoDB supports limited cross-BSON comparison
through type-bracketing.

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

Consider the following example:

```javascript
db.inventory.find( { quantity: { $lte: 20 } } )
```

This query will select all documents in the `inventory` collection
where the `quantity` field value is less than or equal to `20`.

Example output:

```javascript
{
  _id: ObjectId("61ba453ffe687fce2f04241c"),
  item: 'washers',
  quantity: 10,
  carrier: { name: 'Shipit', fee: 1 }
}
```

### Perform an Update Based on Embedded Document Fields

The following example sets the `price` field based on a `$lte`
comparison against a field in an embedded document.

```javascript
db.inventory.updateMany(
   { "carrier.fee": { $lte: 5 } }, { $set: { price: 9.99 } }
)
```

Example output:

```javascript
{
  _id: ObjectId("61ba453ffe687fce2f04241a"),
  item: 'nuts',
  quantity: 30,
  carrier: { name: 'Shipit', fee: 3 },
  price: 9.99
},
{
  _id: ObjectId("61ba453ffe687fce2f04241b"),
  item: 'bolts',
  quantity: 50,
  carrier: { name: 'Shipit', fee: 4 },
  price: 9.99
},
{
  _id: ObjectId("61ba453ffe687fce2f04241c"),
  item: 'washers',
  quantity: 10,
  carrier: { name: 'Shipit', fee: 1 },
  price: 9.99
}
```

This `updateMany()` operation searches for an
embedded document, `carrier`, with a subfield named `fee`. It sets
`{ price: 9.99 }` in each document where `fee` has a value less
than or equal to 5.

To set the value of the `price` field in only the first document
where `carrier.fee` is less than or equal to 5, use
`updateOne()`.

**See also:**

- `find()`
- `$set`
