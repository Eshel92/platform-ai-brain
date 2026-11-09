<!-- Converted from reference/command/usersInfo.txt (reStructuredText). Includes are inlined. -->

# usersInfo (database command)

## Definition

**`usersInfo`**

Returns information about one or more users. 

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

The command has the following syntax:

```javascript
db.runCommand(
   {
     usersInfo: <various>,
     showCredentials: <Boolean>,
     showCustomData: <Boolean>,
     showPrivileges: <Boolean>,
     showAuthenticationRestrictions: <Boolean>,
     filter: <document>,
     comment: <any>
   }
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - `usersInfo`
  - various
  - The user(s) about whom to return information.

    The argument to `usersInfo` has multiple forms depending on the
    requested information.  See usersInfo-field-specification.

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
  - Optional. Set to `true` to show the user's authentication
    restrictions.

    By default, this field is `false`.

    If viewing all users, you cannot specify this field.

* - `filter`   
  - document
  - Optional. A document that specifies `$match` stage
    conditions to return information for users that match the
    filter conditions.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

## `usersInfo: <various>`

```javascript
{ usersInfo: <various> }
```

The argument to `usersInfo` has multiple forms depending on the
requested information:

| Argument | Returns |
|---|---|
| `{ usersInfo: 1 }` | Returns information about the users in the database where the command is run. `mongosh` provides the `db.getUsers()` helper for this invocation of the command. |
| `{ usersInfo: <username> }` | Return information about the a specific user that exists in the database where the command is run. `mongosh` provides the `db.getUser()` helper for this invocation of the command. |
| `{ usersInfo: { user: <name>, db: <db> } }` | Returns information about the user specified by the name and database. |
| \| `{ usersInfo: [ { user: <name>, db: <db> }, ... ] }` \| `{ usersInfo: [ <username1>, ... ] }` | Returns information about the specified users. |
| `{ forAllDBs: true }` | Returns information about users in all databases. |

   
   

## Required Access

Users can always view their own information.

To view another user's information, the user running the command must
have privileges that include the `viewUser` action on the
other user's database.

## Output

The following information can be returned by the
`usersInfo` depending on the options specified:

```javascript
{
   "users" : [
      {
         "_id" : "<db>.<username>",
         "userId" : <UUID>,
         "user" : "<username>",
         "db" : "<db>",
         "mechanisms" : [ ... ],
         "customData" : <document>,
         "roles" : [ ... ],
         "credentials": { ... }, // only if showCredentials: true
         "inheritedRoles" : [ ... ],  // only if showPrivileges: true or showAuthenticationRestrictions: true
         "inheritedPrivileges" : [ ... ], // only if showPrivileges: true or showAuthenticationRestrictions: true
         "inheritedAuthenticationRestrictions" : [ ] // only if showPrivileges: true or showAuthenticationRestrictions: true
         "authenticationRestrictions" : [ ... ] // only if showAuthenticationRestrictions: true
      },
      ...
   ],
   "ok" : 1
}
```

## Examples

### View Specific Users

To see information and privileges, but not the credentials, for the
user `"Kari"` defined in `"home"` database,
run the following command:

```javascript
db.runCommand(
   {
     usersInfo:  { user: "Kari", db: "home" },
     showPrivileges: true
   }
)
```

To view a user that exists in the *current* database, you can specify
the user by name only. For example, if you are in the `home`
database and a user named `"Kari"` exists in the `home` database,
you can run the following command:

```javascript
db.getSiblingDB("home").runCommand(
   {
     usersInfo:  "Kari",
     showPrivileges: true
   }
)
```

### View Multiple Users

To view info for several users, use an array, with or without the
optional fields `showPrivileges` and `showCredentials`. For example:

```javascript
db.runCommand( {
   usersInfo: [ { user: "Kari", db: "home" }, { user: "Li", db: "myApp" } ],
   showPrivileges: true
} )
```

### View All Users for a Database

To view all users on the database the command is run, use a command document
that resembles the following:

```javascript
db.runCommand( { usersInfo: 1 } )
```

When viewing all users, you can specify the `showCredentials` option
but not the `showPrivileges` or the
`showAuthenticationRestrictions` options.

### View All Users for a Database that Match the Specified Filter

The `usersInfo` command can accept a `filter` document
to return information for users that match the filter condition.

To view all users in the current database who have the specified role,
use a command document that resembles the following:

```javascript
db.runCommand( { usersInfo: 1, filter: { roles: { role: "root", db: "admin" } } } )
```

When viewing all users, you can specify the `showCredentials` option
but not the `showPrivileges` or the
`showAuthenticationRestrictions` options.

### View All Users with `SCRAM-SHA-1` Credentials

The `usersInfo` command can accept a `filter` document
to return information for users that match the filter condition.

The following operation returns all users that have `SCRAM-SHA-1`
credentials. Specifically, the command returns all users across all
databases and then uses the `$match` stage to apply the
specified filter to the users.

```javascript
db.runCommand( { usersInfo: { forAllDBs: true}, filter: { mechanisms: "SCRAM-SHA-1" } } )
```

When viewing all users, you can specify the `showCredentials` option
but not the `showPrivileges` or the
`showAuthenticationRestrictions` options.

### Omit Custom Data from Output

**New in version:** 5.2

To omit users' custom data from the `usersInfo` output,
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
`usersInfo` with `showCustomData` set to `false`:

```javascript
db.getSiblingDB("products").runCommand ( {
   usersInfo: "accountAdmin01",
   showCustomData: false 
} )
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
