<!-- Part 3 of 5 of reference/configuration.md (split because the page is big). -->

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
