<!-- Converted from reference/command/revokeRolesFromRole.txt (reStructuredText). Includes are inlined. -->

# revokeRolesFromRole (database command)

## Definition

**`revokeRolesFromRole`**

Removes the specified inherited roles from a role. 

**Tip:**

In `mongosh`, this command can also be run through the `db.revokeRolesFromRole` helper method.

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
     revokeRolesFromRole: "<role>",
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

The command has the following fields:

| Field | Type | Description |
|---|---|---|
| `revokeRolesFromRole` | string | The role from which to remove inherited roles. |
| `roles` | array | The inherited roles to remove. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

In the `roles` field, you can specify both
built-in roles and user-defined
roles.

To specify a role that exists in the same database where
`revokeRolesFromRole` runs, you can either specify the role with the name of
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

The `purchaseAgents` role in the `emea` database inherits privileges
from several other roles, as listed in the `roles` array:

```javascript
{
   "_id" : "emea.purchaseAgents",
   "role" : "purchaseAgents",
   "db" : "emea",
   "privileges" : [],
   "roles" : [
      {
         "role" : "readOrdersCollection",
         "db" : "emea"
      },
      {
         "role" : "readAccountsCollection",
         "db" : "emea"
      },
      {
         "role" : "writeOrdersCollection",
         "db" : "emea"
      }
   ]
}
```

The following `revokeRolesFromRole` operation on the `emea`
database removes two roles from the `purchaseAgents` role:

```javascript
use emea
db.runCommand( { revokeRolesFromRole: "purchaseAgents",
                 roles: [
                          "writeOrdersCollection",
                          "readOrdersCollection"
                        ],
                  writeConcern: { w: "majority" , wtimeout: 5000 }
             } )
```

The `purchaseAgents` role now contains just one role:

```javascript
{
   "_id" : "emea.purchaseAgents",
   "role" : "purchaseAgents",
   "db" : "emea",
   "privileges" : [],
   "roles" : [
      {
         "role" : "readAccountsCollection",
         "db" : "emea"
      }
   ]
}
```
