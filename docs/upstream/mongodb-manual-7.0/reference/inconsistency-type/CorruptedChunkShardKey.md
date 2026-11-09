<!-- Converted from reference/inconsistency-type/CorruptedChunkShardKey.txt (reStructuredText). Includes are inlined. -->

# CorruptedChunkShardKey

## Description

**`CorruptedChunkShardKey`**

The routing table contains a chunk with a min key or max key that doesn't
correspond to the collection shard key.

**New in version:** 7.0

## Format

```json
{
   type: "CorruptedChunkShardKey",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionUUID: UUID("<uuid>"),
      chunk: <chunk>,
      shardKeyPattern: <pattern>
   }
}
```

`CorruptedChunkShardKey` inconsistency documents contain the following fields:

| Field | Type | Description |
|---|---|---|
| `type` | string | .. include:: /includes/inconsistency-type/type |
| `description` | string | .. include:: /includes/inconsistency-type/descr |
| `details` | document | .. include:: /includes/inconsistency-type/details |
| `details.namespace` | string | .. include:: /includes/inconsistency-type/details.namespace |
| `details.collectionUUID` | UUID | UUID of the collection with the corrupted chunk shard key. |
| `details.chunk` | document | Chunk with the corrupted shard key. |
| `details.shardKeyPattern` | document | .. include:: /includes/inconsistency-type/details.shardKeyPattern |

     

## Example

Use the `db.adminCommand` method to call the 
`checkMetadataConsistency` command:

```javascript
db.adminCommand( { checkMetadataConsistency: 1 } )
```

The method returns a cursor with a batch of documents showing the inconsistencies
found in the sharding metadata.  The example below shows a cursor with
a `CorruptedChunkShardKey` inconsistency document:

```json
{ 
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [ 
         {
            type: "CorruptedChunkShardKey",
            description: "Found chunk with a shard key pattern violation",
            details: {
               namespace: "test.authors",
               collectionUUID : new UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4"),
               chunk: { 
                  _id: ObjectId("64ddd81656be208c6685da1b"),
                  uuid: new UUID("de934e0a-74d2-412b-9bb8-409abe9754e3"),
                  min: { 
                     y: 0 
                  }, 
                  max: { 
                     x: MaxKey 
                  }, 
                  shard: "shard0000", 
                  lastmod: Timestamp(1, 0),
                  onCurrentShardSince: Timestamp(1, 0), 
                  history: [ 
                     { 
                        validAfter: Timestamp(1, 0), 
                        shard: "shard0000" 
                     } 
                  ]
               },
               shardKeyPattern: { 
                  x: 1 
               }
            }
         }
      ],
   },
   ok: 1
}
```
