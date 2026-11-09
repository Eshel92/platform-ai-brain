<!-- Converted from tutorial/restore-full-snapshot-http.txt (reStructuredText). Includes are inlined. -->

# Restore a Completed Snapshot

To restore a snapshot, Ops Manager creates and
displays a download link to the appropriate snapshot in
the snapshot storage.

After clicking the download link, Ops Manager streams the snapshot to the
target snapshot host.

**fcv42:**

(Figure: /images/restore-full-wt.bakedsvg.svg)

1. The user selects a snapshot:

   - Through the Ops Manager application:

     1. Click on a snapshot.
     #. Submit their request.

   - Through the API:

     1. Find the cluster to restore.
     #. Create new Restore Job
        for that cluster.

#. Ops Manager creates a RestoreJob document.

#. Ops Manager sets the RestoreJob document status to
   Transferring... and starts streaming the
   snapshot in the requested format from the
   `snapshot store` to Ops Manager. Each
   Snapshot Store streams its snapshot components through Ops Manager:

   - A blockstore streams
      the blocks.
   - An `S3 snapshot store` streams the blocks.

#. With the status set to Waiting for Customer...,
   Ops Manager creates a URL (Uniform Resource Locator).

#. The user clicks the get link link, then
   Download in the Ops Manager application to
   download the snapshot.

**fcv40:**

(Figure: /images/restore-regular-http.bakedsvg.svg)

1. The user selects a snapshot:

   - Through the Ops Manager application:

     1. Click on a snapshot.
     #. Submit their request.

   - Through the API:

     1. Find the cluster to restore.
     #. Create new Restore Job
        for that cluster.

#. Ops Manager creates a RestoreJob document.

#. The `Backup Daemon` service picks up the RestoreJob
   document and sets the status of this RestoreJob document to
   Waiting for Customer....

#. With the status set to Waiting for Customer...,
   Ops Manager creates a URL (Uniform Resource Locator).

#. The user clicks the get link link, then
   Download in the Ops Manager application to
   download the snapshot.

#. Ops Manager sets the RestoreJob document status to
   Transferring... and starts streaming the
   snapshot in the requested format from the
   `snapshot store` to the target snapshot host. Each
   Snapshot Store streams its snapshot components through Ops Manager:

   - A blockstore streams
      the blocks.
   - An `S3 snapshot store` streams the blocks.
   - A `file system store` streams the files.

This process works like
replica set data synchronization.

The backup process:

1. Performs an `initial sync` to back up all of your existing
   data in its current state.
   In sharded clusters, this occurs on each
   shard and on the config servers.

   **Note:** Conditions or Actions that Restart Initial Sync

   During the initial sync process, certain actions or conditions
   can restart the initial sync process. Avoid the following actions
   and conditions:

   **Actions to Avoid during Initial Sync:**

   - Restarting, shutting down, or changing the version or
     FCV (Feature Compatibility Version) value of the source database.
   - Renaming the collection
     of the source database.
   - Changing the $out
     value in the Aggregation Pipeline of the source database.
   - Restarting or shutting down Ops Manager Application or Backup Daemon.
   - Restarting, shutting down, or upgrading the
     MongoDB Agent.

   **Conditions to Avoid during Initial Sync:**

   - Head Directory is full.
   - Network connectivity between Ops Manager components is
     unstable.

#. Takes snapshots of the `data` directory in a deployment as often
   as your snapshot schedule
   specifies and then transfers the snapshots to a storage system.

   **Note:**

   Sharded Clusters also can
   enable checkpoints to permit
   restores at points in time between snapshots. To learn how
   sharded clusters use checkpoints, see
   checkpoints.

   **Important:**

   You may use checkpoints for clusters that run MongoDB with
   Feature Compatibility Version of 4.0 or earlier. Checkpoints were removed from
   MongoDB instances with FCV (Feature Compatibility Version) of 4.2 or later.

#. Monitors the oplog constantly and adds new database
   operations to the latest backup to keep the local Ops Manager copy of
   the data current.

The backup process works in this manner regardless of how snapshots are
stored.
