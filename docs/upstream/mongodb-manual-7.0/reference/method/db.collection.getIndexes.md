<!-- Converted from reference/method/db.collection.getIndexes.txt (reStructuredText). Includes are inlined. -->

# db.collection.getIndexes() (mongosh method)

(Include not available offline: includes/wayfinding/mongosh-method-getIndexes.rst)

## Definition

**`db.collection.getIndexes()`**

Returns an array that holds a list of documents that identify and
describe the existing indexes on the collection, including
hidden indexes and indexes that are currently being built. 

You must call
`db.collection.getIndexes()` on a collection. For example:

```javascript
db.collection.getIndexes()
```

Change `collection` to the name of the collection for which to
return index information.

## Compatibility

This method is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

### Atlas Search Indexes

`getIndexes()` does not return information on Atlas Search indexes. For information on Atlas 
Search indexes, use `$listSearchIndexes`.

### Client Disconnection

If the client that issued `db.collection.getIndexes()` disconnects before the operation 
completes, MongoDB marks `db.collection.getIndexes()` for termination using 
`killOp`.

### Replica Set Member State Restriction

To run on a replica set member, `listIndexes` operations require the member 
to be in `PRIMARY` or `SECONDARY` state. If the member
is in another state, such as `STARTUP2`, the
operation errors.

### Wildcard Indexes

Starting in MongoDB 6.3, 6.0.5, and 5.0.16, the `wildcardProjection`
field stores the index projection in its submitted form. Earlier
versions of the server may have stored the projection in a normalized
form.

The server uses the index the same way, but you may notice a difference
in the output of the `listIndexes` and
`db.collection.getIndexes()` commands.

## Required Access

To run `db.collection.getIndexes()` when access control is
enforced, users must have privileges to `listIndexes` on the
collection. 

The built-in role `read` provides the required privileges to
run `db.collection.getIndexes()` for the collections in a
database.

## Output

`db.collection.getIndexes()` returns an array of documents that
hold index information for the collection. For example:

```javascript
[
   {
      "v" : 2,
      "key" : {
         "_id" : 1
      },
      "name" : "_id_"
   },
   {
      "v" : 2,
      "key" : {
         "status" : 1
      },
      "name" : "status_1"
   },
   {
      "v" : 2,
      "key" : {
         "points" : 1
      },
      "name" : "points_1"
   }
]
```

Index information includes the keys and options used to create the
index. The index option `hidden` is only available if the value is `true`.

For information on the keys and index options, see
`db.collection.createIndex()`.
