<!-- Converted from release-notes/mongodb-agent.txt (reStructuredText). Includes are inlined. -->

# MongoDB Agent Changelog

## MongoDB Agent 107.0.23.8832-1

Released with Ops Manager 7.0.23 on 2026-02-17.

## MongoDB Agent 107.0.22.8822-1

Released with Ops Manager 7.0.22 on 2026-01-15.

## MongoDB Agent 107.0.21.8817-1

Released with Ops Manager 7.0.21 on 2025-12-16.

## MongoDB Agent 107.0.20.8807-1

Released with Ops Manager 7.0.20 on 2025-12-03.

## MongoDB Agent 107.0.19.8805-1

Released with Ops Manager 7.0.19 on 2025-11-06.

## MongoDB Agent 107.0.18.8784-1

Released with Ops Manager 7.0.18 on 2025-09-10.

## MongoDB Agent 107.0.17.8771-1

Released with Ops Manager 7.0.17 on 2025-08-08.

## MongoDB Agent 107.0.16.8756-1

Released with Ops Manager 7.0.16 on 2025-07-03.

## MongoDB Agent 107.0.13.8702-1

Released with Ops Manager 7.0.13 on 2025-01-10.

## MongoDB Agent 107.0.12.8669-1

Released with Ops Manager 7.0.12 on 2024-10-31.

## MongoDB Agent 107.0.11.8645-1

Released with Ops Manager 7.0.11 on 2024-09-05.

## MongoDB Agent 107.0.10.8627-1

Released with Ops Manager 7.0.10 on 2024-08-01.

- Fixes [CVE-2023-45288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45288)

## MongoDB Agent 107.0.9.8621-1

Released with Ops Manager 7.0.9 on 2024-07-18.

## MongoDB Agent 107.0.8.8615-1

Released with Ops Manager 7.0.8 on 2024-06-27.

## MongoDB Agent 107.0.7.8596

Released with Ops Manager 7.0.7 on 2024-06-06.

## MongoDB Agent 107.0.6.8587

Released with Ops Manager 7.0.6 on 2024-05-10.

## MongoDB Agent 107.0.3.8581

Released with Ops Manager 7.0.5 on 2024-05-02.

## MongoDB Agent 107.0.3.8550

Released with Ops Manager 7.0.3 on 2024-03-07.

## MongoDB Agent 107.0.2.8531

Released with Ops Manager 7.0.2 on 2024-02-01

## MongoDB Agent 107.0.0.8507

Released with Ops Manager 7.0.1 on 2024-01-08

## MongoDB Agent 107.0.0.8506-1

Released with Ops Manager 7.0.1 on 2024-01-08

## MongoDB Agent 107.0.0.8490-1

Released with Ops Manager 7.0.0 on 2024-01-04

## MongoDB Agent 12.0.35.7911-1

Released with Ops Manager 6.0.27 on 2025-01-30.

## MongoDB Agent 12.0.34.7888-1

Released with Ops Manager 6.0.26 on 2024-10-31.

## MongoDB Agent 12.0.33.7866-1

Released with Ops Manager 6.0.25 on 2024-08-08.

- Fixes [CVE-2023-45288](https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2023-45288)

## MongoDB Agent 12.0.32.7851-1

Released with Ops Manager 6.0.24 on 2024-07-12.

## MongoDB Agent 12.0.30.7791

Released with Ops Manager 6.0.22 on 2023-01-04.

## MongoDB Agent 12.0.29.7785

Released with Ops Manager 6.0.21 on 2023-12-14.

## MongoDB Agent 12.0.28.7763

Released with Ops Manager 6.0.20 on 2023-11-03.

## MongoDB Agent 12.0.27.7746

Released with Ops Manager 6.0.19 on 2023-10-05

## MongoDB Agent 12.0.26.7740

Released with Ops Manager 6.0.18 on 2023-09-07

## MongoDB Agent 12.0.25.7724

Released with Ops Manager 6.0.17 on 2023-08-03

## MongoDB Agent 12.0.24.7719

Released with Ops Manager 6.0.16 on 2023-07-06

## MongoDB Agent 12.0.23.7711

Released with Ops Manager 6.0.15 on 2023-06-15

## MongoDB Agent 12.0.22.7705

Released with Ops Manager 6.0.14 on 2023-06-01

## MongoDB Agent 12.0.21.7698

Released with Ops Manager 6.0.13 on 2023-05-04

## MongoDB Agent 12.0.20.7686

Released with Ops Manager 6.0.12 on 2023-04-07

## MongoDB Agent 12.0.19.7676

Released with Ops Manager 6.0.11 on 2023-03-15

## MongoDB Agent 12.0.18.7668

Released with Ops Manager 6.0.10 on 2023-03-02

- The agent now compresses its own rotated logs.

## MongoDB Agent 12.0.17.7665

