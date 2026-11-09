<!-- Converted from reference/method/cursor.map.txt (reStructuredText). Includes are inlined. -->

# cursor.map() (mongosh method)

**`cursor.map(function)`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Applies a `function` to each document visited by the cursor and
collects the return values from successive applications of the
`function` into a `Cursor` object.

The `cursor.map()` method has the following parameter:

| Parameter | Type | Description |
|---|---|---|
| `function` | function | A function to apply to each document visited by the cursor. |

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

## Behavior

`cursor.map()` returns a `Cursor` object. Note that
`.map()` only converts the type, it does not create a new cursor. You
can convert the `Cursor` object to an `Array` with `.toArray()`.  

## Examples

These examples refer to the products collection:

```javascript
db.products.insertMany([ 
   { _id: 1, name: 'widget', price: 10.89 },
   { _id: 2, name: 'thing', price: 11.24 },
   { _id: 3, name: 'moppet', price: 8 },
   { _id: 4, name: 'cosa', price: 24.19 }
])
```

### Return a Value From a Collection

Get the product names.

```javascript
db.products.find().map( function(p) { return p.name; } ) ;
```

### Return Results as an `Array`

Calculate a discounted sale price and return the results as an array. 

```javascript
var salePrices = db.products.find().map( function(p) { return p.price * .9 } ).toArray() ;
```

Confirm that the output is an `Array`

```javascript
salePrices.constructor.name
```

**See also:**

`cursor.forEach()` for similar functionality.
