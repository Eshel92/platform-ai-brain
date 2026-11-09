<!-- Converted from core/wiredtiger.txt (reStructuredText). Includes are inlined. -->

# WiredTiger Storage Engine

The WiredTiger storage engine is the default storage engine. For existing 
deployments, if you do not specify the `--storageEngine` or the 
`storage.engine` setting, the `mongod` instance can 
automatically determine the storage engine used to create the data files in the 
`--dbpath` or `storage.dbPath`. 

Deployments hosted in the following environments can use the WiredTiger
storage engine:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

All MongoDB Atlas deployments use the WiredTiger storage engine.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

To learn more about WiredTiger memory use for deployments hosted in MongoDB
Atlas, see Memory.

## Operation and Limitations

The following operational notes and limitations apply to the WiredTiger
engine:

- You can't pin documents to the WiredTiger cache.
- WiredTiger doesn't reserve a portion of the cache for reads and 
  another for writes.
- A heavy write workload can affect performance, but WiredTiger
  prioritizes index caching in such cases.
- WiredTiger allocates its cache to the entire `mongod`
  instance. 
  WiredTiger doesn't allocate cache on a per-database or per-collection
  level.

## Document Level Concurrency

WiredTiger uses *document-level* concurrency control for write
operations. As a result, multiple clients can modify different
documents of a collection at the same time.

For most read and write operations, WiredTiger uses optimistic
concurrency control. WiredTiger uses only intent locks at the global,
database and collection levels. When the storage engine detects
conflicts between two operations, one will incur a write conflict
causing MongoDB to transparently retry that operation.

Some global operations, typically short lived operations involving
multiple databases, still require a global "instance-wide" lock.
Some other operations, such as `renameCollection`, still 
require an exclusive database lock in certain circumstances.

## Snapshots and Checkpoints

WiredTiger uses MultiVersion Concurrency Control (MVCC). At the start
of an operation, WiredTiger provides a point-in-time snapshot of the
data to the operation. A snapshot presents a consistent view of the
in-memory data.

When writing to disk, WiredTiger writes all the data in a snapshot to
disk in a consistent way across all data files. The now-durable
data act as a *checkpoint* in the data files. The *checkpoint* ensures
that the data files are consistent up to and including the last
checkpoint; i.e. checkpoints can act as recovery points.

MongoDB configures WiredTiger to create checkpoints, specifically, writing 
the snapshot data to disk at intervals of 60 seconds. 

During the write of a new checkpoint, the previous checkpoint is still
valid. As such, even if MongoDB terminates or encounters an error while
writing a new checkpoint, upon restart, MongoDB can recover from the
last valid checkpoint.

The new checkpoint becomes accessible and permanent when WiredTiger's
metadata table is atomically updated to reference the new checkpoint.
Once the new checkpoint is accessible, WiredTiger frees pages from the
old checkpoints.

Using WiredTiger, even without journaling, MongoDB can recover from the last
checkpoint; however, to recover changes made after the last checkpoint,
run with journaling.

**Note:**

You cannot specify `--nojournal` option or `storage.journal.enabled: false` 
for replica set members that use the WiredTiger storage engine.

### Snapshot History Retention

Starting in MongoDB 5.0, you can use the
`minSnapshotHistoryWindowInSeconds` parameter to specify how
long WiredTiger keeps the snapshot history.

Increasing the value of `minSnapshotHistoryWindowInSeconds`
increases disk usage because the server must maintain the history of
older modified values within the specified time window. The amount of
disk space used depends on your workload, with higher volume workloads
requiring more disk space.

MongoDB maintains the snapshot history in the `WiredTigerHS.wt` file,
located in your specified `dbPath`.

## Journal

WiredTiger uses a write-ahead log (i.e. journal) in combination with
checkpoints to ensure data
durability.

The WiredTiger journal persists all data modifications between
checkpoints. If MongoDB exits between checkpoints, it uses the journal
to replay all data modified since the last checkpoint. For information
on the frequency with which MongoDB writes the journal data to disk,
see journal-process.

