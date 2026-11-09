<!-- Converted from reference/inconsistency-type/CorruptedZoneShardKey.txt (reStructuredText). Includes are inlined. -->

# CorruptedZoneShardKey

## Description

**`CorruptedZoneShardKey`**

The routing table contains a zone with a min key or max key that doesn't
correspond to the collection shard key.

**New in version:** 7.0

## Format

```json
{
   type: "CorruptedZoneShardKey",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionUUID: UUID("<uuid>"),
      zone: <zone>,
      shardKeyPattern: <pattern>
   }
}
```

`CorruptedZoneShardKey` inconsistency documents contain the following fields:

| Field | Type | Description |
|---|---|---|
| `type` | string | .. include:: /includes/inconsistency-type/type |
| `description` | string | .. include:: /includes/inconsistency-type/descr |
| `details` | document | .. include:: /includes/inconsistency-type/details |
| `details.namespace` | string | .. include:: /includes/inconsistency-type/details.namespace |
| `details.collectionUUID` | UUID | UUID of the collection with the corrupted zone shard key. |
| `details.zone` | document | Zone with the corrupted shard key. |
| `details.shardKeyPattern` | document | .. include:: /includes/inconsistency-type/details.shardKeyPattern |

## Example

Use the `db.adminCommand` method to call the 
`checkMetadataConsistency` command:

```javascript
db.adminCommand( { checkMetadataConsistency: 1 } )
```

The method returns a cursor with a batch of documents showing the inconsistencies
found in the sharding metadata.  The example below shows a cursor with
a `CorruptedZoneShardKey` inconsistency document:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [ 
         {
            type: "CorruptedZoneShardKey",
            description: "Found zone with a shard key pattern violation",
            details: { 
               namespace: "test.authors",
               collection: { 
                  collectionUUID : new UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4"),
                  zone : { 
                     ns : "test.authors",
                     tag: "64ddd81656be208c6685da21", 
                     min: { 
                        y: 0 
                     }, 
                     max: { 
                        x: MaxKey 
                     } 
                  }, 
                  shardKeyPattern: { 
                     x: 1 
                  }
               }
            }
         }
      ],
   },
   ok: 1
}
```
