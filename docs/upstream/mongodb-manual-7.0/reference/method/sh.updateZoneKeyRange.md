<!-- Converted from reference/method/sh.updateZoneKeyRange.txt (reStructuredText). Includes are inlined. -->

# sh.updateZoneKeyRange() (mongosh method)

## Definition

**`sh.updateZoneKeyRange(namespace, minimum, maximum, zone)`**

Associates a range of shard key values with a zone.

You can run `updateZoneKeyRange` database command and its helpers
`sh.updateZoneKeyRange()` and `sh.addTagRange()` on
an unsharded collection or a non-existing collection.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `updateZoneKeyRange` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

`sh.updateZoneKeyRange()` takes the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `namespace` | string | The namespace of the sharded collection associate with the `zone`. The collection must be sharded for the operation to succeed. |
| `minimum` | document | The inclusive lower bound of the range of shard key values. Specify each field of the shard key in the form of `<fieldname> : <value>`. The value must be of the same BSON type or types as the shard key. To use hashed sharding, the field value needs to be of type `NumberLong`. |
| `maximum` | document | The exclusive upper bound of the range of shard key values. Specify each field of the shard key in the form of `<fieldname> : <value>`. The value must be of the same BSON type or types as the shard key. To use hashed sharding, the field value needs to be of type `NumberLong`. |
| `zone` | string | The name of the zone to associate with the range of shard key values bounded by `minimum` and `maximum`. |

Only issue `sh.updateZoneKeyRange()` when connected to a
`mongos` instance.

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

## Behavior

You cannot create a range of shard key values whose lower and upper boundaries
overlap with an existing range for the sharded collection. For example, given
an existing range of `1` to `10`, you cannot create a new range of `5`
to `20`, as the new range would overlap with the existing range.

A zone can have multiple ranges of data associated with it, but a range
can at most be associated with a single zone.

See the zone manual page for more information on zones
in sharded clusters.

### Initial Chunk Distribution for Empty or Non-Existing Collections

If you are considering performing zone sharding
on an empty or non-existent collection, use
`sh.updateZoneKeyRange()` to create the zones and zone ranges
*before* sharding the collection (*since 4.0.2*). Starting in version
4.0.3, creating zones and zone ranges on empty or non-existing
collections allows MongoDB to optimize the initial chunk creation and
distribution process when sharding the collection. This optimized
process supports faster setup of zoned sharding with less balancer
overhead than creating zones after sharding. The balancer performs all chunk management after the optimized
initial chunk creation and distribution.

For an example of defining zones and zone ranges for initial chunk
distribution, see pre-define-zone-range-example.

#### Initial Chunk Distribution with Compound Hashed Shard Keys

MongoDB supports sharding collections on
compound hashed indexes. MongoDB can
perform optimized initial chunk creation and distribution when sharding
the empty or non-existing collection on a compound hashed shard key.

**hash-prefix:**

If the hashed field is the prefix of the shard key (i.e. the first
field in the shard key), all of the following must be true for
MongoDB to perform initial chunk creation and distribution:

- The collection has a single zone range with `MinKey` for 
  all lower-bound fields and `MaxKey` for all upper-bound
  fields.

- `sh.shardCollection()` specifies the 
  presplitHashedZones: true option.

**hash-not-prefix:**

If the hashed field is *not* the prefix of the shard key (i.e. 
the shard key has one or more non-hashed leading fields), all of
the following must be true for MongoDB to perform initial chunk
creation and distribution:

- The collection has one zone range for each combination of distinct 
  prefix field values (i.e. all fields preceding the hashed field).

- For the lower-bound of each zone range, specify `MinKey` for
  the hashed field and all subsequent fields.

- For each zone range, at least one upper-bound prefix field *must*
  differ from its lower-bound counterpart.

- `sh.shardCollection()`
  specifies the presplitHashedZones: true option.

For a more complete example of defining zones and zone ranges for
initial chunk distribution on a compound hashed shard key, see
pre-define-zone-range-hashed-example.

**See also:**

`sh.balancerCollectionStatus()`

### Balancer

After associating a range to a zone, the balancer must first run in order to migrate any chunks
whose ranges are covered by the zone to shards inside of that zone. Until
balancing completes, some chunks may reside on the wrong shard given the
configured zones for the sharded cluster. See zone-sharding-balancer
for more information.

See the sharded cluster balancer manual page for
more information on how migrations work in a sharded cluster.

### Bounds

Zone ranges are always inclusive of the lower boundary and exclusive
of the upper boundary.

