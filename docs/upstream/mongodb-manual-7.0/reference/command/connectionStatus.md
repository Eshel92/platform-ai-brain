<!-- Converted from reference/command/connectionStatus.txt (reStructuredText). Includes are inlined. -->

# connectionStatus (database command)

## Definition

**`connectionStatus`**

Returns information about the current connection, specifically the
state of authenticated users and their available permissions.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
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
     connectionStatus: 1, 
     showPrivileges: <boolean> 
   }
)
```

### Command Fields

`connectionStatus` supports the following optional
field:

| Field | Type | Description |
|---|---|---|
| `showPrivileges` | boolean | Optional. Set `showPrivileges` to true to instruct `connectionStatus` to return the full set of privileges that currently-authenticated users possess. By default, this field is `false`. |

       
       

## Example

To run `connectionStatus` use the `db.runCommand()`
method, as in the following:

```javascript
db.runCommand( { connectionStatus: 1, showPrivileges: true } )
```

## Output

**`connectionStatus.authInfo`**

A document with data about the authentication state of the current
connection, including users and available permissions.

**`connectionStatus.authinfo.authenticatedUsers`**

An array with documents for each authenticated user.

**`connectionStatus.authInfo.authenticatedUsers[n].user`**

The user's name.

**`connectionStatus.authInfo.authenticatedUsers[n].db`**

The database associated with the user's credentials.

**`connectionStatus.authinfo.authenticatedUserRoles`**

An array with documents for each role granted to the current connection:

**`connectionStatus.authinfo.authenticatedUserRoles[n].role`**

The definition of the current roles associated with the current
authenticated users. See /reference/built-in-roles and
/reference/privilege-actions for more information.

**`connectionStatus.authinfo.authenticatedUserRoles[n].db`**

The database to which
`role`
applies.

**`connectionStatus.authInfo.authenticatedUserPrivileges`**

An array with documents describing the actions granted to the current connection,
grouped by resource.

**`connectionStatus.authInfo.authenticatedUserPrivileges[n].resource`**

A document describing the database and, if applicable, collection
to which
`connectionStatus.authInfo.authenticatedUserPrivileges[n].actions`
applies.

**`connectionStatus.authInfo.authenticatedUserPrivileges[n].actions`**

An array listing the privilege actions that
the connection has access to for the specified resource.

**`connectionStatus.ok`**

The return value for the command. A value of `1` indicates
success.
