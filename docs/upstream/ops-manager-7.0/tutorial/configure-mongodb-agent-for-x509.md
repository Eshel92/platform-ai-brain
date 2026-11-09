<!-- Converted from tutorial/configure-mongodb-agent-for-x509.txt (reStructuredText). Includes are inlined. -->

# Configure the MongoDB Agent for X.509 Authentication

Ops Manager enables you to configure the Authentication Mechanisms that all
clients, including the Ops Manager Agents, use to connect to your MongoDB
deployments. You can enable multiple authentication mechanisms for each
of your projects, but you must choose only one mechanism for the Agents.

MongoDB supports X.509 certificate authentication for use
with a secure TLS
connection. X.509 client authentication allows clients to authenticate
to servers with certificates rather than with a username and password.

**Note:**

With Automation, Ops Manager manages MongoDB Agent authentication for
you. To learn more about authentication, see /tutorial/enable-x509-authentication-for-group.

## Considerations

A full description of
Transport Layer Security,
public key infrastructure,
X.509 certificates, and
Certificate Authorities
exceeds the scope of this tutorial. This tutorial assumes prior
knowledge of TLS (Transport Layer Security) and access to valid X.509 certificates.

## Prerequisites

To enable X.509 Authentication for Ops Manager, you must obtain valid TLS (Transport Layer Security)
certificates that a single certificate authority (CA) generated and
signed. To learn more about the certificate requirements, see
Client x.509 Certificate in the MongoDB
Manual.

X.509 Client Certificate Authentication requires you to
enable and configure
TLS (Transport Layer Security) for the deployment.

## Procedures

This tutorial assumes that you have already configured your MongoDB
deployment to use X.509 certificate authentication and TLS (Transport Layer Security). If you
have not done so, refer to the
Use X.509 Certificates to Authenticate Clients and
Configure mongod and mongos for TLS
tutorials.

### Create MongoDB User from the X.509 `subject`

**managed-x509:**

When Automation is activated, Ops Manager manages MongoDB Agent authentication.

To configure X.509 for MongoDB Agent authentication, see
enable-x509-for-project.

**unmanaged-x509:**

For the MongoDB Agent to connect to your MongoDB deployment, you must create a MongoDB user on your deployment that corresponds to the `subject` value of your client certificate.

Where you create the MongoDB user depends upon whether or not you are
using LDAP authorization.

**ldap-auth-x509:**

If you are using LDAP (Lightweight Directory Access Protocol) authorization in your MongoDB deployment,
you must create an LDAP (Lightweight Directory Access Protocol) user and LDAP (Lightweight Directory Access Protocol) group for the
MongoDB Agent on the LDAP (Lightweight Directory Access Protocol) server. After creating the LDAP (Lightweight Directory Access Protocol) user
and group, map the LDAP (Lightweight Directory Access Protocol) group to a MongoDB role in your
deployment's `admin` database.

**Warning:**

When using LDAP (Lightweight Directory Access Protocol) Authorization, do not create *any* MongoDB
users in the `$external` database. MongoDB 3.4 and later
does not start if a MongoDB user exists in the `$external`
database and LDAP (Lightweight Directory Access Protocol) authorization is enabled.

For the MongoDB user representing the MongoDB Agent:

#. Create a new LDAP (Lightweight Directory Access Protocol) user on your LDAP (Lightweight Directory Access Protocol) server named that uses
   the `subject` value of your client certificate as the
   username.

#. Create an LDAP (Lightweight Directory Access Protocol) group whose name matches the MongoDB Agent's
   role.

#. Create the MongoDB Agent's role in your `admin` database with
   the appropriate permissions.

   **Note:**

   When Automation is activated, Automation automatically
   creates a role for for the MongoDB Agent user for LDAP (Lightweight Directory Access Protocol) authentication.

#. Assign the LDAP (Lightweight Directory Access Protocol) user to the LDAP (Lightweight Directory Access Protocol) group.

