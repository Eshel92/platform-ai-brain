<!-- Converted from reference/method/sh.splitFind.txt (reStructuredText). Includes are inlined. -->

# sh.splitFind() (mongosh method)

## Definition

**`sh.splitFind(namespace, query)`**

Splits the chunk that contains the shard key value specified by the
`query` at the chunk's median point. `sh.splitFind()`
creates two roughly equal chunks. To split a chunk at a specific
point instead, see `sh.splitAt()`.

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
| `query` | document | A query document that specifies the shard key value that determines the chunk to split. |

The `sh.splitFind()` method wraps the `split`
command.

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
automated processes within MongoDB.

To use `sh.splitFind()`, the sharded collection must be
populated.

## Example

For the sharded collection `test.foo`, the following example splits,
at the median point, a chunk that contains the shard key value ``x:
70``.

```javascript
sh.splitFind( "test.foo", { x: 70 } )
```
