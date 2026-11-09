<!-- Converted from reference/method/db.createUser.txt (reStructuredText). Includes are inlined. -->

# db.createUser()

## Definition

**`db.createUser(user, writeConcern)`**

Creates a new user for the database on which the method is run.
`db.createUser()` returns a *duplicate user* error if the
user already exists on the database.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `createUser` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `db.createUser()` method has the following syntax:

| Field | Type | Description |
|---|---|---|
| `user` | document | The document with authentication and access information about the user to create. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |

The `user` document defines the user and has the following form:

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
{ 
  user: "<name>",
  pwd: passwordPrompt(),      // Or  "<cleartext password>"
  customData: { <any information> },
  roles: [
    { role: "<role>", db: "<database>" } | "<role>",
    ...
  ],
  authenticationRestrictions: [ 
     { 
       clientSource: ["<IP>" | "<CIDR range>", ...],
       serverAddress: ["<IP>" | "<CIDR range>", ...]
     },
     ...
  ],
  mechanisms: [ "<SCRAM-SHA-1|SCRAM-SHA-256>", ... ],
  passwordDigestor: "<server|client>"
}
```

The `user` document has the following fields:

* - Field

  - Type

  - Description

* - `user`

  - string

  - The name of the new user.

* - `pwd`

  - string

  - The user's password. The `pwd` field is not
    required if you run `db.createUser()` on the `$external`
    database to create users who have credentials stored externally to
    MongoDB.

    The value can be either:

    - the user's password in cleartext string, or

    - `passwordPrompt()` to prompt for the user's password. 

    You can use the `passwordPrompt()` method in conjunction with
    various user authentication/management methods/commands to prompt
    for the password instead of specifying the password directly in the
    method/command call. However, you can still specify the password
    directly as you would with earlier versions of the
    `mongo` shell.

* - `customData`

  - document

  - Optional. Any arbitrary information.  This field can be used to store any data
    an admin wishes to associate with this particular user.  For example,
    this could be the user's full name or employee id.

* - `roles`

  - array

  - The roles granted to the user. Can specify an empty array `[]` to
    create users without roles.

* - authenticationRestrictions

  - array

  - .. _db-createUser-authenticationRestrictions:

    Optional. The authentication restrictions the server enforces on the created
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

      - Requires passwordDigestor to be `server`.

    The default is both `SCRAM-SHA-1` and `SCRAM-SHA-256`.

* - `passwordDigestor`

  - string

  - Optional. Indicates whether the server or the client digests the password.

    Available values are:

    - `"server"` (Default)
          The server receives undigested password from the client and
          digests the password.

    - `"client"` (Not compatible with `SCRAM-SHA-256`)
          The client digests the password and passes the digested
          password to the server.
          

### Roles

In the `roles` field, you can specify both
built-in roles and user-defined
roles.

To specify a role that exists in the same database where
`db.createUser()` runs, you can either specify the role with the name of
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
Authentication.

The `db.createUser()` method wraps the `createUser`
command.

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
   

## Behavior

### User ID

MongoDB automatically assigns a unique `userId` to the user upon creation.

### Replica set

If run on a replica set, `db.createUser()` is executed using
`"majority"` write concern by default.

### Encryption

**Warning:**

By default, `db.createUser()` sends all specified data to the MongoDB 
instance in cleartext, even if using `passwordPrompt()`. Use
TLS transport encryption to protect communications between clients
and the server, including the password sent by `db.createUser()`. For
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

## Examples

The following `db.createUser()` operation creates the
`accountAdmin01` user on the `products` database.

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
use products
db.createUser( { user: "accountAdmin01",
                 pwd: passwordPrompt(),  // Or  "<cleartext password>"
                 customData: { employeeId: 12345 },
                 roles: [ { role: "clusterAdmin", db: "admin" },
                          { role: "readAnyDatabase", db: "admin" },
                          "readWrite"] },
               { w: "majority" , wtimeout: 5000 } )
```

The operation gives `accountAdmin01` the following roles:

- the `clusterAdmin` and `readAnyDatabase` roles on the `admin`
  database

- the `readWrite` role on the `products` database

### Create User with Roles

The following operation creates `accountUser` in the `products` database
and gives the user the `readWrite` and `dbAdmin` roles.

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
use products
db.createUser(
   {
     user: "accountUser",
     pwd: passwordPrompt(),  // Or  "<cleartext password>"
     roles: [ "readWrite", "dbAdmin" ]
   }
)
```

### Create User without Roles

The following operation creates a user named `reportsUser` in the `admin`
database but does not yet assign roles:

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
use admin
db.createUser(
   {
     user: "reportsUser",
     pwd: passwordPrompt(),  // Or  "<cleartext password>"
     roles: [ ]
   }
)
```

### Create Administrative User with Roles

The following operation creates a user named `appAdmin` in the
`admin` database and gives the user `readWrite` access to the
`config` database, which lets the user change certain settings for
sharded clusters, such as to the balancer setting.

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
use admin
db.createUser(
   {
     user: "appAdmin",
     pwd: passwordPrompt(),   // Or  "<cleartext password>"
     roles:
       [
         { role: "readWrite", db: "config" },
         "clusterAdmin"
       ]
   }
)
```

### Create User with Authentication Restrictions

The following operation creates a user named `restricted` in the
`admin` database. This user may only authenticate if connecting from
IP address `192.0.2.0` to IP address `198.51.100.0`.

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
use admin
db.createUser(
   {
     user: "restricted",
     pwd: passwordPrompt(),      // Or  "<cleartext password>"
     roles: [ { role: "readWrite", db: "reporting" } ],
     authenticationRestrictions: [ {
        clientSource: ["192.0.2.0"],
        serverAddress: ["198.51.100.0"]
     } ]
   }
)
```

### Create User with `SCRAM-SHA-256` Credentials Only

**Note:**

To use SCRAM-SHA-256, the
`featureCompatibilityVersion` must be set to `4.0`. For more
information on featureCompatibilityVersion, see view-fcv and
`setFeatureCompatibilityVersion`.

The following operation creates a user with only `SCRAM-SHA-256`
credentials.

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication/management methods/commands to prompt
for the password instead of specifying the password directly in the
method/command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
use reporting
db.createUser(
   {
     user: "reportUser256",
     pwd: passwordPrompt(),   // Or  "<cleartext password>"
     roles: [ { role: "readWrite", db: "reporting" } ],
     mechanisms: [ "SCRAM-SHA-256" ]
   }
)
```

If the `authenticationMechanisms` parameter is set, the
`mechanisms` field can only include values specified in the
`authenticationMechanisms` parameter.
