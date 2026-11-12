<!-- Part 1 of 10 of release-notes/application.md (split because the page is big). -->

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
