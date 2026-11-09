<!-- Converted from admin/backup/groom-priority-page.txt (reStructuredText). Includes are inlined. -->

# Groom Priority

This page displays a list of the status of all of the backup jobs and
their blockstores. Ops Manager maintains a blockstore using three jobs:

* - Job Type
  - Description
  - Trigger

* - Resource Tracking
  - Determines the total number of living and dead bytes in
    blockstores.
  -
    - Runs every three days
    - Runs immediately after a groom job

* - Groom
  - Moves all blocks of living snapshots to an unused span of disk
    space. This removes any dead blocks that only previously expired
    snapshots used.
  - Runs when the percentage of living block bytes drops
    below a given threshold.

    To learn more, see Grooms.

* - Integrity Check
  - Verify that the blockstore has no data integrity issues.
  - Runs every seven days

Each blockstore job runs unless a previously scheduled snapshot
store job remains in progress.

Each blockstore can run only one job at a time unless you change
its Load Factor. The
Load Factor sets how many jobs that a blockstore can
run at the same time. Set to `1` by default.

**See also:**

To learn how to change the Load Factor, see
Edit a Blockstore.

Each row in this table lists a backup job. The background color of the
row indicates the state of its associated blockstore.

| Color | Storage Usage Status |
|---|---|
| Blue | Changing. Ops Manager is grooming this blockstore. |
| Green | Accurate. Ops Manager ran a tracking job since last groom job ran. |
| Red | Stale. Ops Manager ran a groom job since its last tracking job ran. |

## Manual Blockstore Maintenance

Ops Manager runs the Resource Tracking, Groom and Integrity Check jobs at
regular intervals. You can start a Groom or Integrity Check job. You
can't start a Resource Tracking job. A Resource Tracking job runs
immediately after a Groom job.

### Move Blocks to a Different Blockstore

To move a backup job's blocks to a different blockstore:

1. Find the blockstore replica set you want to groom in the
   table.

2. Select a different destination blockstore in the backup job's
   Destination blockstore column.

3. In the Groom Action column, click Schedule.

You might want to do this if you add a new blockstore and would like to
balance data. This removes all dead blocks from the backup job. This
groom job is called an
inter-blockstore groom job.

### Groom a Blockstore

To initiate a groom job:

1. Find the blockstore replica set you want to groom in the
   table.

2. In the Groom Action column, click Schedule.

You should not need to manually schedule groom jobs. Ops Manager
runs the jobs automatically.

### Check Blockstore Integrity

To initiate an integrity check:

1. Find the blockstore replica set you want to groom in the
   table.

2. In Integrity Action column, click
   IntegCheck.

   Ops Manager displays the Integrity Schedule Result modal
   with the status of the blockstore.

**See also:**

/tutorial/configure-block-size.
