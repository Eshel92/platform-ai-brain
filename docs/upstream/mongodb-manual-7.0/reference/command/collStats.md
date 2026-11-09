<!-- Converted from reference/command/collStats.txt (reStructuredText). Includes are inlined. -->

# collStats (database command)

 

## Definition

**`collStats`**

**Deprecated since version:** 6.2

In versions 6.2 and later use the `$collStats` aggregation 
stage.

The `collStats` command returns a variety of storage statistics
for a given collection.

   Specific fields in the `collStats` output can be accessed using the
   `dataSize`,
   `estimatedDocumentCount`,
   `isCapped`,
   `latencyStats`,
   `storageSize`,
   `totalIndexSize`, and
   `totalSize`
   helper methods

**Tip:**

In `mongosh`, this command can also be run through the `stats` helper method..

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

To run `collStats`, use the `db.runCommand( { <command> } )` method.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {
     collStats: <string>,
     scale: <int>
   }
)
```

### Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `collStats` | string | The name of the target collection. |
| `scale` | int | Optional. The scale factor for the various size data (with the exception of those sizes that specify the unit of measurement in the field name). The value defaults to 1 to return size data in bytes. To display kilobytes rather than bytes, specify a `scale` value of `1024`. If you specify a non-integer scale factor, MongoDB uses the integer part of the specified factor. For example, if you specify a scale factor of `1023.999`, MongoDB uses `1023` as the scale factor. The scale factor rounds the affected size values to whole numbers. |

## Behavior

### Redaction

When using Queryable Encryption,
`$collStats` output redacts certain information for encrypted
collections:

* The output omits `"queryExecStats"`
* The output omits `"latencyStats"`
* The output redacts `"WiredTiger"`, if present, to include only the `url` field.

### Scaled Sizes

Unless otherwise specified by the metric name (such as ``"bytes
currently in the cache"``), values related to size are displayed in
bytes and can be overridden by `scale`.

The scale factor rounds the affected size values to whole numbers.

### Accuracy after Unexpected Shutdown

After an unclean shutdown of a `mongod` using the Wired Tiger storage engine, size statistics reported by
`collStats` may be inaccurate.

The amount of drift depends on the number of insert, update, or delete
operations performed between the last checkpoint and the unclean shutdown. Checkpoints
usually occur every 60 seconds. However, `mongod` instances running
with non-default `--syncdelay` settings may have more or less frequent
checkpoints.

Run `validate` on each collection on the `mongod`
to restore statistics after an unclean shutdown.

After an unclean shutdown:

- `validate` updates the count statistic in the `collStats` output with the latest value.

- Other statistics like the number of documents inserted or removed in
  the `collStats` output are
  estimates.

### In-Progress Indexes

`collStats` includes information on indexes currently being built. For details, see:

- `collStats.nindexes`
- `collStats.indexDetails`
- `collStats.indexBuilds`
- `collStats.totalIndexSize`
- `collStats.indexSizes`

### Replica Set Member State Restriction

To run on a replica set member, `collStats` operations require the member 
to be in `PRIMARY` or `SECONDARY` state. If the member
is in another state, such as `STARTUP2`, the
operation errors.

### Non-Existent Collections

If you run `collStats` for a non-existent collection, the command
might return `0` values in the output fields instead of an error.
This behavior depends on your database implementation.

For an example of this behavior, see collStats-example.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following operation runs the `collStats` command on the
`movies` collection, specifying a scale of `1024` bytes:

```javascript
```

Output:

```javascript
```

The following operation runs the `collStats` command on a
non-existent collection:

```javascript
```

Output:

```javascript
```

## Output

The following document provides a representation of the
`collStats` output. Depending on the configuration of your
collection and the storage engine, the output fields may vary.

```javascript
{
  "ns" : <string>,
  "size" : <number>,
  "timeseries" : {
     "bucketsNs" : <bucketName>,
     "bucketCount" : <number>,
     "avgBucketSize" : <number>,
     "numBucketInserts" : <number>,
     "numBucketUpdates" : <number>,
     "numBucketsOpenedDueToMetadata" : <number>,
     "numBucketsClosedDueToCount" : <number>,
     "numBucketsClosedDueToSize" : <number>,
     "numBucketsClosedDueToTimeForward" : <number>,
     "numBucketsClosedDueToTimeBackward" : <number>,
     "numBucketsClosedDueToMemoryThreshold" : <number>,
     "numCommits" : <number>,
     "numWaits" : <number>,
     "numMeasurementsCommitted" : <number>,
     "avgNumMeasurementsPerCommit": <number>
  },
  "count" : <number>,
  "avgObjSize" : <number>,
  "numOrphanDocs" : <number>,      // Available starting in MongoDB 6.0
  "storageSize" : <number>,
  "freeStorageSize" : <number>,
  "capped" : <boolean>,
  "max" : <number>,
  "maxSize" :  <number>,
  "wiredTiger" : {
     "metadata" : {
        "formatVersion" : <num>
     },
     "creationString" : <string>
     "type" :  <string>,
     "uri" :  <string>,
     "LSM" : {
        "bloom filter false positives" : <number>,
        "bloom filter hits" : <number>,
        "bloom filter misses" : <number>,
        "bloom filter pages evicted from cache" : <number>,
        "bloom filter pages read into cache" : <number>,
        "bloom filters in the LSM tree" : <number>,
        "total size of bloom filters" : <number>,
        "chunks in the LSM tree" : <number>,
        "highest merge generation in the LSM tree" : <number>,
        "queries that could have benefited from a Bloom filter that did not exist" : <number>,
        "sleep for LSM checkpoint throttle" : <number>,
        "sleep for LSM merge throttle" : <number>
        "total size of bloom filters" : <number>
     },
     "block-manager" : {
         "allocations requiring file extension" : <number>,
         "blocks allocated" : <number>,
         "blocks freed" : <number>,
         "checkpoint size" : <number>,
         "file allocation unit size" : <number>,
         "file bytes available for reuse" : <number>,
         "file magic number" : <number>,
         "file major version number" : <number>,
         "file size in bytes" : <number>,
         "minor version number" : <number>
     },
     "btree" : {
         "btree checkpoint generation" : <number>,
         "column-store fixed-size leaf pages" : <number>,
         "column-store internal pages" : <number>,
         "column-store variable-size RLE encoded values" : <number>,
         "column-store variable-size deleted values" : <number>,
         "column-store variable-size leaf pages" : <number>,
         "fixed-record size" : <number>,
         "maximum internal page key size" : <number>,
         "maximum internal page size" : <number>,
         "maximum leaf page key size" : <number>,
         "maximum leaf page size" : <number>,
         "maximum leaf page value size" : <number>,
         "maximum tree depth" : <number>,
         "number of key/value pairs" : <number>,
         "overflow pages" : <number>,
         "pages rewritten by compaction" : <number>,
         "row-store empty values" : <number>,
         "row-store internal pages" : <number>,
         "row-store leaf pages" : <number>
     },
     "cache" : {
        "bytes currently in the cache" : <number>,
        "bytes dirty in the cache cumulative" : <number>,
        "bytes read into cache" : <number>,
        "bytes written from cache" : <number>,
        "checkpoint blocked page eviction" : <number>,
        "data source pages selected for eviction unable to be evicted" : <number>,
        "eviction walk passes of a file" : <number>,
        "eviction walk target pages histogram - 0-9" : <number>,
        "eviction walk target pages histogram - 10-31" : <number>,
        "eviction walk target pages histogram - 128 and higher" : <number>,
        "eviction walk target pages histogram - 32-63" : <number>,
        "eviction walk target pages histogram - 64-128" : <number>,
        "eviction walks abandoned" : <number>,
        "eviction walks gave up because they restarted their walk twice" : <number>,
        "eviction walks gave up because they saw too many pages and found no candidates" : <number>,
        "eviction walks gave up because they saw too many pages and found too few candidates" : <number>,
        "eviction walks reached end of tree" : <number>,
        "eviction walks started from root of tree" : <number>,
        "eviction walks started from saved location in tree" : <number>,
        "hazard pointer blocked page eviction" : <number>,
        "in-memory page passed criteria to be split" : <number>,
        "in-memory page splits" : <number>,
        "internal pages evicted" : <number>,
        "internal pages split during eviction" : <number>,
        "leaf pages split during eviction" : <number>,
        "modified pages evicted" : <number>,
        "overflow pages read into cache" : <number>,
        "page split during eviction deepened the tree" : <number>,
        "page written requiring cache overflow records" : <number>,
        "pages read into cache" : <number>,
        "pages read into cache after truncate" : <number>,
        "pages read into cache after truncate in prepare state" : <number>,
        "pages read into cache requiring cache overflow entries" : <number>,
        "pages requested from the cache" : <number>,
        "pages seen by eviction walk" : <number>,
        "pages written from cache" : <number>,
        "pages written requiring in-memory restoration" : <number>,
        "tracked dirty bytes in the cache" : <number>,
        "unmodified pages evicted" : <number>
     },
     "cache_walk" : {
        "Average difference between current eviction generation when the page was last considered" : <number>,
        "Average on-disk page image size seen" : <number>,
        "Average time in cache for pages that have been visited by the eviction server" : <number>,
        "Average time in cache for pages that have not been visited by the eviction server" : <number>,
        "Clean pages currently in cache" : <number>,
        "Current eviction generation" : <number>,
        "Dirty pages currently in cache" : <number>,
        "Entries in the root page" : <number>,
        "Internal pages currently in cache" : <number>,
        "Leaf pages currently in cache" : <number>,
        "Maximum difference between current eviction generation when the page was last considered" : <number>,
        "Maximum page size seen" : <number>,
        "Minimum on-disk page image size seen" : <number>,
        "Number of pages never visited by eviction server" : <number>,
        "On-disk page image sizes smaller than a single allocation unit" : <number>,
        "Pages created in memory and never written" : <number>,
        "Pages currently queued for eviction" : <number>,
        "Pages that could not be queued for eviction" : <number>,
        "Refs skipped during cache traversal" : <number>,
        "Size of the root page" : <number>,
        "Total number of pages currently in cache" : <number>
     },
     "compression" : {
        "compressed page maximum internal page size prior to compression" : <number>,
        "compressed page maximum leaf page size prior to compression " : <number>,
        "compressed pages read" : <number>,
        "compressed pages written" : <number>,
        "page written failed to compress" : <number>,
        "page written was too small to compress" : 1
     },
     "cursor" : {
        "bulk loaded cursor insert calls" : <number>,
        "cache cursors reuse count" : <number>,
        "close calls that result in cache" : <number>,
        "create calls" : <number>,
        "insert calls" : <number>,
        "insert key and value bytes" : <number>,
        "modify" : <number>,
        "modify key and value bytes affected" : <number>,
        "modify value bytes modified" : <number>,
        "next calls" : <number>,
        "open cursor count" : <number>,
        "operation restarted" : <number>,
        "prev calls" : <number>,
        "remove calls" : <number>,
        "remove key bytes removed" : <number>,
        "reserve calls" : <number>,
        "reset calls" : <number>,
        "search calls" : <number>,
        "search near calls" : <number>,
        "truncate calls" : <number>,
        "update calls" : <number>,
        "update key and value bytes" : <number>,
        "update value size change" : <num>
     },
     "reconciliation" : {
        "dictionary matches" : <number>,
        "fast-path pages deleted" : <number>,
        "internal page key bytes discarded using suffix compression" : <number>,
        "internal page multi-block writes" : <number>,
        "internal-page overflow keys" : <number>,
        "leaf page key bytes discarded using prefix compression" : <number>,
        "leaf page multi-block writes" : <number>,
        "leaf-page overflow keys" : <number>,
        "maximum blocks required for a page" : <number>,
        "overflow values written" : <number>,
        "page checksum matches" : <number>,
        "page reconciliation calls" : <number>,
        "page reconciliation calls for eviction" : <number>,
        "pages deleted" : <number>
     },
     "session" : {
        "object compaction" : <number>,
     },
     "transaction" : {
        "update conflicts" : <number>
     }
  },
  "nindexes" : <number>,
  "indexDetails" : {
     "_id_" : {
        "metadata" : {
           "formatVersion" : <number>
        },
        ...
     },
     ...
  },
  "indexBuilds" : [
     <string>,
  ],
  "totalIndexSize" : <number>,
  "totalSize" : <number>, 
  "indexSizes" : {
          "_id_" : <number>,
          "<indexName>" : <number>,
          ...
  },
  "scaleFactor" : <number>
  "ok" : <number>
}
```

**`collStats.ns`**

The namespace of the current collection, which follows the format
`[database].[collection]`.

**`collStats.size`**

The total uncompressed size in memory of all records in a
collection. The `size` does not
include the size of any indexes associated with the collection,
which the `totalIndexSize` field reports.

The `scale` argument affects this value. Data compression does not
affect this value.

**`collStats.timeseries`**

`timeseries` appears when you run the
`collStats` command on a time series collection.

This document contains data for internal diagnostic use.

**`collStats.count`**

The number of objects or documents in this collection.

**`collStats.avgObjSize`**

The average size of an object in the collection. The `scale`
argument does not affect this value.

**`collStats.numOrphanDocs`**

The number of orphaned documents in the 
collection.

**New in version:** 6.0

**`collStats.storageSize`**

The total amount of storage allocated to this collection for
document storage. The `scale` argument affects this
value.

If collection data is compressed (which is the `default for
WiredTiger`), the
storage size reflects the compressed size and may be smaller than
the value for `collStats.size`.

`storageSize` does not include index size. See
`totalIndexSize` for index sizing.

**`collStats.freeStorageSize`**

*Unavailable for the In-Memory Storage Engine*

The amount of storage available for reuse. The `scale` argument
affects this value.

The field is only available if storage is available for reuse (i.e.
greater than zero).

**`collStats.nindexes`**

The number of indexes on the collection. All collections have at
least one index on the _id field.

`nindexes` includes indexes currently being built in
its count.

**`collStats.indexDetails`**

A document that reports data from the WiredTiger
storage engine for each index in the collection. Other storage engines will
return an empty document.

The fields in this document are the names of the indexes, while the
values themselves are documents that contain statistics for the
index provided by the storage engine. These statistics are for
internal diagnostic use.

`indexDetails` contains
details on indexes currently being built, including
warnings and errors.

**`collStats.indexBuilds`**

An array that contains the names of the indexes that are currently
being built on the collection. Once an index build completes, the
index does not appear in the `indexBuilds`.

**`collStats.totalIndexSize`**

Sum of the disk space used by all indexes. The `scale` argument 
affects this value.

If an index uses prefix compression (which is the `default
for WiredTiger`), the
returned size reflects the compressed size for any such indexes when
calculating the total.

`totalIndexSize` includes indexes currently being
built in the total size.

**`collStats.totalSize`**

The sum of the `storageSize` and
`totalIndexSize`. The `scale` argument affects
this value.

**`collStats.indexSizes`**

This field specifies the key and size of every existing index on
the collection. The `scale` argument affects this value.

If an index uses prefix compression (which is the `default
for WiredTiger`), the
returned size reflects the compressed size.

`indexSizes` includes the sizes of indexes currently being built.

**`collStats.scaleFactor`**

The `scale` value used by the command.

If you had specified a non-integer scale factor, MongoDB uses the
integer part of the specified factor. For example, if you specify a
scale factor of `1023.999`, MongoDB uses `1023` as the scale
factor.

**`collStats.capped`**

This field will be "true" if the collection is
capped.

**`collStats.max`**

Shows the maximum number of documents that may be present in a
capped collection.

**`collStats.maxSize`**

Shows the maximum size of a capped collection.

**`collStats.wiredTiger`**

`wiredTiger` only appears when using the
WiredTiger storage engine. When using Queryable Encryption, WiredTiger data is redacted to only the `url` field.

This document contains data reported
directly by the WiredTiger engine and other data for internal
diagnostic use.

**`collStats.inMemory`**

`inMemory` only appears when using the in-memory
storage engine.

This document contains data reported
directly by the storage engine and other data for internal
diagnostic use.
