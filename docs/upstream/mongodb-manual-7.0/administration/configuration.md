<!-- Converted from administration/configuration.txt (reStructuredText). Includes are inlined. -->

# Run-time Database Configuration for Self-Managed Deployments

The command line and configuration
file interfaces provide MongoDB
administrators with a large number of options and settings for
controlling the operation of the database system. This document
provides an overview of common configurations and examples of
best-practice configurations for common use cases.

While both interfaces provide access to the same collection of options
and settings, this document primarily uses the configuration file
interface.

- If you installed MongoDB with a package manager
  such as `yum` or `apt` on Linux or `brew` on macOS, or with the
  MSI installer on Windows, a default configuration file has been provided as part of your
  installation:

  | Platform | Method | Configuration File |
  |---|---|---|
  | Linux | `apt`, `yum`, or `zypper` Package Manager | `/etc/mongod.conf` |
  | macOS | `brew` Package Manager | `/usr/local/etc/mongod.conf` (on Intel processors), or `/opt/homebrew/etc/mongod.conf` (on [Apple M1 processors](https://support.apple.com/en-us/HT211814)) |
  | Windows | MSI Installer | `<install directory>\bin\mongod.cfg` |

- If you installed MongoDB
  through a downloaded `TGZ` or `ZIP` file, you must create
  your own configuration file. The basic example
  configuration is a good place to start.

For package installations of MongoDB on Linux or macOS, an
initialization script which uses this default configuration file is also
provided. This initialization script can be used to start the
`mongod` on these platforms in the following manner:

- On Linux systems that use the **systemd** init system (the
  `systemctl` command):

  ```bash
  sudo systemctl start mongod
  ```

- On Linux systems that use the **SystemV init** init system (the
  `service` command):

  ```bash
  sudo service mongod start
  ```

- On macOS, using the `brew` package manger:

  ```bash
  brew services start mongodb-community@7.0
  ```

If you installed MongoDB using a `TGZ` or `ZIP` file, you will need
to create your own configuration file. A
basic example configuration can be found later in
this document. Once you have created a configuration file, you can start
a MongoDB instance with this configuration file by using either the
`--config` or `-f`
options to `mongod`. For example, on Linux:

```bash
mongod --config /etc/mongod.conf
mongod -f /etc/mongod.conf
```

Modify the values in the `mongod.conf` file on your system to
control the configuration of your database instance.

## Configure the Database

Consider the following basic configuration:

```yaml
processManagement:
   fork: true
net:
   bindIp: localhost
   port: 27017
storage:
   dbPath: /var/lib/mongo
systemLog:
   destination: file
   path: "/var/log/mongodb/mongod.log"
   logAppend: true
```

For most standalone servers, this is a sufficient base
configuration. It makes several assumptions, but consider the
following explanation:

- `fork` is `true`, which enables a
  daemon mode for `mongod`, which detaches (i.e. "forks")
  the MongoDB from the current session and allows you to run the
  database as a conventional server.

- `bindIp` is `localhost`, which forces the
  server to only listen for requests on the localhost IP. Only bind to
  secure interfaces that the application-level systems can access with
  access control provided by system network filtering
  (i.e. "firewall").

- `port` is `27017`, which is the default
  MongoDB port for database instances. MongoDB can bind to any
  port. You can also filter access based on port using network
  filtering tools.

  **Note:**

  UNIX-like systems require superuser privileges to attach processes
  to ports lower than 1024.

- `quiet` is `true`. This disables all but
  the most critical entries in output/log file, and is *not*
  recommended for production systems. If you do set this option, you
  can use `setParameter` to modify this setting during
  run time.

- `dbPath` is `/var/lib/mongo`, which
  specifies where MongoDB will store its data files.
  
  If you installed MongoDB on Linux using a package manager,
  such as `yum` or `apt`, the `/etc/mongod.conf` file provided
  with your MongoDB installation sets the following default `dbPath`,
  depending on your Linux distro:

  | Platform | Package Manager | Default `dbPath` |
  |---|---|---|
  | RHEL (Red Hat Enterprise Linux) / CentOS and Amazon | `yum` | `/var/lib/mongo` |
  | SUSE | `zypper` | `/var/lib/mongo` |
  | Ubuntu and Debian | `apt` | `/var/lib/mongodb` |
  | macOS | `brew` | `/usr/local/var/mongodb` |

  
  The user account that
  `mongod` runs under will need read and write access to
  this directory.

- `systemLog.path` is `/var/log/mongodb/mongod.log`
  which is where `mongod` will write its output. If you do not set
  this value, `mongod` writes all output to standard output
  (e.g. `stdout`.)

- `logAppend` is `true`, which ensures that
  `mongod` does not overwrite an existing log file
  following the server start operation.

Given the default configuration, some of these values may be
redundant. However, in many situations explicitly stating the
configuration increases overall system intelligibility.

## Security Considerations

The following configuration options are useful for limiting access to a
`mongod` instance:

```yaml
net:
   bindIp: localhost,10.8.0.10,192.168.4.24,/tmp/mongod.sock
security:
   authorization: enabled
```

`net.bindIp`
  This example provides four values to the `bindIp`
  option:

  - `localhost`, the localhost interface;
  - `10.8.0.10`, a private IP address typically used for local
    networks and VPN interfaces;
  - `192.168.4.24`, a private network interface typically used for
    local networks; and
  - `/tmp/mongod.sock`, a Unix domain socket path.

  Because production MongoDB instances need to be accessible from
  multiple database servers, it is important to bind MongoDB to
  multiple interfaces that are accessible from your application
  servers. At the same time it's important to limit these interfaces
  to interfaces controlled and protected at the network layer.

`security.authorization`
  Setting this option to `true` enables the authorization
  system within MongoDB. If enabled you will need to log in by
  connecting over the `localhost` interface for the first time to
  create user credentials.

**See also:**

/security

## Replication and Sharding Configuration

### Replication Configuration

Replica set configuration is straightforward, and only
requires that the `replSetName` have a value that is
consistent among all members of the set. Consider the following:

```yaml
replication:
   replSetName: set0
```

Use descriptive names for sets. Once configured, use
`mongosh` to add hosts to the replica set.

**See also:**

Replica set reconfiguration

To enable authentication for the replica set using
keyfiles , add the following
`keyFile` option [#x509]_:

```yaml
security:
   keyFile: /srv/mongodb/keyfile
```

Setting `keyFile` enables authentication and
specifies a keyfile for the replica set member to use when
authenticating to each other.

**See also:**

The Replica Set Security section for
information on configuring authentication with replica sets.

The /replication document for more information
on replication in MongoDB and replica set configuration in general.

    

### Sharding Configuration

Sharding requires `mongod` instances with different
`mongod` configurations for the config servers and the shards. The config servers store the cluster's
metadata, while the shards store the data.

To configure the config server `mongod` instances, in the
configuration file, specify `configsvr` for the
`sharding.clusterRole` setting.

**Note:**

Config servers must be deployed as a replica set.

```yaml
 sharding:
    clusterRole: configsvr
 net:
    bindIp: 10.8.0.12
    port: 27001
replication:
    replSetName: csRS
```

To deploy config servers as a replica set, the config servers must run
the storage-wiredtiger. `Initiate` the
replica set and add members.

To configure the shard `mongod` instances, specify
`shardsvr` for the `sharding.clusterRole` setting, and if
running as a replica set, the replica set name:

```yaml
sharding:
   clusterRole: shardsvr
replication:
   replSetName: shardA
```

If running as a replica set, `initiate` the
shard replica set and add members.

For the router (i.e. `mongos`), configure at least one
`mongos` process with the following setting:

```yaml
sharding:
   configDB: csRS/10.8.0.12:27001
```

You can specify additional members of the config server replica set by
specifying hostnames and ports in the form of a comma separated list
after the replica set name.

**See also:**

The /sharding section of the manual for more
information on sharding and cluster configuration.

## Run Multiple Database Instances on the Same System

In many cases running multiple instances of `mongod` on a
single system is not recommended. On some types of deployments
[#multimongod]_ and for testing purposes you may need to run more than
one `mongod` on a single system.

In these cases, use a base configuration for each
instance, but consider the following configuration values:

```yaml
storage:
   dbPath: /var/lib/mongo/db0/
processManagement:
   pidFilePath: /var/lib/mongo/db0.pid
```

The `dbPath` value controls the location of the
`mongod` instance's data directory. Ensure that each database
has a distinct and well labeled data directory. The
`pidFilePath` controls where `mongod` process
places it's process ID (PID) file. As this tracks the specific
`mongod` file, it is crucial that file be unique and well
labeled to make it easy to start and stop these processes.

Create additional init scripts and/or
adjust your existing MongoDB configuration and init script as
needed to control these processes.

## Diagnostic Configurations

The following configuration options control various `mongod`
behaviors for diagnostic purposes:

- `operationProfiling.mode` sets the database profiler level. The profiler is not active by default
  because of the possible impact on the profiler itself on performance.
  Unless this setting is on, queries are not profiled.

- | `operationProfiling.slowOpThresholdMs` configures the
    threshold which determines whether a query is "slow" for the
    purpose of the logging system and the profiler. The default value is 100 milliseconds. Set
    to a lower value if the logging system and the database profiler do
    not return useful results or set to a higher value to only log the
    longest running queries.

  |

  Secondary members of a replica set now log oplog entries that take longer than the slow operation
  threshold to apply. These slow oplog messages:

  - Are logged for the secondaries in the
    `diagnostic log`.

  - Are logged under the `REPL` component with the text
    `applied op: <oplog entry> took <num>ms`.

  - Do not depend on the log levels (either at the system or component
    level)

  - Do not depend on the profiling level.

  - Are affected by `slowOpSampleRate`.

  The profiler does not capture slow oplog entries.

- `systemLog.verbosity` controls the amount of logging output that
  `mongod` write to the log. Only use this option if you are
  experiencing an issue that is not reflected in the normal logging
  level.

  You can also specify verbosity level for specific components using the
  `systemLog.component.<name>.verbosity` setting. For the available
  components, see `component verbosity settings`.

For more information, see also database-profiling and
/administration/analyzing-mongodb-performance.
