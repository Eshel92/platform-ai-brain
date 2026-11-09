<!-- Converted from reference/inconsistency-type/MissingRoutingTable.txt (reStructuredText). Includes are inlined. -->

# MissingRoutingTable

## Description

**`MissingRoutingTable`**

A sharded collection exists without a routing table.

**New in version:** 7.0

## Format

```json
{
   type: "MissingRoutingTable",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionUUID <uuid>
   }
}
```

`MissingRoutingTable` inconsistency documents contain the following fields:

| Field | Type | Description |
|---|---|---|
| `type` | string | .. include:: /includes/inconsistency-type/type |
| `description` | string | .. include:: /includes/inconsistency-type/descr |
| `details` | document | .. include:: /includes/inconsistency-type/details |
| `details.namespace` | string | .. include:: /includes/inconsistency-type/details.namespace |
| `details.collectionUUID` | UUID | UUID of the collection without the routing table. |

## Example

Use the `db.adminCommand` method to call the 
`checkMetadataConsistency` command:

```javascript
db.adminCommand( { checkMetadataConsistency: 1 } )
```

The method returns a cursor with a batch of documents showing the inconsistencies
found in the sharding metadata.  The example below shows a cursor with
a `MissingRoutingTable` inconsistency document:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "MissingRoutingTable",
            description: "There is a sharded collection without routing table",
            details: {
               namespace: "test.authors",
               collectionUUID: new UUID("1ad56770-61e2-48e9-83c6-8ecefe73cfc4")
            }
         }
      ],
   },
   ok: 1
}
```
