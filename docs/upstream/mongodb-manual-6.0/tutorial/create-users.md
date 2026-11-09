<!-- Converted from tutorial/create-users.txt (reStructuredText). Includes are inlined. -->

# Create a User on Self-Managed Deployments

With access control enabled, users are required to identify themselves.
You have to grant a user one or more roles. A role grants
a user privileges to perform certain actions on MongoDB resources.

Each application and user of a MongoDB system should map to a distinct
user. This principle of *access isolation* facilitates access revocation
and ongoing user maintenance. To ensure a system of least
privilege, only grant the minimal set of privileges required to a user.

The user information on this page applies to self-managed deployments hosted in 
all of the following environments unless specified otherwise:

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## MongoDB Atlas Compatibility

The following limitations apply only to deployments hosted in
MongoDB Atlas. If any of these limits present a problem for your organization, 
contact Atlas support.

* You must use the Atlas CLI, 
  Atlas Administration API, 
  Atlas UI, or a supported integration 
  to add, modify, or delete database users on MongoDB Atlas clusters.
  Otherwise, MongoDB Atlas rolls back any user modifications. To add users 
  in MongoDB Atlas, see add-mongodb-users in the MongoDB Atlas documentation.

* The available MongoDB Atlas built-in roles 
  and specific privileges 
  support a subset of MongoDB commands. 
  See Unsupported Commands in M10+ Clusters 
  for more information.

* MongoDB Atlas supports a maximum of 100 database users per MongoDB Atlas
  project. If you require more than 100 database users on a project,
  contact Atlas support.

## Prerequisites

To be able to create users, you need to:

- enable access control
- create a user administrator

For routine user creation, you must possess the following permissions:

- To create a new user in a database, you must have the
  `createUser` action on
  that database resource.

- To grant roles to a user, you must have the `grantRole`
  action on the role's database.

The `userAdmin` and
`userAdminAnyDatabase` built-in roles provide
`createUser` and `grantRole` actions on their
respective resources.

## Steps

**Note:**

The following procedures use authentication-scram
authentication. For additional information on other authentication
mechanisms, see create-users-examples.

To configure database users for your self-managed MongoDB Enterprise 
or MongoDB Community deployment, follow these steps:

**Step 1: Connect and authenticate**

Using `mongosh`, connect to your primary
`mongod` or, in a sharded cluster, connect to your
`mongos` and authenticate as a user administrator or a
user with the required privileges:

tabs:
   - id: cmdline
     name: Authenticate during Connection
     content: |
        Start `mongosh` with the `-u
        <username>`, `-p`, and the
        `--authenticationDatabase <database>` command line options:

        ```bash
        mongosh --port 27017  --authenticationDatabase \
            "admin" -u "myUserAdmin" -p
        ```

        Enter your password when prompted.

   - id: authafter
     name: Authenticate after Connection
     content: |

        Using `mongosh`, connect to your database
        deployment:

        ```bash
        mongosh --port 27017
        ```

        In `mongosh`, switch to the
        authentication database (in this case, `admin`), and
        use the `db.auth(<username>, <pwd>)` method to authenticate:

        ```javascript
        use admin
        db.auth("myUserAdmin", passwordPrompt()) // or cleartext password
        ```

        **Tip:**

        The `passwordPrompt()` method prompts you to enter the
        password. You can also specify your password directly as a string. We
        recommend to use the `passwordPrompt()` method to avoid the
        password being visible on your screen and potentially leaking the
        password to your shell history.

        Enter the password when prompted.

**Step 2: Create additional users for your deployment**

**Note:**

The following step uses authentication-scram authentication.
For additional information on other authentication mechanisms, see
create-users-examples.

After authenticating as the user administrator, use the
`db.createUser()` method to create additional users. You can assign
any built-in roles or
user-defined roles to the
users.

The following operation adds a user `myTester` to the `test`
database who has the `readWrite` role in the `test`
database as well as the `read` role in the `reporting`
database.

```javascript
use test
db.createUser(
  {
    user: "myTester",
    pwd:  passwordPrompt(),   // or cleartext password
    roles: [ { role: "readWrite", db: "test" },
             { role: "read", db: "reporting" } ]
  }
)
```

**Tip:**

The `passwordPrompt()` method prompts you to enter the
password. You can also specify your password directly as a string. We
recommend to use the `passwordPrompt()` method to avoid the
password being visible on your screen and potentially leaking the
password to your shell history.

The database where you create the user (in this example, `test`) is
that user's authentication database. Although the user authenticates to
this database, the user can have roles in other databases. The
user's authentication database does not limit the user's privileges.

After creating the additional users, exit `mongosh`.

**Step 3: Connect to the instance and authenticate as `myTester`**

**Important:**

It is not possible to switch between users in the same
`mongosh` session. Authenticating as a different user
means the session has the privileges of **both** authenticated
users. To switch between users exit and relaunch
`mongosh`.

After exiting `mongosh` as `myUserAdmin`, reconnect as
`myTester`:

tabs:
   - id: cmdline2
     name: Authenticate during Connection
     content: |
        Start `mongosh` with the `-u
        <username>`, `-p`, and the
        `--authenticationDatabase <database>` command line options:

        ```bash
        mongosh --port 27017 -u "myTester" \
            --authenticationDatabase "test" -p
        ```

        Enter the password for the user when prompted.

   - id: authafter2
     name: Authenticate after Connection
     content: |

        Using `mongosh`, connect to your database
        deployment:

        ```bash
        mongosh --port 27017
        ```

        In `mongosh`, switch to the
        authentication database (in this case, `admin`), and
        use the `db.auth(<username>, <pwd>)` method to authenticate:

        ```javascript
        use test
        db.auth("myTester", passwordPrompt())  // or cleartext password
        ```

        **Tip:**

        The `passwordPrompt()` method prompts you to enter the
        password. You can also specify your password directly as a string. We
        recommend to use the `passwordPrompt()` method to avoid the
        password being visible on your screen and potentially leaking the
        password to your shell history.

        Enter the password for the user when prompted.

**Step 4: Insert a document as `myTester`**

As the user `myTester`, you have privileges to perform read and
write operations in the `test` database (as well as perform read
operations in the `reporting` database). Once authenticated as
`myTester`, insert a document into a collection in the `test`
database. For example, you can perform the following insert
operation in the `test` database:

```javascript
db.foo.insertOne( { x: 1, y: 1 } )
```

**See also:**

/tutorial/manage-users-and-roles

## Additional Examples

### Username/Password Authentication

The following operation creates a user in the `reporting`
database with the specified name, password, and roles.

**Tip:**

The `passwordPrompt()` method prompts you to enter the
password. You can also specify your password directly as a string. We
recommend to use the `passwordPrompt()` method to avoid the
password being visible on your screen and potentially leaking the
password to your shell history.

```javascript
use reporting
db.createUser(
  {
    user: "reportsUser",
    pwd: passwordPrompt(),  // or cleartext password
    roles: [
       { role: "read", db: "reporting" },
       { role: "read", db: "products" },
       { role: "read", db: "sales" },
       { role: "readWrite", db: "accounts" }
    ]
  }
)
```

### Kerberos Authentication

Users that authenticate to MongoDB using an external authentication
mechanism, such as Kerberos, must be created in the `$external`
database, which allows `mongos` or `mongod`
to consult an external source for authentication.

To use sessions with `$external` authentication users
(Kerberos, LDAP, or X.509 users), usernames cannot be greater
than 10k bytes.

For Kerberos authentication, you must add the Kerberos principal as the
username. You do not need to specify a password.

The following operation adds the Kerberos principal
`reportingapp@EXAMPLE.NET` with read-only access to the `records`
database:

```javascript
use $external
db.createUser(
    {
      user: "reportingapp@EXAMPLE.NET",
      roles: [
         { role: "read", db: "records" }
      ]
    }
)
```

**See also:**

For more information about setting up Kerberos authentication for
your MongoDB deployment, see the following tutorials:

- /tutorial/control-access-to-mongodb-with-kerberos-authentication
- /tutorial/control-access-to-mongodb-windows-with-kerberos-authentication

### LDAP Authentication

Users that authenticate to MongoDB using an external authentication
mechanism, such as LDAP, must be created in the `$external`
database, which allows `mongos` or `mongod`
to consult an external source for authentication.

To use sessions with `$external` authentication users
(Kerberos, LDAP, or X.509 users), usernames cannot be greater
than 10k bytes.

For LDAP authentication, you must specify a username. You do not need
to specify the password, as that is handled by the LDAP service.

The following operation adds the `reporting` user with read-only
access to the `records` database:

```javascript
use $external
db.createUser(
    {
      user: "reporting",
      roles: [
         { role: "read", db: "records" }
      ]
    }
)
```

**See also:**

For more information about setting up LDAP authentication for
your MongoDB deployment, see the following tutorials:

- /tutorial/configure-ldap-sasl-activedirectory
- /tutorial/configure-ldap-sasl-openldap

### X.509 Client Certificate Authentication

Users that authenticate to MongoDB using an external authentication
mechanism, such as X.509 Client Certificate Authentication, must be created in the `$external`
database, which allows `mongos` or `mongod`
to consult an external source for authentication.

To use sessions with `$external` authentication users
(Kerberos, LDAP, or X.509 users), usernames cannot be greater
than 10k bytes.

For X.509 Client Certificate authentication, you must add the value of
the `subject` from the client certificate as a MongoDB user. Each
unique X.509 client certificate corresponds to a single MongoDB user.
You do not need to specify a password.

The following operation adds the client certificate subject
`CN=myName,OU=myOrgUnit,O=myOrg,L=myLocality,ST=myState,C=myCountry`
user with read-only access to the `records` database.

```javascript
use $external
db.createUser(
    {
      user: "CN=myName,OU=myOrgUnit,O=myOrg,L=myLocality,ST=myState,C=myCountry",
      roles: [
         { role: "read", db: "records" }
      ]
    }
)
```

**See also:**

For more information about setting up X.509 Client Certificate
authentication for your MongoDB deployment, see the following
tutorials:

- /tutorial/configure-x509-client-authentication

## Next Steps

To manage users, assign roles, and create custom roles for your
self-managed MongoDB Enterprise or MongoDB Community deployment, 
see /tutorial/manage-users-and-roles.
