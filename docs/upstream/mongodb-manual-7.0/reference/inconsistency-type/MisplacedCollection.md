<!-- Converted from reference/inconsistency-type/MisplacedCollection.txt (reStructuredText). Includes are inlined. -->

# MisplacedCollection

## Description

**`MisplacedCollection`**

Indicates that an unsharded collection exists on a shard that is not 
the primary shard.

**New in version:** 7.0

## Format

```json
{
   type: "MisplacedCollection",
   description: "<string>",
   details: {
      namespace: "<string>",
      shard: "<string>",
      localUUID: UUID("<uuid>")
   }
}
```

`MisplacedCollection` inconsistency documents contain the following fields:

| Field | Type | Description |
|---|---|---|
| `type` | string | .. include:: /includes/inconsistency-type/type |
| `description` | string | .. include:: /includes/inconsistency-type/descr |
| `details` | document | .. include:: /includes/inconsistency-type/details |
| `details.namespace` | string | .. include:: /includes/inconsistency-type/details.namespace |
| `details.shard` | string | .. include:: /includes/inconsistency-type/details.shard |
| `details.localUUID` | UUID | The local UUID of the misplaced collection. |

     

## Example

Use the `db.adminCommand` method to call the 
`checkMetadataConsistency` command:

```javascript
db.adminCommand( { checkMetadataConsistency: 1 } )
```

The method returns a cursor with a batch of documents showing the inconsistencies
found in the sharding metadata.  The example below shows a cursor with
a `MisplacedCollection` inconsistency document:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "MisplacedCollection",
            description: "Unsharded collection found on shard different from database primary shard",
            details: {
               namespace: "test.authors",
               shard: "shard02",
               localUUID: new UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4")
            }
         }
      ],
   },
   ok: 1
}
```
