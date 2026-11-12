<!-- Part 9 of 10 of release-notes/application.md (split because the page is big). -->

## Ops Manager Server 2.0

### Ops Manager Server 2.0.10

*Released on 2017-08-03*

- Update JDK to 8u144.

- **Fix:** Backup should compute size of incomplete snapshots.

### Ops Manager Server 2.0.9

*Released on 2017-05-23*

- Agent Upgrades: backup-3.9.1.382-2.0.9

- Upgrade to JDK8u131

### Ops Manager Server 2.0.8

*Released on 2017-01-19*

- Fixed minimum oplog check when starting backup from failing on
  `RECOVERING` members.

- Fixed restores on expired, but not yet deleted, snapshots.

- Upgrade to JDK8u121.

### Ops Manager Server 2.0.7

*Released on 2016-11-03*

- Agent Upgrades: automation-2.5.22.1876

- Improve filesystem backup performance by increasing disk buffer size.

- Fixed backup initial sync failures due to inefficient query on
  oplogs.

- Fixed starting backup when MongoDB was using Kerberos auth and
  Automation was not in use.

- Fixed old application settings appearing as overrides on the Ops
  Manager settings page

- Fixed publish failure due to `weakCertificateValidation` improperly
  being set based on the `allowConnectionsWithoutCertificates` setting.

- Support for Windows Server 2016 and Windows 10.

- Upgrade to JDK8u112. Unlimited strength encryption policy included
  by default.

### Ops Manager Server 2.0.6

*Released on 2016-08-18*

- Agent Upgrades: automation-2.5.20.1755
- Fixed case where acknowledged alerts could be opened again.

- Fixed issue where DNS failures on the hostname(s) of the Ops Manager
  application database cause Ops Manager to shutdown.

- File system snapshot stores can be used in group specific snapshot
  store filters.

- Fixed issue where an unconfigured Backup Daemon could be assigned a
  backup job.

- Upgrade to JDK8u102.

### Ops Manager Server 2.0.5

*Released on 2016-07-14*

- Agent Upgrades: automation-2.5.19.1732,
  monitoring-3.9.1.326

- Fixed credentialstool on Windows, which is used to encrypt passwords
  in the config file.

- Fixed Backup Daemon auto-download of RHEL platform specific builds.

- Added support for LDAP referrals for Ops Manager user authentication.

- Added support for changing LDAP search attribute for Ops Manager user
  authentication.

- Fixed index creation UI in Firefox and IE11.

### Ops Manager Server 2.0.4

*Released on 2016-05-20*

- Agent Upgrades: automation-2.5.18.1647, backup-3.9.1.382

- Fixed failure to generate diagnostics archive due to large amount of
  log data.

- Validate Automation sslMode changes at publish time instead of draft.

- Allow Automation to transition from sslMode disabled to not having a
  sslMode.

- Fixed false positive auth mechanism validation failures when starting
  backup.

- Fixed issue with processing some types of aggregation queries when
  calculating suggested indexes.

- Fixed exception during a backup restore if that data previously was
  on a blockstore that has since been deleted.

- Removed Ubuntu 14.04 enterprise builds for MongoDB 2.4.X that were
  erroneously in the version manifest.

- Ability to edit LDAP Projects for Automation Admin was accidentally
  hidden.

- Fixed javascript error on empty profiler view.

- Upgrade to JDK8u92.

### Ops Manager Server 2.0.3

*Released on 2016-03-24*

- Agent Upgrades: automation-2.5.17.1604

- Fixed critical bug in conversion to config server replica sets.
  Conversions to config server replica sets should be not performed
  with Ops Manager 2.0.2.

- Fixed Ops Manager not recording HTTP access logs.

- Fixed LDAP PEM settings from failing pre-flight checks even when LDAP
  wasn't in use.

- Fixed Automated Point-In-Time restores of Sharded Cluster with config
  server replica sets.

- Fixed removing SSL for a Deployment

- Email configuration changes no longer require a restart of the
  Ops Manager service.

- Allow specifying a temporary port for use during conversion to config
  server replica sets.

- Added Automation support for `net.ssl.disabledProtocols`.

- Allow control over the compression level of the File System Snapshot
  Store.

### Ops Manager Server 2.0.2

*Released on 2016-03-01*

- Agent Upgrades: automation-2.5.16.1552

- Added support rolling upgrades to config servers as a replica set
  (requires MongoDB 3.2.4+).

- Added support for running Agents, the Ops Manager server, and MongoDB
  on SUSE12.

