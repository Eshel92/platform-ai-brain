<!-- Converted from tutorial/deploy-replica-set.txt (reStructuredText). Includes are inlined. -->

# Deploy a Self-Managed Replica Set

This tutorial describes how to create a three-member replica
set from three existing `mongod` instances running with
access control disabled.

To deploy a replica set with enabled access control, see
deploy-repl-set-with-auth. If you wish to deploy a
replica set from a single MongoDB instance, see
/tutorial/convert-standalone-to-replica-set. For more
information on replica set deployments, see the /replication and
/core/replica-set-architectures documentation.

## Overview

Three member replica sets provide enough
redundancy to survive most network partitions and other system
failures. These sets also have sufficient capacity for many distributed
read operations. Replica sets should always have an odd number of
members. This ensures that elections will proceed smoothly. For more about
designing replica sets, see the Replication overview.

This page covers how to deploy a replica set for self-managed 
deployments.

To learn more about deploying a replica set for deployments hosted in MongoDB
Atlas, see Create a Cluster.

## Requirements

For production deployments, you should maintain as much separation between
members as possible by hosting the `mongod`
instances on separate machines. When using virtual machines for
production deployments, you should place each `mongod`
instance on a separate host server serviced by redundant power circuits
and redundant network paths.

Before you can deploy a replica set, you must install MongoDB on
each system that will be part of your replica set.
If you have not already installed MongoDB, see the installation tutorials.

## Considerations When Deploying a Replica Set

### Architecture

In production, deploy each member of the replica set to its own machine.
If possible, ensure that MongoDB listens on the default port of 
`27017`.

**Note:**

Outside of a rolling upgrade, all `mongod` members of 
a replica set should use the same major version of 
MongoDB.

For more information, see /core/replica-set-architectures.

### Hostnames

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

### IP Binding

Use the `--bind_ip` option to ensure that
MongoDB listens for connections from applications on configured
addresses.

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

MongoDB binaries, `mongod` and `mongos`, bind
to localhost by default. If the `net.ipv6` configuration file
setting or the `--ipv6` command line option is set for the binary,
the binary additionally binds to the localhost IPv6 address.

By default `mongod` and `mongos` that are
bound to localhost only accept connections from clients that are
running on the same computer. This binding behavior includes
`mongosh` and other members of your replica set or sharded
cluster. Remote clients cannot connect to binaries that are bound only
to localhost.

To override the default binding and bind to other IP addresses, use the
`net.bindIp` configuration file setting or the `--bind_ip`
command-line option to specify a list of hostnames or IP addresses.

**Warning:**

