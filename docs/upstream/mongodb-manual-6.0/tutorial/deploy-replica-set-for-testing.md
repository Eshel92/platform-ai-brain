<!-- Converted from tutorial/deploy-replica-set-for-testing.txt (reStructuredText). Includes are inlined. -->

# Deploy a Self-Managed Replica Set for Testing and Development

This procedure describes deploying a replica set in a development or
test environment. For a production deployment, refer to the
/tutorial/deploy-replica-set tutorial.

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

## Requirements

For test and development systems, you can run your `mongod`
instances on a local system, or within a virtual instance.

Before you can deploy a replica set, you must install MongoDB on
each system that will be part of your replica set.
If you have not already installed MongoDB, see the installation tutorials.

Each member must be able to connect to every other member. For
instructions on how to check your connection, see
replica-set-troubleshooting-check-connection.

## Considerations

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

### IP Binding

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

In this test deployment, the three members run on the same machine.

### Replica Set Naming

**Important:** These instructions should only be used for test or

development deployments.

The examples in this procedure create a new replica set named `rs0`.

If your application connects to more than one replica set, each set must
have a distinct name. Some drivers group replica set connections by 
replica set name.

## Procedure

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

1. Create the necessary data directories for each member by issuing a
   command similar to the following:

   ```bash
   mkdir -p /srv/mongodb/rs0-0  /srv/mongodb/rs0-1 /srv/mongodb/rs0-2
   ```

   This will create directories called "rs0-0", "rs0-1", and "rs0-2", which
   will contain the instances' database files.

#. Start your `mongod` instances in their own shell windows by issuing the following
   commands:

   **Warning:**

   Before binding to a non-localhost (e.g. publicly accessible) 
   IP address, ensure you have secured your cluster from unauthorized
   access. For a complete list of security recommendations, see 
   /administration/security-checklist. At minimum, consider 
   enabling authentication and 
   hardening network infrastructure.

   First member:

   ```bash
   mongod --replSet rs0 --port 27017 --bind_ip localhost,<hostname(s)|ip address(es)> --dbpath /srv/mongodb/rs0-0  --oplogSize 128
   ```

   Second member:

   ```bash
   mongod --replSet rs0 --port 27018 --bind_ip localhost,<hostname(s)|ip address(es)> --dbpath /srv/mongodb/rs0-1  --oplogSize 128
   ```

   Third member:

   ```bash
   mongod --replSet rs0 --port 27019 --bind_ip localhost,<hostname(s)|ip address(es)> --dbpath /srv/mongodb/rs0-2 --oplogSize 128
   ```

   This starts each instance as a member of a replica set named
   `rs0`, each running on a distinct port, and specifies the path to
   your data directory with the `--dbpath` setting.
   If you are already using the suggested ports, select different ports.

   The instances bind to both the localhost and the ip address
   of the host.

   The `--oplogSize` setting reduces the
   disk space that each `mongod` instance uses. [#oplog]_
   This is ideal for testing and development deployments as it prevents
   overloading your machine. For more information on this and other
   configuration options, see /reference/configuration-options.

#. Connect to one of your `mongod` instances through
   `mongosh`. You will need to indicate which instance by
   specifying its port number. For the sake of simplicity and clarity,
   you may want to choose the first one, as in the following command;

   ```bash
   mongosh --port 27017
   ```

#. In `mongosh`, use `rs.initiate()` to
   initiate the replica set. You can create a replica set
   configuration object in `mongosh` environment, as
   in the following example:

   ```javascript
   rsconf = {
     _id: "rs0",
     members: [
       {
        _id: 0,
        host: "<hostname>:27017"
       },
       {
        _id: 1,
        host: "<hostname>:27018"
       },
       {
        _id: 2,
        host: "<hostname>:27019"
       }
      ]
   }
   ```

   replacing `<hostname>` with your system's hostname,
   and then pass the `rsconf` file to `rs.initiate()` as
   follows:

   ```javascript
   rs.initiate( rsconf )
   ```

#. Display the current replica configuration
   by issuing the following command:

   ```javascript
   rs.conf()
   ```

   The replica set configuration object resembles the following:
   

   ```json
   {
      "_id" : "rs0",
      "version" : 1,
      "protocolVersion" : NumberLong(1),
      "members" : [
         {
            "_id" : 0,
            "host" : "<hostname>:27017",
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
            "host" : "<hostname>:27018",
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
            "host" : "<hostname>:27019",
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
         "replicaSetId" : ObjectId("598f630adc9053c6ee6d5f38")
      }
   }
   ```

Check the status of your replica set at any time with the
`rs.status()` operation.

**See also:**

The documentation of the following shell functions for
more information:

- `rs.initiate()`
- `rs.conf()`
- `rs.reconfig()`
- `rs.add()`

You may also consider the [simple setup script](https://github.com/mongodb/mongo-snippets/blob/master/replication/simple-setup.py)
as an example of a basic automatically-configured replica set.

Refer to Replica Set Read and Write Semantics
for a detailed explanation of read and write semantics in MongoDB.