### Dropped Collections

Dropping a collection deletes its associated zone/tag ranges.

In earlier versions, MongoDB does not remove the tag associations for a
dropped collection, and if you later create a new collection with the
same name, the old tag associations will apply to the new collection.

### Security

For sharded clusters running with authentication, you
must authenticate as either:

- a user whose privileges include the specified actions on various
  collections in the `config` database:

  - `find` on the `config.shards` collection

  - `find` and `update` on the `config.tags`
    collection;

  or, alternatively,

- a user whose privileges include `enableSharding` on the
  cluster resource.

The `clusterAdmin` or `clusterManager` built-in roles have
the appropriate permissions for issuing `sh.updateZoneKeyRange()`. See
the documentation page for Role-Based Access Control
for more information.

## Examples

Given a sharded collection `exampledb.collection` with a shard key of ``{ a
: 1 }`, the following operation creates a range with a lower bound of `1``
and an upper bound of `10` on the `alpha` zone:

```javascript
sh.updateZoneKeyRange(
   "exampledb.collection",
   { a : 1 },
   { a : 10 },
   "alpha"
)
```

The following operation removes the previously created range by passing
`null` to the `zone` field.

```javascript
sh.updateZoneKeyRange( 
   "exampledb.collection",
   { a : 1 },
   { a : 10 },
   null
)
```

The `min` and `max` must match exactly the bounds of the target range.
The following operation attempts to remove the previously created range, but
specifies `{ a : 0 }` as the `min` bound:

```javascript
sh.updateZoneKeyRange(
   "exampledb.collection",
   { a : 0 },
   { a : 10 },
   null
)
```

While the range of `{ a : 0 }` and `{ a : 10 }` encompasses the existing
range, it is not an exact match and therefore `updateZoneKeyRange`
does not remove anything.

### Compound Shard Key

Given a sharded collection `exampledb.collection` with a shard key of ``{ a
: 1, b : 1 }``, the following operation creates a range covering the lower
bound of `{ a: 1, b : 1 }` and an upper bound of `{ a : 10, b : 10}` and associates it
with the `alpha` zone:

```javascript
sh.updateZoneKeyRange(
   "exampledb.collection",
   { a : 1, b : 1 },
   { a : 10, b : 10 },
   "alpha"
)
```

### Pre-Define Zones and Zone Ranges for an Empty or Non-Existing Collection

If you create zones and zone ranges on empty or non-existing collections, 
MongoDB may optimize the initial chunk creation and distribution process when 
sharding the collection. This optimized process supports faster setup of zoned 
sharding with less balancer overhead than creating zones after sharding. The 
balancer performs all chunk management after the 
optimized initial chunk creation and distribution. For more information, see 
updateZoneKeyRange-method-init-chunk-distribution-compound-hashed
for more information.

The sections below contain examples for three different shard key types.

Consider the following examples, which explore pre-defining zones or
zone ranges for three different shard key types:

- updatezonekeyrange-single-or-compound-example
- updatezonekeyrange-compound-prefix-hashed-example
- updatezonekeyrange-compound-non-prefix-hashed-example

#### Single or Compound Shard Keys

**Note:**

This example only applies to single-field or compound shard keys
*without* a hashed field. 

For example, `{ "zip" : 1 }` or  
`{ "zip" : 1, "account" : 1}`

**Step 1: Create the Zones**

Use `sh.addShardToZone()` to create the zones:

```javascript
sh.addShardToZone("shardA", "DC1")
sh.addShardToZone("shardB", "DC2")
```

**Step 2: Create the Zone Ranges**

Use `sh.updateZoneKeyRange()` to create the ranges
for the empty `contacts` collection in the `exampledb`
database:

```javascript
sh.updateZoneKeyRange( 
    "exampledb.contacts",
    { zip: 10001 },
    { zip: 10090 },
    "DC1"
);

sh.updateZoneKeyRange( 
    "exampledb.contacts",
    { zip: 90001 },
    { zip: 96054 },
    "DC2"
);
```

**Step 3: Shard the Collection**

**Note:**

If the collection does not exist, the sharding operation creates
the collection.

If the collection is empty and no index exists to support the 
shard key, the sharding operation creates the index.

Use `sh.shardCollection()` to shard the collection `contacts`:

```javascript
sh.shardCollection("exampledb.contacts",  { zip: 1 } );
```

**Step 4: Review the Created Chunks and Distribution**

To see the created chunks and distribution, run the
`sh.status()` operation:

```javascript
sh.status()
```

The method returns:

