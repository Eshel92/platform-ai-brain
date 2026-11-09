<!-- Converted from admin/backup/resource-usage-page.txt (reStructuredText). Includes are inlined. -->

# Resource Usage

This page provides key size and throughput statistics on a per-job
basis for all projects for which you enabled backup.

Ops Manager displays a list of the following information in two tables
Per Job and Per Project:

* - Column Title
  - Content

* - HEAD Usage
  - Displays the following statistics for the `head database`
    of any backup job with FCV 4.0 or earlier:

    - `Data Size`
    - `Storage Size`
    - File Size: The sum of the uncompressed size of each file in
      the HEAD database
    - Storage Engine

* - Oplog Receiving (last 24 hours)
  - Displays statistics for oplog throughput over the past 24 hours.

* - Oplog Application (last 24 hours)
  - Displays statistics for oplog processing over the past 24 hours.

* - SnapshotStore usage
  - Displays the following information:

    - The size of both the live and dead bytes for the job in the
      snapshot store
    - Timestamp for when Ops Manager last groomed this backup job
    - Timestamp for when Ops Manager last ran tracking job for this
      backup job

    The Resource Tracking job gathers
    these statistics.

**Note:** Multiple backup jobs use the same snapshot store.

To export this information, click Export as CSV.
