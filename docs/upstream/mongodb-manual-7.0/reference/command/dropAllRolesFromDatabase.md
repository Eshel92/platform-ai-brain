<!-- Converted from reference/command/dropAllRolesFromDatabase.txt (reStructuredText). Includes are inlined. -->

# dropAllRolesFromDatabase (database command)

## Definition

**`dropAllRolesFromDatabase`**

Deletes all user-defined roles
on the database where you run the command.

**Warning:**

The `dropAllRolesFromDatabase` removes *all*
user-defined roles from the database.

**Tip:**

In `mongosh`, this command can also be run through the `db.dropAllRoles` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0 and Flex clusters.
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
     dropAllRolesFromDatabase: 1,
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

## Command Fields

The command has the following fields:

| Field | Type | Description |
|---|---|---|
| `dropAllRolesFromDatabase` | integer | Specify `1` to drop all user-defined roles from the database where the command is run. |
| `writeConcern` | document | /includes/source/fact-write-concern-spec-link.rst |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

## Required Access

You must have the `dropRole` action on a database to drop a role from that database.

## Example

The following operations drop all user-defined roles from the `products` database:

```javascript
use products
db.runCommand(
   {
     dropAllRolesFromDatabase: 1,
     writeConcern: { w: "majority" }
   }
)
```

The `n` field in the results document reports the number of roles
dropped:

```javascript
{ "n" : 4, "ok" : 1 }
```
