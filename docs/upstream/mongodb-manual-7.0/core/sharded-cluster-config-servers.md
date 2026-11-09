<!-- Converted from core/sharded-cluster-config-servers.txt (reStructuredText). Includes are inlined. -->

# Config Servers

Config servers store the metadata for a sharded cluster. The metadata
reflects state and organization for all data and components within the
sharded cluster. The metadata includes the list of chunks on every shard and
the ranges that define the chunks.

The `mongos` instances cache this data and use it to route
read and write operations to the correct shards. `mongos`
updates the cache when there are metadata changes for the cluster, such
as adding a shard. Shards also read 
chunk metadata from the config servers.

The config servers also store authentication configuration
information such as Role-Based Access
Control or internal
authentication settings for
the cluster.

MongoDB also uses the config servers to manage distributed locks.

Each sharded cluster must have its own config servers. Do not use the
same config servers for different sharded clusters.

**Warning:**

Administrative operations conducted on config servers may have significant
impact on sharded cluster performance and availability. Depending on the
number of config servers impacted, the cluster may be read-only or
offline for a period of time.

## Replica Set Config Servers

**Changed in version:** 3.4

Config servers for sharded clusters can be
deployed as a replica set (CSRS). 
Using a replica set for the config
servers improves consistency across the config servers, since MongoDB
can take advantage of the standard replica set read and write protocols
for the config data. In addition, using a replica set for config
servers allows a sharded cluster to have more than 3 config servers
since a replica set can have up to 50 members. To deploy config servers
as a replica set, the config servers must run the storage-wiredtiger. 

The following restrictions apply to a replica set configuration when used
for config servers:

- Must have zero arbiters.

- Must have no delayed members.

- Must build indexes (i.e. no member should have
  `members[n].buildIndexes` setting set to false).

## Read and Write Operations on Config Servers

The `admin` database and the config database exist on the config servers.

### Writes to Config Servers

The `admin` database contains the collections related to the
authentication and authorization as well as the other system.*
collections for internal use.

The config database contains the
collections that contain the sharded cluster metadata. MongoDB writes
data to the config database when
the metadata changes, such as after a chunk migration or a chunk split.

Users should avoid writing directly to the config database in the
course of normal operation or maintenance.

When writing to the config servers, MongoDB uses a write concern of `"majority"`.

### Reads from Config Servers

MongoDB reads from the `admin` database for authentication and
authorization data and other internal uses.

MongoDB reads from the `config` database when a `mongos`
starts or after a change in the metadata, such as after a chunk
migration. Shards also read chunk metadata from the config servers.

When reading from the replica set config servers, MongoDB uses a
/reference/read-concern level of `"majority"`.

## Config Server Availability

If the config server replica set loses its primary and cannot elect a
primary, the cluster's metadata becomes *read only*. You can still read
and write data from the shards, but no chunk migration or chunk splits
will occur until the replica set can elect a primary. 

In a sharded cluster, `mongod` and `mongos` instances
monitor the replica sets in the sharded cluster (e.g. shard replica
sets, config server replica set).

If all config servers become unavailable, the cluster can become
inoperable. To ensure that the config servers remain available and
intact, backups of config servers are critical. The data on the config
server is small compared to the data stored in a cluster, and the
config server has a relatively low activity load.

See sharding-config-servers-and-availability for more
information.

## Sharded Cluster Metadata

Config servers store metadata in the /reference/config-database.

**Important:**

Always back up the `config` database before doing any
maintenance on the config server.

To access the `config` database, issue the following command in
`mongosh`:

```javascript
use config
```

In general, you should *never* edit the content of the `config`
database directly. The `config` database contains the following
collections:

- `changelog`
- `chunks`
- `collections`
- `databases`
- `csrs.indexes`
- `mongos`
- `placementHistory`
- `settings`
- `shards`
- `version`

For more information on these collections and their role in sharded
clusters, see /reference/config-database. See
config-server-read-write-ops for more information about reads
and updates to the metadata.

## Sharded Cluster Security

Use /core/security-internal-authentication to enforce intra-cluster
security and prevent unauthorized cluster components from accessing the
cluster. You must start each `mongod` in the cluster with the
appropriate security settings in order to enforce internal authentication.

Starting in MongoDB 5.3, SCRAM-SHA-1
cannot be used for intra-cluster authentication. Only
SCRAM-SHA-256 is supported.

In previous MongoDB versions, SCRAM-SHA-1 and SCRAM-SHA-256 can both be
used for intra-cluster authentication, even if SCRAM is not explicitly
enabled.

See /tutorial/deploy-sharded-cluster-with-keyfile-access-control for a
tutorial on deploying a secured sharded cluster.
