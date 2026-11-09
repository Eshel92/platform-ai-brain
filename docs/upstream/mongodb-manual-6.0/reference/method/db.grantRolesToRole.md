<!-- Converted from reference/method/db.grantRolesToRole.txt (reStructuredText). Includes are inlined. -->

# db.grantRolesToRole()

## Definition

**`db.grantRolesToRole(rolename, roles, writeConcern)`**

Grants roles to a user-defined role.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `grantRolesToRole` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `db.grantRolesToRole()` method uses the following syntax:

```javascript
db.grantRolesToRole( "<rolename>", [ <roles> ], { <writeConcern> } )
```

The `db.grantRolesToRole()` method takes the following
arguments:

| Parameter | Type | Description |
|---|---|---|
| `rolename` | string | The name of the role to which to grant sub roles. |
| `roles` | array | An array of roles from which to inherit. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |

In the `roles` field, you can specify both
built-in roles and user-defined
roles.

To specify a role that exists in the same database where
`db.grantRolesToRole()` runs, you can either specify the role with the name of
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

If run on a replica set, `db.grantRolesToRole()` is executed using
`"majority"` write concern by default.

### Scope

A role can inherit privileges from other roles in its database. A role
created on the `admin` database can inherit privileges from roles in
any database.

## Required Access

You must have the `grantRole` action on a database to grant a role on that database.

## Example

The following `db.grantRolesToRole()` operation updates the
`productsReaderWriter` role in the `products` database to inherit the privileges of `productsReader` role:

```javascript
use products
db.grantRolesToRole(
    "productsReaderWriter",
    [ "productsReader" ],
    { w: "majority" , wtimeout: 5000 }
)
```
