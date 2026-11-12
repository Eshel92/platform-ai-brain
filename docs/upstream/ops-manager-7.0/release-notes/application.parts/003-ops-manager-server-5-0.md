<!-- Part 3 of 10 of release-notes/application.md (split because the page is big). -->

## Ops Manager Server 5.0

### Ops Manager Server 5.0.22

*Released 2023-07-31*

- Updates JDK to `jdk-11.0.20+8`.
- Updates the MongoDB Agent to 11.0.27.7162.
- Includes `MongoDB Database Tools 100.7.1`.
- Fixes CVE-2023-4009: Privilege Escalation for `Project Owner`
  and `Project User Admin` roles in Ops Manager.

  - In MongoDB Ops Manager 5.0 prior to 5.0.22, an authenticated user with
    `Project Owner` or `Project User Admin` access
    roles could generate an API key with the privileges of the
    `Organization Owner` role resulting in privilege escalation.
  - CVSS Score: 7.2.
  - CWE-648: Incorrect Use of Privileged APIs.

### Ops Manager Server 5.0.21

*Released 2023-06-1*

- Updates JDK to `jdk-11.0.19+7`.
- Updates the MongoDB Agent to 11.0.26.7158.
- Includes BI Connector 2.14.6.
- Includes `MongoDB Database Tools 100.7.0`.
- Defaults the Multiple Workers option for a single file 
  during backup to On.
