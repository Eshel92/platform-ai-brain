<!-- Converted from reference/method/Bulk.find.delete.txt (reStructuredText). Includes are inlined. -->

# Bulk.find.delete()

## Definition

**`Bulk.find.delete()`**

Adds a multiple document delete operation to a bulk operations list.
Use the `Bulk.find()` method to specify the condition that
determines which documents to remove. 

`Bulk.find.delete()` deletes all matching documents. To remove the
first matching document, see `Bulk.find.deleteOne()`.

## Compatibility

This command is available in deployments hosted in the following
environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

## Syntax

The command has the following syntax:

```javascript
Bulk.find( <filter document> ).delete()
```

For details on the `find()` method see: `Bulk.find()`

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
bulk.find( { "genre": "pop" } ).delete();
bulk.execute()
```

To delete only the first matching document, use
`Bulk.find.deleteOne()` instead.