```javascript
--- Sharding Status --- 
  sharding version: {
    "_id" : 1,
    "minCompatibleVersion" : 5,
    "currentVersion" : 6,
    "clusterId" : ObjectId("5b80c06d35a961fd0ae1986d")
  }
  shards:
        {  "_id" : "shardA",  "host" : "shardA/mongodb0.example.net:27018,mongodb1.example.net:27018,mongodb2.example.net:27018",  "state" : 1,  "tags" : [ "DC1" ] }
        {  "_id" : "shardB",  "host" : "shardB/mongodb3.example.net:27018,mongodb4.example.net:27018,mongodb5.example.net:27018",  "state" : 1,  "tags" : [ "DC2" ] }
  active mongoses:
        "4.2.0" : 2
  autosplit:
        Currently enabled: yes
  balancer:
        Currently enabled:  yes
        Currently running:  no
        Failed balancer rounds in last 5 attempts:  0
        Migration Results for the last 24 hours: 
                No recent migrations
  databases:
        {  "_id" : "config",  "primary" : "config",  "partitioned" : true }
        {  "_id" : "exampledb",  "primary" : "shardA",  "partitioned" : true,  "version" : {  "uuid" : UUID("6c351bcf-acd2-4fd9-82d8-9f6bd7321558"),  "lastMod" : 1 } }
                exampledb.contacts
                        shard key: { "zip" : 1 }
                        unique: false
                        balancing: true
                        chunks:
                                shardA   3
                                shardB   2
                        { "zip" : { "$minKey" : 1 } } -->> { "zip" : 10001 } on : shardA Timestamp(1, 0) 
                        { "zip" : 10001 } -->> { "zip" : 10090 } on : shardA Timestamp(1, 1) 
                        { "zip" : 10090 } -->> { "zip" : 90001 } on : shardB Timestamp(1, 2) 
                        { "zip" : 90001 } -->> { "zip" : 96054 } on : shardB Timestamp(1, 3) 
                        { "zip" : 96054 } -->> { "zip" : { "$maxKey" : 1 } } on : shardA Timestamp(1, 4) 
                          tag: DC1  { "zip" : 10001 } -->> { "zip" : 10090 }
                          tag: DC2  { "zip" : 90001 } -->> { "zip" : 96054 }
```

For the collection, sharding operation created 5 chunks (two chunks
that correspond to the zone ranges and the other three to cover all
other values) across shardA and shardB.

#### Compound Hashed Shard Key with Hashed Prefix

**Note:**

This example only applies to compound hashed shard keys where the
hashed field is the prefix of the shard key (i.e. the first field in
the shard key is hashed).

For example, `{ "_id" : "hashed", "facility" : 1 }`

MongoDB supports sharding collections on
compound hashed indexes. When
sharding on a compound hashed shard key, MongoDB can perform
optimized initial chunk creation and distribution on the empty or
non-existing collection *only if* the defined zone ranges meet
additional requirements.

Consider an empty collection `examples.metrics` which will store
analytics from one of two manufacturing facilities. The 
planned shard key is `{ "_id" : "hashed", "facility" : 1}`,
where the hashed field is the shard key *prefix*.
 
**Step 1: Create the Zones**

The planned shard key is `{ "_id" : "hashed", "facility" : 1 }`.   
Since the hashed field is the prefix (i.e. the first field in the
shard key), create a *single* zone using 
`sh.addShardToZone()`:

```javascript
sh.addShardToZone("shardA", "FacilityAlpha")
sh.addShardToZone("shardB", "FacilityAlpha")
```

**Step 2: Create the Zone Ranges**

Initial chunk distribution on a compound hashed shard key with a
hashed prefix requires a single zone range with `MinKey` for all
lower-bound fields and `MaxKey` for all upper-bound fields.

Use `sh.updateZoneKeyRange()` to create a single range:

```javascript
sh.updateZoneKeyRange( 
   "examples.metrics",
   { "_id" : MinKey, "facility" : MinKey },
   { "_id" : MaxKey, "facility" : MaxKey },
   "FacilityAlpha"
);
```

**Step 3: Shard the Collection**

**Note:**

If the collection does not exist, the sharding operation creates
the collection.

If the collection is empty and no index exists to support the 
shard key, the sharding operation creates the index.

Use `sh.shardCollection()` with 
presplitHashedZones: true to shard the 
collection and perform initial chunk creation and distribution:

```javascript
sh.shardCollection(
  "examples.metrics",
  { "_id" : "hashed", "facility" : 1 },
  false,
  { presplitHashedZones: true }
)
```

