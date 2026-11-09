<!-- Converted from reference/command.txt (reStructuredText). Includes are inlined. -->

# Database Commands

All command documentation outlined below describes a command and
its available parameters and provides a document template or prototype
for each command. Some command documentation also includes the relevant
`mongosh` helpers.

To run a command against the current database, use `db.runCommand()`:

```javascript
db.runCommand( { <command> } )
```

To run an administrative command against the `admin` database, use `db.adminCommand()`:

```javascript
db.adminCommand( { <command> } )
```

**Note:**

For details on specific commands, including syntax and examples, 
click on the specific command to go to its reference page.

## Command Syntax

When you run a database command, you specify the command as a document 
to `db.runCommand()`. The document's key is the command to run,
and the value is typically supplied as `1`. The value does not affect
the output of the command for example:

```javascript
db.runCommand( { hello: 1 } )
```

## User Commands

### Aggregation Commands

| Name | Description | MongoDB Atlas Support |
|---|---|---|
| `aggregate` | Performs aggregation tasks such as `$group` using an aggregation pipeline. | .. include:: /includes/fact-limited-support-free-or-flex.rst |
| `count` | Counts the number of documents in a collection or a view. | .. include:: /includes/fact-limited-support-free-or-flex.rst |
| `distinct` | Displays the distinct values found for a specified key in a collection or a view. | .. include:: /includes/fact-limited-support-free-or-flex.rst |
| `mapReduce` | Performs map-reduce aggregation for large data sets. | .. include:: /includes/fact-no-support-free-or-flex.rst |

### Query and Write Operation Commands

| Name | Description | MongoDB Atlas Support |
|---|---|---|
| `delete` | Deletes one or more documents. | Yes |
| `find` | Selects documents in a collection or a view. | .. include:: /includes/fact-limited-support-free-or-flex.rst |
| `findAndModify` | Returns and modifies a single document. | Yes |
| `insert` | Inserts one or more documents. | Yes |
| `update` | Updates one or more documents. | Yes |

### Query Plan Cache Commands

| Name | Description | MongoDB Atlas Support |
|---|---|---|
| `planCacheClear` | Removes cached query plan(s) for a collection. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `planCacheClearFilters` | Clears index filter(s) for a collection. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `planCacheListFilters` | Lists the index filters for a collection. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `planCacheSetFilter` | Sets an index filter for a collection. | .. include:: /includes/fact-no-support-free-or-flex.rst |

## Database Operations

### Authentication Commands

| Name | Description | MongoDB Atlas Support |
|---|---|---|
| `authenticate` | Starts an authenticated session using a username and password. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `logout` | Terminates the current authenticated session. | Yes |

### User Management Commands

| Name | Description | MongoDB Atlas Support |
|---|---|---|
| `createUser` | Creates a new user. | .. include:: /includes/fact-no-support-free-flex-or-m10.rst |
| `dropAllUsersFromDatabase` | Deletes all users associated with a database. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `dropUser` | Removes a single user. | No support for M10 clusters. |
| `grantRolesToUser` | Grants a role and its privileges to a user. | .. include:: /includes/fact-no-support-free-flex-or-m10.rst |
| `revokeRolesFromUser` | Removes a role from a user. | .. include:: /includes/fact-no-support-free-flex-or-m10.rst |
| `updateUser` | Updates a user's data. | .. include:: /includes/fact-no-support-free-flex-or-m10.rst |
| `usersInfo` | Returns information about the specified users. | .. include:: /includes/fact-limited-support-free-or-flex.rst |

### Role Management Commands

| Name | Description | MongoDB Atlas Support |
|---|---|---|
| `createRole` | Creates a role and specifies its privileges. | .. include:: /includes/fact-no-support-free-flex-or-m10.rst |
| `dropRole` | Deletes the user-defined role. | .. include:: /includes/fact-no-support-free-flex-or-m10.rst |
| `dropAllRolesFromDatabase` | Deletes all user-defined roles from a database. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `grantPrivilegesToRole` | Assigns privileges to a user-defined role. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `grantRolesToRole` | Specifies roles from which a user-defined role inherits privileges. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `invalidateUserCache` | Flushes the in-memory cache of user information, including credentials and roles. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `revokePrivilegesFromRole` | Removes the specified privileges from a user-defined role. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `revokeRolesFromRole` | Removes specified inherited roles from a user-defined role. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `rolesInfo` | Returns information for the specified role or roles. | Yes |
| `updateRole` | Updates a user-defined role. | .. include:: /includes/fact-no-support-free-flex-or-m10.rst |

