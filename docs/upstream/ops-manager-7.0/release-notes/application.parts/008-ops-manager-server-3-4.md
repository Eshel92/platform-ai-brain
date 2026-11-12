<!-- Part 8 of 10 of release-notes/application.md (split because the page is big). -->

## Ops Manager Server 3.4

### Ops Manager Server 3.4.15

*Released on 2018-08-02*

- Updates Ops Manager JDK (Java Development Kit) (x86_64) to 8u181, which enables endpoint
  identification by default.

### Ops Manager Server 3.4.14

*Released on 2018-05-03*

- **Fix:** At the completion of an automated restore of a sharded
  cluster, Ops Manager ensures that the balancer is enabled.

- **Fix:** Network charts now display physical bytes in/out instead of
  logical bytes in/out. That is, if network compression is enabled for
  MongoDB, the network charts shows the compressed bytes in/out.

- Upgrade: Bundled JDK to 8u172.

- Agent Upgrades: automation-3.2.18.4938-1

### Ops Manager Server 3.4.13

*Released on 2018-04-05*

- **Fix:** Avoid failures in alert processing when monitoring topology
  for disk partitions cannot be derived correctly.

- **Fix:** Public API returns correct value for journalingEnabled for
  MongoDB processes using the WiredTiger storage engine.

- Agent Upgrades: automation-3.2.17.4936, monitoring-5.4.5.415, backup-5.0.12.840

### Ops Manager Server 3.4.12

*Released on 2018-02-01*

- Agent Upgrades: automation-3.2.16.2444, backup-5.0.12.725

- The bundled JDK is version 8u162

- Upgrade jackson-databind to 2.9.3

### Ops Manager Server 3.4.11

*Released on 2017-12-20*

- **Fix:** Issue importing a process into Automation running on a
  custom build.

- **Fix:** Explicitly specify the collation `{locale: simple}` in
  createIndex during the initial sync of a backup.

- **Fix:** Allow `clusterAuthMode` to be configured when deployment
  does not use MONGODB-X509 authentication.

- **Fix:** Allow importing a process into Automation using the
  `allowConnectionsWithoutCertificates` parameter.

- Security enhancements.

### Ops Manager Server 3.4.10

*Released on 2017-11-02*

- Agent Upgrades: automation-3.2.16.2263

- **Fix:** `credentialstool` and `encryptiontool`
  load dependencies correctly.

- **Fix:** Backup groom jobs no longer get stuck on
  partially-deleted snapshots.

- **Fix:** Some of the Cloud Manager interface no longer shown
  when creating groups.

- **Fix:** where sorting during deletion of backups could run out of
  memory.

- Reduce memory usage of backup snapshot deletion.

- Remove a restriction where a shard key range could not have an equal
  minimum and maximum.

- Update JDK to 8u152.

### Ops Manager Server 3.4.9

*Released on 2017-10-05*

- Agent Upgrades: automation-3.2.15.2257, backup-5.0.11.663

- **Fix:** Allow the `mongos` `autoSplit` configuration parameter
  to be removed simultaneously with a major version upgrade from
  MongoDB 3.2 to 3.4.

- **Fix:** During the initial sync of a new backup, documents with a
  compound `_id` that are moved on disk at the source during the
  initial sync may be omitted from the backup under rare conditions.
  This issue affects only MMAPv1.

- Increase the expiration period for snapshots downloaded during an
  automated restore and make the expiration periods a configurable
  parameter.

- Reduce the amount of memory used when a backup is terminated.

### Ops Manager Server 3.4.8

*Released on 2017-09-07*

- Allow session timeouts to be configured to a fraction of an hour.

- **Fix:** Downloading the global diagnostic archive could fail if more
  than 32 MB of agent logs were stored.

- **Fix:** Inconsistent Backup Configuration alert runs for config servers.

  **Important:** Special Advisory

  After upgrading to Ops Manager 3.4.8, the Inconsistent
  Backup Configuration alert may be triggered for config servers.
  The backup for these config servers should be resynchonized.

  1. Click Backup.
  #. From the config server row, click on the Option
     menu [ ellipsis-h ].
  #. Click Resync.

  Do not resync the entire sharded cluster if a
  config server triggers this alert. Resync the config
  server in question only.

- **Fix:** Changes to the storage engine for a config server backup are
  applied on resync.

