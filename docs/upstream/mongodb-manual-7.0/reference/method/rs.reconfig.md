<!-- Converted from reference/method/rs.reconfig.txt (reStructuredText). Includes are inlined. -->

# rs.reconfig() (mongosh method)

## Definition

**`rs.reconfig( configuration, { options } )`**

Reconfigures an existing replica set, overwriting the existing
replica set configuration. To run the method, you must connect to
the primary of the replica set.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `replSetReconfig` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

The `rs.reconfig()` method has the following syntax:

```bash
rs.reconfig(
  <configuration>,
  {
    "force" : <boolean>,
    "maxTimeMS" : <int>
  }
)
```

| Parameter | Type | Description |
|---|---|---|
| .. _rs-reconfig-method-configuration: configuration | document | A document that specifies the configuration of a replica set. |
| .. _rs-reconfig-method-force: force | boolean | *Optional* Specify `true` to force the available replica set members to accept the new configuration. Defaults to `false`. Force reconfiguration can result in unexpected behavior, including rollback of `"majority"` committed writes. |
| .. _rs-reconfig-method-maxTimeMS: maxTimeMS | integer | *Optional* Specifies a cumulative time limit in milliseconds for processing the `rs.reconfig()` operation. By default, `rs.reconfig()` waits indefinitely for the replica configuration to propagate to a majority of replica set members. |

To reconfigure an existing replica set, first retrieve the
current configuration with `rs.conf()`, modify the
configuration document as needed, and then pass the modified
document to `rs.reconfig()`.

The `force` parameter allows a reconfiguration command to be issued
to a non-primary node.

## Compatibility

This method is available in deployments hosted in the following environments:

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

### Global Write Concern

You must explicitly set the global default write concern before attempting to reconfigure a replica set with a configuration that would change the implicit
default write concern. To set the global default write concern, use the
`setDefaultRWConcern` command.

### `term` Replica Configuration Field

The `term` field is set by the primary replica set member. 
The primary ignores the `term` field if set explicitly in the
`rs.reconfig()` operation.

### Reconfiguration Can Add or Remove No More than One Voting Member at a Time

`rs.reconfig()` by default allows adding or
removing no more than `1` `voting`
member at a time. For example, a new configuration can make at most
*one* of the following changes to the cluster `membership`:

- Adding a new voting replica set member.

- Removing an existing voting replica set member.

- Modifying the `votes` for an existing replica
  set member.

To add or remove multiple voting members, issue a series of
`rs.reconfig()` operations to add or remove one member at a
time.

Issuing a force reconfiguration
immediately installs the new configuration even if it adds or removes
multiple voting members. Force reconfiguration can cause unexpected
behavior, such as the rollback of `"majority"`
committed write operations.

### Reconfiguration Waits Until a Majority of Members Install the Replica Configuration

`rs.reconfig()` waits until a majority of voting
replica set members install the new replica configuration before
returning success. A voting member is *any* replica set member where
`members[n].votes` is `1`, including arbiters.

Replica set members propagate their replica configuration via
heartbeats. Whenever a member learns
of a configuration with a higher `version` and
`term`, it installs the new configuration. The
reconfiguration process has two distinct 'waiting' phases:

\1) Wait for the current configuration to be *committed* before installing the new configuration.
   The "current" configuration refers to the replica configuration in
   use by the primary at the time `rs.reconfig()` is issued. 

   A configuration is committed when:

   - A majority of voting replica set members have installed the
     current configuration, *and*

   - All writes which were `"majority"` committed in
     the previous configuration have also replicated to a majority in
     the current configuration.

   Typically, the current configuration has already been installed on
   a majority of voting replica set members. However, the majority
   committed writes in the previous configuration may not all be
   committed in the current configuration. `Delayed` members *or* members that are
   `lagging behind` the
   primary can increase the time spent in this phase.

   If the operation was issued with a 
   maxTimeMS limit *and* 
   the operation exceeds the limit while waiting, the operation
   returns an error and discard the new configuration. The 
   limit is *cumulative* and does not reset after proceeding to 
   the next phase.

