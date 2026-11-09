<!-- Converted from reference/method/db.revokeRolesFromRole.txt (reStructuredText). Includes are inlined. -->

# db.revokeRolesFromRole() (mongosh method)

## Definition

**`db.revokeRolesFromRole(rolename, roles, writeConcern)`**

Removes the specified inherited roles from a role.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `revokeRolesFromRole` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `db.revokeRolesFromRole()` method uses the following syntax:

```javascript
db.revokeRolesFromRole( "<rolename>", [ <roles> ], { <writeConcern> } )
```

The `db.revokeRolesFromRole()` method takes the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `rolename` | string | The name of the role from which to revoke roles. |
| `roles` | array | The inherited roles to remove. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |

In the `roles` field, you can specify both
built-in roles and user-defined
roles.

To specify a role that exists in the same database where
`db.revokeRolesFromRole()` runs, you can either specify the role with the name of
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

If run on a replica set, `db.revokeRolesFromRole()` is executed using
`"majority"` write concern by default.

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

The following `db.revokeRolesFromRole()` operation on the `emea`
database removes two roles from the `purchaseAgents` role:

```javascript
use emea
db.revokeRolesFromRole( "purchaseAgents",
                        [
                          "writeOrdersCollection",
                          "readOrdersCollection"
                        ],
                        { w: "majority" , wtimeout: 5000 }
                      )
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
