<!-- Converted from reference/replica-configuration.txt (reStructuredText). Includes are inlined. -->

# Self-Managed Replica Set Configuration

You can access the configuration of a replica set using the
`rs.conf()` method or the `replSetGetConfig` command.

To modify the configuration for a replica set, use the
`rs.reconfig()` method, passing a configuration document to the
method.

**Warning:**

Avoid reconfiguring replica sets that contain members of different
MongoDB versions as validation rules may differ across MongoDB versions.

## Replica Set Configuration Document Example

The following document provides a representation of a replica set
configuration document. The configuration of your replica set may
include only a subset of these settings:

```none
{
  _id: <string>,
  version: <int>,
  term: <int>,
  protocolVersion: <number>,
  writeConcernMajorityJournalDefault: <boolean>,
  configsvr: <boolean>,
  members: [
    {
      _id: <int>,
      host: <string>,
      arbiterOnly: <boolean>,
      buildIndexes: <boolean>,
      hidden: <boolean>,
      priority: <number>,
      tags: <document>,
      secondaryDelaySecs: <int>,
      votes: <number>
    },
    ...
  ],
  settings: {
    chainingAllowed : <boolean>,
    heartbeatIntervalMillis : <int>,
    heartbeatTimeoutSecs: <int>,
    electionTimeoutMillis : <int>,
    catchUpTimeoutMillis : <int>,
    getLastErrorModes : <document>,
    getLastErrorDefaults : <document>,
    replicaSetId: <ObjectId>
  }
}
```

## Replica Set Configuration Fields

**`_id`**

*Type*: string

The name of the replica set.

`_id` *must* be identical to the
`replication.replSetName` or the value of `--replSet`
specified to `mongod` on the command line.

**See also:**

`replSetName` or `--replSet`
for information on setting the replica set name.

**`version`**

*Type*: int

An incrementing number used to distinguish revisions of the replica
set configuration document from previous iterations of the
configuration.

Replica set members use `term` and `version` to
achieve consensus on the "newest" replica configuration. When
members compare replica configuration documents, the configuration
document with a larger `term` is considered the "newest".
If `term` is the same or absent, the configuration
document with the larger `version` is considered "newest".

**`term`**

*Type*: int

Only available with featureCompatibilityVersion (FCV) "4.4" or later.

An incrementing number used to distinguish revisions of the replica
set configuration document from previous iterations of the
configuration. The `term` of a configuration document matches
the term of the replica set primary which performed the
reconfiguration. The primary increments its term each time it
steps up after winning an election. The primary ignores the
`term` field if set explicitly in the
`replSetReconfig` operation.

Issuing a force reconfiguration
removes the `term` field. When the primary next issues
`replSetReconfig` *without* force, it sets the
`term` to its own term.

Replica set members use `term` and `version` to
achieve consensus on the "newest" replica configuration. When members
compare replica configuration documents, the configuration document
with a larger `term` is considered the "newest". If
`term` is the same or absent, the configuration document with
the larger `version` is considered "newest".

**`configsvr`**

*Type*: boolean

*Default*: false

Indicates whether the replica set is used for a sharded cluster's
config servers. Set to `true` if the replica set is for a sharded
cluster's config servers.

**`protocolVersion`**

*Type*: number

*Default*: 1

MongoDB only supports `protocolVersion: 1` and no longer supports
`protocolVersion: 0`.

**See also:**

replica-set-protocol-version

**`writeConcernMajorityJournalDefault`**

*Type*: boolean

*Default*: true

Determines the behavior of `{ w: "majority" }` write concern if the write concern does not explicitly
specify the journal option j.

The following table lists the `writeConcernMajorityJournalDefault`
values and the associated `{ w: "majority" }` behavior:

| Value | `{ w: "majority" }` Behavior |
|---|---|
| true | MongoDB acknowledges the write operation after a majority of the voting members have written to the on-disk journal. IMPORTANT: All voting members of the replica set must run with journaling when `writeConcernMajorityJournalDefault` is `true`. If any voting member of a replica set uses the in-memory storage engine, you must set `writeConcernMajorityJournalDefault` to `false`. If any voting member of a replica set uses the in-memory storage engine and `writeConcernMajorityJournalDefault` is `true`, `"majority"` write operations may fail. These include operations that inherently use `"majority"` write concern, such as the `replSetStepDown` command, or various `mongosh` methods that by default use `"majority"` write concern, such as user management methods and role management methods. Starting in version 4.2 (and 4.0.13 and 3.6.14 ), if a replica set member uses the in-memory storage engine (voting or non-voting) but the replica set has `writeConcernMajorityJournalDefault` set to true, the replica set member logs a startup warning. |
| false | MongoDB acknowledges the write operation after a majority of the voting members have applied the operation in memory. WARNING: If any voting member of a replica set uses the in-memory storage engine, you must set `writeConcernMajorityJournalDefault` to `false`. Starting in version 4.2 (and 4.0.13 and 3.6.14 ), if a replica set member uses the in-memory storage engine (voting or non-voting) but the replica set has `writeConcernMajorityJournalDefault` set to true, the replica set member logs a startup warning. You cannot run transactions on a sharded cluster that has a shard with `writeConcernMajorityJournalDefault` set to `false` (such as a shard with a voting member that uses the in-memory storage engine). |

**See also:**

- wc-ack-behavior
- replica-set-protocol-version

### `members`

**`members`**

*Type*: array

An array of member configuration documents, one for each member
of the replica set. The `members` array
is a zero-indexed array.

Each member-specific configuration document can contain the following
fields:

**`members[n]._id`**

*Type*: integer

An integer identifier for the member in the replica set, unique
among all members.

Starting in MongoDB 5.0, values may be any integer value greater
than or equal to `0`. Previously, this value was limited to an
integer between `0` and `255` inclusive.

Each replica set member must have a unique
`_id`. Avoid re-using `_id` values
*even if* no `members[n]` entry is using that `_id` in
the current configuration.

Once set, you cannot change the
`_id` of a member.

**Note:**

When updating the replica configuration object, access the replica set
members in the `members` array with the
**array index**. The array index begins with `0`. Do **not** confuse
this index value with the value of the
`members[n]._id` field in each document in
the `members` array.

**`members[n].host`**

*Type*: string

The hostname and, if specified, the port number, of the set
member.

The host name must be resolvable for every host in the
replica set.

**Warning:**

`members[n].host` cannot hold a
value that resolves to `localhost` or the local interface
unless *all* members of the set are on hosts that resolve to
`localhost`.

**`members[n].arbiterOnly`**

*Optional*.

*Type*: boolean

*Default*: false

A boolean that identifies an arbiter. A value of `true`
indicates that the member is an arbiter.

When using the `rs.addArb()` method to add an arbiter,
the method automatically sets
`members[n].arbiterOnly` to `true`
for the added member.

**`members[n].buildIndexes`**

*Optional*.

*Type*: boolean

*Default*: true

A boolean that indicates whether the `mongod` builds
indexes on this member. You can only set this
value when adding a member to a replica set. You cannot change
`members[n].buildIndexes` field after
the member has been added to the set. To add a member, see
`rs.add()` and `rs.reconfig()`.

Do not set to `false` for `mongod` instances that receive
queries from clients.

Setting `buildIndexes` to `false` may be useful if **all**
the following conditions are true:

- you are only using this instance to perform backups using
  `mongodump`, *and*

- this member will receive no queries, *and*

- index creation and maintenance overburdens the host
  system.

Even if set to `false`, secondaries *will* build indexes on the
`_id` field to facilitate operations required for
replication.

**Warning:**

If you set
`members[n].buildIndexes` to
`false`, you must also set
`members[n].priority` to `0`. If
`members[n].priority` is not
`0`, MongoDB will return an error when attempting to add a
member with
`members[n].buildIndexes` equal to
`false`.

To ensure the member receives no queries, you should make all
instances that do not build indexes hidden.

Other secondaries cannot replicate from a member where
`members[n].buildIndexes` is
false.

**`members[n].hidden`**

*Optional*.

*Type*: boolean

*Default*: false

When this value is `true`, the replica set hides this instance
and does not include the member in the output of
`db.hello()` or `hello`. This prevents
read operations (that is, queries) from ever reaching this host by
way of secondary read preference.

