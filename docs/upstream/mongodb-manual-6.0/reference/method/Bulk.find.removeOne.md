<!-- Converted from reference/method/Bulk.find.removeOne.txt (reStructuredText). Includes are inlined. -->

# Bulk.find.removeOne()

**Tip:**

MongoDB also provides the `db.collection.bulkWrite()` method for 
performing bulk write operations.

## Description

**`Bulk.find.removeOne()`**

Starting in `mongosh` 0.12.2, `Bulk.find.removeOne()` is an alias
for `Bulk.find.deleteOne()`.

In new code, use `Bulk.find.deleteOne()` instead of
`Bulk.find.removeOne()`.

## Compatibility

This command is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

## Example

Create the `music` collection:

```javascript
db.music.insertMany( [
   { artist: "DOA", genre: "punk" },
   { artist: "Rick Astley", genre: "pop" },
   { artist: "Black Flag", genre: "punk" },
   { artist: "Justin Bieber", genre: "pop" }
] )
```

The following example:

- Initializes a `Bulk()` operations builder.
- Searches for the genre `pop`.
- Deletes `Rick Astley`, the first matching pop artist, from the
  collection. 

```javascript
var bulk = db.music.initializeOrderedBulkOp();
bulk.find( { "genre": "pop" } ).removeOne();
bulk.execute()
```
