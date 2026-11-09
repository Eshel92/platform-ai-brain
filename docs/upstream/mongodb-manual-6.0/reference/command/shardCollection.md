<!-- Converted from reference/command/shardCollection.txt (reStructuredText). Includes are inlined. -->

# shardCollection

## Definition

**`shardCollection`**

Shards a collection to distribute its documents across
shards. The `shardCollection` command must be run against the
`admin` database.

**Note:**

**Changed in version:** 6.0

Starting in MongoDB 6.0, sharding a collection does **not** require you to
first run the `enableSharding` command to configure the database.

helper method

**Tip:**

In `mongosh`, this command can also be run through the `sh.shardCollection`.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in serverless instances.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

                

## Syntax

To run `shardCollection`, use the `db.runCommand( { <command> } )` method.

The command has the following form:

```javascript
db.adminCommand(
   {
     shardCollection: "<database>.<collection>",
     key: { <field1>: <1|"hashed">, ... },
     unique: <boolean>,
     numInitialChunks: <integer>,
     presplitHashedZones: <boolean>,
     collation: { locale: "simple" },
     timeseries: <object>
   }
 )
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - `shardCollection`
  - string
  - The namespace of the collection to shard in the form
    `<database>.<collection>`.

* - `key`
  - document
  - The document that specifies the field or fields to use as the
    shard key.

    `{ <field1>: <1|"hashed">, ... }`

    Set the field values to either:

    - `1` for ranged based sharding

    - `"hashed"` to specify a
      hashed shard key.

    shard key must be
    supported by an index. Unless the collection is empty, the
    index must exist prior to the `shardCollection`
    command. If the collection is empty, MongoDB creates the
    index prior to sharding the collection if the index that can
    support the shard key does not already exist.

    See also sharding-shard-key-indexes

* - `unique`
  - boolean
  - Specify `true` to ensure that the underlying index
    enforces a unique constraint. Defaults to `false`. 

    You cannot specify `true` when using hashed shard keys.

* - `numInitialChunks`
  - integer
  - Specifies the initial number of chunks to create across all shards in 
    the cluster when sharding an *empty* collection with a
    hashed shard key. MongoDB
    will then create and balance chunks across the cluster. The
    `numInitialChunks` must result in less than `8192` per shard.

    If the collection is not empty or the shard key does not
    contain a hashed field, the operation returns an error.

    - If sharding with presplitHashedZones: true,
      MongoDB attempts to evenly distribute the specified
      number of chunks across the zones in the cluster.

    - If sharding with presplitHashedZones: false or omitted and
      no zones and zone ranges are defined for the empty
      collection, MongoDB attempts to evenly distributed the
      specified number of chunks across the shards in the cluster.

    - If sharding with presplitHashedZones: false or omitted and
      zones and zone ranges have been defined for the empty
      collection, `numInitChunks` has no effect.

* - `collation`
  - document
  - Optional. If the collection specified to `shardCollection`
    has a default collation,
    you *must* include a collation document with
    `{ locale : "simple" }`, or
    the `shardCollection` command fails. At least one of the indexes
    whose fields support the shard key pattern must have the simple
    collation.

* - presplitHashedZones
  - boolean
  - .. _cmd-shard-collection-presplitHashedZones:

    Optional. Specify `true` to perform initial chunk creation
    and distribution for an empty or non-existing collection based
    on the defined zones and zone ranges for the collection. For
    hashed sharding only.

    `shardCollection` with `presplitHashedZones: true` returns
    an error if any of the following are true:

    - The shard key does not contain a hashed field 
      (i.e. is not a single field hashed index or compound hashed index).

    - The collection has no defined zones or zone ranges.

    - The defined zone range or ranges do not meet the 
      requirements.

* - timeseries
  - object
  - .. _cmd-shard-collection-timeseries:

    Optional. Specify this option to create a new sharded time series
    collection.

    To shard an existing time series collection, omit this parameter.

    When the collection specified to `shardCollection` is a time series
    collection and the `timeseries` option is not specified, MongoDB uses
    the values that define the existing time series collection to populate
    the `timeseries` field.

    For detailed syntax, see
    cmd-sharded-time-series-collection-options.

    **New in version:** 5.1

 

### Time Series Options

**New in version:** 5.1

To create a new time series collection that is sharded, specify the
timeseries option to
`shardCollection`.

The timeseries option takes
the following fields:

| Field | Type | Description |
|---|---|---|
| `timeField` | string | .. include:: /includes/time-series/fact-time-field-description.rst |
| `metaField` | string | .. include:: /includes/time-series/fact-meta-field-description.rst |
| `granularity` | string | .. include:: /includes/time-series/fact-granularity-description.rst |

## Considerations

### Shard Keys

While you can change your shard key
later, it is important to carefully consider your shard key choice to
avoid scalability and perfomance issues.

**See also:**

- sharding-shard-key-selection
- sharding-shard-key

#### Shard Keys on Time Series Collections

When sharding time series collections, you can only specify
the following fields in the shard key:

- The `metaField`
- Sub-fields of `metaField`
- The `timeField`

You may specify combinations of these fields in the shard key. No other
fields, including `_id`, are allowed in the shard key pattern.

When you specify the shard key:

- `metaField` can be either a:

  - Hashed shard key
  - Ranged shard key

- `timeField` must be:

  - A ranged shard key
  - At the end of the shard key pattern

**Tip:**

Avoid specifying **only** the `timeField` as the shard key. Since
the `timeField` increases monotonically, it may result in all writes appearing on a
single chunk within the cluster. Ideally, data is evenly distributed
across chunks.

To learn how to best choose a shard key, see:

- sharding-shard-key-requirements
- [MongoDB Blog: On Selecting a Shard Key for MongoDB](https://www.mongodb.com/blog/post/on-selecting-a-shard-key-for-mongodb?tck=docs_server).

### Hashed Shard Keys

Hashed shard keys use a
hashed index or a
compound hashed index
as the shard key.

Use the form `field: "hashed"` to specify a hashed shard key field.

**Note:** If chunk migrations are in progress while creating a hashed

shard key collection, the initial chunk distribution may be
uneven until the balancer automatically balances the
collection.

**See also:**

/core/hashed-sharding

### Zone Sharding and Initial Chunk Distribution

The shard collection operation (i.e. `shardCollection`
command and the `sh.shardCollection()` helper) can perform
initial chunk creation and distribution for an empty or a
non-existing collection if zones and zone ranges have been defined for the collection. Initial
chunk distribution allows for a faster setup of zoned sharding.
After the initial distribution, the balancer manages the chunk
distribution going forward per usual.

See pre-define-zone-range-example for an example. If sharding a
collection using a ranged or single-field hashed shard key, the
`numInitialChunks` option has no effect if zones and zone ranges have
been defined for the empty collection.

To shard a collection using a compound hashed index, see
shardCollection-zones-compound-hashed.

#### Zone Sharding and Compound Hashed Indexes

MongoDB supports sharding collections on
compound hashed indexes. When
sharding an empty or non-existing collection using a compound hashed
shard key, additional requirements apply in order for MongoDB to
perform initial chunk creation and distribution.

The `numInitialChunks` option has no effect if zones and zone ranges
have been defined for the empty collection *and*
presplitHashedZones is
`false`.

See pre-define-zone-range-hashed-example for an example.

**See also:**

- initial-chunks 
- `balancerCollectionStatus`

### Uniqueness

If specifying `unique: true`:

- If the collection is empty, `shardCollection` creates the unique index on the
  shard key if such an index does not already exist.

- If the collection is not empty, you must create the index first
  before using `shardCollection`.

Although you can have a unique compound index where the shard
key is a prefix, if using `unique`
parameter, the collection must have a unique index that is on the shard
key.

See also Sharded Collection and Unique Indexes

### Collation

**Changed in version:** 3.4

If the collection has a default collation,
the `shardCollection` command must include a `collation` parameter with the
value `{ locale: "simple" }`. For non-empty collections with a
default collation, you must have at least one index with the simple
collation whose fields support the shard key pattern.

You do not need to specify the `collation` option for collections
without a collation. If you do specify the collation option for
a collection with no collation, it will have no effect.

### Write Concern

`mongos` uses `"majority"` for the
write concern of the
`shardCollection` command and its helper
`sh.shardCollection()`.

## Example

The following operation enables sharding for the `people` collection
in the `records` database and uses the `zipcode` field as the
shard key:

```javascript
db.adminCommand( { shardCollection: "records.people", key: { zipcode: 1 } } )
```

   

**See also:**

- `refineCollectionShardKey`
- `sh.balancerCollectionStatus()`
- `sh.shardCollection()`
- /sharding
