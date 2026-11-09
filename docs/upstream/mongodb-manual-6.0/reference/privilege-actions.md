<!-- Converted from reference/privilege-actions.txt (reStructuredText). Includes are inlined. -->

# Privilege Actions

                    

Privilege actions define the operations a user can perform on a resource. A MongoDB privilege comprises a
resource and the permitted actions. This page lists
available actions grouped by common purpose.

MongoDB provides built-in roles with pre-defined pairings of resources and
permitted actions. For lists of the actions granted, see:

- built-in-roles. 
- Built-In Roles on Atlas.

To define custom roles, see:

- Create a User-Defined Role in Self-Managed Deployments.
- Create User-Defined Roles in Atlas.

## Query and Write Actions

**`find`**

User can perform the following commands, and their equivalent helper methods:

- `aggregate` for all pipeline operations **except**
  `$collStats`, `$out`, and
  `$indexStats`.
- `count`
- `dataSize`
- `distinct`
- `filemd5`
- `find`
- `getMore`
- `killCursors`, provided that the cursor is associated
  with a currently authenticated user.
- `listCollections`
- `listIndexes`
- `mapReduce` with the `{out: inline}` option.
- `resetError` (*Removed in MongoDB 5.0*)

Required for the query portion of the `mapReduce` command and
`db.collection.mapReduce` helper method when outputting
to a collection.

Required for the query portion of the `findAndModify` command
and `db.collection.findAndModify` helper method.

Required on the *source* collection for the `cloneCollectionAsCapped`
and `renameCollection` commands and the
`db.collection.renameCollection()` helper method.

If the user does not have the `listDatabases`
privilege action, users can run the `listDatabases`
command to return a list of databases for which the user has
privileges (including databases for which the user has privileges
on specific collections) if the command is run with
`authorizedDatabases` option unspecified or set to `true`.

Apply this action to database or collection resources.

**`insert`**

User can perform the following commands and their equivalent methods:

- `insert`
- `create`

Required for the output portion of the `mapReduce`
command and `db.collection.mapReduce()` helper method when
outputting to a collection.

Required for the `aggregate` command and
`db.collection.aggregate()` helper method when using the
`$out` or `$merge` pipeline operator.

Required for the `update` and `findAndModify`
commands and equivalent helper methods when used with the `upsert`
option.

Required on the *destination* collection for the following
commands and their helper methods:

- `cloneCollectionAsCapped`
- `renameCollection`

Apply this action to database or collection resources.

**`remove`**

User can perform the `delete` command and equivalent
helper method.

Required for the write portion of the `findAndModify`
command and `db.collection.findAndModify()` method.

Required for the `mapReduce` command and
`db.collection.mapReduce()` helper method when you specify
the `replace` action when outputting to a collection.

Required for the `aggregate` command and
`db.collection.aggregate()` helper method when using the
`$out` pipeline operator.

Apply this action to database or collection resources.

**`update`**

User can perform the `update` command and equivalent
helper methods.

Required for the
`mapReduce` command and `db.collection.mapReduce()`
helper method when outputting to a collection
without specifying the `replace` action.

Required for the `findAndModify` command and
`db.collection.findAndModify()` helper method.

Apply this action to database or collection resources.

**`bypassDocumentValidation`**

Users can bypass schema validation on commands and methods that support
the `bypassDocumentValidation` option. The following commands and
their equivalent methods support bypassing schema validation:

- `aggregate`
- `applyOps`
- `findAndModify`
- `insert`
- `mapReduce`
- `update`

Apply this action to database or collection resources.

**`useUUID`**

User can execute the following commands using a
UUID (Universally Unique Identifier) as if it were a
namespace:

- `find`
- `listIndexes`

For example, this privilege authorizes a user to run the
following command which executes a `find` command on a
collection with the given UUID. In order to be successful, this
operation also requires that the user is authorized to execute the
`find` command on the collection namespace corresponding to the given
UUID.

```javascript
db.runCommand({find: UUID("123e4567-e89b-12d3-a456-426655440000")})
```

For more information on collection UUIDs, see
Collections.

Apply this action to the `cluster` resource.

## Database Management Actions

**`changeCustomData`**

User can change the custom information of any user in the given
database. Apply this action to database resources.

**`changeOwnCustomData`**

Users can change their own custom information. Apply this action to
database resources. See also
/tutorial/change-own-password-and-custom-data.

**`changeOwnPassword`**

Users can change their own passwords. Apply this action to database
resources. See also
/tutorial/change-own-password-and-custom-data.

**`changePassword`**

User can change the password of any user in the given database. Apply
this action to database resources.

**`createCollection`**

User can perform the `db.createCollection()` method. Apply this
action to database or collection resources.

**`createIndex`**

