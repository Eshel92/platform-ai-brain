<!-- Converted from release-notes/monitoring-agent.txt (reStructuredText). Includes are inlined. -->

# Monitoring Agent Changelog

**Note:** Announcement

The Monitoring and Backup Agent have been merged into the
Automation Agent, which will now be known as the MongoDB Agent.
Learn more about this
change.

----

## Monitoring Agent 6.6.4.472

Released with Ops Manager 4.0.20 on 2020-11-05

## Monitoring Agent 6.6.3.469

Released with Ops Manager 4.0.16 on 2019-11-07

- Adds support for the `businessCategory` field in extended validation
  TLS (Transport Layer Security) certificates.
- The Monitoring Agent is now built using Go 1.13.

## Monitoring Agent 6.6.2.464

Released with Ops Manager 4.0.0 on 2018-06-27

- Added support for MongoDB 4.0.
- Added support for SCRAM-SHA-256.
- Added platform support for:

  - zLinux on RHEL (Red Hat Enterprise Linux) 6
  - Debian 9
  - Amazon Linux 2

----

## Monitoring Agent 6.1.4.442-1

Released with Ops Manager 3.6.7 on 2018-06-06

## Monitoring Agent 6.1.3.436

Released with Ops Manager 3.6.5 on 2018-04-05

- Build system improvements

## Monitoring Agent 6.1.2.402

Released with Ops Manager 3.6.2 on 2018-01-11

## Monitoring Agent 6.1.1.395

Released with Ops Manager 3.6.0 on 2017-12-05

- Support for MongoDB 3.6.

- Support for new Agent API Key model.

----

## Monitoring Agent 5.4.5.415

Released with Ops Manager 3.4.13 on 2018-04-05

- Build system improvements.

## Monitoring Agent 5.4.5.370

Released with Ops Manager 3.4.5 on 2017-05-18

- Tolerate no config.settings document present without printing error
  message.

## Monitoring Agent 5.4.4.366

Released with Ops Manager 3.4.3 on 2017-02-17

- Built with Go 1.7.

- Support for MacOS Sierra.

## Monitoring Agent 5.4.3.361

Released with Ops Manager 3.4.1 on 2016-12-27

- Fix collecting monitoring information for a MongoD in STARTUP2.

## Monitoring Agent 5.4.2.354

Released with Ops Manager 3.4.0 on 2016-11-29

- Added support for monitoring of MongoDB 3.4 deployments.

- Added support for monitoring at higher resolutions, including
  support for gathering of metrics by multiple active Monitoring
  Agents.

- Built using Go 1.6.

- Added ability to run managed Monitoring Agents as a service on 
  Windows.

- Added enhancement to manage appropriate `ulimits` in the package.

- Added enhancement to run `systemd` management on RHEL7 and Ubuntu
  16.04.

----

## Monitoring Agent 3.9.1.326

Released with Ops Manager 2.0.5 on 2016-07-14

- Fixed expired code-signing certificate in MSI. This is a packaging
  change only, the agent version did not change.

## Monitoring Agent 3.9.1.238

Released with Ops Manager 2.0.0 on 2015-12-08

- Added support for MongoDB 3.2.0 config servers as replica sets.

## Monitoring Agent 3.7.1.227

Released with Ops Manager 1.8.2 on 2015-10-20

- Fixed potential memory leak when profiler is enabled.

## Monitoring Agent 3.7.0.212

Released with Ops Manager 1.8.1 on 2015-08-17

- Avoid harmless authentication in `mongod` log files when reading
  `oplog` stats using the `clusterMonitor` role.

## Monitoring Agent 3.3.1.193

Released with Ops Manager 1.8.0 on 2015-06-23

- Added support for x.509 Client Certificate authentication.

- The Kerberos credentials cache now uses a fixed name.

- Improved support for collecting database statistics from secondaries.

- Added an optimization to ensure the Monitoring Agent's database stats
  collection tasks do not synchronize.

## Monitoring Agent 2.9.2.184

*Released 2015-04-28*

- Added an explicit timeout for SSL connections to MongoDB instances.

- Upgraded the MongoDB Go driver (mgo) version, which fixed a rare
  deadlock issue that could occur when monitoring mongos
  instances.

## Monitoring Agent 2.9.1.176

- Added support for non-default Kerberos service names.

- Added support for authentication using MongoDB 2.4 style client
  certificates.

- The Monitoring Agent now identifies itself to the MMS servers using
  the fully qualified domain name (FQDN) of the server on which it is
  running.

- Ops Manager now staggers the timing of DNS look-ups, to avoid triggering a
  rare issue in glibc 2.19 on Ubuntu 14.04.

- Added support for RHEL7.

- Improved error handling on Windows.

- Improved connection management for monitored MongoDB processes.

- Improve correctness of the database statics collection.

- Now uses the `listDatabases` command to retrieve a list of
  databases.

- The default value for `sslTrustedServerCertificates` is now
  `true`. Users upgrading from 2.4.0 and using SSL will need to set
  the value of `sslTrustedServerCertificates` in their
  configuration file. See `sslTrustedServerCertificates` for
  more information.

## Monitoring Agent 2.4.2.113

Released with OnPrem 1.5.0

- Upgraded agent to use Go 1.3.

- Updated mgo driver, which includes fix for MGO-34. All DNS
  lookups should now timeout appropriately.

- Added support for connecting to hosts using LDAP authentication.

- Added support for `version` and `-version` command line options.

- Agent now displays git commit hash of Monitoring Agent in the log 
  file.

- Updates to the configuration file format.

## Monitoring Agent 2.3.1.89-1

Released with OnPrem 1.4.3

- Improved logging for MongoDB 2.6 config servers when connecting with
  a user that has the built-in clusterMonitor role.

- **Fix:** Issue with connecting to replica set members that use auth
  with an updated Go client library.

- Added support for HTTP proxy configuration in the agent
  configuration file.

- Agent includes support for an Offline data collection mode.

## Monitoring Agent 2.1.4.51-1

Released with OnPrem 1.4.2

Prevent high CPU use when monitoring unreachable mongod.

## Monitoring Agent 2.1.3.48-1

Released with OnPrem 1.4.1

Reduction in unnecessary log messages for unsupported operations on
monitored MongoDB 2.2 instances.

## Monitoring Agent 2.1.1.41-1

Released with OnPrem 1.4.0

Ability to monitor hosts using Kerberos authentication.

## Monitoring Agent 1.6.6

Released with OnPrem 1.3.0

- Added kerberos support for agents running on Python 2.4.x.

- Added logging when the `dbstats` command fails.
