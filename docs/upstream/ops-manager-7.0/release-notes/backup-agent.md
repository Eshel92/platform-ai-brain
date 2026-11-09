<!-- Converted from release-notes/backup-agent.txt (reStructuredText). Includes are inlined. -->

# Backup Agent Changelog

**Note:** Announcement

The Backup and Monitoring Agent have been merged into the
Automation Agent, which will now be known as the MongoDB Agent.
Learn more about this
change.

----

## Backup Agent 6.8.9.1030

Released with Ops Manager 4.0.20 on 2020-11-05

## Backup Agent 6.8.8.1027

Released with Ops Manager 4.0.16 on 2019-11-07

- Adds support for the `businessCategory` field in extended validation
  TLS (Transport Layer Security) certificates.
- The Backup Agent is now built using Go 1.13.

## Backup Agent 6.8.7.1024

Released with Ops Manager 4.0.13 on 2019-07-04

- **Fix:** Improve the ability of the Backup Agent to stop the
  balancer when preparing to take a snapshot for a sharded cluster.
- **Fix:** Set a TLS (Transport Layer Security) timeout for connections between the Backup Agent
  and Ops Manager services.

## Backup Agent 6.8.6.1013

Released with Ops Manager 4.0.7 on 2019-01-10

- **Fix:** Improve Backup Agent handling when stopping the balancer in
  preparation for marking a point in time to take a snapshot for a
  sharded cluster. Prior handling could result in the balancer being
  left in a stopped state for MongoDB 3.4+. This has been resolved.

## Backup Agent 6.8.4.1009

Released with Ops Manager 4.0.1 on 2018-08-02

## Backup Agent 6.8.3.1002

Released with Ops Manager 4.0.0 on 2018-06-27

- Added support for MongoDB 4.0.
- Added support for SCRAM-SHA-256
- Added platform support for:

  - zLinux on RHEL (Red Hat Enterprise Linux) 6
  - Debian 9
  - Amazon Linux 2

----

## Backup Agent 6.0.10.976

Released with Ops Manager 3.6.8 on 2018-08-02

## Backup Agent 6.0.10.972-1

Released with Ops Manager 3.6.7 on 2018-06-06

- Improved recovery after transient backup failures.

- Improve retry behavior for aborted network operations during PIT 
  restores.

- **Fix:** Automated PIT restore fails when target does not accept 
  SSL (Secure Sockets Layer).

- **Fix:** Disable session cache refresh during standalone phase of a 
  restore.

- **Fix:** Queryable Restore Daemon file descriptor leak when using a 
  FileSystem Snapshot Store.

## Backup Agent 6.0.9.969

Released with Ops Manager 3.6.6 on 2018-05-03

- Provide option for Backup Agent to use persistent HTTPS connections.

## Backup Agent 6.0.8.960

Released with Ops Manager 3.6.5 on 2018-04-05

- Build system improvements

## Backup Agent 6.0.8.752

Released with Ops Manager 3.6.4

- **Fix:** Backup Agent should produce an error message and not crash 
  when erroneous authentication credentials are provided for a source 
  cluster.

## Backup Agent 6.0.6.724

Released with Ops Manager 3.6.3

- **Fix:** For MongoDB 3.6 deployments, the initial sync of a backup 
  could fail creating an index on a collection with a collation 
  specified.

## Backup Agent 6.0.5.716

Released with Ops Manager 3.6.2 on 2018-01-11

## Backup Agent 6.0.3.689

Released with Ops Manager 3.6.0 on 2017-12-05

- Support for MongoDB 3.6.

- Performance optimizations.

- Support for new Agent API Key model.

----

## Backup Agent 5.0.12.840

Released with Ops Manager 3.4.13 on 2018-04-05

- Build system improvements.

## Backup Agent 5.0.12.725

Released with Ops Manager 3.4.12 on 2018-02-01

- **Fix:** For MongoDB 3.6 deployments, the initial sync of a backup 
  could fail creating an index on a collection with a collation 
  specified.

## Backup Agent 5.0.11.663

Released with Ops Manager 3.4.9 on 2017-10-05

## Backup Agent 5.0.10.634

Released with Ops Manager 3.4.7 on 2017-08-03

- Improve state management when executing an administrative error
  retrieval task.

## Backup Agent 5.0.8.601

Released with Ops Manager 3.4.6 on 2017-07-06

- Performance enhancement: Use bson.Raw for initial sync.

## Backup Agent 5.0.7.494

Released with Ops Manager 3.4.5 on 2017-05-18

- **Fix:** High Memory Usage during Initial Sync with Large Numbers of
  Small Documents.

## Backup Agent 5.0.6.486

Released with Ops Manager 3.4.4 on 2017-03-30

- Performance optimization for initial data collection in the initial
  sync phase.

## Backup Agent 5.0.6.477

