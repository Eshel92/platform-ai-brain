<!-- Converted from reference/method/db.revokePrivilegesFromRole.txt (reStructuredText). Includes are inlined. -->

# db.revokePrivilegesFromRole()

## Definition

**`db.revokePrivilegesFromRole(rolename, privileges, writeConcern)`**

Removes the specified privileges from the user-defined role on the database where the method runs. 

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `revokePrivilegesFromRole` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `db.revokePrivilegesFromRole` method has the following syntax:

```javascript
db.revokePrivilegesFromRole(
    "<rolename>",
    [
        { resource: { <resource> }, actions: [ "<action>", ... ] },
        ...
    ],
    { <writeConcern> }
)
```

The `db.revokePrivilegesFromRole` method takes the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `rolename` | string | The name of the user-defined role from which to revoke privileges. |
| `privileges` | array | An array of privileges to remove from the role.  See `privileges` for more information on the format of the privileges. |
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

### Replica set

If run on a replica set, `db.revokePrivilegesFromRole()` is executed using
`"majority"` write concern by default.

### Scope

To revoke a privilege, the resource document pattern must match **exactly** the
`resource` field of that privilege. The `actions` field can be a
subset or match exactly.

For example, given the role `accountRole` in the `products`
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
db.revokePrivilegesFromRole(
   "accountRole",
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
)

db.revokePrivilegesFromRole(
   "accountRole",
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
)
```

To revoke the `"find"` and/or the `"update"` action from the role
`accountRole`, you must match the resource document exactly. For
example, the following operation revokes just the `"find"` action
from the existing privilege.

```javascript
use products
db.revokePrivilegesFromRole(
   "accountRole",
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
)
```

### Privileges

When you specify the `privileges` array, you can specify privileges to apply to
multiple collections in a database or to an entire database.

The following syntax specifies privileges on multiple collections in the
`products` database. 

```javascript
privileges: [
     {
     resource: { db: 'products', collection: 'coll1' },
     actions: [ 'bypassDocumentValidation' ]
     },
     {
     resource: { db: 'products', collection: 'coll2' },
     actions: [ 'bypassDocumentValidation' ]
     }     
]
```

The following syntax specifies privileges on all collections in the
`products` database. 

```javascript
privileges: [
     {
     resource: { db: 'products', collection: '' },
     actions: [ 'bypassDocumentValidation' ]
     }
]
```

## Required Access

You must have the `revokeRole` action on the database a privilege targets in order to
revoke that privilege. If the privilege targets multiple databases or the
`cluster` resource, you must have the `revokeRole` action
on the `admin` database.

## Example

The following operation removes multiple privileges from the
`associates` role:

```javascript
db.revokePrivilegesFromRole(
   "associate",
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
   { w: "majority" }
)
```
