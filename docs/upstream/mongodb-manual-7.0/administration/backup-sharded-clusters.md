<!-- Converted from administration/backup-sharded-clusters.txt (reStructuredText). Includes are inlined. -->

# Backup and Restore a Self-Managed Sharded Cluster

The following tutorials describe backup and restoration for sharded clusters:

**Tip:**

To use `mongodump` and `mongorestore` as a backup
strategy for sharded clusters, see backup-sharded-dumps.

Sharded clusters can also use one of the following coordinated backup
and restore processes, which maintain the atomicity guarantees of
transactions across shards:

- [MongoDB Atlas](https://www.mongodb.com/atlas/database)

- [MongoDB Cloud Manager](https://www.mongodb.com/cloud/cloud-manager)

- [MongoDB Ops Manager](https://www.mongodb.com/products/ops-manager)

/tutorial/backup-sharded-cluster-with-filesystem-snapshots
   Use file system snapshots back up each component in the sharded
   cluster individually. The procedure involves stopping the cluster
   balancer. If your system configuration allows file system backups,
   this might be more efficient than using MongoDB tools.

/tutorial/backup-sharded-cluster-with-database-dumps
   Create backups using `mongodump` to back up each
   component in the cluster individually.

/tutorial/schedule-backup-window-for-sharded-clusters
   Limit the operation of the cluster balancer to provide a window
   for regular backup operations.

/tutorial/restore-sharded-cluster
   An outline of the procedure and consideration for restoring an
   *entire* sharded cluster from backup.

restore-sharded-dumps
   Restore a sharded cluster from a backup created with
   `mongodump`.
