<!-- Converted from reference/command/killCursors.txt (reStructuredText). Includes are inlined. -->

# killCursors (database command)

## Definition

**`killCursors`**

Kills the specified cursor or cursors for a collection. MongoDB
drivers use the `killCursors` command as part of the
client-side cursor implementation.

**Warning:**

Applications typically should not run the `killCursors`
command directly. Instead, let the driver automatically
handle cursor management.

The `killCursors` command must be run against the database of the
collection whose cursors you wish to kill.

To run killCursors, use the `db.runCommand( { <command> } )` method.

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
db.runCommand( 
   { 
     killCursors: <collection>, 
     cursors: [ <cursor id1>, ... ], comment: <any> 
   } 
)
```

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `killCursors` | string | The name of the collection. |
| `cursors` | array | The ids of the cursors to kill. |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

## Required Access

### Kill Own Cursors

Users can always kill their own cursors regardless of whether they have
the `killCursors` privilege. Cursors are associated with the
users at the time of cursor creation.

### Kill Any Cursor

If a user has the `killAnyCursor` privilege, they can kill
cursors created by any user.

## `killCursors` and Transactions

You cannot specify the `killCursors` command as
the first operation in a transaction.

Additionally, if you run the `killCursors` command within a
transaction, the server immediately stops the specified
cursors. It does **not** wait for the transaction to commit.

## Example

Consider the following `find` operation on the
`test.restaurants` collection:

```javascript
use test
db.runCommand(
   { find: "restaurants",
     filter: { stars: 5 },
     projection: { name: 1, rating: 1, address: 1 },
     sort: { name: 1 },
     batchSize: 5
   }
)
```

which returns the following:

```javascript
{
   "waitedMS" : Long(0),
   "cursor" : {
      "firstBatch" : [
         {
            "_id" : ObjectId("57506d63f578028074723dfd"),
            "name" : "Cakes and more"
         },
         {
            "_id" : ObjectId("57506d63f578028074723e0b"),
            "name" : "Pies and things"
         },
         {
            "_id" : ObjectId("57506d63f578028074723e1d"),
            "name" : "Ice Cream Parlour"
         },
         {
            "_id" : ObjectId("57506d63f578028074723e65"),
            "name" : "Cream Puffs"
         },
         {
            "_id" : ObjectId("57506d63f578028074723e66"),
            "name" : "Cakes and Rolls"
         }
      ],
      "id" : Long("18314637080"),
      "ns" : "test.restaurants"
   },
   "ok" : 1
}
```

To kill this cursor, use the `killCursors` command.

```javascript
use test

db.runCommand( { killCursors: "restaurants", cursors: [ Long("18314637080") ] } )
```

`killCursors` returns the following operation details:

```javascript
{
   "cursorsKilled" : [
      Long("18314637080")
   ],
   "cursorsNotFound" : [ ],
   "cursorsAlive" : [ ],
   "cursorsUnknown" : [ ],
   "ok" : 1
}
```
