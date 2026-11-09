<!-- Converted from reference/monitoring.txt (reStructuredText). Includes are inlined. -->

# Database Commands Used by Monitoring

The Monitoring uses a set of the following MongoDB diagnostic, administrative,
and other database commands to report on
the status of your MongoDB deployment.

- `buildInfo`

- `collStats` on the following local database collections, which support replication
  operations:

  - `local.oplog.rs`

- `connPoolStats`

- `dbStats` The Monitoring collects storage statistics for a
  given database at 20 minute intervals.

- `find` on the following config database
  collections, which support sharding operations:

  - `config.chunks`
  - `config.collections`
  - `config.databases`
  - `config.lockpings`
  - `config.mongos`
  - `config.settings`
  - `config.shards`

- `find` on the following local database
  collections, which support replication operations:

  - `local.system.replset`

- `find` on the `system.profile <<database>.system.profile>`
  collection. Only if database profiling
  is enabled. Database profiling is disabled by default.

- `findOne` on the
  `local.oplog.rs` collection. Only for MongoDB v2.6 and earlier.

- `getCmdLineOpts`

- `getLog` issued with:

  - A value of `global`. Only if you have enabled log collection.

  - A value of `startupWarnings`.

- `getParameter` issued with a value of `*`
- `getShardVersion`
- `hostInfo`
- `listDatabases`
- `netstat`
 
- `ping`

- `profile`. Only if database profiling is enabled. Database profiling is disabled by
  default.

- `replSetGetStatus`
- `serverStatus`
