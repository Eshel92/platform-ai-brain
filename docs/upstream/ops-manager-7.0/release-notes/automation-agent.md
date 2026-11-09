<!-- Converted from release-notes/automation-agent.txt (reStructuredText). Includes are inlined. -->

# Automation Agent Changelog

**Note:** Announcement

The Monitoring and Backup Agent have been merged into the
Automation Agent, which will now be known as the MongoDB Agent.
Learn more about this
change.

----

## Automation Agent 5.4.24.5565

Released with Ops Manager 4.0.17 on 2020-02-06

- Redacts sensitive configuration data in MongoDB Agent log files to
  improve security.

## Automation Agent 5.4.23.5559

Released with Ops Manager 4.0.16 on 2019-11-07

- Adds support for the `businessCategory` field in extended validation
  TLS (Transport Layer Security) certificates.
- The Automation Agent is now built using Go 1.13.

## Automation Agent 5.4.22.5547

Released with Ops Manager 4.0.15 on 2019-09-05

- Fixes a bug where the MongoDB Agent could panic and delete files from
  its current working directory.

## Automation Agent 5.4.21.5544

Released with Ops Manager 4.0.14 on 2019-07-31

- **Fix:** Restore downloads performed by Automation Agent now respect
  the configured `sslTrustedMMSServerCertificate` Ops Manager
  parameter.

**Note:**

`sslTrustedMMSServerCertificate` has been deprecated. Use 
`httpsCAFile` instead.

## Automation Agent 5.4.20.5541

Released with Ops Manager 4.0.13 on 2019-07-04

## Automation Agent 5.4.19.5537

Released with Ops Manager 4.0.12 on 2019-06-06

- **Fix:** Automation Agent now periodically closes all idle HTTP (Hypertext Transfer Protocol)
  connections.

- **Fix:** Allow Automation Agent to connect to `mongos` through either
  "short" or "long" hostnames.

- **Fix:** Fix failure in the
  make-init-scripts tool.

- **Fix:** Lower the default HTTP (Hypertext Transfer Protocol) Header time out in the Automation
  Agent from 15 minutes to 30 seconds. This ensures faster failures
  in the event of Ops Manager service infrastructure changes, such as
  load balancers moving nodes out of a pool.

- **Fix:** When restoring a sharded cluster, remove all sharding
  metadata from the `config.system.sessions` collection. If you
  do not remove the sharding metadata, MongoDB cannot to re-create this
  collection after the restore is complete.

## Automation Agent 5.4.16.5515

Released with Ops Manager 4.0.8 on 2019-02-07

- **Fix:** Reduce the amount of memory used to generate plans for large
  sharded clusters.

- **Fix:** Rotation of log files when MongoDB log rotation is
  enabled and the maximum number of uncompressed log files is set to
  two.

## Automation Agent 5.4.15.5513

Released with Ops Manager 4.0.7 on 2019-01-10

- Add support for the net.ssl.certificateSelector configuration option.

- **Fix:** Allow the successful change in the storageEngine for
  standalone binary: `mongod` with TLS (Transport Layer Security)/SSL (Secure Sockets Layer) enabled.

- **Fix:** Automation Agent no longer attempts to authenticate to
  arbiters that are configured to use X.509 for `clusterAuthMode`.

## Automation Agent 5.4.14.5509

Released with Ops Manager 4.0.6 on 2018-12-10

## Automation Agent 5.4.13.5505

Released with Ops Manager 4.0.5 on 2018-11-01

- Add support for the `ssl.FIPSMode` parameter.

- **Fix:** Memory leak when using Server Pools feature.

## Automation Agent 5.4.12.5501

Released with Ops Manager 4.0.4 on 2018-10-12

- **Critical Fix:** MongoDB 4.0 restores may fail if snapshot
  downloads for nodes in the replica set finish at significantly
  different times.

- **Fix:** Restore the ability to upgrade from `authSchemaVersion` 3
  to 5 in a sharded cluster.

## Automation Agent 5.4.11.5498

Released with Ops Manager 4.0.3 on 2018-10-04