- Added support for Slack and Flowdock notifications as system alerts.

- Fixed Automation Admin Role missing from group LDAP configuration.

- Fixed charting problem on Chrome 48+.

- Fixed issue deleting processes that were part of a config server
  replica set.

- Fixed issue where deployment drafts could prevent Ops Manager from
  starting in local mode.

- Fixed issue where disabling 2FA in Ops Manager still required 2FA for
  users that had it configured.

- Ops Manager upgrades on Windows require an uninstall of the previous
  version. This restriction was added to prevent issues that could
  occur on upgrade that are still unresolved without uninstall.

- Upgrade to JDK8u74.

### Ops Manager Server 2.0.1

*Released 2016-01-21*

- Agent Upgrades: automation-2.5.15.1526.

- Stability and performance improvements for restores via automation.

- Support restores via automation for shared clusters with config
  server replica sets.

- Fixed editing of managed users not promoting to re-enter password
  (Relevant only to imported SCRAM-SHA1 users.)

- Fixed old errors from imports to automation impacting new imports.

- Automation now updates the location of the keyfile according to the
  defined downloadBase.

- Fixed cases where suggested indexes did not handle unexpected
  profiling data.

- Fixed issue with filesystem snapshots failing when trying to resume a
  snapshot after restart.

- Fixed LDAP form validation not allowing "ldaps".

- Fixed the Backup Daemon not recognizing Windows MongoDB Enterprise
  builds.

- Fixed cases where global diagnostic archive would fail if it was too
  large.

- Fixed importing into automation with SSL always requiring client
  certificates.

### Ops Manager Server 2.0.0

*Released 2015-12-08*

#### General

- Added support to monitor, back up, and automate MongoDB 3.2
  deployments.

- Single Ops Manager Package: there is no longer a separate package for
  the Backup Daemon. The single Ops Manager package installs both the
  Ops Manager Application and the Backup Daemon. You can configure any server
  with Ops Manager to handle backups through the Backup Admin interface.

- Configuration in the Database: the Ops Manager application configuration
  is now stored in the application database rather than in configuration
  files. This allows for central configuration management.

  Each Ops Manager instance, on each server, must be configured with
  information on how to connect to the Application Database. Local
  config files override the information in the database: as such,
  switching to configuration in the database is not required, but is
  recommended.

- Backup agent port change: Ops Manager no longer requires a separate port
  for backup traffic. All HTTP traffic is now over a single port. By
  default, Ops Manager uses port `8080`.

- Ops Manager 2.0 updates the admin interface to show the topology of
  Ops Manager software, the application database, and any backup
  databases.

- Added support to convert to LDAP authentication for Ops Manager users at
  any time, with no downtime.

- Upgraded to JDK8u66.

#### Automation

- Added support for X.509 member authentication.

- Improved handling of adding members to replica sets: to avoid
  disrupting majority writes, new members are now added to
  replica sets as `priority=0`, `votes=0`
  until they reach secondary state, after which Ops Manager automatically
  updates the configuration to match the priority and
  votes
  value specified in the deployment.

- Added the ability to manage indexes from the Ops Manager UI.

- Improved index creation: indexes are now created in a rolling
  fashion.

- Added Automation support for Windows MongoDB instances.

#### Monitoring

- Added a new profiler with Suggested Indexes.

- Added support for maintenance windows during which time Ops Manager does
  not send alert notifications.

#### Backup

- Filesystem snapshot storage: added the ability to store snapshots
  on a plain shared file system instead of a MongoDB instance. With
  filesystem storage, Ops Manager stores snapshots in a directory
  hierarchy and the data files themselves are compressed using gzip.

- Backup agent port change: Ops Manager no longer requires a separate port
  for backup traffic. All HTTP traffic is now over a single port. By
  default, Ops Manager uses port `8080`

  Ops Manager will automatically update any Backup Agents managed by
  Automation to use the new port. You will need to manually update any
  Backup Agents set up manually after upgrading Ops Manager. The upgrade
  instructions describe how to configure the `mothership` field in
  the configuration files of non-automated Backup Agents.

- Sync store no longer required: a dedicated sync store is no longer
  required: Backup initial syncs are "streamed"
  to the Backup Daemon and only use a small amount of temporary space
  in the `oplog store`.

- Automated restores: added a new option to automatically restore a
  backup to a running replica set or sharded cluster.

- Added support for namespace whitelisting, which allows you to back up
  only a subset of your data.

