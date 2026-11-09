<!-- Converted from tutorial/stop-restart-terminate-backup.txt (reStructuredText). Includes are inlined. -->

# Stop, Restart, or Terminate a Backup

When you stop backups for a replica set or sharded cluster Ops Manager stops
taking new snapshots but retains existing snapshots until their listed
expiration date.

If you later restart backups for replica set or cluster, Ops Manager might
perform an `initial sync`, depending on how much time has elapsed.

If you **terminate** a backup, Ops Manager immediately **deletes all the
backup's snapshots.**

## Stop Backup for a Deployment

**Step 1: Click Continuous Backup, then the Overview tab.**

**Step 2: On the line listing the process, click the ellipsis icon and click Stop.**

**Step 3: Click the Stop button.**

If prompted for an authentication code, enter the code and click
Verify. Click Stop again.

## Restart Backup for a Deployment

**Step 1: Click Continuous Backup, then the Overview tab.**

**Step 2: On the line listing the process, click the ellipsis icon and click Restart.**

**Step 3: Select a Sync source and click Restart.**

## Terminate a Deployment's Backups

**Warning:** Terminating a backup triggers a full backup

If you terminate a backup, Ops Manager immediately deletes the backup's
snapshots. The next backup job runs as a full backup rather than an
incremental backup.

**Step 1: Click Continuous Backup, then the Overview tab.**

**Step 2: Click the ellipsis-h next to the backup.**

**Step 3: Click the Stop button.**

If prompted for an authentication code, enter the code and click
Verify. Click Stop again.

**Step 4: Once the backup has stopped, click the backup's ellipsis icon and click Terminate.**

**Step 5: Click the Terminate button.**

## Force Terminate a Deployment's Backups

If your attempt to terminate backups fails and you still need to
terminate regardless of any errors, you can force terminate the
backups.

**Note:**

If you wish to Force Terminate backups on a sharded cluster, you
must repeat the following steps for each backup job on each shard
or config server.

**Important:**

You should make sure that the Backup Job you want to terminate is
in the Terminating state.

**Step 1: Navigate to the Administration Backup Jobs page.**

a. Click the Admin link at the top right.
b. Click the Backup tab.
c. Click the Jobs page.
d. Click Search to display all backup jobs, or apply search 
   filters before you click Search to filter the results.

**Step 2: Find then Force Terminate the Backup Job.**

a. Click on the Replica Set ID for the Backup Job to 
   terminate.
b. Click the Force Terminate link for that job.
c. On the Force Terminate Backup modal, click 
   Force Terminate.
