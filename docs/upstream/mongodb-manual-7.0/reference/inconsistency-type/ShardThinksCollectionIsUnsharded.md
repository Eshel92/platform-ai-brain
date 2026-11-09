<!-- Converted from reference/inconsistency-type/ShardThinksCollectionIsUnsharded.txt (reStructuredText). Includes are inlined. -->

# ShardThinksCollectionIsUnsharded

## Description

**`ShardThinksCollectionIsUnsharded`**

A shard thinks a sharded collection is unsharded.

**New in version:** 7.0

## Format

```json
{
   type: "ShardThinksCollectionIsUnsharded",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionUUID: <string>,
      shard: {<document>}
   }
}
```

`ShardThinksCollectionIsUnsharded` inconsistency documents contain the following fields:

| Field | Type | Description |
|---|---|---|
| `type` | string | .. include:: /includes/inconsistency-type/type |
| `description` | string | .. include:: /includes/inconsistency-type/descr |
| `details` | document | .. include:: /includes/inconsistency-type/details |
| `details.namespace` | string | .. include:: /includes/inconsistency-type/details.namespace |
| `details.collectionUUID` | UUID | .. include:: /includes/inconsistency-type/details.collectionUUID |
| `details.shard` | document | .. include:: /includes/inconsistency-type/details.shard |

## Example

Use the `db.adminCommand` method to call the 
`checkMetadataConsistency` command:

```javascript
db.adminCommand( { checkMetadataConsistency: 1 } )
```

The method returns a cursor with a batch of documents showing the inconsistencies
found in the sharding metadata.  The example below shows a cursor with
a `ShardThinksCollectionIsUnsharded` inconsistency document:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "ShardThinksCollectionIsUnsharded",
            description: "Shard thinks collection is unsharded while instead is currently sharded",
            details: {
               namespace: "test.authors",
               collectionUUID: new UUID("8c83ea89-ab6b-4ae4-91ab-813cf781284d"), 
               shard: "shard-rs0"
             }
          }
      ],
   },
   ok: 1
}
```
