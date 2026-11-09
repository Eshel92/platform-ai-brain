<!-- Converted from reference/command/updateRole.txt (reStructuredText). Includes are inlined. -->

# updateRole (database command)

## Definition

**`updateRole`**

Updates a user-defined role. The
`updateRole` command must run on the role's database.

**Tip:**

In `mongosh`, this command can also be run through the `db.updateRole` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

An update to a field **completely replaces** the previous field's values.
To grant or remove roles or privileges without
replacing all values, use one or more of the following commands:

- `grantRolesToRole`
- `grantPrivilegesToRole`
- `revokeRolesFromRole`
- `revokePrivilegesFromRole`

**Warning:**

An update to the `privileges` or `roles` array
completely replaces the previous array's values.

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

To update a role, you must provide the `privileges` array, `roles` 
array, or both.

The command uses the following syntax:

```javascript
db.runCommand(
   {
     updateRole: "<role>",
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
             serverAddress: ["<IP>", ...]
           },
           ...
         ]
     writeConcern: <write concern document>,
     comment: <any>
   }
 )
```

 

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `updateRole` | string | The name of the user-defined role role to update. |
| `privileges` | array | Optional. Required if you do not specify `roles` array. The privileges to grant the role. An update to the `privileges` array overrides the previous array's values. For the syntax for specifying a privilege, see the `privileges` array. |
| `roles` | array | Optional. Required if you do not specify `privileges` array. The roles from which this role inherits privileges. An update to the `roles` array overrides the previous array's values. |
| `authenticationRestrictions` | array | Optional. The authentication restrictions the server enforces on the role. Specifies a list of IP addresses and CIDR (Classless Inter-Domain Routing) ranges users granted this role are allowed to connect to and/or which they can connect from. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

### Roles

In the `roles` field, you can specify both
built-in roles and user-defined
roles.

To specify a role that exists in the same database where
`updateRole` runs, you can either specify the role with the name of
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
authentication.

## Behavior

A role's privileges apply to the database where the role is created. The
role can inherit privileges from other roles in its database. A role
created on the `admin` database can include privileges that apply to all
databases or to the cluster and can inherit
privileges from roles in other databases.

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

The following is an example of the `updateRole` command that
updates the `myClusterwideAdmin` role on the `admin` database.
While the `privileges` and the
`roles` arrays are both optional, at least
one of the two is required:

```javascript
db.adminCommand(
   {
     updateRole: "myClusterwideAdmin",
     privileges:
         [
           {
             resource: { db: "", collection: "" },
             actions: [ "find" , "update", "insert", "remove" ]
           }
         ],
     roles:
         [
           { role: "dbAdminAnyDatabase", db: "admin" }
         ],
     writeConcern: { w: "majority" }
   }
)
```

To view a role's privileges, use the `rolesInfo` command.
