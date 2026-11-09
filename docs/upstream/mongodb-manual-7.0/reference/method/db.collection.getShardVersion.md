<!-- Converted from reference/method/db.collection.getShardVersion.txt (reStructuredText). Includes are inlined. -->

# db.collection.getShardVersion() (mongosh method)

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Definition

**`db.collection.getShardVersion()`**

This method returns information regarding the state of data in a
sharded cluster that is useful when diagnosing underlying issues
with a sharded cluster.

For internal and diagnostic use only.

## Compatibility

This method is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
