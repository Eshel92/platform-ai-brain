<!-- Converted from reference/method/sh.moveRange.txt (reStructuredText). Includes are inlined. -->

# sh.moveRange() (mongosh method)

## Definition

**`sh.moveRange(namespace, toShard, min, max)`**

**New in version:** 6.0

Moves ranges between shards.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `moveRange` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

```none
sh.moveRange(namespace, toShard, min, max)
```

The `sh.moveRange()` method takes the following parameters:

| Parameter | Type | Description |
|---|---|---|
| `namespace` | string | Sets the database and collection of the range to move. |
| `toShard` | string | Sets the ID of the shard to receive the range. |
| `min` | document | Minimum key of the range to move. |
| `max` | document | Maximum key of the range to move. |

## Example

The following example uses a collection with:

- Shard key `postal`, representing a postal code. 

- A range with the boundaries `70007` and `70124`.

To move the postal range to `shard02`, run the following
method:

```javascript
sh.moveRange(
   "contacts.addresses", "shard02", 
   { postal: 70007 },
   { postal: 70124 }
)
```

Output:

```javascript
{
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1742507819, i: 42 }),
    signature: {
      hash: Binary.createFromBase64('AAAAAAAAAAAAAAAAAAAAAAAAAAA=', 0),
      keyId: Long('0')
    }
  },
  operationTime: Timestamp({ t: 1742507819, i: 42 })
}
```
