<!-- Converted from tutorial/prepare-backing-mongodb-instances.txt (reStructuredText). Includes are inlined. -->

# Install the Ops Manager Application Database and Backup Database

Before you install Ops Manager, you must deploy its supporting databases.
These are called backing databases. These databases include the
mms-application-database and the
backup database. The following table
compares the Ops Manager Application Database and the Backup Database:

* - Frequently Asked Questions
  - Application Database
  - Backup Database

* - What does the database store?
  - WARNING: The following items can contain sensitive data. To prevent 
    unauthorized access and protect sensitive data, you must 
    secure
    the mms-application-database.

    - Ops Manager operational data.

    - MongoDB database logs that you can retrieve and view using Ops Manager. 

    - Unoptimized queries if you enabled Performance 
      Advisor, which 
      analyzes logs to recommend performance improvements in the 
      performance-advisor page.

    - Real-time metrics if you enabled Real Time Performance Panel, which collects and displays real time metrics from your MongoDB databases in the Real Time Metrics page. Ops Manager deletes the data 
      when you navigate away from the `Real Time Metrics` page.

  - - Oplog data
    - Temporary sync data
    - Your snapshots, depending on your configuration

* - Is the database necessary?
  - Yes
  - No, unless you use Ops Manager to
    backup the databases that
    Ops Manager manages.

* - How should the database store the data?
  - Dedicated replica set on independent storage volume
  - Dedicated replica set per backup database on independent
    storage volumes

* - Can the database use more than one deployment?
  - No
  - Yes

* - Can Ops Manager use the Automation module with this database?
  - No
  - Yes

* - Can Ops Manager use the Backup Module to back up this database?
  - No
  - No

* - Can Ops Manager use the Monitoring module to monitor this database?
  - Yes
  - Yes

**Important:**

Do not use MongoDB minor releases for backing databases. Backing
databases are compatible only with
major releases, such as v7.0.

**Note:**

Each backing database must use a dedicated replica set. *The replica
set can't store other data*.

Running regular backups, a backup database could fill a volume. If
the application database cannot write to a volume, Ops Manager stops.
Proper storage setup reduces the risk of Ops Manager failures.

## Considerations

### Replica Set Topology

Each backing database replica set
should include three data-bearing members for high availability. If you
lack storage capacity for three data-bearing members, the third member
of a backing database may be an arbiter.

For the Ops Manager application database, you may run one member
of the replica set on the same host as Ops Manager.

**Important:** Backing Databases with fewer than three data-bearing members

When writing to its backing databases, Ops Manager uses the
Replica Acknowledged (`w:2`)
write concern. This write
concern reports a write as successful *only* after the primary *and*
one secondary acknowledge that write. This means that if a backing
database loses one of the two data-bearing members, MongoDB stops
write operations.

**Warning:** Default read and write concerns

The default MongoDB read and write concerns for your MongoDB version should 
match the default read and write concerns for your 
backing databases and your application database. If 
you set a different read or write concern, you might experience data 
loss.

### Application Database Monitoring

You can choose to monitor the application database after you install
Ops Manager.

To monitor your application database:

1. Finish installing the backing databases.
#. Install Ops Manager Application.
#. `Enable Monitoring` for
   the application database.

   a. Install the MongoDB Agent
      on the application database hosts.
   b. Add the application database
      through the Ops Manager UI.

**See also:**

To follow the full procedure, see
/tutorial/enable-appdb-monitoring.

## Prerequisites

### Replica Set Configuration

The replica sets that host the Ops Manager
backing databases must:

#### Use Dedicated Databases

The replica sets must store data to support
Ops Manager metadata *only*. They must store *no other data*.

#### Use Backing Database for S3-compatible storage Block and Oplog Metadata

If you use S3-compatible storage for block or oplog storage, the backing database can
store the metadata for the blocks and oplog. 

#### Use a Compatible MongoDB Version

For the following Ops Manager release series, you may run its
backing databases on any of the following MongoDB versions:

| Ops Manager Release | MongoDB 4.2 | MongoDB 4.4 | MongoDB 5.0 | MongoDB 6.0 | MongoDB 7.0 |
|---|---|---|---|---|---|
| Ops Manager 7.0 | EOL | EOL | Deprecated | Supported | Supported |
| Ops Manager 6.0 | EOL | Deprecated | Supported | Supported | N/A |
| Ops Manager 5.0 | Deprecated | Supported | Supported | N/A | N/A |
| Ops Manager 4.4 | Supported | Supported | N/A | N/A | N/A |
| Ops Manager 4.2 | Supported | N/A | N/A | N/A | N/A |

**Note:**