Released with Ops Manager 3.4.3 on 2017-02-17

- Built with Go 1.7.

- Support for MacOS Sierra.

## Backup Agent 5.0.5.472

Released with Ops Manager 3.4.2 on 2017-01-19

- Fixed Backup Agent logs not getting sent to server on Windows.

## Backup Agent 5.0.4.469

Released with Ops Manager 3.4.1 on 2016-12-27

- Fix initial sync failures in MongoDB 3.4.0 and later.

- Fix crash causes by initial sync of a large capped collection.

- Added support for MongoDB 3.4 feature compatibility version and
  views.

## Backup Agent 5.0.3.465

Released with Ops Manager 3.4.0 on 2016-11-29

- Added support for uncompressed WiredTiger snapshots on the
  filesystem.

- Added support for storing snapshots in S3.

- Added support for WiredTiger encryption at rest.

- Added ability to control the reference time for the snapshot
  schedule. 

  **Example:**

  Can now specify that snapshots are taken every
  6 hours, starting at 12:00:00 AM.

- Added support for all data-format affecting MongoDB configuration
  options: `directoryPerDB`, `smallfiles`, etc.

----

## Backup Agent 3.9.1.382

Released with Ops Manager 2.0.9 on 2017-05-23

- **Fix:** Add a flush method to DigestOutputStream to avoid timeouts.

- **Fix:** Some `deleteIndex` oplog entries not supported during 
  initial sync.

- **Fix:** FileSystemStorejobRunner thread gets killed if exception is
  thrown while getting the Job.

- **Fix:** Failure to create collection if the mongod being backed up
  is configured with encryption.

## Backup Agent 3.9.1.382

Released with Ops Manager 2.0.4 on 2016-05-20

- **Fix:** If a collection was deleted during an initial sync, no 
  crash results.

## Backup Agent 3.9.0.336

Released with Ops Manager 2.0.0 on 2015-12-08

- Added support for streaming initial syncs.

- Added support for MongoDB 3.2.0 config servers as replica sets.

- Added the ability to only backup selected namespaces (whitelist).

- Fixed issue with initial sync failing due to collections being
  deleted during the sync.

- Fixed issue with collection names with trailing spaces.

## Backup Agent 3.4.2.314

Released with Ops Manager 1.8.2 on 2015-10-20

- **Fix:** Initial syncs do not fail if a namespace was deleted
  during the sync.

## Backup Agent 3.4.1.283

Released with Ops Manager 1.8 on 2015-06-23

- Added support for x.509 Client Certificate authentication.

- The Kerberos credentials cache now uses a fixed name.

- **Fix:** Race condition which could result in inconsistent cluster
  snapshots for MongoDB 3.0+ sharded clusters using the
  `backup` role.

## Backup Agent 3.1.2.274

*Released 2015-04-28*

- Added an explicit timeout for SSL connections to MongoDB instances.

- Added an optimization for syncs of collections with lots of small 
  documents.

## Backup Agent 3.1.1.263

*Released 2015-03-02*

- Adds support for non-default Kerberos service names.

- Adds support for authentication using MongoDB 2.4-style client 
  certificates.

- The Backup Agent now identifies itself to the Ops Manager servers using the
  fully qualified domain name (FQDN) of the server on which it is 
  running.

- The Backup Agent now captures a checkpoint even if it is unable to 
  stop the balancer. These checkpoints are not guaranteed to be 
  consistent, because of in-progress chunk migrations. The user 
  interface identifies these checkpoints.

## Backup Agent 2.3.3.209-1

Released with OnPrem 1.5.2

Use no-timeout cursors to work around MGO-53.

## Backup Agent 2.3.1.160

*Released with Ops Manager OnPrem 1.5.0*

- Backup Agent now sends oplog slices in batches.

- Improved stability around oplog tokens for environments with
  unstable networks.

- Support for a new API that allows Ops Manager to ingest oplog entries 
  before the entire payload has reached the Ops Manager servers.

- Upgraded agent to use to Go 1.3.

- Added support for `version` and `-version` command line options.

- Added support for connecting to hosts using LDAP authentication.

- Agent now provides additional logging information when the Backup
  Agent manipulates the balancer.

- Agent now supports configuring HTTP proxies with the config file.

## Backup Agent 1.5.1.83-1

Released with OnPrem 1.4.2

- Critical update for users running the MongoDB 2.6 series that use
  authorization.

- Backup Agent now includes `system.version` and 
  `system.role` collections from the admin database in the
  initial sync.

## Backup Agent 1.5.0.57-1

Released with OnPrem 1.4.1

Support for backing up Kerberos-authenticated replica sets and clusters

## Backup Agent 1.4.6.42-1

Released with OnPrem 1.4.0

- Major stability update.

- Prevent a file descriptor leak.

- Correct handling of timeouts for connections hung in the SSL
  handshaking phase.