\2) Wait for a majority of voting members in the new configuration to install the new configuration.
   The "new" configuration refers to the replica configuration 
   specified to `rs.reconfig()`.

   The primary installs and begins using the new replica
   configuration before propagating the configuration to the
   remaining replica set members. The operation only waits for a
   majority of voting members to install the new configuration, and
   does not require waiting for the new configuration to be
   committed.

   If the operation was issued with a maxTimeMS limit
   *and* the operation exceeds the limit while waiting, the operation
   returns an error *but* continues using and propagating the new
   configuration.

Issuing a force reconfiguration
immediately installs the new configuration regardless of the
commitment status of the previous configuration. Force
reconfiguration can cause unexpected behavior, such as the
rollback of `"majority"` committed write operations.

To check the commitment status of the current replica configuration,
issue `replSetGetConfig` with the 
commitmentStatus parameter 
on the replica set primary.

### Access Control

To run the method on deployments that enforce access
control, the user must have
`replSetConfigure` privilege action on the cluster
resource. The `clusterManager` built-in role, available in
the `admin` database, provides the required privileges for this
command.

### Locking Behavior

`rs.reconfig()` obtains a special mutually
exclusive lock to prevent more than one
`rs.reconfig()` operation from occurring at the same
time.

### Mixed Version Replica Set

**Warning:**

Avoid reconfiguring replica sets that contain members of different
MongoDB versions as validation rules may differ across MongoDB versions.

### Availability

The `rs.reconfig()` shell method can trigger the current primary
to step down in some situations. Primary step-down triggers an 
election to select a new primary:

When the primary steps down, it stops any in-progress writes. For details, see 
replSetStepDown-behavior.

The median time before a cluster elects a new primary should not
typically exceed 12 seconds, assuming default `replica
configuration settings`. This includes time required to
mark the primary as unavailable and
call and complete an election.
You can tune this time period by modifying the 
`settings.electionTimeoutMillis` replication configuration 
option. Factors such as network latency may extend the time required
for replica set elections to complete, which in turn affects the amount 
of time your cluster may operate without a primary. These factors are 
dependent on your particular cluster architecture.

During the election process, the cluster cannot
accept write operations until it elects the new primary.

Your application connection logic should include tolerance for automatic
failovers and the subsequent elections. MongoDB drivers
can detect the loss of the primary and automatically 
retry certain write operations a single time, 
providing additional built-in handling of automatic failovers and elections:

Compatible drivers enable retryable writes by default

To further reduce potential impact to a production cluster,
reconfigure only during scheduled maintenance periods.

### `{ force: true }`

**Warning:**

MongoDB does not synchronize a forced replica set reconfiguration
between the replica sets in a cluster. Using `{ force: true }` can
lead to a rollback of majority-committed writes and an
inconsistent sharded cluster. Exercise caution when you use this option.

### Member Priority and Votes

- .. include:: /includes/fact-rs-nonzero-priority-vote-restriction.rst
   
- .. include:: /includes/fact-rs-non-voting-priority-restriction.rst

### Drop Outgoing Connections After Removing a Member

..
  This behavior will change once SERVER-36417 closes. 

Using `rs.reconfig()` to remove a replica set member does not
automatically drop open outgoing connections from other replica set
members to the removed member.

By default, replica set members wait for 5 minutes before dropping
connections to the removed member. In sharded replica sets, you can
modify this timeout using the
`ShardingTaskExecutorPoolHostTimeoutMS` server parameter.

To immediately drop all outgoing connections from the replica set to
the removed member, run the `dropConnections`
administrative command on each remaining member on the replica set:

```javascript
db.adminCommand( 
  {
    "dropConnections" : 1,
    "hostAndPort" : [
      "<hostname>:<port>"
    ] 
  } 
)
```

Replace `<hostname>` and `<port>` with those of the removed 
member.

### Automatic Reconfiguration for New Voting Replica Set Members

Starting in MongoDB 5.0, a newly added secondary does not count as a
voting member and cannot be elected until it has reached the
`SECONDARY` state.

