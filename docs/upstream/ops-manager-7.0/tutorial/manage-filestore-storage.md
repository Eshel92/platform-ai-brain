<!-- Converted from tutorial/manage-filestore-storage.txt (reStructuredText). Includes are inlined. -->

# Manage File System Snapshot Storage

Ops Manager can back up MongoDB databases as snapshots
to one or more of the following storage options:

- Another MongoDB database, called a `blockstore`,
- As files stored on a local or network-attached file system, and/or
- An [S3-compatible](https://aws.amazon.com/s3/) bucket.

This tutorial covers backing up your snapshots on file system storage.

**Note:**

You might have issues that require you to use more than one snapshot
store. These issues could include needing more capacity, localizing
data, or meeting privacy regulations.

To learn how to assign snapshot stores to different data centers,
see /tutorial/assign-snapshot-stores-to-data-center.

## Considerations

- Ops Manager doesn't compress backups to file system stores from MongoDB
  databases running FCV 4.2 or later. Ops Manager ignores the
  `File System Store Gzip Compression Level` setting for those
  databases.

- .. include:: /includes/fact-shared-file-system-reqs.rst

## Prerequisites

Before creating any file system snapshot stores:

- Attach storage volumes with sufficient capacity to the Ops Manager host.
  The file system snapshot store stores only the backup snapshots. The 
  `Oplog Store` MongoDB database path 
  should be on a different local file system. To learn more, see 
  manage-oplog-storage.

- Grant the storage volumes the relevant permissions:

  - On Windows, grant access to the `SYSTEM` user.
  - On package-installed Linux distributions, grant access to the
    `mongodb-mms:mongodb-mms` user and group.
  - On archive extracted Linux distributions, grant access to the same
    user and group you assigned to the Ops Manager installation.

- Ensure the host running the Ops Manager `Backup Daemon` service
  has sufficient capacity to store the head database for FCV 4.0
  deployments and queryable restores in the head directory.

  **Note:**

  If you have not previously set the head directory,
  set it in the Head Directory box.

- When running many Ops Manager instances, use a NAS (Network Attached Storage) or SAN (Storage Area Network) for your
  file system store. This ensures that all instances share the same
  storage. You can't restore backups or remove expired snapshots if the
  Ops Manager instances don't share the file system store.

**Important:**

If the Ops Manager instances do not share the same view of file system
snapshot storage, Backup restores will not be possible and Ops Manager will
not be able to remove expired snapshots.

## Add a File System Store

**Step 1: Navigate to the Snapshot Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Snapshot Storage page.

**Step 2: Click Create New File System Store.**

**Step 3: Complete the File System Store details.**

| Field | Contents |
|---|---|
| File System Store Name | A name for the file system store. |
| Path | The file system path in which the snapshot will be stored. |
| MMapV1 Compression Setting | Select whether or not MMapV1 storage engine snapshots are compressed. Any backup job using MMapV1 snapshots inherits this setting. The default value is `on`. If you plan on using queryable backups, set this value to `off`. Queryable backup cannot query compressed snapshots. |
| WiredTiger Compression Setting | Select whether or not WiredTiger storage engine snapshots are compressed. Any backup job using WiredTiger snapshots inherits this setting. The default value is `off`. If you plan on using queryable backups, set this value to `off`. Queryable backup cannot query compressed snapshots. |
| New Assignment Enabled checkbox | This enables the filestore once it has been created. If you leave this unchecked, the filestore is created but no newly started backups can be assigned to it. |

**Step 6: Click Create.**

## Edit an Existing File System Store

Once created, file system stores are listed directly on the
Snapshot Storage page in a table. Each row contains the
settings for each File System Store.

**Step 1: Navigate to the Snapshot Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Snapshot Storage page.

**Step 2: Go to the row for the filestore you want to edit.**

**Step 3: In the Store Path column, update any values that need to be changed in the following fields:**

| Field | Contents |
|---|---|
| Store Path | The location where file system-based backups are stored on the Ops Manager server. |
| Assignment Labels | A comma-separated list of labels to assign the filestores to specific groups. |
| Load Factor | A proportional value of how backup jobs are assigned to the given snapshot store compared to other snapshot stores. By default snapshot stores assign one shard per snapshot store. If a snapshot store has more than one shard assigned, it would result in one snapshot store being backed up often than the another. This ratio of backup jobs to shards can be changed using the load factor. An example of how the Load Factor affects backups: You are backing up a 5 shard cluster. Your deployment has filestore (A) with one shard and blockstore (B) with four shards. These blockstores should not get equally distribution of backup jobs, as B is four times larger than A. B should get a Load Factor of 4 and A should get a Load Factor or 1. |

**Step 4: Check the checkbox in the Assignment Enabled column.**

**Step 5: Click Save.**

**Step 6: If you change the path, restart all the Ops Manager instances including those running Backup Daemons.**

## Delete a File System Store

**Step 1: Navigate to the Snapshot Storage page.**

a. Click the Admin link.

b. Click the Backup tab.

c. Click the Snapshot Storage page.

**Step 2: Deselect ASSIGNMENT ENABLED.**

**Step 3: Click the Delete link under the name of the filestore you want to delete.**
