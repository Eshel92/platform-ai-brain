<!-- Converted from reference/method/Bulk.find.deleteOne.txt (reStructuredText). Includes are inlined. -->

# Bulk.find.deleteOne()

## Definition

**`Bulk.find.deleteOne()`**

Adds a single document remove operation to a bulk operations list.
Use the `Bulk.find()` method to specify the condition that
determines which document to remove. 

`Bulk.find.deleteOne()` only deletes the first matching document.
To remove multiple documents, see `Bulk.find.delete()`.

## Syntax

The command has the following syntax:

```javascript
Bulk.find( <filter document> ).deleteOne()
```

For details on the `find()` method see: `Bulk.find()`

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
bulk.find( { "genre": "pop" } ).deleteOne();
bulk.execute()
```

To delete all `"pop"` music, use `Bulk.find.delete()` instead.