When a new voting node is added to a replica set,
`replSetReconfig` will internally add a `newlyAdded`
field to the node's configuration. Nodes with the `newlyAdded` field
do not count towards the current number of voting nodes. When initial
sync completes and the node reaches `SECONDARY` state, the
`newlyAdded` field is automatically removed.

**Note:**

- Configurations that attempt to add a field named `newlyAdded`
  will error even if run with `{ force: true }`.

- If an existing node has a `newlyAdded` field, using
  `rs.reconfig()` to change the configuration will not
  remove the `newlyAdded` field. The `newlyAdded` field will be
  appended to the user provided configuration.

- `replSetGetConfig` will remove any `newlyAdded` fields
  from its output. If you would like to see any `newlyAdded`
  fields, you can query the `local.system.replset` collection
  directly.

## Examples

A replica set named `rs0` has the following configuration:

```javascript
{
   "_id" : "rs0",
   "version" : 1,
   "protocolVersion" : Long(1),
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
         "secondaryDelaySecs" : Long(0),
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
         "secondaryDelaySecs" : Long(0),
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
         "secondaryDelaySecs" : Long(0),
         "votes" : 1
      }
   ],
   "settings" : {
      "chainingAllowed" : true,
      "heartbeatIntervalMillis" : 2000,
      "heartbeatTimeoutSecs" : 10,
      "electionTimeoutMillis" : 10000,
      "catchUpTimeoutMillis" : 2000,
      "getLastErrorModes" : {

      },
      "getLastErrorDefaults" : {
         "w" : 1,
         "wtimeout" : 0
      },
      "replicaSetId" : ObjectId("58858acc1f5609ed986b641b")
   }
}
```

   

### Change Replica Set Member Priority

The following sequence of operations updates the
`members[n].priority` of the second member. The operations are
issued through a `mongosh` session that is connected to
the primary.

```javascript
cfg = rs.conf();
cfg.members[1].priority = 2;
rs.reconfig(cfg);
```

#. The first statement uses the `rs.conf()` method to retrieve
   a document containing the current configuration for the replica set and sets the
   document to the local variable `cfg`.

#. The second statement sets a
   `members[n].priority` value to the
   second document in the `members` array.
   For additional settings, see replica set configuration settings.

   To access the member configuration document in the array, the
   statement uses the array index and **not** the replica set member's
   `members[n]._id` field.

#. The last statement calls the `rs.reconfig()` method with the
   modified `cfg` to initialize this new configuration. Upon
   successful reconfiguration, the replica set configuration will
   resemble the following:

```javascript
{
   "_id" : "rs0",
   "version" : 2,
   "protocolVersion" : Long(1),
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
         "secondaryDelaySecs" : Long(0),
         "votes" : 1
      },
      {
         "_id" : 1,
         "host" : "mongodb1.example.net:27017",
         "arbiterOnly" : false,
         "buildIndexes" : true,
         "hidden" : false,
         "priority" : 2,
         "tags" : {

         },
         "secondaryDelaySecs" : Long(0),
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
         "secondaryDelaySecs" : Long(0),
         "votes" : 1
      }
   ],
   "settings" : {
      "chainingAllowed" : true,
      "heartbeatIntervalMillis" : 2000,
      "heartbeatTimeoutSecs" : 10,
      "electionTimeoutMillis" : 10000,
      "catchUpTimeoutMillis" : 2000,
      "getLastErrorModes" : {

      },
      "getLastErrorDefaults" : {
         "w" : 1,
         "wtimeout" : 0
      },
      "replicaSetId" : ObjectId("58858acc1f5609ed986b641b")
   }
}
```

### Change Replica Set Settings

You can also modify the cluster replica set `settings` document.
The `settings` document contains configuration options that 
apply to the whole replica set.

The following sequence of operations updates the 
`settings.heartbeatTimeoutSecs` of the cluster to `15`.
The operations are issued through a `mongosh` session 
that is connected to the primary.

```javascript
cfg = rs.conf();
cfg.settings.heartbeatTimeoutSecs = 15;
rs.reconfig(cfg);
```

**See also:**

- `rs.conf()`
- replSetGetConfig-output
- /administration/replica-set-member-configuration
- /administration/replica-set-maintenance
