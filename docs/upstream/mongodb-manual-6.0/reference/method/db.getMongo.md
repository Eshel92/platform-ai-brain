<!-- Converted from reference/method/db.getMongo.txt (reStructuredText). Includes are inlined. -->

# db.getMongo()

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

**`db.getMongo()`**

:returns: The current database connection.

`db.getMongo()` runs when the shell initiates. Use this
command to test that `mongosh` has a connection to
the proper database instance.

**Note:**

The legacy `mongo` shell has a sub-command,
`db.getMongo().setSecondaryOk()`, which is not available in
`mongosh`. In `mongosh`, use
`Mongo.setReadPref()` instead.

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
