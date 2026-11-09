<!-- Converted from reference/command/dbStats.txt (reStructuredText). Includes are inlined. -->

# dbStats

## Definition

**`dbStats`**

The `dbStats` command returns storage statistics for a
given database. 

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command has limited support in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

   

## Syntax

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     dbStats: 1, 
     scale: <number>,
     freeStorage: 0
   } 
)
```

## Command Fields

The command takes the following fields:

| Fields | Description |
|---|---|
| `dbStats` | 1 |
| scale | .. _dbStats-scale: Optional. The scale factor for the various size data. The `scale` defaults to 1 to return size data in bytes. To display kilobytes rather than bytes, specify a `scale` value of `1024`. If you specify a non-integer scale factor, MongoDB uses the integer part of the specified factor. For example, if you specify a scale factor of `1023.999`, MongoDB uses `1023` as the scale factor. Starting in version 4.2, the output includes the `scaleFactor` used to scale the size values. |
| freeStorage | .. _dbStats-freeStorage: Optional. To return details on free space allocated to collections, set `freeStorage` to 1. If the instance has a large number of collections or indexes, obtaining free space usage data may cause processing delays. To gather `dbStats` information without free space details, either set `freeStorage` to 0 or do not include the field. |

 
In `mongosh`, the `db.stats()` function
provides a wrapper around `dbStats`.

## Behavior

The time required to run the command depends on the total size of the
database. Because the command must touch all data files, the command
may take several seconds to run.

### Accuracy after Unexpected Shutdown

After an unclean shutdown of a `mongod` using the Wired Tiger storage engine, count and size statistics reported by
`dbStats` may be inaccurate.

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

### Replica Set Member State Restriction

To run on a replica set member, `dbStats` operations require the member 
to be in `PRIMARY` or `SECONDARY` state. If the member
is in another state, such as `STARTUP2`, the
operation errors.

## Output

**`dbStats.db`**

Name of the database.

**`dbStats.collections`**

Number of collections in the database.

**`dbStats.views`**

Number of views in the database.

**`dbStats.objects`**

Number of objects (specifically, documents) in the
database across all collections.

**`dbStats.avgObjSize`**

Average size of each document in bytes. This is the
`dataSize` divided by the number of documents. The
scale argument does not affect the
`avgObjSize` value.

**`dbStats.dataSize`**

Total size of the uncompressed data held in the database. The
`dataSize` decreases when you remove documents.

For databases using the WiredTiger storage engine, `dataSize` may be
larger than `storageSize` if compression is enabled. The
`dataSize` decreases when documents shrink.

**`dbStats.storageSize`**

Sum of the space allocated to all collections in the database for
document storage, including free space.

The `storageSize` does not decrease as you remove or
shrink documents. This value may be smaller than
`dataSize` for databases using the WiredTiger storage
engine with compression
enabled.

`storageSize` does not include space allocated to
indexes. See `indexSize` for the total index size.

**`dbStats.freeStorageSize`**

Sum of the free space allocated to all collections in the database
for document storage. Free database storage space is
allocated to the collection but does not contain data.

`freeStorageSize` does not include free space
allocated to indexes. See `indexFreeStorageSize` for
the total free index size.

To include this value in the `dbStats` output, set
freeStorage to 1.

*Updated in version 5.3.0, 5.2.1, and 5.0.6*

**`dbStats.indexes`**

Total number of indexes across all collections in the database.

**`dbStats.indexSize`**

Sum of the space allocated to all indexes in the database, including
free index space.

**`dbStats.indexFreeStorageSize`**

Sum of the free space allocated to all indexes in the database. Free
database storage space is allocated to the index but does not contain
data.

`indexFreeStorageSize` does not include free space
allocated to document storage. See `freeStorageSize`
for the total free document storage size.

`indexFreeStorageSize` does not include in-progress 
index builds.

To include this value in the `dbStats` output, set
freeStorage to 1.

*Updated in version 7.0, 6.3.2, 6.0.7, 5.3.0, 5.2.1, 5.0.19, and 5.0.6*

**`dbStats.totalSize`**

Sum of the space allocated for both documents and indexes in all
collections in the database. Includes used and free storage space.
This is the sum of `storageSize` and
`indexSize`.

**`dbStats.totalFreeStorageSize`**

Sum of the free storage space allocated for both documents and
indexes in all collections in the database. This is the sum of
`freeStorageSize` and
`indexFreeStorageSize`.

To include this value in the `dbStats` output, set
freeStorage to 1.

*Updated in version 5.3.0, 5.2.1, and 5.0.6.*

**`dbStats.scaleFactor`**

`scale` value used by the command.

If you specified a non-integer scale factor, MongoDB uses the
integer part of the specified factor. For example, if you specify a
scale factor of `1023.999`, MongoDB uses `1023` as the scale
factor.

**`dbStats.fsUsedSize`**

Total size of all disk space in use on the filesystem where MongoDB
stores data.

**See also:**

`--dbpath`

**`dbStats.fsTotalSize`**

Total size of all disk capacity on the filesystem where MongoDB
stores data.

## Examples

The following examples demonstrate `dbStats` usage.

### Limit Data Returned

To limit the data returned to a single field, append the field name to
the `dbStats` command. This example returns the
`indexSize` value:

```javascript
db.runCommand( { dbStats: 1 } ).indexSize
```

### View Free Space Allocated to Collections

To view free storage usage, set freeStorage to 1. 

```javascript
db.runCommand( { dbStats: 1, scale: 1024, freeStorage: 1 } )
```

Example output:

```javascript
{
  db: 'test',
  collections: 2,
  views: 0,
  objects: 1689,
  avgObjSize: 52.56542332741267,
  dataSize: 86.7021484375,
  storageSize: 100,
  freeStorageSize: 32,
  indexes: 2,
  indexSize: 116,
  indexFreeStorageSize: 36,
  totalSize: 216,
  totalFreeStorageSize: 68,
  scaleFactor: 1024,
  fsUsedSize: 60155820,
  fsTotalSize: 61255492,
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1646085664, i: 1 }),
    signature: {
      hash: Binary(Buffer.from("0000000000000000000000000000000000000000", "hex"), 0),
      keyId: Long("0")
    }
  },
  operationTime: Timestamp({ t: 1646085664, i: 1 })
}
```

The freeStorage field enables
the collection and display of the highlighted metrics.

The scale field sets the displayed values to
kilobytes.
