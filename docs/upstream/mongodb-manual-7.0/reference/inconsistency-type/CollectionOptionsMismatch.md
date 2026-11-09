<!-- Converted from reference/inconsistency-type/CollectionOptionsMismatch.txt (reStructuredText). Includes are inlined. -->

# CollectionOptionsMismatch

## Description

**`CollectionOptionsMismatch`**

A collection contains mismatching options across different shards.

**New in version:** 7.0.23

## Format

```json
{
   type: "CollectionOptionsMismatch",
   description: "<string>",
   details: {
      namespace: "<string>",
      options: <array>
   }
}
```

`CollectionOptionsMismatch` inconsistency documents contain these fields:

| Field | Type | Description |
|---|---|---|
| `type` | string | .. include:: /includes/inconsistency-type/type.rst |
| `description` | string | .. include:: /includes/inconsistency-type/descr.rst |
| `details` | document | .. include:: /includes/inconsistency-type/details.rst |
| `details.namespace` | string | .. include:: /includes/inconsistency-type/details.namespace.rst |
| `details.options` | array | .. include:: /includes/inconsistency-type/details.options.rst |

## Example

Use the `db.adminCommand` method to call the 
`checkMetadataConsistency` command:

```javascript
db.adminCommand( { checkMetadataConsistency: 1 } )
```

The method returns a cursor with a batch of documents showing the inconsistencies
found in the sharding metadata.  The example below shows a cursor with
a `CollectionOptionsMismatch` inconsistency document:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "CollectionOptionsMismatch",
            description: "Found collection with mismatching options across shards and/or config server",
            details: {
               namespace: "test.authors",
               options: [ 
                  { "options": { "capped": true }, "shards": [ "shard0" ] },
                  { "options": { "capped": false }, "shards": [ "shard1", "config" ] }
               ]
            }
         }
      ],
   },
   ok: 1
}
```
