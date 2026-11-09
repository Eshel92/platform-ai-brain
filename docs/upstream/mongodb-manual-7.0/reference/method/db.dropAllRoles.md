<!-- Converted from reference/method/db.dropAllRoles.txt (reStructuredText). Includes are inlined. -->

# db.dropAllRoles() (mongosh method)

## Definition

**`db.dropAllRoles( writeConcern )`**

Deletes all user-defined roles on the
database where you run the method.

**Warning:**

The `db.dropAllRoles()` method removes *all*
user-defined roles from the database.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `dropAllRolesFromDatabase` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `db.dropAllRoles()` method takes the following argument:

| Field | Type | Description |
|---|---|---|
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |

:returns:
   The number of user-defined roles dropped.

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

If run on a replica set, `db.dropAllRoles()` is executed using
`"majority"` write concern by default.

## Required Access

You must have the `dropRole` action on a database to drop a role from that database.

## Example

The following operations drop all user-defined roles from the `products` database and uses a
write concern of `majority`.

```javascript
use products
db.dropAllRoles( { w: "majority" } )
```

The method returns the number of roles dropped:

```javascript
4
```
