<!-- Converted from reference/method/db.revokeRolesFromUser.txt (reStructuredText). Includes are inlined. -->

# db.revokeRolesFromUser()

## Definition

**`db.revokeRolesFromUser()`**

Removes one or more roles from a user on the current
database. 

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `revokeRolesFromUser` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `db.revokeRolesFromUser()` method uses the
following syntax:

```javascript
db.revokeRolesFromUser( "<username>", [ <roles> ], { <writeConcern> } )
```

The `db.revokeRolesFromUser()` method takes the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `user` | string | The name of the user from whom to revoke roles. |
| `roles` | array | The roles to remove from the user. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |

In the `roles` field, you can specify both
built-in roles and user-defined
roles.

To specify a role that exists in the same database where
`db.revokeRolesFromUser()` runs, you can either specify the role with the name of
the role:

```javascript
"readWrite"
```

Or you can specify the role with a document, as in:

```javascript
{ role: "<role>", db: "<database>" }
```

To specify a role that exists in a different database, specify the role
with a document.

The `db.revokeRolesFromUser()` method wraps the
`revokeRolesFromUser` command.

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

If run on a replica set, `db.revokeRolesFromUser()` is executed using
`"majority"` write concern by default.

## Required Access

You must have the `revokeRole` action on a database to revoke a role on that database.

## Example

The `accountUser01` user in the `products` database has the following
roles:

```javascript
"roles" : [
    { "role" : "assetsReader",
      "db" : "assets"
    },
    { "role" : "read",
      "db" : "stock"
    },
    { "role" : "readWrite",
      "db" : "products"
    }
]
```

The following `db.revokeRolesFromUser()` method removes the two of
the user's roles: the `read` role on the `stock` database and
the `readWrite` role on the `products` database, which is also
the database on which the method runs:

```javascript
use products
db.revokeRolesFromUser( "accountUser01",
                        [ { role: "read", db: "stock" }, "readWrite" ],
                        { w: "majority" }
                      )
```

The user `accountUser01` user in the `products` database now has only
one remaining role:

```javascript
"roles" : [
    { "role" : "assetsReader",
      "db" : "assets"
    }
]
```
