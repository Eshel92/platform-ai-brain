<!-- Converted from tutorial/configure-mongodb-agent-for-kerberos.txt (reStructuredText). Includes are inlined. -->

# Configure the MongoDB Agent for Kerberos

`MongoDB Enterprise` supports
Kerberos. [Kerberos](https://web.mit.edu/kerberos/) is a network
authentication protocol. The MongoDB Agent can authenticate to
MongoDB instances that run Kerberos.

## Prerequisites

### Configure KDC to Issue Tickets with Four-Hour Minimum Lifetime

Kerberos tickets can authenticate users for a limited time. You must
[configure the Kerberos Key Distribution Center (KDC)](https://web.mit.edu/Kerberos/www/krb5-devel/doc/admin/conf_files/kdc_conf.html#kdc-conf-5)
to issue tickets that are valid for four hours or longer. The
MongoDB Agent periodically renews the ticket. The KDC (Key Distribution Center) service provides
session tickets and temporary session keys to users and hosts.

### Add Kerberos as Authentication Mechanism for Deployment

The MongoDB Agent interacts with the MongoDB databases in your
deployment as a MongoDB user would. As a result, you must configure
your MongoDB deployment and the MongoDB Agent to support authentication.

You can specify the deployment's authentication mechanisms when
adding the
deployment, or you can edit the settings for an existing
deployment. At minimum, the deployment must enable the authentication
mechanism you want the MongoDB Agent to use. The MongoDB Agent can use
any supported authentication mechanism.

For the purposes of this tutorial, you must ensure the following:

- Your deployment supports Kerberos authentication and
- MongoDB Agent uses Kerberos authentication.

To learn how to enable Kerberos authentication, see
/tutorial/enable-kerberos-authentication-for-group.

### Configure MongoDB Agent Host to Use Kerberos

The following Kerberos configuration files are required on any host
running Monitoring or Backup: 

- Create or configure the 
  [krb5.conf](https://web.mit.edu/kerberos/krb5-1.12/doc/admin/conf_files/krb5_conf.html) 
  Kerberos configuration file.

  | Platform | Default Path | Notes |
  |---|---|---|
  | Linux | `/etc/krb5.conf` |  |
  | Windows | `%WINDIR%\krb5.ini` | This is the default path for non-Active Directory-based Kerberos implementations. Refer to the documentation for your Kerberos implementation for your version of Windows to find out where the Kerberos configuration file is stored. |

- On Linux systems, ensure that the [kinit](http://web.mit.edu/KERBEROS/krb5-devel/doc/user/user_commands/kinit.html)
  binary is located at `/usr/bin/kinit`. `kinit`
  obtains or renews a Kerberos ticket-granting ticket, which
  authenticates the Agent using Kerberos.

## Procedures

### Create Kerberos User Principal for the MongoDB Agent

**Step 1: Create or choose a Kerberos User Principal Name (UPN (User Principal Name)) for the MongoDB Agent.**

An UPN (User Principal Name) is formatted in two parts so the service can be uniquely
identified across the Kerberos realm:

| Component | Description |
|---|---|
| Service name | The name of one service a host is providing to the Kerberos realm, such as `pop` or `ftp`. |
| Kerberos realm | A set of managed hosts and services that share the same Kerberos database. By Kerberos naming convention, the `<KERBEROS_REALM>` must be in all `UPPERCASE`. |

**Example:**

In a Kerberos realm set as `EXAMPLE.COM`, the MongoDB Agent
would set its UPN (User Principal Name) to: `mongodb-agent@EXAMPLE.COM`

**Step 2: Generate a `keytab` file for the Kerberos UPN (User Principal Name) of the MongoDB Agent.**

Generate a [keytab](https://web.mit.edu/kerberos/krb5-latest/doc/basic/keytab_def.html)
file (`*.keytab`) for the MongoDB Agent UPN (User Principal Name) and copy it to the
host that runs the MongoDB Agent. Ensure that the operating system
user that runs the MongoDB Agent is the same operating system user
that owns the `keytab` file.

### Create a User and Assign Roles for the MongoDB Agent UPN

**managed-kerberos:**

When Automation is activated, Ops Manager manages MongoDB Agent authentication.

To configure Kerberos for MongoDB Agent authentication, see
/tutorial/enable-kerberos-authentication-for-group.

**unmanaged-kerberos:**

After creating the Kerberos UPN (User Principal Name) for the MongoDB Agent, create a
MongoDB user on your deployment that corresponds to the MongoDB Agent's
UPN (User Principal Name) and grant it privileges.

Where you create the MongoDB user depends upon whether or not you are
using LDAP authorization.

**ldap-auth-kerberos-principal:**

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

#. Create a new LDAP (Lightweight Directory Access Protocol) user on your LDAP (Lightweight Directory Access Protocol) server named with the
   MongoDB Agent's UPN (User Principal Name).

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

If you are not using LDAP (Lightweight Directory Access Protocol) authorization, you must add the
MongoDB Agent's UPN (User Principal Name) as a user in `$external` database in your
MongoDB deployment. Without LDAP (Lightweight Directory Access Protocol) authorization, MongoDB uses
the `$external` database to authenticate a user against
Kerberos.

**Note:**

To discover the appropriate roles for the MongoDB Agent, see
/reference/required-access-mongodb-agent.

From `mongosh`, issue the following commands to create the MongoDB 
user:

```javascript
db.getSiblingDB("$external").createUser(
  {
    user : "<Kerberos Principal>",
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
