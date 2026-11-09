<!-- Converted from reference/inconsistency-type/RoutingTableRangeGap.txt (reStructuredText). Includes are inlined. -->

# RoutingTableRangeGap

## Description

**`RoutingTableRangeGap`**

A range gap exists in the routing table between two consecutive chunks 
for the same collection.

**New in version:** 7.0

## Format

```json
{
   type: "RoutingTableRangeGap",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionUUID: <string>,
      chunkA: {<document>},
      chunkB: {<document>}
   }
}
```

`RoutingTableRangeGap` inconsistency documents contain the following fields:

| Field | Type | Description |
|---|---|---|
| `type` | string | .. include:: /includes/inconsistency-type/type |
| `description` | string | .. include:: /includes/inconsistency-type/descr |
| `details` | document | .. include:: /includes/inconsistency-type/details |
| `details.namespace` | string | .. include:: /includes/inconsistency-type/details.namespace |
| `details.collectionUUID` | UUID | .. include:: /includes/inconsistency-type/details.collectionUUID |
| `details.chunkA` | document | The first chunk that has a gap with the second chunk. |
| `details.chunkB` | document | The second chunk that has a gap with the first chunk. |

## Example

Use the `db.adminCommand` method to call the 
`checkMetadataConsistency` command:

```javascript
db.adminCommand( { checkMetadataConsistency: 1 } )
```

The method returns a cursor with a batch of documents showing the inconsistencies
found in the sharding metadata.  The example below shows a cursor with
a `RoutingTableRangeGap` inconsistency document:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "RoutingTableRangeGap",
            description: "Found a gap between two consecutive chunks",
            details: {
               namespace: "test.authors",
               collectionUUID: new UUID("62ebdb7e-a7bb-4151-a620-49d44cef097f"),
               chunkA: { 
                 _id: ObjectId("64dde749ac6045c92ef3b9ad"), 
                 uuid: new UUID("8c83ea89-ab6b-4ae4-91ab-813cf781284d"), 
                 min: { 
                    x: MinKey 
                 }, 
                 max: { 
                    x: 0 
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
               chunkB: { 
                  _id: ObjectId("64dde749ac6045c92ef3b9af"), 
                  uuid: new UUID("8c83ea89-ab6b-4ae4-91ab-813cf781284d"), 
                  min: { 
                     x: 10
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
               }
            }
         }
      ],
   },
   ok: 1
}
```