Hidden members can acknowledge write operations
issued with write-concern. For write operations issued
with `"majority"` write concern, the member must
also be a voting member (that is, `votes` is
greater than `0`).

**See also:**

Hidden Replica Set Members

**`members[n].priority`**

*Optional*.

*Type*: Number between 0 and 1000 for primary/secondary members, or 0 or 1 for arbiters.

*Default*: 1.0 for primary/secondary members, or 0 for arbiters.

A number that indicates the relative likelihood of a replica set
member to become the primary.

- To increase the likelihood that a member becomes the primary,
  specify a higher `priority` value for that member.

- To decrease the likelihood that a member becomes the primary,
  specify a lower `priority` value for that member.

Changing a member's priority triggers one or more elections. The
election algorithm makes a best-effort attempt to elect the
highest-priority member the primary. However, a lower-priority
member may become the primary even if a higher-priority secondary
is available.

If a lower-priority member becomes the primary, the server
continues to periodically call elections until the
highest-priority replica set member is the primary. The frequency
at which the elections occur depends on the difference in priority
between the elected member and the highest-priority member.

A member with a priority of `0` cannot become the primary.

Non-voting members (meaning members that have
`votes` set to `0`) must have a priority of
`0`.

**See also:**

- Replica Set Elections
- rs-election-priority

**`members[n].tags`**

*Optional*.

*Type*: document

*Default*: none

A `tags` document contains user-defined tag field and value pairs for
the replica set member.

```javascript
{ "<tag1>": "<string1>", "<tag2>": "<string2>",... }
```

- For read operations, you can specify a tag set in the read
  preference to direct the
  operations to replica set member(s) with the specified tag(s).

- For write operations, you can create a customize write concern using
  `settings.getLastErrorModes` and
  `settings.getLastErrorDefaults`.

For more information, see
replica-set-configuration-tag-sets.

**`members[n].secondaryDelaySecs`**

*Optional*.

*Type*: integer

*Default*: 0

The number of seconds "behind" the primary that this
replica set member should "lag".

Use this option to create delayed members. Delayed members maintain a copy
of the data that reflects the state of the data at some time in
the past.

Delayed members can contribute to acknowledging write
operations issued with write-concern. However,
they return write acknowledgment no earlier than the configured
delay value. For write operations issued with
`"majority"` write concern, the member must also be
a voting member (that is, `votes` is greater than
`0`).

**See also:**

replica-set-delayed-members

**`members[n].votes`**

*Optional*.

*Type*: integer

*Default*: 1

The number of votes a server will cast in a replica set
election. The number of votes each
member has is either `1` or `0`, and arbiters always have exactly `1` vote.

Members with `priority` greater than 0 cannot have
0 `votes`.

A replica set can have up to `50 members` but only 7 voting members.
If you need more than 7 members in one replica set, set
`members[n].votes` to `0` for the
additional non-voting members.

Non-voting (i.e. `votes` is `0`) members must have
`priority` of 0.

Starting in MongoDB 5.0, a newly added secondary does not count as
a voting member and cannot be elected until it has reached
`SECONDARY` state.

Non-voting members cannot acknowledge write operations
issued with a `"majority"` write concern.

**See also:**

- `replSetGetStatus.votingMembersCount`
- `replSetGetStatus.writableVotingMembersCount`

### `settings`

**`settings`**

*Optional*.

*Type*: document

A document that contains configuration options that apply to the
whole replica set.

The `settings` document contains the
following fields:

**`settings.chainingAllowed`**

*Optional*.

*Type*: boolean

*Default*: true

In MongoDB 5.0.1 and earlier, if
`settings.chainingAllowed` is:

- `true`, replica set secondary members can
  replicate data from other secondary members.

- `false`, secondary members can replicate data only from the
  primary.

Starting in MongoDB 5.0.2:

- With an override enabled, replica set secondary
  members can replicate data from other secondary members
  even if `settings.chainingAllowed` is `false`.

- To override `settings.chainingAllowed` and allow
  replication from a secondary member, set the
  `enableOverrideClusterChainingSetting` server
  parameter to `true`.

- The default for
  `enableOverrideClusterChainingSetting` is `false`.

**See also:**

/tutorial/manage-chained-replication

**`settings.getLastErrorDefaults`**