Released with Ops Manager 6.0.9 on 2023-02-02

## MongoDB Agent 12.0.16.7656

Released with Ops Manager 6.0.8 on 2023-01-12

## MongoDB Agent 12.0.15.7646

Released with Ops Manager 6.0.7 on 2022-12-01

## MongoDB Agent 12.0.14.7630

Released with Ops Manager 6.0.6 on 2022-11-08

## MongoDB Agent 12.0.13.7627

Released with Ops Manager 6.0.5 on 2022-10-20

- Removes support for unsetting the global default write concern on 
  MongoDB 5.0 and later. The MongoDB Agent now treats 
  `DefaultRWConcern` with null or empty values as unmanaged and no 
  longer attempts to unset the value.

## MongoDB Agent 12.0.12.7624

Released with Ops Manager 6.0.4 on 2022-10-13

## MongoDB Agent 12.0.11.7606

Released with Ops Manager 6.0.3 on 2022-09-01

## MongoDB Agent 12.0.10.7591

Released with Ops Manager 6.0.2 on 2022-08-04

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

- Supports encryption at rest
  for audit logs using
  advanced configuration options.

## MongoDB Agent 12.0.9.7579

Released with Ops Manager 6.0.1 on 2022-07-20

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

## MongoDB Agent 12.0.8.7575

Released with Ops Manager 6.0.0 on 2022-07-19

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

## MongoDB Agent 11.0.27.7162

Released with Ops Manager 5.0.22 on 2023-07-31

## MongoDB Agent 11.0.26.7158

Released with Ops Manager 5.0.21 on 2023-06-01

## MongoDB Agent 11.0.25.7136

Released with Ops Manager 5.0.20 on 2023-03-15

## MongoDB Agent 11.0.24.7131

Released with Ops Manager 5.0.19 on 2023-02-09

## MongoDB Agent 11.0.23.7129

Released with Ops Manager 5.0.18 on 2023-02-02

## MongoDB Agent 11.0.22.7120

Released with Ops Manager 5.0.17 on 2022-11-17

## MongoDB Agent 11.0.21.7116

Released with Ops Manager 5.0.16 on 2022-10-20

- Removes support for unsetting the global default write concern on 
  MongoDB 5.0 and later. The MongoDB Agent now treats 
  `DefaultRWConcern` with null or empty values as unmanaged and no 
  longer attempts to unset the value.

## MongoDB Agent 11.0.20.7108

Released with Ops Manager 5.0.15 on 2022-09-19

- Prevents unnecessary audit log rotations when using with MongoDB 5.0 releases.

## MongoDB Agent 11.0.19.7094

Released with Ops Manager 5.0.14 on 2022-08-04

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

## MongoDB Agent 11.0.18.7089

Released with Ops Manager 5.0.13 on 2022-07-21

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

## MongoDB Agent 11.0.17.7086

Released with Ops Manager 5.0.12 on 2022-06-30

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

## MongoDB Agent 11.0.16.7080

Released with Ops Manager 5.0.11 on 2022-06-02

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

## MongoDB Agent 11.0.15.7073

Released with Ops Manager 5.0.10 on 2022-05-05

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

## MongoDB Agent 11.0.14.7064

Released with Ops Manager 5.0.9 on 2022-04-07

## MongoDB Agent 11.0.13.7055

Released with Ops Manager 5.0.8 on 2022-03-03

Supports MongoDB log rotate configuration and commands for independent 
log rotation configuration for MongoDB Log and MongoDB Audit Log Files.

## MongoDB Agent 11.0.12.7051

Released with Ops Manager 5.0.7 on 2022-02-17

Rejects legacy monitoring and backup agent settings that don't match
MongoDB Agent settings when `configOverrides` field should be used.

## MongoDB Agent 11.0.11.7036

Released with Ops Manager 5.0.6 on 2022-01-13

## MongoDB Agent 11.0.10.7021

Released with Ops Manager 5.0.5 on 2021-12-02

## MongoDB Agent 11.0.9.7010

Released with Ops Manager 5.0.4 on 2021-11-04

## MongoDB Agent 11.0.8.7002

Released with Ops Manager 5.0.3 on 2021-10-06

- Removes support for RHEL/CentOS 6 for the MongoDB Agent.

## MongoDB Agent 11.0.7.6992

Released with Ops Manager 5.0.2 on 2021-09-03

## MongoDB Agent 11.0.6.6981

Released with Ops Manager 5.0.1 on 2021-08-05

## MongoDB Agent 11.0.5.6967-1

Released with Ops Manager 5.0.0 on 2021-07-13

- Stops adding MongoDB binaries (such as `mongod`, `mongos`, etc.)
  to the Linux path when installing from RPM and DEB packages.

## MongoDB Agent 10.14.35.6589

Released with Ops Manager 4.4.24 on 2022-07-29

