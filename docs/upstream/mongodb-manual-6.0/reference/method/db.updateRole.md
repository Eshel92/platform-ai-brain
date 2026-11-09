<!-- Converted from reference/method/db.updateRole.txt (reStructuredText). Includes are inlined. -->

# db.updateRole()

## Definition

**`db.updateRole( rolename, update, writeConcern )`**

Updates a user-defined role. The
`db.updateRole()` method must run on the role's database.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `updateRole` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

An update to a field **completely replaces** the previous field's values.
To grant or remove roles or privileges without
replacing all values, use one or more of the following methods:

- `db.grantRolesToRole()`
- `db.grantPrivilegesToRole()`
- `db.revokeRolesFromRole()`
- `db.revokePrivilegesFromRole()`

**Warning:**

An update to the `privileges` or `roles` array completely replaces
the previous array's values.

The `db.updateRole()` method uses the following syntax:

```javascript
db.updateRole(
    "<rolename>",
    {
      privileges:
          [
            { resource: { <resource> }, actions: [ "<action>", ... ] },
            ...
          ],
      roles:
          [
            { role: "<role>", db: "<database>" } | "<role>",
            ...
          ],
      authenticationRestrictions:
          [
            {
              clientSource: ["<IP>" | "<CIDR range>", ...],
              serverAddress: ["<IP>", | "<CIDR range>", ...]
            },
            ...
          ]
    },
    { <writeConcern> }
)
```

The `db.updateRole()` method accepts the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `rolename` | string | The name of the user-defined role to update. |
| `update` | document | A document containing the replacement data for the role. This data completely replaces the corresponding data for the role. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |

The `update` document specifies the fields to update and the new
values. Each field in the `update` document is optional, but the
document must include at least one field. The `update` document has the
following fields:

| Field | Type | Description |
|---|---|---|
| `privileges` | array | Optional. Required if you do not specify `roles` array. The privileges to grant the role. An update to the `privileges` array overrides the previous array's values. For the syntax for specifying a privilege, see the `privileges` array. |
| `roles` | array | Optional. Required if you do not specify `privileges` array. The roles from which this role inherits privileges. An update to the `roles` array overrides the previous array's values. |
| `authenticationRestrictions` | array | Optional. The authentication restrictions the server enforces on the role. Specifies a list of IP addresses and CIDR (Classless Inter-Domain Routing) ranges users granted this role are allowed to connect to and/or which they can connect from. |

The `db.updateRole()` method wraps the `updateRole`
command.

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

### Roles

In the `roles` field, you can specify both
built-in roles and user-defined
roles.

To specify a role that exists in the same database where
`db.updateRole()` runs, you can either specify the role with the name of
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

### Authentication Restrictions

The `authenticationRestrictions` document can contain *only* the
following fields. The server throws an error if the 
`authenticationRestrictions` document contains an unrecognized field:

| Field Name | Value | Description |
|---|---|---|
| `clientSource` | Array of IP addresses and/or CIDR (Classless Inter-Domain Routing) ranges | If present, when authenticating a user, the server verifies that the client's IP address is either in the given list or belongs to a CIDR range in the list. If the client's IP address is not present, the server does not authenticate the user. |
| `serverAddress` | Array of IP addresses and/or CIDR (Classless Inter-Domain Routing) ranges | A list of IP addresses or CIDR ranges to which the client can connect. If present, the server will verify that the client's connection was accepted via an IP address in the given list. If the connection was accepted via an unrecognized IP address, the server does not authenticate the user. |

**Important:**

If a user inherits multiple roles with incompatible authentication
restrictions, that user becomes unusable.

For example, if a user inherits one role in which the
`clientSource` field is `["198.51.100.0"]` and another role in
which the `clientSource` field is `["203.0.113.0"]` the server is
unable to authenticate the user.

For more information on authentication in MongoDB, see
Authentication.

## Behavior

### Replica set

If run on a replica set, `db.updateRole()` is executed using
`"majority"` write concern by default.

### Scope

Except for roles created in the `admin` database, a role can only
include privileges that apply to its database and can only inherit from
other roles in its database.

A role created in the `admin` database can include privileges that
apply to the `admin` database, other databases or to the
cluster resource, and can inherit from roles
in other databases as well as the `admin` database.

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

You must have the `revokeRole` action on all databases in order to update a role.

You must have the `grantRole` action on the database of each role in the `roles` array
to update the array.

You must have the `grantRole`
action on the database of each privilege
in the `privileges` array to update the array. If a privilege's
resource spans databases, you must have `grantRole` on the
`admin` database. A privilege spans databases if the privilege is any of
the following:

- a collection in all databases

- all collections and all database

- the `cluster` resource

You must have the `setAuthenticationRestriction`
action on the database of the target
role to update a role's `authenticationRestrictions` document.

## Example

The following `db.updateRole()` method replaces the
`privileges` and the
`roles` for the `inventoryControl` role
that exists in the `products` database. The method runs on the
database that contains `inventoryControl`:

```javascript
use products
db.updateRole(
    "inventoryControl",
    {
      privileges:
          [
            {
              resource: { db:"products", collection:"clothing" },
              actions: [ "update", "createCollection", "createIndex"]
            }
          ],
      roles:
          [
            {
              role: "read",
              db: "products"
            }
          ]
    },
    { w:"majority" }
)
```

To view a role's privileges, use the `rolesInfo` command.
