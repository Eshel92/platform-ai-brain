<!-- Converted from reference/command/getDefaultRWConcern.txt (reStructuredText). Includes are inlined. -->

# getDefaultRWConcern (database command)

## Definition

**`getDefaultRWConcern`**

The `getDefaultRWConcern` administrative command retrieves
the global default read or write concern settings.

- For sharded clusters, issue the `getDefaultRWConcern`
  on a `mongos`.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following form:

```javascript
db.adminCommand( 
   { 
     getDefaultRWConcern: 1 , 
     inMemory: <boolean>, 
     comment: <any> 
   } 
)
```

## Command Fields

The command has the following fields:

| Field | Type | Description |
|---|---|---|
| getDefaultRWConcern | int | .. _getDefaultRWConcern-cmd-getDefaultRWConcern: Set to `1`. |
| inMemory | boolean | .. _getDefaultRWConcern-cmd-inMemory: Optional. Set to `true` to return the in-memory cached copy of the global default read or write concern settings. The instance uses the in-memory copy when applying the global defaults to an operation. Set to `false` to return the on-disk copy of the deployment's global default read or write concern. Defaults to `false`. |
| `comment` | any | .. include:: /includes/extracts/comment-content.rst |

## Output

The output may include the following fields:

| Field | Type | Description |
|---|---|---|
| defaultWriteConcern | `object` | .. _getDefaultRWConcern-cmd-defaultWriteConcern: The global default write concern configuration. If the deployment has no global default write concern settings, this field is absent from `getDefaultRWConcern` output. |
| defaultReadConcern | `object` | .. _getDefaultRWConcern-cmd-defaultReadConcern: The global default read concern configuration. If the deployment has no global default read concern settings, this field is absent from `getDefaultRWConcern` output. |
| defaultWriteConcernSource | String | .. _getDefaultRWConcern-cmd-defaultWriteConcernSource: The source of the default write concern. By default, the value is `"implicit"`. Once you set the default write concern with `setDefaultRWConcern`, the value becomes `"global"`. |
| defaultReadConcernSource | String | .. _getDefaultRWConcern-cmd-defaultReadConcernSource: The source of the default read concern. By default, the value is `"implicit"`. Once you set the default read concern with `setDefaultRWConcern`, the value becomes `"global"`. |
| updateOpTime | Timestamp | .. _getDefaultRWConcern-cmd-updateOpTime: The operation timestamp of when any global default read or write concern setting was last modified. Present if a default has ever been set for the cluster. |
| updateWallClockTime | Date | .. _getDefaultRWConcern-cmd-updateWallClockTime: The wall clock date when an administrator last set the global default read or write concern. This value is informational and should not be used for any recency comparisons. |
| localUpdateWallClockTime | Date | .. _getDefaultRWConcern-cmd-localUpdateWallClockTime: The wall clock date when the `mongod` or `mongos` last updated its local copy of the global default read and write concern settings. This value is informational and should not be used for any recency comparisons. |

 

**See also:**

`setDefaultRWConcern`

## Behavior

**Note:** Requires `featureCompatibilityVersion` 4.4+

Each `mongod` in the replica set or sharded cluster 
*must* have featureCompatibilityVersion set to 
at least `4.4` to use `getDefaultRWConcern`.  If you
downgrade your deployment's featureCompatibilityVersion from `4.4` to `4.2`, all cluster-wide read and write
concern defaults are lost, but `mongos` instances may
continue applying the defaults for up to 30 seconds.

### Replica Sets

You can issue `getDefaultRWConcern` against any data-bearing
member of the replica set (i.e. not against an arbiter). 

A secondary can return a 'stale' version of the global default 
settings if it has not yet replicated the latest changes from the 
primary.

### Sharded Clusters

Issue the `setDefaultRWConcern` against a
`mongos` in the cluster. 

Each `mongos` periodically refreshes its local copy of the
global default settings. A `mongos` can return a 'stale'
version of the global default settings if it has not yet refreshed
its local copy after a recent update to the global default settings
*or* if it fetched its settings from a lagged 
config server secondary.

The global default settings do *not* propagate to the individual shards.
You cannot run `getDefaultRWConcern` against a shard.

### Access Control

For replica sets or sharded clusters enforcing 
authentication, `getDefaultRWConcern` requires 
that the authenticated user have the 
`getDefaultRWConcern` privilege action. 

The `clusterManager` or `clusterMonitor` built-in
roles provides the required privileges to run
`getDefaultRWConcern`.

## Example

The following operation retrieves the currently configured
global default read and write concern for the `mongod`.

```javascript
db.adminCommand({
  "getDefaultRWConcern": 1
})
```

The operation returns output similar to the following:

```javascript
{
  "defaultWriteConcern" : {
    "w" : "majority"
  },
  "defaultReadConcern" : {
    "level" : "majority"
  },
  "defaultWriteConcernSource" : "global",
  "defaultReadConcernSource" : "global",
  "updateOpTime" : Timestamp(1586290895, 1),
  "updateWallClockTime" : ISODate("2020-04-07T20:21:41.849Z"),
  "localUpdateWallClockTime" : ISODate("2020-04-07T20:21:41.862Z"),
  "ok" : 1,
  "$clusterTime" : { ... }
  "operationTime" : Timestamp(1586290925, 1)
}
```