Starting in MongDB 5.0, [split horizon DNS](https://en.wikipedia.org/wiki/Split-horizon_DNS) nodes that are
only configured with an IP address fail startup validation and
report an error. See `disableSplitHorizonIPCheck`.

For example, the following `mongod` instance binds to both
the localhost and the hostname `My-Example-Associated-Hostname`, which is
associated with the IP address `198.51.100.1`:

```none
mongod --bind_ip localhost,My-Example-Associated-Hostname
```

In order to connect to this instance, remote clients must specify
the hostname  or its associated IP address `198.51.100.1`:

```none
mongosh --host My-Example-Associated-Hostname

mongosh --host 198.51.100.1
```

### Connectivity

Ensure that network traffic can pass securely between all members of the set and
all clients in the network .

Consider the following:

- Establish a virtual private network. Ensure that your network topology
  routes all traffic between members within a single site over the local
  area network.

- Configure access control to prevent connections from unknown clients
  to the replica set.

- Configure networking and firewall rules so that incoming and outgoing
  packets are permitted only on the default MongoDB port and only from
  within your deployment. See the IP Binding considerations.

Ensure that each member of a replica set is accessible by
way of resolvable DNS or hostnames. You should either configure your
DNS names appropriately or set up your systems' `/etc/hosts` file to
reflect this configuration.

Each member must be able to connect to every other member. For
instructions on how to check your connection, see
replica-set-troubleshooting-check-connection.

### Configuration

Create the directory where MongoDB stores data files before deploying
MongoDB.

Specify the `mongod` configuration in a configuration
file stored in `/etc/mongod.conf`
or a related location.

For more information about configuration options, see
/reference/configuration-options.

## Deploy a Replica Set in the Terminal

This tutorial describes how to create a three-member 
replica set from three existing `mongod` instances
running with access control disabled.

To deploy a replica set with enabled access control, see
deploy-repl-set-with-auth. If you wish to deploy a
replica set from a single MongoDB instance, see
server-replica-set-deploy-convert. For more
information on replica set deployments, see the replication and
replica-set-architecture documentation.

**Step 1: Start each member of the replica set with the appropriate options.**

For each member, start a `mongod` instance with the
following settings:

- Set `replication.replSetName` option to the replica set 
  name. If your application connects to more than one replica set, 
  each set must have a distinct name.

- Set `net.bindIp` option to the hostname/ip or a comma-delimited
  list of hostnames/ips.

- Set any other settings as appropriate for your deployment.

In this tutorial, the three `mongod` instances are
associated with the following hosts:

| Replica Set Member | Hostname |
|---|---|
| Member 0 | `mongodb0.example.net` |
| Member 1 | `mongodb1.example.net` |
| Member 2 | `mongodb2.example.net` |

The following example specifies the replica set name and the ip
binding through the `--replSet` and `--bind_ip`
command-line options:

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

```bash
mongod --replSet "rs0" --bind_ip localhost,<hostname(s)|ip address(es)>
```

For `<hostname(s)|ip address(es)>`, specify the hostname(s) and/or
ip address(es) for your `mongod` instance that remote
clients (including the other members of the replica set) can use to
connect to the instance.

Alternatively, you can also specify the `replica set name` and the `ip addresses` in a configuration file:

```yaml
replication:
   replSetName: "rs0"
net:
   bindIp: localhost,<hostname(s)|ip address(es)>
```

To start `mongod` with a configuration file, specify the
configuration file's path with the `--config` option:

```bash
mongod --config <path-to-config>
```

In production deployments, you can configure a init script
to manage this process. Init scripts are beyond the scope of this
document.

**Step 2: Connect `mongosh` to one of the `mongod` instances.**

From the same machine where one of the `mongod` is running
(in this tutorial, `mongodb0.example.net`), start
`mongosh`. To connect to the `mongod`
listening to localhost on the default port of `27017`, simply issue:

```sh
mongosh
```

Depending on your path, you may need to specify the path to the
`mongosh` binary.

If your `mongod` is not running on the default port, specify the
`--port` option for `mongosh`.

**Step 3: Initiate the replica set.**

From `mongosh`, run `rs.initiate()` on
replica set member 0.

**Important:**

Run `rs.initiate()` on *just one and only one*
`mongod` instance for the replica set.

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

```javascript
rs.initiate( {
   _id : "rs0",
   members: [
      { _id: 0, host: "mongodb0.example.net:27017" },
      { _id: 1, host: "mongodb1.example.net:27017" },
      { _id: 2, host: "mongodb2.example.net:27017" }
   ]
})
```

MongoDB initiates a replica set, using 
the default replica set configuration.

**Step 4: View the replica set configuration.**

Use `rs.conf()` to display the replica set configuration
object:

```javascript
rs.conf()
```

The replica set configuration object resembles the following:

```javascript
{
   "_id" : "rs0",
   "version" : 1,
   "protocolVersion" : NumberLong(1),
   "members" : [
      {
         "_id" : 0,
         "host" : "mongodb0.example.net:27017",
         "arbiterOnly" : false,
         "buildIndexes" : true,
         "hidden" : false,
         "priority" : 1,
         "tags" : {

         },
         "secondaryDelaySecs" : NumberLong(0),
         "votes" : 1
      },
      {
         "_id" : 1,
         "host" : "mongodb1.example.net:27017",
         "arbiterOnly" : false,
         "buildIndexes" : true,
         "hidden" : false,
         "priority" : 1,
         "tags" : {

         },
         "secondaryDelaySecs" : NumberLong(0),
         "votes" : 1
      },
      {
         "_id" : 2,
         "host" : "mongodb2.example.net:27017",
         "arbiterOnly" : false,
         "buildIndexes" : true,
         "hidden" : false,
         "priority" : 1,
         "tags" : {

         },
         "secondaryDelaySecs" : NumberLong(0),
         "votes" : 1
      }

   ],
   "settings" : {
      "chainingAllowed" : true,
      "heartbeatIntervalMillis" : 2000,
      "heartbeatTimeoutSecs" : 10,
      "electionTimeoutMillis" : 10000,
      "catchUpTimeoutMillis" : -1,
      "getLastErrorModes" : {

      },
      "getLastErrorDefaults" : {
         "w" : 1,
         "wtimeout" : 0
      },
      "replicaSetId" : ObjectId("585ab9df685f726db2c6a840")
   }
}
```

**Step 5: Ensure that the replica set has a primary.**

Use `rs.status()` to identify the primary in the replica set.

**See also:**

deploy-repl-set-with-auth
