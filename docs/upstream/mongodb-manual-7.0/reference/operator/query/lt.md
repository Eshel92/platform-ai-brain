<!-- Converted from reference/operator/query/lt.txt (reStructuredText). Includes are inlined. -->

# $lt (query predicate operator)

## Definition

**`$lt`**

*Syntax*: `{ field: { $lt: value } }`

`$lt` selects the documents where the value of the
`field` is less than (i.e. `<`) the specified `value`.

## Behavior

Inequality comparison operators use type bracketing: a comparison on a given BSON type filters out
values of a different type.

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
is less than `20`:

```javascript
db.inventory.find( { quantity: { $lt: 20 } } )
```

Example output:

```javascript
{
  _id: ObjectId("61ba634dfe687fce2f04241f"),
  item: 'washers',
  quantity: 10,
  carrier: { name: 'Shipit', fee: 1 }
}
```

### Perform an Update Based on Embedded Document Fields

The following example sets the `price` field based on a `$lt`
comparison against a field in an embedded document.

```javascript
db.inventory.updateMany( { "carrier.fee": { $lt: 20 } }, { $set: { price: 9.99 } } )
```

Example output:

```javascript
{
  _id: ObjectId("61ba634dfe687fce2f04241d"),
  item: 'nuts',
  quantity: 30,
  carrier: { name: 'Shipit', fee: 3 },
  price: 9.99
},
{
  _id: ObjectId("61ba634dfe687fce2f04241e"),
  item: 'bolts',
  quantity: 50,
  carrier: { name: 'Shipit', fee: 4 },
  price: 9.99
},
{
  _id: ObjectId("61ba634dfe687fce2f04241f"),
  item: 'washers',
  quantity: 10,
  carrier: { name: 'Shipit', fee: 1 },
  price: 9.99
}
```

This `updateMany()` operation searches for an
embedded document, `carrier`, with a subfield named `fee`. It sets
`{ price: 9.99 }` in each document where `fee` has a value less than
20.

To set the value of the `price` field in only the first document
where `carrier.fee` is less than 20, use
`updateOne()`.

**See also:**

- `find()`
- `$set`
