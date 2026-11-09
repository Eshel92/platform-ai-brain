<!-- Converted from reference/command/checkMetadataConsistency.txt (reStructuredText). Includes are inlined. -->

# checkMetadataConsistency (database command)

## Definition

**`checkMetadataConsistency`**

Performs a series of consistency checks on sharding metadata for a cluster,
database, or collection.  The command returns a cursor with either all or a
batch of the inconsistency results found.

   `db.collection.checkMetadataConsistency`, or
   `sh.checkMetadataConsistency` helper methods

**Tip:**

In `mongosh`, this command can also be run through the `db.checkMetadataConsistency`,.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

Run this command after major maintenance operations, such as upgrades and
downgrades, to check the state of the catalog.

By default, the command does not check indexes for consistency across 
the shards.  To check indexes, set the `checkIndexes` option.

**New in version:** 7.0

## Compatibility

This command is available in deployments hosted in the following environments: 

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

**Note:**

The `checkMetadataConsistency` command is executable only when connecting to
`mongos`. `mongod` does not support this command. 

   

## Syntax

-  To check the entire cluster for sharding metadata inconsistencies, run
   the command from the `admin` database.

   ```javascript
   db.adminCommand( {
      checkMetadataConsistency: 1
   } )
   ```

-  To check the database for sharding metadata inconsistencies, run the command
   from the database context:

   ```javascript
   use cars
   db.runCommand( {
      checkMetadataConsistency: 1
   } )
   ```

-  To check a collection for sharding metadata inconsistencies, run the command
   with the collection name:

   ```javascript
   use library
   db.runCommand( {
      checkMetadataConsistency: "authors",
   } )
   ```

### Command Fields

| Field | Type | Description |
|---|---|---|
| `checkMetadataConsistency` | integer or string | Specifies the collection to check. `1` Sets the command to check all collections in the database for metadata inconsistencies. If run on the `admin` database, it checks all collections in all databases. `"<collection>"` Sets the collection to check for metadata inconsistencies. |
| `checkIndexes` | boolean | Sets whether the command also checks indexes in sharding metadata. For more information, see checkMetadataConsistency-indexes. |
| `cursor` | document | Configures the return cursor. |
| `cursor.batchSize` | integer | Maximum number of inconsistency results to include in each batch. |
| `dbMetadataLockMaxTimeMS` | integer | Optional. Maximum time in milliseconds that the command is allowed to wait to acquire a database lock. You can also use this field with max-time-ms. For example, if you set `dbMetadataLockMaxTimeMs` to 500 and `maxTimeMs` to 5000, the operation waits 500 milliseconds to try to acquire the database lock and waits a total of 5000 milliseconds for the entire operation to finish. |

### Output

The `checkMetadataConsistency` command returns a cursor with a document for
each inconsistency found in sharding metadata. To learn more, see 
inconsistency-types.

The return document has the following fields:

| Field | Type | Description |
|---|---|---|
| `cursor` | document | Cursor with the results of the inconsistency checks. |
| `cursor.id` | integer | A 64-bit integer indicated the cursor ID.  Use the `cursor.id` value with the `getMore` command to retrieve the next batch of inconsistencies. If the cursor returns an ID of `0`, it indicates that there are no more batches of information. |
| `cursor.ns` | string | The database and collection checked for inconsistencies. |
| `cursor.firstBatch` | array | Results of metadata consistency checks. |
| `ok` | boolean | Indicates whether the command was successful. |

## Behavior

### Batch Results

The `checkMetadataConsistency` command returns results in batches. To
customize the batch size, the `batchSize` option:

```javascript
var cur = db.runCommand( {
   checkMetadataConsistency: 1,
   cursor: {
      batchSize: 10
   }
} )
```

If the `cursor.id` field is greater than 0, you can use with the
`getMore` command to retrieve the next batch of results.

### Check Indexes

The `checkMetadataConsistency` command does not check indexes by default.  
To check metadata consistency and indexes, use the `checkIndexes` option:

```javascript
db.runCommand( {
   checkMetadataConsistency: 1,
   checkIndexes: true
} )
```

## Example

Use `runCommand` to run the `checkMetadataConsistency` command:

```javascript
db.runCommand( { checkMetadataConsistency: 1 } )
```

Example Output:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "MisplacedCollection",
            description: "Unsharded collection found on shard different from database primary shard",
            details: {
               namespace: "test.authors",
               shard: "shard02",
               localUUID: new UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4")
            }
         }
      ],
   },
   ok: 1
}
```
