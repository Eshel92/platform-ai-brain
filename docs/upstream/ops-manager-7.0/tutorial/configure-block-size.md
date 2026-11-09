<!-- Converted from tutorial/configure-block-size.txt (reStructuredText). Includes are inlined. -->

# Configure Block Size in a Blockstore

Blockstore-based backup performs differently depending on the FCV of the blockstore.

**fcv42:**

When you back up your deployment to a blockstore, the following
actions occur:

1. The MongoDB Agent sends copies of files broken into blocks.
2. The Backup Service writes these blocks to the blockstore.

**fcv40:**

For backup jobs with FCV 4.0 or earlier, the
`Backup Daemon` performs the following actions:

1. Takes a snapshot of the `head database`
#. Breaks this snapshot into blocks
#. Writes these blocks to the blockstore

The different blockstores have different default sizes and ranges of
sizes for blocks.

**fcv42:**

| Blockstore Type | Block Size Range | Default Size |
|---|---|---|
| MongoDB | 64 KB to 15 MB | 1 MB |
| S3 | 64 KB to 16 MB | 16 MB |

For backups with FCV 4.2 or later, Ops Manager changed the default
MongoDB blockstore block size from 64 KB to 1 MB. This change
improves snapshot performance.

If your blockstores include backups with files larger than 100
GB, consider using a block size of 2 MB or greater. If you need
help choosing a block size, contact
[MongoDB Support](https://support.mongodb.com/welcome).

**fcv40:**

| Blockstore Type | Block Size Range | Default Size |
|---|---|---|
| MongoDB | 64 KB to 15 MB | 64 KB |
| S3 | 64 KB to 16 MB | 16 MB |

## Considerations

### Full Snapshot after Change to Block Size

If you change the block size, the next snapshot runs as a full snapshot
rather than an incremental snapshot.

### Increased Block Size Increases Performance and Disk Usage

In general, increasing block size results in faster snapshots and
restores, but requires more disk space. Consider these competing
factors when determining if you should tune the block size.

In these two exceptions performance improves as the block size
increases *without* requiring additional disk space:

| Workload | Impact |
|---|---|
| Update- and Delete-Intensive | No matter how small you make the block size, the entire block file is rewritten. Since the entire file is always rewritten, storage space doesn't change if you change the block size. |
| Insert-only | The existing blocks never change. Block management simplifies as you increase block size. This enables the best possible performance on snapshot and restore. |

### Check Disk Capacity Before Changing Block Size

Before changing the block size, check that your MongoDB blockstore can
fit in the current disk space after the change. Snapshots after the
change can't deduplicate blocks of earlier snapshots. The block sizes
won't match. This results in each blockstore’s disk usage increasing by
the size of the deployments they back up.

Blockstores that can't store new blocks crash. This blocks backups.
Clear space from disk to return the blockstore to working order.

To check if you have enough disk space to change the block size for a
given job, complete the following procedure:

1. Discover the amount of available disk space on the host running the
   blockstore.

2. Estimate the amount by which the blockstore storage usage increases
   when it adds the compressed bytes of the next snapshot. Review the
   compressed bytes of the backup job’s most recent snapshot to make
   that estimate.

   To review the compressed bytes, run the following query:

   ```javascript
   db.getSiblingDB("backupjobs").snapshots.findOne(
     {
       rsId : <rsId>,
       groupId : <groupId>,
       completed: true
     }, {
       compressedSize: 1
     }, {
       sort: {
         startTime: -1
       }
     }
   )
   ```

3. Scale up the value you found to leave some buffer room.

   a. The blockstore storage usage spikes with the first snapshot taken
      after increasing block size. Subsequent snapshots with that new
      block size also grow the blockstore. Not all of their blocks
      deduplicate with that first snapshot.

   b. If Ops Manager reclaims space using one blockstore (an intra-blockstore
      groom job), the blockstore needs a greater amount of buffer
      space. During an intra-blockstore groom job, the blockstore
      allocates space temporarily for the following:

      - the dead bytes from previously expired snapshots
      - two copies of the living bytes of all previously completed
        snapshots
      - two copies of the bytes from the new snapshot

4. Compare the disk space found in step 1 and step 3. The disk space
   calculated in step 3 should fit in the disk space found in step 1.

If your host lacks sufficient disk space to change the block size for a
given job, try one of the following solutions:

- Add more disk space for the blockstores.

- Terminate and restart backup jobs. This purges all existing
  snapshots.

- Run one or more groom jobs from the
  Grooms Priority admin page to clear
  some dead bytes. To see how much data you can actually clean for
  each job, check the
  Resource Usage admin page.

- Add a new blockstore then
  schedule inter-blockstore groom job
  for some of the backup jobs.

- Leave block size unchanged.

  Ops Manager displays the banner to increase block size if you never
  configured block size for one or more backups with FCV 4.2 or
  later and a MongoDB blockstore. To dismiss the banner, set any block
  size for all backup jobs. You can set the old default block size of
  64 KB.

If you need help, contact [MongoDB Support](https://support.mongodb.com/welcome)

**Note:**

Blockstore storage usage spikes and increases gradually after
changing block size. This usage reduces as snapshots taken with the
old block size expire. As Ops Manager keeps monthly snapshots for between
one and seven years, this usage could take a long time before
returning to pre-block-size-change levels.

## Procedure

**Step 1: Navigate to the Backup Jobs page.**

a. Click the Admin link.
b. Click Backup.
c. Click Jobs.

**Step 2: Click on the name of the replica set that you wish to edit.**

**Step 3: Click the Update Size link for Blockstore Minimum Block Size.**

**Step 4: Select the desired minimum block size from the drop-down menu.**

The range of minimum block sizes include:

- 64 KB
- 128 KB
- 256 KB
- 512 KB
- 1 MB
- 2 MB
- 4 MB
- 8 MB
- 15 MB (MongoDB) or 16 MB (S3)

**Note:**

The updated minimum block size only applies to new and updated
files in future snapshots. Existing blocks are not resized.

**Step 5: Click Update.**
