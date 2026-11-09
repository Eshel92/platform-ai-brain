<!-- Converted from tutorial/configure-mongodb-agent-for-ldap.txt (reStructuredText). Includes are inlined. -->

# Configure MongoDB Agent for LDAP

If your MongoDB deployment enforces access control, the MongoDB Agent
must authenticate to MongoDB as a user with the proper access. If you
use Automation, Ops Manager takes care of this for you.

MongoDB Enterprise supports simple and SASL binding to LDAP (Lightweight Directory Access Protocol) servers
via `saslauthd` and operating system libraries:

- MongoDB Enterprise for Linux can bind to an LDAP (Lightweight Directory Access Protocol) server either
  via `saslauthd` or via operating system libraries.

- MongoDB Enterprise for Windows can bind to an LDAP (Lightweight Directory Access Protocol) server via the
  operating system libraries.

MongoDB Agent support authenticating to MongoDB instances using LDAP (Lightweight Directory Access Protocol).

**Note:**

With Automation, Ops Manager manages MongoDB Agent authentication for
you. To learn more about authentication, see /tutorial/enable-ldap-authentication-for-group.

## Prerequisites

### Configure Deployments to Use Authentication

The MongoDB Agent interacts with the MongoDB databases in your
deployment as a MongoDB user would. As a result, you must configure
your MongoDB deployment and the MongoDB Agent to support authentication.

You can specify the deployment's authentication mechanisms when
adding the
deployment, or you can edit the settings for an existing
deployment. At minimum, the deployment must enable the authentication
mechanism you want the MongoDB Agent to use. The MongoDB Agent can use
any supported authentication mechanism.

### Set Require TLS Certificate Environment Variable

On the MongoDB Agent hosts, you must set the
[TLS_REQCERT](https://www.openldap.org/doc/admin21/tls.html#TLS_REQCERT%20%7B%20never%20%7C%20allow%20%7C%20try%20%7C%20demand%20%7D)
environment variable to `demand`.

**Example:**

In a Red Hat Enterprise Linux host, open the
`/etc/openldap/ldap.conf` file and add the following setting and
value:

```sh
TLS_REQCERT demand
```

You can use your application to set this environment variable.

### Considerations

If Automation does not manage your deployment, you must configure
LDAP (Lightweight Directory Access Protocol) authentication separately for each function.

To configure LDAP authentication, add a host or edit
an existing host's configuration.

## Create and Configure User in MongoDB

**automation:**

To automate MongoDB instances that use LDAP (Lightweight Directory Access Protocol) authentication, add
a MongoDB user that possesses the required roles and privileges
to the `$external` database in MongoDB. The `$external`
database allows `mongod` to consult an external source, such as
an LDAP (Lightweight Directory Access Protocol) server, to authenticate.

Use the following commands to create the users from `mongosh`:

```javascript
db.getSiblingDB("$external").createUser(
  {
    user : "<username>",
    roles : [ 
      { role : "clusterAdmin", db : "admin" },
      { role : "readWriteAnyDatabase", db : "admin" },
      { role : "userAdminAnyDatabase", db : "admin" },
      { role : "dbAdminAnyDatabase", db : "admin" },
      { role : "backup", db : "admin" },
      { role : "restore", db : "admin" }
    ]
  }
)
```

To learn more about the required access, see
/reference/required-access-mongodb-agent.

**monitoring-backup-only:**

**backup:**

To back up MongoDB 4.0 or later instances that use LDAP (Lightweight Directory Access Protocol)
authentication, add a user that possess the required roles
to the `$external` database in MongoDB. The `$external`
database stores credentials for external authentication and
authorization details.

Use the following `mongosh` command to create the user:

**backup-fcv4.2:**

```javascript
db.getSiblingDB("$external").createUser(
    {
      user : "<username>",
      roles: [ {
        role: "clusterAdmin", db: "admin"
      } ]
    }
)
```

**backup-fcv4.0:**

```javascript
db.getSiblingDB("$external").createUser(
   {
     user: "<username>",
     roles: [ {
       role: "backup", db: "admin"
     } ]
   }
)
```

To learn more about the required access, see
Required Access for MongoDB Agent Backup

**monitoring:**

To monitor MongoDB 4.0 or later instances that use LDAP (Lightweight Directory Access Protocol)
authentication, add a user to the `$external` database in
MongoDB. The `$external` database stores credentials for
external authentication and authorization details. Assign
this user the roles provided in the following example.

Use the following `mongosh` command to create the user:

```javascript
db.getSiblingDB("$external").createUser(
    {
      user : "<username>",
      roles: [ { role: "clusterMonitor", db: "admin" } ]
    }
)
```

To learn what roles this function requires, see
Monitoring settings.
