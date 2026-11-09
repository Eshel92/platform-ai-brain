<!-- Converted from reference/method/db.dropUser.txt (reStructuredText). Includes are inlined. -->

# db.dropUser()

## Definition

**`db.dropUser(username, writeConcern)`**

Removes the user from the current database.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `dropUser` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `db.dropUser()` method takes the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `username` | string | The name of the user to remove from the database. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |

The `db.dropUser()` method wraps the `dropUser`
command.

Before dropping a user who has the `userAdminAnyDatabase`
role, ensure you have at least another user with user administration
privileges.

## Compatibility

This method is available in deployments hosted in the following
environments:

**Important:**

This command is not supported in MongoDB Atlas clusters.
For information on Atlas support for all commands, 
see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

### Replica set

If run on a replica set, `db.dropUser()` is executed using
`"majority"` write concern by default.

## Required Access

You must have the `dropUser` action on a database to drop a user from that database.

## Example

The following `db.dropUser()` operation drops the `reportUser1`
user on the `products` database.

```javascript
use products
db.dropUser("reportUser1", {w: "majority", wtimeout: 5000})
```
