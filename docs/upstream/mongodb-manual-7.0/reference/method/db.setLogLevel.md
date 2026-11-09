<!-- Converted from reference/method/db.setLogLevel.txt (reStructuredText). Includes are inlined. -->

# db.setLogLevel() (mongosh method)

## Definition

**`db.setLogLevel()`**

Sets a single verbosity level for log messages.

`db.setLogLevel()` has the following form:

```javascript
db.setLogLevel(<level>, <component>)
```

`db.setLogLevel()` takes the following parameters:

* - Parameter

  - Type

  - Description

* - `level`

  - int

  - The log verbosity level.

    The verbosity level can range from `0` to `5`:

    - `0` is the MongoDB's default log verbosity level, to include
      Informational messages.

    - `1` to `5` increases the verbosity level to include
      Debug messages.

    To inherit the verbosity level of the component's parent, you can
    also specify `-1`.

* - `component`

  - string

  - Optional. The name of the component for which to specify the log verbosity
    level. The component name corresponds to the `<name>` from the
    corresponding `systemLog.component.<name>.verbosity` setting:

    - `accessControl`

    - `assert`

    - `command`

    - `control`

    - `ftdc`

    - `geo`

    - `index`

    - `network`

    - `query`

    - `queryStats`

    - `replication`

    - `replication.election`

    - `replication.heartbeats`

    - `replication.initialSync`

    - `replication.rollback`

    - `recovery`

    - `sharding`

    - `storage`

    - `storage.journal`

    - `transaction`

    - `write`

          

          
          
          

## Compatibility

This method is available in deployments hosted in the following environments: 

**Important:**

This command is not supported in MongoDB Atlas clusters.
For information on Atlas support for all commands, 
see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

`db.setLogLevel()` sets a *single* verbosity level. To set
multiple verbosity levels in a single operation, use either the
`setParameter` command to set the
`logComponentVerbosity` parameter. You can also specify the
verbosity settings in the configuration file. See
log-messages-configure-verbosity for examples.

The verbosity levels that you set appear in log messages as the
`D1` through `D5` severity values. These values are unrelated to
labels such as `DUP1` or `DUP2`. To learn more about severity
values, see log-severity-levels.

**Note:**

Starting in version 4.2, MongoDB includes the Debug verbosity level
(1-5) in the log messages. For example,
if the verbosity level is 2, MongoDB logs `D2`. In previous
versions, MongoDB log messages only specified `D` for Debug level.

## Examples

### Set Default Verbosity Level

Omit the `<component>` parameter to set the default verbosity for all
components, which corresponds to the `systemLog.verbosity`
setting. The operation sets the default verbosity to `1`:

```javascript
db.setLogLevel(1)
```

Output:

```javascript
{
   was: {
      verbosity: 1,
      accessControl: { verbosity: -1 },
      assert: { verbosity: -1 },
      command: { verbosity: -1 },
      control: { verbosity: -1 },
      executor: { verbosity: -1 },
      geo: { verbosity: -1 },
      globalIndex: { verbosity: -1 },
      index: { verbosity: -1 },
      network: {
         verbosity: -1,
         asio: { verbosity: -1 },
         bridge: { verbosity: -1 },
         connectionPool: { verbosity: -1 }
      },
      processHealth: { verbosity: -1 },
      query: {
         verbosity: -1,
         optimizer: { verbosity: -1 },
         ce: { verbosity: -1 }
      },
      queryStats: { verbosity: -1 },
      replication: {
         verbosity: -1,
         election: { verbosity: -1 },
         heartbeats: { verbosity: -1 },
         initialSync: { verbosity: -1 },
         rollback: { verbosity: -1 }
      },
      sharding: {
         verbosity: -1,
         rangeDeleter: { verbosity: -1 },
         shardingCatalogRefresh: { verbosity: -1 },
         migration: { verbosity: -1 },
         reshard: { verbosity: -1 },
         migrationPerf: { verbosity: -1 }
      },
      storage: {
         verbosity: -1,
         recovery: { verbosity: -1 },
         journal: { verbosity: 2 },
         wt: {
         verbosity: -1,
         wtBackup: { verbosity: -1 },
         wtCheckpoint: { verbosity: -1 },
         wtCompact: { verbosity: -1 },
         wtEviction: { verbosity: -1 },
         wtHS: { verbosity: -1 },
         wtRecovery: { verbosity: -1 },
         wtRTS: { verbosity: -1 },
         wtSalvage: { verbosity: -1 },
         wtTiered: { verbosity: -1 },
         wtTimestamp: { verbosity: -1 },
         wtTransaction: { verbosity: -1 },
         wtVerify: { verbosity: -1 },
         wtWriteLog: { verbosity: -1 }
         }
      },
      write: { verbosity: -1 },
      ftdc: { verbosity: -1 },
      tracking: { verbosity: -1 },
      transaction: { verbosity: -1 },
      tenantMigration: { verbosity: -1 },
      test: { verbosity: -1 },
      resourceConsumption: { verbosity: -1 },
      streams: { verbosity: -1 }
   },
   ok: 1
}
```