### Replication Commands

| Name | Description | MongoDB Atlas Support |
|---|---|---|
| `appendOplogNote` | Writes a non-operational entry to the oplog. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `applyOps` | Internal command that applies oplog entries to the current data set. | Yes |
| `hello` | Displays information about this member's role in the replica set, including whether it is the primary. | Yes |
| `replSetAbortPrimaryCatchUp` | Forces the elected primary to abort sync (catch up) then complete the transition to primary. | Yes |
| `replSetFreeze` | Prevents the current member from seeking election as primary for a period of time. | .. include:: /includes/fact-no-support-free-flex-or-m10.rst |
| `replSetGetConfig` | Returns the replica set's configuration object. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `replSetGetStatus` | Returns a document that reports on the status of the replica set. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `replSetInitiate` | Initializes a new replica set. | .. include:: /includes/fact-no-support-free-flex-or-m10.rst |
| `replSetMaintenance` | Enables or disables a maintenance mode, which puts a secondary node in a `RECOVERING` state. | .. include:: /includes/fact-no-support-free-flex-or-m10.rst |
| `replSetReconfig` | Applies a new configuration to an existing replica set. | .. include:: /includes/fact-no-support-free-flex-or-m10.rst |
| `replSetResizeOplog` | Dynamically resizes the oplog for a replica set member.  Available for WiredTiger storage engine only. | No support for M10 clusters. |
| `replSetStepDown` | Forces the current primary to *step down* and become a secondary, forcing an election. | .. include:: /includes/fact-no-support-free-flex-or-m10.rst |
| `replSetSyncFrom` | Explicitly override the default logic for selecting a member to replicate from. | .. include:: /includes/fact-no-support-free-flex-or-m10.rst |

**See also:**

/replication for more information regarding
replication.

### Sharding Commands

* - Name

  - Description

  - MongoDB Atlas Support

* - `addShard`

  - Adds a shard to a sharded cluster.

  - Yes

* - `addShardToZone`

  - Associates a shard with a zone. Supports configuring zones in sharded clusters.

  - Yes

* - `analyzeShardKey`

  - Calculates metrics for evaluating a shard key.

    **New in version:** 7.0

  - Yes

* - `balancerCollectionStatus`

  - Returns information on whether the chunks of a sharded
    collection are balanced.

  - Yes

* - `balancerStart`

  - Starts a balancer thread.

  - Yes

* - `balancerStatus`

  - Returns information on the balancer status.

  - Yes

* - `balancerStop`

  - Stops the balancer thread.

  - Yes

* - `checkMetadataConsistency`

  - Performs a series of consistency checks on sharding metadata.

    **New in version:** 7.0

  - Yes

* - `clearJumboFlag`

  - Clears the `jumbo` flag for a chunk.

  - Yes

* - `cleanupOrphaned`

  - Removes orphaned data with shard key values outside of the ranges of the chunks owned by a shard.

  - No support for M0, M2, and M5 clusters.

* - `cleanupReshardCollection`

  - Cleans up a failed resharding operation.

  - Yes

* - `commitReshardCollection`

  - Forces a resharding operation to
    block writes and complete.

  - Yes

* - `configureCollectionBalancing`

  - Configures balancer settings on a sharded collection.

  - Yes

* - `configureQueryAnalyzer`

  - Configures query sampling for a collection.

    **New in version:** 7.0

  - Yes

* - `enableSharding`

  - Creates a database.

  - Yes

* - `flushRouterConfig`

  - Forces a `mongod` / `mongos` instance to update its cached routing metadata.

  - Yes

* - `getShardMap`

  - Internal command that reports on the state of a sharded cluster.

  - .. include:: /includes/fact-no-support-free-or-flex.rst

* - `isdbgrid`

  - Verifies that a process is a `mongos`.

  - Yes

* - `listShards`

  - Returns a list of configured shards.

  - Yes

* - `moveChunk`

  - Internal command that migrates chunks between shards.

  - Yes

* - `movePrimary`

  - Reassigns the primary shard when removing a shard from a sharded cluster.

  - Yes

* - `moveRange`

  - Moves ranges between shards.

  - Yes

* - `mergeAllChunksOnShard`

  - Merges all mergeable chunks that a shard
    owns for a given collection.

  - Yes

* - `mergeChunks`

  - Provides the ability to combine chunks on a single shard.

  - Yes

