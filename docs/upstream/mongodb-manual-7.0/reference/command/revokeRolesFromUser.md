<!-- Converted from reference/command/revokeRolesFromUser.txt (reStructuredText). Includes are inlined. -->

# revokeRolesFromUser (database command)

## Definition

**`revokeRolesFromUser`**

Removes one or more roles from a user on the database where the
roles exist. 

**Tip:**

In `mongosh`, this command can also be run through the `db.revokeRolesFromUser` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**Important:**

This command is not supported in MongoDB Atlas clusters.
For information on Atlas support for all commands, 
see Unsupported Commands.

                

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   { 
     revokeRolesFromUser: "<user>",
     roles: [
       { role: "<role>", db: "<database>" } | "<role>",
       ...
     ],
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `revokeRolesFromUser` | string | The user to remove roles from. |
| `roles` | array | The roles to remove from the user. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

In the `roles` field, you can specify both
built-in roles and user-defined
roles.

To specify a role that exists in the same database where
`revokeRolesFromUser` runs, you can either specify the role with the name of
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

The following `revokeRolesFromUser` command removes the two of
the user's roles: the `read` role on the `stock` database and
the `readWrite` role on the `products` database, which is also
the database on which the command runs:

```javascript
use products
db.runCommand( { revokeRolesFromUser: "accountUser01",
                 roles: [
                          { role: "read", db: "stock" },
                          "readWrite"
                 ],
                 writeConcern: { w: "majority" }
             } )
```

The user `accountUser01` in the `products` database now has only one
remaining role:

```javascript
"roles" : [
    { "role" : "assetsReader",
      "db" : "assets"
    }
]
```
