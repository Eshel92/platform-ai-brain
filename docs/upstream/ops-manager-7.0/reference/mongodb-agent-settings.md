<!-- Converted from reference/mongodb-agent-settings.txt (reStructuredText). Includes are inlined. -->

# MongoDB Agent Settings

This page describes possible settings for the MongoDB Agent. These
values are set after first launching Ops Manager and not through manual
editing of these files.

To learn about the Ops Manager settings and their values, see
/reference/configuration/.

**Warning:**

If you edit authentication or TLS (Transport Layer Security) settings through
Settings or Deployments in the Ops Manager
interface, those changes overwrite any manual changes in this
configuration file.

## Configuration File & Settings Locations

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

You can configure additional
Monitoring settings and
Backup settings through the
Ops Manager Console.

## MongoDB Agent Settings

**`mmsGroupId`**

*Type*: string

Specifies the ID of your Ops Manager project. Find the project ID on the
Project Settings page (Settings >
Project Settings).

Ops Manager configures this setting when you install the MongoDB Agent. If
you need to configure Monitoring separately, include this setting to
bind the server to a project.

```ini
mmsGroupId=8zvbo2s2asigxvmpnkq5yexf
```

**`mmsApiKey`**

*Type*: string

Specifies the MongoDB Agent API (Application Programming Interface) key of your Ops Manager project.

You can use an Agent API key that you have already generated for the
project. Otherwise, you can generate a new Agent API key. A project can
have more than one Agent API key, and any of the project's agents can
use any of the keys. For more information, see
/tutorial/manage-agent-api-key.

To generate an Agent API key, go to the Agent API Keys
tab. To navigate to the tab, from the Deployment view,
click the Agents tab and then the Agent API
Keys tab.

**Important:**

When you generate an Agent API Key, Ops Manager displays it **one time
only**. You must copy this key. Treat it like a password; store
it in a secure place. Ops Manager never displays the full key again.

Ops Manager configures this setting when you install the MongoDB Agent. If
you need to configure Monitoring separately, include this setting.

```ini
mmsApiKey=rgdte4w7wwbnds9nceuodx9mcte2zqem
```

**`mmsBaseUrl`**

*Type*: string

Specifies the URL of the Ops Manager Application.

```ini
mmsBaseUrl=http://example.com:8080
```

### Logging Settings

**`logFile`**

*Type*: string

Specifies the path to which Ops Manager should write the MongoDB Agent's
log.

The default path depends on your platform. The MongoDB Agent uses the
default filename `automation-agent.log` whether or not the
deployment uses Automation.

**Important:**

Automatic rotation of your MongoDB Agent logs only occurs when an update to the log file is made.
To manually rotate your MongoDB Agent logs, 
see Manually Rotate the MongoDB Agent Logs for more information.

| Platform | Default Path |
|---|---|
| Linux | `/var/log/mongodb-mms-automation/automation-agent.log` |
| Windows | `C:\MMSAutomation\log\mongodb-mms-automation\automation-agent.log` |

```ini
logFile=/path/to/mongodb-mms-automation/automation-agent.log
```

**`logLevel`**

*Type*: string

Specifies the level of logging granularity.

**Warning:**

The Admin Project Settings 
for Monitoring Agent Log Level and 
Automation Agent Log Level override this 
parameter.

Choose from the following severity levels, from most to least
amount of information:

- `DEBUG`
- `INFO`
- `WARN`
- `ERROR`
- `FATAL`

By default, `logLevel` is `INFO`.

```ini
logLevel=ROUTINE
```

Each level includes the log items included in the succeeding levels.

**Example:**

- If you choose `DEBUG`, the MongoDB Agent logs all
  messages, including `INFO`, `WARN`, `ERROR`
  and `FATAL`.

- If you choose `FATAL`, the MongoDB Agent only logs
  `FATAL` messages.

**`maxLogFiles`**

*Type*: integer

Specifies the maximum number of rotated log files to retain.

By default, the value of `maxLogFiles` is set to `10`. You
can change the value to retain a different number of rotated log files.

```ini
maxLogFiles=15
```

**`maxLogFileDurationHrs`**

*Type*: float

Specifies the number of hours after which the logs are rotated.

**Note:** Manually Rotate the MongoDB Agent Logs

On UNIX- and Linux-based systems you can manually rotate the
MongoDB Agent logs. Issue a `kill` command with the
`SIGUSR1` signal for the Agent process:

```sh
kill -SIGUSR1 <AgentID>
```

