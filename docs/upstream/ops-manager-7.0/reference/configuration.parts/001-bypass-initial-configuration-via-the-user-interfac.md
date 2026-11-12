<!-- Part 1 of 5 of reference/configuration.md (split because the page is big). -->

## Bypass Initial Configuration via the User Interface

If you would like to skip the initial setup wizard after creating the
first account and either edit the `conf-mms.properties` file or use
the API to configure Ops Manager, change the following settings. This
setting can help if you are automating the deployment of Ops Manager
instances.

**`mms.ignoreInitialUiSetup`**

*Type*: boolean

Set this to `true` to allow full use of Ops Manager without requiring
the first user account to complete the initial setup wizard.

**Warning:**

Ops Manager performs its regular pre-flight check to verify that it
has all of the required settings. If one or more of those
settings are not included in `conf-mms.properties`, Ops Manager
refuses to start and lists which fields are missing in the log
file.

Before starting Ops Manager, add the following required settings to
`conf-mms.properties` to enable basic Ops Manager functionality:

| UI Setting | `conf-mms.properties` Setting | Necessity |
|---|---|---|
| `URL to Access Ops Manager` | `mms.centralUrl` | Required |
| None | `mongo.mongoUri` | Required |
| `Client Certificate Mode` | `mms.https.ClientCertificateMode` | Required |
| `"From" Email Address` | `mms.fromEmailAddr` | Required |
| `"Reply To" Email Address` | `mms.replyToEmailAddr` | Required |
| `Admin Email Address` | `mms.adminEmailAddr` | Required |
| `Email Delivery Method Configuration` | `mms.emailDaoClass` | Required |
| `Transport` | `mms.mail.transport` | Required |
| `SMTP Server Hostname` | `mms.mail.hostname` | Required |
| `SMTP Server Port` | `mms.mail.port` | Required |
| `User Authentication Method` | `mms.userSvcClass` | Optional |
| `Snapshot Interval (Hours)` | `brs.snapshotSchedule.interval` | Optional |
| `Base Retention of Snapshots (in Days)` | `brs.snapshotSchedule.retention.base` | Optional |
| `Daily Retention of Snapshots (in Days)` | `brs.snapshotSchedule.retention.daily` | Optional |
| `Weekly Retention of Snapshots (in Weeks)` | `brs.snapshotSchedule.retention.weekly` | Optional |
| `Monthly Retention of Snapshots (in Months)` | `brs.snapshotSchedule.retention.monthly` | Optional |
| `Versions Directory` | `automation.versions.directory` | Optional |

**Note:**

Fields marked as *Optional* have default values. If you want to
change them, you can provide the setting and a new value.

**Example:**

The following values are examples. Substitute values appropriate
to your Ops Manager installation. You may add any of the other
settings specified in this reference.

To configure an Ops Manager installation with the minimum functionality,
add the following settings to `conf-mms.properties`:

```ini
mms.ignoreInitialUiSetup=true
mongo.mongoUri=mongodb://db1.example.com:27017,db2.example.com:27017,db3.example.com:27017
mms.centralUrl=http://localhost:8080
mms.fromEmailAddr=example@example.com
mms.replyToEmailAddr=example@example.com
mms.adminEmailAddr=example@example.com
mms.mail.transport=smtp
mms.mail.hostname=mail.example.com
mms.mail.port=465
```


## All Clusters View

**`mms.allclusters.onlyMembership`**

*Type*: boolean

*Default*: False

Determines whether the /tutorial/view-all-clusters displays
only the deployments to which an Ops Manager administrator belongs (set
the value to `true`) or the deployments to which the administrator
has access (set the value to `false`).


## Application Database Connection

The following settings configure the Ops Manager connection to the
mms-application-database. You must configure this setting in the
conf-mms.properties file on each Ops Manager
server. To encrypt authentication information, see
encrypt-mongodb-user-credentials.

**`mongo.mongoUri`**

*Type*: string

connection string used
to access the Ops Manager Application Database. If applicable, the connection
string **must** include the authentication credentials for the
`authentication mechanism`
used on the Ops Manager Application database.

How you format your connection string depends on:

- the type of cluster you deployed for your backing databases,
- the protocol you use, and
- the authentication method you use.

**replset:**

