<!-- Converted from reference/command/reIndex.txt (reStructuredText). Includes are inlined. -->

# reIndex (database command)

## Definition

**`reIndex`**

**Deprecated since version:** 6.0

Attempting to run the `reIndex` command writes a warning 
message to the log.

**Tip:**

In `mongosh`, this command can also be run through the `db.collection.reIndex` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

The `reIndex` command drops all indexes on a
collection and recreates them. This operation may be expensive for
collections that have a large amount of data and/or a large number
of indexes. 

**Warning:**

- `reIndex` may only be run on standalone 
  instances. 
- For most users, the `reIndex` command is unnecessary.

## Compatibility

This command is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**Important:**

This command is not supported in MongoDB Atlas clusters.
For information on Atlas support for all commands, 
see Unsupported Commands.

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     reIndex: <collection> 
   }
)
```

## Command Fields

The command takes the following fields:

| Field | Description |
|---|---|
| reIndex | The name of the collection to reindex. |

 

## Behavior

For MongoDB 5.0 or later, `reIndex` may only be run on 
standalone instances.

### Resource Locking

`reIndex` obtains an exclusive (W) lock on the collection and blocks 
other operations on the collection until it completes.

For more information on locking in MongoDB, see /faq/concurrency.

**See also:**

/core/index-creation for more information on the
behavior of indexing operations in MongoDB.