**Step 4: Review the Created Chunks and Distribution**

To see the created chunks and distribution, run the
`sh.status()` operation:

```javascript
sh.status()
```

The output resembles the following 
(*content omitted for  readability*):

```javascript
--- Sharding Status --- 

databases:
  {  "_id" : "config",  "primary" : "config",  "partitioned" : true }
  {  "_id" : "examples",  "primary" : "shardA",  "partitioned" : true,  "version" : {  "uuid" : UUID("245f8abf-a363-48b0-8208-2a5b577bbb4e"),  "lastMod" : 1 } }
    examples.metrics
      shard key: { "_id" : "hashed", "facility" : 1 }
      unique: false
      balancing: true
      chunks:
        shardA  2
        shardB  2
      { "_id" : { "$minKey" : 1 }, "facility" : { "$minKey" : 1 } } -->> { "_id" : NumberLong("-4611686018427387902"), "facility" : { "$minKey" : 1 } } on : shardA Timestamp(1, 0) 
      { "_id" : NumberLong("-4611686018427387902"), "facility" : { "$minKey" : 1 } } -->> { "_id" : NumberLong(0), "facility" : { "$minKey" : 1 } } on : shardA Timestamp(1, 1) 
      { "_id" : NumberLong(0), "facility" : { "$minKey" : 1 } } -->> { "_id" : NumberLong("4611686018427387902"), "facility" : { "$minKey" : 1 } } on : shardB Timestamp(1, 2) 
      { "_id" : NumberLong("4611686018427387902"), "facility" : { "$minKey" : 1 } } -->> { "_id" : { "$maxKey" : 1 }, "facility" : { "$maxKey" : 1 } } on : shardB Timestamp(1, 3) 

        tag: FacilityAlpha  { "_id" : { "$minKey" : 1 }, "facility" : { "$minKey" : 1 } } -->> { "_id" : { "$maxKey" : 1 }, "facility" : { "$maxKey" : 1 } }
```

The sharding operation produced 4 chunks in total. Two chunks
correspond to the absolute lower and upper bounds. One zone was
created on `shardA` and `shardB` corresponding to
`FacilityAlpha`. The zone was subdivided into 2 chunks using the 
hashed field.

#### Compound Hashed Shard Key with Non-Prefix Hashed Field

**Note:**

This example only applies to compound hashed shard keys where the
hashed field is *not* the prefix of the shard key (i.e. the first
field in the shard key is not hashed).

For example, `{ "facility" : 1, "_id" : "hashed" }`

MongoDB supports sharding collections on
compound hashed indexes. When
sharding on a compound hashed shard key, MongoDB can perform
optimized initial chunk creation and distribution on the empty or
non-existing collection *only if* the defined zone ranges meet
additional requirements.

Consider an empty collection `examples.metrics` which will store
analytics from one of two manufacturing facilities. The planned
shard key is `{ "facility" : 1, "_id" : "hashed" }`, where 
the hashed field is *not* the shard key prefix.

- The `facility` field stores the name of the facility: 
  `"FacilityAlpha"` or `"FacilityBaker"`.  The 
  collection requires zone ranges on `facility` to help isolate 
  data for each facility to specific shards. 

- The `_id` field compensates for the low-cardinality of the 
  `facility` field. Hashing compensates for the
  monotonically-increasing nature of the `_id` field.
 
**Step 1: Create the Zones**

Use the `sh.addShardToZone()` command to create the 
zones.

```javascript
sh.addShardToZone("shardA", "FacilityAlpha")
sh.addShardToZone("shardB", "FacilityBaker")
```

**Step 2: Create the Zone Ranges**

The planned shard key is `{"facility" : 1, "_id" : "hashed"}`. The
`facility` field has two possible values: `FacilityAlpha` and
`FacilityBaker`.

Initial chunk distribution on a compound hashed shard key where the
hashed field is *not* the prefix requires one zone range for each
combination of distinct prefix field values (i.e. all fields
preceding the hashed field). Since `facility` has two distinct 
prefix values, the collection requires exactly two zone ranges 
that cover those values.

- The lower bound range specifies `MinKey` for all non-prefix
  fields.

- The upper-bound range has at least one prefix field that 
  differs from its lower-bound counterpart.

Use `sh.updateZoneKeyRange()` to create the range for 
`"facility": "FacilityAlpha"`:

