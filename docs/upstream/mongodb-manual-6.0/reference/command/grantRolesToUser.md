<!-- Converted from reference/command/grantRolesToUser.txt (reStructuredText). Includes are inlined. -->

# grantRolesToUser

## Definition

**`grantRolesToUser`**

Grants additional roles to a user.

**Tip:**

In `mongosh`, this command can also be run through the `db.grantRolesToUser` helper method.

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

The `grantRolesToUser` command uses the following syntax:

```javascript
db.runCommand(
   {  
     grantRolesToUser: "<user>",
     roles: [ <roles> ],
     writeConcern: { <write concern> },
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `grantRolesToUser` | string | The name of the user to give additional roles. |
| `roles` | array | An array of additional roles to grant to the user. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

In the `roles` field, you can specify both
built-in roles and user-defined
roles.

To specify a role that exists in the same database where
`grantRolesToUser` runs, you can either specify the role with the name of
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

The following `grantRolesToUser` operation gives `accountUser01` the
`read` role on the `stock` database and the
`readWrite` role on the `products` database.

```javascript
use products
db.runCommand( { grantRolesToUser: "accountUser01",
                 roles: [
                    { role: "read", db: "stock"},
                    "readWrite"
                 ],
                 writeConcern: { w: "majority" , wtimeout: 2000 }
             } )
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
