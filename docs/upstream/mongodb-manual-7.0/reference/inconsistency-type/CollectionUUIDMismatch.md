<!-- Converted from reference/inconsistency-type/CollectionUUIDMismatch.txt (reStructuredText). Includes are inlined. -->

# CollectionUUIDMismatch

## Description

**`CollectionUUIDMismatch`**

A collection exists on a shard with a locally registered UUID that differs from
the one registered in the `config.collections` cluster catalog.

**New in version:** 7.0

## Format

```json
{
   type: "CollectionUUIDMismatch",
   description: "<string>",
   details: {
      namespace: "<string>",
      shard: "<string>",
      localUUID: UUID("<uuid>"),
      uuid: UUID("<uuid>")
   }
}
```

`CollectionUUIDMismatch` inconsistency documents contain the following fields:

| Field | Type | Description |
|---|---|---|
| `type` | string | .. include:: /includes/inconsistency-type/type |
| `description` | string | .. include:: /includes/inconsistency-type/descr |
| `details` | document | .. include:: /includes/inconsistency-type/details |
| `details.namespace` | string | .. include:: /includes/inconsistency-type/details.namespace |
| `details.shard` | string | .. include:: /includes/inconsistency-type/details.shard |
| `details.localUUID` | UUID | The UUID registered locally on the shard. |
| `details.uuid` | UUID | The UUID of the collection found in the `config.collections` cluster catalog. |

## Example

Use the `db.adminCommand` method to call the 
`checkMetadataConsistency` command:

```javascript
db.adminCommand( { checkMetadataConsistency: 1 } )
```

The method returns a cursor with a batch of documents showing the inconsistencies
found in the sharding metadata.  The example below shows a cursor with
a `CollectionUUIDMismatch` inconsistency document:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "CollectionUUIIDMismatch",
            description: "Found collection on non primary shard with mismatching UUID",
            details: {
               namespace: "test.authors",
               shard: "shard02",
               localUUID: new UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4"),
               uuid: new UUID("a3153e8a-3544-43ec-928f-37f72b48dee9")
            }
         }
      ],
   },
   ok: 1
}
```
