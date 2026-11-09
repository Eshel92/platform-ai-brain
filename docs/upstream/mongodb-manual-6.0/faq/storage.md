<!-- Converted from faq/storage.txt (reStructuredText). Includes are inlined. -->

# FAQ: MongoDB Storage for Self-Managed Deployments

This document addresses common questions regarding MongoDB's storage
system.

## Storage Engine Fundamentals

### What is a storage engine?

A storage engine is the part of a database that is responsible for
managing how data is stored, both in memory and on disk. Many databases
support multiple storage engines, where different engines perform better
for specific workloads. For example, one storage engine might offer
better performance for read-heavy workloads, and another might support a
higher throughput for write operations.

**See also:**

/core/storage-engines

## Can you mix storage engines in a replica set?

Yes. You can have replica set members that use different storage
engines (WiredTiger and in-memory)

## Storage Recommendations

### How many collections and indexes can be in a cluster?

Cluster performance might degrade once the combined number of collections and indexes reaches beyond 100,000. In addition,
many large collections have a greater impact on performance than smaller collections.

## WiredTiger Storage Engine

### Can I upgrade an existing deployment to WiredTiger?

Yes. See:

- /tutorial/change-standalone-wiredtiger

- /tutorial/change-replica-set-wiredtiger

- /tutorial/change-sharded-cluster-wiredtiger

### How much compression does WiredTiger provide?

The ratio of compressed data to uncompressed data depends on your data
and the compression library used. By default, collection data in
WiredTiger use Snappy block compression; zlib
and zstd compression is also available. Index data use
prefix compression by default.

### To what size should I set the WiredTiger internal cache?

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

**Note:**

The `storage.wiredTiger.engineConfig.cacheSizeGB` limits the size of the WiredTiger internal
cache. The operating system uses the available free memory
for filesystem cache, which allows the compressed MongoDB data
files to stay in memory. In addition, the operating system 
uses any free RAM to buffer file system blocks and file system
cache.

To accommodate the additional consumers of RAM, you may have to
decrease WiredTiger internal cache size.

The default WiredTiger internal cache size value assumes that there is a
single `mongod` instance per machine. If a single machine
contains multiple MongoDB instances, then you should decrease the setting to
accommodate the other `mongod`
instances.

If you run `mongod` in a container (for example, `lxc`,
`cgroups`, Docker, etc.) that does *not* have access to all of the
RAM available in a system, you must set `storage.wiredTiger.engineConfig.cacheSizeGB` to a value
less than the amount of RAM available in the container. The exact
amount depends on the other processes running in the container. See
`memLimitMB`.

To view statistics on the cache and eviction rate, see the
`wiredTiger.cache` field
returned from the `serverStatus` command.

### How much memory does MongoDB allocate per connection?

Each connection uses up to 1 megabyte of RAM.

To optimize memory use for connections, ensure that you:

- Monitor the number of open connections to your deployment. Too many
  open connections result in excessive use of RAM and reduce available
  memory for the working set.
  
- Close connection pools when they are
  no longer needed. A connection pool is a cache of open, ready-to-use
  database connections maintained by the driver. Closing unneeded pools
  makes additional memory resources available.

- Manage the size of your connection pool. The `maxPoolSize`
  connection string option specifies the maximum number of open
  connections in the pool. By default, you can have up to 100 open
  connections in the pool. Lowering the `maxPoolSize` reduces the
  maximum amount of RAM used for connections.

  **Tip:**

  To configure your connection pool, see
  connection-pool-settings.

### How frequently does WiredTiger write to disk?

Checkpoints

   MongoDB configures WiredTiger to create checkpoints, specifically, writing 
   the snapshot data to disk at intervals of 60 seconds. 

Journal Data

   WiredTiger syncs the buffered journal records to disk upon any of
   the following conditions:

   - For replica set members (primary and secondary members):

     - If a write operation includes or implies a write concern of
       `j: true`.

     - Additionally for secondary members, after every batch
       application of the oplog entries.

     **Note:**

     Write concern `"majority"` implies `j: true` if
     the `writeConcernMajorityJournalDefault` is true.

   - At every 100 milliseconds (See `storage.journal.commitIntervalMs`).

   - When WiredTiger creates a new journal file. Because MongoDB uses a
     journal file size limit of 100 MB, WiredTiger creates a new
     journal file approximately every 100 MB of data.

### How do I reclaim disk space in WiredTiger?

The WiredTiger storage engine maintains lists of empty records in data
files as it deletes documents. This space can be reused by WiredTiger,
but will not be returned to the operating system unless under very
specific circumstances.

The amount of empty space available for reuse by WiredTiger is reflected
in the output of `db.collection.stats()` under the heading
`wiredTiger.block-manager.file bytes available for reuse`.

To allow the WiredTiger storage engine to release this empty space to the
operating system, you can de-fragment your data file. This can be achieved by 
resyncing a replica set member or using the 
`compact` command. 

## Data Storage Diagnostics

### How can I check the size of a collection?

To view the statistics for a collection, including the data size, use
the `db.collection.stats()` method from within
`mongosh`. The following example issues
`db.collection.stats()` for the `orders` collection:

```javascript
db.orders.stats();
```

MongoDB also provides the following methods to return specific sizes
for the collection:

- `db.collection.dataSize()` to return the uncompressed data
  size in bytes for the collection.

- `db.collection.storageSize()` to return the size in bytes of
  the collection on disk storage. If collection data is compressed
  (which is the `default for WiredTiger`), the storage size reflects
  the compressed size and may be smaller than the value returned by
  `db.collection.dataSize()`.

- `db.collection.totalIndexSize()` to return the index sizes in
  bytes for the collection. If an index uses prefix compression
  (which is the `default for WiredTiger`), the returned size reflects the
  compressed size.

The following script prints the statistics for each database:

```javascript
db.adminCommand("listDatabases").databases.forEach(function (d) {
   mdb = db.getSiblingDB(d.name);
   printjson(mdb.stats());
})
```

The following script prints the statistics for each collection in each
database:

```javascript
db.adminCommand("listDatabases").databases.forEach(function (d) {
   mdb = db.getSiblingDB(d.name);
   mdb.getCollectionNames().forEach(function(c) { 
      s = mdb[c].stats();
      printjson(s);
   })
})
```

### How can I check the size of the individual indexes for a collection?

To view the size of the data allocated for each index, use the
`db.collection.stats()` method and check the
`indexSizes` field in the returned document.

If an index uses prefix compression (which is the `default for
WiredTiger`), the returned
size for that index reflects the compressed size.

### How can I get information on the storage use of a database?

The `db.stats()` method in `mongosh` returns
the current state of the "active" database. For the description of the
returned fields, see dbStats Output.
