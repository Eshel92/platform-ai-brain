<!-- Converted from reference/method/db.updateUser.txt (reStructuredText). Includes are inlined. -->

# db.updateUser() (mongosh method)

## Definition

**`db.updateUser( username, update, writeConcern )`**

Updates the user's profile on the database on which you run the method.
An update to a field **completely replaces** the previous field's values.
This includes updates to the user's `roles` array.

**Warning:**

When you update the `roles` array, you completely replace the
previous array's values. To add or remove roles without replacing all
the user's existing roles, use the `db.grantRolesToUser()` or
`db.revokeRolesFromUser()` methods.

The `db.updateUser()` method uses the following syntax:

**Tip:**

You can use the `passwordPrompt()` method in conjunction with
various user authentication management methods and commands to prompt
for the password instead of specifying the password directly in the
method or command call. However, you can still specify the password
directly as you would with earlier versions of the
`mongo` shell.

```javascript
db.updateUser(
   "<username>",
   {
     customData : { <any information> },
     roles : [
       { role: "<role>", db: "<database>" } | "<role>",
       ...
     ],
     pwd: passwordPrompt(),      // Or  "<cleartext password>"
     authenticationRestrictions: [
        {
          clientSource: ["<IP>" | "<CIDR range>", ...],
          serverAddress: ["<IP>", | "<CIDR range>", ...]
        },
        ...
     ],
     mechanisms: [ "<SCRAM-SHA-1|SCRAM-SHA-256>", ... ],
     passwordDigestor: "<server|client>"
   },
   writeConcern: { <write concern> }
)
```

The `db.updateUser()` method has the following arguments.

| Parameter | Type | Description |
|---|---|---|
| `username` | string | The name of the user to update. |
| `update` | document | A document containing the replacement data for the user. This data completely replaces the corresponding data for the user. |
| `writeConcern` | document | .. include:: /includes/fact-write-concern-spec-link.rst |

The `update` document specifies the fields to update and their
new values. All  fields in the `update` document are optional,
but *must* include at least one field.

The `update` document has the following fields:

* - Field

  - Type

  - Description

* - `customData`

  - document

  - Optional. Any arbitrary information.

* - `roles`

  - array

  - Optional. The roles granted to the user. An update to the `roles` array
    overrides the previous array's values.

* - `pwd`

  - string

  - Optional. The user's password. The value can be either:

    - the user's password in cleartext string, or

    - `passwordPrompt()` to prompt for the user's password. 

    You can use the `passwordPrompt()` method in conjunction with
    various user authentication management methods and commands to prompt
    for the password instead of specifying the password directly in the
    method or command call. However, you can still specify the password
    directly as you would with earlier versions of the
    `mongo` shell.

* - `authenticationRestrictions`

  - array

  - Optional. The authentication restrictions the server enforces upon the user.
    Specifies a list of IP addresses and
    CIDR (Classless Inter-Domain Routing) ranges from which the
    user is allowed to connect to the server or from which the server can
    accept users.

* - `mechanisms`

  - array

  - Optional. The specific SCRAM mechanism or mechanisms for the user credentials.
    If `authenticationMechanisms` is specified, you can only
    specify a subset of the `authenticationMechanisms`.

    If updating the mechanisms field without the password, you can only
    specify a subset of the user's current mechanisms, and only the
    existing user credentials for the specified mechanism or mechanisms
    are retained.

    If updating the password along with the mechanisms, new set of
    credentials are stored for the user.

    Valid values are:

    - `"SCRAM-SHA-1"`

      - Uses the `SHA-1` hashing function.

    - `"SCRAM-SHA-256"`

      - Uses the `SHA-256` hashing function.

      - Requires featureCompatibilityVersion set to `4.0`.

      - Requires passwordDigestor to be `server`.

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
`db.updateUser()` runs, you can either specify the role with the name of
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

The `db.updateUser()` method wraps the `updateUser`
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

### Replica set

If run on a replica set, `db.updateUser()` is executed using
`"majority"` write concern by default.

### Encryption

**Warning:**

By default, `db.updateUser()` sends all specified data to the MongoDB 
instance in cleartext, even if using `passwordPrompt()`. Use
TLS transport encryption to protect communications between clients
and the server, including the password sent by `db.updateUser()`. For
instructions on enabling TLS transport encryption, see
/tutorial/configure-ssl.

MongoDB does not store the password in cleartext. The password
is only vulnerable in transit between the client and the 
server, and only if TLS transport encryption is not enabled.

## Required Access

You must have access that includes the `revokeRole`
action on all databases in order to update a
user's `roles` array.

You must have the `grantRole` action on a role's database to add a role to a user.

To change another user's `pwd` or `customData` field, you must have
the `changePassword` and `changeCustomData`
actions respectively on that user's database.

To modify your own password and custom data, you must have privileges
that grant `changeOwnPassword` and
`changeOwnCustomData` actions respectively on the user's database.

## Example

Given a user `appClient01` in the `products` database with the following
user info:

```javascript
{
   _id : "products.appClient01",
   userId : UUID("c5d88855-3f1e-46cb-9c8b-269bef957986"),
   user : "appClient01",
   db : "products",
   customData : { empID : "12345", badge : "9156" },
   roles : [
       {
         role : "readWrite",
         db : "products"
       },
       {
         role : "read",
         db : "inventory"
       }
   ],
   mechanisms : [ 
      "SCRAM-SHA-1",
      "SCRAM-SHA-256"
   ],
   authenticationRestrictions : [ {
      clientSource: ["69.89.31.226"],
      serverAddress: ["172.16.254.1"]
   } ]
}
```

The following `db.updateUser()` method **completely** replaces the
user's `customData` and `roles` data:

```javascript
use products
db.updateUser( "appClient01",
{
   customData : { employeeId : "0x3039" },
   roles : [
      { role : "read", db : "assets"  }
   ]
} )
```

The user `appClient01` in the `products` database now has the following
user information:

```javascript
{
   _id : "products.appClient01",
   userId : UUID("c5d88855-3f1e-46cb-9c8b-269bef957986"),
   user : "appClient01",
   db : "products",
   customData : { employeeId : "0x3039" },
   roles : [
       {
         role : "read",
         db : "assets"
       }
   ],
   mechanisms : [
      "SCRAM-SHA-1",
      "SCRAM-SHA-256"
   ],
   authenticationRestrictions : [ {
      clientSource: ["69.89.31.226"],
      serverAddress: ["172.16.254.1"]
   } ]
}
```

   

### Update User to Use `SCRAM-SHA-256` Credentials Only

**Note:**

To use SCRAM-SHA-256, the
`featureCompatibilityVersion` must be set to `4.0`. For more
information on featureCompatibilityVersion, see view-fcv and
`setFeatureCompatibilityVersion`.

The following operation updates a user who currently have both
`SCRAM-SHA-256` and `SCRAM-SHA-1` credentials to have only
`SCRAM-SHA-256` credentials.

**Note:**

- If the password is not specified along with the `mechanisms`,
  you can only update the `mechanisms` to a subset of the current
  SCRAM mechanisms for the user.

- If the password is specified along with the `mechanisms`, you
  can specify any supported SCRAM mechanism or mechanisms.

- For `SCRAM-SHA-256`, the `passwordDigestor` must be the
  default value `"server"`.

```javascript
use reporting
db.updateUser(
   "reportUser256",
   {
     mechanisms: [ "SCRAM-SHA-256" ]
   }
)
```
