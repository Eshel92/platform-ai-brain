<!-- Converted from reference/method/cursor.objsLeftInBatch.txt (reStructuredText). Includes are inlined. -->

# cursor.objsLeftInBatch()

**`cursor.objsLeftInBatch()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

`cursor.objsLeftInBatch()` returns the number of
documents remaining in the current batch.

The MongoDB instance returns response in batches. To retrieve
all the documents from a cursor may require multiple batch
responses from the MongoDB instance. When there are no more
documents remaining in the current batch, the cursor will retrieve
another batch to get more documents until the cursor exhausts.

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