* - `refineCollectionShardKey`

  - Refines a collection's shard key by adding a suffix to the
    existing key.

  - No support for M10 clusters.

* - `removeShard`

  - Starts the process of removing a shard from a sharded cluster.

  - No support for M10 clusters.

* - `removeShardFromZone`

  - Removes the association between a shard and a zone. Supports configuring zones in sharded clusters.

  - Yes

* - `reshardCollection`

  - Initiates a resharding operation to change the
    shard key for a collection, changing the distribution of your data.

  - Yes

* - `setAllowMigrations`

  - Prevents new automatic migrations on a collection.

  - Yes

* - `shardCollection`

  - Enables the sharding functionality for a collection, allowing the collection to be sharded.

  - Yes

* - `shardingState`

  - Reports whether the `mongod` is a member of a sharded cluster.

  - Yes

* - `split`

  - Creates a new chunk.

  - Yes

* - `unsetSharding`

  - *Removed in MongoDB 5.0.* Internal command that affects
    connections between instances in a MongoDB deployment.

  - Yes

* - `updateZoneKeyRange`

  - Adds or removes the association between a range of sharded data and a zone. Supports configuring zones in sharded clusters.

  - Yes

**See also:**

/sharding for more information about MongoDB's
sharding functionality.

### Session Commands

| Command | Description | Atlas Support |
|---|---|---|
| `abortTransaction` | Abort transaction. | Yes |
| `commitTransaction` | Commit transaction. | Yes |
| `endSessions` | Expire sessions before the sessions' timeout period. | Yes |
| `killAllSessions` | Kill all sessions. | .. include:: /includes/fact-no-support-free-flex-or-m10.rst |
| `killAllSessionsByPattern` | Kill all sessions that match the specified pattern | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `killSessions` | Kill specified sessions. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `refreshSessions` | Refresh idle sessions. | Yes |
| `startSession` | Starts a new session. | Yes |

### Administration Commands

* - Name

  - Description

  - MongoDB Atlas Support

* - `cloneCollectionAsCapped`

  - Copies a non-capped collection as a new capped collection.

  - .. include:: /includes/fact-no-support-free-or-flex.rst

* - `collMod`

  - Add options to a collection or modify a view definition.

  - Yes

* - `compact`

  - Defragments a collection and rebuilds the indexes.

  - .. include:: /includes/fact-no-support-free-or-flex.rst

* - `compactStructuredEncryptionData`

  -  Compacts documents specified in the state collections and 
     deletes redundant documents.

  - Yes

* - `convertToCapped`

  - Converts a non-capped collection to a capped collection.

  - Yes

* - `create`

  - Creates a collection or a view.

  - Yes

* - `createIndexes`

  - Builds one or more indexes for a collection.

  - Yes

* - `currentOp`

  - Returns a document that contains information on in-progress operations for the database instance.

  - Yes

* - `drop`

  - Removes the specified collection from the database.

  - Yes

* - `dropDatabase`

  - Removes the current database.

  - Yes

* - `dropConnections`

  - Drops outgoing connections to the specified list of hosts.

  - Yes

* - `dropIndexes`

  - Removes indexes from a collection.

  - Yes

* - `filemd5`

  - *Deprecated.* Returns the md5 hash for files stored using GridFS.

  - Yes

* - `fsync`

  - Flushes pending writes to the storage layer and locks the database to allow backups.

  - .. include:: /includes/fact-no-support-free-flex-or-m10.rst

* - `fsyncUnlock`

  - Unlocks one fsync lock.

  - .. include:: /includes/fact-no-support-free-or-flex.rst

* - `getAuditConfig`

  - Retrieves audit configurations from `mongod` and
    `mongos` instances.

  - No

* - `getDefaultRWConcern`

  - Retrieves the global default read and write concern options 
    for the deployment.

  - Yes

* - `getClusterParameter`

  - Retrieves cluster parameter values from all nodes in a cluster.

    **New in version:** 6.0

  - Yes

* - `getParameter`

  - Retrieves configuration options.

  - .. include:: /includes/fact-limited-support-free-or-flex.rst

* - `killCursors`

  - Kills the specified cursors for a collection.

  - Yes

* - `killOp`

  - Terminates an operation as specified by the operation ID.

  - Limited support for Free, 
    M10, and 
    Flex clusters.

* - `listCollections`

  - Returns a list of collections in the current database.

  - Yes

* - `listDatabases`

  - Returns a document that lists all databases and returns basic database statistics.

  - Yes

