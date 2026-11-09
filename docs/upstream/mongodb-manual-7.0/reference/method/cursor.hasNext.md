<!-- Converted from reference/method/cursor.hasNext.txt (reStructuredText). Includes are inlined. -->

# cursor.hasNext() (mongosh method)

**`cursor.hasNext()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

:returns: Boolean.

`cursor.hasNext()` returns `true` if the cursor returned by
the `db.collection.find()` query can iterate further to
return more documents. If the client-side cursor batch is empty and the
server has more data, `hasNext()` fetches the next batch from the server.

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
