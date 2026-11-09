<!-- Converted from reference/method/db.stats.txt (reStructuredText). Includes are inlined. -->

# db.stats() (mongosh method)

## Description

**`db.stats(scale)`**

Returns statistics that reflect the use state of a single database.

The `db.stats()` method is a wrapper around the
`dbStats` database command. 

## Compatibility

This method is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command has limited support in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Parameters

The `db.stats()` method has the following optional parameters:

| Parameter | Type | Description |
|---|---|---|
| scale | number | .. _db.stats-scale: Optional. The scale factor for the various size data. The `scale` defaults to 1 to return size data in bytes. To display kilobytes rather than bytes, specify a `scale` value of `1024`. If you specify a non-integer scale factor, MongoDB uses the integer part of the specified factor. For example, if you specify a scale factor of `1023.999`, MongoDB uses `1023` as the scale factor. Starting in version 4.2, the output includes the `scaleFactor` used to scale the size values. |
| freeStorage | number | .. _db.stats-freeStorage: Optional. To return information on free space allocated to collections, set `freeStorage` to 1. If the instance has a large number of collections or indexes, obtaining free space usage data may cause processing delays. To gather `db.stats()` data without free space details, either set `freeStorage` to 0 or do not include the parameter. |

## Output

The `db.stats()` method returns a document with
statistics about the database system's state. A complete listing,
including freeStorage details, resembles
the following:

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

For an explanation of the output, see dbstats-output.

## Behavior

### Accuracy after Unexpected Shutdown

After an unclean shutdown of a `mongod` using the Wired Tiger storage engine, count and size statistics reported by
`db.stats` may be inaccurate.

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

## Examples

### Scale Output Values

To return values in kilobytes, set the scale
to `1024`:

```javascript
db.stats(1024)
```

**Note:**

The scale factor rounds values to whole numbers.

### Return a Single Value

To return a single value, such as `indexSize`, append
the field name to `db.stats()`.

```javascript
db.stats().indexSize
db.stats(1024).indexSize
```

The output shows the difference between the original and scaled values.

```javascript
118784
116
```

### Return Information on Free Space Allocated to Collections

To return information on free space allocated to collections, pass the
freeStorage parameter to `db.stats()`.

The following example returns the `indexFreeStorageSize`
in kilobytes:

```
db.stats( { freeStorage: 1, scale: 1024 } ).indexFreeStorageSize
```