A deprecated version still works with the corresponding Ops Manager
release, but we will remove the support for this version in the
next release. [MongoDB Support](https://support.mongodb.com) recommends migrating to a supported
version to avoid potential incompatibility issues.

To learn more, see [MongoDB Legacy Support Policy](https://www.mongodb.com/legal/support-policy/legacy) and 
[MongoDB Software Lifecycle Schedules for Ops Manager](https://www.mongodb.com/legal/support-policy/lifecycles).

Version support covers the full release series from the first to the
last release.

To learn more about MongoDB versioning, see
release-version-numbers in the MongoDB Manual.

**Important:**

Only the MongoDB Ops Manager backing databases must meet this
requirement. The MongoDB deployments that Ops Manager manages do not.
For the minimum versions required for managed MongoDB deployments,
see /reference/mongodb-compatibility/.

#### Use the WiredTiger Storage Engine for the Application Database

Use WiredTiger for the Ops Manager
application database.

#### Use the WiredTiger Storage Engine for the Backup Database

For backup database configuration options, see
Backup Preparations.

#### Use Queries that Do Not Require Indexes

Do *not* run the backing databases with the MongoDB
`--notablescan` parameter set. When set, this parameter
specifies that all queries must use indexes.

### Replica Set Security

#### Secure the Connection to the Backing Databases

Ensure that connections from Ops Manager to your backing databases
are secure. Configure these databases to accept connections from
Ops Manager that only use TLS.

#### Configure an Authentication Mechanism for the Backing Databases

Limit access to your backing databases to specific MongoDB users using
an authentication mechanism. To configure your backing
databases to use authentication, see configure-auth-backing.

#### Grant Minimal Roles to the Ops Manager User that Accesses the Backing Databases

Set these users to have the `readWriteAnyDatabase` and
`dbAdminAnyDatabase` roles. If a backing database is a
sharded cluster, add `clusterAdmin`, otherwise add
`clusterMonitor`.

### Host Configuration

The hosts that run the replica sets must meet the
following requirements for:

#### Hardware

The hosts must meet mms-application-database-specifications or
backup-database-specifications depending on which database
the host runs. If a host serves other Ops Manager components in
addition to the database, you must sum the hardware requirements for
each component to determine the requirements for the host.

#### System Configuration

The hosts must be configured according to the requirements given in
the MongoDB Production Notes
except where explicitly contradicted in this tutorial. The Production
Notes include information on ulimits, NUMA, and other configuration
options.

#### Hostnames

Use lowercase FQDN (fully qualified domain name)\s. If you use uppercase characters, Ops Manager may
fail to find your backing database. To learn more about naming hosts,
see RFC 1178.

#### Networking

Host network security must allow the needed ports described in
/reference/firewall-configuration. The appropriate inbound
and outbound firewall rules for each host must allow access to the
required ports.

#### RHEL (Red Hat Enterprise Linux) and CentOS 6 hosts only

RHEL (Red Hat Enterprise Linux) limits the maximum
number of user processes to `1024`. This overrides the general
user process limit (`ulimit -u`) setting.

For the userid that runs Ops Manager (`mongodb-mms` by default), 
add `soft` and `hard` `nproc` (number of processes) entries to the `/etc/security/limits.d/99-mongodb-nproc.conf` user process
configuration file. Use values that are larger than the RHEL (Red Hat Enterprise Linux) `1024` user process limit.

```apache
mongodb-mms soft nproc 200000
mongodb-mms hard nproc 500000
```

If `/etc/security/limits.d/99-mongodb-nproc.conf` does not exist, create it. Use the contents of the
`/etc/security/limits.d/90-nproc.conf` file as a template.

#### RHEL (Red Hat Enterprise Linux) and CentOS hosts running SELinux in `enforcing` mode

If the hosts are not configured to use the default MongoDB
`data` or `log`
paths or ports and are
enforcing SELinux policies, update the SELinux policies before
starting the backing databases.

To learn how to update the SELinux policy:

- For MongoDB Community edition, see
  Configure SELinux

- For MongoDB Enterprise edition, see
  Configure SELinux

## Deploy Backing Databases

To deploy MongoDB replica sets to host the
Ops Manager backing databases:

**Step 1: Provision hosts.**

Your hosts must meet the backing-instances-prerequisites
requirements.

**Important:**

	 Configure the MongoDB deployment for your backing
	 databases according to the MongoDB Production Notes. If you don't, the
	 MongoDB deployment might fail.

   **Step 2: Install MongoDB on each host.**

   Follow the steps to Install MongoDB. If you install `MongoDB Enterprise` for the backing database, you
   must install the MongoDB Enterprise dependencies.

   **Step 3: Deploy replica sets for each backing database.**

   Follow the steps described in Deploy one Replica Set for each application database.
   After deploying your application databases, you can install Ops Manager
   using one of the following procedures:

   - Install with RPM Package
   - Install with DEB Package
   - Install from Archive with Linux

   You can then perform managed replica set deployment with Ops Manager for your remaining
   backing databases. Alternatively, you can manually
   deploy replica sets for each
   backing database.

## Next Steps

- When you install Ops Manager, you must set the `mongo.mongoUri`
  setting to connect to the replica set you created for the
  application database in this tutorial.

- If you enable backup for your Ops Manager deployment, you must
  configure the oplog store to
  use the replica set that you created for the backup database in this
  tutorial. If you *also* choose to use a `blockstore` or
  `S3 snapshot store` to store your
  snapshots, you must
  deploy one Replica Set for
  each blockstore or
  S3 blockstore
  metadata database.