On Windows-based systems, you can manually restart the
MongoDB Agent with a Service restart:

1. Click the Start menu.
#. Search for `services`.
#. Find the MongoDB Agent.
#. Right-click on the Agent and click Restart.

This rotates the MongoDB Agent logs.

**`maxLogFileSize`**

*Type*: integer

Specifies the maximum size, in bytes, of a log file before the logs
are rotated. If unspecified, the MongoDB Agent does not rotate
logs based on file size.

By default, the value of `maxLogFileSize` is set to `268435456` bytes. You
can change the value to assign a different maximum size for a log file. 

```ini
maxLogFileSize=536870912
```

**`maxUncompressedLogFiles`**

*Type*: integer

Specifies the maximum number of rotated log files to keep
uncompressed. MongoDB Agent automatically compresses any additional
retained log files up to the `maxLogFiles` value.

By default, the value of `maxUncompressedLogFiles` is set
to `2`. You can change the value to compress a different number of
rotated log files.

```ini
maxUncompressedLogFiles=10
```

### Connection Settings

**`dialTimeoutSeconds`**

*Type*: integer

Specifies the number of seconds to wait before a connection times
out. By default, connections time out after 40 seconds. However, The
MongoDB Agent may frequently time out of connections for one or more
of the following reasons:

- High network latency

- High server load

- Large TLS (Transport Layer Security) keys

- Lack of TLS (Transport Layer Security) accelerator

- Insufficient CPU speed

MongoDB recommends gradually increasing the value of the
`dialTimeoutSeconds` MongoDB Agent configuration setting
to prevent frequent premature connection timeouts.

```ini
dialTimeoutSeconds=40
```

**Note:**

Increasing this value also increases the time required to deploy
configuration changes to the MongoDB Agent. Experiment with
small, incremental increases until you determine the optimum
value for your deployment.

**`serverSelectionTimeoutSeconds`**

*Type*: integer

Specifies the number of seconds the MongoDB Agent waits before it
stops trying to establish a connection to a MongoDB process. By
default, the MongoDB Agent abandons attempts to establish a
connection after 10 seconds.

```ini
serverSelectionTimeoutSeconds=10
```

### HTTP Proxy Settings

**`httpProxy`**

*Type*: string

Specifies the URL (Uniform Resource Locator) of an HTTP (Hypertext Transfer Protocol) proxy server the MongoDB Agent can
use.

```ini
httpProxy=http://proxy.example.com:8080
```

### Configuration Backup Settings

**`mmsConfigBackup`**

*Type*: string

Specifies the path to the Ops Manager configuration backup file. This file
describes the desired state of the deployment.

If you don't specify the `mmsConfigBackup` setting, the 
MongoDB Agent writes the 
`mongodb-mms-automation-cluster-backup.json` file to a temporary 
folder on the operating system.

If you set `enableLocalConfigurationServer` to `true`, 
the MongoDB Agent doesn't write the `mmsConfigBackup` file.

```ini
mmsConfigBackup=/path/to/mms-cluster-config-backup.json
```

**Note:**

When Ops Manager is installed, it stores the configuration backup
file is stored in one of the following places, depending on
your platform:

| Platform | Configuration Backup File Path |
|---|---|
| Linux | `/var/lib/mongodb-mms-automation/` |
| Windows | `%SystemDrive%\MMSAutomation` |

### Ops Manager TLS (Transport Layer Security) Settings

Specify the settings that the MongoDB Agent uses when communicating
with Ops Manager using TLS (Transport Layer Security).

**`httpsCAFile`**

*Type*: string

Specifies the *absolute* path that contains the trusted Certificate Authority
certificates in `PEM` format. This certificate verifies that the
MongoDB Agent is talking to the designated Ops Manager instance.

```ini
httpsCAFile=/path/to/ca.pem
```

**Note:**

Add the Certificate Authority for the `downloads.mongodb.com` certificate
to this `.pem` file if you:

1. Need your MongoDB Agents to download their MongoDB installers
   from the Internet,

#. Use TLS to encrypt connections, and

#. Signed your certificates with a private Certificate Authority. (You set
   the `httpsCAFile` option.)

