<!-- Converted from tutorial/expand-replica-set.txt (reStructuredText). Includes are inlined. -->

# Add Members to a Self-Managed Replica Set

## Overview

This tutorial explains how to add an additional member to an existing
replica set. For background on replication deployment patterns,
see the /core/replica-set-architectures document.

### Maximum Voting Members

A replica set can have a maximum of seven voting members. To add a member to a replica set
that already has seven voting members, you must either add the member as a
non-voting member or remove a
vote from an `existing member`.

### Init Scripts

In production deployments you can configure a init script
to manage member processes.

### Existing Members

You can use these procedures to add new members to an existing replica
set.

**Warning:**

Each replica set node must belong to one, and only one, replica 
set. Replica set nodes cannot belong to more than one replica set.

### Restore Former Members

You can use these procedures to re-add a node that was removed.

If the data on the removed node is relatively recent, the node recovers
and catches up to the rest of the replica set. 

**Important:**

Avoid creating new replicated collections on the removed node while
it is in standalone mode. If the standalone node rejoins the replica
set, subsequent operations on the new collection produce an error. 

### Data Files

If you have a backup or snapshot of an existing member, you can move
the data files (for example, the `dbPath` directory)
to a new system and use them to quickly initiate a new member. The files
must be:

- A valid copy of the data files from a member of the same replica
  set. See /tutorial/backup-with-filesystem-snapshots
  document for more information.

  **Important:** Always use filesystem snapshots to create a copy of a

  member of the existing replica set. **Do not** use
  `mongodump` and `mongorestore` to seed a
  new replica set member.

- More recent than the oldest operation in the primary's oplog. The new member must be able to become
  current by applying operations from the primary's oplog.

### IP Binding

**Warning:**

Before you bind your instance to a publicly-accessible IP address,
you must secure your cluster from unauthorized access. For a complete
list of security recommendations, see
security-checklist. At minimum, consider
enabling authentication and hardening
network infrastructure.

MongoDB binaries, `mongod` and `mongos`, bind
to localhost by default. If the `net.ipv6` configuration file
setting or the `--ipv6` command line option is set for the binary,
the binary additionally binds to the localhost IPv6 address.

By default `mongod` and `mongos` that are
bound to localhost only accept connections from clients that are
running on the same computer. This binding behavior includes
`mongosh` and other members of your replica set or sharded
cluster. Remote clients cannot connect to binaries that are bound only
to localhost.

To override the default binding and bind to other IP addresses, use the
`net.bindIp` configuration file setting or the `--bind_ip`
command-line option to specify a list of hostnames or IP addresses.

**Warning:**

Starting in MongDB 5.0, [split horizon DNS](https://en.wikipedia.org/wiki/Split-horizon_DNS) nodes that are
only configured with an IP address fail startup validation and
report an error. See `disableSplitHorizonIPCheck`.

For example, the following `mongod` instance binds to both
the localhost and the hostname `My-Example-Associated-Hostname`, which is
associated with the IP address `198.51.100.1`:

```none
mongod --bind_ip localhost,My-Example-Associated-Hostname
```

In order to connect to this instance, remote clients must specify
the hostname  or its associated IP address `198.51.100.1`:

```none
mongosh --host My-Example-Associated-Hostname

mongosh --host 198.51.100.1
```

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

## Requirements

#. An active replica set.

#. A new MongoDB system capable of supporting your data set, accessible by
   the active replica set through the network.

Otherwise, use the MongoDB installation tutorial and the /tutorial/deploy-replica-set
tutorials.

## Procedures

### Prepare the Data Directory

Before adding a new member to an existing replica set, prepare
the new member's data directory using one of the
following strategies:

- Make sure the new member's data directory *does not* contain data. The
  new member will copy the data from an existing member.

  If the new member is in a recovering state, it must exit and
  become a secondary before MongoDB
  can copy all data as part of the replication process. This process
  takes time but does not require administrator intervention.

- Manually copy the data directory from an existing member. The new
  member becomes a secondary member and will catch up to the current
  state of the replica set. Copying the data over may shorten the
  amount of time for the new member to become current.

  Ensure that you can copy the data directory to the new member and
  begin replication within the window allowed by the oplog. Otherwise, the new instance will have
  to perform an initial sync, which completely resynchronizes the
  data, as described in /tutorial/resync-replica-set-member.

  Use `rs.printReplicationInfo()` to check the current state
  of replica set members with regards to the oplog.

For background on replication deployment patterns, see the
/core/replica-set-architectures document.

### Add a Member to an Existing Replica Set

**Important:**

To avoid configuration updates due to IP address changes, use DNS
hostnames instead of IP addresses. It is particularly important to
use a DNS hostname instead of an IP address when configuring replica
set members or sharded cluster members.

Use hostnames instead of IP addresses to configure clusters across a
split network horizon. Starting in MongoDB 5.0, nodes that are only
configured with an IP address fail startup validation and do not start.

1. Start the new `mongod` instance. Specify the data directory
   and the replica set name. The following example specifies the
   `/srv/mongodb/db0` data directory and the `rs0` replica set:

   ```bash
   mongod --dbpath /srv/mongodb/db0 --replSet rs0  --bind_ip localhost,<hostname(s)|ip address(es)>
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

   **Note:** Optional

   You can specify the data directory, replica set name, and the IP
   binding in the `mongod.conf` configuration file, and start the
   `mongod` with the following command:

   ```bash
   mongod --config /etc/mongod.conf
   ```

#. Connect to the replica set's primary.

   You can only add members while connected to the primary. If you do
   not know which member is the primary, log into any member of the
   replica set and issue the `db.hello()` command.

#. Use `rs.add()` to add the new member to the replica set.
   Pass the `member configuration document` to the
   method.  For example, to add a member at host
   `mongodb3.example.net`, issue the following command:

   ```javascript
   rs.add( { host: "mongodb3.example.net:27017" } )
   ```

   **Warning:**

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
