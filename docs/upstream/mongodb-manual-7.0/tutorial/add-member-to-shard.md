<!-- Converted from tutorial/add-member-to-shard.txt (reStructuredText). Includes are inlined. -->

# Add a Member to a Shard

You can add members to an existing shard in a sharded cluster.
You might want to add a member to a shard for the same reasons you'd 
want to add a member to any replica set. For example, 
increasing the number of members provides additional candidates to replace 
a primary in the event of a failover. 
Additional members also increase data redundancy and replica set 
availability.

For more information, refer to replica-set-architecture.

## About This Task

Before MongoDB 5.0, a newly added secondary still counts as a voting
member even though it can neither serve reads nor become primary until
its data is consistent. If you are running a MongoDB version earlier
than 5.0 and add a secondary with its `votes`
and `priority` settings greater than zero, this can
lead to a case where a majority of the voting members are
online but no primary can be elected. To avoid such situations,
consider adding the new secondary initially with
`priority :0` and `votes :0`. Then, run `rs.status()` to ensure the
member has transitioned into `SECONDARY` state. Finally, use
`rs.reconfig()` to update its priority and votes.

## Before You Begin

To add a member to a shard replica set, you need:

#. An active sharded cluster replica set.

#. A new host server for the new member. The new host server must be able 
   to support your sharded data set and be accessible by the active replica 
   set through the network.

## Steps

**Step 1: Prepare the Data Directory**

Prepare the new member's data directory using one of the
following strategies:

- Have the new member automatically sync data from an existing member.
  This process takes time but does not require administrator intervention.

  Make sure the new member's data directory *does not* contain data. The
  new member will copy the data from an existing member.

  If the new member is in a recovering state, it must exit and
  become a secondary before MongoDB
  can copy all data as part of the replication process.

- Manually copy the data directory from an existing member. The new
  member becomes a secondary member and will catch up to the current
  state of the replica set. Copying the data over may shorten the
  amount of time it takes for the new member to sync with the other 
  replica set members.

  Ensure that you can copy the data directory to the new member and
  begin replication within the window allowed by the oplog. Otherwise, the new instance will have
  to perform an initial sync, which completely resynchronizes the
  data, as described in resync-replica-member.

  To check the current state of replica set members with regards to the 
  oplog, use `rs.printReplicationInfo()`.

For background on replication deployment patterns, see the
/core/replica-set-architectures document.

**Step 2: Start the new `mongod` instance**

Specify the data directory
and the replica set name. The following example specifies the
`/srv/mongodb/db0` data directory and the `rs0` replica set:

```sh
mongod --dbpath /srv/mongodb/db0 --replSet rs0  --bind_ip localhost,<ip address of the mongod host>
```

**Warning:**

Before you bind your instance to a publicly-accessible IP address,
you must secure your cluster from unauthorized access. For a complete
list of security recommendations, see
security-checklist. At minimum, consider
enabling authentication and hardening
network infrastructure.

For more information on configuration options, see the
`mongod` manual page.

**Tip:**

You can specify the data directory, replica set name, and the ip
binding in the `mongod.conf` configuration file, and start the
`mongod` with the following command:

```sh
mongod --config /etc/mongod.conf
```

**Step 3: Connect to the replica set's primary**

You can only add members while connected to the primary. To connect to
the primary, use `mongosh`. Replace the `host` and `port` values 
with relevant values for your deployment:

```sh
mongosh --host mongodb0.example.com --port 28015
```

If you do not know which member is the primary, connect to any member 
of the replica set and issue the `db.hello()` command.

**Step 4: Use `rs.add()` to add the new member to the replica set**

Pass the `member configuration document` to the
method.  For example, to add a member at host
`mongodb3.example.net`, issue the following command:

```javascript
rs.add( { host: "mongodb3.example.net:27017", priority: 0, votes: 0 } )
```

**Step 5: Ensure that the new member has reached `SECONDARY` state**

To check the state of the replica set members, run
`rs.status()`:

```javascript
rs.status()
```

## Next Steps

Once the newly added member has transitioned into
`SECONDARY` state, use `rs.reconfig()` to update
the newly added member's `priority` and
`votes` if needed.

**Warning:**

- The `rs.reconfig()` shell method can force the current
  primary to step down, which causes an election. When the primary steps down, the
  `mongod` closes all client connections. While this
  typically takes 10-20 seconds, try to make these changes during
  scheduled maintenance periods.

- .. include:: /includes/warning-mixed-version-rs-config.rst

### Example

If `rs.conf()` returns the configuration document for 
`mongodb3.example.net:27017` as the fifth element in the 
`members` array, to update its priority and votes to
`1`, use the following sequence of operations:

```javascript
var cfg = rs.conf();
cfg.members[4].priority = 1
cfg.members[4].votes = 1
rs.reconfig(cfg)
```
