<!-- Converted from reference/mongodb-compatibility.txt (reStructuredText). Includes are inlined. -->

# MongoDB Compatibility Matrix

This page describes compatibility between Ops Manager features and MongoDB.

## MongoDB Versions Compatible with Ops Manager

Ops Manager can manage databases that run specific versions of MongoDB.
The following table displays the version compatibility. The MongoDB
edition can be either Community or Enterprise.

**Important:**

This section only describes compatibility between versions of
Ops Manager and versions of MongoDB Server. It does not cover
compatibility between versions of MongoDB Server and Ops Manager
backing databases. To learn more about backing database
compatibility, see compatible-mdb-versions.

| MongoDB Version | Ops Manager 7.0 | Ops Manager 6.0 | Ops Manager 5.0 | Ops Manager 4.4 | Ops Manager 4.2 |
|---|---|---|---|---|---|
| MongoDB 7.0 | Supported | N/A | N/A | N/A | N/A |
| MongoDB 6.0 | Supported | Supported | N/A | N/A | N/A |
| MongoDB 5.0 | Supported | Supported | Supported | N/A | N/A |
| MongoDB 4.4 | Supported | Supported | Supported | Supported | N/A |
| MongoDB 4.2 | Deprecated | Supported | Supported | Supported | Supported |

**Note:**

A deprecated version still works with the corresponding Ops Manager
release, but we will remove the support for this version in the
next release. [MongoDB Support](https://support.mongodb.com) recommends migrating to a supported
version to avoid potential incompatibility issues.

To learn more, see [MongoDB Legacy Support Policy](https://www.mongodb.com/legal/support-policy/legacy) and 
[MongoDB Software Lifecycle Schedules for Ops Manager](https://www.mongodb.com/legal/support-policy/lifecycles).

Version support covers the full release series from the first to the
last release.

**See also:**

To learn more about MongoDB versioning, see
release-version-numbers in the MongoDB Manual.

### LDAP (Lightweight Directory Access Protocol) Authorization Compatibility

LDAP authorization
was added to MongoDB Enterprise with version 3.4. This feature
allows you to assign roles to users using LDAP (Lightweight Directory Access Protocol). This feature was
later changed to provide additional security with MongoDB 3.4.11.
Ops Manager 3.4.13 or later,
3.6.3 or later, and
4.0.0 or later are compatible with
MongoDB versions 3.4.11 or later.

### BI Connector Compatibility

Ops Manager 7.0 supports the entire MongoDB release series from
6.0.0 to 6.0.21.

**See also:**

To learn more about MongoDB versioning, see
release-version-numbers in the MongoDB Manual.

### LDAP (Lightweight Directory Access Protocol) Authorization Compatibility

LDAP authorization
was added to MongoDB Enterprise with version 3.4. This feature
allows you to assign roles to users using LDAP (Lightweight Directory Access Protocol). This feature was
later changed to provide additional security with MongoDB 3.4.11.
Ops Manager 3.4.13 or later,
3.6.3 or later, and
4.0.0 or later are compatible with
MongoDB versions 3.4.11 or later.

### BI Connector Compatibility

To use the `MongoDB Connector for BI` on Ops Manager 6.0.0 or later, you must use MongoDB 4.0
or later.

If your BI Connector runs MongoDB 3.6, you must disable the
BI Connector, or update MongoDB to 4.0 before you upgrade Ops Manager
to 6.0.0 or later.

### Backup Considerations for MongoDB Versions

To learn more about backup considerations specific to MongoDB
4.4 and later and 4.2 and earlier, see 4.2-backup-considerations.

To learn more about MongoDB versioning, see release-version-numbers
in the MongoDB Manual.

## Agent Compatibility

The following table lists the Ops Manager versions that are compatible with the 
associated MongoDB Agent release series.

| Ops Manager Version | MongoDB Agent Release Series |
|---|---|
| 7.0 | 107.0.x |
| 6.0 | 12.0.x |

### Monitoring Compatibility

To monitor a deployment running MongoDB 3.6 or later release series,
you must use Monitoring Agent version 2.7.0 or later.

### Automation PowerPC Compatibility

To manage PowerPC Linux-based hosts, you must use
automation-3.2.7.1927 or later.

### Backup Compatibility

To back up MongoDB deployments running the 3.6 or later release
series, upgrade to backup-6.0.3.689 or later.

## MongoDB Deployment Types

Using Ops Manager, you can configure all MongoDB deployment types: sharded
clusters, replica sets, and standalones.

The shards in a sharded cluster **must** be replica sets. That is, a
shard cannot be a standalone mongod. If you must run a shard
as a single mongod (which provides **no** redundancy or
failover), run the shard as a single-member replica set.

**Note:**

You may not upgrade a sharded MongoDB deployment to version 3.4 if 
the deployment uses mirrored mongod instances as config 
servers. To allow the sharded deployment to be upgraded, see 
/tutorial/convert-config-servers-to-replica-set. The 
conversion requires that the sharded deployment run MongoDB version
3.2.4 or later. Deployments running previous versions must upgrade
to version 3.2.4 before an upgrade to version 3.4.
