<!-- Converted from reference/method/db.collection.reIndex.txt (reStructuredText). Includes are inlined. -->

# db.collection.reIndex()

## Definition

**`db.collection.reIndex()`**

**Deprecated since version:** 6.0

Attempting to run the `db.collection.reIndex()` method 
writes a warning message to the log.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `reIndex` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `db.collection.reIndex()` drops all indexes on a
collection and recreates them. This operation may be expensive for
collections that have a large amount of data and/or a large number
of indexes.

**Warning:**

- `db.collection.reIndex()` may only be run on 
  standalone instances. 
- For most users, the `db.collection.reIndex()` command 
  is unnecessary.

## Compatibility

This method is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**Important:**

This command is not supported in MongoDB Atlas clusters.
For information on Atlas support for all commands, 
see Unsupported Commands.

        

## Behavior

For MongoDB 5.0 or later, `db.collection.reIndex()` may only be 
run on standalone instances.

### Resource Locking

`db.collection.reIndex()` obtains an exclusive (W) lock on the 
collection and blocks other operations on the collection until it completes.

For more information on locking in MongoDB, see /faq/concurrency.

**See also:**

/indexes
