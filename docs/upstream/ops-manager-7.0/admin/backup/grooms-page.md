<!-- Converted from admin/backup/grooms-page.txt (reStructuredText). Includes are inlined. -->

# Grooms

This page lists active and recent groom jobs.

Groom jobs remove unused blocks in
`blockstores` and
`S3 blockstores` to reclaim storage
space.

If no existing snapshots reference a given
block, Ops Manager considers the block *unused* or *dead*. Ops Manager grooms
blockstores after the snapshot drops below the threshold of living
bytes. 

## How Groom Jobs Work

Groom job differ based on the snapshot store.

**Note:** File Size Changes during Grooming

During grooming operations, you may notice that the file sizes of
blockstores and S3-compatible storage snapshot stores fluctuate, sometimes
dramatically. This is normal during these operations.

### Intra-Blockstore Groom Job

An intra-blockstore groom job performs the following tasks:

1. Writes all new blocks for ongoing snapshots to a new *target*
   location on the blockstore.

2. Copies all existing living blocks from the *source* location to the
   new *target* location in the same blockstore.

   This means two copies of the living blocks exist on the blockstore
   at the same time. This impacts storage usage.

3. Updates references to maintain data relationships.

4. Drops the *source* database.

### Inter-Blockstore Groom Job

An inter-blockstore groom job performs the following tasks:

1. Writes all new blocks for ongoing snapshots to a different *target*
   blockstore.

2. Copies all existing living blocks from the *source* blockstore to
   the new *target* blockstore.

3. Updates references to maintain data relationships.

4. Drops the database from the *source* blockstore.

### File System Groom Job

A File System Groom Job deletes the database files from the file
system.

### S3 Groom Job

An S3-compatible storage blockstore groom job performs the following tasks:

1. Writes all new blocks for ongoing snapshots to temporary database

2. Sends a delete request for dead blocks in source database

3. Resumes writing new blocks for ongoing snapshots to source database

4. Copies over new blocks from the temporary database back to the
   source database.

## What Triggers a Groom Job

Ops Manager triggers groom jobs when:

- the percentage of living bytes drops below a given threshold and
- the number of dead bytes reaches a minimum value.

Ops Manager also runs groom jobs at the following minimum intervals:

| Blockstore Location | Minimum Groom Interval |
|---|---|
| S3 | One time every two weeks |
| MongoDB | One time per year |

When grooming, Ops Manager removes all the dead bytes.

| Blockstore Type | Percentage of Living to Total Bytes | Minimum Number of Dead Bytes |
|---|---|---|
| S3 | 75% | 0 |
| MongoDB | 45% | 2 GB |

You can start a groom from the
Grooms Priority admin page.

**Note:**

Ops Manager limits a project's Tracking and Groom Jobs to the Backup
Daemons set in the project's Backup Configuration.
