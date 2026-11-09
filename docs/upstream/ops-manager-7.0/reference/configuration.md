<!-- Converted from reference/configuration.txt (reStructuredText). Includes are inlined. -->

# Ops Manager Configuration Settings

Ops Manager stores configuration settings both globally in the
Ops Manager Application Database and locally on each server. Global settings
apply to all your Ops Manager servers. Local settings apply to the server
on which they are configured. Any local settings on a server override
the global settings.

You configure local settings through a server's `conf-mms.properties`
file. Each server's `conf-mms.properties` must contain the connection
string and authentication settings for accessing the Ops Manager
Application Database. The `conf-mms.properties` file also contains
any overrides of global settings specific to that server.

The location of the `conf-mms.properties` file depends on how you
installed Ops Manager, as described in the table below.

| Install method | Location of `conf-mms.properties` |
|---|---|
| `rpm` or `deb` package | `/opt/mongodb/mms/conf/` |
| `tar.gz` archive | `<install-directory>/conf/` |

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

## Backup

**`mms.alerts.BackupAgentConfCallFailure.maximumFailedConfCalls`**

*Type*: integer

*Default*: 10

If the Backup experiences more than this number of consecutive
failed conf calls, Ops Manager triggers the following global alert: ``Backup has too many
conf call failures``.

**`mms.alerts.OutsideSpaceUsedThreshold.maximumSpaceUsedPercent`**

*Type*: integer

*Default*: 85

If the `blockstore` uses at least this percentage of its total
disk capacity, Ops Manager triggers the following system alert:
`Blockstore space used exceeds threshold`.

**`mms.backupCentralUrl`**

*Type*: string

FQDN (fully qualified domain name) of the Ops Manager Application to which the legacy Backup Agents or
MongoDB Agents use to send backup data.

Uses the value of `mms.centralUrl` if not set.

**Important:**

If you plan on accessing your Ops Manager Application using its IPv6 (Internet Protocol version 6)
address, you must enclose the IPv6 (Internet Protocol version 6) address in square brackets
(`[ ]`) to separate it from its port number.

For example:

```ini
http://[2600:1f16:777:8700:93c2:b99c:a875:2b10]:8080
```

**`mms.backup.journal.heads`**

*Type*: boolean

*Default*: False

This sets whether the `HEAD database` should
use journaling. See manage-backup-jobs to
enable or disable journaling for the `head database` of a
single backup job.

FCV `4.2` and later use backup cursors instead of `head databases` 
for backups.

**`mms.backup.minimumOplogWindowHours`**

*Type*: float

*Default*: 3

This sets the minimum number of hours of database operations that the
oplog should record.

Your deployment's oplog needs to be large enough to hold recovery
data since the last snapshot. Increase this value to have Ops Manager
monitor the oplog capacity. You should set this value to meet or
exceed the value in `brs.snapshotSchedule.interval`.

If you set the value to less than `brs.snapshotSchedule.interval`, you may have a
gap between the last snapshot and the end of the oplog. This makes
the backup unusuable for restores. Stale backup jobs must be
resynchronized before it can be used for restores.

### Backup Snapshots

**`backup.fileSystemSnapshotStore.gzip.compressionLevel`**

*Type*: integer

*Default*: 6

Determines how much Ops Manager compresses file system-based snapshots.
The level ranges from `0` to `9`:

- `0` provides no compression.

- `1` to `9` increases the degree of compression at a cost of
  how fast the snapshot is compressed. Level `1` compresses
  snapshots the least but at the fastest speed. Level `9`
  compresses snapshots the most but at the slowest speed.

**Note:**

Changing File System Store Gzip Compression Level
affects new snapshots only. It does not affect the compression
level of existing snapshots.

Corresponds to `File System Store Gzip Compression Level`.

**`brs.restore.digest.method`**

*Type*: string

*Default*: SHA1

Specifies whether or not to generate a SHA1 checksum
for restore archive files.

Accepted values are `SHA1` or `NONE`.

Corresponds to `Restore Digest Method`.

**`brs.snapshotSchedule.interval`**

*Type*: integer

*Default*: 24

Specifies the time, in hours, between two consecutive snapshots.

Accepted values are:

`6`, `8`, `12`, or `24`

Corresponds to `Snapshot Interval (Hours)`

**`brs.snapshotSchedule.retention.base`**

*Type*: integer

*Default*: 2

Specifies how many days an interval snapshot is stored. The accepted
values vary depending upon the value of `brs.snapshotSchedule.interval`:

|  |  |
|---|---|
| `brs.snapshotSchedule.interval` | Accepted Values |
| < `24` | `2`, `3`, `4`, or `5`. |
| = `24` | `2`, `3`, `4`, `5`, `6`, `7`, `8`, `9`, `10`, `11`, `12`, `13`, `14`, `15`, `16`, `17`, `18`, `19`, `20`, `21`, `22`, `23`, `24`, `25`, `26`, `27`, `28`, `29`, `30`. |

Corresponds to `.Base Retention of Snapshots`

**`brs.snapshotSchedule.retention.daily`**

*Type*: integer

*Default*: 0

Specifies how many days a daily snapshot is stored.

Accepted values are:

`0`, `3`, `4`, `5`, `6`, `7`, `15`, `30`, `60`,
`90`, `120`, `180` or `360`

Corresponds to `.Daily Retention of Snapshots`

**`brs.snapshotSchedule.retention.monthly`**

*Type*: integer

*Default*: 1

Specifies how many months a monthly snapshot is stored.

Accepted values are:

`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`,
`9`, `10`, `11`, `12`, `13`, `18`, `24`, `36`,
`48`, `60`, `72`,  and `84`

Corresponds to `Monthly Retention of Snapshots (in Months)`

**`brs.snapshotSchedule.retention.weekly`**

*Type*: integer

*Default*: 2

Specifies how many weeks a weekly snapshot is stored.

Accepted values are:

`0`, `1`, `2`, `3`, `4`, `5`, `6`, `7`, `8`,
`12`, `16`, `20`, `24`, and `52`

Corresponds to `.Weekly Retention of Snapshots`

**`brs.pitWindowInHours`**

*Type*: integer

*Default*: 24

Duration time in hours when you can 
restore from a specific point-in-time (PIT).

Corresponds to `.PIT Window`

**`backup.kmip.server.host`**

*Type*: string

*Default*: None

Specifies the hostname of a KMIP (Key Management Interoperability) server. 

Starting in MongoDB 4.2.1 (and 4.0.14),
you can specify more than one KMIP (Key Management Interoperability) server 
in a comma-seperated list. 

**Important:**

In MongoDB versions earlier than 4.0.14 or 4.2.1,
Ops Manager uses only the first KMIP (Key Management Interoperability) hostname in a list of KMIP (Key Management Interoperability)
server hostnames. 

Corresponds to `KMIP Server Host`.

**`backup.kmip.server.port`**

*Type*: integer

*Default*: None

Specifies the port of the KMIP (Key Management Interoperability) server.

Corresponds to `KMIP Server Port`.

**`backup.kmip.server.ca.file`**

*Type*: string

*Default*: None

Specifies a `.PEM`-format file that contains one or more
certificate authorities.

Corresponds to `KMIP Server CA File`.

**`mms.backup.snapshot.maxSumFileForWorkersMB`**

*Type*: integer

*Default*: 2048

This sets the maximum cumulative size of files, in Megabytes, that
are saved concurrently when taking a snapshot.

**`mms.backup.snapshot.maxWorkers`**

*Type*: integer

*Default*: 4

This sets the number of files that are saved concurrently when
taking a snapshot. Increasing the value of this setting can
improve backup job performance when there are a large number
of small files in a high latency environment.

### Queryable Snapshot Configuration

**`brs.queryable.connecttimeout`**

*Type*: integer

*Default*: 30

Number of seconds to wait for a connection to the Queryable Snapshot
mongod instance before timing out.

Corresponds to `Mongo .Connection Timeout`

**`brs.queryable.expiration`**

*Type*: integer

*Default*: 24

Duration time in hours for a Queryable Snapshop once initiated.

Corresponds to `Expiration (Hours)`.

**`brs.queryable.lruCacheCapacityMB`**

*Type*: integer

*Default*: 512

Size (in megabytes) that you allocate from the JVM (Java Virtual Machine) heap for the
global snapshot cache. The global snapshot cache optimizes
repeated queries for the same snapshot data to the Queryable
Snapshots.