### Set Verbosity Level for a Component

Specify the `<component>` parameter to set the verbosity for the
component. The following operation updates the
`systemLog.component.storage.journal.verbosity` to `2`:

```javascript
db.setLogLevel(2, "storage.journal" )
```

Output:

```javascript
{
   was: {
      verbosity: 1,
      accessControl: { verbosity: -1 },
      assert: { verbosity: -1 },
      command: { verbosity: -1 },
      control: { verbosity: -1 },
      executor: { verbosity: -1 },
      geo: { verbosity: -1 },
      globalIndex: { verbosity: -1 },
      index: { verbosity: -1 },
      network: {
         verbosity: -1,
         asio: { verbosity: -1 },
         bridge: { verbosity: -1 },
         connectionPool: { verbosity: -1 }
      },
      processHealth: { verbosity: -1 },
      query: {
         verbosity: -1,
         optimizer: { verbosity: -1 },
         ce: { verbosity: -1 }
      },
      queryStats: { verbosity: -1 },
      replication: {
         verbosity: -1,
         election: { verbosity: -1 },
         heartbeats: { verbosity: -1 },
         initialSync: { verbosity: -1 },
         rollback: { verbosity: -1 }
      },
      sharding: {
         verbosity: -1,
         rangeDeleter: { verbosity: -1 },
         shardingCatalogRefresh: { verbosity: -1 },
         migration: { verbosity: -1 },
         reshard: { verbosity: -1 },
         migrationPerf: { verbosity: -1 }
      },
      storage: {
         verbosity: -1,
         recovery: { verbosity: -1 },
         journal: { verbosity: -1 },
         wt: {
         verbosity: -1,
         wtBackup: { verbosity: -1 },
         wtCheckpoint: { verbosity: -1 },
         wtCompact: { verbosity: -1 },
         wtEviction: { verbosity: -1 },
         wtHS: { verbosity: -1 },
         wtRecovery: { verbosity: -1 },
         wtRTS: { verbosity: -1 },
         wtSalvage: { verbosity: -1 },
         wtTiered: { verbosity: -1 },
         wtTimestamp: { verbosity: -1 },
         wtTransaction: { verbosity: -1 },
         wtVerify: { verbosity: -1 },
         wtWriteLog: { verbosity: -1 }
         }
      },
      write: { verbosity: -1 },
      ftdc: { verbosity: -1 },
      tracking: { verbosity: -1 },
      transaction: { verbosity: -1 },
      tenantMigration: { verbosity: -1 },
      test: { verbosity: -1 },
      resourceConsumption: { verbosity: -1 },
      streams: { verbosity: -1 }
   },
   ok: 1
}
```

### Get Global Log Level For a Deployment

The following operation gets the default logging level verbosity for a 
deployment:

```javascript
db.adminCommand({getParameter: 1, logLevel: 1});
```

Output:

```javascript
{ 
logLevel: 0, 
ok: 1 
}
```

**Note:**

You can also get log verbosity levels for MongoDB components. 
For details, see `db.getLogComponents()`.
