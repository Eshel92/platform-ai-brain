<!-- Converted from tutorial/resync-backup.txt (reStructuredText). Includes are inlined. -->

# Resync a Backup

**Note:**

You don't need to resync MongoDB databases that run with an
FCV of 4.2 or later.

When a backup becomes out of sync with the MongoDB deployment, Ops Manager
produces a `Backup requires a resync` alert. If you
receive this alert, you must resync the backup for the specified
MongoDB instance.

The following scenarios trigger a `Backup requires a resync` alert:

The Oplog has rolled over
  This is the most common case for the
  `Backup requires a resync` alert. It occurs whenever
  the Backup's tailing cursor
  cannot keep up with the deployment's oplog. This is similar
  to when a secondary falls too far behind the primary in a
  replica set. Without a resync, the backups will not catch up.

Unsafe applyOps
  This occurs when a document that Backup does not have a copy of is
  indicated.

Data corruption or other illegal instruction
  This typically causes replication, and therefore the backup job, to
  break. When the daemon sees the broken job, it requests a resync.

During the resync, data is read from a secondary in each replica set
and Ops Manager does not produce any new snapshots.

**Note:**

For production deployments with an FCV of 4.0 or earlier, you 
should resync all backups annually.

**Important:**

Ops Manager does not attempt to automatically recover from conditions that
caused the `Backup requires a resync` alert. This
alert means there is not enough data to complete a restore. There is
no way to automatically recover from not having enough data from the
snapshots and the oplog. Resyncing the backup is the best option.

## Considerations

As of FCV 4.2, deployments are backed up with WiredTiger checkpoints
using backup cursors. Applications can 
continue read and write operations on the database while WiredTiger
takes the snapshot.

For production deployments with an FCV of 4.0 or earlier, to 
avoid the need for resyncs, ensure the Backup oplog does not fall
behind the deployment's oplog. This requires that:

- Adequate machine resources are provisioned for the agent.

- You restart the Ops Manager agents in a timely manner following maintenance
  or other downtime.

To provide a buffer for maintenance and for occasional activity bursts,
ensure that the oplog on the primary is large enough to contain
at least 24 hours of activity.

You should resync the head database after you
create an index in a rolling fashion to
ensure that the head database takes the new index into account.

**See also:**

For more information on the Backup oplog, see the faq-backup.

## Procedure

**Step 1: Click Continuous Backup, then the Overview tab.**

**Step 2: On the line listing the process, click the ellipsis icon and click Resync.**

**Step 3: Click the Resync button.**

If prompted for an authentication code, enter the code and click
Verify. Click Resync again.