**Important:**

MongoDB does not advise changing this value unless MongoDB support
directs you to change it.

Corresponds to `Read Cache Size (MB)`.

**`brs.queryable.mounttimeout`**

*Type*: integer

*Default*: 60

Number of seconds to wait for the Queryable Snapshot to prepare
before timing out.

Corresponds to `.Queryable Startup Timeout`

**`brs.queryable.pem.pwd`**

*Type*: string

Required if `Proxy Server PEM File` is encrypted.

**Note:**

After updating `Proxy Server PEM File Password`, restart
the Web Server for the change to take effect.

Corresponds to `Proxy Server PEM File Password`.

**`brs.queryable.pem`**

*Type*: string

Required if using Queryable Snapshot. PEM (Privacy-Enhanced Mail) file that contains the
full certificate chain for one or more trusted certificates and the
associated private keys.

`Proxy Server PEM File` has the following restrictions:

- This PEM file must be different than the one used for HTTPS (Hypertext Transfer Protocol Secure)
  connections to Ops Manager (`mms.https.PEMKeyFile`).
- This PEM file should use a key length greater than 512-bit. Using a
  2048-bit RSA key is recommended.
- This PEM file should use a message digest stronger than `sha1`,
  such as `sha256`.

**Note:**

After updating `Proxy Server PEM File`, restart the Web
Server for the change to take effect.

Corresponds to `Proxy Server PEM File`.

**`brs.queryable.proxyPort`**

*Type*: integer

*Default*: 25999

Port for the queryable backup host.

**Note:**

After updating `Proxy Server Port`, restart the Web
Server for the change to take effect.

Corresponds to `Proxy Server Port`.

**`brs.queryable.tls.disabledProtocols`**

*Type*: string

*Default*: SSLv2Hello,SSLv3,TLSv1,TLSv1.1,TLSv1.3

TLS (Transport Layer Security) protocol versions that have been disabled for queryable
snapshots and restores.

**`brs.queryable.tls.disabledCiphers`**

*Type*: string

*Default*:
TLS_DHE_RSA_WITH_AES_128_CBC_SHA,TLS_DHE_RSA_WITH_AES_128_CBC_SHA256,TLS_DHE_RSA_WITH_AES_128_GCM_SHA256,TLS_DHE_RSA_WITH_AES_256_CBC_SHA,TLS_DHE_RSA_WITH_AES_256_CBC_SHA256,TLS_DHE_RSA_WITH_AES_256_GCM_SHA384

List of TLS (Transport Layer Security) ciphers suites that your Ops Manager instance can't accept
when clients connect to the queryable backup host. Specify TLS (Transport Layer Security)
cipher suite names as a comma-separated list with no whitespace
between entries.

## Diagnostic Archive

**`mms.admin.diagnostics.archiveDocCountLimit`**

*Type*: integer

*Default*: 10000

Maximum number of entries that Ops Manager should retrieve from the
activity feed.

**`mms.admin.diagnostics.archiveDocSizeLimit`**

*Type*: integer

*Default*: 7

Maximum number of days of data that Ops Manager should retrieve from the
activity feed.

**`mms.admin.diagnostics.archiveDocAgeLimit`**

*Type*: integer

*Default*: 7

Maximum number of days of data that Ops Manager should retrieve from the
activity feed.

**`mms.automation.diagnostics.lastAgentStatusDocAgeLimit`**

*Type*: integer

*Default*: 7

Add the last specified days of the **automationLastAgentStatus** in
diagnostic archive.

**`mms.automation.diagnostics.includeEmptyProcessConfigs`**

*Type*: boolean

*Default*: False

Flag that indicates whether to add **automationConfigs** for groups
with non-empty processes array in diagnostic archive.

## Email

**`mms.fromEmailAddr`**

*Type*: string

Email address used for sending the general emails, such as
Ops Manager alerts. You can include an alias with the email address.

```ini
mms.fromEmailAddr=mms-alerts@example.com
```

Corresponds to `From Email Address`.

**`mms.replyToEmailAddr`**

*Type*: string

Email address from which to send replies to general emails.

Corresponds to `Reply To Email Address`.

**`mms.adminEmailAddr`**

*Type*: string

Email address of the Ops Manager admin. This address receives emails
related to problems with Ops Manager.

Corresponds to `Admin Email Address`.

**`mms.emailDaoClass`**

*Type*: string

*Default*: `SIMPLE_MAILER`

Email interface to use.

This setting is labeled in different ways for the user interface and
the configuration file.

| Delivery Method | Configuration Setting (`mms.emailDaoClass`) |
|---|---|
| AWS (Amazon Web Services) SES (Simple Email Service) | `AWS_MAILER` |
| SMTP (Simple Mail Transport Protocol) | `SIMPLE_MAILER` |

If you set this to SMTP (Simple Mail Transport Protocol) Email Server, you must set:

- `mms.mail.transport`
- `mms.mail.hostname`
- `mms.mail.port`
- `mms.mail.username`
- `mms.mail.password`
- `mms.mail.tls`

If you set this to AWS (Amazon Web Services) Simple Email Service, you must set:

- `aws.ses.endpoint`
- `aws.accesskey`
- `aws.secretkey`

Corresponds to `Email Delivery Method Configuration`.

### SMTP Email Server

*Conditional.* The following settings appear if you set
`mms.emailDaoClass` to `SIMPLE_MAILER`.

**`mms.mail.transport`**

*Type*: string

*Default*: smtp

Transfer protocol your email provider specifies:

- `smtp` (standard SMTP (Simple Mail Transport Protocol))

Corresponds to `Transport`.

**`mms.mail.hostname`**

*Type*: string

*Default*: localhost

Email hostname your email provider specifies.

```ini
mms.mail.hostname=mail.example.com
```

Corresponds to `SMTP Server Hostname`.

**`mms.mail.port`**

*Type*: number

*Default*: 25

Port number for SMTP (Simple Mail Transport Protocol) your email provider specifies.

Corresponds to `SMTP Server Port`.

**`mms.mail.username`**

*Type*: string

User name of the email account. If unset, defaults to disabled
SMTP (Simple Mail Transport Protocol) authentication.

Corresponds to `Username`.

**`mms.mail.password`**

*Type*: string

Password for the email account. If left blank, this setting disables
SMTP (Simple Mail Transport Protocol) authentication.

Corresponds to `Password`.

**`mms.mail.tls`**

*Type*: boolean

*Default*: False

Set this to `true` if the transfer protocol uses TLS (Transport Layer Security)/SSL (Secure Sockets Layer).

Corresponds to `Use SSL`.

### AWS Simple Email Service

*Conditional.* The following settings appear if you set
`mms.emailDaoClass` to `AWS_MAILER`.

**`aws.ses.endpoint`**

*Type*: string

*Default*: `https://email.us-east-1.amazonaws.com`