If you use a replica set for the database's
backing instance,
your connection string may include either the hostnames of all
replica set members or the hostname for the DNS (Domain Name System) seedlist.

**standardString:**

If you choose a standard connection string, include all members
of the replica set in the URI (Uniform Resource Identifier). If you omit the port number,
Ops Manager uses the default **27017** port for all hosts.

**none:**

```ini
mongo.mongoUri=mongodb://mongod1.example.com:40000,mongod2.example.com:40000,mongod3.example.com:40000
```

**scram:**

Prepend the MongoDB username and password to the hostname. Write the
username and password in this format: **<username>:<password>@**

```ini
mongo.mongoUri=mongodb://mongodbuser1:password@mongod1.example.com:40000,mongod2.example.com:40000,mongod3.example.com:40000
```

**Note:** Necessary MongoDB Roles

The MongoDB user that authenticates to the backing databases must
have the following roles:

- `readWriteAnyDatabase`

- `dbAdminAnyDatabase`

- `clusterAdmin` if the database is a sharded
  cluster, otherwise `clusterMonitor`

**x509:**

You should find the client certificate in the PEM (Privacy-Enhanced Mail) file you
specified in the `mongodb.ssl.PEMKeyFile` setting.

- Prepend the value of the *subject* from the
  client certificate as a MongoDB user
  to the host.

- Append **authMechanism=MONGODB-X509** to the specified port.

```ini
mongo.mongoUri=mongodb://<new_mongodb_user>@mongod1.example.com:40000,mongod2.example.com:40000,mongod3.example.com:40000/?authMechanism=MONGODB-X509
```

**ldap:**

- Prepend the MongoDB username and password to the hostname in this
  format: **<username>:<password>@**.

- Append the authentication mechanism to the port in this format:
  **authMechanism=PLAIN&authSource=$external**

```ini
mongo.mongoUri=mongodb://mongodbuser1:password@mongod1.example.com:40000,mongod2.example.com:40000,mongod3.example.com:40000/?authMechanism=PLAIN&authSource=$external
```

**kerberos:**

- Prepend the hostname with the Kerberos user principal.

  Write Kerberos UPN (User Principal Name)\s as **<username>@<KERBEROS REALM>**. Escape
  the UPN (User Principal Name) using the URL (Uniform Resource Locator) encoded representation. A Kerberos user
  principal of **username@REALM.EXAMPLE.COM** would therefore become
  **username%40REALM.EXAMPLE.COM**.

- Append the authentication mechanism to the port in this format:
  **authMechanism=GSSAPI**.

```ini
mongo.mongoUri=mongodb://username%40REALM.EXAMPLE.COM@mongod1.example.com:40000,mongod2.example.com:40000,mongod3.example.com:40000/?authMechanism=GSSAPI
```

**Note:** Modify Kerberos Settings

To enable Kerberos, modify the following settings:

- `jvm.java.security.krb5.conf`
- `jvm.java.security.krb5.kdc`
- `jvm.java.security.krb5.realm`
- `mms.kerberos.debug`
- `mms.kerberos.keyTab`
- `mms.kerberos.principal`

**Note:**

Ops Manager doesn't require the replicaSet
option in the URI (Uniform Resource Identifier).

**seedlistString:**

**New in version:** Ops Manager 4.4.0

If you choose a DNS (Domain Name System) seedlist connection string, include the
DNS (Domain Name System) SRV (Service) record that describes your database's backing instance
replica set. The connection string uses the **mongodb+srv:**
protocol, not the **mongodb:** protocol.

**none:**

```ini
mongo.mongoUri=mongodb+srv://db.example.com:40000
```

**scram:**

Prepend the MongoDB username and password to the hostname. Write the
username and password in this format: **<username>:<password>@**

```ini
mongo.mongoUri=mongodb+srv://mongodbuser1:password@mongod.example.com:40000
```

**Note:** Necessary MongoDB Roles

The MongoDB user that authenticates to the backing databases must
have the following roles:

- `readWriteAnyDatabase`

- `dbAdminAnyDatabase`

- `clusterAdmin` if the database is a sharded
  cluster, otherwise `clusterMonitor`

**x509:**

You should find the client certificate in the PEM (Privacy-Enhanced Mail) file you
specified in the `mongodb.ssl.PEMKeyFile` setting.

