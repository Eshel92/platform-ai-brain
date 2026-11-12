<!-- Part 4 of 10 of release-notes/application.md (split because the page is big). -->

## Ops Manager Server 4.4

### Ops Manager Server 4.4.24

*Released 2022-07-29*

- Updates the JDK (Java Development Kit) to `jdk-11.0.16+8`.
- Updates the MongoDB Agent to 10.14.35.6589.

### Ops Manager Server 4.4.23

*Released 2022-07-07*

- Fixes an issue where editing an Oplog Store's name that contains dots 
  (`.`) might have resulted in errors.
- Updates the MongoDB Agent to 10.14.34.6588.

### Ops Manager Server 4.4.22

*Released 2022-05-05*

- Adds support for Debian 10 when you use the `BI Connector`.
- Fixes an issue that occurred when you changed the default server
  usage for organizations.
- Updates the MongoDB Agent to 10.14.33.6581.
- Updates the JDK (Java Development Kit) to `jdk-11.0.15+10`.
- Upgrades the `com.google.protobuf:protobuf-java` package to 3.19.4.

### Ops Manager Server 4.4.21

*Released 2022-02-17*

- Removes support for running Ops Manager on:

  - RHEL 7.x/8.x, and Ubuntu 16.x on PowerPC (`ppc64le`)
    architectures.
  - RHEL 6.x/7.x, Ubuntu 18.x, and SUSE 12.x on zSeries (`s390x`)
    architectures.

  To learn more about supported platforms for running Ops Manager on,
  see Ops Manager Software Requirements.

- Fixes an issue where S3-compatible storage Oplog Stores can leave behind S3-compatible storage 
  objects even after the configured retention window has elapsed.

- Updates the JDK (Java Development Kit) to `jdk-11.0.14.1+1`.

- Removes workaround to use an X.509 CommonName instead of a SAN (Subject Alternative Name).

- Updates the MongoDB Agent to 10.14.32.6576.

### Ops Manager Server 4.4.20

*Released 2022-01-13*

- Updates the MongoDB Agent to 10.14.31.6566.

- When taking a snapshot, allows the MongoDB Agent to slow the sending of data blocks 
  when Ops Manager is overloaded, so that the snapshot can complete. Successful 
  completion of snapshots is prioritized over speed.

  **Important:**

  To use this feature, you must upgrade to 
  the latest version of the MongoDB Agent.

### Ops Manager Server 4.4.19

*Released 2021-11-16*

- Updates JDK to jdk-11.0.13+8.
- Updates the MongoDB Agent to 10.14.30.6552.

### Ops Manager Server 4.4.18

*Released 2021-11-04*

- Updates the MongoDB Agent to 10.14.29.6548.
- Removes support for RHEL 6.

### Ops Manager Server 4.4.17

*Released 2021-09-03*

- Fixes a bug where, when running in local mode, with both PowerPC
  RHEL71 and RHEL81 builds of MongoDB present, the RHEL81 build would
  always be selected.

- Updates the MongoDB Agent to 10.14.28.6532.

