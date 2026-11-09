<!-- Converted from reference/method/db.getUser.txt (reStructuredText). Includes are inlined. -->

# db.getUser()

## Definition

**`db.getUser(username, args)`**

Returns user information for a specified user. Run this method on the
user's database. If the user doesn't exist in the database,
`db.getUser()` returns `null`. 

The `db.getUser()` method has the following parameters:

```none
db.getUser( "<username>", { 
   showCredentials: <Boolean>,
   showCustomData: <Boolean>,
   showPrivileges: <Boolean>,
   showAuthenticationRestrictions: <Boolean>,
   filter: <document>
} )
```

| Parameter | Type | Description |
|---|---|---|
| `username` | string | The name of the user for which to retrieve information. |
| `args` | document | Optional. A document specifying additional arguments. |

The `args` document supports the following fields:

* - Field
  - Type
  - Description

* - `showCredentials`
  - boolean
  - Optional. Set to `true` to display the user's password
    hash.

    By default, this field is `false`.

* - `showCustomData`
  - boolean
  - Optional. Set to `false` to omit the user's `customData`
    from the output.

    By default, this field is `true`.

    **New in version:** 5.2

* - `showPrivileges`
  - boolean
  - Optional. Set to `true` to show the user's full set
    of privileges, including expanded information for the
    inherited roles.

    By default, this field is `false`.

    If viewing all users, you cannot specify this field.

* - `showAuthenticationRestrictions`
  - boolean
  - Optional. Set to `true` to show the user's
    authentication restrictions.

    By default, this field is `false`.

    If viewing all users, you cannot specify this field.

* - `filter`
  - document
  - Optional. A document that specifies `$match` stage
    conditions to return information for users that match the
    filter conditions.

`db.getUser()` wraps the `usersInfo: <username>` command.

For details on output, see `usersInfo`.

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

To view another user's information, you must have the
`viewUser` action on the
other user's database.

Users can view their own information.

## Examples

The following operations return information about an example
`appClient` user in an `accounts` database:

```javascript
use accounts
db.getUser("appClient")
```

Example output:

```javascript
{
   _id: 'accounts.appClient',
   userId: UUID("1c2fc1bf-c4dc-4a22-8b04-3971349ce0dc"),
   user: 'appClient',
   db: 'accounts',
   roles: [],
   mechanisms: [ 'SCRAM-SHA-1', 'SCRAM-SHA-256' ]
}
```

### Omit Custom Data from Output

**New in version:** 5.2

To omit a user's custom data from the `db.getUser()` output,
set the `showCustomData` option to `false`.

Use the `createUser` command to create a user named
`accountAdmin01` on the `products` database:

```javascript
db.getSiblingDB("products").runCommand( {
   createUser: "accountAdmin01",
   pwd: passwordPrompt(), 
   customData: { employeeId: 12345 },
   roles: [ { role: 'readWrite', db: 'products' } ]
} )
```

The user contains a `customData` field of `{ employeeId: 12345 }`.

To retrieve the user but omit the custom data from the output, run
`db.getUser()` with `showCustomData` set to `false`:

```javascript
db.getSiblingDB("products").getUser(
   "accountAdmin01",
   { showCustomData: false }
)
```

Example output:

```javascript
{
   _id: 'products.accountAdmin01',
   userId: UUID("0955afc1-303c-4683-a029-8e17dd5501f4"),
   user: 'accountAdmin01',
   db: 'products',
   roles: [ { role: 'readWrite', db: 'products' } ],
   mechanisms: [ 'SCRAM-SHA-1', 'SCRAM-SHA-256' ]
}
```
