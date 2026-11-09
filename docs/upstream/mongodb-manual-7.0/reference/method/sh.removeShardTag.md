<!-- Converted from reference/method/sh.removeShardTag.txt (reStructuredText). Includes are inlined. -->

# sh.removeShardTag() (mongosh method)

## Definition

**`sh.removeShardTag(shard, tag)`**

**Note:**

This method aliases to `sh.removeShardFromZone()`. MongoDB provides Zone sharding as the successor to tag-aware sharding.

Removes the association between a tag and a shard. Only issue
`sh.removeShardTag()` when connected to a `mongos`
instance.

| Parameter | Type | Description |
|---|---|---|
| `shard` | string | The name of the shard from which to remove a tag. |
| `tag` | string | The name of the tag to remove from the shard. |

**See also:**

`sh.addShardTag()`
`sh.addTagRange()`

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
