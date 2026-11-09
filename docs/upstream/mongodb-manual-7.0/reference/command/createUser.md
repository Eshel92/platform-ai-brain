<!-- Converted from reference/command/createUser.txt (reStructuredText). Includes are inlined. -->

# createUser (database command)

## Definition

**`createUser`**

Creates a new user on the database where you run the command. The
`createUser` command returns a *duplicate user* error if the
user exists.

**Tip:**

In `mongosh`, this command can also be run through the `db.createUser` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

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

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication management methods and commands to prompt
for the password instead of specifying the password directly in the
method or command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
db.runCommand(
   {
     createUser: "<name>",
     pwd: passwordPrompt(),      // Or  "<cleartext password>"
     customData: { <any information> },
     roles: [
       { role: "<role>", db: "<database>" } | "<role>",
       ...
     ],
     writeConcern: { <write concern> },
     authenticationRestrictions: [
        { clientSource: [ "<IP|CIDR range>", ... ], serverAddress: [ "<IP|CIDR range>", ... ] }, 
        ...
     ],
     mechanisms: [ "<scram-mechanism>", ... ], 
     digestPassword: <boolean>,
     comment: <any>
   }
)
```

### Command Fields

`createUser` has the following fields:

* - Field
  - Type
  - Description
* - `createUser`
  - string
  - The name of the new user.
* - `pwd`
  - string
  - The user's password. The `pwd` field is not
    required if you run `createUser` on the `$external`
    database to create users who have credentials stored externally to
    MongoDB.

    The value can be either:

    - The user's password in cleartext string
    - `passwordPrompt()`, to prompt for the user's password

    You can use the `passwordPrompt()` method in conjunction with
    various user authentication management methods and commands to prompt
    for the password instead of specifying the password directly in the
    method or command call. However, you can still specify the password
    directly as you would with earlier versions of the
    `mongo` shell.

* - `customData`
  - document
  - Optional. Any arbitrary information. This field can be used to store any data
    an admin wishes to associate with this particular user. For example,
    this could be the user's full name or employee id.

* - `roles`
  - array
  - The roles granted to the user. Can specify an empty array `[]` to
    create users without roles.

* - `digestPassword`
  - boolean
  - Optional. Indicates whether the server or the client digests the password.

    If true, the server receives undigested password from the client and
    digests the password.

    If false, the client digests the password and passes the digested
    password to the server. Not compatible with `SCRAM-SHA-256`

    The default value is `true`.

* - `writeConcern`
  - document
  - .. include:: /includes/fact-write-concern-spec-link.rst
* - `authenticationRestrictions`
  - array
  - Optional. The authentication restrictions the server enforces on the created
    user. Specifies a list of IP addresses and
    CIDR (Classless Inter-Domain Routing) ranges from which the
    user is allowed to connect to the server or from which the server can
    accept users.
* - `mechanisms`
  - array
  - Optional. Specify the specific SCRAM mechanism or mechanisms for creating
    SCRAM user credentials. If `authenticationMechanisms` is
    specified, you can only specify a subset of the
    `authenticationMechanisms`.

    Valid values are:

    - `"SCRAM-SHA-1"`
    - Uses the `SHA-1` hashing function.
    - `"SCRAM-SHA-256"`
    - Uses the `SHA-256` hashing function.
    - Requires featureCompatibilityVersion set to `4.0`.
    - Requires digestPassword to be `true`.

    The default for featureCompatibilityVersion is `4.0` is both
    `SCRAM-SHA-1` and `SCRAM-SHA-256`.

    The default for featureCompatibilityVersion is `3.6` is
    `SCRAM-SHA-1`.

* - `digestPassword`
  - boolean
  - Optional. Indicates whether the server or the client digests the password.

    If true, the server receives undigested password from the client and
    digests the password.

    If false, the client digests the password and passes the digested
    password to the server. Not compatible with `SCRAM-SHA-256`

    The default value is `true`. 

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

### Roles

In the `roles` field, you can specify both
built-in roles and user-defined
roles.

To specify a role that exists in the same database where
`createUser` runs, you can either specify the role with the name of
the role:

```javascript
"readWrite"
```

Or you can specify the role with a document, as in:

```javascript
{ role: "<role>", db: "<database>" }
```

To specify a role that exists in a different database, specify the role
with a document.

### Authentication Restrictions

The `authenticationRestrictions` document can contain *only* the
following fields. The server throws an error if the 
`authenticationRestrictions` document contains an unrecognized field:

| Field Name | Value | Description |
|---|---|---|
| `clientSource` | Array of IP addresses and/or CIDR (Classless Inter-Domain Routing) ranges | If present, when authenticating a user, the server verifies that the client's IP address is either in the given list or belongs to a CIDR range in the list. If the client's IP address is not present, the server does not authenticate the user. |
| `serverAddress` | Array of IP addresses and/or CIDR (Classless Inter-Domain Routing) ranges | A list of IP addresses or CIDR ranges to which the client can connect. If present, the server will verify that the client's connection was accepted via an IP address in the given list. If the connection was accepted via an unrecognized IP address, the server does not authenticate the user. |

**Important:**

If a user inherits multiple roles with incompatible authentication
restrictions, that user becomes unusable.

For example, if a user inherits one role in which the
`clientSource` field is `["198.51.100.0"]` and another role in
which the `clientSource` field is `["203.0.113.0"]` the server is
unable to authenticate the user.

For more information on authentication in MongoDB, see
authentication.

## Behavior

### User ID

MongoDB automatically assigns a unique `userId` to the user upon creation.

### Encryption

**Warning:**

By default, `createUser` sends all specified data to the MongoDB 
instance in cleartext, even if using `passwordPrompt()`. Use
TLS transport encryption to protect communications between clients
and the server, including the password sent by `createUser`. For
instructions on enabling TLS transport encryption, see
/tutorial/configure-ssl.

MongoDB does not store the password in cleartext. The password
is only vulnerable in transit between the client and the 
server, and only if TLS transport encryption is not enabled.

### External Credentials

Users created on the `$external` database should have credentials
stored externally to MongoDB, as, for example, with MongoDB
Enterprise installations that use Kerberos.

To use sessions with `$external` authentication users
(Kerberos, LDAP, or X.509 users), usernames cannot be greater
than 10k bytes.

### `local` Database

You cannot create users on the local database.

### Username Limits

Usernames must consist of at least one character and cannot be larger than 7MB.

## Required Access

- To create a new user in a database, you must have the
  `createUser` action on
  that database resource.

- To grant roles to a user, you must have the `grantRole`
  action on the role's database.

The `userAdmin` and
`userAdminAnyDatabase` built-in roles provide
`createUser` and `grantRole` actions on their
respective resources.

## Example

The following `createUser` command creates a user `accountAdmin01` on the
`products` database. The command gives `accountAdmin01` the
`clusterAdmin` and `readAnyDatabase` roles on the `admin` database
and the `readWrite` role on the `products` database:

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication management methods and commands to prompt
for the password instead of specifying the password directly in the
method or command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
 db.getSiblingDB("products").runCommand( {
       createUser: "accountAdmin01",
       pwd: passwordPrompt(), 
       customData: { employeeId: 12345 },
       roles: [
                { role: "clusterAdmin", db: "admin" },
                { role: "readAnyDatabase", db: "admin" },
                "readWrite"
              ],
       writeConcern: { w: "majority" , wtimeout: 5000 }
} )
```
