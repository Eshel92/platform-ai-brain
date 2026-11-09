<!-- Converted from reference/command/listIndexes.txt (reStructuredText). Includes are inlined. -->

# listIndexes (database command)

## Definition

**`listIndexes`**

Returns information about the indexes on the specified collection, including
hidden indexes and indexes that are currently being built. 
Returned index information includes the keys and options used to create the index. 
You can optionally set the batch size for the first batch of results. 

**Tip:**

In `mongosh`, this command can also be run through the `db.collection.getIndexes()` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

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

## Syntax

The command has the following syntax:

```javascript
db.runCommand ( 
   {
      listIndexes: "<collection-name>", 
      cursor: { batchSize: <int> },
      comment: <any>
   } 
)
```

## Command Fields

The command takes the following fields: 

| Field | Type | Description |
|---|---|---|
| `listIndexes` | string | The name of the collection. |
| `cursor.batchSize` | integer | Optional. Specifies the cursor batch size. |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst Any comment set on a `listIndexes` command is inherited by any subsequent `getMore` commands run on the `listIndexes` cursor. |

## Required Access

If access control is enforced, the built-in `read` role provides the 
required privileges to run `listIndexes` for the collections in a 
database.

## Behavior

### Atlas Search Indexes

`listIndexes` does not return information on Atlas Search indexes. Instead, use 
`$listSearchIndexes`.

### Client Disconnection

If the client that issued `listIndexes` disconnects before the operation 
completes, MongoDB marks `listIndexes` for termination using 
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

## Output

**`listIndexes.cursor`**

A result set returned in the batch size specified by your cursor. 
Each document in the batch output contains the following fields:

| Field | Type | Description |
|---|---|---|
| id | integer | A 64-bit integer. If zero, there are no more batches of information. If non-zero, a cursor ID, usable in a `getMore` command to get the next batch of index information. |
| ns | string | The database and collection name in the following format: `<database-name>.<collection-name>` |
| firstBatch | document | Index information includes the keys and options used to create the index. The index option hidden is only present if the value is true. Use `getMore` to retrieve additional results as needed. |

**`listIndexes.ok`**

The return value for the command. A value of `1` indicates success.

## Examples

### List Database Indexes

This example lists indexes for the `contacts` collection without specifying the 
cursor batch size.

```json
db.runCommand ( 
  { 
     listIndexes: "contacts"
  } 
) 
```

Output:

```
{
   cursor: {
      id: Long("0"),
      ns: 'test.contacts',
      firstBatch: [
         { v: 2, key: { _id: 1 }, name: '_id_', ns: 'test.contacts' },
         { v: 2, key: { a: 1 }, name: 'a_1', ns: 'test.contacts' }
      ]
   },
   ok: 1
}
```

### Specify Result Batch Size

This example lists indexes for the `contacts` collection, and specifies a cursor 
batch size of 1. 

```json
db.runCommand ( 
   {
      listIndexes: "contacts", cursor: { batchSize: 1 }
   }
)
```

Output:

```
{
   cursor: {
     id: Long("4809221676960028307"),
     ns: 'test.contacts',
    firstBatch: [ { v: 2, key: { _id: 1 }, name: '_id_', ns: 'test.contacts' } ]
  },
  ok: 1
}
```

### Retrieve Additional Results

This example uses `getMore` to retrieve additional result batches from the 
`contacts` collection. 

```json
db.runCommand( 
   { 
      getMore: Long("4809221676960028307"), collection: "contacts"
   } 
)
```

Output:

```
{
   cursor: {
    nextBatch: [ { v: 2, key: { a: 1 }, name: 'a_1', ns: 'test.contacts' } ],
    id: Long("0"),
    ns: 'test.contacts'
  },
  ok: 1
}
```
