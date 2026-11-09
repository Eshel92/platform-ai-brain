<!-- Converted from reference/inconsistency-type/InconsistentIndex.txt (reStructuredText). Includes are inlined. -->

# InconsistentIndex

## Description

**`InconsistentIndex`**

An index exists on two different shards that contains differing metadata or
a specific index is missing on some shards.

**New in version:** 7.0

## Format

```json
{
   type: "InconsistentIndex",
   description: "<string>",
   details: {
      namespace: "<string>",
      info: <document>
   }
}
```

`InconsistentIndex` inconsistency documents contain the following fields:

| Field | Type | Description |
|---|---|---|
| `type` | string | .. include:: /includes/inconsistency-type/type |
| `description` | string | .. include:: /includes/inconsistency-type/descr |
| `details` | document | .. include:: /includes/inconsistency-type/details |
| `details.namespace` | string | .. include:: /includes/inconsistency-type/details.namespace |
| `details.info` | document | Information on the inconsistent index. |

## Example

Use the `db.adminCommand` method to call the 
`checkMetadataConsistency` command:

```javascript
db.adminCommand( { 
   checkMetadataConsistency: 1,
   checkIndexes: true
} )
```

The method returns a cursor with a batch of documents showing the inconsistencies
found in the sharding metadata.  The example below shows a cursor with
a `InconsistentIndex` inconsistency document:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "InconsistentIndex",
            description: "Found an index of a sharded collection that is inconsistent between different shards",
            details: {
               namespace: "test.authors",
               info: {
                   missingFromShards: [
                      "shard-rs1"
                   ],
                   inconsistentProperties: [ ],
                   indexName: "index1"
               }
            }
         }
      ],
   },
   ok: 1
}
```
