<!-- Converted from reference/inconsistency-type/RoutingTableMissingMaxKey.txt (reStructuredText). Includes are inlined. -->

# RoutingTableMissingMaxKey

## Description

**`RoutingTableMissingMaxKey`**

A range gap exists in the routing table. The last chunk boundary 
in the routing table does not reach the maximum key value.

**New in version:** 7.0

## Format

```json
{
   type: "RoutingTableMissingMaxKey",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionUUID: <string>,
      maxKeyObj: { <document> },
      globalMax: { <document> }
   }
}
```

`RoutingTableMissingMaxKey` inconsistency documents contain the following fields:

| Field | Type | Description |
|---|---|---|
| `type` | string | .. include:: /includes/inconsistency-type/type |
| `description` | string | .. include:: /includes/inconsistency-type/descr |
| `details` | document | .. include:: /includes/inconsistency-type/details |
| `details.namespace` | string | .. include:: /includes/inconsistency-type/details.namespace |
| `details.collectionUUID` | UUID | .. include:: /includes/inconsistency-type/details.collectionUUID |
| `details.maxKeyObj` | document | The max key used by the collection. |
| `details.globalMax` | document | The expected max key of the collection. |

## Example

Use the `db.adminCommand` method to call the 
`checkMetadataConsistency` command:

```javascript
db.adminCommand( { checkMetadataConsistency: 1 } )
```

The method returns a cursor with a batch of documents showing the inconsistencies
found in the sharding metadata.  The example below shows a cursor with
a `RoutingTableMissingMaxKey` inconsistency document:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "RoutingTableMissingMaxKey",
            description: "Routing table has a gap because last chunk boundary does not reach MaxKey",
            details: {
               namespace: "test.authors",
               collectionUUID: new UUID("62ebdb7e-a7bb-4151-a620-49d44cef097f"),
               maxKeyObj: { 
                  x: 0 
               },
               globalMax: { 
                  x: MaxKey 
               }
            }
         }
      ],
   },
   ok: 1
}
```
