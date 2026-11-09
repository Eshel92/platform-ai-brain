<!-- Converted from reference/method/db.grantRolesToUser.txt (reStructuredText). Includes are inlined. -->

# db.grantRolesToUser()

## Definition

**`db.grantRolesToUser(username, roles, writeConcern)`**

Grants additional roles to a user.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `grantRolesToUser` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `db.grantRolesToUser()` method uses the following syntax:

```javascript
db.grantRolesToUser( "<username>", [ <roles> ], { <writeConcern> } )
```

The `db.grantRolesToUser()` method takes the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `user` | string | The name of the user to whom to grant roles. |
| `roles` | array | An array of additional roles to grant to the user. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |

In the `roles` field, you can specify both
built-in roles and user-defined
roles.

To specify a role that exists in the same database where
`db.grantRolesToUser()` runs, you can either specify the role with the name of
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

The `db.grantRolesToUser()` method wraps the
`grantRolesToUser` command.

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

If run on a replica set, `db.grantRolesToUser()` is executed using
`"majority"` write concern by default.

## Required Access

You must have the `grantRole` action on a database to grant a role on that database.

## Example

Given a user `accountUser01` in the `products` database with the following
roles:

```javascript
"roles" : [
    { "role" : "assetsReader",
      "db" : "assets"
    }
]
```

The following `db.grantRolesToUser()` operation gives `accountUser01`
the `readWrite` role on the `products` database and the
`read` role on the `stock` database.

```javascript
use products
db.grantRolesToUser(
   "accountUser01",
   [ "readWrite" , { role: "read", db: "stock" } ],
   { w: "majority" , wtimeout: 4000 }
)
```

The user `accountUser01` in the `products` database now has the following
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
