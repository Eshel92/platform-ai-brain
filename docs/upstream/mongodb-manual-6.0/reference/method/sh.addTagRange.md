<!-- Converted from reference/method/sh.addTagRange.txt (reStructuredText). Includes are inlined. -->

# sh.addTagRange()

## Definition

**`sh.addTagRange(namespace, minimum, maximum, tag)`**

**Note:**

This method aliases to `sh.updateZoneKeyRange()`. MongoDB provides Zone sharding as the successor to tag-aware sharding.

Attaches a range of shard key values to a shard tag created using the
`sh.addShardTag()` method. 

You can run `updateZoneKeyRange` database command and its helpers
`sh.updateZoneKeyRange()` and `sh.addTagRange()` on
an unsharded collection or a non-existing collection.

`sh.addTagRange()` takes
the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `namespace` | string | The namespace of the sharded collection to tag. |
| `minimum` | document | The minimum value of the shard key range to include in the tag. The minimum is an inclusive match. Specify the minimum value in the form of `<fieldname>:<value>`.  This value must be of the same BSON type or types as the shard key. |
| `maximum` | document | The maximum value of the shard key range to include in the tag. The maximum is an exclusive match.  Specify the maximum value in the form of `<fieldname>:<value>`. This value must be of the same BSON type or types as the shard key. |
| `tag` | string | The name of the tag to attach the range specified by the `minimum` and `maximum` arguments to. |

Use `sh.addShardTag()` to ensure that the balancer migrates
documents that exist within the specified range to a specific shard
or set of shards.

Only issue `sh.addTagRange()` when connected to a
`mongos` instance.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

### Bounds

Zone ranges are always inclusive of the lower boundary and exclusive
of the upper boundary.

### Initial Chunk Distribution for Empty or Non-Existing Collections

If you are considering performing zone sharding
on an empty or non-existent collection, use `sh.addTagRange()`
to create the zones and zone ranges *before* sharding the collection.
Creating zones and zone ranges on empty or non-existing collections allows 
MongoDB to optimize the initial chunk creation and distribution process when 
sharding the collection. This optimized process supports faster setup of zoned 
sharding with less balancer overhead than creating zones after sharding. The 
balancer performs all chunk management after the 
optimized initial chunk creation and distribution.

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

### Dropped Collections

Dropping a collection deletes its associated zone/tag ranges.

In earlier versions, MongoDB does not remove the tag associations for a
dropped collection, and if you later create a new collection with the
same name, the old tag associations will apply to the new collection.

## Example

Given a shard key of `{state: 1, zip: 1}`, the following operation
creates a tag range covering zip codes in New York State:

```javascript
sh.addTagRange( "exampledb.collection",
                { state: "NY", zip: MinKey },
                { state: "NY", zip: MaxKey },
                "NY"
              )
```
