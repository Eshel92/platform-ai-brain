<!-- Converted from reference/method/js-database.txt (reStructuredText). Includes are inlined. -->

# Database Methods

**Note:**

For details on a specific method, including syntax and examples,
click on the link to the method's reference page.

| Name | Description |
|---|---|
| `db.adminCommand()` | Runs a command against the `admin` database. |
| `db.aggregate()` | Runs admin/diagnostic pipeline which does not require an underlying collection. |
| `db.commandHelp()` | Returns help information for a database command. |
| `db.createCollection()` | Creates a new collection or a view. Commonly used to create a capped collection. |
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
| `db.printReplicationInfo()` | Prints a formatted report of the replica set status from the perspective of the primary. |
| `db.printSecondaryReplicationInfo()` | Prints a formatted report of the replica set status from the perspective of the secondaries. |
| `db.printShardingStatus()` | Prints a report of the sharding configuration and the chunk ranges. |
| `db.resetError()` | *Removed in MongoDB 5.0.* Resets the last error status. |
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
