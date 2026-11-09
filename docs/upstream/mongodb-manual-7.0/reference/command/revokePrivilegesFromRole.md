<!-- Converted from reference/command/revokePrivilegesFromRole.txt (reStructuredText). Includes are inlined. -->

# revokePrivilegesFromRole (database command)

## Definition

**`revokePrivilegesFromRole`**

Removes the specified privileges from the user-defined role on the database where the
command is run. 

**Tip:**

In `mongosh`, this command can also be run through the `db.revokePrivilegesFromRole` helper method.

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
     revokePrivilegesFromRole: "<role>",
     privileges: [
       { resource: { <resource> }, actions: [ "<action>", ... ] },
       ...
     ],
     writeConcern: <write concern document>,
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `revokePrivilegesFromRole` | string | The user-defined role to revoke privileges from. |
| `privileges` | array | An array of privileges to remove from the role.  See `privileges` for more information on the format of the privileges. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

## Behavior

To revoke a privilege, the resource document pattern must match **exactly** the
`resource` field of that privilege. The `actions` field can be a
subset or match exactly.

For example, consider the role `accountRole` in the `products`
database with the following privilege that specifies the `products`
database as the resource:

```javascript
{
  "resource" : {
      "db" : "products",
      "collection" : ""
  },
  "actions" : [
      "find",
      "update"
  ]
}
```

You *cannot* revoke `find` and/or `update` from just *one*
collection in the `products` database. The following operations
result in no change to the role:

```javascript
use products
db.runCommand(
    {
      revokePrivilegesFromRole: "accountRole",
      privileges:
        [
          {
            resource : {
                db : "products",
                collection : "gadgets"
            },
            actions : [
                "find",
                "update"
            ]
          }
        ]
    }
)

db.runCommand(
    {
      revokePrivilegesFromRole: "accountRole",
      privileges:
        [
          {
            resource : {
                db : "products",
                collection : "gadgets"
            },
            actions : [
                "find"
            ]
          }
        ]
    }
)
```

To revoke the `"find"` and/or the `"update"` action from the role
`accountRole`, you must match the resource document exactly. For
example, the following operation revokes just the `"find"` action
from the existing privilege.

```javascript
use products
db.runCommand(
    {
      revokePrivilegesFromRole: "accountRole",
      privileges:
        [
          {
            resource : {
                db : "products",
                collection : ""
            },
            actions : [
                "find"
            ]
          }
        ]
    }
)
```

## Required Access

You must have the `revokeRole` action on the database a privilege targets in order to
revoke that privilege. If the privilege targets multiple databases or the
`cluster` resource, you must have the `revokeRole` action
on the `admin` database.

## Example

The following operation removes multiple privileges from the
`associates` role in the `products` database:

```javascript
use products
db.runCommand(
   {
     revokePrivilegesFromRole: "associate",
     privileges:
      [
        {
          resource: { db: "products", collection: "" },
          actions: [ "createCollection", "createIndex", "find" ]
        },
        {
          resource: { db: "products", collection: "orders" },
          actions: [ "insert" ]
        }
      ],
     writeConcern: { w: "majority" }
   }
)
```
