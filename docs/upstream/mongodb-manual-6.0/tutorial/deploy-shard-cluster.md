<!-- Converted from tutorial/deploy-shard-cluster.txt (reStructuredText). Includes are inlined. -->

# Deploy a Self-Managed Sharded Cluster

## Overview

This tutorial involves creating a new sharded cluster that consists of a
`mongos`, the config server replica set, and two shard
replica sets.

## Considerations

### Connectivity

Each member of a sharded cluster must be able to connect to *all* other
members in the cluster. This includes all shards and config servers.
Ensure that network and security systems, including all interface and
firewalls, allow these connections.

### Hostnames and Configuration

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

#### Localhost Deployments

If you use either `localhost` or its IP address as the hostname
portion of any host identifier, you *must* use that identifier as the
host setting for any other MongoDB component in the cluster.

For example, the `sh.addShard()` method takes a `host`
parameter for the hostname of the target shard. If you set `host` to
`localhost`, you must then use `localhost` as the host for all other
shards in the cluster.

### Security

This tutorial does *not* include the required steps for configuring
/core/security-internal-authentication or
/core/authorization.

In production environments, sharded clusters should employ at
minimum /core/security-x.509 security for internal authentication
and client access.

## Procedure

### Create the Config Server Replica Set

The following steps deploys a config server replica set.

For a production deployment, deploy a config server replica set with at
least three members. For testing purposes, you can create a
single-member replica set.

**Note:**

The config server replica set must not use the same name as any of
the shard replica sets.

For this tutorial, the config server replica set members are associated
with the following hosts:

| Config Server Replica Set Member | Hostname |
|---|---|
| Member 0 | `cfg1.example.net` |
| Member 1 | `cfg2.example.net` |
| Member 2 | `cfg3.example.net` |

**Step 1: Start each member of the config server replica set.**

When starting *each* `mongod`, specify the
`mongod` settings either via a configuration file or the
command line.

**config-file:**

If using a configuration file, set:

```yaml
sharding:
  clusterRole: configsvr
replication:
  replSetName: <replica set name>
net:
  bindIp: localhost,<hostname(s)|ip address(es)>
```

- `sharding.clusterRole` to `configsvr`, 

- `replication.replSetName` to the desired name of the
  config server replica set,

- `net.bindIp` option to the hostname/ip address or
  comma-delimited list of hostnames or ip addresses that remote
  clients (including the other members of the config server
  replica set as well as other members of the sharded cluster)
  can use to connect to the instance.

  **Warning:**

  Before binding to a non-localhost (e.g. publicly accessible) 
  IP address, ensure you have secured your cluster from unauthorized
  access. For a complete list of security recommendations, see 
  /administration/security-checklist. At minimum, consider 
  enabling authentication and 
  hardening network infrastructure.

- Additional settings as appropriate to your deployment, such as
  `storage.dbPath` and `net.port`. For more
  information on the configuration file, see configuration
  options.

Start the `mongod` with the `--config` option
set to the configuration file path.

```bash
mongod --config <path-to-config-file>
```

**command-line:**

If using the command line options, start the
`mongod` with the `--configsvr`, `--replSet`,
`--bind_ip`, and other options as appropriate to your
deployment. For example:

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

```bash
mongod --configsvr --replSet <replica set name> --dbpath <path> --bind_ip localhost,<hostname(s)|ip address(es)>
```

For more information on startup parameters, see the
`mongod` reference page.

**Step 2: Connect to one of the config servers.**

Connect `mongosh` to one of the config server 
members. 

```sh
mongosh --host <hostname> --port <port>
```

**Step 3: Initiate the replica set.**

From `mongosh`, run the `rs.initiate()` method.

`rs.initiate()` can take an optional replica set
configuration document. In the
replica set configuration document, include:

- The `_id` set to the replica set name specified in either
  the `replication.replSetName` or the `--replSet` option.

- The `configsvr` field  set to `true` for the config server replica set.

- The `members` array with a document per each member of the replica set.

**Important:**

Run `rs.initiate()` on *just one and only one*
`mongod` instance for the replica set.

```javascript
rs.initiate(
  {
    _id: "myReplSet",
    configsvr: true,
    members: [
      { _id : 0, host : "cfg1.example.net:27019" },
      { _id : 1, host : "cfg2.example.net:27019" },
      { _id : 2, host : "cfg3.example.net:27019" }
    ]
  }
)
```

See /reference/replica-configuration for more information on 
replica set configuration documents.

**Note:**

The `rs.initiate` command may take a few seconds to complete.
To use the config server replica set (CSRS) in this procedure, you must wait
until it completes its initialization.  If the CSRS has not initialized, you 
will see `NotYetInitialized` errors when you try to perform operations on a
CSRS member.

Once the config server replica set (CSRS) is initiated and up, proceed
to creating the shard replica sets.

### Create the Shard Replica Sets

For a production deployment, use a replica set with at least three
members. For testing purposes, you can create a single-member replica
set.

**Note:**

Shard replica sets must not use the same name as the config server replica set.

For each shard, use the following steps to create the shard replica set:

**Step 1: Start each member of the shard replica set.**

When starting *each* `mongod`, specify the
`mongod` settings either via a configuration file or the
command line.

**config-file:**

If using a configuration file, set:

```yaml
sharding:
    clusterRole: shardsvr
replication:
    replSetName: <replSetName>
net:
    bindIp: localhost,<ip address>
```

- `replication.replSetName` to the desired name of the
  replica set,

