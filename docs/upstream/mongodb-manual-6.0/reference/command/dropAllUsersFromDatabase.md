<!-- Converted from reference/command/dropAllUsersFromDatabase.txt (reStructuredText). Includes are inlined. -->

# dropAllUsersFromDatabase

## Definition

**`dropAllUsersFromDatabase`**

Removes all users from the database on which you run the
command.

**Tip:**

In `mongosh`, this command can also be run through the `db.dropAllUsers` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

**Warning:**

The `dropAllUsersFromDatabase` removes all users from the database.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {   
     dropAllUsersFromDatabase: 1,
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `dropAllUsersFromDatabase` | integer | Specify `1` to drop all the users from the current database. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

## Required Access

You must have the `dropUser` action on a database to drop a user from that database.

## Example

The following sequence of operations in `mongosh` drops
every user from the `products` database:

```javascript
use products
db.runCommand( { dropAllUsersFromDatabase: 1, writeConcern: { w: "majority" } } )
```

The `n` field in the results document shows the number of users
removed:

```javascript
{ "n" : 12, "ok" : 1 }
```
