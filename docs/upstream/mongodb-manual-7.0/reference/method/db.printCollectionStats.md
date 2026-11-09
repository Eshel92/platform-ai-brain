<!-- Converted from reference/method/db.printCollectionStats.txt (reStructuredText). Includes are inlined. -->

# db.printCollectionStats() (mongosh method)

**`db.printCollectionStats()`**

Provides a wrapper around the `db.collection.stats()`
method. Returns statistics from every collection separated by three
hyphen characters.

**Note:**

The `db.printCollectionStats()` method run in `mongosh` does
**not** return JSON. Use `db.printCollectionStats()` for manual inspection, and
`db.collection.stats()` in scripts.

**See also:**

/reference/command/collStats

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
