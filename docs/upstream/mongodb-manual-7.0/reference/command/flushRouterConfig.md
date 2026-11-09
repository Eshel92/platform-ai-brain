<!-- Converted from reference/command/flushRouterConfig.txt (reStructuredText). Includes are inlined. -->

# flushRouterConfig (database command)

## Definition

**`flushRouterConfig`**

`flushRouterConfig` marks the cached routing table for a 
sharded cluster as stale, causing the next operation that requests
the routing table to refresh the cache. Management of the routing
table cache is generally handled automatically by the cluster. You
should only need to run the `flushRouterConfig` command
manually in specific instances, as indicated under
flushrouterconfig-considerations.

**Note:**

Running `flushRouterConfig` is no longer required after executing 
the `movePrimary` or `dropDatabase` commands. These 
two commands now automatically refresh a sharded cluster's routing table as 
needed when run.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `flushRouterConfig` is available on both
`mongos` and `mongod` instances, and has the
following syntax:  

- Flush the cache for a specified collection when passed in a
  collection namespace parameter:

  ```javascript
  db.adminCommand(
     { 
       flushRouterConfig: "<db.collection>" 
     } 
  )
  ```

- Flush the cache for a specified database and all of its collections
  when passed in a database namespace parameter:

  ```javascript
  db.adminCommand(
     { 
       flushRouterConfig: "<db>" 
     } 
  ) 
  ```

- Flush the cache for all databases and their collections when run
  without a parameter or passed in a non-string scalar value
  (e.g. `1`):

  ```javascript
  db.adminCommand("flushRouterConfig")
  db.adminCommand( 
     { 
       flushRouterConfig: 1 
     } 
  )
  ```

## Access Control

The `flushRouterConfig` command requires the
`flushRouterConfig` privilege action on the `cluster`
resource.

This privilege action is also available to users with the
following roles:

- `clusterManager`

- `hostManager`

## Considerations

Generally, a sharded cluster's routing table is automatically refreshed
as needed as part of normal operation. However, you should manually
issue the `flushRouterConfig` command before running the 
`db.collection.getShardDistribution()` command. This ensures that the 
command returns the most up-to-date information.
