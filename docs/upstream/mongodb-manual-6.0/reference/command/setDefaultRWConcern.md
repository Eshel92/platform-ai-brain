<!-- Converted from reference/command/setDefaultRWConcern.txt (reStructuredText). Includes are inlined. -->

# setDefaultRWConcern

## Definition

**`setDefaultRWConcern`**

The `setDefaultRWConcern` administrative command sets the
global default read or write concern configuration for a replica set
or sharded cluster. `setDefaultRWConcern` must be run
against the `admin` database.

- For replica sets, issue the `setDefaultRWConcern`
  command on the primary `mongod`.

- For sharded clusters, issue the `setDefaultRWConcern`
  on a `mongos`.

## Compatibility

This command is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
  {
    setDefaultRWConcern : 1,
    defaultReadConcern: { <read concern> },
    defaultWriteConcern: { <write concern> },
    writeConcern: { <write concern> },
    comment: <any>
  }
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - setDefaultRWConcern
  - `int`
  - .. _setDefaultRWConcern-cmd-setDefaultRWConcern:

    Set to `1`.

* - defaultReadConcern
  - `object`
  - .. _setDefaultRWConcern-cmd-defaultReadConcern:

    Document containing the global read concern configuration.
    Specify a valid read concern object. 

    - `setDefaultRWConcern` supports the 
      following subset of level:

      - `"local"`
      - `"available"`
      - `"majority"`

    - To unset the currently configured default read concern,
      specify an empty document `{}`.

    - `setDefaultRWConcern` only supports the
      `levels` read concern setting.
      You cannot specify any other read concern setting in the 
      default read concern.

    Omit this document to leave the current global read concern
    unmodified. If omitted, `setDefaultRWConcern` must
    specify defaultWriteConcern.

* - defaultWriteConcern
  - `object`
  - .. _setDefaultRWConcern-cmd-defaultWriteConcern:

    Document containing the global default write concern
    configuration. 

    - For the write concern w setting, 
      `setDefaultRWConcern` supports all 
      write concern values *except* `w : 0`.

    - For the write concern wc-wtimeout setting,
      `setDefaultRWConcern` defaults to `0` if the
      setting is omitted. Operations block until the requested
      write concern is met. If specifying a global default
      `wtimeout`, ensure the value is large enough to allow
      write operations to achieve the requested write concern. 

    - To unset the currently configured write concern, specify 
      an empty document `{}`.

    Omit this document to leave the current global write concern 
    unmodified. If omitted, `setDefaultRWConcern` must
    specify defaultReadConcern.

* - writeConcern
  - object
  - .. _setDefaultRWConcern-cmd-writeConcern:

    Optional. A document that specifies the 
    write concern to be used by the 
    `setDefaultRWConcern` command itself. 

    If omitted, `setDefaultRWConcern` uses the 
    previously set global default write concern *if* one 
    was configured.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst

`setDefaultRWConcern` returns an object that contains the
currently configured global default read and write concern. See
`getDefaultRWConcern` for more complete documentation on
the returned fields.

## Behavior

**Note:** Requires `featureCompatibilityVersion` 4.4+

Each `mongod` in the replica set or sharded cluster 
*must* have featureCompatibilityVersion set to 
at least `4.4` to use `setDefaultRWConcern`.

Starting in MongoDB 5.0, once the Cluster Wide Write Concern (CWWC) 
is set via the `setDefaultRWConcern` command the write
concern cannot be unset.

MongoDB only applies the global default read or write concern to
operations which do not explicitly specify a read or write concern. 

If MongoDB applies the global default read or write concern to an
operation, that operation behaves as if that read or write concern were
explicitly specified by the issuing client.

### Replica Sets

Issue `setDefaultRWConcern` against the replica set
primary. The primary replicates the new global default settings
to the remaining members of the replica set. Secondaries which have 
not yet replicated the updated global default settings continue 
using their local 'stale' copy of the defaults.

Issue the `setDefaultRWConcern` command with a
writeConcern of
`w : "majority"` to ensure the command only
returns after the changes have propagated to a majority of replica set
members.

### Sharded Clusters

Issue the `setDefaultRWConcern` against a
`mongos` in the cluster. The `mongos` persists
the updated settings to the config server replica set (CSRS). Each `mongos` periodically
issues a `getDefaultRWConcern` against the CSRS to refresh
their local copy of the global settings. A `mongos` uses
its local 'stale' copy of the global defaults during the time period
between refreshes.

Issue the `setDefaultRWConcern` command with a
writeConcern of
`w : "majority"` to ensure the command only
returns after the changes have propagated to a majority of CSRS members.

When an application issues an operation against the 
`mongos` without explicitly specifying a read or 
write concern setting, the `mongos` applies the 
corresponding global default setting.