* - `listIndexes`

  - Lists all indexes for a collection.

  - Yes

* - `logRotate`

  - Rotates the MongoDB logs to prevent a single file from taking too much space.

  - .. include:: /includes/fact-no-support-free-flex-or-m10.rst

* - `reIndex`

  - Rebuilds all indexes on a collection.

  - .. include:: /includes/fact-no-support-free-or-flex.rst

* - `renameCollection`

  - Changes the name of an existing collection.

  - Yes

* - `rotateCertificates`

  - Performs online TLS certificate rotation.

  - Yes

* - `setFeatureCompatibilityVersion`

  - Enables or disables features that persist data that are backwards-incompatible.

  - .. include:: /includes/fact-no-support-free-flex-or-m10.rst

* - `setIndexCommitQuorum`

  - Changes the minimum number of data-bearing members (i.e commit
    quorum), including the primary, that must vote to commit an
    in-progress index build before the primary marks
    those indexes as ready.

  - Yes  

* - `setAuditConfig`

  - Sets audit configurations for `mongod` and
    `mongos` instances at runtime.

  - No

* - `setClusterParameter`

  - Modifies configuration options for all nodes in a replica set or
    sharded cluster.

    **New in version:** 6.0

  - Yes

* - `setParameter`

  - Modifies configuration options.

  - .. include:: /includes/fact-no-support-free-flex-or-m10.rst

* - `setUserWriteBlockMode`

  - Blocks and unblocks writes to the entire cluster.

  - No

* - `setDefaultRWConcern`

  - Sets the global default read and write concern options for the 
    deployment. 

  - Yes

* - `shutdown`

  - Shuts down the `mongod` or `mongos` process.

  - .. include:: /includes/fact-no-support-free-flex-or-m10.rst

### Diagnostic Commands

| Name | Description | MongoDB Atlas Support |
|---|---|---|
| `buildInfo` | Displays statistics about the MongoDB build. | Yes |
| `collStats` | Reports storage utilization statics for a specified collection. | Yes |
| `connPoolStats` | Reports statistics on the outgoing connections from this MongoDB instance to other MongoDB instances in the deployment. | Yes |
| `connectionStatus` | Reports the authentication state for the current connection. | Yes |
| `dataSize` | Returns the data size for a range of data. For internal use. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `dbHash` | Returns hash value a database and its collections. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `dbStats` | Reports storage utilization statistics for the specified database. | .. include:: /includes/fact-limited-support-free-or-flex.rst |
| `explain` | Returns information on the execution of various operations. | Yes |
| `getCmdLineOpts` | Returns a document with the run-time arguments to the MongoDB instance and their parsed options. | Yes |
| `getLog` | Returns recent log messages. | Yes |
| `hostInfo` | Returns data that reflects the underlying host system. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `listCommands` | Lists all database commands provided by the current `mongod` instance. | Yes |
| `lockInfo` | Internal command that returns information on locks that are currently being held or pending. Only available for `mongod` instances. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `ping` | Internal command that tests intra-deployment connectivity. | Yes |
| `profile` | Interface for the database profiler. | Yes |
| `serverStatus` | Returns a collection metrics on instance-wide resource utilization and status. | Yes |
| `shardConnPoolStats` | *Removed in MongoDB 5.0.* Use `connPoolStats` instead. | Yes |
| `top` | Returns raw usage statistics for each database in the `mongod` instance. | Yes |
| `validate` | Internal command that scans for a collection's data and indexes for correctness. | .. include:: /includes/fact-no-support-free-or-flex.rst |
| `validateDBMetadata` | Checks that the stored metadata of a database or a collection is valid within a particular API version. | Yes |
| `whatsmyuri` | Internal command that returns information on the current client. | Yes |

### Auditing Commands

| Name | Description | MongoDB Atlas Support |
|---|---|---|
| `logApplicationMessage` | Posts a custom message to the audit log. | Yes |

## Atlas Search

**New in version:** 7.0 (*Also available starting in 6.0.7*)

| Name | Description |
|---|---|
| `createSearchIndexes` | .. include:: /includes/atlas-search-commands/command-descriptions/createSearchIndexes-description.rst |
| `dropSearchIndex` | .. include:: /includes/atlas-search-commands/command-descriptions/dropSearchIndex-description.rst |
| `updateSearchIndex` | .. include:: /includes/atlas-search-commands/command-descriptions/updateSearchIndex-description.rst |
