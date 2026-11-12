<!-- Part 7 of 7 of reference/configuration-options.md (split because the page is big). -->

### `replication` Options

```yaml
replication:
   oplogSizeMB: <int>
   replSetName: <string>
   enableMajorityReadConcern: <boolean>  
```

**`replication.oplogSizeMB`**

*Type*: integer

The maximum size in megabytes for the oplog. The
`oplogSizeMB` setting configures the uncompressed size of the
oplog, not the size on disk.

**Note:**

The oplog can grow past its configured size
limit to avoid deleting the `majority commit point`.

By default, the `mongod` process creates an oplog based
on the maximum amount of space available. For 64-bit systems, the
oplog is typically 5% of available disk space.

Once the `mongod` has created the oplog for the first
time, changing the `replication.oplogSizeMB` option does not
affect the size of the oplog. To change the maximum oplog size after
starting the `mongod`, use
`replSetResizeOplog`. `replSetResizeOplog`
enables you to resize the oplog dynamically without restarting the
`mongod` process. To persist the changes made using
`replSetResizeOplog` through a restart, update the value
of `oplogSizeMB`.

See replica-set-oplog-sizing for more information.

The `replication.oplogSizeMB` setting is available only for `mongod`.

**`replication.replSetName`**

*Type*: string

The name of the replica set that the `mongod` is part of. All hosts
in the replica set must have the same set name.

If your application connects to more than one replica set, each set must
have a distinct name. Some drivers group replica set connections by 
replica set name.

The `replication.replSetName` setting is available only for `mongod`.

`replication.replSetName` cannot be used in conjunction with
`storage.indexBuildRetry`.

**`replication.enableMajorityReadConcern`**

*Default*: true

Configures support for `"majority"` read concern.

Starting in MongoDB 5.0, 
`enableMajorityReadConcern` cannot be changed 
and is always set to `true`. Attempting to start a storage engine 
that does not support majority read concern with the 
`--enableMajorityReadConcern` option fails and return an error
message.

In earlier versions of MongoDB, 
`enableMajorityReadConcern` was configurable.

**Warning:**

If you are using a three-member primary-secondary-arbiter (PSA) 
architecture, consider the following:

- The write concern `"majority"` can cause
  performance issues if a secondary is unavailable or lagging. For 
  advice on how to mitigate these issues, see 
  performance-issues-psa.

- If you are using a global default `"majority"` 
  and the write concern is less than the size of the majority,
  your queries may return stale (not fully replicated) data.


### `sharding` Options

```yaml
sharding:
   clusterRole: <string>
   archiveMovedChunks: <boolean>
```

**`sharding.clusterRole`**

*Type*: string

The role that the `mongod` instance has in the sharded
cluster. Set this setting to one of the following:

| Value | Description |
|---|---|
| `configsvr` | Start this instance as a config server. The instance starts on port `27019` by default. When you configure a MongoDB instance as clusterRole `configsvr` you must also specify a `replSetName`. |
| `shardsvr` | Start this instance as a shard. The instance starts on port `27018` by default. When you configure a MongoDB instance as a a clusterRole `shardsvr` you must also specify a `replSetName`. |

**Note:**

Setting `sharding.clusterRole` requires the `mongod`
instance to be running with replication. To deploy the instance as
a replica set member, use the `replSetName`
setting and specify the name of the replica set.

The `sharding.clusterRole` setting is available only for `mongod`.

**`sharding.archiveMovedChunks`**

*Type*: boolean

*Default*: false.

During chunk migration, a shard does not save documents migrated from
the shard.


### `auditLog` Options

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).

```yaml
auditLog:
   destination: <string>
   format: <string>
   path: <string>
   filter: <string>
```

**`auditLog.auditEncryptionKeyIdentifier`**

*Type*: string

**New in version:** 6.0

Specifies the unique identifier of the Key Management
Interoperability Protocol (KMIP) key for audit log encryption.

You cannot use this option and
`auditLog.localAuditKeyFile` together.

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced).
MongoDB Enterprise and Atlas have different configuration
requirements.

**`auditLog.compressionMode`**

*Type*: string

**New in version:** 5.3

Specifies the compression mode for audit log encryption. You must also enable audit log
encryption using either `auditLog.auditEncryptionKeyIdentifier` or
`auditLog.localAuditKeyFile`.

You can set this option to one of these values:

| Value | Description |
|---|---|
| `zstd` | Use the zstd algorithm to compress the audit log. |
| `none` *(default)* | Do not compress the audit log. |

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced).
MongoDB Enterprise and Atlas have different configuration
requirements.

**`auditLog.destination`**

*Type*: string

When set, `auditLog.destination` enables auditing and
specifies where `mongos` or `mongod` sends all audit events.

`auditLog.destination` can have one of the following values:

| Value | Description |
|---|---|
| `syslog` | Output the audit events to syslog in JSON format. Not available on Windows. Audit messages have a syslog severity level of `info` and a facility level of `user`. The syslog message limit can result in the truncation of audit messages. The auditing system neither detects the truncation nor errors upon its occurrence. |
| `console` | Output the audit events to `stdout` in JSON format. |
| `file` | Output the audit events to the file specified in `auditLog.path` in the format specified in `auditLog.format`. |

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).

**`auditLog.filter`**

*Type*: string representation of a document

The filter to limit the types of operations the audit system records. The
option takes a string representation
of a query document of the form:

```javascript
{ <field1>: <expression1>, ... }
```

The `<field>` can be any field in the audit message, including fields returned in the
param document. The
`<expression>` is a query condition expression.

To specify an audit filter, enclose the filter document in single
quotes to pass the document as a string.

To specify the audit filter in a 
configuration file, you must use the YAML format 
of the configuration file.

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).

