<!-- Converted from reference/command/nav-administration.txt (reStructuredText). Includes are inlined. -->

# Administration Commands

**Note:**

For details on a specific command, including syntax and examples,
click on the link to the command's reference page.

* - Name

  - Description

* - `cloneCollectionAsCapped`

  - Copies a non-capped collection as a new capped collection.

* - `collMod`

  - Add options to a collection or modify a view definition.

* - `compact`

  - Defragments a collection and rebuilds the indexes.

* - `convertToCapped`

  - Converts a non-capped collection to a capped collection.

* - `create`

  - Creates a collection or a view.

* - `createIndexes`

  - Builds one or more indexes for a collection.

* - `currentOp`

  - Returns a document that contains information on in-progress operations for the database instance.

* - `drop`

  - Removes the specified collection from the database.

* - `dropDatabase`

  - Removes the current database.

* - `dropConnections`

  - Drops outgoing connections to the specified list of hosts.

* - `dropIndexes`

  - Removes indexes from a collection.

* - `filemd5`

  - Returns the md5 hash for files stored using GridFS.

* - `fsync`

  - Flushes pending writes to the storage layer and locks the database to allow backups.

* - `fsyncUnlock`

  - Unlocks one fsync lock.

* - `getDefaultRWConcern`

  - Retrieves the global default read and write concern options
    for the deployment.

* - `getAuditConfig`

  - Retrieves details on audit configuration and filters.

    **New in version:** 5.0

* - `getClusterParameter`

  - Retrieves cluster parameter values from all nodes in a cluster.

    **New in version:** 6.0

* - `getParameter`

  - Retrieves configuration options.

* - `killCursors`

  - Kills the specified cursors for a collection.

* - `killOp`

  - Terminates an operation as specified by the operation ID.

* - `listCollections`

  - Returns a list of collections in the current database.

* - `listDatabases`

  - Returns a document that lists all databases and returns basic database statistics.

* - `listIndexes`

  - Lists all indexes for a collection.

* - `logRotate`

  - Rotates the MongoDB logs to prevent a single file from taking too much space.

* - `reIndex`

  - Rebuilds all indexes on a collection.

* - `renameCollection`

  - Changes the name of an existing collection.

* - `rotateCertificates`

  - Performs online TLS certificate rotation.

* - `setFeatureCompatibilityVersion`

  - Enables or disables features that persist data that are backwards-incompatible.

* - `setIndexCommitQuorum`

  - Changes the minimum number of data-bearing members (i.e commit
    quorum), including the primary, that must vote to commit an
    in-progress index build before the primary marks
    those indexes as ready.

* - `setClusterParameter`

  - Modifies configuration options for all nodes in a cluster.

    **New in version:** 6.0

* - `setParameter`

  - Modifies configuration options.

* - `setDefaultRWConcern`

  - Sets the global default read and write concern options for the
    deployment.

* - `shutdown`

  - Shuts down the `mongod` or `mongos` process.
