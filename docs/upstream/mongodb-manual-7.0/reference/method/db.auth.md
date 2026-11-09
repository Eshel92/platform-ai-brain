<!-- Converted from reference/method/db.auth.txt (reStructuredText). Includes are inlined. -->

# db.auth() (mongosh method)

## Definition

**`db.auth()`**

Allows a user to authenticate to the database from within the
shell.

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication management methods and commands to prompt
for the password instead of specifying the password directly in the
method or command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

If you use the `db.auth(<username>, <password>)` syntax and omit the 
password, the user is prompted to enter a password.

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

## Syntax

The `db.auth()` has the following syntax forms:

### `db.auth(<username>, <password>)`

You can either:

- Omit the password to prompt the user to enter a password:

  ```javascript
  db.auth( <username> )
  ```

- Use `passwordPrompt()` to prompt the user to enter
  a password:
  

  ```javascript
  db.auth( <username>, passwordPrompt() )
  ```

- Specify a cleartext password.

  ```javascript
  db.auth( <username>, <password> )
  ```

### `db.auth(<user document>)`

```javascript
db.auth( {
   user: <username>,
   pwd: passwordPrompt(),   // Or "<cleartext password>"
   mechanism: <authentication mechanism>,
   digestPassword: <boolean>
} )
```

* - Parameter

  - Type

  - Description

* - `user`

  - string

  - The name of the user with access privileges for this database.

* - `pwd`

  - string

  - The user's password. The value can be either:

    - the user's password in cleartext string, or

    - `passwordPrompt()` to prompt for the user's password. 

      You can use the `passwordPrompt()` method in conjunction with
      various user authentication management methods and commands to prompt
      for the password instead of specifying the password directly in the
      method or command call. However, you can still specify the password
      directly as you would with earlier versions of the
      `mongo` shell.

* - `mechanism`

  - string

  - Optional. The `authentication mechanism` 
    to use.

    For available mechanisms, see `authentication mechanisms`.

    If unspecified, uses the `hello` command to determine
    the SASL mechanism or mechanisms for the specified user. See
    `saslSupportedMechs`.

* - `digestPassword`

  - boolean

  - Optional. Determines whether or not the supplied password should be pre-hashed
    before being used with the specified authentication mechanism. 

    - For SCRAM-SHA-1, although you may
      specify `true`, setting this value to `true` does not improve
      security and may interfere with credentials using other mechanisms.

    - For all other methods, this value must be set to `false`
      (default value). Any other value will result in authentication
      failure since those methods do not understand MongoDB pre-hashing.

    The default value is `false`.

**Note:**

`mongosh` excludes all `db.auth()` operations
from the saved history.

Returns
  `db.auth()` returns `0` when authentication is
  **not** successful, and `1` when the operation is successful.

## Behavior

### Client Disconnection

If the client that issued `db.auth()` disconnects before the operation 
completes, MongoDB marks `db.auth()` for termination using 
`killOp`.

## Example

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication management methods and commands to prompt
for the password instead of specifying the password directly in the
method or command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

If you use the `db.auth(<username>, <password>)` syntax and omit the 
password, the user is prompted to enter a password.

### Authenticate after Connecting to the Shell

To authenticate after connecting `mongosh`, issue
`db.auth()` in the user's authentication database:

```javascript
use test
db.auth( "myTestDBUser", passwordPrompt() )
```

You can omit the `password` value entirely to prompt the user to enter their 
password:

```javascript
use test
db.auth( "myTestDBUser" )
```

Starting in MongoDB 5.0, if your connection specifies the 
`--apiStrict` option, you may not use the `db.auth()` 
method to:

- Authenticate again as the same user on the same database.
- Authenticate as a different user when previously authenticated 
  on the same database.
- Authenticate with a new database when previously authenticated on a 
  different database.

### Authenticate when Connecting to the Shell

Alternatively, you can use `mongosh`'s
command-line options `--username`,
`--password`,
`--authenticationDatabase`,
and `--authenticationMechanism` to specify authentication credentials when
connecting `mongosh`:

```bash
mongosh --username "myTestDBUser" --password --authenticationDatabase test --authenticationMechanism SCRAM-SHA-256
```
