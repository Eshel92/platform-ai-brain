<!-- Converted from reference/inconsistency-type/MissingShardKeyIndex.txt (reStructuredText). Includes are inlined. -->

# MissingShardKeyIndex

## Description

**`MissingShardKeyIndex`**

A sharded collection exists that doesn't have an index compatible with the
collection shard key.

**New in version:** 7.0

## Format

```json
{
   type: "MissingShardKeyIndex",
   description: "<string>",
   details: {
      namespace: "<string>",
      shard: "<string>",
      shardKey: { <document> }
   }
}
```

`MissingShardKeyIndex` inconsistency documents contain the following fields:

| Field | Type | Description |
|---|---|---|
| `type` | string | .. include:: /includes/inconsistency-type/type |
| `description` | string | .. include:: /includes/inconsistency-type/descr |
| `details` | document | .. include:: /includes/inconsistency-type/details |
| `details.namespace` | string | .. include:: /includes/inconsistency-type/details.namespace |
| `details.shard` | string | .. include:: /includes/inconsistency-type/details.shard |
| `details.shardKey` | document | The shard key that requires an index. |

## Example

Use the `db.adminCommand` method to call the 
`checkMetadataConsistency` command:

```javascript
db.adminCommand( { checkMetadataConsistency: 1 } )
```

The method returns a cursor with a batch of documents showing the inconsistencies
found in the sharding metadata.  The example below shows a cursor with
a `MissingShardKeyIndex` inconsistency document:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "MissingShardKeyIndex",
            description: "Found sharded collection without a shard key index",
            details: {
               namespace: "test.authors",
               shard: "shard-rs0",
               shardKey: { 
                  skey: 1
               }
            }
         }
      ],
   },
   ok: 1
}
```