Provides access to the `db.collection.createIndex()` method
and the `createIndexes` command.
Apply this action to database or collection resources.

**`createRole`**

User can create new roles in the given database. Apply this action to
database resources.

**`createUser`**

User can create new users in the given database. Apply this action to
database resources.

**`dropCollection`**

User can perform the `db.collection.drop()` method. Apply this
action to database or collection resources.

**`dropRole`**

User can delete any role from the given database. Apply this action to
database resources.

**`dropUser`**

User can remove any user from the given database. Apply this action to
database resources.

**`enableProfiler`**

User can perform the `db.setProfilingLevel()` method. Apply
this action to database resources.

**`grantRole`**

User can grant any role in the database to any user from any database
in the system. Apply this action to database resources.

**`killCursors`**

Users can always terminate their own cursors, regardless of whether the users 
have the privilege to `killCursors`. 

**`killAnyCursor`**

User can kill **any** cursor, even cursors created by other users.
Apply this action to collection resources.

**`planCacheIndexFilter`**

User can run the `planCacheClearFilters`,
`planCacheListFilters`, and
`planCacheSetFilter` commands. Apply the
`planCacheIndexFilter` action to collection resources.

**`revokeRole`**

User can remove any role from any user from any database in the system.
Apply this action to database resources.

**`setAuthenticationRestriction`**

User can specify the
authenticationRestrictions
field in the `user` document when running the following commands:

- createUser
- updateUser

User can specify the `authenticationRestrictions` field in the
`role` document when running the following commands:

- createRole
- updateRole

**Note:**

The following built-in roles grant this privilege:

- The `userAdmin` role provides this privilege
  on the database that the role is assigned.

- The  `userAdminAnyDatabase` role provides this
  privilege on all databases.

Transitively, the `restore` and `root` roles
also provide this privilege.

Apply this action to database resources.

**`setFeatureCompatibilityVersion`**

User can run the `setFeatureCompatibilityVersion` command. 
Apply this action to the `cluster` resource.

**`unlock`**

User can perform the `db.fsyncUnlock()` method. Apply this
action to the `cluster` resource.

**`viewRole`**

User can view information about any role in the given database. Apply
this action to database resources.

**`viewUser`**

User can view the information of any user in the given database. Apply
this action to database resources.

## Deployment Management Actions

**`authSchemaUpgrade`**

User can perform the `authSchemaUpgrade` command. Apply this
action to the `cluster` resource.

**`cleanupOrphaned`**

User can perform the `cleanupOrphaned` command. Apply this
action to the `cluster` resource.

**`cpuProfiler`**

User can enable and use the CPU profiler. Apply this action to the
`cluster` resource.

**`inprog`**

User can use the `db.currentOp()` method to return
information on pending and active operations. Apply this action to
the `cluster` resource.

Even without the `inprog` privilege, on `mongod` 
instances, users can view their own operations by running 
`db.currentOp( { "$ownOps": true } )`.

**`invalidateUserCache`**

Provides access to the `invalidateUserCache` command. Apply
this action to the `cluster` resource.

**`killop`**

User can perform the `db.killOp()` method. Apply this action to
the `cluster` resource.

Even without the `killop` privilege, on `mongod` 
instances, users can kill their own operations.

**`planCacheRead`**

User can run the following operations:

- `$planCacheStats` aggregation stage.

Apply this action to database or collection resources.

**`planCacheWrite`**

User can perform the `planCacheClear` command and the
`PlanCache.clear()` and `PlanCache.clearPlansByQuery()`
methods. Apply this action to database or collection resources.

**`storageDetails`**

User can perform the deprecated `storageDetails` command. Apply this
action to database or collection resources.

## Change Stream Actions

**`changeStream`**

User with `changeStream` and `find` on the
specific collection, all non-`system` collections in a
specific database, or all non-`system` collections across all databases can
open change stream cursor for that resource.

## Replication Actions

**`appendOplogNote`**

User can append notes to the oplog. Apply this action to the
`cluster` resource.

**`replSetConfigure`**

User can configure a replica set. Apply this action to the `cluster`
resource.

**`replSetGetConfig`**

User can view a replica set's configuration. Provides access to the
`replSetGetConfig` command and `rs.conf()` helper
method.

Apply this action to the `cluster` resource.

**`replSetGetStatus`**

User can perform the `replSetGetStatus` command. Apply this
action to the `cluster` resource.

**`replSetHeartbeat`**

User can perform the deprecated `replSetHeartbeat` command. Apply this
action to the `cluster` resource.

**`replSetStateChange`**

User can change the state of a replica set through the
`replSetFreeze`, `replSetMaintenance`,
`replSetStepDown`, and `replSetSyncFrom`
commands. Apply this action to the `cluster` resource.

**`resync`**

User can perform the deprecated `resync` command. Apply this action to
the `cluster` resource.

