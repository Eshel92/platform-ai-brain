<!-- Converted from reference/inconsistency-type/HiddenShardedCollection.txt (reStructuredText). Includes are inlined. -->

# HiddenShardedCollection

## Description

**`HiddenShardedCollection`**

A collection is registered in the `config.collections` cluster catalog
under a non-existent database.

**New in version:** 7.0

## Format

```json
{
   type: "HiddenShardedCollection",
   description: "<string>",
   details: {
      namespace: "<string>",
      collection: "<object>",
   }
}
```

`HiddenShardedCollection` inconsistency documents contain the following fields:

| Field | Type | Description |
|---|---|---|
| `type` | string | .. include:: /includes/inconsistency-type/type |
| `description` | string | .. include:: /includes/inconsistency-type/descr |
| `details` | document | .. include:: /includes/inconsistency-type/details |
| `details.namespace` | string | .. include:: /includes/inconsistency-type/details.namespace |
| `details.collection` | document | .. include:: /includes/inconsistency-type/details.collection |

## Example

Use the `db.adminCommand` method to call the 
`checkMetadataConsistency` command:

```javascript
db.adminCommand( { checkMetadataConsistency: 1 } )
```

The method returns a cursor with a batch of documents showing the inconsistencies
found in the sharding metadata.  The example below shows a cursor with
a `HiddenShardedCollection` inconsistency document:

```json
{
   cursor: {
      id: Long("0"),
      ns: "test.$cmd.aggregate",
      firstBatch: [
         {
            type: "HiddenShardedCollection",
            description: "Found sharded collection but relative database does not exist",
            details: {
               namespace: "test.authors",
               collection: {
                   _id: "test.authors",
                   lastmodEpoch: ObjectId("64ddd78de906038182671674"),
                   lastmod: ISODate("2023-08-17T08:17:17.944Z"),
                   timestamp: Timestamp(1692260237, 58),
                   uuid: new UUID("69317741-7bc5-4eca-8877-7858cecf67d6"),
                   key: {
                      "skey" : 1
                   },
                   unique: false,
                   noBalance: false
                }
            }
         }
      ],
   },
   ok: 1
}
```
