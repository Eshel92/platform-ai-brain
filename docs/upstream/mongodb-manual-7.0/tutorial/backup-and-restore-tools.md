<!-- Converted from tutorial/backup-and-restore-tools.txt (reStructuredText). Includes are inlined. -->

# Back Up and Restore with MongoDB Tools

                 

This tutorial covers creating backups and restoring data using
`mongodump` and `mongorestore`.

To restore a backup of your self-hosted deployment
to a managed [MongoDB Atlas deployment](https://www.mongodb.com/docs/atlas),
see Seed with mongorestore.

## Considerations

### Deployments

The `mongorestore` and `mongodump` utilities 
work with BSON data dumps, and are 
useful for creating backups of small deployments. For resilient and 
non-disruptive backups, use file system snapshots
or block-level disk snapshots with  
Cloud Backups from MongoDB Atlas.

**Note:** Back Up Sharded Clusters with MongoDB Atlas

To use `mongodump` and `mongorestore` as a backup
strategy for sharded clusters, see backup-sharded-dumps.

Sharded clusters can also use one of the following coordinated backup
and restore processes, which maintain the atomicity guarantees of
transactions across shards:

- [MongoDB Atlas](https://www.mongodb.com/atlas/database)

- [MongoDB Cloud Manager](https://www.mongodb.com/cloud/cloud-manager)

- [MongoDB Ops Manager](https://www.mongodb.com/products/ops-manager)

### Performance Impacts

Because `mongodump` and `mongorestore` interact with a running
`mongod` instance, they can impact database performance.
The tools create traffic and force the database to read all data
through memory. When MongoDB reads infrequently accessed data, it
evicts frequently accessed data, degrading performance for the
database's regular workload.

When backing up data with MongoDB tools, follow these guidelines:

- Label files to identify backup contents and the backup time.

- If the performance impact of `mongodump` and `mongorestore` is
  unacceptable, use an alternative such as
  Filesystem Snapshots
  or Cloud Backups in MongoDB Atlas.

- To ensure `mongodump` can take a consistent backup of
  a replica set, you must either use the 
  `--oplog` option to capture writes
  received during backup operations or stop all writes to the 
  replica set for the duration of the backup.

  For sharded cluster replica sets, see
  backup-sharded-dumps.

- Verify your backups by restoring them to a test deployment.

- To reduce backup inconsistencies in a sharded cluster, stop the
  balancer, all write operations, and any schema transformations
  during the backup.

**See also:**

For more information, see backup-methods.
For MongoDB Database Tools reference, see:

- `mongoexport`
- `mongoimport`
- `mongodump`
- `mongorestore`

### Output Format

`mongorestore` and `mongodump` can output data
to an archive file, which is a single-file alternative to multiple BSON
files. Archive files are special-purpose formats that support
non-contiguous file writes. They enable concurrent backups from MongoDB
and restores to MongoDB. Archive files also optimize disk I/O during
backup and restore.

You can also write archive files to standard output (`stdout`).
Writing to standard output enables data migration over networks,
reduced disk I/O, and concurrency gains in both MongoDB tools and
your storage engine.

For more information on archive files, see the
`--archive` option. 

### Stale Backups

Backups provide a snapshot of the current state of the database.
When you restore from a backup, the restored database doesn't
include any changes made after the backup was taken, which can
result in data loss.

## Procedures

### Back Up a Database with `mongodump`

The `mongodump` utility backs up data by connecting to
a running `mongod`. It can back up an entire server,
database, or collection, or use a query to back up part of a
collection. `mongodump` excludes the content of the `local`
database from its output.

Without any arguments, `mongodump` connects to the MongoDB instance
on the local system on port `27017` and creates a database backup
named `dump/` in the current directory:

```bash
mongodump
```

To specify the host and port, use one of the following:

- Specify the `--uri` string using an
  SRV or
  standard
  connection string:

  ```bash
  mongodump --uri="mongodb+srv://username:password@cluster0.example.mongodb.net" <additional_options>
  ```

- Specify the hostname and port in `--host`:

  ```bash
  mongodump --host="mongodb0.example.com:27017" <additional_options>
  ```

- Specify `--host` and `--port` separately:

  ```bash
  mongodump --host="mongodb0.example.com" --port=27017 <additional_options>
  ```

To specify a different output directory, use
`--out` (or `-o`):

```bash
mongodump --out=/opt/backup/mongodump-1
```

To limit the dump to a specific database or collection, use
`--db` and
`--collection`:

```none
mongodump --collection=myCollection --db=test
```

This creates a dump of `myCollection` from the `test` database
in a `dump/` subdirectory of the current directory.

`mongodump` overwrites existing files in the output folder
(default: `dump/`). Before running it multiple times, back up or
rename the output folder.

#### Required Access

To run `mongodump` against a MongoDB deployment that has
access control enabled, you must have
privileges that grant `find` action for each database to
back up. The built-in `backup` role provides the required
privileges to perform backup of any and all databases.

The `backup` role provides additional privileges to back
up the `system.profile <`
collection that exists when running with database profiling.

#### Specify Host and Port

Use `--host` and
`--port` to connect to a remote instance:

```bash
mongodump \
   --host=mongodb1.example.net \
   --port=3017 \
   --username=user \
   --password="pass" \
   --out=/opt/backup/mongodump-1
```

Specify username and password on any `mongodump` command to
authenticate.

#### Create Backups Using Oplogs

The `--oplog` option collects
oplog entries during the backup so you can restore the
database to its state at the moment the backup completed.

With `--oplog`, `mongodump` copies all data from the source
database and all oplog entries from the beginning to the end of the
backup. Use this in conjunction with
`mongorestore --oplogReplay` to
restore a backup that reflects the exact moment `mongodump`
completed.

### Restore a Database with `mongorestore`

The `mongorestore` utility restores a binary backup
created by `mongodump` by connecting to a running `mongod`
directly. By default, `mongorestore` looks for a database backup
in the `dump/` directory and can restore an entire backup or
a subset.

To connect `mongorestore` to an active `mongod`:

```bash
mongorestore --uri <connection string> <path to the backup>
```

For example, to restore from a directory:

```bash
mongorestore /opt/backup/mongodump-1
```

This restores the backup to the `mongod` instance on
`localhost:27017`.

#### Access Control

To restore data to a deployment that has access control enabled, the `restore` role provides
the necessary privileges *if* the data does not include
`system.profile <` collection data
and you run `mongorestore` without the `--oplogReplay` option.

You need additional privileges if the backup data includes
`system.profile <` collection data
or you run with `--oplogReplay`:

|  |  |
|---|---|
| `system.profile` | If the backup data includes `system.profile <` collection data and the target database does not contain the `system.profile <` collection, `mongorestore` attempts to create the collection even though the program does not actually restore `system.profile` documents. The user requires additional privileges to perform `createCollection` and `convertToCapped` actions on the `system.profile <` collection for a database. Both the built-in roles `dbAdmin` and `dbAdminAnyDatabase` provide the additional privileges. |
| `--oplogReplay` | To run with `--oplogReplay`, create a user-defined role that has `anyAction` on resource-anyresource. Grant only to users who must run `mongorestore` with `--oplogReplay`. |

#### Specify Host and Port

By default, `mongorestore` connects to `localhost:27017`. To
restore to a different host or port, use `--host` and `--port`:

```bash
mongorestore --host=mongodb1.example.net --port=3017
```

To authenticate, include
`--username` and
`--authenticationDatabase`. Omit
`--password` to have
`mongorestore` prompt for the password:

```bash
mongorestore \
   --host=mongodb1.example.net \
   --port=3017 \
   --username=user \
   --authenticationDatabase=admin \
   /opt/backup/mongodump-1
```

#### Use an Oplog File to Restore Data

To capture writes that occur while `mongodump` is running, use
`--oplog`. `mongodump` creates an `oplog.bson` file with oplog
entries for each write during the run. Apply those operations with
`--oplogReplay` when restoring.

For examples, see mongodump-examples and
mongorestore-examples.

`mongorestore --oplogReplay` restores all data from `oplog.bson`
but does not support restoring to an arbitrary point in time. Use it
to ensure the restored data reflects any writes that occurred during
the `mongodump --oplog` run.

**Note:**

`--oplog` is intended for use with replica sets. For sharded
clusters, including replica sets that are part of a sharded
environment, see backup-sharded-dumps.

Use `--objcheck` to validate
document integrity during insertion, or
`--drop` to drop each collection
before restoring.