- **Fix:** Validation for Backup Agent authentication mechanism failed
  if `MONGODB-X509` was implicitly enabled.

- **Fix:** In Local Mode,
  checks during Ops Manager startup allow configurations of deleted
  Groups to require MongoDB versions which are not present.

- Security enhancements.

### Ops Manager Server 3.4.7

*Released on 2017-08-03*

- Agent Upgrades: automation-3.2.14.2187,
  backup-5.0.10.634.

- Update JDK to 8u144.

- Additional logging for oplog extensions due to delayed backups.

- Additional logging for backup snapshots that retry due to unexpected
  file changes.

- **Fix:** Ability to restore SCCC sharded clusters without a healthy
  mongos.

- **Fix:** Race condition between snapshots and schedule update
  requests.

- **Fix:** Do not query arbiters when executing an administrative error
  retrieval task.

- Security improvements.

### Ops Manager Server 3.4.6

*Released on 2017-07-06*

- Agent Upgrades: automation-3.2.13.2141,
  backup-5.0.8.601.

- **Fix:** Server Pool servers can get stuck in cleaning state if
  server is reimaged.

- **Fix:** Make Backup ingestion collection stats calls idempotent.

- **Fix:** Avoid skipping storage measurement rollups if customers have
  a database named `hm`.

- **Fix:** Cause Discovery to update shard ID when shard is repurposed
  to arbiter.

- **Fix:** Following upgrade from 2.x to 3.4.x, show progress of
  monitoring data migration.

- **Fix:** Make all metrics available to cluster view.

- **Fix:** Delay in Metric alerts check when opening and closing alerts
  for oplog metrics.

- **Fix:** Metric alerts check may miss system measurements.

### Ops Manager Server 3.4.5

*Released on 2017-05-18*

- Agent Upgrades: automation-3.2.12.2107,
  monitoring-5.4.5.370, backup-5.0.7.494.

- Ability to disable daily/weekly/monthly snapshots through the API.

- Fix validation error for automated restores where the source or
  target cluster uses the `storage.wiredTiger.directoryForIndexes`
  parameter.

- Fix validation errors when using LDAP Authorization along with LDAP
  and SCRAM-SHA1 authentication.

- Various security enhancements.

### Ops Manager Server 3.4.4

*Released on 2017-03-30*

- Agent Upgrades: automation-3.2.11.2025, backup-5.0.6.486

- Fix for premature forceful shutdown of the HEAD mongod
  instances for Ops Manager Backup Daemons running on Windows.

- Fix problem with shutdown of mongod processes during an
  automated restores on Windows.

- Fix for issues using Automation in multi-server deployments using SSL
  and encrypted PEM key files.

- Fix for restores of backup snapshots stored unencrypted using file
  system storage.

- Expose newest AWS regions as a storage option for S3 blockstores.

- Optimization: Performance optimization for sending monitoring data to
  New Relic.

- Security enhancement: Set X-Frame-Options: DENY HTTP headers for all
  authenticated requests.

- Security enhancement: New option to allow enablement of HTTP Strict
  Transport Security (HSTS) with configurable maximum age.

- Security enhancement: New option to allow use of browser session
  cookies, rather than time-limited persistent cookies.

- Security enhancement: New option to disable all browser caching.

### Ops Manager Server 3.4.3

*Released on 2017-02-17*

- Agent Upgrades: automation-3.2.10.1997,
  backup-5.0.6.477, monitoring-5.4.4.366

- Fix resource leak preventing successful backups when Ops Manager
  Backup is running on Windows.

- Fix bug in removal of shards for sharded clusters on MongoDB 3.4.

- Various security enhancements.

- Support for running Automation, Backup and Monitoring Agents on MacOS
  Sierra.

- Support for MongoDB Enterprise builds for Debian 7.1.

- Fix import into Automation for deployments using LDAP authorization
  and SCRAM-SHA1 authentication.

- Automation will deploy SSL-capable Windows builds for MongoDB 3.2.12+
  and 3.4.2+.

- Fix possible stall in the oplog application phase of Ops Manager
  Backups of MongoDB 3.4.

### Ops Manager Server 3.4.2

*Released on 2017-01-19*

- Agent Upgrades: automation-3.2.9.1985, backup-5.0.5.472

