<!-- Converted from release-notes/application.txt (reStructuredText). Includes are inlined. -->

# Ops Manager Server Changelog

## Ops Manager Server 7.0

   

### Ops Manager Server 7.0.23

*Released 2026-02-17*

### Improvements

- Updates the MongoDB Agent to 107.0.23.8832-1.
- Supports `MongoDB Database Tools 100.14.1`.
- Updates JDK to [jdk-17.0.18+8](https://adoptium.net/temurin/release-notes/?version=jdk-17.0.18+8).
- Adds support for [MongoDB Shell 2.6.0](https://github.com/mongodb-js/mongosh/releases).

### Bug Fixes

- Fixes the following CVE (Common Weakness Enumeration)\s:  

  - [CVE-2022-25883](https://nvd.nist.gov/vuln/detail/CVE-2022-25883)
  - [GHSA-c2qf-rxjj-qqgw](https://github.com/advisories/GHSA-c2qf-rxjj-qqgw)
  - [CVE-2024-10491](https://nvd.nist.gov/vuln/detail/CVE-2024-10491)
  - [CVE-2024-51999](https://nvd.nist.gov/vuln/detail/CVE-2024-51999)

### Ops Manager Server 7.0.22

*Released 2026-01-15*

### Improvements

- Releases MongoDB Agent 107.0.22.8822-1.
- Adds code reformatting hooks for Go source files.
- Re-enables the Agent to download `mongosh` on RHEL 9 s390x.
- Makes deadcode report when an entry in `ignored-deadcode.yml` cannot be matched.
- Upgrades the `bc-fips` library from version 1.0.2.5 to 1.0.2.6 and adds pre-flight 
  validations for certificate compatibility.
- Updates the Slack integration to leverage the latest supported Slack app.
- Addresses a security finding by updating the `qs` package to version 6.14.1.

### Bug Fixes

- Validates that `net.tls` parameters are removed when TLS is disabled.
- Introduces the following fixes related to certificate validation and security 
  vulnerabilities:

  - Adds a preflight check that scans the following customer certificates, when 
    present, and prevents Ops Manager from starting if any are affected by 
    [CVE-2025-8885](https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902025%E2%80%908885):

    - `mongodb.ssl.PEMKeyFile`
    - `mms.https.PEMKeyFile`
    - `mms.ldap.ssl.PEMKeyFile`
    - `mms.saml.ssl.PEMKeyFile`
    - `brs.queryable.pem`
    - `mongodb.ssl.CAFile`
    - `mms.https.CAFile`
    - `mms.ldap.ssl.CAFile`
    - `backup.kmip.server.ca.file`
    - `mms.saml.x509.cert`

  - Fixes the following CVEs:

    - [CVE-2025-8885](https://github.com/bcgit/bc-java/wiki/CVE%E2%80%902025%E2%80%908885)
    - [CVE-2024-29371](https://nvd.nist.gov/vuln/detail/CVE-2024-29371)
    - [CVE-2025-15284](https://nvd.nist.gov/vuln/detail/CVE-2025-15284)
    - [CVE-2025-58056](https://nvd.nist.gov/vuln/detail/CVE-2025-58056)
    - [CVE-2025-67735](https://nvd.nist.gov/vuln/detail/CVE-2025-67735)
    - [GHSA-fghv-69vj-qj49](https://github.com/advisories/GHSA-fghv-69vj-qj49)

### Ops Manager Server 7.0.21

*Released 2025-12-16*

### Improvements

- Updates the MongoDB Agent to 107.0.21.8817-1.
- Updates the Project Read Only role to grant access to the Real Time 
  metrics tab.
- Backports the `mms-automation` upgrade to go1.24 for ops-manager branches.
- Improves log rotation to handle files with incorrect permissions and prevent the 
  log rotator from becoming unresponsive.

### Bug Fixes

- Prevents agent versions from being sent back to Ops Manager when custom agent 
  download URLs are defined to reduce automation configuration size and prevent 
  max-size errors.
- Restores RHEL 7 RPM and tar.gz agent downloads in Ops Manager 7.0.
- Fixes the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2025-11226](https://nvd.nist.gov/vuln/detail/CVE-2025-11226)
  - [GHSA-25qh-j22f-pwp8](https://github.com/advisories/GHSA-25qh-j22f-pwp8)
  - [CVE-2025-64718](https://nvd.nist.gov/vuln/detail/CVE-2025-64718)

### Ops Manager Server 7.0.20

*Released 2025-12-08*

### Improvements

- Updates the MongoDB Agent to 107.0.20.8807-1.
- Implements a Telemetry report to collect and send 
  Ops Manager usage data to MongoDB, with controls to enable or disable telemetry 
  through the Ops Manager UI or API.
- Addresses [CVE-2025-12383](https://www.cve.org/CVERecord?id=CVE-2025-12383) 
  by updating the Jersey libraries to 3.1.10.

### Bug Fixes

- Fixes an issue where disabling LDAP (Lightweight Directory Access Protocol) authorization did not trigger a rolling 
  restart, ensuring proper configuration changes.
- Fixes a problem where requesting logs via the UI for BSON (Binary Javascript Object Notation) files could 
  generate unusable files due to BSON (Binary Javascript Object Notation) size errors.
- Fixes an issue that prevented modifying the custom configuration when the 
  `mms.mail.transport` setting is present.
- Fixes an issue where FTDC (full-time diagnostic data capture) logs generated through the Request Logs button in the Ops Manager UI were 
  corrupted and unusable, causing `bsondump` to fail with `invalid BSONSize` 
  errors.

### Ops Manager Server 7.0.19

*Released 2025-11-06*

### Improvements

- Updates the MongoDB Agent to 107.0.19.8805-1.
- Adds support for `MongoDB Connector for BI` 2.14.25.
- Updates JDK to [jdk-17.0.17+10](https://adoptium.net/temurin/release-notes/?version=jdk-17.0.17+10).
- Upgrades `golangci-lint` to version 2.5.0.
- Upgrades deprecated dependencies, including Puppeteer and Sinon packages.
- Tests and releases BI Connector 2.14.25 in MongoDB Agent.
- Improves accuracy when the database path is not cleaned up after a restore operation.
- Improves the Ops Manager UI:

  - Adds an ellipsis dropdown menu for logs retrieval on `mongos` instances in sharded clusters.
  - Ensures the shutdown dialog for replica sets shows all impacted servers.
  - Specifies the button type for table paginator buttons to prevent unintended form submissions during navigation.
  - Shows restore job IDs in the `CONCURRENT_RESTORES_JOB_IDS` error code for improved error clarity.
  - Displays a warning on the Deployment page regarding unsupported hosts.
  - Improves messaging for slow query threshold updates by removing hardcoded values.
  - Removes the OIDC (OpenID Connect) `Preview` tag as OIDC (OpenID Connect) support is now generally available (GA).

- Includes the source error in log messages when unable to retrieve the FCV (Feature Compatibility Version) from MongoDB.
- Collects process CPU metrics when using a Host Mappings alias.
- Admin Settings API now includes LDAP validation for API use cases.
- Introduces the following features for managing deprecated deployments:

  - Adds a REST API for retrieving information about deprecated deployments.
  - Adds an admin page for managing deprecated deployments.
  - Adds system alerts for deprecated hosts.

- Introduces a feature flag for unsupported host monitoring.
- Public API now supports updating project settings.

### Bug Fixes

- Performs Atlas maintenance actions sequentially to prevent downtime resulting from replication issues.
- Adds info-level logging for different `RollingRestartArgs` to assist in troubleshooting.
- Fixes the time range filter's functionality in the Ops Manager Activity Feed tab.
- Allows new backups to start for unmanaged clusters.
- Fixes a race condition when starting or finishing a clustershot in sharded clusters.
- Corrects the misalignment of the Prometheus integration Copy button in the Ops Manager UI.
- Fixes an issue where the `UnsupportedMongoDbVersionCheck` fails due to missing host version.
- Addresses cases where invalid metric types prevent the global alert configuration from rendering.
- Treats missing migrations as pending to prevent Ops Manager from becoming stuck in upgrade mode during updates.
- Fixes the following CVE (Common Weakness Enumeration):

  - [CVE-2025-59343 (tar-fs)](https://nvd.nist.gov/vuln/detail/CVE-2025-59343).

### Ops Manager Server 7.0.18

*Released 2025-09-10*

### Improvements

- Updates the MongoDB Agent to 107.0.18.8784-1
- Supports MongoDB Database Tools 100.13.0
- Redacts sensitive fields (passwords, keys, etc.) in the Public API, including
  new endpoints `GET /automationConfig/noSecrets` and `PUT /automationConfig/noSecrets`
  to receive and partially update a redacted version of the existing `/automationConfig`
  endpoint
- Makes additional SAML fields (Service Provider Base URL, Entity ID, and SLS/logout
  redirect) configurable on the Admin Configuration page
- Adds a `New Server` option in the `Hostname` dropdown for Standalone deployments; includes search
- Logs `mongod.lock` contents in unexpected cases
- The MongoDB Agent detects the absence of the AVX instruction set and handles failures gracefully
- For ThirdParty, `GetValidRestoreTargets` for replica sets that were previously shards now uses
  `hostCluster.getReplicaSetName` for proper identification

### Bug Fixes

- `AdjustRoles` now accounts for role dependencies when creating roles
- Fixes a memory spike when iterating the logs directory by introducing chunked iteration and logging
- Diagnostics archive per group now includes disabled hosts
- Fixes generation of outdated Java dependencies
- Upgrades deprecated `@babel/plugin-proposal-*` dependencies to recommended packages
- Removes deprecated `@types/react-select` and `@types/classnames` dependencies
- Improves Javadoc for the `CanonicalHost` class
- Bell icon now links to the Alerts page instead of the Activity Feed
- Disables TRACE requests for the embedded Prometheus server
- Fixes the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2025-5115](https://nvd.nist.gov/vuln/detail/CVE-2025-5115)
  - [CVE-2025-55163](https://nvd.nist.gov/vuln/detail/CVE-2025-55163)

### Ops Manager Server 7.0.17

*Released 2025-08-08*

### Improvements

- Updates the MongoDB Agent to 107.0.17.8771-1.
- Supports `MongoDB Connector for BI` 2.14.24.
- Updates JDK to `jdk-17.0.16+8`.
- Updates `mongosh` to 2.5.6.
- Improves MongoDB Usage logic to represent licensing needs more
  accurately. Splits RAM Pool category into RAM Pool (Prod) and RAM Pool
  (Test/QA).
- Implements skip migration when Ops Manager version is not changing to
  improve efficiency.
- Adds MongoDB Agent, Automation, and UI support for MongoDB on RHEL 9
  (s390x).
- Backports and aligns golangci-lint configuration across OM branches.
- Removes `AutomationConfigDeploymentView` and `Mapper` for improved
  code clarity.
- Creates a new JSON Based Redaction Logic framework.
- Adds timeout to SMTP server connections to prevent hangs and improve
  error diagnosis.
- Updates Ops Manager logic to use single task release-distros in
  Evergreen.
- Updates PACKAGE_OPS_MANAGER to stub out `sign_artifact` when
  Garasign credentials aren't available, allowing patch builds without
  Garasign credentials.
- Generates new certs for KMIP server and re-enables related tests.
- Improves shard/replset startup with
  `wiredTigerSkipTableLoggingChecksOnStartup`.

### Bug Fixes

- Fixes a bug where `auditLog.auditEncryptionKeyIdentifier` could not
  be set through the UI.
- Fixes a bug where the Miscellaneous Ops Manager Config tab always showed
  a "Changes you made may not be saved" warning, even when no changes
  were made.
- Fixes an Agent bug that caused crashes when modifying a process's
  storage fields. Now includes ENCRYPTION_CIPHER_MODE in removed fields
  for ephemeral standalone runs to prevent crashes.
- MongoDB Agent now ensures that global update operations for PSSSA
  replica sets do not attempt to take down two data bearing nodes at
  once.

- Fixes the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2025-48924](https://nvd.nist.gov/vuln/detail/CVE-2025-48924) 
  - [CVE-2025-48976](https://nvd.nist.gov/vuln/detail/CVE-2025-48976) 
  - [CVE-2025-7783](https://nvd.nist.gov/vuln/detail/CVE-2025-7783) 

### Ops Manager Server 7.0.16

*Released 2025-07-03*

- Updates the MongoDB Agent to 107.0.16.8756-1.
- Adds support for `MongoDB Connector for BI` 2.14.23.
- Supports MongoDB Database Tools 100.12.2.
- Updates JDK to `jdk-17.0.15+6`.
- Updates `mongosh` to 2.5.3.
- Customizable webhooks – Adds support for custom headers and body templating in project and global alert webhooks.
- Improves logging for the `webhooksImproved` agent job to aid debugging.
- Enhanced validation and handling for Oplog, Shard, and Backup workflows, including:
  - Updated `ThirdPartyJob` cluster name to reflect name changes.
  - Oplog snapshot now waits before failing if no oplogs are available.
  - Improved handling of duplicate oplog metadata.
  - Cleanups of snapshot and `backup_cursor_file_list` now occur only during the appropriate lifecycle events.
  - Better handling of topology changes and preferred node processing in backup workflows.
- `ThirdPartyBackup` now updates LastTopology if the cluster topology changes after management but before preferredNodesSet.
- Enhanced logging for agent jobs and backup workflows.
- Improved backup daemon configuration so `emptyDaemonFilter` arrays match as intended.
- Cache S3 custom keystore creation and reduce excessive log calls in OEM S3 operations.
- Added and improved validations in Automation and various workflows.

#### Bug Fixes

- Added validation that head directory ends in a slash.
- Auto extends the queryable restore job expiry to prevent queryable restore expiry mid-restore.
- Update `automationConfig` validations for `lastErrorMode` and `lastErrorDefaults` to eliminate false positives due to Map ordering.
- Make KMIP proxy’s `custodian.Stop()` wait till server is fully stopped.
- Fix errors verifying TLS connections on stand-alone hosts.
- Prevent key rotation via the OM UI when a kmip.keyIdentifier is specified.
- Fix for `passVersion` mismatch when resetting a password, now updates version as required.

- Fixes the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2025-27789](https://nvd.nist.gov/vuln/detail/CVE-2025-27789).
  - [CVE-2025-32996](https://nvd.nist.gov/vuln/detail/CVE-2025-32996).
  - [CVE-2025-32997](https://nvd.nist.gov/vuln/detail/CVE-2025-32997).
  - [CVE-2025-30360](https://nvd.nist.gov/vuln/detail/CVE-2025-30360).
  - [CVE-2025-30359](https://nvd.nist.gov/vuln/detail/CVE-2025-30359).
  - [CVE-2025-48734](https://nvd.nist.gov/vuln/detail/CVE-2025-48734).

### Ops Manager Server 7.0.15

*Released 2025-04-03*

- Updates the MongoDB Agent to 107.0.15.8741-1.
- Releases `mongosh` 2.4.0 to Ops Manager.
- Adds support for `MongoDB Connector for BI` 2.14.22.
- Compatible with `MongoDB Database Tools 100.11.0`.
- Upgrades Jetty library to 11.0.25.
- Reduces the maximum session length (`mms.session.maxHours`)
  from two months to one week to improve security.
- Adds a new `mms.cookies.sameSite` setting to configure cookie behavior:

  - `Lax` allows top-level navigation cookies.
  - `Strict` restricts cookies to same-site requests.
  - `None` permits all cross-site cookies over HTTPS.

  All cookies are now `httpOnly` and marked as secure when
  using HTTPS.

- Adds support for configuing multiple passwords in `security.ldap.bind.queryPassword`
  so that users can ensure that MongoDB won't disconnect from LDAP after a restart when 
  performing an LDAP credential rotation. To learn more, see security-ldap.

- Improves handling of misconfigured core/max pool sizes.

- Adds the ability for Ops Manager to recognize dashes (`-`) in deployment names.

- Exports all stored telemetry data into the related files in the diagnostic logs.

- Improves error handling to prevent `mongodb-mms-stop` from crashing 
  with `Mongodb-mms-backup-daemon` errors when the pid file doesn't exist.

- Fixes the following issues:

  - Fixes possibly innacurate FCV (Feature Compatibility Version) change timestamp warnings.
  - Fixes incorrect redirection to an Identity Provider\s entity ID for 
    Identity Provider\s that don't have single logout (SLO) configured.

    After logging out of Ops Manager, users are now reminded to also log out of the
    Identity Provider to complete the logout process.

  - Fixes  inaccurate restore job statuses when cancelled.

  - Fixes an issue where the user interface passes incorrect values
    for `pemFilePwd` for the `verifyTLSCertificate` job.

  - Fixes an issue where the MongoDB Agent ignores the Windows 
    MongoDB Agent Certificate File information and uses the Linux path instead.

  - Fixes a broken documentation link for Create API Key > Add Access List Entry.

  - Fixes saving custom parameter settings due to `mms.mail.transport`.

- Fixes the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2021-32050](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2021-32050).
  - [CVE-2023-26159](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2023-26159).
  - [CVE-2023-42282](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2023-42282).
  - [CVE-2024-11831](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-11831).
  - [CVE-2024-12905](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-12905).
  - [CVE-2024-21536](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-21536).
  - [CVE-2024-21538](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-21538).
  - [CVE-2024-28849](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-28849).
  - [CVE-2024-29180](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-29180).
  - [CVE-2024-37890](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-37890).
  - [CVE-2024-47535](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-47535).
  - [CVE-2025-22868](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2025-22868).
  - [CVE-2025-22869](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2025-22869).
  - [CVE-2025-22870](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2025-22870).
  - [CVE-2025-24970](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2025-24970).
  - [CVE-2025-27789](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2025-27789).
  - [CVE-2025-30204](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2025-30204).

### Ops Manager Server 7.0.14

*Released 2025-01-23*

- Adds support for `MongoDB Connector for BI` 2.14.21.

- Fixes the following issues:

  - Deployment IDs were not filtered out when multi-region backups are enabled.

  - Downloading logs could fail for systems that use 
    syslog.

### Ops Manager Server 7.0.13

*Released 2025-01-10*

- Updates the MongoDB Agent to 107.0.13.8702-1.

- Adds support for `MongoDB Connector for BI` 2.14.19.

- Updates the release infrastructure:

  - Updates the password hashing algorithm to `PBKDF2-SHA512`. 
    Migrates old passwords automatically without any user impact.
  - New passwords can't exceed 256 characters to avoid a potential 
    resource exhaustion attack if users enter very long passwords.
  - Users with passwords longer than 256 characters must migrate their 
    password.

- New `mms.user.passwordHashIterations` custom configuration 
  variable for Ops Manager to dynamically modify the number of iterations 
  for the algorithm.

- Adds the following fields to the  snapshot APIs: `machineId`, `name`, `completedTime`, 
  `fcv`, and `replicaState`.

- Hardens the algorithm used for two-way encryption in AppDB. 

- Adds a trigger so that changes to the feature compatibility version (FCV) triggers
  a snapshot.

- Adds an AppDB health check to the Ops Manager upgrade process to ensure a successful upgrade.

- Adds `clusterID` to the Ops Manager logs for each snapshot.

- Includes deleted groups in the diagnostic archive for better debugging.

- Improves error handling for the `FileSystemSnapshotStore` in the event the 
  job directory does not exist.

- Adds 320 character limit for Email Address and Mobile Phone Number 
  fields in the user profile UI.

- Adds the ability to cancel a failed queryable restore for sharded clusters.

- Fixes [CVE-2024-52046](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-52046).

#### Bug Fixes

Fixes the following issues:

- Arbiter nodes caused the 
  Edit Namespace Filter UI option to not appear.

- Labels did not appear on the 
  Backup Job Config page in the Admin UI.

- Upgrades from MongoDB 6.0.x to 7.0.x with OIDC (OpenID Connect) configured 
  and a pinned FCV became stuck.

- Configuring or updating Blockstore Max Capacity (GB)
  in the UI caused an error.

- `bytesReclaimed` reported compressed size for filesystems
  instead of showing `fileSize`.

- The MongoDB Agent tried to set the OIDC (OpenID Connect) parameter on 
  MongoDB 7.x clusters with FCV 6.0 set.

- The MongoDB Agent downloaded incorrect `MongoDB Connector for BI` versions on certain platforms.

- `.tmp` files were left behind in Hybrid mode.

- Unsupported mail transport protocol appeared as an option in the Admin UI.

- The MongoDB Agent could incorrectly report that the goal state was reached while
  encountering a transient error.

- The Admin UI redirected back to the logs page after viewing.

- The link to the MongoDB Deployment Authentication Mechanism documentation in 
  the UI was incorrect.

### Ops Manager Server 7.0.12

*Released 2024-10-31*

- Updates JDK to `jdk-17.0.13+11`.
- Supports Workload Identity Federation on top of the already existing Workforce Identity Federation. 
- Supports configuring separate SAML signature validation for responses and assertions so that only one is 
  required through the `mms.saml.signedAssertions` and `mms.saml.signedMessages` settings.
- Supports ability to set a custom idle session timeout using new application settings, Idle Session Timeout Mode and Idle Session Timeout Max Minutes.
- Supports taking on-demand snapshots in addition to scheduled snapshots.
- Removes the Ops Manager version number from the login page if you set `mms.security.show.om.version` to false.
- Updates the MongoDB Agent to 107.0.12.8669-1.
- Adds support for `MongoDB Connector for BI` 2.14.17.
- Upgrades Jetty library to 11.0.23.
- Fixes an issue where the MongoDB Agent gets stuck because indexes are set to the `CANCEL` action.
- Fixes [CVE-2024-8184](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-8184).

### Ops Manager Server 7.0.11

*Released 2024-09-05*

- Updates the MongoDB Agent to 107.0.11.8645-1.
- Adds support `MongoDB Connector for BI` 2.14.15.
- Compatible with `MongoDB Database Tools 100.10.0`.
- Removes the MongoDB Agent dependencies on the `redhat-lsb-core` 
  package for RHEL and `lsb-release` pacakge for Debian.  
- Ensures that Ops Manager retains at least one snapshot regardless of expiration schedule.
- Fixes the following issues:

  - Upgrades from Ops Manager 6 to Ops Manager 7 fail due to a missing field
    in the SNMP (Simple Network Management Protocol) alert configuration used for upgrade validation.
  - Diagnostics archive shows incorrect free space for File System snapshot store.
  - `DeploymentId` not displayed for shards with regional backup enabled.
  - Potential error when saving updates to oplog or snapshot stores due to `DeploymentId` validation.
  - Possible shutdown loop when KMIP rotation and initial sync run concurrently.

### Ops Manager Server 7.0.10

*Released 2024-08-01*

- Updates the MongoDB Agent to 107.0.10.8627-1.
- Updates JDK (Java Development Kit) to `jdk-17.0.12+7`. 
- Improves metadata clean up when terminating backup jobs.
- Fixes [CVE-2023-45288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45288)
- Fixes the following issues:

  - Creating a new regional backup errors on internal sync store assignment. 
  - Agent potentially crashes during restart due to a race condition.

### Ops Manager Server 7.0.9

*Released 2024-07-18*

- Updates the MongoDB Agent to 107.0.9.8621-1.
- Adds support for `MongoDB Connector for BI` 2.14.14.
- Compatible with `MongoDB Database Tools 100.9.5`.
- Improves validation for regional backup
  configurations. 
- Fixes the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2024-5157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-5157).
  - [CVE-2024-5159](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-5159).
  - [CVE-2024-5160](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-5160).
  - [CVE-2024-5493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-5493).
  - [CVE-2024-5494](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-5494).
  - [CVE-2024-5495](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-5495).
  - [CVE-2024-5496](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-5496).
  - [CVE-2024-6100](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-6100).
  - [CVE-2024-6103](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-6103).
  - [CVE-2024-24786](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-24786).

- Fixes a potential restore validation error.
- Fixes a bug where altering the snapshot time skips longer retained snapshots.

### Ops Manager Server 7.0.8

*Released 2024-06-27*

- Updates the MongoDB Agent to 107.0.8.8615-1.
- Adds support for `MongoDB Connector for BI` 2.14.13.
- Improves a snapshot's ability to use the same node from a previous
  snapshot.
- Improves the warning when file system stores doesn't exist.
- Ensures that a groom job has enough space to run before starting.
- Fixes the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2024-3156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-3156).
  - [CVE-2024-5831](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-5831).
  - [CVE-2024-5832](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-5832).
  - [CVE-2024-22017](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-22017).

- Fixes an issue where the HTTP (Hypertext Transfer Protocol) transport for automation didn't always
  use the configured TLS (Transport Layer Security) configuration. 
- Improves the redaction of sensitive fields.

### Ops Manager Server 7.0.7

*Released 2024-06-06*

- Updates the MongoDB Agent to 107.0.7.8596.
- Fixes an issue that could cause termination jobs to timeout due to unassigned blockstores.
- Fixes an issue where required backup job fields could become null.

### Ops Manager Server 7.0.6

*Released 2024-05-10*

- Updates the MongoDB Agent to 107.0.6.8587-1.
- Supports parsing multiple certificates, or a chain, from PEM
  files for S3-compatible storage backup store configuration.
- Adds alert to verify `defaultRWConcern` of the AppDB and other
  backing databases. 
- Fixes the following issues:

  - Backup job logs for a specific logger didn't appear correctly in the
    UI. 
  - ObjectId fields in snapshot history rendered incorrectly.

### Ops Manager Server 7.0.5

*Released 2024-05-02*

- Updates the MongoDB Agent to 107.0.3.8581-1.
- Releases `mongosh` 2.2.4 to Ops Manager. To learn more, see `mongosh` 
  Release Notes.
- Updates JDK (Java Development Kit) to `jdk-17.0.11+9`. 
- Displays S3-compatible storage `oplog store` databases as a
  backing database in the Admin Overview tab.
- Adds additional diagnostics information related to backup speed in a
  separate download ingestible format from diagnostic archive. 
- Adds additional snapshot history metadata for block tracking,
  incrementality for data and indexes, transfer speed, and duration in
  the Admin UI and diagnostic archives.
- Increases the number of snapshots retained to 60 snapshots per cluster
  for the snapshot history metadata.
- Fixes an issue with backup configuration daemon filter for deleted
  daemons. 
- Fixes [CVE-2024-29025](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-29025).

### Ops Manager Server 7.0.4

*Released 2024-04-04*

- Releases `mongosh` 2.2.3 to Ops Manager. To learn more, see `mongosh` 
  Release Notes.
- Supports enabling and configuring regional backups.
- Supports `net.tls.clusterAuthX509` parameter in MongoDB 7.0 for
  `clusterAuthMode` set to `x509`. 
- Adds API support for project level MongoDB log rotation settings. 
- Adds ability for backup to automatically configure an improved default
  blocksize for mongo blockstores.
- Adds automation support for at-rest encryption of
  audit logs in MongoDB
  6.0 and later versions.  
- Enhances logging for MongoDB blockstores groom progress.
- Fixes the following issues:

  - Inactive accounts prevented users from navigating to the continuous backup page.
  - Restore would fail in existing deployments if credentials version didn't match.
  - Restores couldn't progress due to a DOWN host.
  - The `mongodVersion` in the backup jobs collection doesn't update correctly.

- Fixes [CVE-2023-33546](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2023-33546)
- Fixes [CVE-2024-22201](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-22201)

### Ops Manager Server 7.0.3

*Released 2024-03-07*

- Updates the MongoDB Agent to 107.0.3.8550-1.
- Fixes a bug where Ops Manager upgrades might become stuck
  when webhook notifications are configured due to `webhook_url` 
  not populating correctly.
- Adds MongoDB Agent support for Ubuntu 20.04 and RHEL 9 on ARM.
- Fixes a bug where the MongoDB Agent wasn't considering all of 
  a certificate's SANs (Subject Alternative Names).
- Adds the ability to edit WiredTiger job setting, number of 
  backup workers, and bandwidth for backups in the
  admin-console.
- Adds the ability for Ops Manager to automatically choose the
  number of backup workers based on available CPU cores and
  memory.
- Fixes [CVE-2023-52428](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2023-52428)
- Fixes [CVE-2024-25710](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-25710)
- Fixes [CVE-2024-26308](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2024-26308)
- Releases `mongosh` 2.1.5 to Ops Manager. To learn more, see `mongosh`
  `Release Notes`.
- Fixes an issue where Ops Manager inaccurately reported the 
  network bytes out metric that appears in the 
  System Network chart. This release resets this metric and 
  the previous values no longer appear. To learn more, see 
  review-available-metrics and system-disk-alerts.

### Ops Manager Server 7.0.2

*Released 2024-02-01*

- Updates the MongoDB Agent to 107.0.2.8531.
- Updates JDK (Java Development Kit) to `jdk-17.0.10+7`. 
- Adds MongoDB Agent support for Debian 12.
- Adds support for deploying Ops Manager on Debian 12.
- Adds ability to configure the `net.tls.clusterCAFile` parameter. 
- Adds additional snapshot metrics to the snapshot summary table.
- Adds ability to track restore block download performance.
- Improves MongoDB and S3-compatible blockstore snapshot performance for
  large files through enhanced memory utilization.
- Improves the agent's ability to retry for more blockstore errors.
- Fixes the following bugs:

  - DBUsage API endpoint issue that affected totalCount, pageNum,
    filtering and pagination in the UI.
  - `Oplog Behind` warning could be displayed for non-active shards.
  - `LOW_APP_DB_FREE_SPACE_PERCENT` alert was not working correctly.
  - Servers might display stale statuses in the Ops Manager UI.
- Removes ability to delete a project that has 
  managed deployments.

### Ops Manager Server 7.0.1

*Released 2024-01-08*

**Important:**

If you're using MongoDB 7.0.0 to 7.0.4, upgrade to Ops Manager 7.0.1
or later before upgrading to MongoDB 7.0.5.

- Updates the MongoDB Agent to 107.0.0.8507.
- Bumps the minimum required MongoDB Agent version for Ops Manager 7.0
  to 107.0.0.8506-1. You must 
  upgrade to this version of the MongoDB Agent to allow clusters 
  using OIDC (OpenID Connect) to continue functioning after upgrading to MongoDB 7.0.5.
- Fixes a bug where clusters on MongoDB 7.0.0 to 7.0.4 using OpenID
  Connect authentication 
  fail to properly upgrade to MongoDB 7.0.5.

### Ops Manager Server 7.0.0

*Released 2024-01-04*

**Important:**

If you're using MongoDB 7.0.0 to 7.0.4, upgrade to Ops Manager 7.0.1
or later before upgrading to MongoDB 7.0.5.

- Updates the MongoDB Agent to 107.0.0.8490-1.

#### MongoDB Cluster Management

- Supports managing, monitoring, and backing up MongoDB 7.0 deployments.
- Supports MongoDB 7.0 as a deployment option.

#### Backup

- Exposes performance and snapshot metrics to admins.

  - Admins can now use Prometheus
    to view metrics graphs and query newly created collections in the 
    admin-console.

#### Alerting

- Removes support for SNMP (Simple Network Management Protocol) alerts. 

  - You can monitor your clusters with Ops Manager instead. To
    learn about other alert options, see third-party-integrations.

- Redacts third-party credentials.

  - Ops Manager redacts credentials for third-party metrics and alert integrations 
    when you view or edit an alert through the UI or query third-party 
    integration settings through the API (Application Programming Interface). 

    You can still edit these credentials. We recommend that you store these credentials outside of Ops Manager.  

#### Automation

- Adds support for enabling OIDC authentication through an IdP (Identity Provider) that supports OIDC (OpenID Connect), such as 
  Microsoft Entra ID, Okta, or Ping Identity.
- Replaces the target of the `/var/lib/mongodb-mms-automation/bin` symlink. This symlink now points to the 
  latest downloaded version of `mongosh`. In the previous releases, this symlink pointed to the latest 
  MongoDB version in the `/bin` folder. This change ensures that you always use the newest downloaded 
  `mongosh` version in all scripts for your deployments. 

#### Migration

- Removes support for the MongoDB Cloud Migration Service in Ops Manager. 
  If you need to use push-based migrations to migrate your 
  deployments to MongoDB Atlas, you can use the Cloud Migration Service in MongoDB Cloud Manager.

#### User Interface

- Removes support for the Manage Sharded Collections UI. 

  - Removes the ability to shard a collection, 
    manage the sharded cluster balancer, and manage sharded 
    zones through the UI. You still have full control
    of your sharded cluster available through the command line 
    by using `mongosh`.

- Removes support for Internet Explorer 11.

#### Ops Manager Platform Support

- Adds support for deploying Ops Manager on RedHat Enterprise Linux 9 on x86_64 architectures.
- Adds support for deploying Ops Manager on Ubuntu 22.04 on x86_64 architectures.
- Adds support for deploying Ops Manager on Amazon Linux 2023.
- Adds support to fix broken `rpm` packages for Ops Manager versions 6.0.0, 6.0.1, and 6.0.2 
  containing incorrect version information that could cause standard 
  upgrades to fail. If upgrading from any of these versions to 
  version 6.0.3 or greater, upgrade the package using the 
  `--oldpackage` flag:

  ```sh
  sudo rpm -Uvh --oldpackage mongodb-mms-<version>.x86_64.rpm
  ```

- Removes Ops Manager support for Debian 10.
- Removes Ops Manager support for Ubuntu 18.04 LTS.
- Deprecates Ops Manager support for RedHat Enterprise Linux 7.
- Deprecates Ops Manager support for SUSE Linux Enterprise Server 12.
- Deprecates Ops Manager support for Ubuntu 20.04 LTS.

#### Automation Platform Support

- Adds MongoDB Agent support for RedHat Enterprise Linux 9 on x86_64 and ARM architectures.
- Adds MongoDB Agent support for Ubuntu 22.04 on x86_64 and ARM architectures.
- Adds MongoDB Agent support for Amazon Linux 2023.
- Removes MongoDB Agent support for Debian 10.
- Removes MongoDB Agent support for Ubuntu 18.04 LTS.
- Deprecates MongoDB Agent support for RedHat Enterprise Linux 7.
- Deprecates MongoDB Agent support for SUSE Linux Enterprise Server 12.
- Deprecates MongoDB Agent support for Ubuntu 20.04 LTS.

## Ops Manager Server 6.0

### Ops Manager Server 6.0.27:

*Released 2025-01-30*

**Important:** Ops Manager 6.0 EOL

This is the final release of Ops Manager 6.0. Ops Manager 6.0 has reached [end of life (EOL)](https://www.mongodb.com/legal/support-policy/lifecycles).
Upgrade to at least Ops Manager 7.0 immediately to keep your Ops Manager support.

- Updates the MongoDB Agent to 12.0.35.7911-1.
- Adds support for `MongoDB Connector for BI` 2.14.21.
- Updates JDK to `jdk-11.0.26+4`.
- Fixes an issue so that the MongoDB Agent downloads the correct `MongoDB Connector for BI`
  versions for all platforms.
- Fixes the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2024-10229](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-10229)
  - [CVE-2024-10487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-10487)
  - [CVE-2024-10827](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-10827)
  - [CVE-2024-11110](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-11110)
  - [CVE-2024-12053](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-12053)
  - [CVE-2024-12798](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-12798)
  - [CVE-2024-21534](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-21534)
  - [CVE-2024-47535](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-47535)
  - [CVE-2024-52046](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-52046)
  - [CVE-2025-0436](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-0436)

### Ops Manager Server 6.0.26:

*Released 2024-10-31*

- Updates the MongoDB Agent to 12.0.34.7888-1.
- Adds support for `MongoDB Connector for BI` 2.14.17.
- Updates JDK to `jdk-11.0.25+9`.
- Improves the metadata clean up when you terminate a backup job.
- Fixes the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2024-6291](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6291)
  - [CVE-2024-6292](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6292)
  - [CVE-2024-6293](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6293)
  - [CVE-2024-6773](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6773)
  - [CVE-2024-6778](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6778)
  - [CVE-2024-6779](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6779)
  - [CVE-2024-6991](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6991)
  - [CVE-2024-7966](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7966)
  - [CVE-2024-7969](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7969)
  - [CVE-2024-7970](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-7970)
  - [CVE-2024-8184](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-8184)
  - [CVE-2024-8193](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-8193)
  - [CVE-2024-8198](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-8198)
  - [CVE-2024-8362](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-8362)
  - [CVE-2024-8636](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-8636)
  - [CVE-2024-8904](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-8904)
  - [CVE-2024-9120](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-9120)
  - [CVE-2024-9121](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-9121)
  - [CVE-2024-9123](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-9123)
  - [CVE-2024-9602](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-9602)

### Ops Manager Server 6.0.25:

*Released 2024-08-08*

- Compatible with `MongoDB Database Tools 100.10.0`.
- Updates the MongoDB Agent to 12.0.33.7866-1.
- Updates Go to 1.22 to build the MongoDB Agent.
- Adds support for `MongoDB Connector for BI` 2.14.14.
- Removes the requirement that RHEL
  OS (Operating System) must include the `redhat-lsb-core` 
  package. 
- Removes the requirement that a Debian installation must include the
  `lsb-release` package. To learn more, see [lsb-release](https://packages.debian.org/sid/lsb-release). 
- Fixes the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2021-4279](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2021-4279)
  - [CVE-2023-22467](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-22467)
  - [CVE-2023-45288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45288)
  - [CVE-2024-37298](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-37298)

- Updates JDK to `jdk-11.0.24+8`.
- Fixes an issue so that a race condition no longer causes an agent to 
  crash during restart.

### Ops Manager Server 6.0.24:

*Released 2024-07-12*

- Compatible with `MongoDB Database Tools 100.9.5`.
- Adds support for `MongoDB Connector for BI` 2.14.13.
- Updates the MongoDB Agent to 12.0.32.7851-1.
- Releases `mongosh` 2.2.4 to Ops Manager. To learn more, see `mongosh`
  `Release Notes`.
- Uses server-side random sampling to distribute data points in
  Profiler more evenly across the
  scatterplot.
- Displays S3 Oplog Store DBs as a backing DB in the Admin 
  interface's Overview tab.
- Provides additional diagnostics information related to backup speed in 
  a separate download format from Diagnostic Archive.
- Updates snapshot history to include additional metadata for block tracking, 
  incrementality for data and indexes, transfer speed, and duration in the 
  Admin interface and Diagnostic Archive.
- Updates snapshot history from 20 to 60 snapshots for each cluster.
- Adds API support for project level MongoDB log rotation
  settings.
- Fixes the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2024-3156](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-3156)
  - [CVE-2024-5157](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5157)
  - [CVE-2024-5159](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5159)
  - [CVE-2024-5160](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5160)
  - [CVE-2024-5493](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5493)
  - [CVE-2024-5494](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5494)
  - [CVE-2024-5495](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5495)
  - [CVE-2024-5496](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5496)
  - [CVE-2024-5831](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5831)
  - [CVE-2024-5832](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-5832)
  - [CVE-2024-6100](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6100)
  - [CVE-2024-6103](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-6103)

- Fixes a potential restore validation error.
- Fixes a bug where the backup configuration `daemon` 
  filter appears incorrectly for removed hardware.
- Fixes a bug where a specific logger doesn't appear correctly in the UI for backup job logs.
- Fixes a bug where the objectid field in snapshot history renders incorrectly.
- Resolves a `NullPointerException` from bad `hostInfo`.
- Fixes a bug where altering the snapshot time skips longer retained snapshots.
- Fixes a bug where unassigned `blockstores` 
  terminate backup jobs to timeout.
- Fixes a bug where snapshots in the process of restore are groomed.

### Ops Manager Server 6.0.23:

*Released 2024-04-04*

- Fixes the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2023-34062](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-34062)
  - [CVE-2023-3635](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-3635)
  - [CVE-2023-44483](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44483)
  - [CVE-2023-51775](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-51775)
  - [CVE-2023-52428](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-52428)
  - [CVE-2024-22201](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-22201)
  - [CVE-2024-25710](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-25710)
  - [CVE-2024-26308](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2024-26308)

- Updates JDK to `jdk-11.0.22+7`.
- Releases `mongosh` 2.1.5 to Ops Manager. To learn more, see `mongosh`
  `Release Notes`. 
- Supports automating deployments on RedHat Enterprise Linux 9 ARM architectures.
- Adds API support for project level MongoDB log rotation settings.
- Adds ability for backup to automatically configure an improved default
  blocksize for mongo blockstores.
- Enhances logging for MongoDB blockstores groom progress.
- Improves MongoDB and S3-compatible blockstore snapshot performance for
  large files through enhanced memory utilization. 
- Supports tracking restore block download performance.
- Supports editing WiredTiger job setting, number of backup workers, and
  bandwidth for backups in the Administration Console. 
- Automatically chooses the number of backup workers based on available
  CPU cores and memory. 
- Adds additional snapshot metrics to the snapshot summary table.
- Adds automation support for at-rest encryption of
  audit logs in MongoDB
  6.0 and later versions.
- Supports configuration of the `net.tls.clusterCAFile` parameter.
- Improves the agent's ability to retry for more blockstore errors.
- Fixes the following bugs:

  - Restore would fail in existing deployments if credentials version
    didn't match. 
  - Restores couldn't progress due to a DOWN host.
  - The `mongodVersion` in the backup jobs collection didn't update correctly.
  - LDAP version manifest URLs weren't constructed properly in local mode.
  - Enabling automation on a deployment might fail.
  - DBUsage API endpoint issue that affected totalCount, pageNum,
    filtering and pagination in the UI. 
  - `Oplog Behind` warning would be displayed for non-active shards.
  - `LOW_APP_DB_FREE_SPACE_PERCENT` alert wasn't working correctly.
  - Servers might display stale statuses in the Ops Manager UI.

### Ops Manager Server 6.0.22:

*Released 2024-01-04*

- Updates the MongoDB Agent to 12.0.30.7791.
- Fixes a bug where backups might default to the wrong storage engine.
- Fixes a bug where the MongoDB Agent might download the wrong binaries for certain 
  operating systems.

### Ops Manager Server 6.0.21:

*Released 2023-12-14*

- Updates the MongoDB Agent to 12.0.29.7785.

- Compatible with `MongoDB Database Tools 100.9.4`.
- Adds support for `MongoDB Connector for BI` 2.14.12.
- Adds the `backupJobsEnabledOnly` API (Application Programming Interface) parameter to indicate whether to 
  exclude `daemons` not enabled for backing up 
  databases from the API (Application Programming Interface) response. 
- Disallows setting your `logRotate` configuration to `reopen`
  if you've already configured log rotation
  by the MongoDB Agent in the UI.
- Fixes a bug where users in local mode 
  could not use the Validate LDAP Connection button when 
  configuring LDAP (Lightweight Directory Access Protocol) in the UI.
- Fixes a bug where a backup with namespace filtering 
  fails due to a file list error.
- Fixes a bug where a backup successfully restarts before an oplog store could be assigned.
- Fixes a bug where the Blockstore Minimum Block Size dropdown displays 
  incorrectly in the Admin UI.
- Fixes the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2023-45285](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45285)
  - [CVE-2023-39326](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-39326)

### Ops Manager Server 6.0.20:

*Released 2023-11-03*

- Updates JDK to `jdk-11.0.21+9`.
- Updates jetty to 10.0.17.
- Updates the MongoDB Agent to 12.0.28.7763.
- Compatible with `MongoDB Database Tools 100.9.0`.
- Updates `log4j-over-slf4j` to 1.7.36.
- Eliminates `fileSystemStore` alerts if you have no filesystem 
  stores configured.
- Fixes `Invalid cong` bug that occurred when you upgraded a managed 
  deployment with multiple tags.
- Fixes a bug that prevented S3 store deletion.
- Improves `SystemSpaceAlertChecks` to check all the members.
- Adds the hostname and port to the abort error log for a job.
- Releases `mongosh` 2.0.2 to Ops Manager. To learn more, see `mongosh`
  `Release Notes`.
- Adds support for automating deployments on RedHat Enterprise Linux 9 
  x86_64 architectures (with BI connector support).
- Adds support for automating deployments on Ubuntu 22.04 for both 
  x86_64 and ARM64/aarch64 architectures (with BI connector support).
- Adds support for running Ops Manager on RedHat Enterprise Linux 9 and 
  Ubuntu 22.04 for x86_64 architectures.
- Fixes the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2023-40167](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2023-40167)
  - [CVE-2023-36479](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2023-36479)
  - [CWE-611](https://cwe.mitre.org/data/definitions//611.html)
  - [CVE-2023-44487](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-44487)

### Ops Manager Server 6.0.19:

*Released 2023-10-05*

- Updates the MongoDB Agent to 12.0.27.7746.
- Releases `mongosh` 2.0.0 to Ops Manager. To learn more, see `mongosh`
  `Release Notes`.
- Compatible with `MongoDB Database Tools 100.8.0`.

### Ops Manager Server 6.0.18:

*Released 2023-09-07*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates the MongoDB Agent to 12.0.26.7740.
- Updates JDK to `jdk-11.0.20.1+1`.
- Compatible with `MongoDB Database Tools 100.8.0`.
- Includes `MongoDB Connector for BI` 2.14.10.
- Includes [MongoDB Shell](https://www.mongodb.com/docs/mongodb-shell/) 1.10.4.

### Ops Manager Server 6.0.17:

*Released 2023-08-03*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates the MongoDB Agent to 12.0.25.7724.
- Updates JDK to `jdk-11.0.20+8`.
- Compatible with `MongoDB Database Tools 100.7.4`.
- Fixes CVE-2023-4009: Privilege Escalation for `Project Owner`
  and `Project User Admin` roles in Ops Manager.

  - In MongoDB Ops Manager 6.0 prior to 6.0.17, an authenticated user with
    with `Project Owner` or `Project User Admin`
    access roles could generate an API key with the privileges of the
    `Organization Owner` role resulting in privilege escalation.
  - CVSS Score: 7.2.
  - CWE-648: Incorrect Use of Privileged APIs.

### Ops Manager Server 6.0.16:

*Released 2023-07-06*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates the MongoDB Agent to 12.0.24.7719.
- Upgrades [org.xerial.snappy:snappy-java](https://mvnrepository.com/artifact/org.xerial.snappy/snappy-java/1.1.10.1) to version 1.1.10.1.
- Compatible with `MongoDB Database Tools 100.7.3`.

### Ops Manager Server 6.0.15:

*Released 2023-06-15*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates the MongoDB Agent to 12.0.23.7711.
- Adds support for `MongoDB Connector for BI` 2.14.7.
- Updates Go to 1.19.9+ to address the following CVE (Common Weakness Enumeration)\s:

  - [CVE-2023-29400](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2023-29400)
  - [CVE-2023-24539](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2023-24539)
  - [CVE-2023-24540](https://cve.mitre.org/cgi-bin/cvename.cgi?name=/CVE-2023-24540)

- Compatible with `MongoDB Database Tools 100.7.0`.

### Ops Manager Server 6.0.14

*Released 2023-06-01*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates the MongoDB Agent to 12.0.22.7705.
- Updates `org.bitbucket.b_c:jose4j` version 0.7.10 to version 0.9.3 to address 
  [SNYK-JAVA-ORGBITBUCKETBC-5488281](https://security.snyk.io/vuln/SNYK-JAVA-ORGBITBUCKETBC-5488281).
- Updates `net.minidev:json-smart@2.4.2` to version 2.4.11 to address 
  [CVE-2023-1370](https://www.cve.org/CVERecord?id=CVE-2023-1370).
- Updates `org.json:json@20211205` to `org.json:json@20230227` 
  to address [CVE-2022-45688](https://www.cve.org/CVERecord?id=CVE-2022-45688).
- Includes BI Connector 2.14.6.
- Snapshots now include a flag that indicates whether or not they are incremental.
- Adds the ability for Ops Manager administrators to access performance and snapshot metrics.
  Administrators can now use Prometheus to query newly created collections and view metrics graphs.
- Compatible with `MongoDB Database Tools 100.7.0`.

### Ops Manager Server 6.0.13

*Released 2023-05-04*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

**Note:**

To improve user experience, Ops Manager server 6.0.13 updates the Ops Manager systemd unit file from 
`after=network.target` to `after=network-online.target`. This prevents reboot failures caused 
by attempting to start mongod after 
the network management stack has started, but before verifying that network connectivity has 
been established.

- Updates the MongoDB Agent to 12.0.21.7698.
- Updates JDK to `jdk-11.0.19+7`.
- Updates `com.fasterxml.woodstox:woodstox-core` to 6.4.0 to address 
  [CVE-2022-40152](https://nvd.nist.gov/vuln/detail/CVE-2022-40152).
- Defaults the Backup Multiple Workers Per File option to 
  On.
- Adds the ability to regularly rotate the 
  `automation-agent-fatal.log` file. 
  Reinstall the MongoDB Agent 
  to enable automatic fatal log file rotation.
- Compatible with `MongoDB Database Tools 100.7.0`.

### Ops Manager Server 6.0.12

*Released 2023-04-07*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates the MongoDB Agent to 12.0.20.7686.
- Compatible with `MongoDB Database Tools 100.7.0`.
- Adds support for managing MongoDB deployments on the Ubuntu 22.04 (x86) operating system.
  BI Connector is not currently supported on the Ubuntu 22.04 (x86) operating system.
- Fixes [CVE-2023-0342](https://nvd.nist.gov/vuln/detail/CVE-2023-0342).
- Fixes a bug in the MongoDB Agent where the shutdown sequence might get
  blocked under certain circumstances, resulting in failed Agent upgrades.

### Ops Manager Server 6.0.11

*Released 2023-03-15*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates the MongoDB Agent to 12.0.19.7676.
- Updates [Apache Commons FileUpload](https://commons.apache.org/proper/commons-fileupload/) to 1.5 to 
  address [CVE-2023-24998](https://nvd.nist.gov/vuln/detail/CVE-2023-24998).
- Adds an option to support using multiple workers for a single file 
  during backups for backup blockstore database and `S3 Snapshot Store` 
  storage. This feature does not support File System Store snapshot storage. 
  You can enable this beta feature by doing the following: 

  1. In the Settings page for
     your Project, click the Beta Features tab.
  2. Toggle Backup Multiple Workers Per File to enable the 
     feature. 

### Ops Manager Server 6.0.10

*Released 2023-03-02*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates the MongoDB Agent to 12.0.18.7668.
- The MongoDB Agent now compresses its own rotated logs.
- Fixes an issue where sharded collections could be missing from the chunks dropdown for the backing cluster in the UI.
- Fixes an issue where clicking the refresh button in the Backup Job Timeline UI resulted in a failure.
- Includes the latest version of MongoDB Shell 1.6.2.
- Compatible with `MongoDB Database Tools 100.6.1`.

### Ops Manager Server 6.0.9

*Released 2023-02-02*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates the MongoDB Agent to 12.0.17.7665.
- Updates JDK to `jdk-11.0.18+10`.

### Ops Manager Server 6.0.8

*Released 2023-01-12*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates the MongoDB Agent to 12.0.16.7656.
- Reintroduces Namespace Filtering for backups.

### Ops Manager Server 6.0.7

*Released 2022-12-01*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates the MongoDB Agent to 12.0.15.7646.
- Fixes an issue where the list of projects was overriden in the left
  navigation bar.
- Adds global alerts for backup groom jobs running late.
- Adds system alerts for AppDB, Oplog Store, and Blockstore disk space
  filling up.
- Adds a new summary page in the Administration UI, under the Backup tab,
  with the status of the most recent snapshots.

### Ops Manager Server 6.0.6

*Released 2022-11-08*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates the MongoDB Agent to 12.0.14.7630.
- Updates JDK to `jdk-11.0.17+8`.
- Updates jetty to 10.0.12 to fix a bug that occurred when SSL 
  connection errors prevented the release of the memory associated 
  with the connection.
- Fixes an issue that prevented downloading the MongoDB Agent for 
  PowerPC (ppc64le) and zSeries (s390x) architectures.

### Ops Manager Server 6.0.5

*Released 2022-10-20*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates `commons-text` to 1.10.0 to address 
  [CVE-2022-42889](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2022-42889).

### Ops Manager Server 6.0.4

*Released 2022-10-13*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates the MongoDB Agent to 12.0.12.7624.
- Compatible with `MongoDB Database Tools 100.6.0`.
- Uses amazon2 packages instead of RHEL7 packages on amazon2 hosts for
  MongoDB Database Tools. If you run Ops Manager in the local mode, you can download
  amazon2 MongoDB Database Tools binaries via the MongoDB Agent.
- Fixes an issue where the Project List was overriden in the
  left navigation bar in the UI.

### Ops Manager Server 6.0.3

*Released 2022-09-01*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Moves the User to Distinguished Name Mapping field in
  Security Settings from the LDAP Authorization
  section to the Other Settings section in
  Native LDAP Authentication. To learn more, see
  Enable LDAP Authentication.
- Updates the delay of the `Query Targeting: Scanned Objects / Returned`
  default alert from 0 to 10 minutes, so that the alert fires only if
  this threshold is maintained for 10 minutes. This affects only the
  default alert configuration.
- Updates JDK to `jdk-11.0.16.1+1`.
- Updates the MongoDB Agent to 12.0.11.7606.
- Fixes incorrect version information in `rpm` Ops Manager packages. To
  learn more, see Install Ops Manager.

### Ops Manager Server 6.0.2

*Released 2022-08-04*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Removes spurious audit log rotation errors from the MongoDB Agent log 
  files and corrects file suffix handling.
- Adds MongoDB 6.0.0 as a deployment option.
- Introduces FCV 6.0 option in Ops Manager.
- Updates JDK to `jdk-11.0.16+8`.
- Updates the MongoDB Agent to 12.0.10.7591.

  **Important:** Live Migration (push) Deprecated or Not Supported for Source Deployments Managed or Monitored by Ops Manager

  - For source deployments running any MongoDB 6.0.+ versions, where the
    deployments are managed or monitored by Ops Manager, live migration (push)
    is not supported.
  - For source deployments running any MongoDB 5.0 and earlier versions,
    where the deployments are managed or monitored by Ops Manager, live
    migration (push) is deprecated.
  - For source deployments running MongoDB 6.0.+, where the deployments
    are monitored by Cloud Manager, live migration (push) is supported.
    To learn more, see Live Migrate Your MongoDB Cluster Monitored by Cloud Manager to Atlas.

  **Warning:**

  Due to critical issue SERVER-68925, Ops Manager deployments
  using this version of the MongoDB Agent should not perform [automated rolling index builds](https://www.mongodb.com/docs/ops-manager/v6.0/data-explorer/indexes/#optional-build-indexes-with-rolling-builds) on clusters running the following MongoDB versions:

  - MongoDB 4.2.19-4.2.22
  - MongoDB 4.4.13-4.4.16
  - MongoDB 5.0.6-5.0.11
  - MongoDB 6.0.0-6.0.1

  You can continue to perform manual rolling index builds safely on your clusters.
  To perform automated rolling index builds safely, upgrade the MongoDB Agent to 12.0.11.7606 or later or 
  upgrade your clusters to:

  - MongoDB 4.2.23 or later
  - MongoDB 4.4.17 or later
  - MongoDB 5.0.12 or later
  - MongoDB 6.0.2 or later

### Ops Manager Server 6.0.1

*Released 2022-07-20*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Supports MongoDB 6.0 as a deployment option, but doesn't display 
  MongoDB 6.0.0 as an available deployment option by default. To 
  display MongoDB 6.0.0 as a deployment option, set  
  `mms.featureFlag.automation.enableV6` configuration option in the `conf-mms.properties` file to 
  `enabled`.
- Updates the MongoDB Agent to 12.0.9.7579.

  **Warning:**

  Due to critical issue SERVER-68925, Ops Manager deployments
  using this version of the MongoDB Agent should not perform [automated rolling index builds](https://www.mongodb.com/docs/ops-manager/v6.0/data-explorer/indexes/#optional-build-indexes-with-rolling-builds) on clusters running the following MongoDB versions:

  - MongoDB 4.2.19-4.2.22
  - MongoDB 4.4.13-4.4.16
  - MongoDB 5.0.6-5.0.11
  - MongoDB 6.0.0-6.0.1

  You can continue to perform manual rolling index builds safely on your clusters.
  To perform automated rolling index builds safely, upgrade the MongoDB Agent to 12.0.11.7606 or later or 
  upgrade your clusters to:

  - MongoDB 4.2.23 or later
  - MongoDB 4.4.17 or later
  - MongoDB 5.0.12 or later
  - MongoDB 6.0.2 or later

### Ops Manager Server 6.0.0

*Released 2022-07-19*

**Note:**

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

- Updates the MongoDB Agent to 12.0.8.7575.

  **Warning:**

  Due to critical issue SERVER-68925, Ops Manager deployments
  using this version of the MongoDB Agent should not perform [automated rolling index builds](https://www.mongodb.com/docs/ops-manager/v6.0/data-explorer/indexes/#optional-build-indexes-with-rolling-builds) on clusters running the following MongoDB versions:

  - MongoDB 4.2.19-4.2.22
  - MongoDB 4.4.13-4.4.16
  - MongoDB 5.0.6-5.0.11
  - MongoDB 6.0.0-6.0.1

  You can continue to perform manual rolling index builds safely on your clusters.
  To perform automated rolling index builds safely, upgrade the MongoDB Agent to 12.0.11.7606 or later or 
  upgrade your clusters to:

  - MongoDB 4.2.23 or later
  - MongoDB 4.4.17 or later
  - MongoDB 5.0.12 or later
  - MongoDB 6.0.2 or later

#### MongoDB Cluster Management

- Supports managing, monitoring, and backing up MongoDB 6.0
  deployments.

#### Backup

- Improves backpressure support to throttle down the snapshot process
  when the load is too high, resulting in improved stability of
  backups.

- Adds support to upload custom certificates for S3 snapshot/oplog
  stores from the admin console.

- Adds support for parallel resumable restores when using Automation.

- Adds support for concurrent WiredTiger snapshots and grooms when the
  S3 snapshot store is used.

#### Monitoring

- Adds support for
  MongoDB cluster monitoring via Prometheus:

  - Allows configuring Ops Manager to make MongoDB cluster metric data
    available for Prometheus to consume.

  - Provides MongoDB process metrics and hardware metrics for the
    clusters.

  - Supports file-based and http-based discovery for metric resources.

  - Supports integrating with Prometheus:

    - You can configure Ops Manager to send metric data about your MongoDB
      clusters to your Prometheus instance.
    - Ops Manager sends MongoDB process metrics and hardware metrics for
      the clusters.
    - Ops Manager supports file based and http based discovery for metric
      resources.

- Adds support for the following elements in Data Explorer:

  - Creation, deletion, and viewing of Clustered collections.

  - Creation of secondary indexes for Timeseries collections using the
    hybrid or rolling build approaches.

- Adds the following options for queries initiated in the Data Explorer
  Find tab:

  - Project
  - Sort
  - Collation

- Adds a new metric, `OPLOG_REPLICATION_LAG_TIME`, accessible through
  the Metrics API (Application Programming Interface).

  - This new metric, along with the existing **Replication Lag** metric,
    chart now has sub-second precision.

- Adds a new option to disable monitoring
  of Ops Manager's backing database (AppDB).

  - When the AppDB is configured for monitoring, it is no longer
    possible to remove the project from Ops Manager.

  - Previously, after enabling
    Application Database Monitoring,
    the user couldn't disable monitoring or remove the project from the
    Ops Manager projects list.

  - In this release, admins can now permit removal of the Application
    DB project, allowing application database monitoring to be fully
    disabled and/or removed.

  - This new option can be found under Admin->Ops Manager
    Config->Backing DBs.

#### Alerting

- Adds support for Microsoft Teams as an alert notification destination.

- Improves integration flow with PagerDuty through its Events v2 API
  for alert notifications.

- Deprecates SNMP (Simple Network Management Protocol) alerts. Ops Manager 7.0.0 will not include SNMP (Simple Network Management Protocol)
  alerts.

#### Automation

- Adds support for MongoDB log rotate configuration and commands for
  independent log rotation configuration of MongoDB Log and MongoDB
  Audit Log Files.

- Adds download of the new mongo shell (mongosh) to the deployment
  nodes.

  **Note:**

  This isn't supported in Local mode.

- Improves usability by offering a modernized Deployment Security
  Configuration UI.

  - Adds support for validating TLS (Transport Layer Security) and LDAP (Lightweight Directory Access Protocol) configuration before
    deployment.

#### User Interface

- Changes to MongoDB's current fonts, colors and UI components.
- Deprecates the Managed Sharded Collections UI. Ops Manager 7.0.0 will not
  include this feature.

#### Ops Manager Platform Support

- Adds support for running Ops Manager on Debian 11.

#### Automation Platform Support

- Adds support for automating deployments on RedHat Enterprise Linux
  version 8 and Amazon Linux 2 on the ARM64/aarch64 architecture.

- Removes support for automating deployments on Debian 9 and RedHat
  Enterprise Linux 6.

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

## Ops Manager Server 3.6

### Ops Manager Server 3.6.12

*Released on 2019-05-02*

- Logging improvements.

- Updated JDK to version 8u212. On Windows, Ops Manager now requires
  the [Visual C++ Redistributable Packages for Visual Studio 2013](https://www.microsoft.com/en-us/download/details.aspx?id=40784).

- **EOL:** Ops Manager support for Ubuntu 14.04 has ended. Ops Manager
  3.6.12 is not supported on Ubuntu 14.04.

### Ops Manager Server 3.6.11

*Released on 2019-02-07*

- Updated JDK (Java Development Kit) to [AdoptOpenJDK 8u202](https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/tag/jdk8u202-b08).

- **Fix:** For queryable restores, the configurable expiration value
  (`brs.queryable.expiration`) now also applies to
  MongoDB authentication requests.

- **Fix:** Resolve transient inability to restore a snapshot if a
  backup data pruning job (garbage collection) is running during the
  restore.

- **Fix:** Improve password verification for sensitive actions within
  Ops Manager, for Ops Manager installations using LDAP (Lightweight Directory Access Protocol) for user
  authentication, and ActiveDirectory as the LDAP (Lightweight Directory Access Protocol) server.

### Ops Manager Server 3.6.10

*Released on 2019-01-10*

- Updated JDK (Java Development Kit) to [AdoptOpenJDK 8u192](https://github.com/AdoptOpenJDK/openjdk8-binaries/releases/tag/jdk8u192-b12).

- Agent Upgrades: automation-4.5.17.5289-1.

### Ops Manager Server 3.6.9

*Released on 2018-11-01*

- **Critical Fix:** Backup initial syncs may fail with an error during
  the oplog application phase, if retryable writes are executed on the
  source cluster during the backup initial sync.

- **Fix:** Log Collection was unable to complete if one of the
  requested files was an empty file.

- LDAP (Lightweight Directory Access Protocol) connections will now use a connection pool. This should reduce
  load on LDAP (Lightweight Directory Access Protocol) servers.

- Update JDK (Java Development Kit) to 8u192.

- Agent Upgrades: automation-4.5.16.5284-1.

### Ops Manager Server 3.6.8

*Released on 2018-08-02*

- **Critical Fix:** Avoid failures to upgrade from Ops Manager 3.4
  when using local mode for MongoDB version management.

- Improve support for global diagnostic download for large deployments.

- Updates Ops Manager JDK (Java Development Kit) (x86_64) to 8u181, which enables endpoint
  identification by default.

- When configuring MongoDB LDAP (Lightweight Directory Access Protocol) authentication, allow setting the
  User to Distinguished Name Mapping without setting the Authorization
  Query Template.

- Agent Upgrades: automation-5.4.9.5483, backup-6.0.10.976

- **Critical Fix:** Set `TasksMax=infinity` and 
  `TasksAccounting=false` in `systemd` scripts for
  SUSE 12 versions of Ops Manager.

### Ops Manager Server 3.6.7

*Released on 2018-06-06*

- Ends support for SLES 11 and Ubuntu 12.04.

- Allow compound text indexes.

- **Fix:** Ops Manager holds file handles open on rotated logfiles.

- **Fix:** Error editing some System Alerts.

- Agent Upgrades: automation-4.5.15.5279-1,  backup-6.0.10.972-1, monitoring-6.1.4.442-1

### Ops Manager Server 3.6.6

*Released on 2018-05-03*

- At the completion of an automated restore of a sharded cluster,
  ensure that the balancer is enabled.

- Improved handling of MongoDB Server Parameters with boolean values.
  Accept all of true, "true" and 1 as the boolean value true.

- Network charts now display physical bytes in/out instead of logical
  bytes in/out. That is, if network compression is enabled for MongoDB,
  the network charts will now show the compressed bytes in/out.

- Ops Manager now properly handles LDAP names which contain special
  characters.

- Fix: Performance Advisor now supports ingesting MongoDB logs using
  ISO8601-UTC timestamps.

- Fix: Include the script needed to seed a secondary when creating a
  TAR.GZ restore for a config server replica set.

- Fix: Retrieving logs via the Ops Manager UI succeeds when the Server
  Pools feature is also in use.

- Upgrade the bundled JDK to 8u172.

- Agent Upgrades: automation-4.5.14.5266,  backup-6.0.9.969

### Ops Manager Server 3.6.5

*Released on 2018-04-05*

- Allow Projects to be deleted from the admin pages, and from Project
  settings.

- Allow queryable restores for compressed snapshots stored in MongoDB
  blockstore snapshot storage.

- Automation support for the new security.ldap.validateLDAPServerConfig
  (MongoDB 3.4.14+)

- Enable log rotation for Backup HEAD dbs.

- Never save localhost/127.0.0.1 as a host mapping.

- Show agent out of date warnings for manually managed Monitoring and
  Backup Agents.

- Support for the MongoDB Connector for BI, version 2.4.1.

- When importing replica sets into Automation, include information on
  replica set tags.

- Agent Upgrades: automation-4.5.13.5261, monitoring-6.1.3.436, backup-6.0.8.960

### Ops Manager Server 3.6.4

*Released on 2018-03-01*

- **Fix:** Avoid failures in alert processing when monitoring topology
  for disk partitions cannot be derived correctly.
- **Fix:** Changes to the `admin.system.version` collection on
  documents other than the `featureCompatibilityVersion` document
  should not abort an initial sync of a backup.
- **Fix:** Prevent the deletion of the last `Global Owner` of
  an Ops Manager installation.
- **Fix:** Suggested Indexes for
  nested predicate and sort should not ignore the predicate.
- Support for version 2.4.0 of the
  `MongoDB Business Intelligence Connector`.

- Agent Upgrades: automation-4.5.12.2514, backup-6.0.8.752

### Ops Manager Server 3.6.3

*Released on 2018-02-01*

- **Fix:** Email delivery of System Alerts was suppressed and is now
  enabled.

- Security improvements.

- Add new API for administrators to configure Backup infrastructure

- The bundled JDK is version 8u162.

- Add new property (mms.ignoreInitialUiSetup) that allows full
  automation of Ops Manager installation and configuration.

- Agent Upgrades: automation-4.5.11.2453, backup-6.0.6.724

### Ops Manager Server 3.6.2

*Released on 2018-01-11*

- Add support for MongoDB 3.6.1.

- Add BI Connector information to the Diagnostic Archive.

- Allow Project User Admin to set team roles and remove teams from
  projects.

- Allow user to specify `sampleRefreshIntervalSecs` BI Connector
  flag.

- Avoid "Inconsistent backup configuration" message when Monitoring
  Agent fails to communicate with MongoDB.

- Improve parsing of queries by Performance Advisor.

- Log Collection now collects log files from mongos instances.

- Log the list of TLS ciphers in use and any disabled by config.

- MongoDB Enterprise 3.6.2+ is needed on daemons to perform
  queryable restores of 3.6 sharded clusters.

- **Fix:** Bug that prevented backups on an S3-compatible snapshot
  store from being terminated.

- Restrict downgrading clusterAuthMode in the Automation Agent UI.

- Upgrade `jackson-databind` to 2.9.3.

- When doing an automated restore, only allow restoring to clusters
  that have a higher FCV than the snapshot and where all mongod
  versions support the snapshots FCV.

- Expand access for the Automation Agent user by adding the
  `restore@admin` role.

#### Fixes

- **Fix:** Bug where Performance Advisor could display "A server error
  has occurred".

- **Fix:** PIT restores of inactive replica sets.

- **Fix:** Add timeouts to Queryable Restores.

- **Fix:** Always set the correct From and
  Reply-To fields in System Alert emails.

- **Fix:** Extra System Alerts are no longer created.

- **Fix:** Version Manifest no longer reverts to the on-disk version.

- **Fix:** MongoDB 3.6 sharded cluster import no longer blocked.

- **Fix:** Set correct Maximum Number of Connections for
  MongoDB 3.6 for Alerting.

### Ops Manager Server 3.6.1

*Released on 2017-12-19*

- Agent Upgrades: automation-4.5.9.2403

- **Fix:** Point in time automated restores now downloads the correct
  utility.

- **Fix:** When Ops Manager is configured to use LDAP for user
  authentication, do not allow users to be invited.

- **Fix:** Allow MongoDB Advanced Options to be edited for an entire
  sharded cluster.

- **Fix:** Allow clusterAuthMode independently of X509 auth.

- **Fix:** Allow import of deployments using the
  net.ssl.allowConnectionsWithoutCertificates parameter.

- **Fix:** Explicitly specify the collation {locale: "simple"} in
  createIndex during initial sync.

- **Fix:** Users should be able to convert from LDAP native to saslauthd
  using the UI.

- Performance improvements for queryable restores.

- Security enhancements.

### Ops Manager Server 3.6.0

*Released 2017-12-05*

- Added support for a new organizations and projects hierarchy to facilitate the management of your Ops
  Manager deployments. Groups are now known as Projects. You can put
  multiple Projects under an Organization.

- Added support for nested LDAP groups via the `member` field when
  configuring Ops Manager to use LDAP for Ops Manager authentication.

  Although Ops Manager 3.6 supports the use of either `member` or
  `memberOf` for configuration, support for LDAP via the `memberOf`
  field will be removed in a future version of Ops Manager. When
  possible, use `member` instead.

- Added support for a new Agent API Key model. Multiple Agent API Keys can now be
  associated with a project. This gives users the ability to perform
  Agent key rotation.

- The bundled JDK (Java Development Kit) is version 8u152.

#### Automation

- Added support for management of the MongoDB Connector for
  Business Intelligence. The MongoDB
  Connector for Business Intelligence allows you to query a MongoDB
  database using SQL commands to aid in data analysis. It translates
  SQL queries from data analysis tools to MongoDB aggregation pipelines
  on MongoDB database.

- Added the ability to retrieve the on-disk logs for all MongoDB and Ops Manager Agent
  processes. The logs are sent to the Ops Manager server and available
  for download by Ops Manager administrators.

- Ended support for the `seedSecondary.sh` script. You cannot run the
  `seedSecondary.sh` script on any MongoDB database running MongoDB
  3.6 or later. To learn more about restoring a snapshot, see
  Restore a Completed Snapshot.

- Agent Upgrade: automation-4.5.7.2375

#### Backup

- Added support for queryable backups.
  This functionality allows you to query specific backup snapshot. You
  can use the queryable backups to:

  - Restore a subset of data within the MongoDB deployment.

  - Compare previous versions of data against the current data.

  - Identify the best point in time to restore a system by comparing
    data from multiple snapshots.

  **Important:**

  On Windows, queryable restores
  work on MongoDB 3.2, 3.4, and 3.6 snapshots once the Ops Manager
  `Backup Daemon`
  can access MongoDB 3.4.11 or later.

- Added support for IBM Cloud Object Storage and DellEMC Elastic Cloud
  Storage for S3 blockstore snapshot storage

- Added support for performing
  automated restores from one Project to another Project.

- Added the ability to reschedule the expiration time of a snapshot.

- Added support for automated restores via the Public API.

- Agent Upgrade: backup-6.0.3.689.

#### Monitoring

- Added Real-Time Metrics.

- Added the Performance Advisor.
  The Performance Advisor monitors any operation with a query predicate
  that MongoDB considers slow and suggests new indexes to improve query
  performance.

- Added the Data Explorer. This feature
  provides the ability to introspect collections in your managed
  MongoDB deployments via the Data Explorer view.

- Agent Upgrade: monitoring-6.1.1.395.

#### Release Advisories for Ops Manager 3.6

Before upgrading Ops Manager from 3.4 to 3.6, complete the following 
actions:

- Upgrade all backing databases to MongoDB 3.2 or later.

- Upgrade the monitoring schema.

  To monitor the schema upgrade:

  a. Click Admin.
  b. Click Ops Manager Config.
  c. Click the Miscellaneous tab.

     The progress should be shown before the 
     Default Monitoring Data Retention heading.

- Change `mms.minimumTLSVersion` if you must support
  older TLS (Transport Layer Security) versions. 

  Ops Manager Application supports TLS (Transport Layer Security) 1.2 only by default. 

  To re-enable ciphers which have been disabled, change 
  `mms.disableCiphers`.

  **Warning:**

  Consider the security implications carefully before doing this.

#### Deprecation

- MongoDB 2.4 is no longer supported for Automation and Backups:

  - All MongoDB 2.4 processes in Automation will be unmanaged.

  - All MongoDB 2.4 backups will be stopped.

- MongoDB 3.0 is no longer supported as a backing store for Ops Manager.

#### Upcoming Incompatibilities

- Support for MongoDB 3.2 as a backing store for Ops Manager will be
  removed in Ops Manager 4.0.

- Support for restores delivered by SCP will be removed in Ops Manager
  4.0.

- Support for LDAP via the `memberOf` field will be removed in Ops
  Manager 4.0. Use `member` instead. In Ops Manager 3.6, you may use
  either `member` or `memberOf`.

- Support for the older Agent API Key model will be removed in Ops
  Manager 4.0. Instead, use the new-style keys. In Ops Manager 3.6, the
  new-style keys are preferred, the but the older keys will still work.

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
