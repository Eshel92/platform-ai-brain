<!-- Converted from tutorial/configure-ssl-connection-to-backing-mongodb.txt (reStructuredText). Includes are inlined. -->

# Configure the Connections to the Application Database

If your Ops Manager Application Database uses
authentication or TLS (Transport Layer Security), update the connection settings from Ops Manager
to the Ops Manager Application database in the `conf-mms.properties` file.

## Prerequisites

This tutorial assumes you deployed the mms-application-database
and configured it to use authentication, TLS (Transport Layer Security), or both.

**See also:**

To learn how to deploy MongoDB with access control or to use TLS (Transport Layer Security),
see Security Concepts in the MongoDB
manual.

## Configure Ops Manager to Authenticate with Application Databases

Ops Manager can authenticate with the Ops Manager Application databases using one of
the following methods:

**Using MongoDB Community**

- Username and Password (`MONGODB-CR`/`SCRAM-SHA-1`/`SCRAM-SHA-256`)
- LDAP (Lightweight Directory Access Protocol)
- X.509 Client Certificates

**Using MongoDB Enterprise**

- Username and Password (`MONGODB-CR`/`SCRAM-SHA-1`/`SCRAM-SHA-256`)
- LDAP (Lightweight Directory Access Protocol)
- Kerberos
- X.509 Client Certificates

If your Ops Manager Application database uses authentication, you must configure
Ops Manager to be able to connect to the database.

**Step 1: Open the `conf-mms.properties` file with elevated privileges.**

Open the `conf-mms.properties` file in your preferred text editor
with `root` privileges.

This file configures Ops Manager's connection to the
mms-application-database.

**Step 2: Configure Ops Manager to connect to the Ops Manager Application Database.**

`mongo.mongoUri` contains the connection string used to
access the mms-application-database. The connection string
**must** include the following when applicable:

- All members of the replica set, if the Ops Manager Application database is a
  replica set.

- Authentication credentials for the `authentication
  mechanism` used on the Ops Manager Application
  database.

The `mongo.mongoUri` reference provides examples of the
connection string format for each authentication mechanism and
details the required permissions for the connecting user.

These include any
connection string options
that a MongoDB database could use. These options include, but aren't
limited to, TLS (Transport Layer Security), set read and write concerns, and authentication.

**Example:**

For an Ops Manager Application Database using Kerberos authentication, the
`mongo.mongoUri` setting might resemble:

```ini
mongo.mongoUri=mongodb://username%40REALM.example.net@mydb1.example.net:
40000/?authMechanism=GSSAPI
```

**Step 3: Configure any other authentication mechanism-specific settings.**

Edit the following settings in  `conf-mms.properties`:

**kerberos:**

If you are using Kerberos authentication, you must
configure the Kerberos settings, as in the following:

```ini
jvm.java.security.krb5.kdc=kdc.example.com
jvm.java.security.krb5.realm=EXAMPLE.COM
mms.kerberos.principal=mms/mmsweb.example.com@EXAMPLE.COM
mms.kerberos.keyTab=/path/to/mms.keytab
```

**x509:**

If you are using x.509 Client Certificate Authentication,
you must also be connecting over TLS (Transport Layer Security)/SSL (Secure Sockets Layer). The next
section, configure-ssl-backing, covers the TLS (Transport Layer Security)/SSL (Secure Sockets Layer)
configuration instructions.

**Step 4: Restart all the Ops Manager instances, including those with the Backup Daemon enabled.**

If the Ops Manager Application Database runs using TLS (Transport Layer Security), proceed to the
SSL configuration tutorial.

Restart Ops Manager using the appropriate command for your platform:

**linux-pkg:**

```sh
sudo service mongodb-mms restart
```

**linux-tar:**

```sh
<install_dir>/bin/mongodb-mms restart
```

## Configure TLS (Transport Layer Security) Connections to Application Database

To enable TLS (Transport Layer Security) connections to the Ops Manager Application database, follow this
procedure.

**Step 1: Open the `conf-mms.properties` file with `root` privileges.**

This file configures Ops Manager's connection to the mms-application-database.

**Step 2: Configure Ops Manager to connect to the Ops Manager Application Database over SSL.**

Configure the following settings in `conf-mms.properties`:

| Option | Setting |
|---|---|
| \| `mongo` \| `.ssl` | Set this to `true` to indicate that the mms-application-database is using TLS (Transport Layer Security)/SSL (Secure Sockets Layer). |
| \| `mongodb` \| `.ssl` \| `.CAFile` | Specify the PEM file that contains the root certificate chain from the Certificate Authority that signed the MongoDB server certificate. |
| \| `mongodb` \| `.ssl` \| `.PEMKeyFile` | If the MongoDB instance is running with `--sslCAFile` option, specify the PEM file containing an x.509 certificate and private key. The `Extended Key Usage` field of that certificate should include `TLS Web client authentication`. |
| \| `mongodb` \| `.ssl` \| `.PEMKeyFilePassword` | If the client PEM file contains an encrypted private key, specify the password for PEM file. To encrypt this password in the configuration file, use the Ops Manager `credentialstool` tool. See credentialstool. |

**Step 3: Restart all the Ops Manager instances, including those with the Backup Daemon enabled.**

Restart Ops Manager using the appropriate command for your platform:

**linux-pkg:**

```sh
sudo service mongodb-mms restart
```

**linux-tar:**

```sh
<install_dir>/bin/mongodb-mms restart
```
