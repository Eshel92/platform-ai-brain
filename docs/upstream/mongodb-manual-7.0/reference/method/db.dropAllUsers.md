<!-- Converted from reference/method/db.dropAllUsers.txt (reStructuredText). Includes are inlined. -->

# db.dropAllUsers() (mongosh method)

## Definition

**`db.dropAllUsers(writeConcern)`**

Removes all users from the current database.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `dropAllUsersFromDatabase` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

**Warning:**

The `db.dropAllUsers` method removes all users from the
database.

The `db.dropAllUsers` method takes the following arguments:

| Field | Type | Description |
|---|---|---|
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |

The `db.dropAllUsers()` method wraps the
`dropAllUsersFromDatabase` command.

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

If run on a replica set, `db.dropAllUsers()` is executed using
`"majority"` write concern by default.

## Required Access

You must have the `dropUser` action on a database to drop a user from that database.

## Example

The following `db.dropAllUsers()` operation drops every user from
the `products` database.

```javascript
use products
db.dropAllUsers( {w: "majority", wtimeout: 5000} )
```

The `n` field in the results document shows the number of users
removed:

```javascript
{ "n" : 12, "ok" : 1 }
```
