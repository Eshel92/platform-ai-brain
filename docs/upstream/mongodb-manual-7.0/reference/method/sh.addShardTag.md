<!-- Converted from reference/method/sh.addShardTag.txt (reStructuredText). Includes are inlined. -->

# sh.addShardTag() (mongosh method)

## Definition

**`sh.addShardTag(shard, tag)`**

**Note:**

This method aliases to `sh.addShardToZone()`. MongoDB provides Zone sharding as the successor to tag-aware sharding.

Associates a shard with a tag or identifier. MongoDB uses these
identifiers to direct chunks that fall within a
tagged range to specific shards. `sh.addTagRange()`
associates chunk ranges with tag ranges.

| Parameter | Type | Description |
|---|---|---|
| `shard` | string | The name of the shard to which to give a specific tag. |
| `tag` | string | The name of the tag to add to the shard. |

Only issue `sh.addShardTag()` when connected to a
`mongos` instance.

**Tip:**

By defining the zones and the zone ranges *before* sharding an empty
or a non-existing collection, the shard collection operation creates
chunks for the defined zone ranges as well as any additional chunks
to cover the entire range of the shard key values and performs an
initial chunk distribution based on the zone ranges. This initial
creation and distribution of chunks allows for faster setup of zoned
sharding. After the initial distribution, the balancer manages the
chunk distribution going forward.

See pre-define-zone-range-example for an example.

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

## Example

The following example adds three tags, `NYC`, `LAX`, and `NRT`, to
three shards:

```javascript
sh.addShardTag("shard0000", "NYC")
sh.addShardTag("shard0001", "LAX")
sh.addShardTag("shard0002", "NRT")
```

**See also:**

- `sh.addTagRange()`
- `sh.removeShardTag()`
