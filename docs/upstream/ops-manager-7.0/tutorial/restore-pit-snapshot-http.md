<!-- Converted from tutorial/restore-pit-snapshot-http.txt (reStructuredText). Includes are inlined. -->

# Restore from a Specific Point-in-Time

To restore a snapshot using HTTP (Hypertext Transfer Protocol), Ops Manager
creates and displays a download link to the appropriate
snapshot in snapshot storage.

After clicking the download link, Ops Manager streams the snapshot to the
target snapshot host.

**Note:**

PIT restores include points in time and oplog timestamps. PIT (point in time)
restores include checkpoints for sharded clusters running FCV
of 4.0 or earlier.

(Figure: /images/restore-full-wt.bakedsvg.svg)

## Considerations

- The Ops Manager point-in-time restore might have oplog gaps in some
  situations such as the following:

  - If the oplog tailing stops because of an issue with backup
    job tailing the oplog and the oplog rolls over before
    MongoDB Agent tails it again.

  - After a topology change until Ops Manager completes a new snapshot.

  - After the FCV (Feature Compatibility Version) change, which causes a gap between the time Ops Manager detects
    the FCV (Feature Compatibility Version) change and Ops Manager completes a new snapshot. You can't apply a
    point-in-time restore across MongoDB version changes.

  - After a restore until Ops Manager completes a new snapshot.

- If there is an oplog gap after Ops Manager takes the latest snapshot, then a
  point-in-time restore fails if the restore time selected is after
  the oplog gap began and before the next snapshot. Once Ops Manager takes the
  next snapshot, you can use point-in-time restore as normal from that
  snapshot time onward.

- You only see oplog gaps when you attempt and fail a point-in-time
  restore.

- You can request a point-in-time restore to a specific point in time
  that includes stale data.

## Procedure

1. The user selects a timestamp:

   - Through the Ops Manager application:

     1. Click on a timestamp.
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

   a. A blockstore streams
      blocks.
   #. A `S3 snapshot store` streams the blocks.

#. With the status set to Waiting for Customer..., Ops Manager
   creates a URL (Uniform Resource Locator).

#. The user clicks the get link link, then
   Download in the Ops Manager application to download the
   snapshot.

#. The user downloads the MongoDB Backup Restore Utility from the Ops Manager
   application to the target snapshot host.

   **Note:**

   The MBRU (MongoDB Backup Restore Utility) can be used with any restore. If the utility is
   installed on the host where you want to restore the snapshot, the
   user doesn't need to download it again.

#. The user starts a temporary MongoDB instance on the target snapshot
   host. The fetched oplog is applied to the snapshot restored
   to this instance.

#. The user runs the MBRU (MongoDB Backup Restore Utility) to request the oplog.

#. The MBRU (MongoDB Backup Restore Utility) fetches the oplog for the point-in-time snapshot.

#. The MBRU (MongoDB Backup Restore Utility) applies the oplog to snapshot in the temporary MongoDB
   instance.

#. The user exports the restored database from the temporary MongoDB
   instance.
