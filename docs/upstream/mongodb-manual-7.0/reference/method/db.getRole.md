<!-- Converted from reference/method/db.getRole.txt (reStructuredText). Includes are inlined. -->

# db.getRole() (mongosh method)

## Definition

**`db.getRole(rolename, args)`**

Returns the roles from which this role inherits privileges. Optionally, the
method can also return all the role's privileges.

Run `db.getRole()` from the database that contains the role. The
command can retrieve information for both user-defined roles and built-in roles.

The `db.getRole()` method accepts the following parameters:

| Parameter | Type | Description |
|---|---|---|
| `rolename` | string | The name of the role. |
| `args` | document | Optional. A document specifying additional arguments. |

The `args` document supports the following optional fields:

| Field | Type | Description |
|---|---|---|
| `showAuthenticationRestrictions` | boolean | .. include:: /includes/fact-show-auth-restrictions-description.rst |
| `showBuiltinRoles` | boolean | Optional. Set this field to `true` to include built-in roles in the output. By default, this field is set to `false`, and the output for `rolesInfo: 1` displays only user-defined roles. |
| `showPrivileges` | boolean | Optional. Set this field to `true` to show role privileges, including both privileges inherited from other roles and privileges defined directly. By default, the command returns only the roles from which this role inherits privileges and does not return specific privileges. |

`db.getRole()` wraps the `rolesInfo` command.

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

- db-getRole-example-inheritance

- db-getRole-example-privileges

- db-getRole-example-auth-restrictions

### Show Role Inheritance Information

The following operation returns role inheritance information for the role
`associate` defined on the `products` database:

```javascript
use products
db.getRole( "associate" )
```

Example output:

```javascript
{
  _id: 'products.associate',
  role: 'associate',
  db: 'products',
  roles: [ { role: 'readWrite', db: 'products' } ],
  inheritedRoles: [ { role: 'readWrite', db: 'products' } ],
  isBuiltin: false
}
```

### Show Role Privileges

The following operation returns role inheritance information *and privileges*
for the role `associate` defined on the `products` database:

```javascript
use products
db.getRole( "associate", { showPrivileges: true } )
```

Example output:

```javascript
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
        'convertToCapped',
        'createCollection',
        'createIndex',
        'dbHash',
        'dbStats',
        'dropCollection',
        'dropIndex',
        'find',
        'insert',
        'killCursors',
        'listCollections',
        'listIndexes',
        'planCacheRead',
        'remove',
        'renameCollectionSameDB',
        'update'
      ]
    }
  ],
  isBuiltin: false
}
```

### Show Authentication Restrictions

The following operation returns role inheritance information and
authentication restrictions for the role `associate` defined on the
`products` database:

```javascript
use products
db.getRole( "associate", { showAuthenticationRestrictions: true } )
```

Example output:

```javascript
{
  _id: 'products.associate',
  role: 'associate',
  db: 'products',
  roles: [ { role: 'readWrite', db: 'products' } ],
  authenticationRestrictions: [
    [ { clientSource: [ '198.51.100.0' ] } ]
  ],
  inheritedRoles: [ { role: 'readWrite', db: 'products' } ],
  inheritedAuthenticationRestrictions: [
    [ { clientSource: [ '198.51.100.0' ] } ]
  ],
  isBuiltin: false
}
```
