<!-- Converted from tutorial/restore-replica-set-from-backup.txt (reStructuredText). Includes are inlined. -->

# Restore a Self-Managed Replica Set from MongoDB Backups

This procedure outlines the process for taking MongoDB data and
restoring that data into a new replica set. Use this approach
for seeding test deployments from production backups or as part
of disaster recovery.

**Important:**

You *cannot* restore a single data set to three new `mongod`
instances and **then** create a replica set. If you copy the data set
to each `mongod` instance and then create the replica set,
MongoDB will force the secondaries to perform an initial
sync. The procedures in this document describe the correct and
efficient ways to deploy a restored replica set.

You can also use `mongorestore` to restore database files
using data created with `mongodump`. See
/tutorial/backup-and-restore-tools for more information.

## Considerations

Backups provide a snapshot of the current state of the database.
When you restore from a backup, the restored database doesn't
include any changes made after the backup was taken, which can
result in data loss.

## Restore Database into a Single Node Replica Set

**Step 1: Obtain backup MongoDB Database files.**

The backup files may come from a file system snapshot. The [MongoDB Cloud Manager](https://www.mongodb.com/products/tools/cloud-manager?tck=docs_server)
produces MongoDB database files for `stored snapshots` and `point in time
snapshots`.
For Ops Manager, an on-premises solution available in
MongoDB Enterprise Advanced,
see also the `Ops Manager Backup overview`.

Considerations for Encrypted Storage Engines
   For encrypted storage engines that
   use `AES256-GCM` encryption mode, `AES256-GCM` requires that every
   process use a unique counter block value with the key.

   For encrypted storage engine
   configured with `AES256-GCM` cipher:

   - Restoring from Hot Backup
         Starting in 4.2, if you restore from files taken via "hot"
         backup (i.e. the `mongod` is running), MongoDB
         can detect "dirty" keys on startup and automatically rollover
         the database key to avoid IV (Initialization Vector) reuse.

   - Restoring from Cold Backup
         However, if you restore from files taken via "cold" backup
         (i.e. the `mongod` is not running), MongoDB
         cannot detect "dirty" keys on startup, and reuse of IV voids
         confidentiality and integrity guarantees.

         Starting in 4.2, to avoid the reuse of the keys after
         restoring from a cold filesystem snapshot, MongoDB adds a new
         command-line option `--eseDatabaseKeyRollover`. When started with the
         `--eseDatabaseKeyRollover` option, the `mongod`
         instance rolls over the database keys configured with
         `AES256-GCM` cipher and exits.

**Step 2: Drop the `local` database if it exists in the backup.**

If you are restoring from a filesystem backup (or any backup with
the `local` database), drop the `local` database.

You must also specify the same startup options that were used when the snapshot was created.

```sh
mongod --dbpath /data/db <startup options>
```

Connect `mongosh` to the `mongod`
instance and drop the `local` database.

```javascript
use local
db.dropDatabase()
```

Shut down the standalone.

**Step 3: Start a new single-node replica set.**

Start a `mongod` instance as a new single-node replica set.
Specify the path to the backup data files with `--dbpath` option
and the replica set name with the `--replSet` option. 
For config server replica set (CSRS),
include the `--configsvr` option.
Include any other options as appropriate for your deployment.

You must also specify the same startup options
that were used when the snapshot was created.

**Note:**

If your replica set members are run on
different hosts or if you wish remote clients to connect to your
instance, you must specify the `net.bindIp` setting (or
`--bind_ip`).

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

```sh
mongod --dbpath /data/db --replSet <replName> <startup options>
```

**Step 4: Connect `mongosh` to the `mongod` instance.**

From the same machine where one of the `mongod` is running
(in this tutorial, `mongodb0.example.net`), start
`mongosh`. To connect to the `mongod`
listening to localhost on the default port of `27017`, simply issue:

```sh
mongosh
```

Depending on your path, you may need to specify the path to the
`mongosh` binary.

If your `mongod` is not running on the default port, specify the
`--port` option for `mongosh`.

**Step 5: Initiate the new replica set.**

Use `rs.initiate()` on *one and only one* member of the replica set:

```javascript
rs.initiate( {
   _id : <replName>,
   members: [ { _id : 0, host : <host:port> } ]
})
```

MongoDB initiates a set that consists of the current member and that
uses the default replica set configuration.

## Add Members to the Replica Set

MongoDB provides two options for restoring secondary members of a
replica set:

- Manually copy the database files
  to each data directory.

- Allow initial sync to distribute
  data automatically.

**Note:**

If your database is large, initial sync can take a long time to
complete. For large databases, it might be preferable to copy the
database files onto each host.

### Copy Database Files and Restart `mongod` Instance

Use the following sequence of operations to "seed" additional members
of the replica set with the restored data by copying MongoDB data
files directly.

**Step 1: Shut down the `mongod` instance that you restored.**

Use `--shutdown` or
`db.shutdownServer()` to ensure a clean shut down.

**Step 2: Copy the primary's data directory to each secondary.**

Copy the primary's data directory into the
`dbPath` of the other members of the replica set.

**Step 3: Start the `mongod` instance that you restored.**

**Step 4: Add the secondaries to the replica set.**

In a `mongosh` session that is connected to the
primary, add the secondaries to the
replica set using the `rs.add()` method. See
/tutorial/deploy-replica-set for more information about
deploying a replica set.

### Update Secondaries using Initial Sync

Use the following sequence of operations to "seed" additional members
of the replica set with the restored data using the default initial
sync operation.

**Step 1: Empty the data directory for each prospective replica set member.**

For example, if the replica set member has a 
`storage.dbPath` or `--dbpath`
of `/data/db`, you **must** ensure that directory exists *and*
is empty.

**Step 2: Start each replica set member.**

**Step 3: Add each prospective member to the replica set.**

Connect to the primary using the `mongo`
shell and add each secondary to the replica set using
`rs.add()`.

When you add a member to the replica set, Initial Sync copies the data from the primary to
the new member.
