<!-- Converted from reference/command/dropUser.txt (reStructuredText). Includes are inlined. -->

# dropUser

## Definition

**`dropUser`**

Removes the user from the database on which you run the command. 

**Tip:**

In `mongosh`, this command can also be run through the `db.dropUser` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M10+ clusters.
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
     dropUser: "<user>",
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

## Command Fields

The command has the following fields:

| Field | Type | Description |
|---|---|---|
| `dropUser` | string | The name of the user to delete. You must issue the `dropUser` command while using the database where the user exists. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

Before dropping a user who has the `userAdminAnyDatabase`
role, ensure you have at least another user with user administration
privileges.

## Required Access

You must have the `dropUser` action on a database to drop a user from that database.

## Example

The following sequence of operations in `mongosh` removes
`reportUser1` from the `products` database:

```javascript
use products
db.runCommand( { 
   dropUser: "reportUser1",
   writeConcern: { w: "majority", wtimeout: 5000 }
} )
```
