<!-- Part 2 of 5 of reference/configuration.md (split because the page is big). -->

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
