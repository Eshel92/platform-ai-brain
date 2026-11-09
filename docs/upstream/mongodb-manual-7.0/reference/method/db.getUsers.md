<!-- Converted from reference/method/db.getUsers.txt (reStructuredText). Includes are inlined. -->

# db.getUsers() (mongosh method)

## Definition

**`db.getUsers(<options>)`**

Returns information for all the users in the database.

`db.getUsers()` wraps the `usersInfo: 1`  command.

The `db.getUsers()` method can take the following options:

```none
db.getUsers( { 
   showCredentials: <Boolean>,
   showCustomData: <Boolean>,
   filter: <document>
} )
```

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

* - `filter`
  - document
  - Optional. A document that specifies `$match` stage
    conditions to return information for users that match the
    filter conditions.

For more information, see `usersInfo`.

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

### View All Users for a Database that Match the Specified Filter

The `db.getUsers()` method can accept a `filter` document
to return information for users that match the filter condition.

To view all users for the current database who have `SCRAM-SHA-256`
credentials:

```javascript
db.getUsers({ filter: { mechanisms: "SCRAM-SHA-256" } })
```

When viewing all users, you can specify the `showCredentials` option
but not the `showPrivileges` or the
`showAuthenticationRestrictions` options.

### Omit Custom Data from Output

**New in version:** 5.2

To omit users' custom data from the `db.getUsers()` output,
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
`db.getUsers()` with `showCustomData` set to `false`:

```javascript
db.getSiblingDB("products").getUsers( { showCustomData: false } )
```

Example output:

```javascript
{
   users: [
     {
       _id: 'products.accountAdmin01',
       userId: UUID("0955afc1-303c-4683-a029-8e17dd5501f4"),
       user: 'accountAdmin01',
       db: 'products',
       roles: [ { role: 'readWrite', db: 'products' } ],
       mechanisms: [ 'SCRAM-SHA-1', 'SCRAM-SHA-256' ]
     }
   ],
   ok: 1
}
```