## Sharding Actions

**`addShard`**

User can perform the `addShard` command. Apply this action
to the `cluster` resource.

**`clearJumboFlag`**

Required to clear a chunk's jumbo flag using the
`clearJumboFlag` command. Apply this action to database
or collection resources.

Included in the `clusterManager` built-in role.

**`enableSharding`**

**Note:** Applicable Resources

The action can apply to either:

- Database or collection resource to enable sharding
  for a database or shard a collection.

- Cluster resource to
  perform various shard zone operations (Starting in version
  4.2.2, 4.0.14, 3.6.16).

* - Resources
  - Description

* - | Database or
    | Collection

  - Grants users privileges to perform the following operations:

    - Enable sharding on a database using the
      `enableSharding` command, and

    - Shard a collection using the `shardCollection`
      command.

* - | Cluster

  - Grants users privileges to perform the following shard zone
    operations:

    - `addShardToZone`

    - `updateZoneKeyRange`

    - `removeShardFromZone`

    You can also perform these shard zone operations if you have
    `find`/`update` actions on the
    appropriate collections in the `config` database. Refer to
    the specific operations for details.

**`refineCollectionShardKey`**

Provides privileges to refine the shard key for a sharded
collection; i.e. run the `refineCollectionShardKey`
command. Apply this action to database
or collection resource.

Included in the `clusterManager` built-in role.

**`reshardCollection`**

User can perform the `reshardCollection` command. Apply 
this action to database or 
collection resources.

**New in version:** 5.0

**`flushRouterConfig`**

User can perform the `flushRouterConfig` command. Apply this
action to the `cluster` resource.

**`getShardMap`**

User can perform the `getShardMap` command. Apply this action
to the `cluster` resource.

**`listShards`**

User can perform the `listShards` command. Apply this action
to the `cluster` resource.

**`moveChunk`**

User can perform the `moveChunk` and 
`moveRange` commands. In addition, user can perform the 
`movePrimary` command provided that the privilege is 
applied to an appropriate database resource. Apply this action to 
database or collection resources.

**`removeShard`**

User can perform the `removeShard` command. Apply this
action to the `cluster` resource.

**`shardedDataDistribution`**

User can perform the `$shardedDataDistribution` aggregation 
pipeline stage.

**New in version:** 6.0.3

**`shardingState`**

User can perform the `shardingState` command. Apply this
action to the `cluster` resource.

## Server Administration Actions

**`applicationMessage`**

User can perform the `logApplicationMessage` command. Apply
this action to the `cluster` resource.

**`bypassWriteBlockingMode`**

User can perform writes even when writes are blocked by the
`setUserWriteBlockMode` command.
Apply this action to the `cluster` resource.

**`closeAllDatabases`**

User can perform the deprecated `closeAllDatabases` command. Apply this
action to the `cluster` resource.

**`collMod`**

User can perform the `collMod` command. Apply this action to
database or collection resources.

**`compact`**

User can perform the `compact` command. Apply this action to
database or collection resources.

**`compactStructuredEncryptionData`**

User can perform the `compactStructuredEncryptionData`
command. Apply this action to database or collection resources.

**`connPoolSync`**

User can perform the internal `connPoolSync` command. Apply this
action to the `cluster` resource.

**`convertToCapped`**

User can perform the `convertToCapped` command. Apply this
action to database or collection resources.

**`dropConnections`**

User can perform the `dropConnections` command. Apply this
action to the `cluster` resource.

**`dropDatabase`**

User can perform the `dropDatabase` command. Apply this action
to database resources.

**`dropIndex`**

User can perform the `dropIndexes` command. Apply this action
to database or collection resources.

**`forceUUID`**

User can create a collection with a user-defined
collection UUID using the
`applyOps` command.

Apply this action to the `cluster` resource.

**`fsync`**

User can perform the `fsync` command. Apply this action to
the `cluster` resource.

**`getDefaultRWConcern`**

User can issue the administrative `getDefaultRWConcern`
command. Apply this action to the `cluster` resource.

**`getParameter`**

User can perform the `getParameter` command. Apply this
action to the `cluster` resource.

**`hostInfo`**

Provides information about the server the MongoDB instance runs on. Apply
this action to the `cluster` resource.

**`oidReset`**

Required to reset the 5 byte random string that is used in the
ObjectID.

**`logRotate`**

User can perform the `logRotate` command. Apply this action
to the `cluster` resource.

**`reIndex`**

User can perform the `reIndex` command. Apply this action to
database or collection resources.

**`renameCollectionSameDB`**

Allows the user to rename collections on the current database using the
`renameCollection` command. Apply this action to database
resources.

Additionally, the user must either *have* `find` on the
source collection or *not have* `find` on the destination
collection.