- Snapshots now include a flag that indicates whether or not they are incremental.
- Fixes [CVE-2023-0342](https://nvd.nist.gov/vuln/detail/CVE-2023-0342).
- Fixes a bug in the MongoDB Agent where the shutdown sequence might get
  blocked under certain circumstances, resulting in failed Agent upgrades.

### Ops Manager Server 5.0.20

*Released 2023-03-15*

- Updates the MongoDB Agent to 11.0.25.7136.
- Updates [Apache Commons FileUpload](https://commons.apache.org/proper/commons-fileupload/) to 1.5 to 
  address [CVE-2023-24998](https://nvd.nist.gov/vuln/detail/CVE-2023-24998).
- Adds an option to support using multiple workers for a single file 
  during backups. You can enable this beta feature by doing the
  following: 

  1. In the Settings page for
     your Project, click the Beta Features tab.
  2. Toggle Backup Multiple Workers Per File to enable the 
     feature. 

### Ops Manager Server 5.0.19

- Updates `woodstox:woodstox-core` to 6.2.6 to address 
  [CWE-611](https://cwe.mitre.org/data/definitions/611.html).
- Updates the MongoDB Agent to 11.0.24.7131.
- Compatible with `MongoDB Database Tools 100.6.1`.

### Ops Manager Server 5.0.18

*Released 2023-02-02*

- Updates JDK to `jdk-11.0.18+10`.
- Updates the MongoDB Agent to 11.0.23.7129.

### Ops Manager Server 5.0.17

*Released 2022-11-17*

- Updates JDK to `jdk-11.0.17+8`.
- Updates the MongoDB Agent to 11.0.22.7120.

### Ops Manager Server 5.0.16

*Released 2022-10-20*

- Updates `commons-text` to 1.10.0 to address 
  [CVE-2022-42889](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42889).
- Compatible with `MongoDB Database Tools 100.6.0`.
- Uses amazon2 packages instead of RHEL7 packages on amazon2 hosts for
  MongoDB Database Tools. If you run Ops Manager in the local mode, you can download
  amazon2 MongoDB Database Tools binaries via the MongoDB Agent.

### Ops Manager Server 5.0.15

*Released 2022-09-19*

- Removes spurious audit log rotation errors from the MongoDB Agent log 
  files and corrects file suffix handling.
- Updates JDK to `jdk-11.0.16.1+1`.
- Updates the MongoDB Agent to 11.0.20.7108.

### Ops Manager Server 5.0.14

*Released 2022-08-04*

- Updates JDK to jdk-11.0.16+8.
- Updates the MongoDB Agent to 11.0.19.7094.

  **Warning:**

  Due to critical issue SERVER-68925, Ops Manager deployments
  using this version of the MongoDB Agent should not perform [automated rolling index builds](https://www.mongodb.com/docs/ops-manager/v5.0/data-explorer/indexes/#optional-build-indexes-with-rolling-builds) on clusters running the following MongoDB versions:

  - MongoDB 4.2.19-4.2.22
  - MongoDB 4.4.13-4.4.16
  - MongoDB 5.0.6-5.0.11
  - MongoDB 6.0.0-6.0.1

  You can continue to perform manual rolling index builds safely on your clusters.
  To perform automated rolling index builds safely,  
  upgrade your clusters to:

  - MongoDB 4.2.23 or later
  - MongoDB 4.4.17 or later
  - MongoDB 5.0.12 or later
  - MongoDB 6.0.2 or later

### Ops Manager Server 5.0.13

*Released 2022-07-21*

- Updates the MongoDB Agent to 11.0.18.7089.

  **Warning:**

  Due to critical issue SERVER-68925, Ops Manager deployments
  using this version of the MongoDB Agent should not perform [automated rolling index builds](https://www.mongodb.com/docs/ops-manager/v5.0/data-explorer/indexes/#optional-build-indexes-with-rolling-builds) on clusters running the following MongoDB versions:

  - MongoDB 4.2.19-4.2.22
  - MongoDB 4.4.13-4.4.16
  - MongoDB 5.0.6-5.0.11
  - MongoDB 6.0.0-6.0.1

  You can continue to perform manual rolling index builds safely on your clusters.
  To perform automated rolling index builds safely,  
  upgrade your clusters to:

  - MongoDB 4.2.23 or later
  - MongoDB 4.4.17 or later
  - MongoDB 5.0.12 or later
  - MongoDB 6.0.2 or later

- Fixes an issue that caused premature termination of sharded cluster 
  snapshots when one shard completed its snapshot before the other 
  shards.

### Ops Manager Server 5.0.12

*Released 2022-06-30*

- Updates `log4j-over-slf4j` to 1.7.36 to address
  [CVE-2020-9493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2020-9493).
- Fixes an issue where editing an Oplog Store's name that contains dots 
  (`.`) might have resulted in errors.
- Compatible with `MongoDB Database Tools 100.5.3`.
- Updates the MongoDB Agent to 11.0.17.7086.
- Switches to the BCFIPS Java Security Provider library.
- Switches from using `/dev/random` for random number generation to
  using `/dev/urandom`.

  **Warning:**

  Due to critical issue SERVER-68925, Ops Manager deployments
  using this version of the MongoDB Agent should not perform [automated rolling index builds](https://www.mongodb.com/docs/ops-manager/v5.0/data-explorer/indexes/#optional-build-indexes-with-rolling-builds) on clusters running the following MongoDB versions:

  - MongoDB 4.2.19-4.2.22
  - MongoDB 4.4.13-4.4.16
  - MongoDB 5.0.6-5.0.11
  - MongoDB 6.0.0-6.0.1

  You can continue to perform manual rolling index builds safely on your clusters.
  To perform automated rolling index builds safely,  
  upgrade your clusters to:

  - MongoDB 4.2.23 or later
  - MongoDB 4.4.17 or later
  - MongoDB 5.0.12 or later
  - MongoDB 6.0.2 or later

### Ops Manager Server 5.0.11

*Released 2022-06-02*

- Adds support for the [PagerDuty](https://www.pagerduty.com/) Events API V2. All new [PagerDuty](https://www.pagerduty.com/) keys use their [Events API v2](https://developer.pagerduty.com/docs/ZG9jOjExMDI5NTgw-events-api-v2-overview). 
- Fixes an issue where updating MongoDB Agent versions via the API fails when you 
  use controlled features.
- Updates the MongoDB Agent to 11.0.16.7080.

  **Warning:**

  Due to critical issue SERVER-68925, Ops Manager deployments
  using this version of the MongoDB Agent should not perform [automated rolling index builds](https://www.mongodb.com/docs/ops-manager/v5.0/data-explorer/indexes/#optional-build-indexes-with-rolling-builds) on clusters running the following MongoDB versions:

  - MongoDB 4.2.19-4.2.22
  - MongoDB 4.4.13-4.4.16
  - MongoDB 5.0.6-5.0.11
  - MongoDB 6.0.0-6.0.1

  You can continue to perform manual rolling index builds safely on your clusters.
  To perform automated rolling index builds safely,  
  upgrade your clusters to:

  - MongoDB 4.2.23 or later
  - MongoDB 4.4.17 or later
  - MongoDB 5.0.12 or later
  - MongoDB 6.0.2 or later

### Ops Manager Server 5.0.10

*Released 2022-05-05*

- Adds support for Debian 10 when you use the `BI Connector`.
- Fixes an issue that occured when you changed the default server usage
  for organizations.
- Updates the JDK (Java Development Kit) to `jdk-11.0.15+10`.
- Updates the MongoDB Agent to 11.0.15.7073.

  **Warning:**

  Due to critical issue SERVER-68925, Ops Manager deployments
  using this version of the MongoDB Agent should not perform [automated rolling index builds](https://www.mongodb.com/docs/ops-manager/v5.0/data-explorer/indexes/#optional-build-indexes-with-rolling-builds) on clusters running the following MongoDB versions:

  - MongoDB 4.2.19-4.2.22
  - MongoDB 4.4.13-4.4.16
  - MongoDB 5.0.6-5.0.11
  - MongoDB 6.0.0-6.0.1

  You can continue to perform manual rolling index builds safely on your clusters.
  To perform automated rolling index builds safely,  
  upgrade your clusters to:

  - MongoDB 4.2.23 or later
  - MongoDB 4.4.17 or later
  - MongoDB 5.0.12 or later
  - MongoDB 6.0.2 or later

### Ops Manager Server 5.0.9

*Released 2022-04-07*

- Adds support for concurrent MongoDB version 4.2+ snapshots and S3 snapshot store grooms.
- Fixes an incorrect link when filtering backup jobs on the admin pages.
- Fixes an issue where the MongoDB Agent erroneously rejects changes when you use controlled features.
- Changes how disk space is calculated for Cloud Live Migrations. Starting with this release, 
  the migration process validates that the target MongoDB Atlas cluster has enough free disk based 
  on the storage size of the compressed data. To learn more about data and storage sizes, see 
  dbStats.
- Fixes an issue when creating LDAP group mappings through the API.
- Updates the MongoDB Agent to 11.0.14.7064.
- Compatible with `MongoDB Database Tools 100.5.2`.

### Ops Manager Server 5.0.8

*Released 2022-03-03*

- Supports MongoDB log rotate configuration and commands for 
  independent log rotation configuration for MongoDB Log and MongoDB 
  Audit Log Files.

- Updates the MongoDB Agent to 11.0.13.7055.

- Compatible with `MongoDB Database Tools 100.5.2`.

### Ops Manager Server 5.0.7

*Released 2022-02-17*

- Removes support for running Ops Manager on:

  - RHEL 7.x/8.x, and Ubuntu 16.x on PowerPC (`ppc64le`)
    architectures.
  - RHEL 6.x/7.x, Ubuntu 18.x, and SUSE 12.x on zSeries (`s390x`)
    architectures.

  To learn more about supported platforms for running Ops Manager on, see
  Ops Manager Software Requirements.
- Fixes an issue where S3 Oplog Stores can leave behind S3 objects even
  after the configured retention window has elapsed.
- Updates JDK to jdk-11.0.14.1+1
- Keeps legacy monitoring and backup agents in sync with MongoDB agent
  configuration when making `automationConfig` API and UI updates.
- Removes workaround to use an X.509 CommonName instead of a SAN (Subject Alternative Name).
- Updates the MongoDB Agent to 11.0.12.7051
- Compatible with `MongoDB Database Tools 100.5.2`.

### Ops Manager Server 5.0.6

*Released 2022-01-13*

- Improves storage size calculation for a Cloud Live Migration of a
  sharded cluster.

- Fixes a bug that prevents Ops Manager from syncing user information from
  LDAP servers.

- Fixes a bug where Ops Manager incorrectly escaped characters in LDAP
  search filters.

- Updates the MongoDB Agent to 11.0.11.7036.

- When taking a snapshot, allows the MongoDB Agent to slow the sending
  of data blocks when Ops Manager is overloaded, so that the snapshot can
  complete. Successful completion of snapshots is prioritized over
  speed.

  **Important:**

  To use this feature, you must upgrade to 
  the latest version of the MongoDB Agent.

- Compatible with `MongoDB Database Tools 100.5.1`.

### Ops Manager Server 5.0.5

*Released 2021-12-02*

- Upgrades the JDK to version 11.0.13.
- Updates the MongoDB Agent to 11.0.10.7021.

### Ops Manager Server 5.0.4

*Released 2021-11-04*

- Fixed an issue where S3-compatible oplog store\s would not appear on the 
  Oplog Storage page in the administration console in all
  configurations.

- Updates the MongoDB Agent to 11.0.9.7010.

- Removes support for RHEL 6.

### Ops Manager Server 5.0.3

*Released 2021-10-06*

- Updates the MongoDB Agent to 11.0.8.7002.

### Ops Manager Server 5.0.2

*Released 2021-09-03*

- Fixes a bug where, when running in local mode, with both PowerPC
  RHEL71 and RHEL81 builds of MongoDB present, the RHEL81 build would
  always be selected.

- Updates the MongoDB Agent to 11.0.7.6992.

- Upgrades the JDK to version 11.0.12, which restricts the use of
  insecure TLS versions 1.0 and 1.1. To learn more, see the
  [JDK release notes](https://www.oracle.com/java/technologies/javase/11-0-11-relnotes.html#JDK-8202343).

- Compatible with `MongoDB Database Tools 100.4.0`.

### Ops Manager Server 5.0.1

*Released 2021-08-05*

- Improves Log Collection Jobs.

- Adds a warning message when Ops Manager has less than 10GB of disk 
  space available.

- Fixes a bug that prevents clusters' Real-Time Panel tab from 
  loading properly.

- Disables the continuous backup page when AppDB monitoring is enabled.

- Updates the MongoDB Agent to 11.0.6.6981.

- Compatible with `MongoDB Database Tools 100.4.0`.

### Ops Manager Server 5.0.0

*Released 2021-07-13*

#### MongoDB Cloud Migration Service

Adds the MongoDB Cloud Migration Service. This service powers Live
Migrations from Ops Manager or MongoDB Cloud Manager to MongoDB Atlas. The service runs
when you use the Live Migration wizard in MongoDB Atlas. After preparing a
target cluster in Atlas, provisioning a migration host in
Ops Manager, and linking your Ops Manager or MongoDB Cloud Manager organization to your
MongoDB Atlas organization, you can launch a Live Migration process in
MongoDB Atlas for an existing cluster in Ops Manager or MongoDB Cloud Manager, and migrate
all data from the source cluster to a target cluster in Atlas.
You can also migrate a MongoDB Community to MongoDB Atlas.

For more information, see lm-workflow in the
Atlas documentation.

To live migrate your deployment from Ops Manager or MongoDB Cloud Manager to
Atlas, see migrate-to-atlas.
To live migrate your MongoDB Community deployments to Atlas
using Ops Manager, see migrate-community-to-atlas.

#### MongoDB Cluster Management

- Supports managing, monitoring, and backing up MongoDB 5.0 deployments.

- Highlights deployments running without best-practice security
  features enabled (TLS (Transport Layer Security), authentication, authorization) in the
  **Clusters** page.

- Highlights changes to MongoDB clusters that result in processes
  restarts in the **Review and Deploy** confirmation modal.

#### Backup

- Improves snapshot resiliency to transient failures for clusters
  running MongoDB 4.2 or later.

- Improves performance for snapshots running MongoDB 4.2 or later.

- Improves metadata management and handling of large files.

#### Activity Feed

- Increases granularity of date filters in Activity Feed to the hour. 

- Adds ability for admins to download a JSON (Javascript Object Notation) view of the Activity
  Feed.

- Adds categories of events for improved filtering of Activity Feed
  items. These improvements exist in both the console and the API (Application Programming Interface).

#### Deprecated Language

- Changes all instances of the following terms in the activity feed,
  console, and API (Application Programming Interface) endpoint URL (Uniform Resource Locator)\s:

  - **Whitelist** or **Blacklist** to **Access List**
  - **slaveDelay** to **secondaryDelaySecs**

  Make sure to update any application code or scripts with these
  updated labels to reflect this change.

#### Deactivated Personal API Keys

- Fully removes personal API (Application Programming Interface) keys. Use programmatic API keys 
  to access the API.

#### Performance Advisor

- Supports up to 200,000 logs.

- Doesn't cap logs read at 10 MB.

- Suggests removing redundant, unused, or hidden indexes.

#### Monitoring

Adds new hardware charts for system level memory, swap, and network
usage on RHEL Linux.

#### Kubernetes

Simplifies deploying Kubernetes MongoDB resources. This release adds a
wizard-like interface to generate configuration files in the Ops Manager
console. MongoDB Kubernetes Enterprise Operator
`improvements released` separately.

#### Ops Manager Packaging

- Signs Ops Manager packages with PGP.

- Supports Ops Manager services on RedHat Enterprise Linux version 8 on
  the ppc64le architecture.

#### Security

Disables TLS (Transport Layer Security) versions 1.0 and 1.1 by default.

#### MongoDB Agent

Updates the MongoDB Agent to 11.0.5.6967-1.