- Fixed PageDuty notifications failing to send for System Alerts.

- Fixed issue creating deployments with overlapping replica set / shard
  names of other deployments.

- Fixed Global Alert UI validation being incorrect for some roles.

- Fixed failure configuring MONGODB-CR + LDAP auth mechanisms + LDAP
  authz.

- Added option to disable checksums during restores.

- Upgrade to JDK8u121.

### Ops Manager Server 3.4.1

*Released on 2016-12-27*

- Agent Upgrades: automation-3.2.8.1942,
  monitoring-5.4.3.361, backup-5.0.4.469

- Support for Ops Manager using Active Directory to authenticate to
  application databases.

- Fixed roles info being lost when editting a database user.

- Fixed issue starting backup when 'net.compression' is in use.

- Prevent Ops Manager URLs from having a double forward slash when the
  URL configured by the user ends in a forward slash.

- Fixed editing LDAP group mappings.

- Fixed new OM 3.4.0 being unable to start for the first time without
  internet connectivity

### Ops Manager Server 3.4.0

*Released on 2016-11-29*

#### General

- Added support to monitor, back up, and automate MongoDB 3.4
  deployments.

- Added support for deploying Ops Manager on SUSE12.

- Added support for Automation Agents, Backup Agents and Monitoring
  Agents on Ubuntu 16.x Power (ppc64le) and RHEL 7 Power (ppc64le).

- Added support for mutual TLS/SSL between all Agents and Ops Manager.

- Added the ability to assign tags to Projects and to filter global
  alerts by tags.

- Added the ability to change a the name of a Project.

#### Automation

- Includes more flexible handling of MongoDB User and Roles;
  specifically:

  - Ability to choose whether or not specific users and roles are
    managed, and

  - Ability to choose whether or not to allow MongoDB Users and Roles
    to be managed externally from Ops Manager.

- Added the ability to manage sharded collections and zones.

- Added support for MongoDB 3.4 LDAP Authorization.

- Added support for Kerberos Authentication on Windows.

#### Backup

- Added support for uncompressed WiredTiger snapshots on the
  filesystem.

- Added support for storing snapshots in S3.

- Added support for WiredTiger encryption at rest.

- Added the ability to control the reference time for the snapshot
  schedule; e.g., specify that snapshots are taken every 6 hours,
  starting at 12:00:00 AM.

- Added support for all data-format affecting MongoDB configuration
  options: directoryPerDB, smallfiles, etc.

#### Monitoring

- Provides high resolution monitoring: metrics are now captured every
  10 seconds.

- Supports flexible retention monitoring: metrics at each resolution
  can be retained for a configurable amount of time.

- Allows hardware metrics to be collected for any managed MongoDB
  process (i.e. any process that is managed by an Automation Agent).

- Provides new API endpoint to retrieve all metrics for a particular
  MongoDB process in one API call.

#### Provisioning

- Added support for maintaining a pool of provisioned servers from
  which users in a group can request servers to host new MongoDB
  deployments.

#### Associated Agent Updates (v3.4)

- automation-3.2.7.1927
- monitoring-5.4.2.354
- backup-5.0.3.465

#### Release Advisories for Ops Manager 3.4

Before upgrading Ops Manager from 2.0.x to 3.4, complete the following 
actions:

- Upgrade backing databases to at least MongoDB 3.0.8.
  MongoDB 2.6 is no longer allowed as a backing store.

- Ensure the data partitions for the Ops Manager Application Database have at 
  least 50% free disk space.

  Once the Ops Manager upgrade to 3.4 completes, Ops Manager begins 
  migrating of all monitoring data to a new schema in the background. 
  This migration requires significant free disk space.

- Add necessary IP addresses or CIDR (Classless Inter-Domain Routing) blocks for to the access lists
  for any API clients connecting to the Automation configuration 
  endpoints.

- Back up the `mms.conf` file in your current installation if you 
  have modified it.

  This is not a regular practice as `mms.conf` contains platform and
  network administration settings for Java VM and Ops Manager network port
  settings. You must use the new `mms.conf` file the upgrade 
  installs. Reapply any modifications from your backed up copy to the 
  new `mms.conf` after completing  the upgrade.

For procedures to upgrade to 3.4, see
/tutorial/upgrade-ops-manager.
