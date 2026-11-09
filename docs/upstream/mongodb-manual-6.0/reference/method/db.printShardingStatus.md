<!-- Converted from reference/method/db.printShardingStatus.txt (reStructuredText). Includes are inlined. -->

# db.printShardingStatus()

## Definition

**`db.printShardingStatus()`**

Prints a formatted report of the sharding configuration and the
information regarding existing chunks in a sharded cluster.

Only use `db.printShardingStatus()` when connected to a
`mongos` instance.

The `db.printShardingStatus()` method has the following
parameter:

* - Parameter

  - Type

  - Description

* - `verbose`

  - boolean

  - Optional. Determines the level of verbosity.

    If `true`, the method displays:

    - Full details of the chunk distribution across shards even if
      you have 20 or more chunks, as well as the number of chunks
      on each shard.

    - Details of active mongos instances.

    If `false`, the method displays:

    - Full details of the chunk distribution across shards only if
      you have less than 20 chunks. If you have 20 or more chunks,
      the method instead returns a `too many chunks to print ...`
      message, showing only the number of chunks on each shard.

    - Only the version and number of active mongos
      instances.

    The default verbose value is `false`.

See /reference/method/sh.status for details of the output.

**Note:**

The `db.printShardingStatus()` method run in `mongosh` does
**not** return JSON. Use `db.printShardingStatus()` for manual inspection, and
/reference/config-database/ in scripts.

**See also:**

`sh.status()`

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
