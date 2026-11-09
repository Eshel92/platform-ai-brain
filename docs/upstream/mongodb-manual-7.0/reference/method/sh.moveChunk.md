<!-- Converted from reference/method/sh.moveChunk.txt (reStructuredText). Includes are inlined. -->

# sh.moveChunk() (mongosh method)

## Definition

**`sh.moveChunk(namespace, query, destination)`**

Moves the chunk that contains the document specified by the
`query` to the `destination` shard. `sh.moveChunk()`
provides a wrapper around the `moveChunk` database
command.

**Important:** In most circumstances, allow the balancer to

automatically migrate chunks, and avoid calling
`sh.moveChunk()` directly.

**Warning:**

This command cannot be used for hashed shard keys, as it 
uses the `find` option from the `moveChunk` command. 
To move a chunk with a hashed shard key, use the 
`moveChunk` command specifying the `bounds` field. 

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `moveChunk` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

`sh.moveChunk()` takes the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `namespace` | string | The namespace of the sharded collection that contains the chunk to migrate. |
| `query` | document | An equality match on the shard key that selects the chunk to move. |
| `destination` | string | The ID of the recipient shard. |

By default, MongoDB cannot move a chunk if the number of documents
in the chunk is greater than 2 times the result of dividing the
configured chunk size by the average
document size. The `moveChunk` command can specify the 
forceJumbo option to allow for the manual 
migration of chunks too large to move, with or without the 
jumbo label. See moveChunk 
command for details.

**See also:**

- `moveChunk`
- `sh.splitAt()`
- `sh.splitFind()`
- /sharding, and chunk migration

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

Given the `people` collection in the `records` database, the
following operation finds the chunk that contains the documents with the
`zipcode` field set to `53187` and then moves that chunk to the
shard named `shard0019`:

```javascript
sh.moveChunk("records.people", { zipcode: "53187" }, "shard0019")
```
