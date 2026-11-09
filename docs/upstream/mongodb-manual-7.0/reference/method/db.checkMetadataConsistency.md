<!-- Converted from reference/method/db.checkMetadataConsistency.txt (reStructuredText). Includes are inlined. -->

# db.checkMetadataConsistency() (mongosh method)

## Definition

**`db.checkMetadataConsistency(options)`**

Performs a series of consistency checks on sharding metadata for the cluster 
or database.   This method returns a cursor with either all or a batch of
the inconsistency results found.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `checkMetadataConsistency` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Run this method after major maintenance operations, such as upgrades and
downgrades, or to check if the cluster metadata is inconsistent or
corrupted due to bugs in previous releases of MongoDB.

By default, the method does not check indexes for consistency across the shards.
Index checks can return false positive inconsistencies if they run concurrent
with operations that create, delete, or modify indexes.  To check indexes
with this method, set the `checkIndexes` option.

By default, the method checks sharding metadata for the given database.
If run on the `admin` database, it instead checks sharding metadata
for the entire cluster.

For more information on the inconsistencies this method searches for,
see inconsistency-types.

:returns: This method returns a cursor with a `documents` array, 
   which contains a document for each inconsistency found in 
   the sharding metadata.

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

**Note:**

The `checkMetadataConsistency` helper is executable only when connecting to
`mongos`. `mongod` does not support this method. 

## Syntax

The `db.checkMetadataConsistency` method has the following syntax:

```javascript
db.checkMetadataConsistency( { <options> } )
```

The `options` document can take the following fields and values:

| Field | Type | Description |
|---|---|---|
| `checkIndexes` | boolean | Sets whether the command also checks indexes in sharding metadata. By default, this operation is disabled, because if it can return false positives inconsistencies when run concurrent with operations that create, delete, or modify indexes.  Only check indexes at times when you know these operations are unlikely to occur. |
| `cursor` | document | Configures the return cursor. |
| `cursor.batchSize` | integer | Maximum number of sharding metadata inconsistency documents to include in each batch. |

## Example

### Perform a Consistency Check on the Database

To perform consistency checks on a database, call the 
`db.checkMetadataConsistency()` method:

```javascript
use library
db.checkMetadataConsistency()
```

Output:

```json
{
   cursorHasMore: false,
   documents: [
      {
         type: "MisplacedCollection",
         description: "Unsharded collection found on shard different from database primary shard",
         details: {
            namespace: "library.authors",
            shard: "shard02",
            localUUID: new UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4")
         }
      }
   ],
}
```

 

### Perform Consistency Checks on the Cluster

To perform consistency checks on a cluster, call the 
`db.checkMetadataConsistency()` method from the `admin` database:

```javascript
use admin
db.checkMetadataConsistency()
```

Output:

```json
{
   cursorHasMore: false,
   documents: [
      {
         type: "MisplacedCollection",
         description: "Unsharded collection found on shard different from database primary shard",
         details: {
            namespace: "library.authors",
            shard: "shard02",
            localUUID: new UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4")
         }
      }
   ],
}
```