**See also:**

| To learn how to: | See |
|---|---|
| Create an LDAP (Lightweight Directory Access Protocol) user | Documentation for your LDAP (Lightweight Directory Access Protocol) implementation. |
| Create an LDAP (Lightweight Directory Access Protocol) group | Documentation for your LDAP (Lightweight Directory Access Protocol) implementation. |
| Assign the appropriate roles for the MongoDB Agent | /reference/required-access-mongodb-agent. |
| Map an LDAP (Lightweight Directory Access Protocol) group and MongoDB role | LDAP Roles section of the LDAP authorization page in the MongoDB manual. |
| Configure LDAP (Lightweight Directory Access Protocol) authorization without Ops Manager automation | LDAP Authorization page in the MongoDB manual. |

**no-ldap-auth-kerbersos-principal:**

If you are not using LDAP (Lightweight Directory Access Protocol) authorization, you must add the `subject` value of your client certificate as the username
of the MongoDB Agent in the `$external` database of your
MongoDB deployment. Without LDAP (Lightweight Directory Access Protocol) authorization, MongoDB uses
the `$external` database to authenticate a user against
X.509.

**Note:**

To discover the appropriate roles for the MongoDB Agent, see
/reference/required-access-mongodb-agent.

Use the following commands to create the users from `mongosh`:

```javascript
db.getSiblingDB("$external").createUser(
  {
    user : "<x.509 subject>",
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

To learn what access is required, see
/reference/required-access-mongodb-agent.

Each MongoDB user must have its own X.509 certificate.

### Edit MongoDB Agent Configuration File

To use X.509 authentication, you must configure the MongoDB Agent for
TLS (Transport Layer Security):

**Step 1: Specify the absolute file path to your trusted CA certificate in the MongoDB Agent config file.**

If you enabled TLS (Transport Layer Security) for your Ops Manager deployment, then you must
configure the MongoDB Agent to use TLS. To configure the MongoDB Agent to
use TLS (Transport Layer Security), you must have the trusted Certificate Authority certificate that
signed the MongoDB instance's certificate.

In the MongoDB Agent's install directory, edit the configuration
file to set `httpsCAFile` field to the
path of a file containing one or more certificates in PEM (Privacy-Enhanced Mail) format.

**windows:**

The location of the MongoDB Agent configuration file is
`C:\MMSData\Automation\automation-agent.config`.

**Note:**

The MongoDB Agent configuration file is named
`automation-agent.config` as a way to enable easier upgrades
for those using legacy agents.

**linux:**

The location of the MongoDB Agent configuration file is
`/path/to/install/local.config`.

**rhel:**

The location of the MongoDB Agent configuration file is
`/etc/mongodb-mms/automation-agent.config`.

**Note:**

The MongoDB Agent configuration file is named
`automation-agent.config` as a way to enable easier upgrades
for those using legacy agents.

**debian:**

The location of the MongoDB Agent configuration file is
`/etc/mongodb-mms/automation-agent.config`.

**Note:**

The MongoDB Agent configuration file is named
`automation-agent.config` as a way to enable easier upgrades
for those using legacy agents.

**Example:**

Use the following command to connect through `mongosh`:

```sh
mongosh --tls --tlsCAFile /etc/ssl/ca.pem example.net:27017
```

Then, modify the configuration file and set the following
key/value pair:

```ini
httpsCAFile=/etc/ssl/ca.pem
```

Save the configuration file.

To learn more about these settings, see
mongodb-agent-ssl-settings.

**Step 2: Restart the MongoDB Agent.**

/tutorial/configure-mongodb-agent-for-tls provides more
details about configuring the MongoDB Agent for TLS (Transport Layer Security).

After you configure the MongoDB Agent, 
configure the X.509 Authentication mechanism in the Ops Manager interface, as
described in /tutorial/enable-x509-authentication-for-group.
