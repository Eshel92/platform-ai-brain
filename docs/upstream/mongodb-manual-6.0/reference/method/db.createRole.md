<!-- Converted from reference/method/db.createRole.txt (reStructuredText). Includes are inlined. -->

# db.createRole()

## Definition

**`db.createRole(role, writeConcern)`**

Creates a role in a database. You can specify privileges for the
role by explicitly listing the privileges or by having the role
inherit privileges from other roles or both. The role applies to
the database on which you run the method.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `createRole` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `db.createRole()` method accepts the following arguments:

| Parameter | Type | Description |
|---|---|---|
| `role` | document | A document containing the name of the role and the role definition. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |

The `role` document has the following form:

```javascript
{
  role: "<name>",
  privileges: [
     { resource: { <resource> }, actions: [ "<action>", ... ] },
     ...
  ],
  roles: [
     { role: "<role>", db: "<database>" } | "<role>",
      ...
  ],
  authenticationRestrictions: [
    {
      clientSource: ["<IP>" | "<CIDR range>", ...],
      serverAddress: ["<IP>" | "<CIDR range>", ...]
    },
    ...
  ]
}
```

The `role` document has the following fields:

| Field | Type | Description |
|---|---|---|
| `role` | string | The name of the new role. |
| `privileges` | array | The privileges to grant the role. A privilege consists of a resource and permitted actions. For the syntax of a privilege, see the `privileges` array. You must include the `privileges` field. Use an empty array to specify *no* privileges. |
| `roles` | array | An array of roles from which this role inherits privileges. You must include the `roles` field. Use an empty array to specify *no* roles to inherit from. |
| `authenticationRestrictions` | array | Optional. The authentication restrictions the server enforces on the role. Specifies a list of IP addresses and CIDR (Classless Inter-Domain Routing) ranges users granted this role are allowed to connect to and/or which they can connect from. |

          

### Roles

In the `roles` field, you can specify both
built-in roles and user-defined
roles.

To specify a role that exists in the same database where
`db.createRole()` runs, you can either specify the role with the name of
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

If run on a replica set, `db.createRole()` is executed using
`"majority"` write concern by default.

### Scope

Except for roles created in the `admin` database, a role can only
include privileges that apply to its database and can only inherit from
other roles in its database.

A role created in the `admin` database can include privileges that
apply to the `admin` database, other databases or to the
cluster resource, and can inherit from roles
in other databases as well as the `admin` database.

The `db.createRole()` method returns a *duplicate role* error
if the role already exists in the database.

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

To create a role in a database, you must have:

- the `createRole` action on
  that database resource.

- the `grantRole` action on
  that database to specify privileges for the new role as well as to
  specify roles to inherit from.

Built-in roles `userAdmin` and
`userAdminAnyDatabase` provide `createRole` and
`grantRole` actions on their respective resources.

To create a role with `authenticationRestrictions` specified, you
must have the `setAuthenticationRestriction`
action on the
database resource which the role is
created.

## Example

The following `db.createRole()` method creates the
`myClusterwideAdmin` role on the `admin` database:

```javascript
use admin
db.createRole(
   {
     role: "myClusterwideAdmin",
     privileges: [
       { resource: { cluster: true }, actions: [ "addShard" ] },
       { resource: { db: "config", collection: "" }, actions: [ "find", "update", "insert", "remove" ] },
       { resource: { db: "users", collection: "usersCollection" }, actions: [ "update", "insert", "remove" ] },
       { resource: { db: "", collection: "" }, actions: [ "find" ] }
     ],
     roles: [
       { role: "read", db: "admin" }
     ]
   },
   { w: "majority" , wtimeout: 5000 }
)
```