- Added the ability to manage HTTP restore link expiration from the
  Ops Manager UI and through the API for each individual restore request.

- Added support for the Backup Daemon to download required MongoDB
  binaries from the Ops Manager web server when they are not available
  locally.

#### Associated Agent Updates

- automation-2.5.11.1484
- monitoring-3.9.1.238
- backup-3.9.0.336

#### Release Advisories for Ops Manager 2.0

Before upgrading to Ops Manager 2.0, ensure the following are true:

Backup Database
  Databases that store the backup-database must be online.

  There are data migrations that touch the various backup data stores 
  that make up the backup-database. Any data stores that are no 
  longer in use should be deleted through the Ops Manager UI before
  upgrading.

Backup Daemon
  The Ops Manager package installs the `Backup Daemon`.
  When started, the Ops Manager package automatically starts two
  services: the Ops Manager Application and the Backup Daemon. You choose on
  which hosts to "activate" the Backup Daemon. The daemon always
  runs, but performs no operations until activated.

  After upgrading to 2.0, a host that runs **only** the Ops Manager Application continues also runs a "dormant" Backup Daemon service. The Backup Daemon remains dormant as long as you do not activate it.

  A host that runs **only** a Backup Daemon runs Ops Manager with an "activated" Backup Daemon and a "dormant" Ops Manager Application. The Ops Manager Application remains dormant as long as you do not direct HTTP traffic to it.

Backup HTTP Service
  Change the `mothership` setting in all Backup Agent
  configuration files for any **manually** installed agents to use port
  `8080`. Any **manually installed** Backup   Agents that are not set
  to use port `8080` cannot connect to Ops Manager You must have access
  to the hosts running any manually installed Backup Agents.

  Beginning with Ops Manager 2.0, there is no Backup HTTP Service on port 
  `8081`. Any Backup Agents that Automation manages are updated to 
  use the new port (`8080`) automatically.

Agent Updates
  The agents have not been updated before the Ops Manager Application has been upgraded. If you use Automation,
  Ops Manager prompts you to update the agents after you upgrade.
  Follow the prompts to update the agents through the Ops Manager Application.
  Do *not* update the agents manually.

conf-mms.properties
  Beginning in 2.0, Ops Manager stores global configuration settings
  in the Ops Manager Application Database and stores only local
  settings in the Ops Manager host's `conf-mms.properties` file.
  The upgrade procedure uses the existing `conf-mms.properties`
  file to connect to the Ops Manager Application Database before replacing
  the existing file with the new, smaller 2.0 file.

Restore properties
  The following properties no longer apply and are replaced by
  settings specified when initiating a restore:

  - `mms.backup.restore.linkExpirationHours`

  - `mms.backup.restore.linkUnlimitedUses`

- If you have modified the `mms.conf` file in your current
  installation, you have backed it up. 

  This is not a regular practice as `mms.conf` contains platform and
  network administration settings for Java VM and Ops Manager network port
  settings. You must use the new `mms.conf` file the upgrade 
  installs. Reapply any modifications from your backed up copy to the 
  new `mms.conf` after completing  the upgrade.

See: /tutorial/upgrade-ops-manager for upgrade instructions
for your operating system.


## Ops Manager Server 1.8

### Ops Manager Server 1.8.3

*Released 2015-12-15*

- Fixed issue where monitoring settings for existing servers were not
  always editable.

- Support for additional Amazon Simple Email Server regions. To specify
  regions other than the default US-EAST, see
  `aws.ses.endpoint`.

- Fixed SNMP notification mechanism for System Alerts.

- Fixed user privileges for MongoDB 3.0 missing from UI on
  Users & Roles page.

- Upgraded to JDK8u66.

### Ops Manager Server 1.8.2

*Released 2015-10-20*

- Agent Updates: automation-2.0.14.1398,
  monitoring-3.7.1.227, and backup-3.4.2.314.

- MONGODB-X509 authentication mechanism no longer requires MongoDB
  Enterprise.

- Fixed system alerts failing to connect to Application Database and
  Backup Databases running with SSL.

- Fixed issue where Backup resync of a Config Server could cause the
  Backup Job to get stuck.

### Ops Manager Server 1.8.1

*Released 2015-08-17*

- Agent Updates: automation-2.0.12.1238,
  monitoring-3.7.0.212

- Updated Backup `seedSecondary` script for MongoDB 3.0.

- Fixed adding users with `GLOBAL` roles to individual groups.

- Fixed Host Down alerts not firing correctly for arbiters.

