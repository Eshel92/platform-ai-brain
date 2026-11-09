<!-- Converted from reference/method/sh.enableSharding.txt (reStructuredText). Includes are inlined. -->

# sh.enableSharding()

## Definition

**`sh.enableSharding(database, primaryShard)`**

**Note:**

**Changed in version:** 6.0

Starting in MongoDB 6.0, this method is **not** required to
shard a collection.

Explicitly creates a database.  Use the `mongosh` method
`sh.shardCollection()` to shard collections on the database.
The `mongosh` method `sh.enableSharding()` wraps the
`enableSharding` command.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `enableSharding` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `sh.enableSharding` has the following form:

```javascript
sh.enableSharding( 
   <database>,
   <primary shard>  // Optional. 
)
```

### Parameter

The `sh.enableSharding()` method takes the following parameter:

* - Parameter
  - Type
  - Description

* - database

  - String

  - .. _method-enableSharding-db:

    The name of the database you want to create.

* - primaryShard

  - String

  - .. _method-enableSharding-primaryShard:

    Optional. The primary shard for the
    database; the primary shard contains the unsharded collection
    for this database. In general, rather than explicitly specifying
    the primary shard, it is recommended to let the balancer select
    the primary shard instead.

    **Warning:** Tip

    In general, you should not need to specify the primary shard. Allow
    the balancer to select the primary shard instead.

## Behavior

### Write Concern

`mongos` uses
`"majority"` for the 
`enableSharding` command and its helper
`sh.enableSharding()`.

### Primary Shard

In general, you should not need to specify the primaryShard in the command. Instead, allow the
balancer to select the primary shard. 

However, if you do specify the primary shard for a database and the database
is already enabled for sharding with a different primary shard, the
operation returns an error and the primary shard for the database
remains as before. To change the primary shard for a database, use the
`movePrimary` command instead.

## Example

The following example, run from a `mongos`, explicitly
creates the `shardTest` database:

```javascript
sh.enableSharding("shardTest")
```

To verify, run `sh.status()`.

**See also:**

- `sh.shardCollection()`
- /tutorial/deploy-shard-cluster
