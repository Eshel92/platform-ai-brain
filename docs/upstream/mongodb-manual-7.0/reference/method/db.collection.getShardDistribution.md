<!-- Converted from reference/method/db.collection.getShardDistribution.txt (reStructuredText). Includes are inlined. -->

# db.collection.getShardDistribution() (mongosh method)

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Definition

**`db.collection.getShardDistribution()`**

Prints the data distribution statistics for a sharded collection.

## Compatibility

This method is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `getShardDistribution()` method has the following 
form: 

```javascript
db.collection.getShardDistribution()
```

## Output

**Note:**

The behavior of `getShardDistribution()` changed in MongoDB Shell
version 2.3.3:

- Starting in MongoDB Shell version 2.3.3, `getShardDistribution()`
  only contains regular sharded data and does not account for
  orphaned documents.

- Prior to MongoDB Shell version 2.3.3, `getShardDistribution()`
  accounts for both regular sharded data and orphaned documents
  pending deletion. If the collection contains orphaned documents,
  `getShardDistribution()` might indicate that the collection is
  unbalanced even if the collection is balanced in terms of regular
  data. The shard containing orphaned data has more documents and
  greater data size, but the same number of chunks compared to other
  shards.

### Sample Output

The following is a sample output for the distribution of a sharded
collection:

```none
Shard shard01 at shard01/localhost:27018
{
  data: '38.14MB',
  docs: 1000003,
  chunks: 2,
  'estimated data per chunk': '19.07B',
  'estimated docs per chunk': 500001
}
---
Shard shard02 at shard02/localhost:27019
{
  data: '38.14B',
  docs: 999999,
  chunks: 3,
  'estimated data per chunk': '12.71B',
  'estimated docs per chunk': 333333
}
---
Totals
{
  data: '76.29B',
  docs: 2000002,
  chunks: 5,
  'Shard shard01': [ '50 % data', '50 % docs in cluster', '40B avg obj size on shard' ],
  'Shard shard02': [ '49.99 % data', '49.99 % docs in cluster', '40B avg obj size on shard' ]
}
```

### Output Fields

```none
Shard shard01 at <host-a>   {
  data: <size-a>,
  docs: <count-a>,
  chunks: <number of chunks-a>,
  'estimated data per chunk': <size-a>/<number of chunks-a>,
  'estimated docs per chunk': <count-a>/<number of chunks-a>
}
---
Shard shard02 at <host-b>
{
  data: <size-b>,
  docs: <count-b>,
  chunks: <number of chunks-b>,
  'estimated data per chunk': <size-b>/<number of chunks-b>,
  'estimated docs per chunk': <count-b>/<number of chunks-b>
}
---
Totals
{
  data: <stats.size>,
  docs: <stats.count>,
  chunks: <calc total chunks>,
  Shard shard01: [ <estDataPercent-a> % data, <estDocPercent-a> % docs in cluster, stats.shards[ <shard-a> ].avgObjSize avg obj size on shard ],
  Shard shard02: [ <estDataPercent-b> % data, <estDocPercent-b> % docs in cluster, stats.shards[ <shard-b> ].avgObjSize avg obj size on shard ]
}
```

The output information displays:

* - Output
  - Description 

* - `<shard-x>` 
  - A string that holds the shard name.

* - `<host-x>`
  - A string that holds the host name(s).

* - `<size-x>`
  - A number that includes the size of the data,
    including the unit of measure (e.g. `b`, `Mb`).

* - `<count-x>`
  - A number that reports the number of documents in the shard.

* - `<number of chunks-x>`
  - A number that reports the number of chunks in the shard.

* - `<size-x>/<number of chunks-x>`
  - A calculated value that reflects the estimated data size per chunk 
    for the shard, including the unit of measure (e.g. `b`, `Mb`).

* - `<count-x>/<number of chunks-x>`
  - A calculated value that reflects the estimated number of documents 
    per chunk for the shard.

* - `<stats.size>`
  - A value that reports the total size of the data in the sharded collection,
    including the unit of measure.

* - `<stats.count>`
  - A value that reports the total number of documents in the sharded 
    collection.

* - `<calc total chunks>` 
  - A calculated number that reports the number of chunks from all shards. 
    For example:

    ```bash
    <calc total chunks> = <number of chunks-a> + <number of chunks-b>
    ```

* - `<estDataPercent-x>`
  - A calculated value that reflects, for each shard, the data size as the 
    percentage of the collection's total data size. For example:

    ```bash
    <estDataPercent-x> = <size-x>/<stats.size>
    ```

* - `<estDocPercent-x>`
  - A calculated value that reflects, for each shard, the number of
    documents as the percentage of the total number of documents for the
    collection. For example:

    ```bash
    <estDocPercent-x> = <count-x>/<stats.count>
    ```

* - `stats.shards[ <shard-x> ].avgObjSize`
  - A number that reflects the average object size, including the unit 
    of measure, for the shard.

## Behavior

After an unclean shutdown of a `mongod` using the Wired Tiger storage engine, count and size statistics reported by
`db.collection.getShardDistribution()` may be inaccurate.

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
