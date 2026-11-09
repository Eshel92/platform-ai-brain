<!-- Converted from reference/method/rs.reconfigForPSASet.txt (reStructuredText). Includes are inlined. -->

# rs.reconfigForPSASet()

## Definition

**`rs.reconfigForPSASet( memberIndex, config, { options } )`**

**New in version:** 5.0

Safely perform some reconfiguration changes on a
primary-secondary-arbiter (PSA) replica set or on a replica set that
is changing to a PSA architecture. You should only use this method in
one of the following cases:

- You want to reconfigure a secondary in an existing three-member
  replica set with a PSA architecture to become a voting,
  data-bearing node with a non-zero `priority`.
- You want to add a new voting, data-bearing node with a non-zero
  priority to an existing two-member replica set that contains one
  voting, data-bearing node and one arbiter.

**Warning:**

If the secondary you are adding is lagged and the resulting
replica set is a PSA configuration, the first configuration change
will change the number of nodes that need to commit a change with
`"majority"`. In this case, your commit point will
lag until the secondary has caught up.

For details about the behavior of this method, see
reconfigForPSASet-behavior.

## Compatibility

This method is available in deployments hosted in the following environments:

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `rs.reconfigForPSASet()` method has the following syntax:

```bash
rs.reconfigForPSASet(
  memberIndex: <num>,
  config: <configuration>,
  {
    "force" : <boolean>,
    "maxTimeMS" : <int>
  }
)
```

| Parameter | Type | Description |
|---|---|---|
| `memberIndex` | integer | The index of the secondary that is being added or modified. |
| `config` | document | A document that specifies the new configuration of a replica set. |
| `force` | boolean | *Optional* WARNING: Running the `rs.reconfigForPSASet()` method with `force: true` is not recommended and can lead to committed writes being rolled back. Specify `true` to force the available replica set members to accept the new configuration. Defaults to `false`. Force reconfiguration can result in unexpected or undesired behavior, including rollback of `"majority"` committed writes. |
| `maxTimeMS` | integer | *Optional* Specifies a cumulative time limit in milliseconds for processing each reconfiguration during the `rs.reconfigForPSASet()` operation. By default, `rs.reconfigForPSASet()` waits indefinitely for the replica configurations to propagate to a majority of replica set members. |

## Behavior

The `rs.reconfigForPSASet()` method reconfigures your replica
set in two steps:

1. The method reconfigures your replica set to add or modify a secondary
   with  `{ votes: 1, priority: 0 }`.
2. Once the added or modified secondary has caught up with all committed
   writes, the method reconfigures the secondary to have the
   `priority` specified in the
   `rs.reconfigForPSASet()` command
   (`{ votes: 1, priority: <num> }`).

The two-step approach avoids the possibility of rolling back committed
writes in the case of a failover to the new secondary before the new
secondary has all committed writes from the previous configuration.

## Example

A replica set named `rs0` has the following configuration:

```javascript
{
   "_id" : "rs0",
   "version" : 1,
   "term": 1,
   "members" : [
      {
         "_id" : 0,
         "host" : "mongodb0.example.net:27017",
         "arbiterOnly" : false,
         "buildIndexes" : true,
         "hidden" : false,
         "priority" : 1,
         "tags" : {},
         "secondaryDelaySecs" : Long("0"),
         "votes" : 1
      },
      {
         "_id" : 2,
         "host" : "mongodb1.example.net:27017",
         "arbiterOnly" : true,
         "buildIndexes" : true,
         "hidden" : false,
         "priority" : 0,
         "tags" : {},
         "secondaryDelaySecs" : Long("0"),
         "votes" : 1
      }
   ],
   "protocolVersion" : Long("1"),
   "writeConcernMajorityJournalDefault": true,
   "settings" : {
      "chainingAllowed" : true,
      "heartbeatIntervalMillis" : 2000,
      "heartbeatTimeoutSecs" : 10,
      "electionTimeoutMillis" : 10000,
      "catchUpTimeoutMillis" : 2000,
      "getLastErrorModes" : {},
      "getLastErrorDefaults" : {
         "w" : 1,
         "wtimeout" : 0
      },
      "replicaSetId" : ObjectId("60e6f83923193faa336889d2")
   }
}
```

The following sequence of operations add a new secondary to the replica
set. The operations are issued in the `mongosh` shell while
connected to the primary.

```javascript
cfg = rs.conf();
cfg["members"] = [
  {
     "_id" : 0,
     "host" : "mongodb0.example.net:27017",
     "arbiterOnly" : false,
     "buildIndexes" : true,
     "hidden" : false,
     "priority" : 1,
     "tags" : {},
     "secondaryDelaySecs" : Long("0"),
     "votes" : 1
  },
  {
     "_id" : 1,
     "host" : "mongodb1.example.net:27017",
     "arbiterOnly" : false,
     "buildIndexes" : true,
     "hidden" : false,
     "priority" : 2,
     "tags" : {},
     "secondaryDelaySecs" : Long("0"),
     "votes" : 1
  },
  {
     "_id" : 2,
     "host" : "mongodb2.example.net:27017",
     "arbiterOnly" : true,
     "buildIndexes" : true,
     "hidden" : false,
     "priority" : 0,
     "tags" : {},
     "secondaryDelaySecs" : Long("0"),
     "votes" : 1
  }
]
rs.reconfigForPSASet(1, cfg);
```

#. The first statement uses the `rs.conf()` method to retrieve
   a document containing the current configuration for the replica set and stores the
   document in the local variable `cfg`.

#. The second statement adds the new secondary to the `members` array.
   In this configuration the new secondary is added at `memberIndex`
   `1`. The `memberIndex` is the same as the array index. For
   additional settings, see replica set configuration settings.

#. The last statement calls the `rs.reconfigForPSASet()` method
   with the `memberIndex` `1` and the modified `cfg`. The
   `memberIndex` is the array position of the new member in the
   `members` array. Upon successful reconfiguration, the replica set
   configuration resembles the following:

   ```javascript
   {
      "_id" : "rs0",
      "version" : 1,
      "term": 1,
      "members" : [
         {
            "_id" : 0,
            "host" : "mongodb0.example.net:27017",
            "arbiterOnly" : false,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 1,
            "tags" : {},
            "secondaryDelaySecs" : Long("0"),
            "votes" : 1
         },
         {
            "_id" : 1,
            "host" : "mongodb1.example.net:27017",
            "arbiterOnly" : false,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 2,
            "tags" : {},
            "secondaryDelaySecs" : Long("0"),
            "votes" : 1
         },
         {
            "_id" : 2,
            "host" : "mongodb2.example.net:27017",
            "arbiterOnly" : true,
            "buildIndexes" : true,
            "hidden" : false,
            "priority" : 0,
            "tags" : {},
            "secondaryDelaySecs" : Long("0"),
            "votes" : 1
         }
      ],
      "protocolVersion" : Long("1"),
      "writeConcernMajorityJournalDefault": true,
      "settings" : {
         "chainingAllowed" : true,
         "heartbeatIntervalMillis" : 2000,
         "heartbeatTimeoutSecs" : 10,
         "electionTimeoutMillis" : 10000,
         "catchUpTimeoutMillis" : 2000,
         "getLastErrorModes" : {},
         "getLastErrorDefaults" : {
            "w" : 1,
            "wtimeout" : 0
         },
         "replicaSetId" : ObjectId("60e6f83923193faa336889d2")
      }
   }
   ```

**See also:**

- `rs.conf()`
- `rs.reconfig()`
- replSetGetConfig-output
- /administration/replica-set-member-configuration
- /administration/replica-set-maintenance