Sets the [sending API endpoint](https://docs.aws.amazon.com/ses/latest/DeveloperGuide/regions.html#region-endpoints)
for the AWS (Amazon Web Services) SES (Simple Email Service).

Corresponds to `AWS Endpoint`.

**`aws.accesskey`**

*Type*: string

Access key ID for AWS (Amazon Web Services).

Corresponds to `AWS Access Key`.

**`aws.secretkey`**

*Type*: string

Secret access key for AWS (Amazon Web Services).

Corresponds to `AWS Secret Key`.

## HTTP Proxy

**`http.proxy.host`**

*Type*: string

Specify the hostname of the HTTP (Hypertext Transfer Protocol) or HTTPS (Hypertext Transfer Protocol Secure) proxy to which you
wish to connect.

```ini
http.proxy.host=proxy.example.com
```

Corresponds to `Proxy Host`.

**`http.proxy.port`**

*Type*: integer

Specify the port on which you wish to connect to the host. You must
specify both the `Proxy Port` and `Proxy Host` to
use a proxy.

Corresponds to `Proxy Port`.

**`http.proxy.username`**

*Type*: string

If the proxy requires authentication, use this setting to specify
the username with which to connect to the proxy.

Corresponds to `Proxy Username`.

**`http.proxy.password`**

*Type*: string

If the proxy requires authentication, use this setting to specify
the password with which to connect to the proxy.

Corresponds to `Proxy Password`.

**`http.proxy.nonProxyHosts`**

*Type*: string

Specify a pipe-separated (`|`) list of internal hosts
to bypass the outgoing proxy that you configured.

```ini
*.foo.com|localhost
```

Corresponds to `Non Proxy Hosts`.

### Kubernetes Setup

**`kubernetes.templates.credentialsFilePath`**

*Type*: string

Path to the YAML file that contains your Programmatic API Key as a Kubernetes secret to create or update [objects](https://kubernetes.io/docs/concepts/overview/working-with-objects/kubernetes-objects/)
in your Ops Manager project. This file must be in YAML format and must be
stored under the `/mongodb-ops-manager/` directory. This file
corresponds to `Kubernetes Secret Setup`.

```yaml
apiVersion: v1
kind: Secret
metadata:
  name: organization-secret
  namespace: mongodb
stringData:
  user: ${publicKey}
  publicApiKey: ${privateKey}
```

**`kubernetes.templates.projectFilePath`**

*Type*: string

Path to the YAML file that contains the ConfigMap to use to link to your
Ops Manager project. This file must be in YAML format and must be stored under
the `/mongodb-ops-manager/` directory. This file corresponds to
`Kubernetes ConfigMap Setup`.

## MongoDB Version Management

**`automation.versions.source`**

*Type*: string

*Default*: `remote`

Indicates the source of MongoDB installer binaries.

Accepted values for `automation.versions.source` and the conditions that must exist to
set the value are:

| Value | Condition |
|---|---|
| `remote` | Ops Manager and Agents have internet access. |
| `hybrid` | Ops Manager has internet access, but Agents do not. Ops Manager downloads MongoDB binaries from the internet; Agents download the binaries from Ops Manager. |
| `local` | Neither Ops Manager nor the Agents have internet access. An Ops Manager administrator must upload the version manifest and the MongoDB binaries to the Ops Manager host, as described in /tutorial/configure-local-mode. |

Corresponds to `Installer Download Source`.

**`automation.versions.download.baseUrl`**

*Type*: string

*Default*: mongodb.com, fastdl.mongodb.org

HTTP(S) endpoint to fetch MongoDB binaries from. If the endpoint is 
an HTTPS endpoint, the Certificate Authority file specified by 
`httpsCAFile` will be used to validate the certificate. If 
`automation.versions.download.baseUrl` is unset, the remote URLs 
for mongodb binaries are **mongodb.com** and **fastdl.mongodb.org**.

Corresponds to `Base URL`.

**`automation.versions.download.baseUrl.allowOnlyAvailableBuilds`**

*Type*: boolean

*Default*: True

When set to `true`, Ops Manager limits the MongoDB versions you can 
specify to those available for your deployment. 

This setting is applied only when
`automation.versions.download.baseUrl` is set with a 
custom value.

**`automation.versions.directory`**

*Type*: string

*Default*: `/opt/mongodb/mms/mongodb-releases/`

Specify the directory on the Ops Manager Application server where Ops Manager
stores the MongoDB binaries. The Automation accesses the
binaries when installing or changing versions of MongoDB on your
deployments. If you set `Version Manifest Source` to run in
`Local` mode, the Backup Daemons also access the MongoDB binaries
from this directory. See /tutorial/configure-local-mode for
more information.

Corresponds to `Versions Directory`.

**`mongodb.release.autoDownload`**

*Type*: boolean

*Default*: True

Flag indicating whether the Backup Daemons automatically install the
versions of MongoDB that the Backup Daemons need.

|  |  |
|---|---|
| `true` | The daemons retrieve the binaries from MongoDB Inc. over the internet. |
| `false` | Backup Daemons do not have internet access and require that an Ops Manager administrator manually download and extract every archived version of a MongoDB release that the backup daemons need. The administrator must place the extracted binaries into the `Versions Directory` on the Ops Manager hosts. |

**Warning:**

Set to `false` when Ops Manager is running in
Local Mode.

Corresponds to `Backup Versions Auto Download`.

**`mongodb.release.autoDownload.enterprise`**

*Type*: boolean

Flag indicating whether the Backup Daemons automatically install the
Enterprise editions of the versions of MongoDB that the Backup
Daemons need. Requires `mongodb.release.autoDownload` be set to `true`.

**Warning:**

If you plan on running
`MongoDB Enterprise` on
Linux hosts, then you must manually install a set of dependencies
to each host *before installing MongoDB*. The MongoDB manual
provides the appropriate command to install the dependencies.

See /tutorial/configure-local-mode.

Corresponds to `Backup Versions Auto Download Enterprise Builds`

**`mongodb.release.modulePreference`**

*Type*: string

Specifies whether to use MongoDB Community or Enterprise binaries
for backup.

Accepted values are:

- `enterprisePreferred`
- `enterpriseRequired`
- `communityRequired`

When `enterpriseRequired` or `communityRequired` is selected, Ops Manager only uses those
binaries for backup. When `enterprisePreferred` is selected, Ops Manager uses
Enterprise binaries if available and Community binaries if they are
not.

**Note:**

When `enterpriseRequired` is selected, you must either set `mongodb.release.autoDownload.enterprise` to
`true` or manually place Enterprise binaries in the `automation.versions.directory`
in Local Mode.

**Warning:**

Backup fails when either `enterpriseRequired` or `communityRequired` is selected,
but the `automation.versions.directory` does not contain the required binary.

Corresponds to `Required Module For Backup`.

## MongoDB Usage

**`mms.mongoDbUsage.defaultUsageType`**

*Type*: string

*Default*: Production Server

Default MongoDB Enterprise server type for all Enterprise
processes that this Ops Manager instance manages.

The following table shows the accepted Server Type values and the
corresponding number of licenses required for each:

* - Server Intention
  - Environment Purpose
  - License Requirement

* - Production Server
  - Hosts your application to your internal or external end users.

    If an end user might use an environment, it functions as a
    Production environment. This applies whether the environment
    also provides testing, quality assurance, evaluation, or
    development capabilities.

  - One license per server

* - Test/QA Server
  - This type of environment can be used to:

    |  |  |
    |---|---|
    | Test | Exercises your application to verify that it works as designed and expected. The platform configuration might be a less performant version of Production in compute, network, and storage capability. |
    | Assure system quality | Validates your application against a combination of data, hardware, and software configured to simulate Production. The platform configuration should be a smaller scale of Production in compute, network, and storage capability. |
    | Stage | Simulates the Production environment including performance testing and release candidate approval. The platform configuration should mirror Production in compute, network, and storage capability. |

  - One license per server

* - Development Server
  - Hosts in progress design, code, debugging or some combination
    thereof for your application. Used to evaluate if the current
    state of your application can be promoted to another
    environment.
  - None

* - RAM Pool
  - Provides any combination of servers for any environment purpose.
  - One license for any number of servers up to the maximum of
    the total GB of RAM you purchased across these servers.

|  |  |  |
|---|---|---|
| Backing Database | Hosts your Ops Manager backing database. enable-application-database-monitoring to enable this option. | None |

Corresponds to `Default Ops Manager MongoDB Server Type`.

**`mms.mongoDbUsage.ui.enabled`**

*Type*: boolean

Enables the MongoDB Usage UI in the Ops Manager Admin if set to
`true`.

Corresponds to `MongoDB Usage UI`.

**`mms.mongoDbUsage.collectData`**

*Type*: boolean

*Default*: False

Enables the daily collection of MongoDB Usage Data if set to
`true`.

Corresponds to `MongoDB Usage Data Collection`.

## Monitoring

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

### Monitoring Failover

You can activate the Monitoring function
on multiple MongoDB Agents to distribute monitoring assignments and
provide failover. Ops Manager distributes monitoring assignments among up to
100 running MongoDB Agents. Each MongoDB Agent running active Monitoring
monitors a different set of MongoDB processes. One MongoDB Agent running
active Monitoring per project is the primary Monitor. The primary
Monitor reports the cluster's status to Ops Manager. As MongoDB Agents have
Monitoring enabled or disabled, Ops Manager redistributes assignments. If the
primary Monitor fails, Ops Manager assigns another MongoDB Agent running
active Monitoring to be the primary Monitor.

The following settings tune the interval Ops Manager uses to determine if
a Monitoring is unaccessible and the frequency with which standby
agents poll Ops Manager to determine if they should receive monitoring
assignments.

**`mms.monitoring.agent.session.timeoutMillis`**

*Type*: integer

*Default*: 90000

Interval that Ops Manager uses to determine if a standby agent should
start monitoring. If Ops Manager does not hear from a Monitoring for
the duration specified, Ops Manager promotes a standby agent. Configuring
the timeout below `90000` (90 seconds) will cause Ops Manager to fail at
startup with a configuration error.

**`mms.monitoring.agent.standbyCollectionFactor`**

*Type*: integer

*Default*: 4

Specifies how frequently a standby agent checks in with Ops Manager to see
if it should start monitoring. The following values are permitted:

| Value | Standby Agents Check Frequency |
|---|---|
| `1` | Every 55 seconds |
| `2` | Every 27 seconds |
| `3` | Every 18 seconds |
| `4` | Every 14 seconds |

## Ops Manager Administration API

**`mms.publicApi.whitelistEnabled`**

*Type*: boolean

Certain API (Application Programming Interface) calls require that requests originate from a
IP address in the access list. To
turn off this requirement, add this setting and set its value to
`false`.

## Prometheus

You must configure the following settings to enable the metrics that are 
available for ingestion through Prometheus. You can also configure these
settings in the Custom tab of the Ops Manager Config page in the
admin-console-general-tab. 
   
After configuring these settings, you must restart Ops Manager on each
instance. After restarting, the new Prometheus endpoint can be
accessed at a URL (Uniform Resource Locator) in the following format: 
   

```shell
http(s)://<opsManagerUri>:<port>/metrics
```

**Note:**

You can designate a listening port for the Prometheus metrics. This
doesn't have to be the default port that Ops Manager uses, 8080 for HTTP (Hypertext Transfer Protocol) or
8443 for HTTPS (Hypertext Transfer Protocol Secure). Ensure that your network allows traffic to the
specified Prometheus metrics port. 

After enabling, you must configure a new scrape config similar to the
following in Prometheus for each Ops Manager server that you would like to
gather statistics from. 

```shell
scrape_configs:

- job_name: 'opsmanager'
   static_configs:
      - targets: [<opsManagerHostname>:<port>]
```

Note that each server's endpoint only provides metrics for the same server.

**`prom.listening.enabled`**

*Type*: boolean

Flag that specifies whether to enable access for Prometheus. To
enable Ops Manager Prometheus endpoint, set value to `true`. If omitted,
defaults to `false`. 

**`prom.listening.port`**

*Type*: number

The port over which Ops Manager listens for requests to the Prometheus
endpoint. The port must be different than the port Ops Manager is already
listening on, 8080 for HTTP (Hypertext Transfer Protocol) or 8443 for HTTPS (Hypertext Transfer Protocol Secure). Every server will
listen on the specified port. So, ensure that the port is available
as an open port on every server. If you want to specify different
port for each server, use `conf-mms.properties` instead to specify
the ports. 

## Push Live Migrations

**`mms.pushLiveMigrations.mmsUi.centralUrl`**

*Type*: string

Base URL for Live Migration from Ops Manager to Atlas,
such as `https://cloud.mongodb.com`.

**`mms.pushLiveMigrations.syncJobs.enabled`**

*Type*: boolean

If set to `true`, allows Ops Manager to request information about Live Migration
processes, such as:

- The list of available projects and deployments that can be used as
  sources for Live Migrations.
- The list of available configured migration hosts that can
  facilitate Live Migrations in their respective deployments and projects.
- The current status of running Live Migrations in Atlas.

Ops Manager uses this information to facilitate Live Migration processes.
The default is `true`.

**`mms.pushLiveMigrations.updateJob.intervalSeconds`**

*Type*: boolean

The repeat interval, in seconds, between sync refreshes.
The syncs of the organization's project information between
Ops Manager and Atlas occur periodically. The default interval
between syncs is `60`. Ops Manager expects sync refreshes to occur
within an interval from 10 to 43200 seconds (12 hours). If the
actual interval between sync refreshes is longer than 43200 seconds
or if the actual interval between sync refreshes is longer than 1800
seconds (30 minutes) during the validation phase, the Live Migration
to Atlas might stall, time out, or fail.

**Note:**

After updating this setting, restart the Web Server
for the change to take effect.

**`mms.pushLiveMigrations.updateJob.cooldownSeconds`**

*Type*: boolean

The interval, in seconds, between information
sync refreshes for an organization's project. The default interval
between sync refreshes is `10`. Ops Manager expects sync refreshes to
occur within an interval from 10 to 43200 seconds (12 hours). If
the actual interval between consecutive syncs is longer than 43200
seconds, the Live Migration to Atlas might stall, time out,
or fail.

**Note:**

After updating this setting, restart the Web Server
for the change to take effect.

**`mms.pushLiveMigrations.fetchJob.intervalSeconds`**

*Type*: boolean

The repeat interval, in seconds, for syncing the Live Migration plan
updates from Atlas.The plan lists the steps in the
Atlas migration process. Ops Manager periodically retrieves the
current plan from Atlas to check progress. Without this
information, Ops Manager does not move the Live Migration process to the
next stage.

The default interval between syncs is `60`. Ops Manager expects sync
refreshes to occur within an interval from 10 to 43200 seconds (12
hours). If the actual interval between consecutive syncs is longer
than 43200 seconds, the Live Migration to Atlas might
stall, time out, or fail.

**Note:**

After updating this setting, restart the Web Server
for the change to take effect.

**`mms.automation.agentFeatures.migrationHosts.canManageDeployments`**

*Type*: boolean

Indicates whether to show Live Migration hosts as available agents
in the Add new deployment view under Projects
in the user interface. The default is `false`.

**See also:**

- opsmgr-config-add-custom
- migrate-to-atlas

## Security

**`mms.security.disableBrowserCaching`**

*Type*: boolean

*Default*: False

When `true`, Ops Manager makes all HTTP (Hypertext Transfer Protocol) responses not cacheable.

**`mms.security.hstsMaxAgeSeconds`**

*Type*: integer

*Default*: 0 (Can use HTTP (Hypertext Transfer Protocol) or HTTPS (Hypertext Transfer Protocol Secure).)

How long (in seconds) Ops Manager limits browser connections to use
HTTPS (Hypertext Transfer Protocol Secure). This value must be a positive integer. A value of `0`
means that it can use HTTP (Hypertext Transfer Protocol) or HTTPS (Hypertext Transfer Protocol Secure).

**See also:**

To learn how to deploy
HSTS (HTTP Strict Transport Security), see
HTTP Strict Transport Security <https://en.wikipedia.org/w/index.php?title=HTTP_Strict_ Transport_Security&oldid=774831831>,
RFC 6797 and
[hstspreload.org](https://hstspreload.org/#deployment-recommendations).

**`mms.security.show.om.version`**

*Type*: boolean

*Default*: True

When `false`, Ops Manager doesn't display the version number in the login
page.

### Non-Uniform Memory Access (NUMA)

**`mongodb.disable.numa`**

*Type*: boolean

To disable NUMA for the `head databases`,
follow the Modify a Custom Setting
procedure using the following values:

|  |  |
|---|---|
| Key | `mongodb.disable.numa` |
| Value | `true` |

To learn more about NUMA, see production-numa in the MongoDB
Production Notes.

**Important:**

Each Ops Manager instance with Backup Daemons enabled must have the
`numactl` service installed. If `numactl` is not installed
and this setting is set to `true`, backup jobs fail.

FCV `4.2` and later use 
backup cursors instead of
`head databases`. For
more information, see backup-daemon.

## Third-Party Integrations

### Datadog Integration

**`datadog.api.url`**

*Type*: string

*Default*: `https://api.datadoghq.com/api/v1`

URL (Uniform Resource Locator) that Ops Manager uses to access the Datadog API.

Enable this custom parameter if you have deployed Datadog locally. Set this to a value appropriate for your deployment.

**See also:**

To learn how to add this setting, see
opsmgr-config-add-custom.

### Opsgenie Integration

**`opsgenie.api.url`**

*Type*: string

*Default*: `https://api.opsgenie.com/v2/alerts`

URL (Uniform Resource Locator) that Ops Manager uses to access the Ops Genie API (Application Programming Interface) in European countries. 

Enable this custom parameter if your Ops Manager instance runs in Europe.
Then, set its value to `https://api.eu.opsgenie.com/v2/alerts`.

For more information, see 
[Opsgenie Alert documentation](https://docs.opsgenie.com/docs/alert-api#:~:text=If%20using%20the%20EU%20instance,for%20requests%20to%20be%20successful.).

**See also:**

To learn how to add this setting, see
opsmgr-config-add-custom.

### Twilio Integration

To receive alert notifications via SMS (short message service) or 2FA (two-factor authentication) code,
you must have a [Twilio](http://www.twilio.com/docs/quickstart)
account.

**`twilio.account.sid`**

*Type*: string

[Twilio](http://www.twilio.com/docs/quickstart) account ID.

Corresponds to `Account SID`.

**`twilio.auth.token`**

*Type*: string

Twilio API (Application Programming Interface) token.

Corresponds to `Twilio Auth Token`.

**`twilio.from.num`**

*Type*: string

Twilio phone number.

Corresponds to `Twilio From Number`.

## User Authentication

**`mms.email.validation`**

*Type*: string

*Default*: false

Determines if Ops Manager requires usernames to be email addresses.

| Value | Description |
|---|---|
| `false` | (**Default**) Username is not required to be an email address. |
| `loose` | Username must contain an `@` symbol followed by a period. |
| `strict` | Username must adhere to a strict email address validation regular expression. |

If set to `strict`, Ops Manager uses the following regular expression
to validate that an email address adheres to the requirements
described in Section 3 of 3696:

```sh
^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$
```

**Example:**

`jane.smith@example.com` is valid. `jane.smith@ex@mple.com`
is not.

Corresponds to `Username Validation`.

**`mms.userSvcClass`**

*Type*: string

*Default*: `UserSvcDb`

Select whether to store authentication credentials in the Ops Manager
Application Database or in an LDAP (Lightweight Directory Access Protocol) directory.

Accepted values are:

| Auth Method | Accepted Value |
|---|---|
| Application Database | `UserSvcDb` IMPORTANT: In Ops Manager 6.0, the accepted value is `com.xgen.svc.mms.svc.user.UserSvcDb`. If you use this old accepted value, your Ops Manager instance will not start during preflight checks. |
| LDAP (Lightweight Directory Access Protocol) | `UserSvcLdap` |
| SAML (Security Assertion Markup Language) | `UserSvcSaml` |

Corresponds to `User Authentication Method`.

### Authentication through Ops Manager Application Database

**`mms.password.maxDaysBeforeChangeRequired`**

*Type*: number

Number of days a password is valid before the password expires.

Corresponds to `Days Before Password Change Required`.

**`mms.password.maxDaysInactiveBeforeAccountLock`**

*Type*: number

Maximum number of days with no visits to the Ops Manager website
before Ops Manager locks an account.

Corresponds to `Days Inactive Before Account Lock`.

**`mms.password.maxFailedAttemptsBeforeAccountLock`**

*Type*: number

Number of failed login attempts before an account becomes
locked. Only an an Ops Manager Administrator can unlock a locked account.

Corresponds to `Failed Login Attempts Before Account Lock`.

**`mms.password.minChangesBeforeReuse`**

*Type*: number

Number of previous passwords to remember. You cannot reuse a
remembered password as a new password.

Corresponds to `Password Changes Before Reuse`.

**`mms.login.ratelimit.attemptsAllowed`**

*Type*: number

Number of logins a user from a specific IP address 
can attempt during a timeout period.
You must configure this setting alongside 
`Login Attempts Timeout Period`.

Corresponds to `Login Attempts Allowed Before Timeout`.

**`mms.login.ratelimit.lockedPeriodMinutes`**

*Type*: number

This setting specifies:

- The time period (in minutes) used to determine 
  if too many login attempts have been made.
- The duration that accounts are locked before you can 
  resume login attempts.

You must configure this setting alongside 
`Login Attempts Allowed Before Timeout`.

**Important:**

The dropdown menu lists the only possible 
values for this setting. Attempting to set a value
in your `conf-mms.properties` file or 
local database 
that is not listed in the dropdown causes an error 
when restarting the Ops Manager instance.

Corresponds to `Login Attempts Timeout Period`.

**`mms.user.invitationOnly`**

*Type*: boolean

If true, new users can register by invitation only. The invitation
provides a URL (Uniform Resource Locator) that displays the registration link. If false, new
users can register if they have the Ops Manager URL (Uniform Resource Locator).

Corresponds to `Invitation Only Mode`.

**`mms.user.bypassInviteForExistingUsers`**

*Type*: boolean

*Default*: False

This checkbox appears when you set `mms.userSvcClass` to 
`UserSvcDb`.

* - Value
  - Results

* - `true`
  -
    - You can add existing users to any organization or project
      without an invitation.
    - Ops Manager deletes and invalidates any pending invitations.
    - *New* users continue to receive and must accept invitations.

* - `false`
  -
    - *All* users continue to receive and must accept invitations.

Corresponds to `Bypass Invitation Mode`.

**`mms.user.passwordHashIterations`**

*Type*: number

Number of iterations for the `pbkdf2` hashing algorithm.

Corresponds to `Password Hashing Iterations`.

### Authentication through LDAP

These settings configure Ops Manager to use an LDAP server for
authentication. If you use LDAP authentication, users must belong to an
LDAP group to log into Ops Manager. You must create LDAP groups for each
Ops Manager user role.

*Settings that begin with* `mms.ldap.global.role` assign Ops Manager
global roles to the members of the specified LDAP
groups. Specify groups using the format used by the LDAP attribute
specified in the `LDAP User Group` setting. You can specify
multiple groups using the `;;` delimiter. To change the default
delimiter, use the `mms.ldap.group.separator` setting. Each
Ops Manager global role provides its level of access to all the Ops Manager
projects in the deployment. To
provide access to specific groups, use 
group-level roles.

**`mms.ldap.bindDn`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) user used to execute searches for other users.

```ini
mms.ldap.bindDn=authUser@acme.example.com
```

Corresponds to `LDAP Bind Dn`.

**`mms.ldap.bindPassword`**

*Type*: string

Password for the search user.

```ini
mms.ldap.bindPassword=<password>
```

Corresponds to `LDAP Bind Password`.

**`mms.ldap.global.role.automationAdmin`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the global automation
admin role in Ops Manager. Specify projects
using the format used by the LDAP (Lightweight Directory Access Protocol) attribute specified in the
`LDAP User Group` setting. You can specify multiple projects
using the `;;` delimiter. To change the default delimiter, use the
`mms.ldap.project.separator` setting.

```ini
mms.ldap.global.role.automationAdmin=CN\=MMS-AutomationAdmin,OU\=MMS,OU\=acme Groups,DC\=acme,DC\=example,DC\=com
```

Each Ops Manager global role provides its level of access to all the Ops Manager
projects in the deployment. To
provide access to specific projects, use group-level roles.

Corresponds to `LDAP Global Role Automation Admin`.

**`mms.ldap.global.role.backupAdmin`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the global backup admin
role in Ops Manager.

```ini
mms.ldap.global.role.backupAdmin=CN\=MMS-BackupAdmin,OU\=MMS,OU\=acme Groups,DC\=acme,DC\=example,DC\=com
```

Corresponds to `LDAP Global Role Backup Admin`.

**`mms.ldap.global.role.monitoringAdmin`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the global monitoring
admin role in Ops Manager.

```ini
mms.ldap.global.role.monitoringAdmin=CN\=MMS-MonitoringAdmin,OU\=MMS,OU\=acme Groups,DC\=acme,DC\=example,DC\=com
```

Corresponds to `LDAP Global Role Monitoring Admin`.

**`mms.ldap.global.role.owner`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group that has full privileges for the Ops Manager deployment,
including full access to all Ops Manager
projects and all administrative
permissions. Users in the specified LDAP (Lightweight Directory Access Protocol) group receive the
global owner role in Ops Manager. Specify the
project using the format that is used by the LDAP (Lightweight Directory Access Protocol) attribute
specified in the `LDAP User Group` setting.

```ini
mms.ldap.global.role.owner=CN\=MMSGlobalOwner,OU\=MMS,OU\=acme Groups,DC\=acme,DC\=example,DC\=com
```

Corresponds to `LDAP Global Role Owner`.

**`mms.ldap.global.role.readOnly`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the
global read-only role in Ops Manager.

```ini
mms.ldap.global.role.readOnly=CN\=MMS-ReadOnly,OU\=MMS,OU\=acme Groups,DC\=acme,DC\=example,DC\=com
```

Corresponds to `LDAP Global Role Read Only`.

**`mms.ldap.global.role.userAdmin`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) group whose members have the global user admin role in Ops Manager.

```ini
mms.ldap.global.role.userAdmin=CN\=MMS-UserAdmin,OU\=MMS,OU\=acme Groups,DC\=acme,DC\=example,DC\=com
```

Corresponds to `LDAP Global Role User Admin`.

**`mms.ldap.group.baseDn`**

*Type*: string

*Default*: `LDAP User Base Dn` value

Base Distinguished Name (DN) that Ops Manager uses to search for
groups. If left blank, this setting uses the default value.

```ini
mms.ldap.group.baseDn=OU\=groups,DC\=acme,DC\=com
```

Corresponds to `LDAP Group Base Dn`.

**`mms.ldap.group.member`**

*Type*: string

Field on the group entry containing user Distinguished Names (DN).
The groupOfNames or
groupOfUniqueNames object classes are
commonly used.

```ini
mms.ldap.group.member=member
```

Corresponds to `LDAP Group Member Attribute`.

**`mms.ldap.group.separator`**

*Type*: string

*Default*: `;;`

To set the LDAP (Lightweight Directory Access Protocol) separator, follow the Modify a Custom Setting procedure using the following values:

|  |  |
|---|---|
| Key | `mms.ldap.group.separator` |
| Value | `<desired-separator>` |

Each of the global role values takes a delimited list of projects:

```ini
"dbas,sysadmins"
```

If a group value contains the delimiter, the delimiter must be set
to another value.

**Example:**

If you have the group value `"CN\=foo,DN\=bar"` and the
delimiter is `,` then Ops Manager parses `"CN\=foo,DN\=bar"` as two
elements rather than as the description for a single group.

**`mms.ldap.referral`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) field used to set how to handle referrals. Accepts two values:

- `ignore`: Ignore referrals.
- `follow`: Automatically follow any referrals.

Corresponds to `LDAP Referral`.

**`mms.ldap.ssl.CAFile`**

*Type*: string

A file containing one or more trusted certificates in PEM format.
Use this setting if you are using LDAPS (Secure Lightweight Directory Access Protocol) and the server is using a
certificate that is not from a well-known Certificate Authority.

```ini
mms.ldap.ssl.CAFile=/opt/CA.pem
```

Corresponds to `LDAP SSL CA File`.

**`mms.ldap.ssl.PEMKeyFile`**

*Type*: string

A file containing a client certificate and private key. Use this
setting when your TLS (Transport Layer Security)/SSL (Secure Sockets Layer) LDAP (Lightweight Directory Access Protocol) server requires client
certificates.

```ini
mms.ldap.ssl.PEMKeyFile=/opt/keyFile.pem
```

Corresponds to `LDAP SSL PEM Key File`.

**`mms.ldap.ssl.PEMKeyFilePassword`**

*Type*: string

Password for `LDAP SSL PEM Key File`. Use this setting
if the `PEMKeyFile` is encrypted.

```ini
mms.ldap.ssl.PEMKeyFilePassword=<password>
```

Corresponds to `LDAP SSL PEM Key File Password`.

**`mms.ldap.url`**

*Type*: string

URI (Uniform Resource Identifier) for the LDAP (Lightweight Directory Access Protocol) or LDAPS (Secure Lightweight Directory Access Protocol) server.

```ini
mms.ldap.url=ldaps://acme-dc1.acme.example.com:3890
```

Corresponds to `LDAP URI`.

**`mms.ldap.user.baseDn`**

*Type*: string

Base Distinguished Name (DN) that Ops Manager uses to search for
users.

Escape the `=` sign with `\`.

```ini
mms.ldap.user.baseDn=DC\=acme,DC\=example,DC\=com
```

Corresponds to `LDAP User Base Dn`.

**`mms.ldap.user.email`**

*Type*: string

*Default*: `mail` per RFC2256

LDAP (Lightweight Directory Access Protocol) user attribute that contains the user's email address.
After successful LDAP (Lightweight Directory Access Protocol) authentication, Ops Manager synchronizes the
specified LDAP (Lightweight Directory Access Protocol) attribute with the email address from the Ops Manager
user record.

```ini
mms.ldap.user.email=mail
```

Corresponds to `LDAP User Email`.

**`mms.ldap.user.firstName`**

*Type*: string

*Default*: `givenName` per RFC2256

LDAP (Lightweight Directory Access Protocol) user attribute that contains the user's first name. After
successful LDAP (Lightweight Directory Access Protocol) authentication, Ops Manager synchronizes the specified
LDAP (Lightweight Directory Access Protocol) attribute with the first name from the Ops Manager user record.

```ini
mms.ldap.user.firstName=givenName
```

Corresponds to `LDAP User First Name`.

**`mms.ldap.user.group`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) user attribute that contains the list of LDAP (Lightweight Directory Access Protocol) groups
the user belongs to. The LDAP (Lightweight Directory Access Protocol) attribute can use any format to list
the projects, including Common Name (`cn`) or Distinguished Name
(`dn`). All Ops Manager settings in this configuration file that specify
projects must match the chosen format.

**Important:**

Ops Manager deprecated `mms.ldap.user.group`. Use `mms.ldap.group.member`.

If you provide values for:

- Both `mms.ldap.user.group` and `mms.ldap.group.member`, Ops Manager uses
  `mms.ldap.group.member` and ignores `mms.ldap.user.group`.
- `mms.ldap.user.group` only, Ops Manager doesn't recognize
  the user's membership in nested LDAP groups.

```ini
mms.ldap.user.group=memberOf
```

Corresponds to `LDAP User Group`.

**`mms.ldap.user.lastName`**

*Type*: string

*Default*: `surname` per RFC2256

LDAP (Lightweight Directory Access Protocol) user attribute that contains the user's last name. After
successful LDAP (Lightweight Directory Access Protocol) authentication, Ops Manager synchronizes the specified
LDAP (Lightweight Directory Access Protocol) attribute with the last name from the Ops Manager user record.

```ini
mms.ldap.user.lastName=sn
```

Corresponds to `LDAP User Last Name`.

**`mms.ldap.user.searchAttribute`**

*Type*: string

LDAP (Lightweight Directory Access Protocol) field used for the LDAP (Lightweight Directory Access Protocol) search. This is typically a
username or an email address. The value of this field is also used
as the Ops Manager username.

```ini
mms.ldap.user.searchAttribute=<myAccountName>
```

Corresponds to `LDAP User Search Attribute`.

**`mms.login.newDeviceNotification.enabled`**

*Type*: boolean

Indicator as to the user should be notified that they have logged
in from a new device.

Corresponds to `New Device Login Notification`.

### Authentication through SAML

**`mms.saml.idp.uri`**

*Type*: string

URI (Uniform Resource Identifier) of the Identity Provider (IdP (Identity Provider)) that you use to coordinate
your Single Sign-On. This might be referred to as the *EntityId* or
the *Identity Provider Issuer*.

**`mms.saml.sso.url`**

*Type*: string

URL (Uniform Resource Locator) of the Single Sign-On endpoint that Ops Manager calls when a user
attempts to sign in.

**`mms.saml.slo.url`**

*Type*: string

URL (Uniform Resource Locator) of the Single Logout endpoint that Ops Manager calls when a user
attempts to log out. If set, when a user attempts to log out of
Ops Manager, they log out of your IdP (Identity Provider). If left blank, logging out of
Ops Manager doesn't log the user out of their IdP (Identity Provider) session.

**`mms.saml.x509.cert`**

*Type*: string

Certificate provided by your IdP (Identity Provider) that Ops Manager uses to verify its
validity to the IdP (Identity Provider).

**`mms.saml.ssl.PEMKeyFile`**

*Type*: string

Absolute path to the PEM file for the certificate that the SP (Service Provider)
uses to sign requests, containing both the private and public key. If
this is left blank, Ops Manager doesn't sign SAML (Security Assertion Markup Language) auth requests to the
IdP (Identity Provider) and you can't encrypt SAML (Security Assertion Markup Language) assertions.

**`mms.saml.ssl.PEMKeyFilePassword`**

*Type*: string

Required if the PEM (Privacy-Enhanced Mail) file contains an encrypted private key. Specify
the password for PEM (Privacy-Enhanced Mail) file.

**`mms.saml.encrypted.assertions`**

*Type*: boolean

Flag that indicates whether or not the IdP (Identity Provider) encrypts the assertions
it sends to Ops Manager.

**`mms.saml.signedAssertions`**

*Type*: boolean

*Default*: `true`

Flag that indicates whether or not the IdP (Identity Provider) signs the assertions
it sends to Ops Manager.

**Important:**

Ensure that either the assertions or the response are signed. 
The configuration will fail the verification and Ops Manager returns 
an error if either the assertions or the response aren't signed.

Corresponds to `SAML Signed Assertions`.

**`mms.saml.signedMessages`**

*Type*: boolean

*Default*: `true`

Flag that indicates whether or not the IdP (Identity Provider) signs the responses
it sends to Ops Manager.

**Important:**

Ensure that either the assertions or the response are signed. 
The configuration will fail the verification and Ops Manager returns 
an error if either the assertions or the response aren't signed.

Corresponds to `SAML Signed Messages`.

**`mms.saml.signature.algorithm`**

*Type*: string

Algorithm to encrypt the signature sent to and from the IdP (Identity Provider).

You must use one of the following full W3.org signature algorithm values:

- `http://www.w3.org/2001/04/xmldsig-more#rsa-sha1`
- `http://www.w3.org/2000/09/xmldsig#dsa-sha1`
- `http://www.w3.org/2001/04/xmldsig-more#rsa-sha256`
- `http://www.w3.org/2001/04/xmldsig-more#rsa-sha384`
- `http://www.w3.org/2001/04/xmldsig-more#rsa-sha512`

**Important:**

You must specify the complete W3.org signature algorithm URL, not 
a simple string value. Using simple string values, such as `rsa-sha256`, 
causes Ops Manager to return an `unauthorized` error because the 
IdP (Identity Provider) cannot validate the signatures properly.

**Example:**

```text
mms.saml.signature.algorithm=http://www.w3.org/2001/04/xmldsig-more#rsa-sha256
```

**`mms.saml.global.role.owner`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have full
privileges over this deployment, including full access to all groups
and all administrative permissions.

**`mms.saml.global.role.automationAdmin`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global Automation Admin` role.

**`mms.saml.global.role.backupAdmin`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global Backup Admin` role.

**`mms.saml.global.role.monitoringAdmin`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global Monitoring Admin` role.

**`mms.saml.global.role.userAdmin`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global User Admin` role.

**`mms.saml.global.role.readOnly`**

*Type*: string

Group in the SAML (Security Assertion Markup Language) Group Member Attribute whose members have the
`Global Read Only` role.

**`mms.saml.user.firstName`**

*Type*: string

SAML (Security Assertion Markup Language) User Attribute that contains the user's first name.

**`mms.saml.user.lastName`**

*Type*: string

SAML (Security Assertion Markup Language) User Attribute that contains the user's last name.

**`mms.saml.user.email`**

*Type*: string

SAML (Security Assertion Markup Language) User Attribute that contains the user's email address.

**`mms.saml.group.member`**

*Type*: string

*Default*: `groups`

SAML (Security Assertion Markup Language) Attribute that contains the list of groups Ops Manager uses to
map roles to Projects and Organizations.

Corresponds to `SAML Group Member Attribute`.

### Multi-Factor Authentication (MFA)

**`mms.multiFactorAuth.level`**

*Type*: string

*Default*: OFF

Configures the two-factor authentication "level":

| Setting | Description |
|---|---|
| `OFF` | Disables two-factor authentication. Ops Manager does not use two-factor authentication. |
| `OPTIONAL` | Users can choose to set up two-factor authentication for their Ops Manager account. |
| `REQUIRED_FOR_GLOBAL_ROLES` | Users who possess a global role *must* set up two-factor authentication. Two factor authentication is optional for all other users. |
| `REQUIRED` | *All* users must set up two-factor authentication for their Ops Manager account. |

Two-factor authentication is recommended for the security of your
Ops Manager deployment.

**Warning:**

If enabling `mms.multiFactorAuth.level` through the
configuration file, you must create a
user account first before updating the
configuration file. Otherwise, you cannot login to Ops Manager.

**Note:**

If you enable Twilio integration
(optional), ensure that Ops Manager servers can access the
`twilio.com` domain.

Corresponds to `Multi-factor Auth Level`.

**`mms.multiFactorAuth.allowReset`**

*Type*: boolean

*Default*: False

When `true`, Ops Manager allows users to reset their two-factor
authentication settings via email in an analogous fashion to
resetting their passwords.

To reset two-factor authentication, a user must:

- be able to receive email at the address associated with the user
  account.
- know the user account's password.
- know the `agent API key` for each Ops Manager project the user
  belongs to.

Corresponds to `Multi-factor Auth Allow Reset`.

**`mms.multiFactorAuth.issuer`**

*Type*: string

If Google Authenticator provides two-factor authentication, this
string is the `issuer` in the Google Authenticator app. If left
blank, the `issuer` is the domain name of the Ops Manager installation.

Corresponds to `Multi-factor Auth Issuer`.

**`mms.multiFactorAuth.require`**

*Type*: boolean

*Default*: False

When `true`, Ops Manager will require two-factor authentication for
users to log in or to perform certain destructive operations within
the application.

If you configure
Twilio integration,
users may obtain their second factor tokens via Google
Authenticator, SMS, or voice calls. Otherwise, the only mechanism
to provide two-factor authentication is Google Authenticator.

### reCaptcha and Session Length

**`reCaptcha.enabled.registration`**

*Type*: boolean

*Default*: false

Indicator as to you want a new user to validate themselves
using reCaptcha validation when they register to use Ops Manager.

Set to `true` to require
[reCaptcha](https://www.google.com/recaptcha)
validation when a new user registers.

This setting requires a
[reCaptcha account](https://www.google.com/recaptcha/admin).

Corresponds to `ReCaptcha Enabled On Registration`.

**`reCaptcha.enabled`**

*Type*: boolean

*Default*: false

Indicator as to you want a user to validate themselves using
reCaptcha validation when they log into Ops Manager.

Set to `true` to require
[reCaptcha](https://www.google.com/recaptcha)
validation when a user logs in.

This setting requires a
[reCaptcha account](https://www.google.com/recaptcha/admin).

Corresponds to `ReCaptcha Enabled`.

**`reCaptcha.private.key`**

*Type*: string

ReCaptcha private key associated with your account.

Corresponds to `ReCaptcha Private Key`.

**`reCaptcha.public.key`**

*Type*: string

ReCaptcha public key associated with your account.

Corresponds to `ReCaptcha Public Key`.

**`mms.session.maxHours`**

*Type*: number

Number of hours before a session on the Ops Manager website expires.

**Note:**

Session Max Hours reflects the total Ops Manager session time, not
just idle time. Both active and idle sessions expire when 
Session Max Hours elapses.

Set this value to `0` to use browser session cookies only.

Corresponds to `Session Max Hours`.

**`mms.session.mode`**

*Type*: String

Either `None` or `Idle`.

`None` disables idle session timeout.
`Idle` logs users out after a period of inactivity.

**`mms.session.idleTimeoutMinutes`**

*Type*: number

The maximum amount of time in minutes that a session can be active with no user activity.

## Web Server

**`mms.centralUrl`**

*Type*: string

FQDN (fully qualified domain name) and port number of the Ops Manager Application.

To use a port other than `8080`, see
/tutorial/manage-ports.

```ini
mms.centralUrl=http://mms.example.com:8080
```

Corresponds to `URL to Access Ops Manager`.

**Important:**

If you plan on accessing your Ops Manager Application using its IPv6 (Internet Protocol version 6)
address, you must enclose the IPv6 (Internet Protocol version 6) address in square brackets
(`[ ]`) to separate it from its port number.

For example: 

```ini
http://[2600:1f16:777:8700:93c2:b99c:a875:2b10]:8080
```

**`mms.https.PEMKeyFile`**

*Type*: string

Absolute path to the PEM file that contains the Ops Manager Application's
valid certificate and private key. The PEM file is required if the
Ops Manager Application uses HTTPS (Hypertext Transfer Protocol Secure) to encrypt connections between the
Ops Manager Application, the agents, and the web interface.

The default port for HTTPS (Hypertext Transfer Protocol Secure) access to the Ops Manager Application is
`8443`, as set in `<install_dir>/conf/mms.conf` file. If you
change this default, you must also change the port specified in the
`mms.centralUrl` setting.

Corresponds to `HTTPS PEM Key File`.

**`mms.https.PEMKeyFilePassword`**

*Type*: string

Password for the HTTPS (Hypertext Transfer Protocol Secure) PEM key file. You must include this setting
if the PEM (Privacy-Enhanced Mail) key file contains an encrypted private key.

Corresponds to `HTTPS PEM Key File Password`.

**`mms.https.ClientCertificateMode`**

*Type*: string

Specifies if Ops Manager requires clients to present valid TLS (Transport Layer Security)/SSL (Secure Sockets Layer)
client certificates when connecting to it. Accepted values are:

- `none`
- `agents_only`
- `required`

Corresponds to `Client Certificate Mode`.

**`mms.https.CAFile`**

*Type*: string

Required if:

- You are using a private certificate authority.
- You set `mms.https.ClientCertificateMode` to
  `agents_only` or `required`.
- You run Ops Manager in hybrid mode with TLS (Transport Layer Security) enabled.

Specifies the filesystem location of a private certificate authority
file containing the list of acceptable client certificates. The
Ops Manager Application authenticates HTTPS (Hypertext Transfer Protocol Secure) requests from clients bearing a
certificate described in this file.

```ini
mms.https.CAFile=/path/to/ca_file.pem
```

Corresponds to `CA File`.

**`mms.https.dualConnectors`**

*Type*: boolean

*Default*: False

Enables connections to Ops Manager using HTTP (Hypertext Transfer Protocol) and HTTPS (Hypertext Transfer Protocol Secure) concurrently.

You can use this setting temporarily while you upgrade Ops Manager and the
MongoDB Agent\s to use TLS (Transport Layer Security). To ensure zero downtime, set to
`true` and provide a value for `mms.http.bindhostname`.
After you configure Ops Manager and the MongoDB Agent\s, set to `false`.

**Important:**

Ops Manager is accessible using insecure connections while
`mms.https.dualConnectors` is `true`.

Set `mms.https.dualConnectors` to `false` to allow secure
connections only after you have updated the MongoDB Agent\s to use
TLS (Transport Layer Security) connections.

**`mms.http.bindhostname`**

*Type*: string

*Default*: 127.0.0.1

The hostname or IP (Internet Protocol) at which MongoDB Agent\s can connect to
Ops Manager using HTTP (Hypertext Transfer Protocol).

You can use this setting temporarily while you upgrade Ops Manager and the
MongoDB Agent\s to use TLS (Transport Layer Security). To ensure zero downtime, set a value and
set `mms.https.dualConnectors` to `true`. After you
configure Ops Manager and the MongoDB Agent\s, remove the value.

**`mms.remoteIp.header`**

*Type*: string

If you use a load balancer with the Ops Manager Application, set this to the
HTTP (Hypertext Transfer Protocol) header field the load balancer uses to identify the
originating client's IP address to the Ops Manager host. When you
specify `Load Balancer Remote IP Header`, do not allow
clients to connect directly to any Ops Manager host. A load
balancer placed in front of the Ops Manager hosts must not
return cached content.

Once `Load Balancer Remote IP Header` is set, Ops Manager
enables the following HTTP (Hypertext Transfer Protocol) headers:

| HTTP (Hypertext Transfer Protocol) Header | Forwards to Ops Manager |
|---|---|
| X-Forwarded-Host | Original host that the client requested in the Host HTTP (Hypertext Transfer Protocol) request header. |
| X-Forwarded-Proto | Protocol used to make the HTTP (Hypertext Transfer Protocol) request. |
| [X-Forwarded-Server](https://www.eclipse.org/jetty/javadoc/current/org/eclipse/jetty/server/ForwardedRequestCustomizer.html) | Hostname of the proxy server. |
| [X-Proxied-Https](https://www.eclipse.org/jetty/javadoc/current/org/eclipse/jetty/server/ForwardedRequestCustomizer.html) | HTTPS (Hypertext Transfer Protocol Secure) status of a request. |

To learn more, see
/tutorial/configure-application-high-availability.

Corresponds to `Load Balancer Remote IP Header`.

**`mms.minimumTLSVersion`**

*Type*: string

*Default*: `TLSv1.2`

Specifies the TLS (Transport Layer Security) version required for clients to connect to Ops Manager.
This property affects all clients, such as browsers used to connect
to the Ops Manager Admin interface and command-line tools, such
as `curl`, used to connect to the REST (Representational State Transfer) API (Application Programming Interface).

Ops Manager versions between 4.0.9 and 4.0.18 and earlier than 4.2.13 and 4.4.0
  Ops Manager supports `TLSv1.2` only. If you change this value to
  anything other than `TLSv1.2`, including a blank value, you can't
  connect to this Ops Manager.

Ops Manager versions 4.0.0 to 4.0.8, 4.0.18 or later, 4.2.13 or later, 4.4.0 or later
  Ops Manager supports `TLSv1.0`, `TLSv1.1` and `TLSv1.2`.

**Note:**

TLSv1.2 requires connecting clients to meet the following minimum
requirements:

* Browser supports TLS (Transport Layer Security) version 1.2

* `curl` version 7.34.0+

* OpenSSL version 1.0.1+

To set `minimum.TLSVersion`, follow the Modify a Custom
Setting procedure with the following
values:

|  |  |
|---|---|
| Key | `minimum.TLSVersion` |
| Value | `<tls-versions>` |

**`mms.disableCiphers`**

*Type*: string

*Default*: `SSL_DHE_DSS_WITH_3DES_EDE_CBC_SHA`,
`SSL_DHE_DSS_WITH_DES_CBC_SHA`,
`SSL_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA`,
`SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA`, `SSL_DHE_RSA_WITH_DES_CBC_SHA`,
`SSL_RSA_EXPORT_WITH_DES40_CBC_SHA`,
`SSL_RSA_EXPORT_WITH_RC4_40_MD5`,
`TLS_DHE_DSS_WITH_AES_128_CBC_SHA256`,
`TLS_DHE_DSS_WITH_AES_128_CBC_SHA`,
`TLS_DHE_DSS_WITH_AES_256_CBC_SHA256`,
`TLS_DHE_DSS_WITH_AES_256_CBC_SHA`,
`TLS_DHE_RSA_WITH_AES_128_CBC_SHA256`,
`TLS_DHE_RSA_WITH_AES_128_CBC_SHA`,
`TLS_DHE_RSA_WITH_AES_128_GCM_SHA256`,
`TLS_DHE_RSA_WITH_AES_256_CBC_SHA256`,
`TLS_DHE_RSA_WITH_AES_256_CBC_SHA`,
`TLS_DHE_RSA_WITH_AES_256_GCM_SHA384`,
`TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`,
`TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`

Specifies a list of TLS (Transport Layer Security) cipher suites which your instance of Ops Manager
can't accept when clients connect to the Ops Manager Application and API (Application Programming Interface).
Specify TLS (Transport Layer Security) cipher suite names as a comma-separated list, as in
the following example.

**Important:**

Cipher suite names used in Ops Manager must follow RFC 5246 naming conventions. Do not use the OpenSSL
naming convention. For convenience, Ops Manager logs a list of all
supported cipher suite names during startup. If Ops Manager does not
recognize a TLS (Transport Layer Security) cipher suite name, it logs the following
warning:

Your config lists the following as ciphers which should be
disabled as the JDK (Java Development Kit) does not recognize them. Please check the
format of the entries and list of enabled ciphers.
[*unrecognized_cipher_name*]

To change `mms.disableCiphers`, follow the Modify a Custom
Setting procedure with the following
values:

* - Key
  - `mms.disableCiphers`
* - Value
  - `<ciphers>`

    For example:

    ```ini
    TLS_DHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_DHE_RSA_WITH_AES_256_CBC_SHA256
    ```

**Warning:**

Setting `mms.disableCiphers` to a custom value could
re-enable one or more of these disabled ciphers.

## Webhook

**`mms.alerts.webhook.adminEndpoint`**

*Type*: string

Corresponds to `Webhook URL`.

**`mms.alerts.webhook.adminSecret`**

*Type*: string

Corresponds to `Webhook Secret`.
