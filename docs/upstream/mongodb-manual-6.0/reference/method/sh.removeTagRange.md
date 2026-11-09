<!-- Converted from reference/method/sh.removeTagRange.txt (reStructuredText). Includes are inlined. -->

# sh.removeTagRange()

## Definition

**`sh.removeTagRange(namespace, minimum, maximum)`**

**Note:**

This method aliases to `sh.removeRangeFromZone()`. MongoDB provides Zone sharding as the successor to tag-aware sharding.

Removes a specified shard tag from a defined range of shard key values. 
`sh.removeTagRange()` takes the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `namespace` | string | The namespace of the sharded collection to tag. |
| `minimum` | document | The minimum value of the shard key from the tag. Specify the minimum value in the form of `<fieldname>:<value>`.  This value must be of the same BSON type or types as the shard key. |
| `maximum` | document | The maximum value of the shard key range from the tag. Specify the maximum value in the form of `<fieldname>:<value>`. This value must be of the same BSON type or types as the shard key. |

Use `sh.removeTagRange()` to ensure that unused or out of
date ranges are removed and hence chunks are balanced as required.

Only run `sh.removeTagRange()` when connected to a
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

## Example

Given a shard key of `{state: 1, zip: 1}`, the following operation
removes an existing tag range covering zip codes in New York State:

```javascript
sh.removeTagRange( "exampledb.collection",
                { state: "NY", zip: MinKey },
                { state: "NY", zip: MaxKey }
              )
```
