<!-- Part 10 of 10 of release-notes/application.md (split because the page is big). -->

## Ops Manager Server 1.6

### Ops Manager Server 1.6.4

*Released 2015-08-17*

- Ops Manager no longer shuts down if the mms-application-database
  is unreachable. (This issue was erroneously reported as resolved in
  Ops Manager 1.6.3.)

### Ops Manager Server 1.6.3

*Released 2015-06-23*

- Agent updates: automation-1.4.18.1199-1

- Added full support for restores of WiredTiger backups. Previously,
  Ops Manager only supported
  SCP Individual File restores
  for WiredTiger backups.

- Added optimization to prevent some Backup Daemon background tasks
  from doing excessive logging when databases are down.

- Fixed a user interface issue when displaying an empty Automation
  diff.

### Ops Manager Server 1.6.2

*Released 2015-04-28*

- Fixed issue with grooms on a WiredTiger backup blockstore.

- Fixed a possible connection leak with the SCP Individual File restore
  type.

- LDAP users are now periodically synced with the LDAP server to
  prevent communications after a user is removed from a group.

- Fixed an issue with backups of MongoDB 3.0 mongod
  instances running with the `--setParameter failIndexKeyTooLong=0`
  option.

### Ops Manager Server 1.6.1

*Released 2015-03-26*

- Agent updates: Automation Agent 1.4.15.999.

- **Security Update**: resolved an issue where users removed from LDAP
  groups were not always removed from corresponding Ops Manager
  groups. This upgrade is **highly recommended** for anyone using LDAP
  authentication.

- Selecting wildcards in the Version Manager is no longer supported
  when `automation.versions.source` is set to `local`.

- Added a 1 hour timeout to kill a Backup `head database` if
  it does not shutdown cleanly.
  You must perform a resync following a hard kill.

- Windows support for Backup Daemon using Windows 64-bit 2008 R2+
  MongoDB builds.

- Fix for Backups stored in
  WiredTiger
  format in which a single collection grows from under 8 GB to over
  8 GB in size.

- The time before an unreachable mongos process is
  deactivated is now configurable on a per group basis. See
  admin-only-group-settings.

- The time before a standby Monitoring Agent takes over after the
  primary Monitoring Agent stops responding is now configurable to a
  minimum of 90 seconds. See the
  `mms.monitoring.agent.session.timeoutMillis` setting in
  /reference/configuration.

- For Backup HTTP pull restore, the link expiration and the number of
  allowed uses of a link are now configurable.

### Ops Manager Server 1.6.0

*Released 2015-03-02*

#### New Features

- Initial release of Automation. Automation manages
  many basic administrative tasks for MongoDB deployments, including
  version upgrades, adding replica set members, adding shards, and
  changing oplog size. You can both
  import existing deployments into Automation
  and create new deployments
  on your provisioned hardware.

- Windows support (Monitoring and Backup only). You can
  /tutorial/nav/install-application on Microsoft Windows using 
  MSI files. Ops Manager supports Windows Server 2008 R2 and above.

- Support for MongoDB 3.0, including support for backups that use the
  WiredTiger storage
  engine.

  To monitor or back up MongoDB 3.0 deployments, you must install
  Ops Manager 1.6 or higher. To monitor a MongoDB 3.0 deployment, you must
  also run Monitoring Agent version 2.7.0 or higher.

- Support for using the SSL and MONGODB-X509 authentication mechanisms
  for the backing MongoDB databases. See
  /tutorial/configure-ssl-connection-to-backing-mongodb.

- Public API endpoints to manage Automation configuration. For more
  information, see Automation in the API
  documentation.

#### Improvements

- The Ops Manager's Administration
  interface provides more information to make it easier to monitor the
  health of the Ops Manager installation.

- The Ops Manager Deployment tab now displays all deployment information
  on one page, with icons for selecting view options. The new Topology
  View groups all hosts by the replica set or sharded cluster they are
  part of. The new Servers View shows information about MongoDB
  processes and Ops Manager agents grouped by server.