- **Fix:** Automation Agent can add new MongoDB users even if
  SCRAM-SHA-1 authentication was enabled for the deployment after
  enabling SCRAM-SHA-256.

## Automation Agent 5.4.10.5496

Released with Ops Manager 4.0.2 on 2018-09-06

- Storage affecting field changes in a replica set could result in
  data loss if processes were restarted unexpectedly.

- Automation Agent was unable to properly determine state if
  the process ID previously used by a MongoDB process was reclaimed by
  a different process after an unexpected server reboot.

- **Fix:** Allow CSRS (Config Server Replica Set) members to
  be shut down.

## Automation Agent 5.4.9.5483

Released with Ops Manager 4.0.1 on 2018-08-02

- **Critical Fix:** Set `TasksMax=infinity` and
  `TasksAccounting=false` in `systemd` scripts for
  Automation Agent.

- **Fix:** Automation Agent handling of enterprise builds for
  Amazon Linux 2.

## Automation Agent 5.4.6.5465

Released with Ops Manager 4.0.0 on 2018-06-27

- Added support for MongoDB 4.0.
- Added support for SCRAM-SHA-256
- Added platform support for:

  - zLinux on RHEL (Red Hat Enterprise Linux) 6
  - Debian 9
  - Amazon Linux 2

**Important:**