- Prepend the value of the *subject* from the
  client certificate as a MongoDB user
  to the host.

- Append **authMechanism=MONGODB-X509** to the specified port.

```ini
mongo.mongoUri=mongodb+srv://<new_mongodb_user>@mongod.example.com:40000/?authMechanism=MONGODB-X509
```

**ldap:**

- Prepend the MongoDB username and password to the hostname in this
  format: **<username>:<password>@**.

- Append the authentication mechanism to the port in this format:
  **authMechanism=PLAIN&authSource=$external**

```ini
mongo.mongoUri=mongodb+srv://mongodbuser1:password@mongod.example.com:40000/?authMechanism=PLAIN&authSource=$external
```

**kerberos:**

- Prepend the hostname with the Kerberos user principal.

  Write Kerberos UPN (User Principal Name)\s as **<username>@<KERBEROS REALM>**. Escape
  the UPN (User Principal Name) using the URL (Uniform Resource Locator) encoded representation. A Kerberos user
  principal of **username@REALM.EXAMPLE.COM** would therefore become
  **username%40REALM.EXAMPLE.COM**.

- Append the authentication mechanism to the port in this format:
  **authMechanism=GSSAPI**.

```ini
mongo.mongoUri=mongodb+srv://username%40REALM.EXAMPLE.COM@mongod.example.com:40000/?authMechanism=GSSAPI
```

**Note:** Modify Kerberos Settings

To enable Kerberos, modify the following settings:

- `jvm.java.security.krb5.conf`
- `jvm.java.security.krb5.kdc`
- `jvm.java.security.krb5.realm`
- `mms.kerberos.debug`
- `mms.kerberos.keyTab`
- `mms.kerberos.principal`

This option requires a DNS (Domain Name System) SRV (Service) record for the application
database. The DNS (Domain Name System) entry uses the DNS (Domain Name System) seedlist string format.
Make sure Ops Manager can connect to this application database.

**See also:**

DNS Seedlist Connection Format

**sharded:**

If you use a sharded cluster for the database's
backing instance,
your connection string may include either the hostnames of all
`mongos` routers or the hostname for the DNS (Domain Name System) seedlist.

**standardString:**

If you choose a standard connection string, include all shards in
the URI (Uniform Resource Identifier). If you omit the port number, Ops Manager uses the default
**27017** port for all hosts.

**none:**

```ini
mongo.mongoUri=mongodb://mongos1.example.com:40000,mongos2.example.com:40000
```

**scram:**

Prepend the MongoDB username and password to the hostname. Write the
username and password in this format: **<username>:<password>@**

```ini
mongo.mongoUri=mongodb://mongodbuser1:password@mongos1.example.com:40000,mongos2.example.com:40000
```

**Note:** Necessary MongoDB Roles

The MongoDB user that authenticates to the backing databases must
have the following roles:

- `readWriteAnyDatabase`

- `dbAdminAnyDatabase`

- `clusterAdmin` if the database is a sharded
  cluster, otherwise `clusterMonitor`

**x509:**

You should find the client certificate in the PEM (Privacy-Enhanced Mail) file you
specified in the `mongodb.ssl.PEMKeyFile` setting.

- Prepend the value of the *subject* from the
  client certificate as a MongoDB user
  to the host.

- Append **authMechanism=MONGODB-X509** to the specified port.

```ini
mongo.mongoUri=mongodb://<new_mongodb_user>@mongos1.example.com:40000,mongos2.example.com:40000/?authMechanism=MONGODB-X509
```

**ldap:**

- Prepend the MongoDB username and password to the hostname in this
  format: **<username>:<password>@**.

- Append the authentication mechanism to the port in this format:
  **authMechanism=PLAIN&authSource=$external**

```ini
mongo.mongoUri=mongodb://mongodbuser1:password@mongos1.example.com:40000,mongos2.example.com:40000/?authMechanism=PLAIN&authSource=$external
```

**kerberos:**

- Prepend the hostname with the Kerberos user principal.

  Write Kerberos UPN (User Principal Name)\s as **<username>@<KERBEROS REALM>**. Escape
  the UPN (User Principal Name) using the URL (Uniform Resource Locator) encoded representation. A Kerberos user
  principal of **username@REALM.EXAMPLE.COM** would therefore become
  **username%40REALM.EXAMPLE.COM**.