*Optional*.

*Type*: document

Unavailable starting in MongoDB 5.0.

**Important:**

Starting in MongoDB 5.0, you cannot specify a default write concern with
`settings.getLastErrorDefaults` other than the default of 
`{ w: 1, wtimeout: 0 }` . Instead, use the 
`setDefaultRWConcern` command to set the default read or
write concern configuration for a replica set or sharded cluster.

**`settings.getLastErrorModes`**

*Optional*.

*Type*: document

A document used to define a custom write concern through the use of `members[n].tags`.
The custom write concern can provide data-center
awareness.

```none
{ getLastErrorModes: {
   <name of write concern> : { <tag1>: <number>, .... },
   ...
} }
```

The `<number>` refers to the number of different tag values
required to satisfy the write concern. For example, the following
`settings.getLastErrorModes` defines a write concern
named `datacenter` that requires the write to propagate to two
members whose `dc` tag values differ.

```none
{ getLastErrorModes: { datacenter: { "dc": 2 } } }
```

To use the custom write concern, pass in the write concern name
to the wc-w, for example:

```none
{ w: "datacenter" }
```

See replica-set-configuration-tag-sets for more
information and example.

**`settings.heartbeatTimeoutSecs`**

*Optional*.

*Type*: int

*Default*: 10

Number of seconds that the replica set members wait for a
successful heartbeat from each other. If a member does not
respond in time, other members mark the delinquent member as
inaccessible.

**`settings.electionTimeoutMillis`**

*Optional*.

*Type*: int

*Default*: 10000 (10 seconds)

The time limit in milliseconds for detecting when a replica set's
primary is unreachable. This setting controls failover sensitivity
when using `protocolVersion: 1`. You can
expect the failover timeout to not exceed the value of
`electionTimeoutMillis`.

Consider the following when selecting a value:

- Higher values result in slower failovers but decreased
  sensitivity to primary node or network slowness or spottiness.

- Lower values result in faster failover but increased
  sensitivity to primary node or network slowness or spottiness.

The setting only applies when using `protocolVersion: 1`.

**Note:**

When you step down a primary using `rs.stepDown` or
`replSetStepDown` without setting the `force` field to
`true`, the stepped-down primary nominates an eligible secondary
to call an election immediately. 

**`settings.catchUpTimeoutMillis`**

*Optional*.

*Type*: int

*Default*: -1, infinite catchup time.

Time limit in milliseconds for a newly elected primary to sync
(catch up) with the other replica set members that may have more
recent writes. Infinite or high time limits may reduce the
amount of data that the other members would need to roll back
after an election but may increase the failover time.

The newly elected primary ends the catchup period early once it
is fully caught up with other members of the set. During the
catchup period, the newly elected primary is unavailable for
writes from clients. Use `replSetAbortPrimaryCatchUp`
to abort the catchup then complete the transition to primary.

The setting only applies when using
`protocolVersion: 1`.

**`settings.catchUpTakeoverDelayMillis`**

*Optional*.

*Type*: int

*Default*: 30000 (30 seconds)

Time in milliseconds a node waits to initiate a
*catchup takeover* after determining it is ahead of the current
primary. During a catchup takeover, the node ahead of the
current primary initiates an election to become the new
primary of the replica set.

After the node initiating the takeover determines that it is
ahead of the current primary, it waits the specified
number of milliseconds and then verifies the following:

1. It is still ahead of the current primary,

#. It is the most up-to-date node among all available nodes,

#. The current primary is currently catching up to it.

Once determining that all of these conditions are met, the node
initiating the takeover immediately runs for election.

For more information on Replica
Set Elections, see replica-set-elections.

**Note:**

Setting `catchUpTakeoverDelayMillis` to `-1` disables
catchup takeover. Setting `catchUpTimeoutMillis` to
`0` disables *primary catchup* and consequently also catchup
takeover.

**`settings.heartbeatIntervalMillis`**

*Internal use only*.

The frequency in milliseconds of the heartbeats.

**`settings.replicaSetId`**

*Type*: ObjectId

The ObjectId associated with the replica set and automatically
created during `rs.initiate()` or
`replSetInitiate`. You cannot change the
`replicaSetId`.
