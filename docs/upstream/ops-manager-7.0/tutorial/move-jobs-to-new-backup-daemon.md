<!-- Converted from tutorial/move-jobs-to-new-backup-daemon.txt (reStructuredText). Includes are inlined. -->

# Move Jobs from a Lost Backup Daemon to another Backup Daemon

If the server running a Backup Daemon fails, and
if you run multiple Backup Daemons,
then an administrator with the `Global Owner`
or global backup admin role role
can move all the daemon's jobs to another Backup Daemon. The new
daemon takes over the responsibility to back up the associated
shards and replica sets.

When you move jobs, the destination daemon reconstructs the data using
a snapshot and the oplog from the backup-database.
Reconstruction of data takes time, depending on the size of the
databases on the source.

During the time it takes to reconstruct the data and reassign the
backups to the new Backup Daemon:

- Ops Manager does not take new snapshots of the jobs that are moving until
  the move is complete. Jobs that are not moving are not affected.

- Ops Manager *does* save incoming oplog data. Once the jobs are on the new
  Backup Daemon's server, Ops Manager takes the missed snapshots at the
  regular snapshot intervals.

- Restores of previous snapshots are still available.

- Ops Manager can produce restore artifacts using existing snapshots with
  point-in-time restore for replica sets
  or sharded clusters that run FCV of
  4.2 or later. (Sharded clusters that run
  FCV (Feature Compatibility Version) of 4.0 or earlier can use checkpoints.)

## Procedure

With administrative privileges, you can move jobs between Backup
daemons using the following procedure:

**Step 1: Click the Admin link at the top of Ops Manager.**

**Step 2: Select Backup and then select Daemons.**

The Daemons page lists all active Backup Daemons.

**Step 3: Locate the failed Backup Daemon and click the Move all heads link.**

Ops Manager displays a drop-down list from which to choose the destination daemon.
The list displays only those daemons with more free space than there is
used space on the source daemon.

**Step 4: Move the jobs to the new daemon.**

Select the destination daemon and click the Move all heads
button.
