<!-- Converted from reference/method/db.hello.txt (reStructuredText). Includes are inlined. -->

# db.hello() (mongosh method)

**`db.hello()`**

**New in version:** 5.0

Returns a document that describes the role of the `mongod`
instance.

If the `mongod` is a member of a replica set, then
the `isWritablePrimary` and `secondary`
fields report if the instance is the primary or if it is a
secondary member of the replica set.

**See also:**

`hello` for the complete documentation of
the output of `db.hello()`.

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
