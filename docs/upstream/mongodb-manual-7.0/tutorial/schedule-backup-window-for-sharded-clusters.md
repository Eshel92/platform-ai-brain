<!-- Converted from tutorial/schedule-backup-window-for-sharded-clusters.txt (reStructuredText). Includes are inlined. -->

# Schedule Backup Window for a Self-Managed Sharded Cluster

## Overview

In a sharded cluster, the balancer process is responsible for
distributing sharded data around the cluster, so that each
shard has roughly the same amount of data.

However, when creating backups from a sharded cluster it is important
that you disable the balancer while taking backups to ensure that no
chunk migrations affect the content of the backup captured by the
backup procedure. 

**Note:**

Disabling the balancer is only necessary when **manually** taking backups,
either by calling `mongodump` or scheduling a task that calls
`mongodump` at a specific time.

You do **not** have to disable the balancer when using coordinated backup
and restore processes:

- [MongoDB Atlas](https://www.mongodb.com/atlas/database)

- [MongoDB Cloud Manager](https://www.mongodb.com/cloud/cloud-manager)

- [MongoDB Ops Manager](https://www.mongodb.com/products/ops-manager)

Using the procedure outlined in the section
sharding-balancing-disable-temporarily you can manually stop the
balancer process temporarily. As an alternative, you can
use the following procedure to define a balancing window so that the
balancer is always disabled during your automated backup operation.

**Tip:**

To use `mongodump` and `mongorestore` as a backup
strategy for sharded clusters, see backup-sharded-dumps.

Sharded clusters can also use one of the following coordinated backup
and restore processes, which maintain the atomicity guarantees of
transactions across shards:

- [MongoDB Atlas](https://www.mongodb.com/atlas/database)

- [MongoDB Cloud Manager](https://www.mongodb.com/cloud/cloud-manager)

- [MongoDB Ops Manager](https://www.mongodb.com/products/ops-manager)

## Procedure

If you have an automated backup schedule, you can disable all
balancing operations for a period of time. For instance, consider the
following command:

```javascript
use config
db.settings.updateOne(
   { _id : "balancer" }, 
   { $set : { activeWindow : { start : "06:00", stop : "23:00" } } }, 
   true
)
```

This operation configures the balancer to run between 6:00am and
11:00pm, server time. Schedule your backup operation to run *and
complete* outside of this time. Ensure that the backup can complete
outside the window when the balancer is running *and* that the
balancer can effectively balance the collection among the shards
in the window allotted to each.
