<!-- Converted from reference/method.txt (reStructuredText). Includes are inlined. -->

# `mongosh` Methods

## Introduction

This page contains `mongosh` methods.

**Note:** JavaScript in MongoDB

Although these methods use JavaScript, most
interactions with MongoDB do not use JavaScript but use an
`idiomatic driver` in the language
of the interacting application.

## Native Methods

The methods listed in this section are `mongosh` functional
replacements for the native methods that were available in the legacy 
`mongo` shell. These methods are not exact replacements: output 
formats and some functionality may differ from the corresponding 
legacy methods.

In addition to these methods, the [mongocompat snippet](https://github.com/mongodb-labs/mongosh-snippets/blob/main/snippets/mongocompat/index.js)
provides access to legacy `mongo` shell APIs.

**Note:**

In the following table `<path>` and `<filename>` are strings and
should be in quotes.

```javascript
// process.chdir( <path> )

process.chdir( "./data/incoming" )
```

* - Legacy Method Name
  - Replacement

* - `cat()`
  - Returns the contents of the specified file

    ```javascript
    fs.readFileSync( <filename>, 'utf8' )
    ```

    The legacy `useBinaryMode` option is not supported. Emulate 
    the `useBinaryMode = false` option with:

    ```javascript
    fs.readFileSync( <filename>, 'utf8' ).replace( /\r\n/g, '\n' )
    ```

* - `getHostName()`
  - Returns the hostname of the system running `mongosh`.

    ```javascript
    os.hostname()
    ```

* - `getMemInfo()`
  - Returns a document that reports memory used by the shell.

    ```javascript
    process.memoryUsage()
    ```

* - `hostname()`
  - Returns the hostname of the computer running the shell.

    ```javascript
    os.hostname()
    ```

* - `isInteractive()`
  - Returns a boolean indicating whether `mongosh` is
    running in interactive or script mode.

    ```
    isInteractive()
    ```

* - `listFiles()`
  - Returns an array of documents that give the name and type of
    each object in the directory.

    ```javascript
    fs.readdirSync( <path>, { withFileTypes: true } )
    ```

* - `load()`
  - Loads and runs a JavaScript file in the shell.

    `load()` is available in `mongosh`. See also
    load-and-require.

* - `ls()`
  - Returns a list of the files in the current directory.

    ```javascript
    fs.readdirSync( <path> )
    ```

* - `md5sumFile()`
  - Returns the md5 hash of the specified file.

    ```javascript
    crypto.createHash( 'md5' ).update( fs.readFileSync( <filename> ) ).digest( 'hex' )
    ```

* - `mkdir()`
  - Creates a directory at the specified path.

    ```javascript
    fs.mkdirSync( <path>, { recursive: true } )
    ```

* - `quit()`
  - Exits the current shell session.

    ```javascript
    quit()
    ```

* - `removeFile()`
  - Removes the specified file from the local file system.

    ```javascript
    fs.unlinkSync( <filename> )
    ```

* - `sleep()`
  - Sleep for the specified number of milliseconds.

    ```javascript
    sleep( <number> )
    ```

* - `version()`
  - Returns the current version of `mongosh` instance.

    ```javascript
    version()
    ```

* - `_isWindows()`
  - Returns `true` if the shell in running on Windows.

    ```javascript
    process.platform === 'win32'
    ```

* - `_rand()`
  - Returns a random number between `0` and `1`.                    

    ```javascript
    Math.random() 
    ```

## Atlas Search Index

**New in version:** 7.0 (*Also available starting in 6.0.7*)

Atlas Search indexes let you query data
in Atlas Search, while Atlas Vector Search indexes 
let you query data in Atlas Vector Search. Atlas Search and
Atlas Vector Search indexes enable performant
text search queries by mapping search terms to the documents that
contain those terms.

Use the following methods to manage Atlas Search and Atlas Vector Search indexes.

**Important:**

The following methods can only be run on deployments hosted on
MongoDB Atlas, and require an Atlas cluster tier of at
least M10.

| Name | Description |
|---|---|
| `db.collection.createSearchIndex()` | .. include:: /includes/atlas-search-commands/command-descriptions/createSearchIndex-method.rst |
| `db.collection.dropSearchIndex()` | .. include:: /includes/atlas-search-commands/command-descriptions/dropSearchIndex-description.rst |
| `db.collection.getSearchIndexes()` | .. include:: /includes/atlas-search-commands/command-descriptions/getSearchIndexes-description.rst |
| `db.collection.updateSearchIndex()` | .. include:: /includes/atlas-search-commands/command-descriptions/updateSearchIndex-description.rst |

## Atlas Stream Processing

Atlas Stream Processors
let you perform aggregation operations against streams of
continuous data using the same data model and query API that
you use with at-rest data.

Use the following methods to manage Stream Processors:

**Important:**

The following methods can only be run on deployments hosted on
MongoDB Atlas.

| Name | Description |
|---|---|
| `sp.createStreamProcessor()` | Creates a stream processor. |
| `sp.listConnections()` | Lists all existing connections in the connection registry of the current stream processing workspace. |
| `sp.listStreamProcessors()` | Lists all existing stream processors on the current stream processing workspace. |
| `sp.process()` | Creates an ephemeral stream processor. |
| `sp.processor.drop()` | Deletes an existing stream processor. |
| `sp.processor.modify()` | Modifies an existing stream processor. |
| `sp.processor.sample()` | Returns an array of sampled results from a currently running stream processor. |
| `sp.processor.start()` | Starts an existing stream processor. |
| `sp.processor.stats()` | Returns statistics summarizing an existing stream processor. |
| `sp.processor.stop()` | Stops a currently running stream processor. |

## Collections

| Name | Description |
|---|---|
| `db.collection.analyzeShardKey()` | Calculates metrics for evaluating a shard key. |
| `db.collection.aggregate()` | Provides access to the aggregation pipeline. |
| `db.collection.bulkWrite()` | Provides bulk write operation functionality. |
| `db.collection.compactStructuredEncryptionData()` | Wraps `compactStructuredEncryptionData` to return a success or failure object. |
| `db.collection.configureQueryAnalyzer()` | Configures query sampling for a collection. |
| `db.collection.count()` | Wraps `count` to return a count of the number of documents in a collection or a view. |
| `db.collection.countDocuments()` | Wraps the `$group` aggregation stage with a `$sum` expression to return a count of the number of documents in a collection or a view. |
| `db.collection.createIndex()` | Builds an index on a collection. |
| `db.collection.createIndexes()` | Builds one or more indexes on a collection. |
| `db.collection.dataSize()` | Returns the size of the collection. Wraps the `size` field in the output of the `collStats`. |
| `db.collection.deleteOne()` | Deletes a single document in a collection. |
| `db.collection.deleteMany()` | Deletes multiple documents in a collection. |
| `db.collection.distinct()` | Returns an array of documents that have distinct values for the specified field. |
| `db.collection.drop()` | Removes the specified collection from the database. |
| `db.collection.dropIndex()` | Removes a specified index on a collection. |
| `db.collection.dropIndexes()` | Removes all indexes on a collection. |
| `db.collection.estimatedDocumentCount()` | Wraps `count` to return an approximate count of the documents in a collection or a view. |
| `db.collection.explain()` | Returns information on the query execution of various methods. |
| `db.collection.find()` | Performs a query on a collection or a view and returns a cursor object. |
| `db.collection.findAndModify()` | Atomically modifies and returns a single document. |
| `db.collection.findOne()` | Performs a query and returns a single document. |
| `db.collection.findOneAndDelete()` | Finds a single document and deletes it. |
| `db.collection.findOneAndReplace()` | Finds a single document and replaces it. |
| `db.collection.findOneAndUpdate()` | Finds a single document and updates it. |
| `db.collection.getIndexes()` | Returns an array of documents that describe the existing indexes on a collection. |
| `db.collection.getShardDistribution()` | For collections in sharded clusters, `db.collection.getShardDistribution()` reports data of chunk distribution. |
| `db.collection.getShardVersion()` | Internal diagnostic method for sharded cluster. |
| `db.collection.hideIndex()` | Hides an index from the query planner. |
| `db.collection.insert()` | **Deprecated**. For alternative methods, see compatibility. |
| `db.collection.insertOne()` | Inserts a new document into a collection. |
| `db.collection.insertMany()` | Inserts several new documents into a collection. |
| `db.collection.isCapped()` | Reports if a collection is a capped collection. |
| `db.collection.latencyStats()` | Returns latency statistics for a collection. |
| `db.collection.mapReduce()` | Performs map-reduce style data aggregation. |
| `db.collection.reIndex()` | Rebuilds all existing indexes on a collection. |
| `db.collection.remove()` | Deletes documents from a collection. |
| `db.collection.renameCollection()` | Changes the name of a collection. |
| `db.collection.replaceOne()` | Replaces a single document in a collection. |
| `db.collection.stats()` | Reports on the state of a collection. Provides a wrapper around the `collStats`. |
| `db.collection.storageSize()` | Reports the total size used by the collection in bytes. Provides a wrapper around the `storageSize` field of the `collStats` output. |
| `db.collection.totalIndexSize()` | Reports the total size used by the indexes on a collection. Provides a wrapper around the `totalIndexSize` field of the `collStats` output. |
| `db.collection.totalSize()` | Reports the total size of a collection, including the size of all documents and all indexes on a collection. |
| `db.collection.unhideIndex()` | Unhides an index from the query planner. |
| `db.collection.update()` | **Deprecated**. For alternative methods, see compatibility. |
| `db.collection.updateOne()` | Modifies a single document in a collection. |
| `db.collection.updateMany()` | Modifies multiple documents in a collection. |
| `db.collection.watch()` | Establishes a Change Stream on a collection. |
| `db.collection.validate()` | Performs diagnostic operations on a collection. |

## Cursors

These methods modify the way that the underlying query is executed.

| Name | Description |
|---|---|
| `cursor.addOption()` | Adds special wire protocol flags that modify the behavior of the query.' |
| `cursor.allowDiskUse()` | Allows MongoDB to use temporary files on disk to store data exceeding the 100 megabyte system memory limit while processing an in-memory sort operation. |
| `cursor.batchSize()` | Controls the number of documents MongoDB will return to the client in a single network message. |
| `cursor.close()` | Close a cursor and free associated server resources. |
| `cursor.collation()` | Specifies the collation for the cursor returned by the `db.collection.find()`. |
| `cursor.comment()` | Attaches a comment to the query to allow for traceability in the logs and the system.profile collection. |
| `cursor.count()` | Modifies the cursor to return the number of documents in the result set rather than the documents themselves. |
| `cursor.disableBlockWarnings()` | Silence warnings that `mongosh` prints when you run blocking calls on cursors, such as `.next()` or `.hasNext()` on tailable cursors. |
| `cursor.explain()` | Reports on the query execution plan for a cursor. |
| `cursor.forEach()` | Applies a JavaScript function for every document in a cursor. |
| `cursor.hasNext()` | Returns true if the cursor has documents and can be iterated. |
| `cursor.hint()` | Forces MongoDB to use a specific index for a query. |
| `cursor.isClosed()` | Returns `true` if the cursor is closed. |
| `cursor.isExhausted()` | Returns `true` if the cursor is closed *and* there are no objects remaining in the batch. |
| `cursor.itcount()` | Computes the total number of documents in the cursor client-side by fetching and iterating the result set. |
| `cursor.limit()` | Constrains the size of a cursor's result set. |
| `cursor.map()` | Applies a function to each document in a cursor and collects the return values in an array. |
| `cursor.max()` | Specifies an exclusive upper index bound for a cursor. For use with `cursor.hint()` |
| `cursor.maxAwaitTimeMS()` | Specifies a limit in milliseconds to wait for the next query result update. |
| `cursor.maxTimeMS()` | Specifies a cumulative time limit in milliseconds for processing operations on a cursor. |
| `cursor.min()` | Specifies an inclusive lower index bound for a cursor. For use with `cursor.hint()` |
| `cursor.next()` | Returns the next document in a cursor. |
| `cursor.noCursorTimeout()` | Instructs the server to avoid closing a cursor automatically after a period of inactivity. |
| `cursor.objsLeftInBatch()` | Returns the number of documents left in the current cursor batch. |
| `cursor.pretty()` | Configures the cursor to display results in an easy-to-read format. |
| `cursor.readConcern()` | Specifies a read concern for a `find()` operation. |
| `cursor.readPref()` | Specifies a read preference to a cursor to control how the client directs queries to a replica set. |
| `cursor.returnKey()` | Modifies the cursor to return index keys rather than the documents. |
| `cursor.showRecordId()` | Adds an internal storage engine ID field to each document returned by the cursor. |
| `cursor.size()` | Returns a count of the documents in the cursor after applying `skip()` and `limit()` methods. |
| `cursor.skip()` | Returns a cursor that begins returning results only after passing or skipping a number of documents. |
| `cursor.sort()` | Returns results ordered according to a sort specification. |
| `cursor.tailable()` | Marks the cursor as tailable. Only valid for cursors over capped collections. |
| `cursor.toArray()` | Returns an array that contains all documents returned by the cursor. |
| `cursor.tryNext()` | Returns the next element in the iteration if available or else null. |

## Databases

| Name | Description |
|---|---|
| `db.adminCommand()` | Runs a command against the `admin` database. |
| `db.aggregate()` | Runs admin/diagnostic pipeline which does not require an underlying collection. |
| `db.commandHelp()` | Returns help information for a database command. |
| `db.createCollection()` | Creates a new collection or a view. Commonly used to create a capped collection. |
| `db.createEncryptedCollection()` | Creates an encrypted collection. |
| `db.createView()` | Creates a view. |
| `db.currentOp()` | Reports the current in-progress operations. |
| `db.dropDatabase()` | Removes the current database. |
| `db.fsyncLock()` | Flushes writes to disk and locks the database to prevent write operations and assist backup operations. Wraps `fsync`. |
| `db.fsyncUnlock()` | Allows writes to continue on a database locked with `db.fsyncLock()`. |
| `db.getCollection()` | Returns a collection or view object. Used to access collections with names that are not valid in `mongosh`. |
| `db.getCollectionInfos()` | Returns collection information for all collections and views in the current database. |
| `db.getCollectionNames()` | Lists all collections and views in the current database. |
| `db.getLogComponents()` | Returns the log message verbosity levels. |
| `db.getMongo()` | Returns the `Mongo()` connection object for the current connection. |
| `db.getName()` | Returns the name of the current database. |
| `db.getProfilingStatus()` | Returns a document that reflects the current profiling level and the profiling threshold. |
| `db.getReplicationInfo()` | Returns a document with replication statistics. |
| `db.getSiblingDB()` | Provides access to the specified database. |
| `db.hello()` | Returns a document that reports the state of the replica set. |
| `db.help()` | Displays descriptions of common `db` object methods. |
| `db.hostInfo()` | Returns a document with information about the system MongoDB runs on. Wraps `hostInfo` |
| `db.killOp()` | Terminates a specified operation. |
| `db.listCommands()` | Displays a list of common database commands. |
| `db.logout()` | *Deprecated*. Ends an authenticated session. |
| `db.printCollectionStats()` | Prints statistics from every collection. Wraps `db.collection.stats()`. |
| `db.printReplicationInfo()` | Prints a report of the status of the replica set from the perspective of the primary. |
| `db.printSecondaryReplicationInfo()` | Prints the status of the replica set from the perspective of the secondaries. |
| `db.printShardingStatus()` | Prints a report of the sharding configuration and the chunk ranges. |
| `db.rotateCertificates()` | Performs online TLS certificate rotation. Wraps `rotateCertificates`. |
| `db.runCommand()` | Runs a database command. |
| `db.serverBuildInfo()` | Returns a document that displays the compilation parameters for the `mongod` instance. Wraps `buildInfo`. |
| `db.serverCmdLineOpts()` | Returns a document with information about the runtime used to start the MongoDB instance. Wraps `getCmdLineOpts`. |
| `db.serverStatus()` | Returns a document that provides an overview of the state of the database process. |
| `db.setLogLevel()` | Sets a single log message verbosity level. |
| `db.setProfilingLevel()` | Modifies the current level of database profiling. |
| `db.shutdownServer()` | Shuts down the current `mongod` or `mongos` process cleanly and safely. |
| `db.stats()` | Returns a document that reports on the state of the current database. |
| `db.version()` | Returns the version of the `mongod` instance. |
| `db.watch()` | Opens a change stream cursor for a database to report on all its non-`system` collections. Cannot be opened on the `admin`, `local` or `config` databases. |

## Query Plan Caches

The PlanCache methods are only accessible from a collection's plan
cache object. To retrieve the plan cache object, use the
`db.collection.getPlanCache()` method.

| Name | Description |
|---|---|
| `db.collection.getPlanCache()` | Returns an interface to access the query plan cache object and associated PlanCache methods for a collection. |
| `PlanCache.clear()` | Clears all the cached query plans for a collection. Accessible through the plan cache object of a specific collection, i.e. `db.collection.getPlanCache().clear()`. |
| `PlanCache.clearPlansByQuery()` | Clears the cached query plans for the specified query shape. Accessible through the plan cache object of a specific collection, i.e. `db.collection.getPlanCache().clearPlansByQuery()` |
| `PlanCache.help()` | Displays the methods available for a collection's query plan cache. Accessible through the plan cache object of a specific collection, i.e. `db.collection.getPlanCache().help()`. |
| `PlanCache.list()` | Returns the plan cache information for a collection. Accessible through the plan cache object of a specific collection, i.e. `db.collection.getPlanCache().list()`. |

## Bulk Operations

**Tip:**

MongoDB also provides the `db.collection.bulkWrite()` method for 
performing bulk write operations.

| Name | Description |
|---|---|
| `db.collection.initializeOrderedBulkOp()` | Initializes a `Bulk()` operations builder for an ordered list of operations. |
| `db.collection.initializeUnorderedBulkOp()` | Initializes a `Bulk()` operations builder for an unordered list of operations. |
| `Bulk()` | Bulk operations builder. |
| `Bulk.execute()` | Executes a list of operations in bulk. |
| `Bulk.find()` | Specifies the query condition for an update or a remove operation. |
| `Bulk.find.arrayFilters()` | Specifies the filters that determine which elements of an array to update for an `update` or `updateOne` operation. |
| `Bulk.find.collation()` | Specifies the collation for the query condition. |
| `Bulk.find.delete()` | Adds a multiple document delete operation to a list of operations. |
| `Bulk.find.deleteOne()` | Adds a single document delete operation to a list of operations. |
| `Bulk.find.hint()` | Specifies the index to use for the update/replace operation. |
| `Bulk.find.remove()` | An alias for `Bulk.find.delete()`. |
| `Bulk.find.removeOne()` | An alias for `Bulk.find.deleteOne()`. |
| `Bulk.find.replaceOne()` | Adds a single document replacement operation to a list of operations. |
| `Bulk.find.updateOne()` | Adds a single document update operation to a list of operations. |
| `Bulk.find.update()` | Adds a `multi` update operation to a list of operations. |
| `Bulk.find.upsert()` | Specifies `upsert: true` for an update operation. |
| `Bulk.getOperations()` | Returns an array of write operations executed in the `Bulk()` operations object. |
| `Bulk.insert()` | Adds an insert operation to a list of operations. |
| `Bulk.toJSON()` | Returns a JSON document that contains the number of operations and batches in the `Bulk()` operations object. |
| `Bulk.toString()` | Returns the `Bulk.toJSON()` results as a string. |

## User Management

| Name | Description |
|---|---|
| `db.auth()` | Authenticates a user to a database. |
| `db.changeUserPassword()` | Changes an existing user's password. |
| `db.createUser()` | Creates a new user. |
| `db.dropUser()` | Removes a single user. |
| `db.dropAllUsers()` | Deletes all users associated with a database. |
| `db.getUser()` | Returns information about the specified user. |
| `db.getUsers()` | Returns information about all users associated with a database. |
| `db.grantRolesToUser()` | Grants a role and its privileges to a user. |
| `db.removeUser()` | Deprecated. Removes a user from a database. |
| `db.revokeRolesFromUser()` | Removes a role from a user. |
| `db.updateUser()` | Updates user data. |
| `passwordPrompt()` | Prompts for the password as an alternative to specifying passwords directly in various `mongosh` user authentication/management methods. |

## Role Management

| Name | Description |
|---|---|
| `db.createRole()` | Creates a role and specifies its privileges. |
| `db.dropRole()` | Deletes a user-defined role. |
| `db.dropAllRoles()` | Deletes all user-defined roles associated with a database. |
| `db.getRole()` | Returns information for the specified role. |
| `db.getRoles()` | Returns information for all the user-defined roles in a database. |
| `db.grantPrivilegesToRole()` | Assigns privileges to a user-defined role. |
| `db.revokePrivilegesFromRole()` | Removes the specified privileges from a user-defined role. |
| `db.grantRolesToRole()` | Specifies roles from which a user-defined role inherits privileges. |
| `db.revokeRolesFromRole()` | Removes inherited roles from a role. |
| `db.updateRole()` | Updates a user-defined role. |

## Replication

| Name | Description |
|---|---|
| `rs.add()` | Adds a member to a replica set. |
| `rs.addArb()` | Adds an arbiter to a replica set. |
| `rs.conf()` | Returns the replica set configuration document. |
| `rs.freeze()` | Prevents the current member from seeking election as primary for a period of time. |
| `rs.help()` | Returns basic help text for replica set functions. |
| `rs.initiate()` | Initializes a new replica set. |
| `rs.printReplicationInfo()` | Prints a formatted report of the replica set status from the perspective of the primary. |
| `rs.printSecondaryReplicationInfo()` | Prints a formatted report of the replica set status from the perspective of the secondaries. |
| `rs.reconfig()` | Re-configures a replica set by applying a new replica set configuration object. |
| `rs.reconfigForPSASet()` | Safely perform some reconfiguration changes on a primary-secondary-arbiter (PSA) replica set or on a replica set that is changing to a PSA architecture. |
| `rs.remove()` | Remove a member from a replica set. |
| `rs.status()` | Returns a document with information about the state of the replica set. |
| `rs.stepDown()` | Causes the current primary to become a secondary which forces an election. |
| `rs.syncFrom()` | Sets the member that this replica set member will sync from, overriding the default sync target selection logic. |

## Sharding

* - Name

  - Description

* - `sh.abortReshardCollection()`

  - Aborts a resharding operation.

    **New in version:** 5.0

* - `sh.addShard()`

  - Adds a shard to a sharded cluster.

* - `sh.addShardTag()`

  - This method aliases to `sh.addShardToZone()`.

* - `sh.addShardToZone()`

  - Associates a shard to a zone. Supports configuring zones in sharded clusters.

* - `sh.addTagRange()`

  - This method aliases to `sh.updateZoneKeyRange()`.

* - `sh.balancerCollectionStatus()`

  - Returns information on whether the chunks of a sharded
    collection are balanced.

* - `sh.commitReshardCollection()`

  - Forces a resharding operation to
    block writes and complete.

    **New in version:** 5.0

* - `sh.disableBalancing()`

  - Disable balancing on a single collection in a sharded database. Does not affect balancing of other collections in a sharded cluster.

* - `sh.enableBalancing()`

  - Activates the sharded collection balancer process if previously disabled using `sh.disableBalancing()`.

* - `sh.disableAutoMerger()`

  - .. include:: /includes/disableAutoMerger.rst

    **New in version:** 7.0

* - `sh.disableAutoSplit()`

  - Disables auto-splitting for the sharded cluster.

    Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
    This is because of balancing policy improvements. Auto-splitting commands 
    still exist, but do not perform an operation. 

* - `sh.enableAutoMerger()`

  - .. include:: /includes/enableAutoMerger.rst

    **New in version:** 7.0

* - `sh.enableAutoSplit()`

  - Enables auto-splitting for the sharded cluster.

    Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
    This is because of balancing policy improvements. Auto-splitting commands 
    still exist, but do not perform an operation. 

* - `sh.enableSharding()`

  - Creates a database.

* - `sh.getBalancerState()`

  - Returns a boolean to report if the balancer is currently enabled.

* - `sh.getShardedDataDistribution()`

  - .. include:: /includes/sharding/getShardedDataDistribution-shell-helper-method-summary.rst

* - `sh.removeTagRange()`

  - This method aliases to `sh.removeRangeFromZone()`.

* - `sh.removeRangeFromZone()`

  - Removes an association between a range of shard keys and a zone. Supports configuring zones in sharded clusters.

* - `sh.help()`

  - Returns help text for the `sh` methods.

* - `sh.isBalancerRunning()`

  - Returns a document describing the status of the balancer.

* - `sh.moveChunk()`

  - Migrates a chunk in a sharded cluster.

* - `sh.moveRange()`

  - Move ranges between shards.

* - `sh.removeShardTag()`

  - This method is an alias for `sh.removeShardFromZone()`.

* - `sh.removeShardFromZone()`

  - Removes the association between a shard and a zone. Use to manage zone sharding.

* - `sh.reshardCollection()`

  - Initiates a resharding operation to change the
    shard key for a collection, changing the distribution of your data.

    **New in version:** 5.0

* - `sh.setBalancerState()`

  - Enables or disables the balancer which migrates chunks between shards.

* - `sh.shardCollection()`

  - Enables sharding for a collection.

* - `sh.splitAt()`

  - Divides an existing chunk into two chunks using a specific value of the shard key as the dividing point.

* - `sh.splitFind()`

  - Divides an existing chunk that contains a document matching a query into two approximately equal chunks.

* - `sh.startAutoMerger()`

  - .. include:: /includes/startAutoMerger.rst

    **New in version:** 7.0

* - `sh.startBalancer()`

  - Enables the balancer and waits for balancing to start.

* - `sh.status()`

  - Reports on the status of a sharded cluster, as `db.printShardingStatus()`.

* - `sh.stopAutoMerger()`

  - .. include:: /includes/stopAutoMerger.rst

    **New in version:** 7.0

* - `sh.stopBalancer()`

  - Disables the balancer and waits for any in progress balancing rounds to complete.

* - `sh.waitForBalancer()`

  - Internal. Waits for the balancer state to change.

* - `sh.waitForBalancerOff()`

  - Internal. Waits until the balancer stops running.

* - `sh.waitForPingChange()`

  - Internal. Waits for a change in ping state from one of the `mongos` in the sharded cluster.

* - `sh.updateZoneKeyRange()`

  - Associates a range of shard keys to a zone. Supports configuring zones in sharded clusters.

* - `convertShardKeyToHashed()`

  - Returns the hashed value for the input.

## Object Constructors

| Name | Description |
|---|---|
| `Binary.createFromBase64()` | Creates a binary object from a base64 value. |
| `Binary.createFromHexString()` | Creates a binary object from a hexadecimal value. |
| `BinData()` | Returns a binary data object. |
| `BulkWriteResult()` | Wrapper around the result set from `Bulk.execute()`. |
| `Date()` | Creates a date object. By default creates a date object including the current date. |
| `HexData()` | Returns a binary data object. |
| `ObjectId()` | Returns an ObjectId. |
| `ObjectId.createFromBase64()` | Creates an ObjectId from a base64 value. |
| `ObjectId.createFromHexString()` | Creates an ObjectId from a hexadecimal value. |
| `ObjectId.getTimestamp()` | Returns the timestamp portion of an ObjectId. |
| `ObjectId.toString()` | Displays the string representation of an ObjectId. |
| /reference/method/UUID | Converts a 32-byte hexadecimal string to the UUID BSON subtype. |
| `WriteResult()` | Wrapper around the result set from write methods. |

## Connections

| Name | Description |
|---|---|
| `connect()` | Connects to a MongoDB instance and to a specified database on that instance. |
| `Mongo()` | Creates a new connection object. |
| `Mongo.getDB()` | Returns a database object. |
| `Mongo.getDBNames()` | Returns a list of databases. |
| `Mongo.getDBs()` | Returns a document with a list of databases and metadata. |
| `Mongo.getWriteConcern` | Returns the write concern for the connection object. |
| `Mongo.getReadPrefMode()` | Returns the current read preference mode for the MongoDB connection. |
| `Mongo.getReadPrefTagSet()` | Returns the read preference tag set for the MongoDB connection. |
| `Mongo.setCausalConsistency()` | Enables or disables causal consistency on the connection object. |
| `Mongo.setReadPref()` | Sets the read preference for the MongoDB connection. |
| `Mongo.setWriteConcern` | Sets the write concern for the connection object. |
| `Mongo.startSession()` | Starts a session on the connection object. |
| `Mongo.watch()` | Opens a change stream cursor for a deployment to report on all its non-`system` collections across all its databases, excluding the internal `admin`, `local`, and `config` databases. |
| `Session` | The session object. |
| `SessionOptions` | The options object for the session. |

## Client-Side Field Level Encryption

**Note:**

The `mongosh` client-side field level encryption methods
require a database connection with client-side field level encryption
enabled. If the current database connection was not initiated with
client-side field level encryption enabled, either:

- Use the `Mongo()` constructor from the `mongosh`
  to establish a connection with the required client-side field
  level encryption options. The `Mongo()` method supports the
  following Key Management Service (KMS) providers for Customer
  Master Key (CMK) management:

  - Amazon Web Services KMS
  - Azure Key Vault
  - Google Cloud Platform KMS
  - Locally Managed Key

  *or*

- Use the `mongosh` command line options to establish a
  connection with the required options. The command line options only
  support the Amazon Web Services KMS provider for CMK management. 

| Name | Description |
|---|---|
| `getKeyVault()` | Returns the key vault object for the current MongoDB connection. |
| `KeyVault.createDataKey()` | An alias for `KeyVault.createKey()`. |
| `KeyVault.createKey()` | Creates a data encryption key for use with client-side field level encryption. |
| `KeyVault.deleteKey()` | Deletes the specified data encryption key from the key vault. |
| `KeyVault.getKey()` | Retrieves the specified data encryption key from the key vault. |
| `KeyVault.getKeys()` | Retrieves all keys in the key vault. |
| `KeyVault.addKeyAlternateName()` | Associates a key's alternative name to the specified data encryption key. |
| `KeyVault.addKeyAltName()` | An alias for `KeyVault.addKeyAlternateName()`. |
| `KeyVault.removeKeyAlternateName()` | Removes a key's alternative name from the specified data encryption key. |
| `KeyVault.removeKeyAltName()` | An alias for `KeyVault.removeKeyAlternateName()`. |
| `KeyVault.getKeyByAltName()` | Retrieves keys with the specified key alternative name. |
| `KeyVault.rewrapManyDataKey()` | Decrypts multiple data keys and re-encrypts them. |
| `getClientEncryption()` | Returns the client encryption object for supporting explicit encryption/decryption of fields. |
| \| `db.createEncryptedCollection()` \| `ClientEncryption.createEncryptedCollection()` | Creates a collection with encrypted fields. |
| `ClientEncryption.encrypt()` | Encrypts a field using a specified data encryption key and encryption algorithm. |
| `ClientEncryption.decrypt()` | Decrypts a field using the associated data encryption key and encryption algorithm. |