- Fixed an issue
  ([MMS-2273](https://jira.mongodb.org/browse/MMS-2273))
  where, in certain situations, the Backup Agent was not reporting a
  cluster snapshot as potentially inconsistent.

- Improved handling of cursor timeouts by the Backup Agent. To use this
  improvement, upgrade to the latest Backup Agent, which is included
  with Ops Manager. The improvement became available with
  Backup Agent 2.3.3.209-1.

#### Considerations for Upgrade to 1.6

- Ops Manager 1.8.0, when released, **will not** support MongoDB 2.4 for
  the mms-application-database and backup-database.
  Ops Manager Server 1.8.0 *will* continue to support MongoDB 2.4 for your
  monitored and backed-up databases.

- Ops Manager 1.6.0 supports direct upgrades only from MMS On Prem 1.3 and
  above.

- The procedure to configure Ops Manager to run with HTTPS has changed and
  is greatly simplified. The previous procedure no longer works. For
  the new procedure, see /tutorial/configure-ssl-connection-to-web-interface.

- The connection string to the backup blockstore database is now
  configured through the Administration interface's
  Blockstores page and not through the
  `mongo.backupdb.mongoUri` field in the `conf-daemon.properties`
  configuration file.

- Ops Manager no longer requires you to supply the replica set name of the
  backing MongoDB instances. The `mongo.replicaSet` and
  `mongo.backupdb.replicaSet` properties have been removed from the
  configuration files. These properties had previously controlled
  whether Ops Manager treated a connection to a backing instance as a
  standalone or replica set, for the purpose of setting the write
  concern. Ops Manager now sets write concern based on how many hosts are
  supplied in the connection string.

- You can disable Automation for the entire Ops Manager installation
  through the `mms.featureFlag.automation` setting in the
  `conf-daemon.properties` configuration file.

- Removed the Dashboards view from the Ops Manager UI. You can
  view monitoring metrics from the Deployment tab.
  See: /tutorial/view-diagnostics for an overview
  of the available metrics and how to access them.


## MMS Onprem Server 1.5

### MMS Onprem Server 1.5.5

*Released 2015-03-26*

- **Security Update**: resolved issue where users removed from LDAP
  groups were not always removed from corresponding Ops Manager groups.
  This upgrade is **highly recommended** for anyone using LDAP
  authentication.

### MMS Onprem Server 1.5.4

*Released 2015-03-18*

- Fixed race condition that could cause the Backup Daemon to hang when
  the MongoDB process for a `head database` fails to start.

- Fixed an issue where a rollback occurring shortly after a terminate
  could step on the terminate.

- The time before an unreachable mongos process is
  deactivated is now configurable on a per group basis. See
  admin-only-group-settings.

- The time before a standby Monitoring Agent takes over after the
  primary Monitoring Agent stops responding is now configurable to a
  minimum of 90 seconds. See the
  `mms.monitoring.agent.session.timeoutMillis` setting in
  /reference/configuration.

- For Backup HTTP pull restore, the link expiration and the number of
  allowed uses of a link are now configurable.

### MMS OnPrem Server 1.5.3

*Released 2014-12-17*

Significant improvements in performance for the processing of MMS OnPrem
Monitoring data for MMS OnPrem Projects with a large number of hosts

### MMS OnPrem Server 1.5.2

*Released 2014-11-18*

- Added Support for archive restores (`.tar.gz`) for databases whose
  filenames exceed 100 characters.

- API: Skip missed points in metrics data, instead of returning empty
  data.

- API: Return correct number of data points when querying metric data
  with the period option.

- Backup Agent update to `2.3.3.209-1`

### MMS OnPrem Server 1.5.1

*Released 2014-09-26*

- Fix cases where replica set member alerts (e.g. no primary, number
  of healthy members) could send false positives.

- Skip `backup-daemon` `rootDirectory` and
  `mongo.backupdb.mongoUri` overlap check when the
  `mongo.backupdb.mongoUri` is on a different
  host.

- `mms-gen-key` script handles user's effective group being
  different than the username.

- Security enhancements.

### MMS OnPrem Server 1.5.0

*Released 2014-09-02*

#### Considerations for Upgrade

- MMS OnPrem *only* supports direct upgrades from 1.3 and 1.4.

- Change in configurations and policy for 2FA:  Two-factor
  authentication must now be explicitly enabled using the
  `mms.multiFactorAuth.require` setting.

- The default LDAP group separator became `;;`. Previously the
  separator was `,`. See the LDAP configuration documentation for more information.

- Suppressed hosts will only remain suppressed for 30 minutes.

  Previously, if after deleting a host, from MMS OnPrem Monitoring the
  hostname and port combination would be added to a suppression list
  with an infinite lifetime. The suppression list prevented a race
  condition where host in a cluster would be auto-discovered by another
  member of a deployment before the host could was fully removed. Now,
  hostname and port combinations remain on the suppression list for
  only 30 minutes.

- Set the `mms.remoteIp.header` in the
  `conf-mms.properties` file  if clients access the MMS OnPrem
  Application via a load balancer.

- `mongo.backupdb.mongoUri` is no longer in
  `conf-mms.properties`. This was previously a required field in this
  file. It remains in the backup daemons's `conf-daemon.properties`.

- Stored MongoDB profile data is not transferred between OnPrem 1.4
  and OnPrem 1.5 during the upgrade process.

#### Improvements

- When an MMS OnPrem Backup job fails to bind, the system periodically
  and automatically retries.

- All MMS OnPrem Backup jobs will retry indefinitely.

- Point in Time restores are now available with one second granularity.

#### New Features

- MMS OnPrem Public API.

- Explicit support for multiple MMS OnPrem backup blockstore databases
  and the ability to pin MMS OnPrem Projects to specific backup daemons
  and databases. See
  /tutorial/assign-snapshot-stores-to-data-center.

- MMS OnPrem can authenticate using LDAP to both the database backing
  MMS OnPrem and the monitored and backed up MongoDB deployments.
  See security-ldap.

- Enhanced auditing. See /reference/audit-events for more
  information.

- Ability to acknowledge alerts with comments.

- New cluster page that shows individual, sum or average metrics for
  all shards in a cluster.


## MMS OnPrem Server 1.4

### MMS OnPrem Server 1.4.3

*Released 2014-07-22*

- Addressed issues related to Backup Job assignment for 2.6.x clusters
  that used the `clusterMonitor` role to support MMS OnPrem
  Monitoring.

- Fixed problem importing email addresses for users for deployments
  that use LDAP integration.

- Fixed rare race condition caused high CPU usage in the MMS OnPrem
  HTTP Service if the application cannot connect to one of the backing
  databases.

- Additional security enhancements.

### MMS OnPrem Server 1.4.2

*Released 2014-05-29*

- Critical bug fix for backing up MongoDB 2.6 deployments that include
  user or custom role definitions:

  - The `system.version` collection in the admin database will
    be included in all future snapshots.

  - The `system.roles` collection in the admin database will be
    included after a new initial sync is performed.

  Users capturing backups of MongoDB 2.6 replica sets or clusters with
  MMS OnPrem that include custom role definitions should perform a new
  initial sync. Taking a new initial sync will ensure that the role
  definitions are included in the backup.

- Disable MongoDB `usePowerOf2Sizes` for insert-only MMS
  OnPrem Backup collections.

- Speed optimization for MMS OnPrem Backup HTTP pull restores.

- Fix for LDAP integration, MMS OnPrem now passes full `dn` correctly
  when authenticating the user.

### MMS OnPrem Server 1.4.1

*Released 2014-04-28*

- Ability to Backup replica sets or clusters using Kerberos
  authentication.

- Ability to Backup replica sets or clusters running specific custom
  MongoDB builds provided by MongoDB, Inc.

- Fix validation issue preventing Backup of MongoDB 2.6.0 clusters.

- Reduced log noise from Monitoring Agent when monitoring MongoDB 2.0
  or unreachable `mongod`\s.

### MMS OnPrem Server 1.4.0

*Released 2014-04-08*

- Includes MMS OnPrem Backup: continuous backup with point-in-time
  recovery of replica sets and cluster-wide snapshots of sharded
  clusters.

- Finer-grained roles and permissions.

- Improved user interface for alerts.

- Enhanced Activity Feed for auditing of all activity.

- Monitoring Agent distributed as OS-specific binary. Python dependency
  removed.

- LDAP integration for managing users and groups.

MMS OnPrem 1.4.0 requires MongoDB 2.4.9+ instances for backing
storage.


## MMS OnPrem Server 1.3

*Released 2013-12-01*

- Packaging/support for Debian and SUSE Linux.

- Kerberos authentication support between MMS OnPrem server and backing
  MongoDBs, as well as between Monitoring Agent and the MongoDBs it
  monitors.

- OnPrem users can be overall site administrators. (MMS OnPrem Admins)

- New admin section where MMS OnPrem Admins can manage user roles and
  message banners.

- Tunable advanced password and session management configurations.

- Encryption key rotation, more specific CORS policy, auth tokens
  removed from chart URLs, and other security enhancements.


## MMS OnPrem Server 1.2

*Released 2013-07-24*

- Redesigned user interface and enhanced algorithm to auto-discover
  hosts and derive host topology.

- SNMP monitoring.

- Ability to export charts.

- Option to store encrypted authentication credentials in the `mmsDb`
  property in the configuration file.

- Ability to classify users within an MMS OnPrem Project as group
  administrators or read-only users.
