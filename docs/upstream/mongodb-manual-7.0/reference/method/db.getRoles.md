<!-- Converted from reference/method/db.getRoles.txt (reStructuredText). Includes are inlined. -->

# db.getRoles() (mongosh method)

## Definition

**`db.getRoles()`**

Returns information for all the roles in the database on which the command
runs. The method can be run with or without an argument.

If run without an argument, `db.getRoles()` returns inheritance
information for the database's user-defined
roles.

To return more information, pass the `db.getRoles()` a
document with the following fields:

| Field | Type | Description |
|---|---|---|
| `rolesInfo` | integer | Set this field to `1` to retrieve all user-defined roles. |
| `showAuthenticationRestrictions` | boolean | .. include:: /includes/fact-show-auth-restrictions-description.rst |
| `showBuiltinRoles` | boolean | Optional. Set this field to true to display built-in roles as well as user-defined roles. |
| `showPrivileges` | boolean | Optional. Set this field to `true` to show role privileges, including both privileges inherited from other roles and privileges defined directly. By default, the command returns only the roles from which this role inherits privileges and does not return specific privileges. |

`db.getRoles()` wraps the `rolesInfo` command.

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

## Required Access

To view a role's information, you must be either explicitly granted the
role or must have the `viewRole` action on the role's database.

## Examples

The examples in this section show how to use `db.getRoles` to:

- db-getRoles-example-return-built-in-roles

- db-getRoles-example-auth-restrictions

### Show Role Privileges and Built-In Roles

The following operation returns all the roles on the `products`
database, including role privileges and built-in roles:

```javascript
use products

db.getRoles(
    {
      rolesInfo: 1,
      showPrivileges: true,
      showBuiltinRoles: true
    }
)
```

Example output (shortened for readability):

```javascript
{
  roles: [
    {
      role: 'dbOwner',
      db: 'products',
      isBuiltin: true,
      roles: [],
      inheritedRoles: [],
      privileges: [
        {
          resource: { db: 'products', collection: '' },
          actions: [
            'analyze',
            'bypassDocumentValidation',
            'changeCustomData',
            ...
          ]
        },
        {
          resource: { db: 'products', collection: 'system.profile' },
          actions: [
            'changeStream',
            'collStats',
            'convertToCapped',
            ...
          ]
        }
      ],
      inheritedPrivileges: [
        {
          resource: { db: 'products', collection: '' },
          actions: [
            'analyze',
            'bypassDocumentValidation',
            'changeCustomData',
            ...
          ]
        }
      ]
    },
    ...
  ]
}
```

  

### Show Authentication Restrictions

The following operation returns role inheritance information and
authentication restrictions for all user-defined roles on the `product` database:

```javascript
use products

db.getRoles( { rolesInfo: 1, showAuthenticationRestrictions: true } )
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
