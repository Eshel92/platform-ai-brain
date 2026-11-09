<!-- Converted from reference/method/db.grantPrivilegesToRole.txt (reStructuredText). Includes are inlined. -->

# db.grantPrivilegesToRole()

## Definition

**`db.grantPrivilegesToRole(rolename, privileges, writeConcern)`**

Grants additional privileges to a user-defined role.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `grantPrivilegesToRole` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `db.grantPrivilegesToRole()` method uses the following syntax:

```javascript
db.grantPrivilegesToRole(
    "< rolename >",
    [
        { resource: { <resource> }, actions: [ "<action>", ... ] },
        ...
    ],
    { < writeConcern > }
)
```

The `db.grantPrivilegesToRole()` method takes the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `rolename` | string | The name of the role to grant privileges to. |
| `privileges` | array | The privileges to add to the role. For the format of a privilege, see `privileges`. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |

The `db.grantPrivilegesToRole()` method can grant one or more
privileges. Each `<privilege>` has the following syntax:

```javascript
{ resource: { <resource> }, actions: [ "<action>", ... ] }
```

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

If run on a replica set, `db.grantPrivilegesToRole()` is executed using
`"majority"` write concern by default.

### Scope

Except for roles created in the `admin` database, a role can only
include privileges that apply to its database 

A role created in the `admin` database can include privileges that
apply to the `admin` database, other databases or to the
cluster resource.

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

You must have the `grantRole` action on the database a privilege targets in order to
grant the privilege. To grant a privilege on multiple databases or on the
`cluster` resource, you must have the `grantRole` action on
the `admin` database.

## Example

The following `db.grantPrivilegesToRole()` operation grants two
additional privileges to the role `inventoryCntrl01`, which exists on the
`products` database. The operation is run on that database:

```javascript
use products
db.grantPrivilegesToRole(
  "inventoryCntrl01",
  [
    {
      resource: { db: "products", collection: "" },
      actions: [ "insert" ]
    },
    {
      resource: { db: "products", collection: "system.js" },
      actions: [ "find" ]
    }
  ],
  { w: "majority" }
)
```

The first privilege permits users with this role to perform the
`insert` action on all collections of
the `products` database, except the system collections. To access a system collection, a
privilege must explicitly specify the system collection in the resource
document, as in the second privilege.

The second privilege permits users with this role to perform the
`find` action on the
`product` database's system collection named `system.js
<`.
