<!-- Converted from reference/command/enableSharding.txt (reStructuredText). Includes are inlined. -->

# enableSharding

## Definition

**`enableSharding`**

**Note:**

**Changed in version:** 6.0

Starting in MongoDB 6.0, this command is **not** required to
shard a collection.

The `enableSharding` command explicitly creates a database.

   helper method

**Tip:**

In `mongosh`, this command can also be run through the `sh.enableSharding`.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in serverless instances.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

- *Recommended*.  Specify the database to create:

  ```javascript
  db.adminCommand( 
     { 
       enableSharding: "<database name>"
     } 
  )
  ```

- Optionally, you can include the primary shard specification in the command, 
  although this is not recommended:

  ```javascript
  db.adminCommand( 
     { 
       enableSharding: "<database name>",
       primaryShard: "<shard name>"  
     } 
  )
  ```

You can only run the `enableSharding` command on the `admin` database
from a `mongos` instance.

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - enableSharding
  - String
  - .. _cmd-enableSharding-db:

    The database you want to use.  The database is created if it
    does not exist.

* - primaryShard
  - String
  - .. _cmd-enableSharding-primaryShard:

    Optional. The primary shard for the
    database; the primary shard contains the unsharded collection
    for this database. In general, rather than explicitly specifying
    the primary shard, it is recommended to let the balancer select
    the primary shard instead.

    **Warning:** Tip

    In general, you should not need to specify the primary shard. Allow
    the balancer to select the primary shard instead.

### Returns

The command returns a document that contains status of the operation.

## Behavior

### Write Concern

`mongos` uses
`"majority"` for the 
`enableSharding` command and its helper
`sh.enableSharding()`.

### Primary Shard

In general, you should not need to specify the primaryShard in the command. Instead, allow the
balancer to select the primary shard. 

However, if you do specify the primaryShard in the command for a database and the database is already sharding enabled
with a different primary shard, the operation returns an error and the
primary shard for the database remains as before. To change the primary
shard for a database, use `movePrimary` instead.

## Example

The following command, run from a `mongos`, creates the 
the `shardTest` database:

```javascript
db.adminCommand( { enableSharding: "shardTest" } )
```

**See also:**

- /tutorial/deploy-shard-cluster
- `sh.shardCollection()`