- Append the authentication mechanism to the port in this format:
  **authMechanism=GSSAPI**.

```ini
mongo.mongoUri=mongodb://username%40REALM.EXAMPLE.COM@mongos1.example.com:40000,mongos2.example.com:40000/?authMechanism=GSSAPI
```

**Note:** Modify Kerberos Settings

To enable Kerberos, modify the following settings:

- `jvm.java.security.krb5.conf`
- `jvm.java.security.krb5.kdc`
- `jvm.java.security.krb5.realm`
- `mms.kerberos.debug`
- `mms.kerberos.keyTab`
- `mms.kerberos.principal`

**Note:**

Ops Manager doesn't require the
replicaSet option in the URI (Uniform Resource Identifier).

**seedlistString:**

**New in version:** Ops Manager 4.4.0

If you choose a DNS (Domain Name System) seedlist connection string, include the
DNS (Domain Name System) SRV (Service) record that describes your database's backing instance
sharded cluster. The connection string uses the **mongodb+srv:**
protocol, not the **mongodb:** protocol.

**none:**

```ini
mongo.mongoUri=mongodb+srv://db.example.com:40000
```

**scram:**

Prepend the MongoDB username and password to the hostname. Write the
username and password in this format: **<username>:<password>@**

```ini
mongo.mongoUri=mongodb+srv://mongodbuser1:password@mongos.example.com:40000
```

**Note:** Necessary MongoDB Roles

The MongoDB user that authenticates to the backing databases must
have the following roles:

- `readWriteAnyDatabase`

- `dbAdminAnyDatabase`

- `clusterAdmin` if the database is a sharded
  cluster, otherwise `clusterMonitor`

**x509:**

You should find the client certificate in the PEM (Privacy-Enhanced Mail) file you
specified in the `mongodb.ssl.PEMKeyFile` setting.

- Prepend the value of the *subject* from the
  client certificate as a MongoDB user
  to the host.

- Append **authMechanism=MONGODB-X509** to the specified port.

```ini
mongo.mongoUri=mongodb+srv://<new_mongodb_user>@mongos.example.com:40000/?authMechanism=MONGODB-X509
```

**ldap:**

- Prepend the MongoDB username and password to the hostname in this
  format: **<username>:<password>@**.

- Append the authentication mechanism to the port in this format:
  **authMechanism=PLAIN&authSource=$external**

```ini
mongo.mongoUri=mongodb+srv://mongodbuser1:password@mongos.example.com:40000/?authMechanism=PLAIN&authSource=$external
```

**kerberos:**

- Prepend the hostname with the Kerberos user principal.

  Write Kerberos UPN (User Principal Name)\s as **<username>@<KERBEROS REALM>**. Escape
  the UPN (User Principal Name) using the URL (Uniform Resource Locator) encoded representation. A Kerberos user
  principal of **username@REALM.EXAMPLE.COM** would therefore become
  **username%40REALM.EXAMPLE.COM**.

- Append the authentication mechanism to the port in this format:
  **authMechanism=GSSAPI**.

```ini
mongo.mongoUri=mongodb+srv://username%40REALM.EXAMPLE.COM@mongos.example.com:40000/?authMechanism=GSSAPI
```

**Note:** Modify Kerberos Settings

To enable Kerberos, modify the following settings:

- `jvm.java.security.krb5.conf`
- `jvm.java.security.krb5.kdc`
- `jvm.java.security.krb5.realm`
- `mms.kerberos.debug`
- `mms.kerberos.keyTab`
- `mms.kerberos.principal`

This option requires a DNS (Domain Name System) SRV (Service) record for the application
database. The DNS (Domain Name System) entry uses the DNS (Domain Name System) seedlist string format.
Make sure Ops Manager can connect to this application database.

**See also:**

DNS Seedlist Connection Format

**`mongo.encryptedCredentials`**

*Type*: boolean

To use encrypted credentials in `mongo.mongoUri`, encrypt
the credentials using the Ops Manager
credentialstool, enter
them in the `mongo.mongoUri` setting, and set this to
`true`:

```ini
mongo.encryptedCredentials=true
```

### Kerberos Authentication to Ops Manager Application Database

