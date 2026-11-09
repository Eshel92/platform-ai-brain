<!-- Converted from admin/backup/snapshot-storage-page.txt (reStructuredText). Includes are inlined. -->

# Snapshot Storage

MongoDB database backups called *snapshots* and they are stored in
containers called *snapshot stores*. This page lists existing snapshot
stores and allows you to create or modify snapshot stores.

Ops Manager supports the following snapshot stores:

- On a File System,
- In a MongoDB database (`blockstore`), or
- In an S3 Bucket (S3 blockstore)

| Storage Method | Name | Description |
|---|---|---|
| File system | File system store | Snapshots are stored in a directory on a file system. Each snapshot is found in its own sub-directory. The snapshot files can be compressed individually based upon its `File System Store Gzip Compression Level`. To create or edit a file system store, see /tutorial/manage-filestore-storage. |
| Database storage | blockstore | Snapshots are stored in a managed MongoDB database in a compressed, de-duplicated format. Depending on data usage patterns the deduplication can provide significant storage savings without the need for any specialized hardware or other software. To create or edit a blockstore, see /tutorial/manage-blockstore-storage |
| S3-compatible storage bucket | S3-compatible storage blockstore | Snapshot data is stored as blocks in an AWS (Amazon Web Services) [S3](https://aws.amazon.com/s3/) bucket. Snapshot metadata is stored in a managed MongoDB database. The metadata database tracks which blocks comprise each snapshot. The blocks are compressed and de-duplicated. To create or edit an S3 blockstore, see /tutorial/manage-s3-blockstore-storage |

You can add, edit or delete any snapshot store listed.

## Additional Information

For additional information on managing snapshots, see:

- /tutorial/manage-blockstore-storage

- /tutorial/manage-s3-blockstore-storage

- /tutorial/manage-filestore-storage

- /tutorial/assign-snapshot-stores-to-data-center

- /tutorial/configure-block-size

- groom-priority-page, to manually direct Ops Manager to move
  blocks between blockstores
