<!-- Converted from core/read-preference-hedge-option.txt (reStructuredText). Includes are inlined. -->

# Hedged Read Option

You can specify the use of hedged reads for 
non-`primary` read preferences on sharded 
clusters.

With hedged reads, the `mongos` instances can route read
operations to two replica set members per each queried shard and return
results from the first respondent per shard.

Hedged reads are supported for the following operations:

- `collStats`
- `count`
- `dataSize`
- `dbStats`
- `distinct`
- `filemd5`
- `find`
- `listCollections`
- `listIndexes`
- `planCacheListFilters`

To specify hedged read for a read preference, use the hedged read option for 
read preferences.

## Enable Hedged Reads

To use hedged reads, enable the hedge read option for non-`primary`
read preferences. Read preference `nearest` specifies hedged
read by default.

- When using the drivers, refer to the `drivers' read preference API`.

- When using `mongosh`, you can use the helper
  methods `cursor.readPref()` and `Mongo.setReadPref()`.

## Additional Information

For more information on hedged reads, see mongos-hedged-reads.

### Member Selection with Hedged Reads

For details on member selection for hedged reads, see
read-preference-mechanics-sharded-cluster.

### Hedged Reads Diagnostics

The command `serverStatus` and its corresponding
`mongosh` method `db.serverStatus()` return
`hedgingMetrics`.
