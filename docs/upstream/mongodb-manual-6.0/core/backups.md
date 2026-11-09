<!-- Converted from core/backups.txt (reStructuredText). Includes are inlined. -->

# Backup Methods for a Self-Managed Deployment

When deploying MongoDB in production, you should have a 
strategy for capturing and restoring backups in the case of data loss
events.

This page covers backup methods for self-managed 
deployments.

To learn more about Backup Methods for deployments hosted in MongoDB
Atlas, see Back Up, Restore, and Archive Data.

## Back Up with MongoDB Cloud Manager or Ops Manager

MongoDB Cloud Manager is a hosted back up, monitoring, and automation service for
MongoDB. [MongoDB Cloud Manager](https://www.mongodb.com/products/tools/cloud-manager?tck=docs_server) supports backing up and restoring MongoDB
replica sets and sharded clusters from a graphical user interface.

### MongoDB Cloud Manager

**Important:**

To back up your replica sets and sharded clusters using MongoDB Cloud Manager, 
you must be using MongoDB Enterprise Server. 
For more information, see install-mdb-enterprise.

The [MongoDB Cloud Manager](https://www.mongodb.com/products/tools/cloud-manager?tck=docs_server) supports the backing up and restoring of MongoDB
deployments.

MongoDB Cloud Manager continually backs up MongoDB replica sets
and sharded clusters by reading the
oplog data from your MongoDB deployment. MongoDB Cloud Manager creates snapshots
of your data at set intervals, and can also offer point-in-time recovery
of MongoDB replica sets and sharded clusters.

**Tip:**

Sharded cluster snapshots are difficult to achieve with other MongoDB
backup methods.

To get started with MongoDB Cloud Manager Backup, sign up for [MongoDB Cloud Manager](https://www.mongodb.com/products/tools/cloud-manager?tck=docs_server). For
documentation on MongoDB Cloud Manager, see the `MongoDB Cloud Manager documentation`.

### Ops Manager

With Ops Manager, MongoDB subscribers can install and run the same core
software that powers backup-with-mms on their own infrastructure.
Ops Manager is an on-premises solution that has similar functionality to
MongoDB Cloud Manager and is available with Enterprise Advanced subscriptions.

For more information about Ops Manager, see the [MongoDB Enterprise Advanced](https://www.mongodb.com/products/mongodb-enterprise-advanced?tck=docs_server) page
and the `Ops Manager Manual`.

## Back Up by Copying Underlying Data Files

**Note:** Considerations for Encrypted Storage Engines using AES256-GCM

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

In general, if using filesystem based backups for MongoDB Enterprise, use 
the "hot" backup feature, if possible.

### Back Up with Filesystem Snapshots

You can create a backup of a MongoDB deployment by making a copy of MongoDB's
underlying data files.

If the volume where MongoDB stores its data files supports point-in-time
snapshots, you can use these snapshots to create backups of a MongoDB
system at an exact moment in time.
File system snapshots are an operating system volume manager feature,
and are not specific to MongoDB. With file system snapshots, the operating
system takes a snapshot of the volume to use as a baseline for data backup.
The mechanics of snapshots depend on
the underlying storage system. For example, on Linux, the Logical Volume
Manager (LVM) can create snapshots. Similarly, Amazon’s EBS storage
system for EC2 supports snapshots.

To get a correct snapshot of a running `mongod` process, you
must have journaling enabled and the journal must reside on the same
logical volume as the other MongoDB data files. Without journaling
enabled, there is no guarantee that the snapshot will be consistent or
valid.

To get a consistent snapshot of a sharded cluster, you must
disable the balancer and capture a snapshot from every shard as well as a
config server at approximately the same moment in time.
To backup sharded clusters, see backup-sharded-dumps.

For more information, see the
/tutorial/backup-with-filesystem-snapshots and
/tutorial/backup-sharded-cluster-with-filesystem-snapshots for
complete instructions on using LVM to create snapshots.

### Back Up with `cp` or `rsync`

If your storage system does not support snapshots, you can copy the
files directly using `cp`, `rsync`, or a similar tool. Since
copying multiple files is not an atomic operation, you must stop all
writes to the `mongod` before copying the files. Otherwise, you will
copy the files in an invalid state.

Backups produced by copying the underlying data do not support point
in time recovery for replica sets and are difficult to manage for
larger sharded clusters. Additionally, these backups are larger
because they include the indexes and duplicate underlying storage
padding and fragmentation. `mongodump`, by contrast, creates
smaller backups.

## Back Up with `mongodump`

`mongodump` reads data from a MongoDB database and
creates high fidelity BSON files which the `mongorestore`
tool can use to populate a MongoDB database.
`mongodump` and `mongorestore` are simple and
efficient tools for backing up and restoring small
MongoDB deployments, but are not ideal for capturing backups of larger
systems.

`mongodump` and `mongorestore` operate against a
running `mongod` process, and can manipulate the underlying
data files directly. By default, `mongodump` does not
capture the contents of the local database.

`mongodump` only captures the documents in the database. The
resulting backup is space efficient, but `mongorestore` or
`mongod` must rebuild the indexes after restoring data.

When connected to a MongoDB instance, `mongodump` can
adversely affect `mongod` performance. If your data is larger
than system memory, the queries will push the working set out of
memory, causing page faults.

Applications can continue to modify data while `mongodump`
captures the output. For replica sets, `mongodump` provides
the `--oplog` option to include in its
output oplog entries that occur during the `mongodump`
operation. This allows the corresponding `mongorestore`
operation to replay the captured oplog. To restore a backup created
with `--oplog`, use `mongorestore`
with the `--oplogReplay` option.

However, for replica sets, consider backup-with-mms or
backup-with-mms-onprem.

To backup sharded clusters, see backup-sharded-dumps.

**Note:**

To use `mongodump` and `mongorestore` as a backup
strategy for sharded clusters, see backup-sharded-dumps.

Sharded clusters can also use one of the following coordinated backup
and restore processes, which maintain the atomicity guarantees of
transactions across shards:

- [MongoDB Atlas](https://www.mongodb.com/atlas/database?tck=docs_server)

- [MongoDB Cloud Manager](https://www.mongodb.com/cloud/cloud-manager?tck=docs_server)

- [MongoDB Ops Manager](https://www.mongodb.com/products/ops-manager?tck=docs_server)

See /tutorial/backup-and-restore-tools
and /tutorial/backup-sharded-cluster-with-database-dumps
for more information.