**`auditLog.format`**

*Type*: string

The format of the output file for auditing if `destination` is
`file`. The
`auditLog.format` option can have one of the following values:

| Value | Description |
|---|---|
| `JSON` | Output the audit events in JSON format to the file specified in `auditLog.path`. |
| `BSON` | Output the audit events in BSON binary format to the file specified in `auditLog.path`. |

Printing audit events to a file in JSON format degrades server
performance more than printing to a file in BSON format.

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced)
and [MongoDB Atlas](https://cloud.mongodb.com/user#/atlas/login).

**`auditLog.localAuditKeyFile`**

*Type*: string

**New in version:** 5.3

Specifies the path and file name for a local audit key file for
audit log encryption.

**Note:**

Only use this option for testing because the key is
not secured. To secure the key, use
`auditLog.auditEncryptionKeyIdentifier` and an external Key
Management Interoperability Protocol (KMIP) server.

You cannot use both options together.

**Note:**

Available only in [MongoDB Enterprise](http://www.mongodb.com/products/mongodb-enterprise-advanced).
MongoDB Enterprise and Atlas have different configuration
requirements.

**`auditLog.path`**

*Type*: string

The output file for auditing if
`destination` has value of `file`. The `auditLog.path`
option can take either a full path name or a relative path name.

**`auditLog.runtimeConfiguration`**

*Type*: boolean

Specifies if a node allows runtime configuration of audit filters
and the auditAuthorizationSuccess variable. If `true` the node
can take part in Online Audit Filter Management. 


## `mongos`-only Options

```yaml
replication:
   localPingThresholdMs: <int>

sharding:
   configDB: <string>
```

**`replication.localPingThresholdMs`**

*Type*: integer

*Default*: 15

The ping time, in milliseconds, that `mongos` uses
to determine which secondary replica set members to pass read
operations from clients. The default value of `15` corresponds to
the default value in all of the client `drivers`.

When `mongos` receives a request that permits reads to
secondary members, the `mongos`:

- Finds the member of the set with the lowest ping time.

- Constructs a list of replica set members that is within a ping time of
  15 milliseconds of the nearest suitable member of the set.

  If you specify a value for the
  `replication.localPingThresholdMs` option, 
  `mongos` construct the list of replica members that are
  within the latency allowed by this value.

- Selects a member to read from at random from this list.

The ping time used for a member compared by the `replication.localPingThresholdMs` setting is a
moving average of recent ping times, calculated at most every 10
seconds. As a result, some queries may reach members above the threshold
until the `mongos` recalculates the average.

See the replica-set-read-preference-behavior-member-selection
section of the read preference
documentation for more information.

**`sharding.configDB`**

*Type*: string

The configuration servers for the
sharded cluster.

Config servers for sharded clusters are 
deployed as a replica set. The
replica set config servers must run the WiredTiger storage engine.

Specify the config server replica set name and the hostname and port of
at least one of the members of the config server replica set.

```javascript
sharding:
  configDB: <configReplSetName>/cfg1.example.net:27019, cfg2.example.net:27019,...
```

The `mongos` instances for the sharded cluster must specify
the same config server replica set name but can specify hostname and
port of different members of the replica set.


## Windows Service Options

```yaml
processManagement:
   windowsService:
      serviceName: <string>
      displayName: <string>
      description: <string>
      serviceUser: <string>
      servicePassword: <string>
```

**`processManagement.windowsService.serviceName`**

*Type*: string

*Default*: MongoDB

The service name of `mongos` or `mongod` when running as a
Windows Service. Use this name with the `net start <name>` and
`net stop <name>` operations.

You must use `processManagement.windowsService.serviceName` in conjunction with either
the `--install` or `--remove` option.

**`processManagement.windowsService.displayName`**

*Type*: string

*Default*: MongoDB

The name listed for MongoDB on the Services administrative
application.

**`processManagement.windowsService.description`**

*Type*: string

*Default*: MongoDB Server

Run `mongos` or `mongod` service description.

You must use `processManagement.windowsService.description` in conjunction with the
`--install` option.

For descriptions that contain spaces, you must enclose the
description in quotes.

**`processManagement.windowsService.serviceUser`**

*Type*: string

The `mongos` or `mongod` service in the context of a certain user. This
user must have "Log on as a service" privileges.

You must use `processManagement.windowsService.serviceUser` in conjunction with the
`--install` option.

**`processManagement.windowsService.servicePassword`**

*Type*: string

The password for `<user>` for `mongos` or `mongod` when running with
the `processManagement.windowsService.serviceUser` option.

You must use `processManagement.windowsService.servicePassword` in conjunction with the
`--install` option.


## Removed MMAPv1 Options

MongoDB removed the deprecated MMAPv1 storage engine and the MMAPv1-specific 
configuration options:

| Removed Configuration File Setting | Removed Command-line Option |
|---|---|
| `storage.mmapv1.journal.commitIntervalMs` |  |
| `storage.mmapv1.journal.debugFlags` | `mongod --journalOptions` |
| `storage.mmapv1.nsSize` | `mongod --nssize` |
| `storage.mmapv1.preallocDataFiles` | `mongod --noprealloc` |
| `storage.mmapv1.quota.enforced` | `mongod --quota` |
| `storage.mmapv1.quota.maxFilesPerDB` | `mongod --quotaFiles` |
| `storage.mmapv1.smallFiles` | `mongod --smallfiles` |
| `storage.repairPath` | `mongod --repairpath` |
| `replication.secondaryIndexPrefetch` | `mongod --replIndexPrefetch` |

For earlier versions of MongoDB, refer to the [legacy documentation](https://www.mongodb.com/docs/legacy/).
