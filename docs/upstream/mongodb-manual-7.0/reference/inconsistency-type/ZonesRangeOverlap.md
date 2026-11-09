<!-- Converted from reference/inconsistency-type/ZonesRangeOverlap.txt (reStructuredText). Includes are inlined. -->

# ZonesRangeOverlap

## Description

**`ZonesRangeOverlap`**

Overlapping zones exist for the same collection.

**New in version:** 7.0

## Format

```json
{
   type: "ZonesRangeOverlap",
   description: "<string>",
   details: {
      namespace: "<string>",
      collectionUUID: <string>,
      zoneA: {<document>},
      zoneB: {<document>}
   }
}
```

`ZonesRangeOverlap` inconsistency documents contain the following fields:

| Field | Type | Description |
|---|---|---|
| `type` | string | .. include:: /includes/inconsistency-type/type |
| `description` | string | .. include:: /includes/inconsistency-type/descr |
| `details` | document | .. include:: /includes/inconsistency-type/details |
| `details.namespace` | string | .. include:: /includes/inconsistency-type/details.namespace |
| `details.collectionUUID` | UUID | .. include:: /includes/inconsistency-type/details.collectionUUID |
| `details.zoneA` | document | The first zone that overlaps with the second zone. |
| `details.zoneB` | document | The second zone that overlaps with the first zone. |

## Example

Use the `db.adminCommand` method to call the 
`checkMetadataConsistency` command:

```javascript
db.adminCommand( { checkMetadataConsistency: 1 } )
```

The method returns a cursor with a batch of documents showing the inconsistencies
found in the sharding metadata.  The example below shows a cursor with
a `ZonesRangeOverlap` inconsistency document:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "ZonesRangeOverlap",
            description: "Found two overlapping zones",
            details: {
               namespace: "test.authors",
               collectionUUID: new UUID("62ebdb7e-a7bb-4151-a620-49d44cef097f"),
               zoneA: { 
                  ns: "test.authors", 
                  tag: "64ddec77e0d32b766bb8d5fe", 
                  min: { x: MinKey }, 
                  max: { x: 0 } 
               },
               zoneB: { 
                  ns: "test.authors", 
                  tag: "64ddec77e0d32b766bb8d5ff", 
                  min: { x: -10 }, 
                  max: { x: MaxKey }
               }
             }
          }
      ],
   },
   ok: 1
}
```
