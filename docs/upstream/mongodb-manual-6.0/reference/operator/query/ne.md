<!-- Converted from reference/operator/query/ne.txt (reStructuredText). Includes are inlined. -->

# $ne

## Definition

**`$ne`**

`$ne` selects the documents where the value of the
specified field is not equal to the specified value.
This includes documents that do not contain the specified field. 

For comparison of different BSON type values, see the specified
BSON comparison order.

## Compatibility

You can use `$ne` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$ne` operator has the following form:

```javascript
{ field: { $ne: value } }
```

**Note:**

If the value of the `$ne` operator is null, see
non-equality-filter for more information. 

## Examples

The following examples use the `inventory` collection. To create the
collection run the following `insertMany()` 
command in `mongosh`:

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

### Match Document Fields That Are Not Equal

Select all documents in the `inventory` collection where `quantity`
is not equal to `20`. This query also selects documents that do not
have the `quantity` field:

```javascript
db.inventory.find( { quantity: { $ne: 20 } } )
```

Output:

```javascript
{
 _id: ObjectId("61ba667dfe687fce2f042420"),
 item: 'nuts',
 quantity: 30,
 carrier: { name: 'Shipit', fee: 3 }
},
{
 _id: ObjectId("61ba667dfe687fce2f042421"),
 item: 'bolts',
 quantity: 50,
 carrier: { name: 'Shipit', fee: 4 }
},
{
 _id: ObjectId("61ba667dfe687fce2f042422"),
 item: 'washers',
 quantity: 10,
 carrier: { name: 'Shipit', fee: 1 }
}
```

The SQL equivalent to this query is:

```sql
SELECT * FROM INVENTORY WHERE QUANTITIY != 20
```

### Update Based on Not Equal Embedded Document Fields

The following example sets the `price` field based on a `$ne`
comparison against a field in an embedded document. The 
`updateMany()` operation searches for an
embedded document, `carrier`, with a subfield named `fee`. It uses 
`$set` to update the `price` field to `9.99` in each 
document where `fee` has a value that does not equal `1` or 
where the `fee` subfield does not exist:

```javascript
db.inventory.updateMany( 
   { "carrier.fee" : { $ne: 1 } }, 
   { $set: { "price": 9.99 } } 
)
```

Output:

```javascript
{
 _id: ObjectId("61ba66e2fe687fce2f042423"),
 item: 'nuts',
 quantity: 30,
 carrier: { name: 'Shipit', fee: 3 },
 price: 9.99
},
{
 _id: ObjectId("61ba66e2fe687fce2f042424"),
 item: 'bolts',
 quantity: 50,
 carrier: { name: 'Shipit', fee: 4 },
 price: 9.99
},
{
 _id: ObjectId("61ba66e2fe687fce2f042425"),
 item: 'washers',
 quantity: 10,
 carrier: { name: 'Shipit', fee: 1 }
}
```

The SQL equivalent to this query is:

```sql
UPDATE INVENTORY SET PRICE = '9.99' WHERE carrierfee != 1
```

The inequality operator `$ne` is *not* very selective since
it often matches a large portion of the index. As a result, in many
cases, a `$ne` query with an index may perform no better
than a `$ne` query that must scan all documents in a
collection. See also read-operations-query-selectivity.

### Arrays

When comparing arrays, `$ne` matches documents where the document
array differs from the array specified in `$ne`. Specifically, `$ne`
matches any of these documents where the arrays:

- have different element values or strings
- have elements in a different order
- have a different number of elements
- are missing from a document

For example, the following query returns  `inventory` documents where
the `type` array differs from `[ "hardware", "fasteners" ]`:

```javascript
db.inventory.find( { type: { $ne: [ "hardware", "fasteners" ] } } )
```

The following complete example adds a `type` array to two
`inventory` documents and runs a query with `$ne`:

```javascript
// Update the nuts document to include a type array
db.inventory.updateOne(
   { item: "nuts" },
   { $set: { type: [ "hardware" ] } }
)

// Update the bolts document to include a type array
db.inventory.updateOne(
   { item: "bolts" },
   { $set: { type: [ "hardware", "fasteners" ] } }
)

// Find documents where the type array differs from [ "hardware", "fasteners" ]
db.inventory.find( { type: { $ne: [ "hardware", "fasteners" ] } } )
```

Output shows the `nuts` document because the array differs from ``[
"hardware", "fasteners" ]`, and the `washers`` document because it
doesn't have a `type` array:

```javascript
[
  {
    _id: ObjectId('679d26907c5a58595234305c'),
    item: 'nuts',
    quantity: 30,
    carrier: { name: 'Shipit', fee: 3 },
    type: [ 'hardware' ]
  },
  {
    _id: ObjectId('679d26907c5a58595234305e'),
    item: 'washers',
    quantity: 10,
    carrier: { name: 'Shipit', fee: 1 }
  }
]
```

The following query reverses the elements in the array:

```javascript
db.inventory.find( { type: { $ne: [ "fasteners", "hardware" ] } } )
```

Because the `type` array in the `bolts` document is ``[ "hardware",
"fasteners" ]`, which differs from `[ "fasteners", "hardware" ]``, the
query returns the `bolts` document in addition to the `nuts` and
`washers` documents:

```javascript
[
   {
      _id: ObjectId('679d26907c5a58595234305c'),
      item: 'nuts',
      quantity: 30,
      carrier: { name: 'Shipit', fee: 3 },
      type: [ 'hardware' ]
   },
   {
      _id: ObjectId('679d26907c5a58595234305d'),
      item: 'bolts',
      quantity: 50,
      carrier: { name: 'Shipit', fee: 4 },
      type: [ 'hardware', 'fasteners' ]
   },
   {
      _id: ObjectId('679d26907c5a58595234305e'),
      item: 'washers',
      quantity: 10,
      carrier: { name: 'Shipit', fee: 1 }
   }
]
```

`$ne` matches documents where the array doesn't contain the specified
value and documents that don't have the array. For example:

```javascript
db.inventory.find( { type: { $ne: "fasteners" } } )
```

The query returns the `nuts` document because the array ``[ "hardware"
]` differs from `"fasteners"``. Also, the query returns the
`washers` document because the document doesn't have a `type` array.
Query output:

```javascript
[
   {
      _id: ObjectId('679d26907c5a58595234305c'),
      item: 'nuts',
      quantity: 30,
      carrier: { name: 'Shipit', fee: 3 },
      type: [ 'hardware' ]
   },
   {
      _id: ObjectId('679d26907c5a58595234305e'),
      item: 'washers',
      quantity: 10,
      carrier: { name: 'Shipit', fee: 1 }
   }
]
```

## Learn More

- sql-to-mongodb-mapping
- read-operations-query-document