- Fixed error when trying to enable X.509 authentication for Monitoring
  only (without Automation).

- Fixed error when trying to enable host log collection.

- Fixed case where an acknowledged Alert can be re-opened when Alert
  processing is behind.

- Fixed case where monitoring classified a Config Server as a
  Standalone when there were no mongos services.

### Ops Manager Server 1.8.0

*Released 2015-06-23*

#### Security

- Automation now supports
  SSL and
  MongoDB Enterprise authentication mechanisms:
  Kerberos,
  LDAP, and
  X.509.

  Ops Manager 1.8 can start new MongoDB instances using SSL and enterprise
  authentication mechanisms and import existing instances using SSL and
  enterprise authentication for management.

- Added the ability to specify a proxy server for Ops Manager to use to
  access external services.

- Added support for self-signed CAs and client certificates when using SSL LDAP for Ops Manager user authentication.

#### Alerts

- System Alerts: system alerts allow an
  Ops Manager Administrator to receive alerts when the state of the
  software itself is unhealthy.

- Global Alerts: global alerts
  allow an Ops Manager administrator to monitor any set of Ops Manager groups
  without needing to configure the alerts on a group-by-group basis.

- Added the ability to deliver Project, Global, and System alerts
  via an HTTP webhook.

- Lowered the alerting check frequency from five minutes to one minute,
  allowing for more responsive alerts.

#### Automation

- Automation now uses distribution-specific builds for MongoDB
  Community Edition when one is available for the operating system and
  version in use. Previously, Automation used the generic MongoDB
  Community Edition build.

  Upgrading the Automation Agent and Ops Manager to the new version will
  not automatically change your MongoDB deployments to a distribution-
  specific build: if you wish to use the distribution-specific build,
  you will need to
  update the MongoDB version.

- Added support to change the storage engine for a MongoDB
  deployment using Automation.

- **Beta**: Added Automation support for Windows MongoDB instances.
  This feature must be enabled for an Ops Manager group for it to be
  available.

#### Monitoring

- Standby Monitoring Agents now check in with Ops Manager more frequently.
  You can now configure the Monitoring Agent session timeout to allow
  for faster failover. See: standby-monitoring-agent for
  more information.

#### Backup

- Added the ability to configure the Backup Database's block size.
  The /tutorial/configure-block-size tutorial describes
  how to configure the size of the blocks in the Backup Database's
  blockstore.

- Added the ability to initiate backup SCP restores through the
  Public API. See: /reference/api/restore-jobs.

#### Associated Agent Updates (v1.8)

- automation-2.0.9.1201
- monitoring-3.3.1.193
- backup-3.4.1.283

#### Considerations for Upgrade (v1.8)

- Ops Manager 1.8 requires that the mms-application-database and
  backup-database run MongoDB 2.6 or later.
  Ops Manager will not start after upgrade if your backing databases are
  using an earlier version of MongoDB. The MongoDB Manual provides
  upgrade tutorials with each release.

- When you upgrade to Ops Manager 1.8, Ops Manager disables all Automation
  Agents until they are upgraded to automation-2.0.9.1201. You
  can upgrade the Automation Agents by clicking the link that appears in
  the Please upgrade your agents banner that will appear on
  the Deployment page in the Ops Manager interface.

- Direct upgrade is only allowed from Ops Manager 1.5 and Ops Manager 1.6. To
  upgrade to Ops Manager 1.8 from an earlier version of MongoDB, you must
  first upgrade to Ops Manager 1.6, and then to 1.8.

- In Ops Manager 1.8, `mms.multiFactorAuth.level` replaces the
  deprecated `mms.multiFactorAuth.require` setting.
  `mms.multiFactorAuth.level`
  supports more values than its predecessor.

  Ops Manager will not start with `mms.multiFactorAuth.require`
  in the properties file, but will report an error indicating that the
  setting has been deprecated, and that you must update your
  configuration.

- Ops Manager 1.8 does not include the Backup HTTP Service: its
  functionality is now part of System Alerts
  and Global Alerts.

- System Alerts give new insight into the health of Ops Manager and may
  immediately trigger on upgrade if Ops Manager is not in the expected
  state. For example, if your Application or Backup databases have
  startup warnings or if the connection strings to those databases point
  to any unreachable MongoDB instances, Ops Manager will issue an alert.

- The Ops Manager Deployment user interface has been streamlined such that
  the View Mode and Edit Mode dual views have
  been merged into a unified view.
