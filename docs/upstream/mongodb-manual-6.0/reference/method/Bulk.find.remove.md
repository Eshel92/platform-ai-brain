<!-- Converted from reference/method/Bulk.find.remove.txt (reStructuredText). Includes are inlined. -->

# Bulk.find.remove()

**Tip:**

MongoDB also provides the `db.collection.bulkWrite()` method for 
performing bulk write operations.

## Description

**`Bulk.find.remove()`**

Starting in `mongosh` 0.12.2, `Bulk.find.remove()` is an alias
for `Bulk.find.delete()`.

In new code, use `Bulk.find.delete()` instead of
`Bulk.find.remove()`.

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
- Deletes `pop` music from the collection. 

```javascript
var bulk = db.music.initializeOrderedBulkOp();
bulk.find( { "genre": "pop" } ).remove();
bulk.execute()
```