The global default settings do *not* propagate to the individual shards.
You cannot run `setDefaultRWConcern` against a shard.

**Important:**

`setDefaultRWConcern` requires
featureCompatibilityVersion `4.4+`. If you
downgrade your deployment's featureCompatibilityVersion from `4.4` to `4.2`, all cluster-wide read and write
concern defaults are lost, but `mongos` instances may
continue applying the defaults for up to 30 seconds.

#### Sharding Administrative Commands Override Write Concern Settings

Sharding administrative commands that perform write operations on the
config server, such as the
`enableSharding` or `addShard` commands,
have specific behavior with global default write concern settings:

- The commands use `"majority"` regardless of the 
  configured global default write concern.

- The commands use a minimum wtimeout of `60000`. 
  The commands only use the global default write concern `wtimeout` if
  it is greater than `60000`.

### Access Control

For replica sets or sharded clusters enforcing 
authentication, `setDefaultRWConcern` requires 
that the authenticated user have the 
`setDefaultRWConcern` privilege action. 

The `clusterManager` built-in role provides the required 
privileges to run `setDefaultRWConcern`.

## Example

### Set Global Default Write Concern

The following operation sets the global write concern to the following:

- `w: 2 <`

```javascript
db.adminCommand({
  "setDefaultRWConcern" : 1,
  "defaultWriteConcern" : {
    "w" : 2
  }
})
```

The operation returns a document similar to the following:

```javascript
{
  "defaultWriteConcern" : {
   "w" : 2
  },
  "updateOpTime" : Timestamp(1586290895, 1),
  "updateWallClockTime" : ISODate("2020-04-07T20:21:41.849Z"),
  "localUpdateWallClockTime" : ISODate("2020-04-07T20:21:41.862Z"),
  "ok" : 1,
  "$clusterTime" : { ... }
  "operationTime" : Timestamp(1586290925, 1)
}
```

### Set Global Default Read Concern

The following operation sets the global read concern to 
`"majority"`:

```javascript
db.adminCommand({
  "setDefaultRWConcern" : 1,
  "defaultReadConcern" : { "level" : "majority" }
})
```

The operation returns a document similar to the following:

```javascript
{
  "defaultReadConcern" : {
    "level" : "majority"
  },
  "updateOpTime" : Timestamp(1586290895, 1),
  "updateWallClockTime" : ISODate("2020-04-07T20:21:41.849Z"),
  "localUpdateWallClockTime" : ISODate("2020-04-07T20:21:41.862Z"),
  "ok" : 1,
  "$clusterTime" : { ... }
  "operationTime" : Timestamp(1586290925, 1)
}
```

### Set Global Default Read and Write Concern

The following operation sets the global default read and write concern
to the following:

- `w: 2 <` write concern
- `level: "majority"` read concern.

```javascript
db.adminCommand({
  "setDefaultRWConcern" : 1,
  "defaultWriteConcern" : {
    "w" : 2
  },
  "defaultReadConcern" : { "level" : "majority" }
})
```

The operation returns a document similar to the following:

```javascript
"defaultWriteConcern" : {
  "w" : 2
},
"defaultReadConcern" : {
  "level" : "majority"
}
```

### Unset Global Default Read and Write Concern

You can:

- Unset the global default read concern.
- Only unset the global default write concern if you haven't already
  set it.

For example, assume the global default read concern is set to
`level: "majority"`. To unset the global
default read concern, use an empty document `{}`:

```javascript
db.adminCommand( {
   "setDefaultRWConcern" : 1, 
   "defaultReadConcern" : {}
} )
```

The operation returns a document that indicates the operation was
successful:

```javascript
{
   defaultReadConcern: { level: 'local' },
   defaultWriteConcern: { w: 2, wtimeout: 0 },
   updateOpTime: Timestamp({ t: 1656696934, i: 1 }),
   updateWallClockTime: ISODate("2022-07-01T17:35:40.578Z"),
   defaultWriteConcernSource: 'global',
   defaultReadConcernSource: 'implicit',
   localUpdateWallClockTime: ISODate("2022-07-01T17:35:40.578Z"),
   ok: 1,
   '$clusterTime': {
      ...
   },
   operationTime: Timestamp({ t: 1656632593, i: 1 })
}
```

You can only unset the global default write concern if you haven't
already set it.

To unset the global default write concern, use an empty document `{}`:

```javascript
db.adminCommand( {
   "setDefaultRWConcern" : 1, 
   "defaultWriteConcern" : {}
} )
```

If the global default write concern is:

- Unset, the operation succeeds.
- Already set, the operation returns the following error.

```javascript
MongoServerError: The global default write concern cannot be unset
once it is set.
```
