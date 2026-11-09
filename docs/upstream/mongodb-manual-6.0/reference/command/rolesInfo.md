<!-- Converted from reference/command/rolesInfo.txt (reStructuredText). Includes are inlined. -->

# rolesInfo

## Definition

**`rolesInfo`**

Returns inheritance and privilege information for specified roles,
including both user-defined roles and
built-in roles.

The `rolesInfo` command can also retrieve all roles
scoped to a database.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB
   

## Syntax

The command has the following syntax:

```javascript
db.runCommand(
   {  
     rolesInfo: { role: <name>, db: <db> },
     showAuthenticationRestrictions: <Boolean>,
     showBuiltinRoles: <Boolean>,
     showPrivileges: <Boolean>,
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `rolesInfo` | string, document, array,  or integer | The role(s) to return information about. For the syntax for specifying roles, see rolesinfo-behavior. |
| `showAuthenticationRestrictions` | boolean | .. include:: /includes/fact-show-auth-restrictions-description.rst |
| `showBuiltinRoles` | boolean | Optional. When the `rolesInfo` field is set to `1`, set `showBuiltinRoles` to `true` to include built-in roles in the output. By default, this field is set to `false`, and the output for `rolesInfo: 1` displays only user-defined roles. |
| `showPrivileges` | boolean | Optional. Set the field to `true` to show role privileges, including both privileges inherited from other roles and privileges defined directly. By default, the command returns only the roles from which this role inherits privileges and does not return specific privileges. |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

## Behavior

### Return Information for a Single Role

To specify a role from the current database, specify the role by its name:

```javascript
{ rolesInfo: "<rolename>" }
```

To specify a role from another database, specify the role by a document that
specifies the role and database:

```javascript
{ rolesInfo: { role: "<rolename>", db: "<database>" } }
```

### Return Information for Multiple Roles

To specify multiple roles, use an array. Specify each role in the array as a
document or string. Use a string only if the role exists on the database on
which the command runs:

```javascript
{
  rolesInfo: [
     "<rolename>",
     { role: "<rolename>", db: "<database>" },
     ...
  ]
}
```

### Return Information for All Roles in the Database

To specify all roles in the database on which the command runs, specify
`rolesInfo: 1`. By default MongoDB displays all the user-defined roles in the database. To include built-in roles as well, include the parameter-value pair
`showBuiltinRoles: true`:

```javascript
{ rolesInfo: 1, showBuiltinRoles: true }
```

## Required Access

To view a role's information, you must be either explicitly granted the
role or must have the `viewRole` action on the role's database.

## Output

**`rolesInfo.role`**

The name of the role.

**`rolesInfo.db`**

The database on which the role is defined. Every database has built-in
roles. A database might also have user-defined
roles.

**`rolesInfo.isBuiltin`**

A value of `true` indicates the role is a built-in role. A value of `false` indicates the role is a
user-defined role.

**`rolesInfo.roles`**

The roles that directly provide privileges to this role and the databases
on which the roles are defined.

**`rolesInfo.inheritedRoles`**

All roles from which this role inherits privileges. This includes the roles
in the `rolesInfo.roles` array as well as the roles from which the
roles in the `rolesInfo.roles` array inherit privileges. All
privileges apply to the current role. The documents in this field list the
roles and the databases on which they are defined.

**`rolesInfo.privileges`**

The privileges directly specified by this role; i.e. the array
excludes privileges inherited from other roles. By default the
output does not include the `privileges` field. To
include the field, specify `showPrivileges: true` when running the
`rolesInfo` command.

Each privilege document specifies the resources and the actions allowed on the resources.

**`rolesInfo.inheritedPrivileges`**

All privileges granted by this role, including those inherited from
other roles. By default the output does not include the
`inheritedPrivileges` field. To include the field,
specify `showPrivileges: true` when running the
`rolesInfo` command.

Each privilege document specifies the resources and the actions allowed on the resources.

## Examples

The examples in this section show how to use the `rolesInfo` command
to:

- rolesInfo-example-single-role

- rolesInfo-example-multiple-roles

- rolesInfo-example-user-defined-roles

- rolesInfo-example-user-defined-and-built-in-roles

- rolesInfo-example-auth-restrictions

### View Information for a Single Role

The following command returns the role inheritance information for the
role `associate` defined in the `products` database:

```javascript
db.runCommand(
    {
      rolesInfo: { role: "associate", db: "products" }
    }
)
```

The following command returns the role inheritance information for the role
`siteManager` on the database on which the command runs:

```javascript
db.runCommand(
    {
      rolesInfo: "siteManager"
    }
)
```

The following command returns *both* the role inheritance and the privileges
for the role `associate` defined on the `products` database:

```javascript
db.runCommand(
    {
      rolesInfo: { role: "associate", db: "products" },
      showPrivileges: true
    }
)
```

### View Information for Multiple Roles

The following command returns information for two roles on two different
databases:

```javascript
db.runCommand(
    {
      rolesInfo: [
         { role: "associate", db: "products" },
         { role: "manager", db: "resources" }
      ]
    }
)
```

The following returns *both* the role inheritance and the privileges:

```javascript
db.runCommand(
    {
      rolesInfo: [
         { role: "associate", db: "products" },
         { role: "manager", db: "resources" }
      ],
      showPrivileges: true
    }
)
```

### View All User-Defined Roles for a Database

The following operation returns all user-defined roles on the database on which the command runs and includes
privileges:

```javascript
db.runCommand(
    {
      rolesInfo: 1,
      showPrivileges: true
    }
)
```

Example output (shortened for readability):

```javascript
{
  roles: [
    {
      _id: 'products.associate',
      role: 'associate',
      db: 'products',
      privileges: [
        {
          resource: { db: 'products', collection: '' },
          actions: [ 'bypassDocumentValidation' ]
        }
      ],
      roles: [ { role: 'readWrite', db: 'products' } ],
      isBuiltin: false,
      inheritedRoles: [ { role: 'readWrite', db: 'products' } ],
      inheritedPrivileges: [
        {
          resource: { db: 'products', collection: '' },
          actions: [ 'bypassDocumentValidation' ]
        },
        {
          resource: { db: 'products', collection: '' },
          actions: [
            'changeStream',
            'collStats',
            'compactStructuredEncryptionData',
            ...
          ]
        },
        ...
      ]
    }
  ],
  ok: 1
}
```

### View All User-Defined and Built-In Roles for a Database

The following operation returns all roles on the database on which the command
runs, including both built-in and user-defined roles:

```javascript
db.runCommand(
    {
      rolesInfo: 1,
      showBuiltinRoles: true
    }
)
```

Example output (shortened for readability):

```javascript
{
  roles: [
    {
      role: 'enableSharding',
      db: 'products',
      isBuiltin: true,
      roles: [],
      inheritedRoles: []
    },
    {
      role: 'userAdmin',
      db: 'products',
      isBuiltin: true,
      roles: [],
      inheritedRoles: []
    },
    {
      role: 'read',
      db: 'products',
      isBuiltin: true,
      roles: [],
      inheritedRoles: []
    },
    ...
  ],
  ok: 1
}
```

### View Authentication Restrictions for Roles

The following operation returns all user-defined roles on the
`products` database and includes authentication restrictions:

```javascript
db.runCommand(
    {
      rolesInfo: 1,
      showAuthenticationRestrictions: true
    }
)
```

Example output:

```javascript
{
  roles: [
    {
      _id: 'products.associate',
      role: 'associate',
      db: 'products',
      roles: [ { role: 'readWrite', db: 'products' } ],
      authenticationRestrictions: [
        [ { clientSource: [ '198.51.100.0' ] } ]
      ],
      isBuiltin: false,
      inheritedRoles: [ { role: 'readWrite', db: 'products' } ],
      inheritedAuthenticationRestrictions: [
        [ { clientSource: [ '198.51.100.0' ] } ]
      ]
    }
  ],
  ok: 1
}
```
