<!-- Converted from tutorial/restart-sharded-cluster.txt (reStructuredText). Includes are inlined. -->

# Restart a Self-Managed Sharded Cluster

The tutorial is specific to MongoDB 6.0. For earlier 
versions of MongoDB, refer to the corresponding version of the MongoDB 
Manual.

This procedure demonstrates the shutdown and startup sequence for restarting
a sharded cluster. Stopping or starting the components of a sharded cluster
in a different order may cause communication errors between members. For
example, shard servers may appear to hang
if there are no config servers
available.

**Important:** This procedure should only be performed during a planned

maintenance period. During this period, applications should stop
all reads and writes to the cluster in order to prevent potential
data loss or reading stale data.

## Disable the Balancer

Disable the balancer to stop chunk migration and do not perform any metadata
write operations until the process finishes. If a migration is in
progress, the balancer will complete the in-progress migration before
stopping.

To disable the balancer, connect to one of the cluster's
`mongos` instances and issue the following command: [#autosplit-stop]_

```javascript
sh.stopBalancer()
```

To check the balancer state, issue the `sh.getBalancerState()`
command.

For more information, see sharding-balancing-disable-temporarily.

## Stop Sharded Cluster

**Step 1: Stop `mongos` routers.**

Run `db.shutdownServer()` from the `admin` database on each
`mongos` router:

```javascript
use admin
db.shutdownServer()
```

**Step 2: Stop each shard replica set.**

Run `db.shutdownServer()` from the `admin` database on each
shard replica set member to shutdown
its `mongod` process. Shutdown all secondary members
before shutting down the primary in each replica set.

**Step 3: Stop config servers.**

Run `db.shutdownServer()` from the `admin` database on each
of the config servers to
shutdown its `mongod` process. Shutdown all
secondary members before shutting down the primary.

## Start Sharded Cluster

**Step 1: Start config servers.**

When starting each `mongod`, specify the
`mongod` settings using either a configuration file or the
command line. For more information on startup parameters, see the
`mongod` reference page.

**Configuration File**

If using a configuration file, start the `mongod` with
the `--config` option set to the configuration file path.

```sh
mongod --config <path-to-config-file>
```

**Command Line**

If using the command line options, start the `mongod`
with the `--configsvr`, `--replSet`, `--bind_ip`,
and other options as appropriate to your deployment. For example:

```sh
mongod --configsvr --replSet <replica set name> --dbpath <path> --bind_ip localhost,<hostname(s)|ip address(es)>
```

After starting all config servers, connect to the primary
`mongod` and run `rs.status()` to confirm the
health and availability of each CSRS member.

**Step 2: Start each shard replica set.**

When starting each `mongod`, specify the
`mongod` settings using either a configuration file or the
command line.

**Configuration File**

If using a configuration file, start the `mongod` with
the `--config` option set to the configuration file path.

```sh
mongod --config <path-to-config-file>
```

**Command Line**

If using the command line option,  start the `mongod` with
the `--replSet`, `--shardsvr`, and `--bind_ip` options,
and other options as appropriate to your deployment.  For example:

```sh
mongod --shardsvr --replSet <replSetname> --dbpath <path> --bind_ip localhost,<hostname(s)|ip address(es)>
```

After starting all members of each shard, connect to each primary
`mongod` and run `rs.status()` to confirm the health
and availability of each member.

**Step 3: Start `mongos` routers.**

Start `mongos` routers using either a configuration file or a
command line parameter to specify the config servers.

**Configuration File**

If using a configuration file, start the `mongos` specifying
the `--config` option and the path to the configuration file.

```shell
mongos --config <path-to-config>
```

For more information on the configuration file, see
configuration options.

**Command Line**

If using command line parameters, start the `mongos` and specify
the `--configdb`,  `--bind_ip`,
and other options as appropriate to your deployment. For example:

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

```sh
mongos --configdb <configReplSetName>/cfg1.example.net:27019,cfg2.example.net:27019 --bind_ip localhost,<hostname(s)|ip address(es)>
```

Include any other options as appropriate for your deployment.

## Re-Enable the Balancer

Re-enable the balancer to resume
chunk migrations.

Connect to one of the cluster's `mongos` instances and run
the `sh.startBalancer()` command: [#autosplit-start]_

```javascript
sh.startBalancer()
```

To check the balancer state, issue the `sh.getBalancerState()`
command.

For more information, see sharding-balancing-enable.

## Validate Cluster Accessibility

Connect a `mongo` shell to one of the cluster's
`mongos` processes. Use `sh.status()`
to check the overall cluster status.

To confirm that all shards are accessible and communicating, insert
test data into a temporary sharded collection. Confirm that data is
being split and migrated between each shard in your cluster. You can
connect a `mongo` shell to each shard primary and
use `db.collection.find()` to validate that the data was
sharded as expected.

**Important:** To prevent potential data loss or reading stale data,

do not start application reads and writes to the cluster
until after confirming the cluster is healthy and accessible.
