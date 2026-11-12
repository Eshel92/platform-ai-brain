<!-- Part 5 of 10 of release-notes/application.md (split because the page is big). -->

## Ops Manager Server 4.2

### Ops Manager Server 4.2.26

*Released 2021-07-29*

- Upgrades third-party dependencies and fixes minor bugs.

### Ops Manager Server 4.2.25

*Released 2021-06-03*

- Upgrades JDK (Java Development Kit) to `jdk-11.0.11+9`.
- Disables TLS (Transport Layer Security) versions 1.0 and 1.1.
- Fixes a bug that would re-enable Ops Manager instances for API writes 
  during an upgrade of Ops Manager.
- Caches the computed list of MongoDB binaries available on disk in 
  Local Mode.
- Updates the MongoDB Agent to 10.2.25.6010.

### Ops Manager Server 4.2.24

*Released 2021-05-05*

- Fixes an issue where the MongoDB usage report might find duplicate 
  hosts based on network aliases.

- Updates an outdated comment 
  in the `conf-mms.properties` file that comes with Ops Manager. When 
  you upgrade to this version, you receive a notification that the 
  configuration file changed. For example, on Redhat systems: 
  `/opt/mongodb/mms/conf/conf-mms.properties` saves as 
  `/opt/mongodb/mms/conf/conf-mms.properties.rpmsave`. You can 
  disregard this notification and keep using the existing or current 
  configuration file. No new parameters are added.

- Adds further protections against [CVE-2021-20335](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20335).

- Updates the MongoDB Agent to 10.2.24.6007.

### Ops Manager Server 4.2.23

*Released 2021-01-27*

- Fixes a bug where Ops Manager reported a server error when trying to save
  an invalid configuration on the LDAP Admin configuration page.
- Generates diagnostic archives that contain:

  - Host ping information only for active groups.
  - Backup logs limited by the Backup log settings.

- Fixes a medium severity vulnerability in Ops Manager.
  [CVE-2021-20335](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-20335) is allocated for this issue.

|  |  |
|---|---|
| Title | SSL may be unexpectedly disabled during upgrade of multiple-server MongoDB Ops Manager |
| Description | For MongoDB Ops Manager 4.2.X with multiple OM application servers, that have SSL (Secure Sockets Layer) turned on for their MongoDB processes, the upgrade to MongoDB Ops Manager 4.4.X triggers a bug where Automation thinks SSL (Secure Sockets Layer) is being turned off, and can disable SSL (Secure Sockets Layer) temporarily for members of the cluster. This issue is temporary and eventually corrects itself after MongoDB Ops Manager instances have finished upgrading to MongoDB Ops Manager 4.4. In addition, customers must be running with `clientCertificateMode=OPTIONAL` / `allowConnectionsWithoutCertificates=true` to be impacted. |
| CVSS (Common Vulnerability Scoring System) score | 6.7 [CVSS:3.1/AV:A/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:A/AC:L/PR:L/UI:R/S:U/C:L/I:L/A:N) |
| Affected versions | MongoDB Ops Manager 4.2, 4.2.0 to 4.2.22 |

### Ops Manager Server 4.2.22

*Released 2020-12-03*

- Fixes a bug that prevents Ops Manager from correctly authenticating to an
  HTTP Proxy.

- Updates the MongoDB Agent to 10.2.22.6000.

### Ops Manager Server 4.2.21

*Released 2020-11-05*

- Adds a migration that removes `REPLICATION_OPLOG_WINDOW_RUNNING_OUT`
  events when upgrading to Ops Manager 4.0 or 4.2. If any alerts or alert
  configurations of event type `REPLICATION_OPLOG_WINDOW_RUNNING_OUT`
  exist, global alerts throw the runtime exception "Alert job failed due
  to runtime error: No enum constant".

- Updates the JDK (Java Development Kit) to `jdk-jdk-11.0.9.11.1`.

- Updates the MongoDB Agent to 10.2.21.5995.

### Ops Manager Server 4.2.20

*Released 2020-10-07*