```javascript
sh.updateZoneKeyRange( 
   "examples.metrics",
   { "facility": "FacilityAlpha", "_id" : MinKey },
   { "facility": "FacilityBaker", "_id" : MinKey },
   "FacilityAlpha"
);
```

- Since zone range upper bounds are *exclusive*, this range only
  covers documents with the distinct shard key prefix value 
  `"facilty" : "FacilityAlpha"` and all possible values of `_id`. 

Use `sh.updateZoneKeyRange()` to create the range for 
`"facility": "FacilityBaker"`:

```javascript
sh.updateZoneKeyRange( 
   "examples.metrics",
   { "facility": "FacilityBaker", "_id" : MinKey },
   { "facility": MaxKey, "_id" : MinKey },
   "FacilityBaker"
);
```

- While the upper bound of this range can technically
  capture other values of `facility`, the initial chunk
  distribution logic relies on the assumption that no other distinct
  values for `facility` exist. Since the collection only contains
  documents where `facility` is `FacilityAlpha` or 
  `FacilityBaker`, this range only covers
  documents with the distinct shard key prefix value 
  `"facility" : "FacilityBaker"` and all possible values of 
  `_id`.

**Step 3: Shard the Collection**

**Note:**

If the collection does not exist, the sharding operation creates
the collection.

If the collection is empty and no index exists to support the 
shard key, the sharding operation creates the index.

Use `sh.shardCollection()` with 
presplitHashedZones: true to shard the 
collection and perform initial chunk creation and distribution:

```javascript
sh.shardCollection(
  "examples.metrics",
  { "facility" : 1, "_id" : "hashed"},
  false,
  { presplitHashedZones: true }
)
```

**Step 4: Review the Created Chunks and Distribution**

To see the created chunks and distribution, run the
`sh.status()` operation:

```javascript
sh.status()
```

The output resembles the following 
(*content omitted for  readability*):

```javascript
--- Sharding Status --- 

  databases:
    {  "_id" : "config",  "primary" : "config",  "partitioned" : true }
    {  "_id" : "examples",  "primary" : "shardA",  "partitioned" : true,  "version" : {  "uuid" : UUID("6c351bcf-acd2-4fd9-82d8-9f6bd7321558"),  "lastMod" : 1 } }
      examples.metrics
        shard key: { "facility" : 1, "_id" : "hashed" }
        unique: false
        balancing: true
        chunks:
          shardA  3
          shardB  3
        { "facility" : { "$minKey" : 1 }, "_id" : { "$minKey" : 1 } } -->> { "facility" : "FacilityAlpha", "_id" : { "$minKey" : 1 } } on : shard1 Timestamp(1, 0) 
        { "facility" : "FacilityAlpha", "_id" : { "$minKey" : 1 } } -->> { "facility" : "FacilityAlpha", "_id" : NumberLong(0) } on : shard1 Timestamp(1, 1) 
        { "facility" : "FacilityAlpha", "_id" : NumberLong(0) } -->> { "facility" : "FacilityBaker", "_id" : { "$minKey" : 1 } } on : shard1 Timestamp(1, 2) 
        { "facility" : "FacilityBaker", "_id" : { "$minKey" : 1 } } -->> { "facility" : "FacilityBaker", "_id" : NumberLong(0) } on : shard2 Timestamp(1, 3) 
        { "facility" : "FacilityBaker", "_id" : NumberLong(0) } -->> { "facility" : { "$maxKey" : 1 }, "_id" : { "$minKey" : 1 } } on : shard2 Timestamp(1, 4) 
        { "facility" : { "$maxKey" : 1 }, "_id" : { "$minKey" : 1 } } -->> { "facility" : { "$maxKey" : 1 }, "_id" : { "$maxKey" : 1 } } on : shard2 Timestamp(1, 5) 

          tag: FacilityAlpha  { "facility" : "FacilityAlpha", "_id" : { "$minKey" : 1 } } -->> { "facility" : "FacilityBaker", "_id" : { "$minKey" : 1 } }
          tag: FacilityBaker  { "facility" : "FacilityBaker", "_id" : { "$minKey" : 1 } } -->> { "facility" : { "$maxKey" : 1 }, "_id" : { "$minKey" : 1 } }
```

The sharding operation produced 6 chunks in total. Two chunks
correspond to the absolute lower and upper bounds. Two zones were
created, one on `shardA` and one on `shardB`, corresponding to
`FacilityAlpha` and `FacilityBaker`. Each of these zones has been
further subdivided into 2 chunks using the hashed field.

**See also:**

- `sh.addShardToZone()`
- `sh.removeRangeFromZone()`