WiredTiger journal is compressed using the snappy compression
library. To specify a different compression algorithm or no
compression, use the
`storage.wiredTiger.engineConfig.journalCompressor` setting.
For details on changing the journal compressor, see
manage-journaling-change-wt-journal-compressor.

**Note:**

If a log record is less than or equal to 128 bytes, which is the minimum
log record size for WiredTiger,
WiredTiger does not compress that record.

You can disable journaling for standalone instances by setting
`storage.journal.enabled` to `false`, which can reduce the
overhead of maintaining the journal. For standalone instances,
not using the journal means that, when MongoDB exits unexpectedly, you
will lose all data modifications after the last checkpoint.

**Note:**

You cannot specify `--nojournal` option or `storage.journal.enabled: false` 
for replica set members that use the WiredTiger storage engine.

**See also:**

Journaling with WiredTiger

## Compression

With WiredTiger, MongoDB supports compression for all collections and
indexes. Compression minimizes storage use at the expense of additional
CPU.

By default, WiredTiger uses block compression with the snappy
compression library for all collections and prefix compression
for all indexes.

For collections, the following block compression libraries are also available:

- zlib 

- zstd 

To specify an alternate compression algorithm or no compression, use
the `storage.wiredTiger.collectionConfig.blockCompressor`
setting.

For indexes, to disable prefix compression, use the
`storage.wiredTiger.indexConfig.prefixCompression` setting.

Compression settings are also configurable on a per-collection and
per-index basis during collection and index creation. See
create-collection-storage-engine-options and
db.collection.createIndex() storageEngine option.

For most workloads, the default compression settings balance storage
efficiency and processing requirements.

The WiredTiger journal is also compressed by default. For information
on journal compression, see storage-wiredtiger-journal.

## Memory Use

With WiredTiger, MongoDB utilizes both the WiredTiger internal cache
and the filesystem cache.

The default WiredTiger internal cache size is the larger of either:

- 50% of (RAM - 1 GB), or

- 256 MB.

For example, on a system with a total of 4GB of RAM the
WiredTiger cache uses 1.5GB of RAM (``0.5 * (4 GB - 1 GB) =
1.5 GB``). Conversely, on a system with a total of 1.25 GB of
RAM WiredTiger allocates 256 MB to the WiredTiger cache
because that is more than half of the total RAM minus one
gigabyte (`0.5 * (1.25 GB - 1 GB) = 128 MB < 256 MB`).

**Note:**

In some instances, such as when running in a container, the database
can have memory constraints that are lower than the total system
memory. In such instances, this memory limit, rather than the total
system memory, is used as the maximum RAM available.

To see the memory limit, see `hostInfo.system.memLimitMB`.

By default, WiredTiger uses Snappy block compression for all collections
and prefix compression for all indexes. Compression defaults are configurable
at a global level and can also be set on a per-collection and per-index
basis during collection and index creation.

Different representations are used for data in the WiredTiger internal cache
versus the on-disk format:

- Data in the filesystem cache is the same as the on-disk format, including
  benefits of any compression for data files. The filesystem cache is used
  by the operating system to reduce disk I/O.
- Indexes loaded in the WiredTiger internal cache have a different data
  representation to the on-disk format, but can still take advantage of
  index prefix compression to reduce RAM usage. Index prefix compression
  deduplicates common prefixes from indexed fields.
- Collection data in the WiredTiger internal cache is uncompressed
  and uses a different representation from the on-disk format. Block
  compression can provide significant on-disk storage savings, but
  data must be uncompressed to be manipulated by the server.

With the filesystem cache, MongoDB automatically uses all free memory
that is not used by the WiredTiger cache or by other processes.

To adjust the size of the WiredTiger internal cache, see
`storage.wiredTiger.engineConfig.cacheSizeGB` and
`--wiredTigerCacheSizeGB`. Avoid increasing the WiredTiger
internal cache size above its default value.