- Upgrades the JDK to version 11.0.12, which restricts the use of
  insecure TLS versions 1.0 and 1.1. To learn more, see the
  [JDK release notes](https://www.oracle.com/java/technologies/javase/11-0-11-relnotes.html#JDK-8202343).

- Compatible with `MongoDB Database Tools 100.5.0`.

### Ops Manager Server 4.4.16

*Released 2021-08-05*

- Fixes a bug that caused restore to fail due to an invalid ping from 
  the backup agent.

- Adds a warning message when Ops Manager has less than 10GB of disk space 
  available.

- Fixes a bug that caused the System Alerts UI to fail after a system 
  alert was saved with a webhook URL.

- Updates the MongoDB Agent to 10.14.27.6524.

- Compatible with `MongoDB Database Tools 100.3.1`.

### Ops Manager Server 4.4.15

*Released 2021-07-01*

- When creating a global owner, the generated API (Application Programming Interface) keys now also
  include the selected IP access list
- Compatible with `MongoDB Database Tools 100.3.1`.

### Ops Manager Server 4.4.14

*Released 2021-06-10*

- Fixes a bug that caused restore to fail due to an invalid tar header 
  for filesystem stores.
- Compatible with `MongoDB Database Tools 100.3.1`.

### Ops Manager Server 4.4.13

*Released 2021-06-03*

- Upgrades JDK (Java Development Kit) to `jdk-11.0.11+9`.
- Disables TLS (Transport Layer Security) versions 1.0 and 1.1.
- Fixes a bug that would re-enable Ops Manager instances for API writes 
  during an upgrade of Ops Manager.
- Fixes a date formatting issue when listing logs in the `admin` 
  user interface.
- Adds MongoDB server for RHEL 8.1 running on PowerPC to Ops Manager\'s 
  version manifest.
- Caches the computed list of MongoDB binaries available on disk in 
  Local Mode.
- Updates the MongoDB Agent to 10.14.24.6508.
- Compatible with `MongoDB Database Tools 100.3.1`.

### Ops Manager Server 4.4.12

*Released 2021-05-06*

- Fixed a bug that caused the User Authentication Method 
  field on the Ops Manager Config page to not display a 
  visual indicator that the setting is overwritten in the configuration 
  file.
- Removed support for Ubuntu 16.04 since Ubuntu 16.04 is End OF Life
  (EOL) as of April 2021.

- Updates the MongoDB Agent to
  10.14.23.6498.

- Compatible with `MongoDB Database Tools 100.3.1`.

### Ops Manager Server 4.4.11

*Released 2021-04-01*

- Updates an outdated comment in the `conf-mms.properties` file.
  Even though Ops Manager 4.4.11 does not add any new parameters to this
  file, the upgrade process detects that the file had changed.
  To avoid having to manually reconfigure Ops Manager, ensure that Ops Manager
  uses the current version of this file after the upgrade. Create and
  store backup copies of all your configuration files, to avoid losing
  important Ops Manager configuration.

  - For upgrades that use the `.deb` package,
    the upgrade process prompts you
    to choose which version of the `conf-mms.properties` file
    Ops Manager should use. Choose the current `conf-mms.properties`
    file.

  - For upgrades that use the `rpm` package,
    the upgrade process saves
    the `conf-mms.properties` file as the
    `conf-mms.properties.rpmsave`
    file. Use the `mv` command to rename
    `conf-mms.properties.rpmsave`
    to `conf-mms.properties`. This ensures that Ops Manager uses the
    current file after the upgrade.

- Fixes a bug in the MongoDB usage report where backing databases are
  not correctly identified.
- Fixes a bug in the MongoDB usage report where Ops Manager  could
  potentially find duplicate hosts based on network aliases.
- Fixes a bug that causes some MongoDB versions to be considered as
  custom builds when validating the Automation configuration.
- Fixes a bug that disallows configuring LDAP (Lightweight Directory Access Protocol) group names longer
  than 100 characters.
- Updates the MongoDB Agent to 10.14.22.6489.
- Requires [MongoDB Database Tools 100.3.1](https://www.mongodb.com/docs/database-tools/release-notes/database-tools-changelog#100.3.1-changelog).
- Changes the protocolVersion 
  API parameter from an integer to a string. For example, previously, 
  you could specify  `1` for this parameter. Now, you must specify 
  `"1"` for this parameter instead.

### Ops Manager Server 4.4.10

*Released 2021-03-04*

- Allows you to choose either redact, or to not redact, sensitive
  information from the server usage report. If you choose to redact,
  Ops Manager redacts before it generates the report for download.
- Updates the MongoDB Agent to
  10.14.21.6476.
- Requires `MongoDB Database Tools 100.3.0`.

### Ops Manager Server 4.4.9

*Released 2021-02-17*

- Fixes a regression introduced in Ops Manager 4.4.8 that prevents the MongoDB
  Version Manifest from being updated.
- Updates the MongoDB Agent to
  10.14.20.6466.
- Requires `MongoDB Database Tools 100.2.0`.

### Ops Manager Server 4.4.8

*Released 2021-02-05*

- Improves backup snapshot performance.
- Requires `MongoDB Database Tools 100.2.0`.

### Ops Manager Server 4.4.7

*Released 2021-01-11*

- Fixes a bug that causes the Ops Manager
  Backup process to require excess
  memory when terminating the backup job.
- Fixes a bug that causes the backup process to fail to take new
  snapshots when using a File System Store during a
  backup of a MongoDB
  deployment on version 4.2 or later.
- Limits host ping information from active groups to when
  generating the diagnostic archives file.
- Limits backup logs based on the `limit` option when generating the
  diagnostic archives.
- Updates the MongoDB Agent to
  10.14.18.6453.
- Requires `MongoDB Database Tools 100.2.0`.

### Ops Manager Server 4.4.6

*Released 2020-12-03*

- Fixes a bug that prevents Ops Manager from correctly authenticating to an
  HTTP Proxy.
- Limits Tracking and Groom Jobs to the Backup Daemons set in the
  Backup Configuration. This applies to the project in which you set
  the configuration and run the jobs.
- Updates the MongoDB Agent to
  10.14.17.6445
- Requires `MongoDB Database Tools 100.2.0`.

### Ops Manager Server 4.4.5

*Released 2020-11-05*

- Updates the JDK (Java Development Kit) to `jdk-jdk-11.0.9.11.1`.

- Supports viewing MongoDB Profiler entries with overlapping timestamps
  separately in the Visual Query Profiler.

- Updates the MongoDB Agent to
  10.14.16.6437.

- Requires `MongoDB Database Tools 100.2.0`.

### Ops Manager Server 4.4.4

*Released 2020-10-07*

- Adds JVM (Java Virtual Machine) Arguments in the Ops Manager diagnostic archive.

- Adds a new configuration parameter `Non Proxy Hosts`
  which allows the Ops Manager Application Server to bypass the
  outgoing proxy you configured when accessing specific hosts.

- Fixes a bug that prevents users from changing their password.

- Updates the MongoDB Agent to
  10.14.15.6432.

- Adds support for Ubuntu 20.04.

- Requires `MongoDB Database Tools 100.1.0`.

### Ops Manager Server 4.4.3

*Released 2020-09-23*

- Fixes a high severity vulnerability in Ops Manager. `CVE-2020-7927`
  is allocated for this issue.

- Fixes an issue that can prevent alert processing for monitored
  clusters with partial status information.

- Removes `muninEnabled` and `muninPort` fields from the
  Hosts API (Application Programming Interface).

- Updates the MongoDB Agent to
  10.14.14.6427.

- Requires `MongoDB Database Tools 100.1.0`.

### Ops Manager Server 4.4.2

*Released 2020-09-03*

- Fixes unexpected errors that occur when:

  - Editing a blockstore with one or more dots (`.`) in its name.
  - Trying to update
    Global API Keys via the
    API (Application Programming Interface) with an invalid request.
  - Trying to update a global whitelist IP.

- Includes `MongoDB Business Intelligence Connector v2.14.0`.

- Supports file system snapshot stores with MongoDB databases running
  FCV 4.2 or later.

- Updates the MongoDB Agent to
  10.14.13.6423.

- Requires `MongoDB Database Tools 100.1.0`.

### Ops Manager Server 4.4.1

*Released 2020-08-05*

- Allows replica sets to be force reconfigured using console.

- Fixes an issue with Organization-level API (Application Programming Interface) key returning
  [HTTP error 500](https://httpstatuses.com/500) when no roles are
  defined.

- Improves Ops Manager packaging.

- Updates MongoDB Agent to 10.14.12.6411.

- Requires `MongoDB Database Tools 100.0.2`.

### Ops Manager Server 4.4.0

*Released 2020-07-08*

- Supports management, monitoring and backup of MongoDB 4.4
  deployments.

- Can be deployed to Kubernetes using the
  `MongoDB Enterprise Kubernetes Operator`.

- Improves summary and detailed views of MongoDB deployments.

- Improves the operational performance of managing large sharded
  clusters.

  **Example:**

  Applies requested configuration changes across the cluster faster.

- Improves rendering performance of the Metrics page.

- Supports direct monitoring of the Ops Manager application database.

- Supports fetching MongoDB binaries from a custom HTTP (Hypertext Transfer Protocol) server.

- Sets the Profiler to use MongoDB slow query logs as the default data
  source.

  If you had not enabled the Profiler:
    You now see the Profiler. Ops Manager
    sources the data points from your
    slow query logs. These
    data points have
    been logged since Ops Manager 4.2 through the
    Performance Advisor.

  If you had enabled the Profiler:
    You continue to see the Profiler. Ops Manager sources the data points
    from your slow query logs  rather than
    through the
    MongoDB Profiler entries.
    (These entries continue to be ingested.) The MongoDB Profiler
    entries contain more detailed information than the slow query
    logs. To revert to using the profiler entries, toggle the
    Project's feature flag Profiler Nds to `OFF`.

- Introduces Schema Advisor for automatic identification of schema
  optimization opportunities.

- Supports AWS (Amazon Web Services) IAM (Identity and Access Management) roles in S3-compatible storage Snapshot Store configurations.

- Upgrades OpenJDK to 11.0.8+10.

- Requires `MongoDB Database Tools 100.0.2`.

**Note:** Ops Manager Support Ends after 4.4 Series

- Support for running Ops Manager on the Windows platform ends after the
  4.4 series.

- Ops Manager still supports managing MongoDB deployments that run on
  Windows 2016, 2019, 2020.
