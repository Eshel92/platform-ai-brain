<!-- Converted from reference/method/db.dropRole.txt (reStructuredText). Includes are inlined. -->

# db.dropRole()

## Definition

**`db.dropRole( rolename, writeConcern )`**

Deletes a user-defined role from the
database on which you run the method.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `dropRole` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `db.dropRole()` method takes the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `rolename` | string | The name of the user-defined role to remove from the database. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |

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

### Authentication

When a role is dropped on a `mongod`, previously authenticated users 
remain logged in to the database but immediately lose the role's privileges.

When a role is dropped on a `mongos`, previously authenticated users 
remain logged in to the database but lose the role's privileges when the cache 
refreshes. The cache refreshes automatically after the time specified with the
`userCacheInvalidationIntervalSecs` parameter or manually when 
you run the `invalidateUserCache` command.

### Replica Set

If run on a replica set, `db.dropRole()` is executed using
`"majority"` write concern by default.

## Required Access

You must have the `dropRole` action on a database to drop a role from that database.

## Example

The following operations remove the `readPrices` role from the
`products` database:

```javascript
use products
db.dropRole( "readPrices", { w: "majority" } )
```