- Adds a new configuration parameter (`http.proxy.nonProxyHosts`)
  which allows the Ops Manager Application Server to bypass the configured
  outgoing proxy when accessing specific hosts.

### Ops Manager Server 4.2.19

*Released 2020-09-25*

- Fixes an issue that prevents rendering the All Clusters
  view for some users in Ops Manager 4.2.18.

- Adds support for Debian 10.

### Ops Manager Server 4.2.18

*Released 2020-09-23*

- Fixes a high severity vulnerability in Ops Manager. `CVE-2020-7927`
  is allocated for this issue.

### Ops Manager Server 4.2.17

*Released 2020-09-13*

- Fixes a bug where editing a blockstore with
  dots or periods (`.`) in its name may result in unexpected errors.
- Fixes an unexpected error when trying to
  update Global API Keys via the API
  results in an invalid request.
- Fixes an unexpected error when trying to
  update a global whitelist IP.
- Sets the day of the week to takes a full snapshot.
  This ensures a recent complete backup.
- Updates MongoDB Agent to 10.2.20.5992.

### Ops Manager Server 4.2.16

*Released 2020-08-06*

- Fixes an error when creating API Keys without roles.

- Updates the diagnostic archive filename to include the current date
  and time of the server when generated or downloaded.

- Updates JDK to AdoptOpenJDK 11.0.8+10.

- Updates MongoDB Agent to 10.2.20.5991.

### Ops Manager Server 4.2.15

*Released 2020-07-02*

- Allows users to audit user creation / modification events through the
  API (Application Programming Interface).

#### Fixes

- Fixes a bug that prevented Ops Manager upgrades when the Application
  Database is a sharded cluster.

- Fixes a bug with converting from LDAP (Lightweight Directory Access Protocol) Native Authentication to
  `saslauthd`.

- Fixes a bug where the Backup dashboard can be
  inaccessible while a snapshot is in progress for a MongoDB 4.2
  deployment.

- Fixes an issue that can prevent a successful snapshot of a MongoDB
  4.2 deployment that contains a large number of files.

#### Agents

Upgrades MongoDB Agent: 10.2.19.5989.

### Ops Manager Server 4.2.14

*Released 2020-06-04*

#### Alerts

- Fixes an issue with the `BACKUP_AGENT_DOWN` alert and MongoDB 4.2+
  deployments.

#### Backup

- Removes enforcement of a minimum oplog window size on a replica set
  before you can enable Backup.

- Fixes an issue with snapshots of MongoDB 4.2+ running on Windows while
  the Ops Manager Application runs on Linux.

- Fixes an issue where a MongoDB 4.2+ queryable restore fails if the
  snapshot contains a large `WiredTiger.wt` file.

- Fixes an issue that caused snapshot generation of the CSRS (Config Servers as Replica Sets) of a
  sharded cluster to stall in certain arrangements of MongoDB Agent\s
  running the Backup module.

- Fixes an issue that prevented editing block stores in the Ops Manager
  Administration Console.

#### Agents

Upgrades MongoDB Agent: 10.2.18.5978.

### Ops Manager Server 4.2.13

*Released 2020-05-14*

#### Backup

- Supports point-in-time restores for
  MongoDB 4.2 deployments.

- Retries rather than fails when a transient network error to the
  KMIP (Key Management Interoperability) server configured for Ops Manager occurs.

- Improves the algorithm for which MongoDB 4.2 replica set and shard
  members use to select for creating snapshots.

- Supports queryable restores for MongoDB 4.2 deployments.

- Supports incremental backup with MongoDB 4.2.6 or later.

#### Fixes

- Fixes bug that prevented creating a new group via the API (Application Programming Interface) when
  SAML (Security Assertion Markup Language) is enabled.

- Fixes a console issue for managed deployments where a shard key's
  fields can be displayed out of order.

- Fixes an issue for managed deployments on Windows with spaces in
  directory paths.

- Fixes an issue that could prevent enabling authentication on a
  managed deployment through the API (Application Programming Interface).

