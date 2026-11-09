<!-- Converted from reference/method/cursor.tryNext.txt (reStructuredText). Includes are inlined. -->

# cursor.tryNext()

**`cursor.tryNext()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

:returns: The next document in the cursor returned by the
          `db.collection.find()` method or `null`.
             

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
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

`cursor.tryNext()` is a special case of the `cursor.next()`
method that returns the next element in the iteration if available or
else `null`.
