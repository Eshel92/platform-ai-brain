<!-- Converted from reference/ddl-operations.txt (reStructuredText). Includes are inlined. -->

# DDL Operations

DDL (Data Description Language) operations change the properties of a 
database or collection. MongoDB supports both 
explicit-ddl-operations and implicit-ddl-operations. 
Explicit DDL operations directly run an operation like creating or 
dropping a collection or index. Implicit DDL operations create 
collections by referencing a non-existent collection, like inserting 
data into a non-existent collection.

## Explicit DDL Operations

MongoDB supports the following explicit DDL operations:

- `cloneCollectionAsCapped`
- `collMod`
- `compactStructuredEncryptionData`
- `convertToCapped`
- `create`
- `createIndexes`
- `drop`
- `dropDatabase`
- `dropIndexes`
- `enableSharding`
- `movePrimary`
- `renameCollection`
- `refineCollectionShardKey`
- `reshardCollection`
- `shardCollection`

## Implicit DDL Operations

MongoDB also supports write operations such as `insert` or 
`update` with `upsert:true`. Any command that writes to a
non-existing collection creates that collection. 

### Examples

For example, this `insert` command creates the `users` collection
if it does not already exist.

```javascript
db.runCommand(
   {
      insert: "users",
      documents: [ { _id: 1, user: "abc123", status: "A" } ]
   }
)
```

This `update` command with `upsert: true` creates the `people`
collection if it does not already exist.

```javascript
db.runCommand(
   {
      update: "people",
      updates: [
        { q: { name: "Andy" }, u: { $inc: { score: 1 } }, upsert: true }
      ]
   }
)
```