- Fixes an issue that could prevent managed deployments from upgrading
  to a custom MongoDB build.

- Fixes issue in console for managed deployments where the Review and
  Deploy confirmation can mistakenly display that a sharded cluster
  CSRS (Config Servers as Replica Sets) is being removed from the deployment.

- Reduces impact of RTPP on backing MongoDB.

#### Backend

- Updates JDK to AdoptOpenJDK 11.0.8+10.

#### Agents

Upgrades MongoDB Agent: 10.2.17.5970.

### Ops Manager Server 4.2.12

*Released 2020-04-09*

Upgrades Agent: mongodb-10.2.16.5960.

### Ops Manager Server 4.2.11

*Released 2020-04-06*

- Bootstrapping a Backup
  initial sync using
  rsync 
  can now complete when syncing from a hidden secondary.
- Logs are viewable in the Ops Manager Admin panel.
- Ensures initial sync can complete after FCV downgrades.
- Upgrades Agent: mongodb-10.2.15.5958.

### Ops Manager Server 4.2.10

*Released 2020-03-16*

- No longer requires that JavaScript be enabled on the Ops Manager
  Application Database.

### Ops Manager Server 4.2.9

*Released 2020-03-05*

- Fixes an issue which arose when toggling the authentication mechanism
  for a MongoDB user in the Deployment: Security: Users tab
  between `SCRAM-SHA-256` and `SCRAM-SHA-1`.

- Adds the new version (2.13.4) for the
  `MongoDB Business Intelligence Connector`.

- Removes all uses of the MMAPv1 `noPadding` option for Ops Manager
  backing databases. This resolves issues encountered when upgrading
  Ops Manager backing databases from MongoDB version 4.0 to 4.2.

- Shows progress of backup snapshots for MongoDB version 4.2+ on the
  backup dashboard.

### Ops Manager Server 4.2.8

*Released 2020-02-06*

- Allows you to manage the LDAP (Lightweight Directory Access Protocol) and SAML (Security Assertion Markup Language) configuration for the
  `Organization Project Creator` and
  `Project User Admin` roles via the Ops Manager user interface.

- Fixes a bug that prevented the Backup Daemon from correctly working
  on RHEL8 when using a MongoDB 4.2 database.

- Updates JDK to AdoptOpenJDK 11.0.6+10.

- **Upgrades Agent:** mongodb-10.2.13.5943

### Ops Manager Server 4.2.7

*Released 2020-01-09*

- Optimizes snapshots of MongoDB 4.2 and later clusters. This increases
  parallelism when sending bytes to the snapshot store for large files.
- Upgrades Agent: mongodb-10.2.12.5930.

### Ops Manager Server 4.2.6

*Released 2019-12-19*

Upgrades Agent: mongodb-10.2.11.5927.

### Ops Manager Server 4.2.5

*Released 2019-12-12*

- Supports backup of MongoDB 4.2 sharded clusters.

- Ops Manager is now supported on RHEL8 and Debian 10.

- Upgrades Agent: mongodb-10.2.10.5921.

### Ops Manager Server 4.2.4

*Released 2019-11-07*

- Supports the MongoDB Agent on RHEL 8 and CentOS 8.

- Shards of a sharded cluster now appear in alphanumeric order.

- Adds support for managing deployments using
  Externally Sourced Configuration File Values.

- Upgrades JDK to 11.0.5.10.

- Upgrades Agent: mongodb-10.2.9.5909.

### Ops Manager Server 4.2.3

*Released 2019-10-10*

- Removes the **Version Behind** alert if:

  - The alert had been configured for deployments using the legacy
    Monitoring and Backup Agents, and
  - Deployments using that alert were upgraded to using the
    MongoDB Agent.

- Upgrades Agent: mongodb-10.2.8.5901-1.

### Ops Manager Server 4.2.2

*Released 2019-10-03*

- Adds support for
  changing the MongoDB keyfile in a rolling fashion.

- Fixes an issue where the Backup Daemon attempts to automatically
  download MongoDB binaries when running in local mode. This avoids
  many spurious errors in the log files.