To learn how to download TLS (Transport Layer Security) certificates from another web
site, see the
[OpenSSL Cookbook entry](https://www.feistyduck.com/library/openssl-cookbook/online/ch-testing-with-openssl.html#extracting-remote-certificates).

**Important:**

When Ops Manager starts, it caches the Certificate Authority you provided. If you
change your Certificate Authority certificate, restart Ops Manager.

**`sslRequireValidMMSServerCertificates`**

*Type*: boolean

**Important:**

Deprecated. Use `tlsRequireValidMMSServerCertificates`
instead.

**`tlsRequireValidMMSServerCertificates`**

*Type*: boolean

Specifies if the MongoDB Agent should validate TLS (Transport Layer Security) certificates
presented by Ops Manager.

**Warning:**

Setting this option to `false` disables certificate
verification and makes connections between the MongoDB Agent
and Ops Manager susceptible to *man-in-the-middle*
attacks. Setting this option to `false` is only recommended for
testing purposes.

```ini
tlsRequireValidMMSServerCertificates=true
```

**`sslMMSServerClientCertificate`**

*Type*: string

**Important:**

Deprecated. Use `tlsMMSServerClientCertificate` 
instead.

**`tlsMMSServerClientCertificate`**

*Type*: string

Specifies the path to the file containing the client's private
key, certificate, and optional intermediate certificates in
`PEM` format. The MongoDB Agent uses the client certificate
when connecting to Ops Manager over TLS (Transport Layer Security) if Ops Manager requires client
certificates, such as when Ops Manager runs with `Client
Certificate Mode` set to `Required for Agents Only` or
`Required for All Requests`.

**See also:**

To learn how to set `Client Certificate Mode`, see
/reference/configuration.

The encrypted private key for the `.pem` certificate file must be in
PKCS #1 format. The MongoDB Agent doesn't support
the PKCS #8 format.

```ini
tlsMMSServerClientCertificate=/path/to/client.pem        
```

**`sslMMSServerClientCertificatePassword`**

*Type*: string

**Important:**

Deprecated. Use `tlsMMSServerClientCertificatePassword` 
instead.

**`tlsMMSServerClientCertificatePassword`**

*Type*: string

Specifies the password needed to decrypt the private key in
the `tlsMMSServerClientCertificate` file. This setting is
required when the client certificate `PEM` file is
encrypted.

The encrypted private key for the `.pem` certificate file must be in
PKCS #1 format. The MongoDB Agent doesn't support
the PKCS #8 format.

**Note:**

Use the
`tlsMMSServerClientCertificatePasswordExec` option
instead of `tlsMMSServerClientCertificatePassword` to 
specify the password from a shell command.

```ini
tlsMMSServerClientCertificatePassword=password
```

**`sslServerClientCertificate`**

*Type*: string

Specifies the path to the file containing the client's private
key, certificate, and optional intermediate certificates in
`PEM` format. The MongoDB Agent uses the client certificate
when connecting to Ops Manager over TLS (Transport Layer Security) if Ops Manager requires client
certificates, such as when Ops Manager runs with `Client
Certificate Mode` set to `Required for Agents Only` or
`Required for All Requests`.

**See also:**

- See `Client Certificate Mode` in
  conf-mms.properties for how to specify this
  setting in the Ops Manager Application.

- See configure-tls-mdbagent to enable TLS (Transport Layer Security)
  connections for the MongoDB Agent.

```ini
sslServerClientCertificate=/path/to/client.pem
```

**`sslServerClientCertificatePassword`**

Specifies the password needed to decrypt the private key in
the `sslServerClientCertificate` file. This setting is
required when the client certificate `PEM` file is
encrypted.

```ini
sslServerClientCertificatePassword=password
```

**`sslRequireValidMMSBackupServerCertificate`**

Specifies if the MongoDB Agent should validate TLS (Transport Layer Security) certificates
from Ops Manager.

**Warning:**

Setting this option to `false` disables certificate
verification and makes connections between the MongoDB Agent and
Ops Manager susceptible to *man-in-the-middle* attacks. Setting this
option to `false` is only recommended for testing purposes.

```ini
sslRequireValidMMSBackupServerCertificate=true
```

### Push Live Migration Settings

**`agentFeatureCloudMigrationEnabled`**

*Type*: boolean

*Optional*.

Specifies whether the MongoDB Agent on the migration host
is configured to run the Live Migration process from a source Ops Manager deployment
to a target cluster in Atlas.

This option defaults to `false`, which prevents using the MongoDB Agent
on this host for Live Migration to Atlas.

To enable the Live Migration process, provision a migration host and set
`agentFeatureCloudMigrationEnabled` to `true`.

**`cloudMigrationOplogPath`**

*Type*: string

*Optional*.

Path to the oplog files. If specified, this setting
buffers the initial sync oplog window to disk.
Provision enough storage in the specified directory for
the oplog buffering.

### Externally Sourced Configuration Settings

**`enableLocalConfigurationServer`**

*Type*: boolean

Specifies whether the MongoDB Agent stores MongoDB process
configuration files on disk or cached in memory.

This option defaults to `false`, which stores the
configuration files on disk. Setting this option to `true` caches
the configuration in memory.

If you set this option to `true`, the MongoDB Agent doesn't write
the `mmsConfigBackup` file.

Don't set this option to `true` if your MongoDB databases are running
FCV 4.2 or earlier.

**Warning:**

Setting this option to `true` impacts the availability of your
deployment.

When this feature is enabled, the MongoDB Agent doesn't store the MongoDB
process configuration on disk. If the Ops Manager app server
is unavailable and the MongoDB Agent attempts to restart, then the
MongoDB Agent stops running because it doesn't have the necessary
configuration information. If a MongoDB process crashes while the
MongoDB Agent isn't running, then the MongoDB Agent can't restart the
process. 

```ini
enableLocalConfigurationServer=false
```

**See also:**

/reference/mongodb-agent-external-configuration

      

**`keepUnusedMongodbVersions`**

*Type*: boolean

Flag that indicates whether the MongoDB Agent retains unused MongoDB
version binaries that it downloads. By default,
`keepUnusedMongodbVersions` is false.

```ini
keepUnusedMongodbVersions=false
```

**`localConfigurationServerPort`**

*Type*: integer

Specifies the port to serve the MongoDB process configuration to
when using the local configuration server. To set this option,
`enableLocalConfigurationServer` must be `true`.

If unspecified, the MongoDB Agent chooses an available port
automatically.

```ini
localConfigurationServerPort=20128
```

**`mmsApiKeyExec`**

*Type*: string

Specifies a shell command to call the Ops Manager agent API (Application Programming Interface) key of your
Ops Manager project.

```ini
mmsApiKeyExec=echo $myKey
```

**`sslMMSServerClientCertificatePasswordExec`**

*Type*: string

**Important:**

Deprecated. Use `tlsMMSServerClientCertificatePasswordExec`
instead.

**`tlsMMSServerClientCertificatePasswordExec`**

*Type*: string

Specifies a shell command to call the password needed to decrypt
the private key in the `MMSServerClientCertificate` file.
Either this setting or
`tlsMMSServerClientCertificatePassword` is required when
the client certificate `PEM` file is encrypted.

```ini
tlsMMSServerClientCertificatePasswordExec=python /path/to/PEMPassword.py
```

## Transparent Huge Page (THP) Settings

**`enableAgentManagingTHPSettings`**

*Type*: boolean

Specifies whether the MongoDB Agent manages disabling Transparent 
Huge Pages (THP) for MongoDB processes. See Disable Transparent Huge Pages (THP) 
to learn more.

This option defaults to `false`.

When set to `true`, the MongoDB Agent disables THP on a per-process basis, overriding any OS-level THP settings. 
This option will only affect deployed `mongod` and `mongos` processes on Linux systems using a MongoDB version 
earlier than 8.0.

```ini
enableAgentManagingTHPSettings=false
```

## Automation Settings

The following configuration settings are used for authentication in
automated clusters.

### MongoDB Kerberos Settings

Specify these settings if Automation authenticates to hosts
using Kerberos. To configure Kerberos, see
/tutorial/configure-mongodb-agent-for-kerberos.

**`krb5ConfigLocation`**

*Type*: string

Specifies an *absolute* path to an non-system-standard location for
the Kerberos configuration file.

```ini
krb5ConfigLocation=/path/to/krb_custom.conf
```

**Note:**

Ops Manager creates a Kerberos Credential (Ticket) Cache for each agent
automatically when Kerberos is enabled. If you want to override the
location of the 
[Kerberos Credential Cache](https://web.mit.edu/kerberos/krb5-latest/doc/basic/ccache_def.html),
you must set the `KRB5CCNAME` environment variable to the desired
file name and path before running the agent.

## Monitoring Settings

Use the Ops Manager interface to configure Monitoring settings.

### Log Settings

1. In the navigation, click Deployment.
#. Click the Agents tab.
#. Click Downloads & Settings.
#. In the Agent Log Settings section, click
   `edit` next to Monitoring Log Settings.
#. Edit the Monitoring log settings:

   | Setting | Default Value | Console Suggested Value |
   |---|---|---|
   | Linux Log File Path | `/var/log/mongodb-mms-automation/monitoring-agent.log` |  |
   | Windows Log File Path | `%SystemDrive%\MMSAutomation\log\mongodb-mms-automation\monitoring-agent.log` |  |
   | Rotate Logs | YES |  |
   | Size Threshold (MB) | 1000 |  |
   | Time Threshold (Hours) | 24 |  |
   | Max Uncompressed Files |  | 5 |
   | Max Percent of Disk |  | 2 |
   | Total Number of Log Files | 0 |  |

#. Click Save.

### Custom Settings

1. In the navigation, click Deployment.
#. Click the Agents tab.
#. Click Downloads & Settings.
#. In the Custom Configuration section, next to
   Edit Custom Configurations, click `edit`.
#. Enter the Monitoring configuration setting and value.
#. Click Save and Close.

You can configure the following Monitoring settings:

#### Connection Settings

**`mmsGroupId`**

*Type*: string

Specifies the ID of your Ops Manager project. Find the project ID on the
Project Settings page (Settings >
Project Settings).

Ops Manager configures this setting when you install the MongoDB Agent. If
you need to configure Monitoring separately, include this setting to
bind the server to a project.

```ini
mmsGroupId=8zvbo2s2asigxvmpnkq5yexf
```

**`mmsApiKey`**

*Type*: string

Specifies the MongoDB Agent API (Application Programming Interface) key of your Ops Manager project.

You can use an Agent API key that you have already generated for the
project. Otherwise, you can generate a new Agent API key. A project can
have more than one Agent API key, and any of the project's agents can
use any of the keys. For more information, see
/tutorial/manage-agent-api-key.

To generate an Agent API key, go to the Agent API Keys
tab. To navigate to the tab, from the Deployment view,
click the Agents tab and then the Agent API
Keys tab.

**Important:**

When you generate an Agent API Key, Ops Manager displays it **one time
only**. You must copy this key. Treat it like a password; store
it in a secure place. Ops Manager never displays the full key again.

Ops Manager configures this setting when you install the MongoDB Agent. If
you need to configure Monitoring separately, include this setting.

```ini
mmsApiKey=rgdte4w7wwbnds9nceuodx9mcte2zqem
```

**`mmsBaseUrl`**

*Type*: string

Specifies the URL (Uniform Resource Locator) of the Ops Manager Application.

```ini
mmsBaseUrl=http://example.com:8080
```

#### HTTP Proxy Settings

**`httpProxy`**

*Type*: string

Specifies the URL (Uniform Resource Locator) of an HTTP (Hypertext Transfer Protocol) proxy server that Monitoring can
use.

```ini
httpProxy=http://proxy.example.com:8080
```

#### MongoDB Kerberos Settings

Specify these settings if Monitoring authenticates to hosts
using Kerberos.

To configure Kerberos, see
/tutorial/configure-mongodb-agent-for-kerberos. The same
procedures and requirements apply, only use a different UPN (User Principal Name) for
Monitoring.

**Note:**

Ops Manager creates a Kerberos Credential (Ticket) Cache for each agent
automatically when Kerberos is enabled. If you want to override the
location of the 
[Kerberos Credential Cache](https://web.mit.edu/kerberos/krb5-latest/doc/basic/ccache_def.html),
you must set the `KRB5CCNAME` environment variable to the desired
file name and path before running the agent.

**`krb5Principal`**

*Type*: string

Specifies the Kerberos principal that Monitoring uses.

```ini
krb5Principal=monitoring/myhost@EXAMPLE.COM
```

**`krb5Keytab`**

*Type*: string

Specifies the *absolute* path to Kerberos principal's `keytab`
file.

```ini
krb5Keytab=/path/to/mms-monitoring.keytab
```

**`krb5ConfigLocation`**

*Type*: string

Specifies the *absolute* path to an non-system-standard location for
the Kerberos configuration file.

```ini
krb5ConfigLocation=/path/to/krb_custom.conf
```

**`gssapiServiceName`**

*Type*: string

Specifies the service name with the `gssapiServiceName`
setting.

*By default, MongoDB uses* `mongodb` *as its service name.*

#### MongoDB TLS Settings

Specify these settings when Monitoring connects to MongoDB
deployments using TLS (Transport Layer Security). 

To learn more, see
/tutorial/configure-mongodb-agent-for-tls.

**`useSslForAllConnections`**

*Type*: boolean

Specifies whether or not to encrypt **all** connections to MongoDB
deployments using TLS (Transport Layer Security).

**Important:**

Setting this to `true` overrides any
per-host TLS (Transport Layer Security) settings configured in the Ops Manager interface.

**`sslClientCertificate`**

*Type*: string

Specifies the *absolute* path to the private key, client
certificate, and optional intermediate certificates in PEM (Privacy-Enhanced Mail)
format. Monitoring uses the client certificate to connect to any
configured MongoDB deployment that uses TLS (Transport Layer Security) and requires client
certificates. (The deployment runs with the
--tlsCAFile setting.)

**Example:**

If you want to connect to a MongoDB deployment that uses both
TLS (Transport Layer Security) and certificate validation using `mongosh`:

```sh
mongosh --tls --tlsCertificateKeyFile /path/to/client.pem --tlsCAFile /path/to/ca.pem example.net:27017
```

You must set these settings in your Custom Settings:

```ini
sslTrustedServerCertificates=/path/to/ca.pem
sslClientCertificate=/path/to/client.pem
```

**`sslClientCertificatePassword`**

*Type*: string

Specifies the password needed to decrypt the private key in
the `sslClientCertificate` file.  Include this setting if you encrypted the client certificate PEM (Privacy-Enhanced Mail) file.

```ini
sslClientCertificatePassword=password
```

**`sslTrustedServerCertificates`**

*Type*: string

Specifies the *absolute* path that contains the trusted Certificate Authority
certificates in PEM (Privacy-Enhanced Mail) format. These certificates verify the server
certificate returned from any MongoDB deployments running with TLS (Transport Layer Security).

```ini
sslTrustedServerCertificates=/path/to/ca.pem
```

**`sslRequireValidServerCertificates`**

*Type*: boolean

Specifies whether Monitoring should validate the TLS (Transport Layer Security) certificates
that the MongoDB databases present.

```ini
sslRequireValidServerCertificates=true
```

By default, Ops Manager sets `sslRequireValidServerCertificates` to
`true`. You need a valid trusted certificate to connect to MongoDB
instances using TLS (Transport Layer Security).

- If MongoDB Agent manages Monitoring, you can't set this option to
  `false`.

- If you configure Monitoring manually, you *can* set
  `sslRequireValidServerCertificates` to `false`.

- If you set `sslRequireValidServerCertificates` to
  `false`, don't set `sslTrustedServerCertificates`. Ops Manager
  won't verify the certificates.

**Warning:**

Changing this setting to `false` disables certificate verification
and makes connections between Monitoring and MongoDB deployments
susceptible to *man-in-the-middle* attacks. Change this setting to
`false` only for testing purposes.

#### Ops Manager Server TLS Settings

Specify the settings Monitoring use when communicating with Ops Manager using
TLS (Transport Layer Security).

**`httpsCAFile`**

*Type*: string

Specifies the *absolute* path that contains the trusted Certificate Authority
certificates in PEM (Privacy-Enhanced Mail) format. Monitoring uses this certificate to
verify that the agent can communicate with the designated Ops Manager
instance.

*By default, Monitoring uses the trusted root* Certificate Authorities
*installed on the host.*

If the agent cannot find the trusted root Certificate Authorities, configure
these settings manually.

If the Ops Manager instance uses a self-signed TLS (Transport Layer Security) certificate, you
*must* specify a `httpsCAFile` value.

```ini
httpsCAFile=/path/to/mms-certs.pem
```

**`sslRequireValidMMSServerCertificates`**

*Type*: boolean

Specifies if Monitoring should validate TLS (Transport Layer Security) certificates from
Ops Manager.

**Warning:**

Changing this setting to `false` disables certificate
verification and makes connections between Monitoring and Ops Manager
susceptible to *man-in-the-middle* attacks. Change this setting
to `false` only for testing purposes.

**`sslServerClientCertificate`**

*Type*: string

Specifies the path to the file containing the client's private key,
certificate, and optional intermediate certificates in PEM (Privacy-Enhanced Mail)
format. Monitoring uses the client certificate when connecting to
Ops Manager over TLS (Transport Layer Security) if Ops Manager requires client certificates, such
as when Ops Manager runs with `Client Certificate Mode` set to
`Required for Agents Only` or `Required for All Requests`.

**See also:**

To learn how to specify this setting in the Ops Manager Application, see
`Client Certificate Mode` in
/reference/configuration.

```ini
sslServerClientCertificate=/path/to/client.pem
```

**`sslServerClientCertificatePassword`**

Specifies the password needed to decrypt the private key in the
`sslServerClientCertificate` file. Include this setting if
you encrypted the client certificate PEM (Privacy-Enhanced Mail) file.

```ini
sslServerClientCertificatePassword=password
```

## Backup Settings

Use the Ops Manager interface to configure Backup settings.

### Log Settings

1. In the navigation, click Deployment.
#. Click the Agents tab.
#. Click Downloads & Settings.
#. In the Agent Log Settings section, click
   `edit` next to Backup Log Settings.
#. Edit the Backup log settings:

   | Setting | Default Value | Console Suggested Value |
   |---|---|---|
   | Linux Log File Path | `/var/log/mongodb-mms-automation/backup-agent.log` |  |
   | Windows Log File Path | `%SystemDrive%\MMSAutomation\log\mongodb-mms-automation\backup-agent.log` |  |
   | Rotate Logs | YES |  |
   | Size Threshold (MB) | 1000 |  |
   | Time Threshold (Hours) | 24 |  |
   | Max Uncompressed Files |  | 5 |
   | Max Percent of Disk |  | 2 |
   | Total Number of Log Files | 0 |  |

#. Click Save.

### Custom Settings

1. In the navigation, click Deployment.
#. Click the Agents tab.
#. Click Downloads & Settings.
#. In the Custom Configuration section, next to
   Edit Custom Configurations, click `edit`.
#. Enter a Backup configuration setting and value.
#. Click Save and Close.

You can configure the following Backup settings:

#### Connection Settings

**`mmsGroupId`**

*Type*: string

Specifies the ID of your Ops Manager project. Find the project ID on the
Project Settings page (Settings >
Project Settings).

```ini
mmsGroupId=8zvbo2s2asigxvmpnkq5yexf
```

**`mmsApiKey`**

*Type*: string

Specifies the MongoDB Agent API (Application Programming Interface) key of your Ops Manager project.

You can use an Agent API key that you have already generated for the
project. Otherwise, you can generate a new Agent API key. A project can
have more than one Agent API key, and any of the project's agents can
use any of the keys. For more information, see
/tutorial/manage-agent-api-key.

To generate an Agent API key, go to the Agent API Keys
tab. To navigate to the tab, from the Deployment view,
click the Agents tab and then the Agent API
Keys tab.

**Important:**

When you generate an Agent API Key, Ops Manager displays it **one time
only**. You must copy this key. Treat it like a password; store
it in a secure place. Ops Manager never displays the full key again.

Ops Manager configures this setting when you install the MongoDB Agent. If
you need to configure Backup separately, include this setting.

```ini
mmsApiKey=rgdte4w7wwbnds9nceuodx9mcte2zqem
```

**`mothership`**

*Type*: string

Specifies the hostname and port of the Ops Manager Application used by the Backup agent.

**Note:**

Don't include the protocol (`http://` or `https://`) in the
`mothership` setting.

```ini
mothership=example.com:8080
```

**`mothershipResponseHeaderTimeout`**

*Type*: integer

Specifies the length of time in seconds Backup waits for the
Ops Manager Application to respond. If the MongoDB Agent doesn't get a
response, it resets and retries the connection to the Ops Manager Application.
This value defaults to `90` seconds.

**`backupSocketTimeoutMs`**

*Type*: integer

Specifies the length of time, in milliseconds, that a socket between
Backup and Ops Manager can remain idle before Ops Manager breaks the
connection. If omitted, defaults to `180000` milliseconds (`3`
minutes). 

**`https`**

*Type*: boolean

Specifies whether or not communication with the Ops Manager web server
uses Secure HTTP (Hypertext Transfer Protocol).

#### HTTP Proxy Settings

**`httpProxy`**

*Type*: string

Specifies the URL (Uniform Resource Locator) of an HTTP (Hypertext Transfer Protocol) proxy that Backup can use.

```ini
httpProxy=http://proxy.example.com:8080
```

#### MongoDB Kerberos Settings

To configure Kerberos, see
/tutorial/configure-mongodb-agent-for-kerberos. The same 
procedures and requirements apply, only use a different UPN (User Principal Name) for
Backup

**Note:**

Ops Manager creates a Kerberos Credential (Ticket) Cache for each agent
automatically when Kerberos is enabled. If you want to override the
location of the 
[Kerberos Credential Cache](https://web.mit.edu/kerberos/krb5-latest/doc/basic/ccache_def.html),
you must set the `KRB5CCNAME` environment variable to the desired
file name and path before running the agent.

**`krb5Principal`**

*Type*: string

Specifies the Kerberos principal that Backup uses.

```ini
krb5Principal=backup/myhost@EXAMPLE.COM
```

**`krb5Keytab`**

*Type*: string

Specifies the *absolute* path to Kerberos principal's keytab file.

```ini
krb5Keytab=/path/to/mms-backup.keytab
```

**`krb5ConfigLocation`**

*Type*: string

Specifies the *absolute* path to an non-system-standard location for
the Kerberos configuration file.

```ini
krb5ConfigLocation=/path/to/krb_custom.conf
```

**`gsapiServiceName`**

*Type*: string

Specifies the service name with the `gsapiServiceName`
setting.

*By default, MongoDB uses* `mongodb` *as its service name.*

#### MongoDB TLS Settings

Specify these settings when Backup connects to MongoDB deployments
using TLS (Transport Layer Security).

To learn more, see
/tutorial/configure-mongodb-agent-for-tls.

**`sslClientCertificate`**

*Type*: string

Specifies the path to the private key, client certificate, and
optional intermediate certificates in PEM (Privacy-Enhanced Mail) format. Backup
uses the client certificate when connecting to a MongoDB deployment
that uses TLS (Transport Layer Security) and requires client certificates. (The deployment
runs with the --tlsCAFile setting.)

**`sslClientCertificatePassword`**

*Type*: string

Specifies the password needed to decrypt the private key in the
`sslClientCertificate` file. Include this setting if you
encrypted the client certificate PEM (Privacy-Enhanced Mail) file.

**`sslTrustedServerCertificates`**

*Type*: string

Specifies the path that contains the trusted CA certificates in
PEM (Privacy-Enhanced Mail) format. These certificates verify the server certificate
returned from any MongoDB deployments running with TLS (Transport Layer Security).

```ini
sslTrustedServerCertificates=/path/to/mongodb-certs.pem
```

**`sslRequireValidServerCertificates`**

*Type*: boolean

Specifies if Backup should validate TLS (Transport Layer Security) certificates
presented by the MongoDB deployments.

**Warning:**

Changing this setting to `false` disables certificate
verification and makes connections between Backup and MongoDB
deployments susceptible to *man-in-the-middle* attacks. Set this
setting to `false` only for testing purposes.

#### Ops Manager Server TLS Settings

Specify the settings Backup use when communicating with Ops Manager using
TLS (Transport Layer Security).

**`sslTrustedMMSBackupServerCertificate`**

Specifies the *absolute* path that contains the trusted Certificate Authority
certificates in PEM (Privacy-Enhanced Mail) format. Backup uses this certificate to
verify that the MongoDB Agent can communicate with the designated
Ops Manager instance.

*By default, Backup uses the trusted root* Certificate Authorities
*installed on the system.*

If Backup cannot find the trusted root Certificate Authorities, configure
these settings manually.

If Ops Manager use a self-signed TLS (Transport Layer Security) certificate, provide a value for
this setting.

```ini
sslTrustedMMSBackupServerCertificate=/path/to/mms-certs.pem
```

**`sslRequireValidMMSBackupServerCertificate`**

Specifies if Backup should validate TLS (Transport Layer Security) certificates from
Ops Manager.

**Warning:**

Changing this setting to `false` disables certificate
verification and makes connections between Backup Agent and Ops Manager
susceptible to *man-in-the-middle* attacks. Change this setting
to `false` only for testing purposes.

```ini
sslRequireValidMMSBackupServerCertificate=true
```

**`sslServerClientCertificate`**

*Type*: string

Specifies the path to the file containing the client's private
key, certificate, and optional intermediate certificates in
PEM (Privacy-Enhanced Mail) format. Backup uses the client certificate when
connecting to Ops Manager over TLS (Transport Layer Security) if Ops Manager requires client
certificates, such as when Ops Manager runs with
`Client Certificate Mode` set to
`Required for Agents Only` or `Required for All Requests`.

**See also:**

To learn how to specify this setting in the Ops Manager Application, see
`Client Certificate Mode` in
/reference/configuration.

```ini
sslServerClientCertificate=/path/to/client.pem
```

**`sslServerClientCertificatePassword`**

*Type*: string

Specifies the password needed to decrypt the private key in the
`sslServerClientCertificate` file. Include this setting
if you encrypted the client certificate PEM (Privacy-Enhanced Mail) file.

```ini
sslServerClientCertificatePassword=password
```