If a collection with the new name already exists, the user must also
have the `dropCollection` action on the destination
collection.

**`rotateCertificates`**

User can perform the `rotateCertificates` command
command. Apply this action to the `cluster` resource.

**`setDefaultRWConcern`**

User can issue the administrative `setDefaultRWConcern`
command. Apply this action to the `cluster` resource.

**`setParameter`**

User can perform the `setParameter` command. Apply this
action to the `cluster` resource.

**`setUserWriteBlockMode`**

User can perform the `setUserWriteBlockMode` command.
Apply this action to the `cluster` resource.

**`shutdown`**

User can perform the `shutdown` command. Apply this action
to the `cluster` resource.

**`touch`**

User can perform the deprecated `touch` command. Apply this action to
the `cluster` resource.

## Session Actions

**`impersonate`**

User can perform the `killAllSessionsByPattern` command
with `users` and `roles` pattern. Apply this action to the
`cluster` resource.

To run `killAllSessionsByPattern` command, users must
also have `killAnySession` privileges on the cluster
resource.

**`listSessions`**

User can perform the `$listSessions` operation or
`$listLocalSessions` operation for all users or specified
user(s). Apply this action to the `cluster` resource.

**`killAnySession`**

User can perform the `killAllSessions` and the
`killAllSessionsByPattern` command. Apply this action to
the `cluster` resource.

**See also:**

`impersonate`

## Atlas Search Index Actions

The following actions enable users to run Atlas Search Database
Commands. These actions are only relevant
for deployments hosted on MongoDB Atlas.

**`createSearchIndexes`**

User can run the `createSearchIndexes` database command.
Apply this action to the database or collection resource.

**`dropSearchIndex`**

User can run the `dropSearchIndex` database command.
Apply this action to the database or collection resource.

**`listSearchIndexes`**

User can run the `$listSearchIndexes` aggregation stage.
Apply this action to the database or collection resource.

**`updateSearchIndex`**

User can run the `updateSearchIndex` database command.
Apply this action to the database or collection resource.

## Free Monitoring Actions

**`checkFreeMonitoringStatus`**

User with this action on the `cluster` resource can check the
status of free-monitoring-mongodb.

**New in version:** 4.0

**`setFreeMonitoring`**

User with this action on the `cluster` resource can enable or
disable free-monitoring-mongodb.

**New in version:** 4.0

## Diagnostic Actions

**`collStats`**

User can perform the `collStats` command. Apply this action
to database or collection resources.

**`connPoolStats`**

User can perform the `connPoolStats` command. Apply this
action to the `cluster` resource.

**`dbHash`**

User can perform the `dbHash` command. Apply this action to
database or collection resources.

**`dbStats`**

User can perform the `dbStats` command. Apply this action to
database resources.

**`getCmdLineOpts`**

User can perform the `getCmdLineOpts` command. Apply this
action to the `cluster` resource.

**`getLog`**

User can perform the `getLog` command. Apply this action to
the `cluster` resource.

**`indexStats`**

User can run the `$indexStats` aggregation pipeline stage. Apply 
this action to database or collection resources.

To use the `$indexStats` stage, users must authenticate with at least the 
`clusterMonitor` role.
   

**`listDatabases`**

User can perform the `listDatabases` command. Apply this
action to the `cluster` resource.

If the user does not have the `listDatabases`
privilege action, users can run the `listDatabases`
command to return a list of databases for which the user has
privileges (including databases for which the user has privileges
on specific collections) if the command is run with
`authorizedDatabases` option unspecified or set to `true`.

**`listCollections`**

User can perform the `listCollections` command. Apply this
action to database resources.

**Note:**

Users without the required privilege can run the 
`listCollections` command with **both**
`authorizedCollections` and `nameOnly` options set to
`true`. In this case, the command returns just the name and
type of the collection(s) to which the user has privileges.

**`listIndexes`**

User can perform the `listIndexes` command. Apply this
action to database or collection resources.

**`queryStatsRead`**

User can run the `$queryStats` aggregation stage without
the `transformIdentifiers` option.

**`queryStatsReadTransformed`**

User can run the `$queryStats` aggregation stage with or without
the `transformIdentifiers` option.

**`serverStatus`**

User can perform the `serverStatus` command. Apply this action
to the `cluster` resource.

**`validate`**

User can perform the `validate` and 
`validateDBMetadata` commands. Apply this action to 
database or collection resources.

**`top`**

User can perform the `top` command. Apply this action to the
`cluster` resource.

## Internal Actions

**`anyAction`**

Allows any action on a resource. **Do not** assign this action unless
it is absolutely necessary.

**`internal`**

Allows internal actions. **Do not** assign this action unless
it is absolutely necessary.

**`applyOps`**

User can perform the `applyOps` command. Apply this action
to a `cluster` resource.