## MongoDB Agent 10.14.34.6588

Released with Ops Manager 4.4.23 on 2022-07-07

## MongoDB Agent 10.14.33.6581

Released with Ops Manager 4.4.22 on 2022-05-05

## MongoDB Agent 10.14.32.6576

Released with Ops Manager 4.4.21 on 2022-02-17

## MongoDB Agent 10.14.31.6566

Released with Ops Manager 4.4.20 on 2022-01-13

## MongoDB Agent 10.14.30.6552

Released with Ops Manager 4.4.19 on 2021-11-16

## MongoDB Agent 10.14.29.6548

Released with Ops Manager 4.4.18 on 2021-11-04

- Removes support for RHEL/CentOS 6 for the MongoDB Agent.

## MongoDB Agent 10.14.28.6532

Released with Ops Manager 4.4.17 on 2021-09-03

## MongoDB Agent 10.14.27.6524

Released with Ops Manager 4.4.16 on 2021-08-05

## MongoDB Agent 10.14.24.6508

Released with Ops Manager 4.4.13 on 2021-06-03

## MongoDB Agent 10.14.23.6498

Released with Ops Manager 4.4.12 on 2020-05-06

- Uses Go 1.15 to build the MongoDB Agent. Before upgrading to this 
  version, ensure that all TLS (Transport Layer Security) certificates used in your MongoDB 
  deployment contain a Subject Alternative Name. For more information, 
  see Troubleshooting Automation.

## MongoDB Agent 10.14.22.6489

Released with Ops Manager 4.4.11 on 2020-04-01

## MongoDB Agent 10.14.21.6476

Released with Ops Manager 4.4.10 on 2020-03-04

## MongoDB Agent 10.14.20.6466

Released with Ops Manager 4.4.9 on 2021-02-17

- Fixes a bug that ensures fixed ordering of index options for all nodes
  in a rolling index build.

## MongoDB Agent 10.14.18.6453

Released with Ops Manager 4.4.7 on 2021-01-11

- Fixes a bug that can crash the agent after upgrading to Ops Manager 4.4.6 
  on deployments that use the MongoDB Enterprise Kubernetes Operator.

## MongoDB Agent 10.14.17.6445

Released with Ops Manager 4.4.6 on 2020-12-03

## MongoDB Agent 10.14.16.6437

Released with Ops Manager 4.4.5 on 2020-11-05

## MongoDB Agent 10.14.15.6432

Released with Ops Manager 4.4.4 on 2020-10-07

## MongoDB Agent 10.14.14.6427

Released with Ops Manager 4.4.3 on 2020-09-23

## MongoDB Agent 10.14.13.6423

Released with Ops Manager 4.4.2 on 2020-09-03

## MongoDB Agent 10.14.12.6411

Released with Ops Manager 4.4.1 on 2020-08-05

## MongoDB Agent 10.2.25.6010

Released with Ops Manager 4.2.25 on 2021-06-03.

## MongoDB Agent 10.2.24.6007

Released with Ops Manager 4.2.24 on 2020-05-05.

- Uses Go 1.15 to build the MongoDB Agent. Before upgrading to this 
  version, ensure that all TLS (Transport Layer Security) certificates used in your MongoDB 
  deployment contain a Subject Alternative Name. For more information, 
  see Troubleshooting Automation.

## MongoDB Agent 10.2.22.6000

Released with Ops Manager 4.2.22 on 2020-12-03.

## MongoDB Agent 10.2.21.5995

Released with Ops Manager 4.2.21 on 2020-11-05.

## MongoDB Agent 10.2.20.5992

Released with Ops Manager 4.2.17 on 2020-09-13

- Fixes a bug where the MongoDB Agent ignored other agent
  authentication mechanisms if `clusterAuth`was set to `x509`.

## MongoDB Agent 10.2.20.5991

Released with Ops Manager 4.2.16 on 2020-08-06

## MongoDB Agent 10.2.19.5989

Released with Ops Manager 4.2.15 on 2020-07-02

- Reduces number of connections per second.

- Improves the Backup Module oplog tail performance.

## MongoDB Agent 10.2.18.5978

Released with Ops Manager 4.2.14 on 2020-06-04

- Allows Automation for managed deployments to start `mongos` processes
  if only the CSRS (Config Servers as Replica Sets) primary is available, instead of requiring all
  CSRS (Config Servers as Replica Sets) members to be available.

- Fixes a rare issue with managed deployments where the MongoDB Agent is
  unable to start MongoDB processes.

- Fixes an issue where the MongoDB Agent ignores other agent
  authentication mechanisms if `clusterAuth` is set to `x509`.

## MongoDB Agent 10.2.17.5970

Released with Ops Manager 4.2.13 on 2020-05-14

- Fixes an issue with managed deployments that can occur when a sharded
  cluster has a shard added and an index built at the same time.

