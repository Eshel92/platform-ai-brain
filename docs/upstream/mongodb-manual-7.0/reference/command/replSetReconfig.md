<!-- Converted from reference/command/replSetReconfig.txt (reStructuredText). Includes are inlined. -->

# replSetReconfig (database command)

## Definition

**`replSetReconfig`**

The `replSetReconfig` administrative command modifies the
configuration of an existing replica set. You can use this command to
add and remove members, and to alter the options set on existing
members. You must run this command on the `admin`
database of the primary replica set member.

**Tip:**

In `mongosh`, this command can also be run through the `rs.reconfig` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

**Important:**

This command is not supported in MongoDB Atlas clusters.
For information on Atlas support for all commands, 
see Unsupported Commands.

## Syntax

The command has the following syntax:

```javascript
db.adminCommand(
   { 
     replSetReconfig: <new_config_document>, 
     force: <boolean>,
     maxTimeMS: <int>
    }
 )
```

## Command Fields

The command takes the following optional field:

| Field | Description |
|---|---|
| .. _replSetReconfig-cmd-force: force | Defaults to `false`. Specify `true` to force the available replica set members to accept the new configuration. Force reconfiguration can result in unexpected or undesired behavior, including rollback of `"majority"` committed writes. |
| .. _replSetReconfig-cmd-maxTimeMS: maxTimeMS | Optional. Specifies a cumulative time limit in milliseconds for processing the `replSetReconfig`. By default, `replSetReconfig` waits indefinitely for the replica configuration to propagate to a majority of replica set members. Setting `maxTimeMS` may result in the operation failing *before* it can apply the new configuration. See replSetReconfig-cmd-majority-install for more information. |

You may also run `replSetReconfig` with the shell's
`rs.reconfig()` method.

## Behavior

### Global Write Concern

You must explicitly set the global default write concern before attempting to reconfigure a replica set with a configuration that would change the implicit
default write concern. To set the global default write concern, use the
`setDefaultRWConcern` command.

### `term` Replica Configuration Field

The `term` field is set by the primary replica set member. 
The primary ignores the `term` field if set explicitly in the
`replSetReconfig` operation.

### Reconfiguration Can Add or Remove No More than One Voting Member at a Time

`replSetReconfig` by default allows adding or
removing no more than `1` `voting`
member at a time. For example, a new configuration can make at most
*one* of the following changes to the cluster `membership`:

- Adding a new voting replica set member.

- Removing an existing voting replica set member.

- Modifying the `votes` for an existing replica
  set member.

To add or remove multiple voting members, issue a series of
`replSetReconfig` operations to add or remove one member at a
time.

Issuing a force reconfiguration
immediately installs the new configuration even if it adds or removes
multiple voting members. Force reconfiguration can cause unexpected
behavior, such as the rollback of `"majority"`
committed write operations.

### Reconfiguration Waits Until a Majority of Members Install the Replica Configuration

`replSetReconfig` waits until a majority of voting
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
   use by the primary at the time `replSetReconfig` is issued. 

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
   specified to `replSetReconfig`.

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

### Access Control

To run the command on deployments that enforce access
control, the user must have
`replSetConfigure` privilege action on the cluster
resource. The `clusterManager` built-in role, available in
the `admin` database, provides the required privileges for this
command.

### Locking Behavior

`replSetReconfig` obtains a special mutually
exclusive lock to prevent more than one
`replSetReconfig` operation from occurring at the same
time.

### Mixed Version Replica Set

**Warning:**

Avoid reconfiguring replica sets that contain members of different
MongoDB versions as validation rules may differ across MongoDB versions.

### Availability

A majority of the set's members must be operational for the changes to 
propagate properly.

`replSetReconfig` can trigger the current 
primary to step down in some situations. Primary step-down triggers 
an election to select a new 
primary:

- When the new primary steps up, it increments the `term` field to 
  distinguish configuration changes made on the new primary from changes made 
  on the previous primary.

- When the primary steps down, it no longer
  closes all client connections; however, writes that were in progress
  are killed. For details, see replSetStepDown-behavior.

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

### Drop Outgoing Connections After Removing a Member

Using `replSetReconfig` to remove a replica set member does
not automatically drop open outgoing connections from other replica
set members to the removed member.

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

**Warning:**

Starting in MongDB 5.0, [split horizon DNS](https://en.wikipedia.org/wiki/Split-horizon_DNS) nodes that are
only configured with an IP address fail startup validation and
report an error. See `disableSplitHorizonIPCheck`.

### Member Priority and Votes

- .. include:: /includes/fact-rs-nonzero-priority-vote-restriction.rst
   
- .. include:: /includes/fact-rs-non-voting-priority-restriction.rst

## Additional Information

replSetGetConfig-output,
/reference/replica-configuration, `rs.reconfig()`, and
`rs.conf()`.
