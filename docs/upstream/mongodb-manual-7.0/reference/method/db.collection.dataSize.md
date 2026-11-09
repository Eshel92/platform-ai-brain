<!-- Converted from reference/method/db.collection.dataSize.txt (reStructuredText). Includes are inlined. -->

# db.collection.dataSize() (mongosh method)

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `size` field returned by the.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Definition

**`db.collection.dataSize()`**

   `collStats` command

:returns: The size in bytes of the collection.

          `Data compression` does not affect
          this value.

To run on a replica set member, `collStats` operations require the member 
to be in `PRIMARY` or `SECONDARY` state. If the member
is in another state, such as `STARTUP2`, the
operation errors.

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
