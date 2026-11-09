<!-- Converted from reference/method/cursor.showRecordId.txt (reStructuredText). Includes are inlined. -->

# cursor.showRecordId() (mongosh method)

## Definition

**`cursor.showRecordId()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Appends the `$recordId` field to documents returned by a query.
`$recordId` is the internal key that uniquely identifies a document
in a collection. `$recordId` format:

```javascript
'$recordId': Long(<int>)
```

:returns: A modified cursor object that contains the document fields
          and the appended `$recordId` field.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Example

The example uses this `pizzas` collection:

```javascript
db.pizzas.insertMany( [
   { type: "pepperoni", size: "small", price: 4 },
   { type: "cheese", size: "medium", price: 7 },
   { type: "vegan", size: "large", price: 8 }
] )
```

The following `find()` example uses
`showRecordId()` to append the `$recordId` to the
`pizza` document fields in the output:

```javascript
db.pizzas.find().showRecordId()
```

Example output:

```javascript
[
   {
      _id: ObjectId("62ffc70660b33b68e8f30435"),
      type: 'pepperoni',
      size: 'small',
      price: 4,
      '$recordId': Long("1")
   },
   {
      _id: ObjectId("62ffc70660b33b68e8f30436"),
      type: 'cheese',
      size: 'medium',
      price: 7,
      '$recordId': Long("2")
   },
   {
      _id: ObjectId("62ffc70660b33b68e8f30437"),
      type: 'vegan',
      size: 'large',
      price: 8,
      '$recordId': Long("3")
   }
]
```
