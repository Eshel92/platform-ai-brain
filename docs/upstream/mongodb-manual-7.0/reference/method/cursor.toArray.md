<!-- Converted from reference/method/cursor.toArray.txt (reStructuredText). Includes are inlined. -->

# cursor.toArray() (mongosh method)

**`cursor.toArray()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `toArray()` method returns an array that
contains all the documents from a cursor. The method iterates
completely the cursor, loading all the documents into RAM and
exhausting the cursor.

:returns: An array of documents.

Consider the following example that applies `toArray()`
to the cursor returned from the `find()` method:

```javascript
var allProductsArray = db.products.find().toArray();

if (allProductsArray.length > 0) { printjson (allProductsArray[0]); }
```

The variable `allProductsArray` holds the array of documents returned by
`toArray()`.

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
