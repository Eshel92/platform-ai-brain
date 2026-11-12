<!-- Part 6 of 10 of release-notes/application.md (split because the page is big). -->

## Ops Manager Server 4.0

### Ops Manager Server 4.0.20

*Released on 2020-11-05*

- Updates the JDK (Java Development Kit) to jdk-jdk8u272b10.1.

- **Upgrades Agents**: backup-6.8.9.1030 and
  monitoring-6.6.4.472. 

### Ops Manager Server 4.0.19

*Released on 2020-08-06*

- Fixes a bug with converting from LDAP (Lightweight Directory Access Protocol) Native Authentication to
  `saslauthd`.

### Ops Manager Server 4.0.18

*Released on 2020-05-14*

- Upgrade from [urllib3](https://urllib3.readthedocs.io/en/latest/)
  1.15.8 to 1.25.2 due to a
  [Denial of Service (DoS) vulnerability](https://snyk.io/vuln/SNYK-PYTHON-URLLIB3-559452).

- Resolves issue when toggling the authentication mechanism for a
  MongoDB User in the Deployment arrow-right
  Security arrow-right Users tab
  between SCRAM-SHA-256 and SCRAM-SHA-1.

- Updates JDK (Java Development Kit) to AdoptOpenJDK 1.8.0-252.

### Ops Manager Server 4.0.17

*Released on 2020-02-06*

- Updates JDK (Java Development Kit) to AdoptOpenJDK 1.8.0-242.

- **Upgrades Agent:** automation-5.4.24.5565

### Ops Manager Server 4.0.16

*Released on 2019-11-07*

- Improves backup initial sync time for MMAPv1 collections in which
  there is a high rate of change during the backup initial sync.
- Improves handling of operations that modify the data directory
  (restores, storage engine changes, etc.) for deployments where the
  MongoDB journal directory is mounted on a separate partition.
- Includes various security improvements.
- Upgrades the JDK (Java Development Kit) to 1.8.232.

- **Agent Upgrades:** automation-5.4.23.5559,
  backup-6.8.8.1027, and monitoring-6.6.3.469

### Ops Manager Server 4.0.15

*Released on 2019-09-05*

- Loosens validations to allow for spaces in replica set names.

- Agent Upgrades: automation-5.4.22.5547

### Ops Manager Server 4.0.14

*Released on 2019-07-31*

- **Dependency Update:** Updates `org.quartz-scheduler:quartz` to
  2.3.1 to address CVE-2018-20433.

- **Fix:** Backup Daemons on Amazon Linux 2 and SUSE 12/15 can
  successfully download required MongoDB builds.

  **Note:**

  This problem was introduced in Ops Manager
  4.0.13 and resolved in Ops Manager
  4.0.14.

- **Fix**: Fixes a bug which prevented the following two algorithms to
  be disabled by default when using
  SSL connections with Ops Manager:

  - `TLS_DHE_RSA_WITH_AES_256_GCM_SHA384`
  - `TLS_DHE_RSA_WITH_AES_256_CBC_SHA256`

  These algorithms are now disabled by default.

- Improves performance when downloading multiple restores concurrently.

- **Agent Upgrades:** automation-5.4.21.5544

### Ops Manager Server 4.0.13

*Released on 2019-07-04*

- Removing whitelist from Admin (General > Users) now possible.
  Displays error message when Authentication expires

- **Agent Upgrades:** automation-5.4.20.5541,
  backup-6.8.7.1024

### Ops Manager Server 4.0.12

*Released on 2019-06-06*

- **Fix:** Authentication & TLS/SSL settings allows removal
  of `PEM` key file and password no matter the
  `tlsMode`.

- **Fix:** Fixes support for the `security.clusterIpSourceWhitelist`
  MongoDB configuration option.

- **Dependency Update:** Updates jetty to 9.4.18.

- **Agent Upgrades:** automation-5.4.19.5537

- **EOL:** Ops Manager support for Ubuntu 14.04 has ended. Ops Manager
  4.0.12 is not supported on Ubuntu 14.04.

### Ops Manager Server 4.0.11

*Released on 2019-05-02*

**Important:**

Fixes important security fixes, including a
[CVSSv3.1 score](https://www.first.org/cvss/specification-document)
of [5.8 (Medium Severity)](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:N/A:N).

* - ID
  - [CVE-2019-2388](https://cve.mitre.org/cgi-bin/cvename.cgi?name=2019-2388)

* - Title
  - Potential exposure of log information in Ops Manager

* - Description
  - In affected Ops Manager versions, an exposed HTTP (Hypertext Transfer Protocol) route may
    allow attackers to view a specific access log of a publicly
    exposed Ops Manager instance.

* - CVE (Common Weakness Enumeration)
  - [CVE-425: Direct Request ('Forced Browsing') (4.0)](https://cwe.mitre.org/data/definitions/425.html)

* - CVSS (Common Vulnerability Scoring System) score
  - 5.8 (Medium): [CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:N/A:N](https://www.first.org/cvss/calculator/3.1#CVSS:3.1/AV:N/AC:L/PR:N/UI:N/S:C/C:L/I:N/A:N)

* - Affected versions
  -
    - Ops Manager 4.0 series: 4.0.9, 4.0.10
    - Ops Manager 4.1 series: 4.1.5

- Provides a new option to bypass invitations so you can add users to
  organizations and projects immediately, without requiring them to
  accept an invitation. Organization and project owners can enable
  this setting in the User Authentication section of the
  Ops Manager Config wizard.

  This setting is only available when managing user accounts in the
  Application Database. The
  invitation bypass option is available for users added via the UI
  and the API (Application Programming Interface).

- **Fix:** When enabling MongoDB profiling from the Profile
  tab, ensure that the pending changes banner is shown without
  requiring a browser refresh.

- Updated JDK (Java Development Kit) to version 8u212. On Windows, Ops Manager now requires
  the [Visual C++ Redistributable Packages for Visual Studio 2013](https://www.microsoft.com/en-us/download/details.aspx?id=40784).

### Ops Manager Server 4.0.10

*Released on 2019-04-04*

- **Fix:** Creating new projects now succeeds in Firefox.
- **Fix:** When managing authentication for a deployment, the MongoDB
  `keyfile` parameter is not required if all processes set the
  `clusterAuthMode` parameter to `x509`.
- **Fix:** A backup initial sync of MongoDB 3.4 can misapply oplogs in
  rare circumstances in which `mongod` returns a partial `applyOps`
  result array.
- **Fix:** Hidden secondaries display the correct icon in the user interface.
- Improved the durability of backup data in the event that a head
  database experiences an unclean shutdown.
- Improved performance for the Deployment page for deployments with many items.
- Easier to disable TLS/SSL when managing TLS/SSL configuration for a deployment.
- Update BI Connector to 2.10.

### Ops Manager Server 4.0.9

*Released on 2019-03-09*

- Add support for managing MongoDB deployments on IBM zSeries for the
  Ubuntu 18.04, SUSE12 and RHEL7 operating systems.
- **Fix:** Add validation for allowed characters for the names of
  filesystem snapshot stores, S3 snapshot stores and MongoDB blockstore
  snapshot stores.
- **Fix:** Do not remind users to configure two-factor authentication,
  if two-factor authentication has been disabled for the Ops Manager
  installation.
- **Fix:** Ensure that all redirects are always relative URI (Uniform Resource Identifier)\s.

### Ops Manager Server 4.0.8

*Released on 2019-02-07*

- Updated JDK (Java Development Kit) to [AdoptOpenJDK 8u202](https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/tag/jdk8u202-b08).

- **Fix:** For queryable restores, the configurable expiration value
  (`brs.queryable.expiration`) now also applies to
  MongoDB authentication requests.

- **Fix:** Improve password verification for sensitive actions within
  Ops Manager, for Ops Manager installations using LDAP (Lightweight Directory Access Protocol) for user
  authentication, and ActiveDirectory as the LDAP (Lightweight Directory Access Protocol) server.

- **Agent Upgrades:** automation-5.4.16.5515

### Ops Manager Server 4.0.7

*Released 2019-01-10*

- Address the [CVE-2018-19361](https://nvd.nist.gov/vuln/detail/CVE-2018-19361)
  affecting the [jackson-databind](https://github.com/FasterXML/jackson-databind)
  library up to and including version 2.9.7.

- **Fix:** Resolve transient inability to restore a snapshot, if a
  backup data pruning job (garbage collection) is running during the
  restore.

- Updated JDK (Java Development Kit) to [AdoptOpenJDK 8u192](https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/tag/jdk8u192-b12).

- **Agent Upgrades:** automation-5.4.15.5513, backup-6.8.6.1013

### Ops Manager Server 4.0.6

*Released 2018-12-10*

- **Bug fix:** When a project is deleted, remove any open Global Alerts.

- **Bug fix:** Authentication & TLS (Transport Layer Security)/SSL (Secure Sockets Layer) Settings allows removal of
  PEM (Privacy-Enhanced Mail) key file and password no matter the `sslMode`.

- **Bug fix:** Restore ability to rotate the KMIP (Key Management Interoperability) master key.

- Increase timeout for starting queryable restore jobs. This increases
  robustness for data sets with large numbers of namespaces.

- Various optimizations to allow faster backup restores.

- Visual Query Profiler can handle value of Infinity.

- **Agent Upgrades:** automation-5.4.14.5509

### Ops Manager Server 4.0.5

*Released 2018-11-01*

- **Fix:** Removed memory leak in proxy server used for queryable
  restores.

- **Fix:** Removed race condition that could cause a backup initial
  sync to be required when the `featureCompatibilityVersion` is
  updated on the source replica set.

- **Fix:** Automatic download of MongoDB binaries fails when hybrid
  mode is enabled for MongoDB binary management.

- **Fix:** When importing a cluster into Ops Manager, ignore the value
  of `pidFilePath` if it set to the CentOS default in `/var/run`.

- Updated JDK (Java Development Kit) to
  [8u192](https://www.oracle.com/technetwork/java/javase/8u192-relnotes-4479409.html).

- Updated bundled version of the `BI Connector` to 2.7.0.

- **Agent Upgrades:** automation-5.4.13.5505

### Ops Manager Server 4.0.4

*Released 2018-10-12*

- **Critical Fix:** When running in local mode for MongoDB binary
  management, the Backup Daemon may try to use MongoDB binaries for
  the wrong operating system.

- **Agent Upgrades:** automation-5.4.12.5501

### Ops Manager Server 4.0.3

*Released 2018-10-04*

- **Critical Fix:** Backup initial syncs may fail with an error during
  the oplog application phase, if retryable writes are executed on the
  source cluster during the backup initial sync.
- **Fix:** Log collection fails for log files greater than
  approximately 2.2 GB.
- LDAP (Lightweight Directory Access Protocol) connections will now use a connection pool. This reduces load
  on LDAP (Lightweight Directory Access Protocol) servers.
- Update bundled version of the `MongoDB Connector for BI` to version 2.6.1.

### Ops Manager Server 4.0.2

*Released 2018-09-06*

- Adds support for management of MongoDB processes on Ubuntu 18.04.

- User alerts are now available.

- **Fix:** When performing a point in time restore for MongoDB 4.0,
  drop the `minOptimeRecovery` document before bringing up the
  target cluster.

- Show MongoDB start-up warnings on the cluster overview page.

- Log Collection was unable to complete if one of the
  requested files was an empty file.

- Real Time Performance Panel adds support for killing
  sessions in MongoDB 4.0+.

- Support additional schema-related options when configuring
  the MongoDB BI Connector.

- Perform additional validations for deployments managed by external
  orchestration platforms (such as the
  `MongoDB Enterprise Operator for Kubernetes`).

- **Agent Upgrades:** automation-5.4.10.5496

### Ops Manager Server 4.0.1

*Released 2018-08-02*

- **Critical Fix:** Allow removal of processes from
  Deployment arrow-right List view.

- **Critical Fix:** Avoid failures to upgrade from Ops Manager 3.4
  when using local mode for MongoDB version management.

- **Critical Fix:** Fix issue which caused the All Clusters
  page to fail to display content.

- During a backup initial sync, ensure that the UUID of the
  `system.views` collection is preserved.

- In Local Mode, the Backup Daemon will now unpack MongoDB tarballs.
  Administrators no longer need to unpack them themselves.

- Reinstate support for `security.encryptionKeyFile` parameter.

- Security patches for third-party library dependencies.

- Updates Ops Manager JDK (Java Development Kit) (x86_64) to 8u181, which enables endpoint
  identification by default.

- When configuring MongoDB LDAP (Lightweight Directory Access Protocol) authentication, allow setting the
  User to Distinguished Name Mapping without setting the Authorization
  Query Template.

- **Agent Upgrades:** automation-5.4.9.5483,  backup-6.8.4.1009

- **Critical Fix:** Set `TasksMax=infinity` and
  `TasksAccounting=false` in `systemd` scripts for
  SUSE 12 versions of Ops Manager.

### Ops Manager Server 4.0.0

*Released 2018-06-27*

- Revised Ops Manager interface for deployment management.

- Added new CRUD (create, read, update, and delete) features
  to Data Explorer.

- Improved the
  Real-Time Performance Panel.

- Added integrations for:

  - [Pivotal Cloud Foundry](https://pivotal.io/platform/services-marketplace/data-management/mongodb)
  - `Kubernetes` (beta)

- Improved Monitoring

  - Added alert for rollback.

- Updated Public API (Application Programming Interface)

  - Added endpoints for Public
    API (Application Programming Interface) Keys.
  - Added endpoints to manage Agent
    API (Application Programming Interface) keys.
  - Removed support for Agent
    API (Application Programming Interface) keys created
    before Ops Manager 3.4.

- Provided new option to only
  have Ops Manager connect to the internet to download MongoDB installer
  binaries.

- Deprecated Server Pools.

  - In Ops Manager 4.0, Server Pools are disabled by default.
  - If you are currently using Server Pools, they will continue to
    work as expected after upgrading to Ops Manager 4.0.

- Added platform support to include:

  - Amazon Linux 2
  - Debian 9
  - SLES (SUSE Linux Enterprise Server) 12

- Deprecated platform support for:

  - Windows 2008 R2
  - MongoDB 2.6, 3.0

  **Note:**

  Support for these platforms will be removed in a future Ops Manager
  release.

- Removed platform support for:

  - Ubuntu 12.04
  - SLES (SUSE Linux Enterprise Server) 11
  - Debian 7

- Added support for PowerPC hardware using the following Linux distros:

  - Ubuntu 16.04
  - RHEL (Red Hat Enterprise Linux) 7.x

- **Agent Upgrades:**
  automation-5.4.6.5465,
  backup-6.8.3.1002,
  monitoring-6.6.2.464