- `sharding.clusterRole` option to `shardsvr`,

- `net.bindIp` option to the ip or a comma-delimited
  list of ips that remote clients (including the other members
  of the config server replica set as well as other members of
  the sharded cluster) can use to connect to the instance.

  **Warning:**

  Before binding to a non-localhost (e.g. publicly accessible) 
  IP address, ensure you have secured your cluster from unauthorized
  access. For a complete list of security recommendations, see 
  /administration/security-checklist. At minimum, consider 
  enabling authentication and 
  hardening network infrastructure.

- Additional settings as appropriate to your deployment, such as
  `storage.dbPath` and `net.port`. For more
  information on the configuration file, see configuration
  options.

Start the `mongod` with the `--config` option set
to the configuration file path.

```bash
mongod --config <path-to-config-file>
```

**command-line:**

If using the command line option,  start the `mongod` with
the `--replSet`, and `--shardsvr`, `--bind_ip` options,
and other options as appropriate to your deployment.  For example:

```bash
mongod --shardsvr --replSet <replSetname>  --dbpath <path> --bind_ip localhost,<hostname(s)|ip address(es)>
```

For more information on startup parameters, see the
`mongod` reference page.

**Step 2: Connect to one member of the shard replica set.**

Connect `mongosh` to one of the replica set members.

```sh
mongosh --host <hostname> --port <port>
```

**Step 3: Initiate the replica set.**

From `mongosh`, run the `rs.initiate()` method.

`rs.initiate()` can take an optional replica set
configuration document. In the
replica set configuration document, include:

- The `_id` field set to the replica set name specified in
  either the `replication.replSetName` or the `--replSet`
  option.

- The `members` array with a document per each member of the
  replica set.

The following example initiates a three member replica set.

**Important:**

Run `rs.initiate()` on *just one and only one*
`mongod` instance for the replica set.

```javascript
rs.initiate(
  {
    _id : "myReplSet",
    members: [
      { _id : 0, host : "s1-mongo1.example.net:27018" },
      { _id : 1, host : "s1-mongo2.example.net:27018" },
      { _id : 2, host : "s1-mongo3.example.net:27018" }
    ]
  }
)
```

### Start a `mongos` for the Sharded Cluster

Start a `mongos` using either a configuration file or a
command line parameter to specify the config servers.

**config-file:**

If using a configuration file, set the
`sharding.configDB` to the config server replica set
name and at least one member of the replica set in
`<replSetName>/<host:port>` format.

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

```yaml
sharding:
  configDB: <configReplSetName>/cfg1.example.net:27019,cfg2.example.net:27019
net:
  bindIp: localhost,<hostname(s)|ip address(es)>
```

Start the `mongos` specifying the `--config`
option and the path to the configuration file.

```bash
mongos --config <path-to-config>
```

For more information on the configuration file, see 
configuration options.

**command-line:**

If using command line parameters start the `mongos`
and specify the `--configdb`,  `--bind_ip`, and other
options as appropriate to your deployment. For example:

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

```bash
mongos --configdb <configReplSetName>/cfg1.example.net:27019,cfg2.example.net:27019,cfg3.example.net:27019 --bind_ip localhost,<hostname(s)|ip address(es)>
```

Include any other options as appropriate for your deployment.

At this point, your sharded cluster consists of the
`mongos` and the config servers.  You can now connect to
the sharded cluster using `mongosh`.

### Connect to the Sharded Cluster

Connect `mongosh` to the `mongos`. 
Specify the `host` and `port` on which the `mongos` is running:

```bash
mongosh --host <hostname> --port <port>
```

Once you have connected `mongosh` to the
`mongos`, continue to the next procedure to add shards to
the cluster.

### Add Shards to the Cluster

In a `mongosh` session that is connected to the
`mongos`, use the `sh.addShard()` method to add
each shard to the cluster.

The following operation adds a single shard replica set to the cluster:

```javascript
sh.addShard( "<replSetName>/s1-mongo1.example.net:27018,s1-mongo2.example.net:27018,s1-mongo3.example.net:27018")
```

Repeat these steps until the cluster includes all desired shards.

### Shard a Collection

To shard a collection, connect `mongosh` to the
`mongos` and use the `sh.shardCollection()` method. 

**Note:** Sharding and Indexes

If the collection already contains data, you must
create an index that supports the
shard key before sharding the collection. If the collection
is empty, MongoDB creates the index as part of
`sh.shardCollection()`.

MongoDB provides two strategies to shard collections:

- Hashed sharding uses a
  hashed index of a single field as the
  shard key to partition data across your sharded cluster.

  ```javascript
  sh.shardCollection("<database>.<collection>", { <shard key field> : "hashed" } )
  ```

- Range-based sharding can use multiple
  fields as the shard key and divides data into contiguous ranges
  determined by the shard key values.

  ```javascript
  sh.shardCollection("<database>.<collection>", { <shard key field> : 1, ... } )
  ```

### Shard Key Considerations

Your selection of shard key affects the efficiency of sharding,
as well as your ability to take advantage of certain sharding
features such as zones. To learn how to choose
an effective shard key, see sharding-shard-key-selection.

`mongosh` provides the method `convertShardKeyToHashed()`. 
This method uses the same hashing function as the hashed index and
can be used to see what the hashed value would be for a key.

**See also:**

- For hashed sharding shard keys, see
  hashed-sharding-shard-key

- For ranged sharding shard keys, see
  sharding-ranged-shard-key
