<!-- Converted from reference/inconsistency-type/RoutingTableMissingMinKey.txt (reStructuredText). Includes are inlined. -->

# RoutingTableMissingMinKey

## Description

**`RoutingTableMissingMinKey`**

A range gap exists in the routing table. The first chunk does not start from
the minimum key value.

**New in version:** 7.0

## Format

```json
{
   type: "RoutingTableMissingMinKey",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionUUID: <string>,
      minKeyObj: { <document> },
      globalMin: { <document> }
   }
}
```

`RoutingTableMissingMinKey` inconsistency documents contain the following fields:

| Field | Type | Description |
|---|---|---|
| `type` | string | .. include:: /includes/inconsistency-type/type |
| `description` | string | .. include:: /includes/inconsistency-type/descr |
| `details` | document | .. include:: /includes/inconsistency-type/details |
| `details.namespace` | string | .. include:: /includes/inconsistency-type/details.namespace |
| `details.collectionUUID` | UUID | .. include:: /includes/inconsistency-type/details.collectionUUID |
| `details.minKeyObj` | document | The minimum key used by the collection. |
| `details.globalMin` | document | The expected minimum key of the collection. |

## Example

Use the `db.adminCommand` method to call the 
`checkMetadataConsistency` command:

```javascript
db.adminCommand( { checkMetadataConsistency: 1 } )
```

The method returns a cursor with a batch of documents showing the inconsistencies
found in the sharding metadata.  The example below shows a cursor with
a `RoutingTableMissingMinKey` inconsistency document:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "RoutingTableMissingMinKey",
            description: "Routing table has a gap because first chunk does not start from MinKey",
            details: {
               namespace: "test.authors",
               collectionUUID: new UUID("62ebdb7e-a7bb-4151-a620-49d44cef097f"),
               minKeyObj: { 
                  x: 0 
               },
               globalMin: { 
                  x: MinKey 
               }
            }
         }
      ],
   },
   ok: 1
}
```
