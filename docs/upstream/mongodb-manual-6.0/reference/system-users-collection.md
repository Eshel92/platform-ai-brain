<!-- Converted from reference/system-users-collection.txt (reStructuredText). Includes are inlined. -->

# `system.users` Collection in Self-Managed Deployments

The `system.users` collection in the `admin` database stores user
authentication and authorization information. To manage data in this collection,
MongoDB provides user management commands.

## `system.users` Schema

The documents in the `system.users` collection have the following
schema:

```javascript
{
  _id: <system defined id>,
  userId : <system assigned UUID>, 
  user: "<name>",
  db: "<database>",
  credentials: { <authentication credentials> },
  roles: [
           { role: "<role name>", db: "<database>" },
           ...
         ],
  customData: <custom information>,
  authenticationRestrictions : [ <documents> ]
 }
```

Each `system.users` document has the following fields:

**`admin.system.users.userId`**

A unique identifier for the user assigned to the user upon creation.

**`admin.system.users.user`**

The user name. A user exists in the context of a single logical
database (see `admin.system.users.db`) but can have access on
other databases through roles specified in the
`roles` array.

**`admin.system.users.db`**

The authentication database
associated with the user. The user's privileges are not necessarily
limited to this database. The user can have privileges in additional
databases through the `roles` array.

**`admin.system.users.credentials`**

User's authentication information. For users with externally stored
authentication credentials, such as users that use Kerberos
or X.509 certificates for authentication, the `system.users`
document for that user does not contain the
`credentials` field. For
authentication-scram user credentials, the information
includes the mechanism,  iteration count, and authentication parameters.

**See also:**

- `scramSHA256IterationCount`
- `scramIterationCount`

**`admin.system.users.roles`**

An array of roles granted to the user. The array contains both
built-in roles and user-defined role.

A role document has the following syntax:

```javascript
{ role: "<role name>", db: "<database>" }
```

A role document has the following fields:

**`admin.system.users.roles[n].role`**

The name of a role. A role can be a built-in role provided by MongoDB or a custom
user-defined role.

**`admin.system.users.roles[n].db`**

The name of the database where role is defined.

When specifying a role using the role management or user management commands, you can specify the role name alone
(e.g. `"readWrite"`) if the role that exists on the database on which
the command is run.

**`admin.system.users.customData`**

Optional custom information about the user.

**`admin.system.users.authenticationRestrictions`**

An array of authentication restrictions the server enforces for the
user. The array containsa list of IP addresses and CIDR ranges from
which the user is allowed to connect to the server or from which the
server can accept users.

## Example

Consider the following document in the `system.users` collection:

```javascript
{
   "_id" : "home.Kari",
   "userId" : UUID("ec1eced7-055a-4ca8-8737-60dd02c52793"), 
   "user" : "Kari",
   "db" : "home",
   "credentials" : {
      "SCRAM-SHA-1" : {
         "iterationCount" : 10000,
         "salt" : "S/xM2yXFosynbCu4GzFDgQ==",
         "storedKey" : "Ist4cgpEd1vTbnRnQLdobgmOsBA=",
         "serverKey" : "e/0DyzS6GPboAA2YNBkGYm87+cg="
      },
      "SCRAM-SHA-256" : {
         "iterationCount" : 15000,
         "salt" : "p1G+fZadAeYAbECN8F/6TMzXGYWBaZ3DtWM0ig==",
         "storedKey" : "LEgLOqZQmkGhd0owm/+6V7VdJUYJcXBhPUvi9z+GBfk=",
         "serverKey" : "JKfnkVv9iXwxyc8JaapKVwLPy6SfnmB8gMb1Pr15T+s="
      }
   },
   "authenticationRestrictions" : [  
      { "clientSource" : [ "69.89.31.226" ], "serverAddress" : [ "172.16.254.1" ] }
   ], 
   "customData" : {
      "zipCode" : "64157"
   },
   "roles" : [
      {
         "role" : "read",
         "db" : "home"
      },
      {
         "role" : "readWrite",
         "db" : "test"
      }
   ]
}
```

The document shows that a user `Kari`'s authentication database is
the `home` database. `Kari` has the `read` role in the
`home` database, the `readWrite` role in the `test`
database.