- Supports SUSE 15.

## MongoDB Agent 10.2.16.5960

Released with Ops Manager 4.2.12 on 2020-04-09

- Fixes an issue that resulted in failures creating snapshots when 
  handling sessions between the MongoDB Agent and MongoDB 4.2 clusters.

## MongoDB Agent 10.2.15.5958

Released with Ops Manager 4.2.11 on 2020-04-06

- Ensures that the MongoDB Agent never interprets network errors as 
  authentication configuration errors, leading to illegitimate attempts 
  to rotate the keyfile.

## MongoDB Agent 10.2.14.5953

Released with Ops Manager 4.2.10 on 2020-03-16

- Ensures that an error when rotating one type of log file does not interfere
  with log rotation of other log files.

- Ensures that the MongoDB Agent always respects the optionality of keyfiles
  for MongoDB deployments using X-509 cluster authentication.

- Ensures that a majority of healthy nodes remains up at all times if a cluster
  has unhealthy nodes prior to the initiation of a storage-affecting rolling
  change.

- Ensures that when importing a new sharded cluster for monitoring, the
  algorithm for auto-discovering all processes in the sharded cluster
  will also consider the fully qualified domain names.

- Upgrades the backup module of the MongoDB Agent to use the MongoDB Go Driver
  version 1.1.4.

## MongoDB Agent 10.2.14.5953

Released with Ops Manager 4.2.9 on 2020-03-05

- Ensures that an error when rotating one type of log file does not interfere
  with log rotation of other log files.

- Ensures that the MongoDB Agent always respects the optionality of keyfiles
  for MongoDB deployments using X-509 cluster authentication.

- Ensures that a majority of healthy nodes remains up at all times if a cluster
  has unhealthy nodes prior to the initiation of a storage-affecting rolling
  change.

- Upgrades the backup module of the MongoDB Agent to use the MongoDB Go Driver
  version 1.1.4.

## MongoDB Agent 10.2.13.5943

Released with Ops Manager 4.2.8 on 2020-02-06

- Adds support for management of MongoDB deployments on Debian 10.

- Fixes the following issues:

  - During a rolling index build for an unsharded collection on a
    sharded collection, only index the collection on the shard on which
    it already exists.

  - When the MongoDB Agent authenticates to MongoDB clusters using
    GSSAPI (Generic Security Services Application Program Interface) authentication, ensure that Ops Manager falls back to other
    authentication methods if the `kinit` call fails.

- Can perform a restore to a cluster that is unhealthy before the
  restore is requested.

- Redacts sensitive configuration data in MongoDB Agent log files to
  improve security.

## MongoDB Agent 10.2.12.5930

Released with Ops Manager 4.2.7 on 2020-01-09

- Improves the behavior when a rollback occurs on a source cluster
  using replication protocol v0 when backing up clusters running
  MongoDB 4.0 and earlier.

## MongoDB Agent 10.2.11.5927

Released with Ops Manager 4.2.6 on 2019-12-19

- Resolves memory leak in MongoDB Agent when performing snapshots for
  MongoDB 4.2 clusters.

## MongoDB Agent 10.2.10.5921

Released with Ops Manager 4.2.5 on 2019-12-12

- MongoDB Agent is now built using Go 1.13.

## MongoDB Agent 10.2.9.5909

Released with Ops Manager 4.2.4 on 2019-11-07

- MongoDB Agent is now built using Go 1.13.
- Fixes an issue where the MongoDB Agent fails to complete some
  requested actions on a sharded cluster if a config server is down.
- When creating an index using Data Explorer,
  the optional name property of an index is no longer ignored.

## MongoDB Agent 10.2.8.5901-1

Released with Ops Manager 4.2.3 on 2019-10-10

- Fixes an issue where upgrading to
  MongoDB Agent 10.2.7 from any previous
  version restarted all `mongos` processes.

## MongoDB Agent 10.2.7.5898

Released with Ops Manager 4.2.2 on 2019-10-03

- Adds support for the `businessCategory` field in extended
  validation TLS (Transport Layer Security) certificates.
- MongoDB Agent is now built using Go 1.12.
- Adds support for the
  `partialFilterExpression`
  index option when creating an index using
  Data Explorer.
- **Backup:** Adds support for the `businessCategory` field in
  extended validation TLS (Transport Layer Security) certificates.
- **Monitoring:** Adds support for the `businessCategory` field in
  extended validation TLS (Transport Layer Security) certificates.

## MongoDB Agent 10.2.6.5879-1

Released with Ops Manager 4.2.1 on 2019-09-05

- Fixes a bug where the MongoDB Agent could panic and delete files from
  its current working directory.
- Improves logging in the MongoDB Agent such that when a connection to
  a MongoDB process is deliberately canceled, it does not appear as an
  error.
