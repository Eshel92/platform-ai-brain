<!-- Converted from reference/command/dropRole.txt (reStructuredText). Includes are inlined. -->

# dropRole

## Definition

**`dropRole`**

Deletes a user-defined role from the
database on which you run the command.

**Tip:**

In `mongosh`, this command can also be run through the `db.dropRole` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, M10+, and Flex clusters.
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
     dropRole: "<role>",
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

## Command Fields

The command has the following fields:

| Field | Type | Description |
|---|---|---|
| `dropRole` | string | The name of the user-defined role to remove from the database. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

## Behavior

### Authentication

When a role is dropped on a `mongod`, previously authenticated users 
remain logged in to the database but immediately lose the role's privileges.

When a role is dropped on a `mongos`, previously authenticated users 
remain logged in to the database but lose the role's privileges when the cache 
refreshes. The cache refreshes automatically after the time specified with the
`userCacheInvalidationIntervalSecs` parameter or manually when 
you run the `invalidateUserCache` command.

## Required Access

You must have the `dropRole` action on a database to drop a role from that database.

## Example

The following operations remove the `readPrices` role from the
`products` database:

```javascript
use products
db.runCommand(
   {
     dropRole: "readPrices",
     writeConcern: { w: "majority" }
   }
)
```
