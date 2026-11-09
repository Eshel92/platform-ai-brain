<!-- Converted from reference/method/sh.splitAt.txt (reStructuredText). Includes are inlined. -->

# sh.splitAt() (mongosh method)

## Definition

**`sh.splitAt(namespace, query)`**

Splits a chunk at the shard key value specified by the query.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `split` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The method takes the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `namespace` | string | The namespace (i.e. `<database>.<collection>`) of the sharded collection that contains the chunk to split. |
| `query` | document | A query document that specifies the shard key value at which to split the chunk. |

          

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

## Consideration

In most circumstances, you should leave chunk splitting to the
automated processes within MongoDB. However, when initially deploying a
sharded cluster, it may be beneficial to pre-split manually an empty collection using methods such as
`sh.splitAt()`.

## Behavior

`sh.splitAt()` splits the original chunk into two chunks. One
chunk has a shard key range that starts with the original lower bound
(inclusive) and ends at the specified shard key value (exclusive). The
other chunk has a shard key range that starts with the specified shard
key value (inclusive) as the lower bound and ends at the original upper
bound (exclusive).

To split a chunk at its median point instead, see
`sh.splitFind()`.

## Example

For the sharded collection `test.foo`, the following example splits a
chunk at the shard key value `x: 70`.

```javascript
sh.splitAt( "test.foo", { x: 70 } )
```
