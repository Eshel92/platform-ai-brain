<!-- Converted from tutorial/delete-backup-snapshots.txt (reStructuredText). Includes are inlined. -->

# Delete a Snapshot

To delete snapshots for replica sets and sharded clusters, use the
Ops Manager console to find then select a backup snapshot to delete.

**Important:** Affects next backup and point-in-time restores

- The next backup job runs as a full backup rather than an
  incremental backup.

- Point-in-time restores apply oplog entries to the last snapshot
  taken before the specified point. Deleting a snapshot removes the
  base snapshot for a PIT restore.

## Procedure

**Step 1: Click Continuous Backup, then the Overview tab.**

**Step 2: On the line listing the process, click the ellipsis icon and click View All Snapshots.**

**Step 3: Select backup file to delete.**

On the list of snapshots, click the Delete link to the right 
of a snapshot.

**Step 4: Confirm deletion.**

Click the OK button on the Delete Snapshot interface 
to confirm deletion of the backup.
