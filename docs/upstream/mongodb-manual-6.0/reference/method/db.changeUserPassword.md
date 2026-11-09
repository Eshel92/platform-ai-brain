<!-- Converted from reference/method/db.changeUserPassword.txt (reStructuredText). Includes are inlined. -->

# db.changeUserPassword()

## Definition

**`db.changeUserPassword(username, password)`**

Updates a user's password. Run the method in the database where the
user is defined, i.e. the database you `created` the user.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `updateUser` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

* - Parameter
  - Type
  - Description
* - `username`
  - string
  - The name of the user whose password you wish to change.
* - `password`
  - string
  - The user's password. The value can be either:

    - the user's password in cleartext string, or
    - `passwordPrompt()` to prompt for the user's password. 

    **Tip:**

    You can use the `passwordPrompt()` method in conjunction with
    various user authentication/management methods/commands to prompt
    for the password instead of specifying the password directly in the
    method/command call. However, you can still specify the password
    directly as you would with earlier versions of the
    `mongo` shell.

* - `writeConcern`
  - document
  - .. include:: /includes/fact-write-concern-spec-link.rst

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

To modify the password of another user on a database, you must have the
`changePassword` action
on that database.

## Behavior

**Warning:**

By default, `db.changeUserPassword()` sends all specified data to the MongoDB 
instance in cleartext, even if using `passwordPrompt()`. Use
TLS transport encryption to protect communications between clients
and the server, including the password sent by `db.changeUserPassword()`. For
instructions on enabling TLS transport encryption, see
/tutorial/configure-ssl.

MongoDB does not store the password in cleartext. The password
is only vulnerable in transit between the client and the 
server, and only if TLS transport encryption is not enabled.

## Example

The following operation changes the password of the user named
`accountUser` in the `products` database to `SOh3TbYhx8ypJPxmt1oOfL`:

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
use products
db.changeUserPassword("accountUser", passwordPrompt())
```

When prompted in `mongosh` for the password, enter
the new password.

You can also pass the new password directly to
`db.changeUserPassword()`:

```javascript
use products
db.changeUserPassword("accountUser", "SOh3TbYhx8ypJPxmt1oOfL")
```