- Agent Upgrade: mongodb-10.2.7.5898.

### Ops Manager Server 4.2.1

*Released 2019-09-05*

- Fixes an issue in Ops Manager 4.2.0 that prevented Ops Manager
  versions 4.0.2, 4.0.3, 4.0.4 and 4.0.5 from being upgraded to Ops Manager 4.2.0. This is
  resolved in Ops Manager 4.2.1 such that all Ops Manager 4.0.x
  versions can be upgraded to Ops Manager 4.2.1+.

- Removes need for a persistent cookie to be set on login.

- Agent Upgrade: mongodb-10.2.6.5879-1.

### Ops Manager Server 4.2.0

*Released 2019-08-16*

- Supports management of MongoDB 4.2 deployments.

- Merges Automation, Backup and Monitoring Agents into a single
  MongoDB Agent.

- Replaces Personal API (Application Programming Interface) Keys with
  Programmatic API Keys.
  New users of the API (Application Programming Interface) should use Programmatic API (Application Programming Interface) Keys. Personal
  API (Application Programming Interface) Keys will be deprecated in a future release of Ops Manager.

- Begins support for MongoDB 4.2 with ``"featureCompatibilityVersion" :
  4.2``. Backup of MongoDB 4.2 instances with FCV: 4.2 no longer
  require `head databases` within the Ops Manager
  installation.

  **Note:** Support is incomplete; see release advisories.

- Supports running and managing MongoDB in IPv6 (Internet Protocol version 6)\-only environments.
  For additional details, see the release advisories.

- Allows you to track your usage of MongoDB instances in the Ops Manager
  Admin panel.

- Allows you to upgrade Ops Manager without downtime of Monitoring or
  Alerting. This applies to upgrades from Ops Manager 4.2.0 and later
  versions.

- Containerizes Ops Manager in a Docker Container for use with the
  `MongoDB Enterprise Kubernetes Operator`. This support is
  currently in alpha and not recommended for production use.

- Supports SAML authentication.

- Removes the Version Manager.

- Disables weak TLS (Transport Layer Security) ciphers.

  - `SSL_DHE_DSS_WITH_3DES_EDE_CBC_SHA`
  - `SSL_DHE_DSS_WITH_DES_CBC_SHA`
  - `SSL_DHE_RSA_EXPORT_WITH_DES40_CBC_SHA`
  - `SSL_DHE_RSA_WITH_3DES_EDE_CBC_SHA`
  - `SSL_DHE_RSA_WITH_DES_CBC_SHA`
  - `SSL_RSA_EXPORT_WITH_DES40_CBC_SHA`
  - `SSL_RSA_EXPORT_WITH_RC4_40_MD5`
  - `TLS_DHE_DSS_WITH_AES_128_CBC_SHA256`
  - `TLS_DHE_DSS_WITH_AES_128_CBC_SHA`
  - `TLS_DHE_DSS_WITH_AES_256_CBC_SHA256`
  - `TLS_DHE_DSS_WITH_AES_256_CBC_SHA`
  - `TLS_DHE_RSA_WITH_AES_128_CBC_SHA256`
  - `TLS_DHE_RSA_WITH_AES_128_CBC_SHA`
  - `TLS_DHE_RSA_WITH_AES_128_GCM_SHA256`
  - `TLS_DHE_RSA_WITH_AES_256_CBC_SHA256`
  - `TLS_DHE_RSA_WITH_AES_256_CBC_SHA`
  - `TLS_DHE_RSA_WITH_AES_256_GCM_SHA384`
  - `TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA256`
  - `TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA384`

  **See also:**

  `mms.disableCiphers`

#### Platform Support

- Ops Manager supports the following new platforms:

  - SUSE Linux 15

- Ops Manager no longer supports the following platforms:

  - Debian 8
  - Ubuntu 14.04
  - Windows Server 2008R2

- Ops Manager has deprecated the following platforms. These platforms will
  not be supported in a future Ops Manager release:

  - Windows Server 2012
