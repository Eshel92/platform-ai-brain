<!-- Converted from reference/method/sh.shardCollection.txt (reStructuredText). Includes are inlined. -->

# sh.shardCollection() (mongosh method)

## Definition

**`sh.shardCollection(namespace, key, unique, options)`**

Shards a collection using the `key` as a the shard key.
The shard key determines how MongoDB distributes the collection's
documents among the shards.

**Note:**

**Changed in version:** 6.0

Starting in MongoDB 6.0, sharding a collection does **not** require you to
first run the `sh.enableSharding` method to configure the database.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `shardCollection` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

`sh.shardCollection()` takes the following
arguments:

* - Parameter

  - Type

  - Description

* - `namespace`

  - string

  - The namespace of the collection to shard in the form
    `"<database>.<collection>"`.

* - `key`

  - document

  - The document that specifies the field or fields to use as the
    shard key. 

    `{ <field1>: <1|"hashed">, ... }`

    Set the field value to either:

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

  - Optional. Specify `true` to ensure that the underlying index
    enforces a unique constraint. Defaults to `false`. 

    You cannot specify `true` when using hashed shard keys.

    If specifying the `options` document, you must explicitly
    specify the value for `unique`.

* - `options`

  - document

  - Optional. A document containing optional fields, including
    `numInitialChunks` and `collation`.

The `options` argument supports the following options:

* - Parameter

  - Type

  - Description

* - `numInitialChunks`

  - integer

  - Optional. Specifies the minimum number of chunks to create
    initially when sharding an *empty* collection with a
    hashed shard key. MongoDB
    then creates and balances chunks across the cluster. The
    `numInitialChunks` parameter must be less than `8192` chunks per shard.
    Defaults to `2` chunks per shard.

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
    has a default collation, you *must* include 
    a collation document with`{ locale : "simple" }`, or the 
    `shardCollection` command fails. At least one of the indexes
    whose fields support the shard key pattern must have the simple
    collation.

* - presplitHashedZones

  - boolean

  - .. _method-shard-collection-presplitHashedZones:

    Optional. Specify `true` to perform initial chunk creation
    and distribution for an empty or non-existing collection based
    on the defined zones and zone ranges for the collection. For
    hashed sharding only.

    `shardCollection()` with `presplitHashedZones: true` returns
    an error if any of the following are true:

    - The shard key does not contain a hashed field 
      (i.e. is not a single field hashed index or compound hashed index).

    - The collection has no defined zones or zone ranges.

    - The defined zone ranges do not meet the 
      requirements.

* - timeseries

  - document

  - .. _method-shard-collection-timeseries:

    Optional. Specify this option to create a new sharded time series
    collection.

    To shard an existing time series collection, omit this parameter.

    When the collection specified to `shardCollection` is a time series
    collection and the `timeseries` option is not specified, MongoDB uses
    the values that define the existing time series collection to populate
    the `timeseries` field.

    For detailed syntax, see
    method-sharded-time-series-collection-options.

### Time Series Options

**New in version:** 5.1

To create a new time series collection that is sharded, specify the
timeseries option to
`sh.shardCollection()`.

The timeseries option takes
the following fields:

| Field | Type | Description |
|---|---|---|
| `timeField` | string | .. include:: /includes/time-series/fact-time-field-description.rst |
| `metaField` | string | .. include:: /includes/time-series/fact-meta-field-description.rst |
| `granularity` | string | .. include:: /includes/time-series/fact-granularity-description.rst |

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

## Considerations

Once a collection has been sharded, MongoDB provides no method to
unshard a sharded collection.

### Shard Keys

While you can change your shard key
later, it is important to carefully consider your shard key choice to
avoid scalability and perfomance issues.

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
- [MongoDB Blog: On Selecting a Shard Key for MongoDB](https://www.mongodb.com/blog/post/on-selecting-a-shard-key-for-mongodb).

**See also:**

- sharding-shard-key
- sharding-shard-key-selection

### Hashed Shard Keys

Hashed shard keys use a
hashed index or  a
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
sh.shardCollection-zones-compound-hashed.

#### Initial Chunk Distribution with Compound Hashed Indexes

MongoDB supports sharding collections on
compound hashed indexes. When
sharding an empty or non-existing collection using a compound hashed
shard key, additional requirements apply in order for MongoDB to
perform initial chunk creation and distribution.

The `numInitialChunks` option has no effect if zones and zone ranges
have been defined for the empty collection *and*
presplitHashedZones
is `false`.

See pre-define-zone-range-hashed-example for an example.

**See also:**

initial-ranges

 

### Uniqueness

If specifying `unique: true`:

- If the collection is empty, `sh.shardCollection()` creates the unique index on the
  shard key if such an index does not already exist.

- If the collection is not empty, you must create the index first
  before using `sh.shardCollection()`.

Although you can have a unique compound index where the shard
key is a prefix, if using `unique`
parameter, the collection must have a unique index that is on the shard
key.

See also Sharded Collection and Unique Indexes

### Collation

If the collection has a default collation,
the `sh.shardCollection` command must include a `collation` parameter with the
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

## Examples

### Simple Usage

Given a collection named `people` in a database named `records`,
the following command shards the collection by the
`zipcode` field:

```javascript
sh.shardCollection("records.people", { zipcode: 1 } )
```

### Usage with Options

The `phonebook` database has a collection `contacts` with no
default collation. The 
following example uses
`sh.shardCollection()` to shard the `phonebook.contacts` with:

- a hashed shard key on the
  `last_name` field,
- `5` initial chunks, and
- a collation of `simple`. 

```javascript
sh.shardCollection(
  "phonebook.contacts",
  { last_name: "hashed" },
  false,
  {
    numInitialChunks: 5,
    collation: { locale: "simple" }
  }
)
```

**See also:**

- `refineCollectionShardKey`
- `sh.balancerCollectionStatus()`
- `shardCollection`
- /sharding