**`mms.kerberos.debug`**

*Type*: boolean

Debug flag to output more information on Kerberos authentication
process.

```ini
mms.kerberos.debug=false
```

**`mms.kerberos.keyTab`**

*Type*: string

Required if using Kerberos. The absolute path to the keytab file for
the principal.

```ini
mms.kerberos.keyTab=/path/to/mms.keytab
```

**`mms.kerberos.principal`**

*Type*: string

Required if using Kerberos. Principal used to authenticate with
MongoDB. This should be the exact same user on the
`mongo.mongoUri`.

```ini
mms.kerberos.principal=mms/mmsweb.example.com@EXAMPLE.COM
```

**`jvm.java.security.krb5.conf`**

*Type*: string

Optional. Path to an alternate Kerberos configuration file. The value
is set to JVM (Java Virtual Machine)\'s `java.security.krb5.conf`.

```ini
jvm.java.security.krb5.conf=/etc/conf/krb5.conf
```

**`jvm.java.security.krb5.kdc`**

*Type*: string

Required if using Kerberos. IP/FQDN (fully qualified domain name) of the KDC (Key Distribution Center) server. The value
will be set to JVM (Java Virtual Machine)\'s `java.security.krb5.kdc`.

```ini
jvm.java.security.krb5.kdc=kdc.example.com
```

**`jvm.java.security.krb5.realm`**

*Type*: string

Required if using Kerberos. This is the default realm for Kerberos.
It is being used for JVM (Java Virtual Machine)\'s `java.security.krb5.realm`.

```ini
jvm.java.security.krb5.realm=EXAMPLE.COM
```

### TLS/SSL Connection to the Application Database

**`mongo.ssl`**

*Type*: boolean

Enables TLS (Transport Layer Security) connection to the mms-application-database
when set to `true`.

**`mongodb.ssl.CAFile`**

*Type*: string

Name of the PEM file that contains the root certificate chain
from the Certificate Authority that signed the MongoDB server certificate.

**`mongodb.ssl.PEMKeyFile`**

*Type*: string

Name of the PEM file that contains the X509 certificate and
private key. Required if the MongoDB instance is running with the
`--tlsCAFile` option or
`net.tls.CAFile` setting.

The `Extended Key Usage` field of that certificate should include `TLS Web client authentication`.

If you authenticate using the `MONGODB-X509` authentication
mechanism, you also enter this as the name of the user in the
`mongoUri` connection string.

**`mongodb.ssl.PEMKeyFilePassword`**

*Type*: string

Required if the PEM (Privacy-Enhanced Mail) file contains an encrypted private key. Specify
the password for PEM (Privacy-Enhanced Mail) file. You can encrypt the password using the
Ops Manager `encryptiontool`.


## Automation Default Paths

**`automation.default.backupAgentLogFile`**

*Type*: string

*Default*: `/var/log/mongodb-mms-automation/backup-agent.log`

Default path for the Backup logs on Linux/macOS.

**`automation.default.certificateAuthorityFile`**

*Type*: string

Default path for the Certificate Authority file on Linux/macOS.

**`automation.default.dataRoot`**

*Type*: string

*Default*: `/data`

Default data path for the MongoDB databases that Automation manages.

**`automation.default.downloadBase`**

*Type*: string

*Default*: /var/lib/mongodb-mms-automation

Default path for the Monitoring, Backup, and MongoDB
binaries for the deployments managed by Automation on Linux/macOS.

**`automation.default.monitoringAgentLogFile`**

*Type*: string

*Default*: `/var/log/mongodb-mms-automation/monitoring-agent.log`

Default path for the Monitoring logs on Linux/macOS.

**`mms.agentCentralUrl`**

*Type*: string

FQDN (fully qualified domain name) of the Ops Manager Application to which the legacy Monitoring Agents or
MongoDB Agents use to push monitoring data.

Uses the value of `mms.centralUrl` if not set.

**Important:**

If you plan on accessing your Ops Manager Application using its IPv6 (Internet Protocol version 6)
address, you must enclose the IPv6 (Internet Protocol version 6) address in square brackets
(`[ ]`) to separate it from its port number.

For example:

```ini
http://[2600:1f16:777:8700:93c2:b99c:a875:2b10]:8080
```