MongoDB 4.0 Community Edition requires
[libcurl](https://curl.haxx.se/libcurl/). Install `libcurl`
before using Ops Manager to install MongoDB 4.0 Community.

----

## Automation Agent 4.5.17.5289-1

Released with Ops Manager 3.6.10 on 2019-01-10

- **Fix:** Allow CSRS replica set members to be shut down.

## Automation Agent 4.5.16.5284-1

Released with Ops Manager 3.6.9 on 2018-11-01

- **Critical Fix:** Storage affecting field changes in a replica set
  could result in data loss if processes were restarted unexpectedly.

- **Fix:** Memory leak when using Server Pools feature.

## Automation Agent 4.5.15.5281

Released with Ops Manager 3.6.8 on 2018-08-02

- **Critical Fix:** Set `TasksMax=infinity` and 
  `TasksAccounting=false` in `systemd` scripts for
  Automation Agent.

## Automation Agent 4.5.15.5279-1

- Ends support for SLES 11 and Ubuntu 12.04.

- Automation Agent support for BI Connector 2.5.

- Compound Text Indexes through Automation.

- **Fix:** When collecting logs, ignore errors for files that have 
  disappeared.

- Replace evergreen Ubuntu 12 testing with Ubuntu 14.

- Update version of BI Connector tested to 2.5.0.

## Automation Agent 4.5.14.5266

Released with Ops Manager 3.6.6 on 2018-05-03

- **Fix:** Automation Agents should not attempt to rotate BI Connector
  log files for BI Connectors on other servers.

## Automation Agent 4.5.13.5261

Released with Ops Manager 3.6.5 on 2018-04-05

- **Fix:** Disable MongoDB's TTL monitor thread while applying oplogs
  during a point in time restore.

- When performing maintenance on a MongoDB 3.2 shard member for oplog
  resizing, start the node with `--recoverShardingState` false.

- When the Automation Agent performs a resize on a MongoDB 3.2 sharded
  cluster, disable sharding recovery while the node is started up as a
  standalone.

## Automation Agent 4.5.12.2514

Released with Ops Manager 3.6.4 on 2018-03-01

- Changes made to any storage-affecting options in MongoDB will 
  automatically result in a rolling initial sync of the replica set. 

  For single node replica sets and standalones a 
  `mongodump` / 
  `mongorestore`
  will be performed. These options include 
  `security.enableEncryption`, 
  `storage.smallfiles`, `storage.directoryPerDb` and 
  `wiredTiger.directoryForIndexes`. (The `storage.engine` parameter 
  has always had this treatment.)

- **Fix:** Automation Agent correctly resizes the oplog for 
  MongoDB clusters that use X-509 for cluster authentication.

**Note:** RELEASE ADVISORY

Ops Manager 3.6.4 fixes an issue in 
which setting a value for a `setParameter` field using Automation 
may not have resulted in appropriate restart of the MongoDB cluster. 
As a consequence of this fix, clusters in which a `setParameter` 
field is specifically set to the default value for the 
`setParameter` may experience a rolling restart on upgrade to 
Ops Manager 3.6.4.

When configuring a `setParameter` field in the MongoDB 
configuration via Automation, always perform a rolling restart.

## Automation Agent 4.5.11.2453

Released with Ops Manager 3.6.3 on 2018-02-01

- **Fix:** Automation Agent determination of Goal State was incorrect
  for multi-server deployments using the `ldap.bind.queryPassword`
  parameter. This is now resolved and rolling changes will proceed
  correctly on these deployments.

- **Fix:** Rotation of `BI Connector` logs by the Automation 
  Agent for timezones with positive GMT offsets.

## Automation Agent 4.5.10.2429

Released with Ops Manager 3.6.2 on 2018-01-11

- Allow user to specify sampleRefreshIntervalSecs and sampleSize BI
  Connector flags

- **Fix:** Relax validation when `krb5ConfigLocation parameter` is 
  specified. This no longer implies that `krb5Principal` and 
  `krb5Keytab` are required.

- **Fix:** BI Connector Log Rotation config now respects timestamps 
  from UTC (Coordinated Universal Time) hosts.

- **Fix:** Improve logic controlling when the Backup Agent uses the 
  Primary as a sync source.

## Automation Agent 4.5.9.2403

Released with Ops Manager 3.6.1 on 2017-12-19

- **Fix:** Prevent race condition when MongoDB version and FCV are
  updated at the same time.

- Manage Windows Firewall rules for the BI Connector.

## Automation Agent 4.5.7.2375

Released with Ops Manager 3.6.0 on 2017-12-05

- Support for MongoDB 3.6.

- Support for advanced replica set configuration fields.

- Support for new Agent API Key model.

----

## Automation Agent 3.2.18.4938-1

Released with Ops Manager 3.4.14 on 2018-05-03

## Automation Agent 3.2.17.4936

Released with Ops Manager 3.4.13 on 2018-04-05

- **Fix:** Automation Agent determination of Goal State was incorrect
  for multi-server deployments using the ldap.bind.queryPassword
  parameter. This is now resolved and rolling changes will proceed
  correctly on these deployments.

## Automation Agent 3.2.16.2444

Released with Ops Manager 3.4.12 on 2018-02-01

- Logging enhancements

## Automation Agent 3.2.16.2263

Released with Ops Manager 3.4.10 on 2017-11-02

## Automation Agent 3.2.15.2257

Released with Ops Manager 3.4.9 on 2017-10-05

- Fix failure to collect disk-related hardware statistics on some
  hardware configurations.

- When Automation creates a temporary Windows service in order to
  perform maintenance operations on a `mongod`, remove the service
  when the maintenance is completed.

## Automation Agent 3.2.14.2187

Released with Ops Manager 3.4.7 on 2017-08-03

- Optimization to reduce the number of checks to see if a process is
  running.

- Improve state detection during conversions to config server
  replica sets.

## Automation Agent 3.2.13.2141

Released with Ops Manager 3.4.6 on 2017-07-06

- **Fix:** During CSRS conversion, use differently named log files for
  temporary config servers.

- **Fix:** During CSRS conversion, only shut down a member when it is
  in secondary state.

- **Fix:** Config file parsing code on Windows did not parse all
  possible options.

## Automation Agent 3.2.12.2107

Released with Ops Manager 3.4.5 on 2017-05-18

- When performing an automated restore to a sharded cluster with
  different shard names, update the shard identity document.

- When performing an automated restore, ensure that shard metadata
  is always updated in the right order.

- When performing an automated restore, always restore to the default 
  protocol version.

- **Fix:** RHEL7 packaging so that Automation Agent starts on server 
  boot.

- Reduce frequency at which Automation Agent checks managed log files 
  to reduce CPU overhead.

- Ignore get_mempolicy errors and assume numa not enabled.

## Automation Agent 3.2.11.2025

Released with Ops Manager 3.4.4 on 2017-03-30

- Fix problem with shutdown of `mongod` processes during an automated
  restores on Windows.

- Fix for issues using Automation in multi-server deployments using
  SSL and encrypted PEM key files.

- Optimization for goal state maintenance of sharded clusters.
  Automation Agents will execute far fewer commands in steady state.

## Automation Agent 3.2.10.1997

Released with Ops Manager 3.4.3 on 2017-02-17

- Fix bug in removal of shards for sharded clusters on MongoDB 3.4.

- Built with Go 1.7.

- Support for MacOS Sierra.

## Automation Agent 3.2.9.1985

Released with Ops Manager 3.4.2 on 2017-01-19

- **Fix:** Can install Agent on Windows if the Windows Firewall was 
  disabled.

- **Fix:** Can use MONGODB-CR for Agent authentication when LDAP
  was being used for User authentication.

- **Fix:** Issue where Agent would stop sending status after MongoDB
  reaches its connection limit.

## Automation Agent 3.2.8.1942

Released with Ops Manager 3.4.1 on 2016-12-27

- **Fix:** Can install MongoDB on Power Linux when using Ops Manager in
  'Local Mode'.

## Automation Agent 3.2.7.1927

*Released with OpsManager 3.4.0 on 2016-11-29*

- Adds support for automation of MongoDB 3.4 deployments.

- Adds support for management of Monitoring/Backup Agents on
  PowerPC-based Linux systems for MongoDB 3.4 or later deployments
  only.

- Built using Go 1.6.

- Adds support for gathering of hardware metrics.

- When importing a process that uses a password for the PEMKeyFile,
  no longer requires user to re-enter the PEMKeyFile password.

- **Fix:** Can upgrade from MongoDB 2.4 to 2.6 while staying
  on authSchemaVersion 1.

- Does not create Windows firewall rules for processes that are
  started on temporary ports where external access is not required.

- Uses `systemd` management on RHEL7 and Ubuntu 16.04.

----

## Automation Agent 2.5.22.1876

Released with Ops Manager 2.0.7 on 2016-11-03

- MongoDB data and log files will have a `umask` of `027`.
  Requires new package install.

## Automation Agent 2.5.20.1755

Released with Ops Manager 2.0.6 on 2016-08-18

- Improve logging on authentication failures.

- **Fix:** Can set `clusterAuthMode` on sharded clusters.

## Automation Agent 2.5.19.1732

Released with Ops Manager 2.0.5 on 2016-07-14

- Substantial optimization in state-gathering.

- Configurable timeout for connections to MongoDB processes.

- **Fix:** Problem verifying success when creating text indexes in
  rolling index builds.

## Automation Agent 2.5.18.1647

Released with Ops Manager 2.0.4 on 2016-05-20

- Agent no longer downloads restore data for arbiters.

- **Fix:** Some cases where CSRS conversion could get stuck.

- **Fix:** Agent can restart a config server if all config servers are 
  down.

- **Fix:** validating MongoDB versions when a cluster was on
  mixed operating systems.

## Automation Agent 2.5.17.1604

Released with Ops Manager 2.0.3 on 2016-03-24

- **Fix:** Can import of arbiter using a different keyfile then
  existing configuration.

- Allow specifying a temporary port for use during a CRSR upgrade.

## Automation Agent 2.5.16.1552

Released with Ops Manager 2.0.2 on 2016-03-01

- Added support for managing MongoDB on SUSE12.

- Added support for rolling upgrades to config servers as a replica
  set. See /tutorial/convert-config-servers-to-replica-set.

## Automation Agent 2.5.15.1526

Released with Ops Manager 2.0.1 on 2016-01-21

- Stability and performance improvements for restores via automation.

- Added optimization to prioritize replica set reconfiguration
  actions over index builds.

- Improved index building mechanism: index builds are no longer
  performed in a rolling fashion for 2-node replica sets, but
  instead are built in the background.

- Added optimization to not compare unsupported index options when
  determining whether or not an index already exists.

- **Fix:** Can import existing deployments that include
  arbiters running with authentication.

- **Fix:** Rolling storage engine conversion for replica
  sets to ensure a super majority is always up.

- **Fix:** Can create custom roles on sharded clusters running
  MongoDB 3.2 with config server replica sets.

## Automation Agent 2.5.11.1484

Released with Ops Manager 2.0.0 on 2015-12-08

- Added aupport for MongoDB 3.2.0 clusters with config servers as
  replica sets.

- Added aupport for automated restores via the Automation Agent.

- Added aupport for rolling index builds.

- Added aupport for configuring WiredTiger encrypted storage for
  MongoDB 3.2.

- Added aupport for rolling conversion to X-509 member authentication.

- Improved handling of sharded clusters with members running on both
  Linux and Windows-based operating systems.

- Added optimization when starting a new Monitoring or Backup Agent
  to ensure that the process is running before achieving Goal State.

- **Fix:** `glibc` compatibility issue on RHEL5 and RHEL6.

- **Fix:** Automation Agent automatic update failures could cause
  surge in configuration calls from the Automation Agent.

## Automation Agent 2.0.14.1398

Released with Ops Manager 1.8.2 on 2015-10-20

- **Fix:** Agent from not recognizing RHEL Workstations as RHEL.

## Automation Agent 2.0.12.1238

Released with Ops Manager 1.8.1 on 2015-08-17

- **Fix:** Can manage an existing deploy with user that has "root"
  privileges.

- **Fix:** Storage engine conversions do not get stuck if
  replica set contained an arbiter.

- **Fix:** Can update credentials after failed attempt to manage an
  existing deployment.

## Automation Agent 2.0.9.1201

Released with Ops Manager 1.8 on 2015-06-23

- Added support for managing SSL-enabled deployments.

- Added support for managing deployment using Kerberos, LDAP, and
  x.509 Client Certificate authentication.

- Added support to import an existing mongos with a config 
  file.

- Added support for importing an existing deployment that contains
  authenticated arbiters on which the hostname does
  not resolve locally to the loopback interface.

- Added the ability to upgrade the `authSchemaVersion` when auth is
  not enabled.

- Added support to change the storage engine for replica sets with more than one data node.

- Enabled storage engine conversions for single-node replica sets
  and standalones.

- Added more detailed logging of when MongoDB, the Monitoring Agent,
  or the Backup Agent rotate their logs.

- Added support for distribution-specific MongoDB Community Edition 
  builds.

- Added up-front validation to ensure that MongoDB processes are
  running as the same user as the Automation Agent.

- Added functionality to delete MongoDB binaries on disk that are
  not used by a managed process.

- Added optimization where Ops Manager assumes success when starting a forked
  MongoDB process, rather than waiting for EOF.

- Improved algorithm for balancing mongod processes across
  cores.

- When deleting directories, symlinks are no longer deleted.

- **Fix:** Can import credentials for `MONGODB-CR` users from
  `SCRAM-SHA-1` deployments. See: MMS-2612 for more
  details.

- **Fix:** Can derive the default port for config servers
  started with the `--configsvr` option but
  with no port specified. See: MMS-2489.

- **Fix:** Can configure oplog sizes greater than 1TB.

- **Fix:** Automation Agent does not interfere with
  manually-created replica set tags.

- Ensured that the Automation Agent fails gracefully when an expected
  user does not exist during an initial import.

## Automation Agent 1.4.18.1199-1

Released with Ops Manager 1.6.3 on 2015-06-23

- Added support for importing an existing deployment that contains
  authenticated arbiters on which the hostname does
  not resolve locally to the loopback interface.

- **Fix:** Logic used for performing a rolling restart.

- **Fix:** with deriving the default port for config servers started
  with the `--configsvr` option but with no port specified. See
  MMS-2489.

## Automation Agent 1.4.16.1075

*Released 2015-04-28*

- **Fix:** Can update users created on MongoDB 2.4.

- **Fix:** No longer have config server repair occur if the
  third config server was out of sync.

## Automation Agent 1.4.15.999

*Released 2015-03-26*

- **Fix:** a rare edge-case that prevented the Automation Agent from
  successfully enabling authentication.

## Automation Agent 1.4.14.983

*Released 2015-03-02*

Initial release.
