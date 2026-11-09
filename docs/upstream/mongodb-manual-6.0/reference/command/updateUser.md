<!-- Converted from reference/command/updateUser.txt (reStructuredText). Includes are inlined. -->

# updateUser

## Definition

**`updateUser`**

Updates the user's profile on the database on which you run the
command. An update to a field **completely replaces** the previous
field's values, including updates to the user's `roles` and
`authenticationRestrictions` arrays.

**Tip:**

In `mongosh`, this command can also be run through the `db.changeUserPassword` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

**Warning:**

When you update the `roles` array, you completely replace the
previous array's values. To add or remove roles without replacing all
the user's existing roles, use the `grantRolesToUser` or
`revokeRolesFromUser` commands.

To update a user, you must specify the `updateUser` field and at 
least one other field, other than `writeConcern`.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, M10+, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command uses the following syntax:

```javascript
 db.runCommand(
    { 
      updateUser: "<username>",
      pwd: passwordPrompt(),      // Or  "<cleartext password>"
      customData: { <any information> },
      roles: [
        { role: "<role>", db: "<database>" } | "<role>",
        ...
      ],
      authenticationRestrictions: [
         {
           clientSource: ["<IP>" | "<CIDR range>", ...],
           serverAddress: ["<IP>", | "<CIDR range>", ...]
         },
         ...
      ],
      mechanisms: [ "<scram-mechanism>", ... ],
      digestPassword: <boolean>,
      writeConcern: { <write concern> },
      comment: <any>
    }
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - `updateUser`
  - string
  - The name of the user to update.

* - `pwd`
  - string
  - Optional. The user's password. The value can be either:

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
  - Optional. Any arbitrary information.

* - `roles`
  - array
  - Optional. The roles granted to the user. An update to the `roles` array
    overrides the previous array's values.

* - `writeConcern`
  - document
  - .. include:: /includes/fact-write-concern-spec-link.rst

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

      - Requires digestPassword to be `true`.

* - `digestPassword`
  - boolean
  - Optional. Indicates whether the server or the client digests the password.

    If `true` (default), the server receives undigested password from the client and
    digests the password.

    If `false`, the client digests the password and passes the digested
    password to the server. Not compatible with `SCRAM-SHA-256`

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

### Roles

In the `roles` field, you can specify both
built-in roles and user-defined
roles.

To specify a role that exists in the same database where
`updateUser` runs, you can either specify the role with the name of
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

## Behavior

**Warning:**

By default, `updateUser` sends all specified data to the MongoDB 
instance in cleartext, even if using `passwordPrompt()`. Use
TLS transport encryption to protect communications between clients
and the server, including the password sent by `updateUser`. For
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
   "_id" : "products.appClient01",
   "userId" : UUID("c5d88855-3f1e-46cb-9c8b-269bef957986"),
   "user" : "appClient01",
   "db" : "products",
   "customData" : { "empID" : "12345", "badge" : "9156" },
   "roles" : [
       { "role" : "readWrite",
         "db" : "products"
       },
       { "role" : "read",
         "db" : "inventory"
       }
   ],
   "mechanisms" : [
      "SCRAM-SHA-1",
      "SCRAM-SHA-256"
   ]
}
```

The following `updateUser` command **completely** replaces the
user's `customData` and `roles` data:

```javascript
use products
db.runCommand( {
   updateUser : "appClient01",
   customData : { employeeId : "0x3039" },
   roles : [ { role : "read", db : "assets" } ]
} )
```

The user `appClient01` in the `products` database now has the following
user information:

```javascript
{
   "_id" : "products.appClient01",
   "userId" : UUID("c5d88855-3f1e-46cb-9c8b-269bef957986"),
   "user" : "appClient01",
   "db" : "products",
   "customData" : { "employeeId" : "0x3039" },
   "roles" : [
       { "role" : "read",
         "db" : "assets"
       }
   ],
   "mechanisms" : [
      "SCRAM-SHA-1",
      "SCRAM-SHA-256"
   ]

}
```
