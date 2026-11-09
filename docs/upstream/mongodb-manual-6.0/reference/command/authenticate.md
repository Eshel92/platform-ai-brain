<!-- Converted from reference/command/authenticate.txt (reStructuredText). Includes are inlined. -->

# authenticate

**`authenticate`**

Authenticates using the X.509 authentication mechanism. When using
`mongosh`, use the `db.auth()` helper
as follows:

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
db.auth( "username", passwordPrompt() )
```

In earlier versions, to use the `db.auth()` method, specify
the password:

```javascript
db.auth( "username", "password" )
```

**See also:**

- `db.auth()`
- /security

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

### Client Disconnection

Starting in MongoDB 4.2, if the client that issued `authenticate`
disconnects before the operation completes, MongoDB marks `authenticate` 
for termination using `killOp`.
