<!-- Converted from tutorial/replace-config-server.txt (reStructuredText). Includes are inlined. -->

# Replace a Self-Managed Config Server

**Important:**

The following procedure applies to 6.0 config 
servers. For earlier versions of MongoDB, refer to the corresponding 
version of the MongoDB Manual.

## Overview

If the config server replica set becomes read only, i.e. does not
have a primary, the sharded cluster cannot support operations that change
the cluster metadata, such as chunk splits and migrations. Although no
chunks can be split or migrated, applications will be able to write data
to the sharded cluster.

If one of the config servers is unavailable or inoperable, repair or
replace it as soon as possible. The following procedure replaces a member
of a config server replica set with a new
member.

The tutorial is specific to MongoDB 6.0. For earlier 
versions of MongoDB, refer to the corresponding version of the MongoDB
Manual.

## Considerations

The following restrictions apply to a replica set configuration when used
for config servers:

- Must have zero arbiters.

- Must have no delayed members.

- Must build indexes (i.e. no member should have
  `members[n].buildIndexes` setting set to false).

## Procedure

**Step 1: Start the replacement config server.**

Start a `mongod` instance, specifying the `--configsvr`,
`--replSet`, `--bind_ip` options, and other options as
appropriate to your deployment.

**Warning:**

Before binding to a non-localhost (e.g. publicly accessible) 
IP address, ensure you have secured your cluster from unauthorized
access. For a complete list of security recommendations, see 
/administration/security-checklist. At minimum, consider 
enabling authentication and 
hardening network infrastructure.

```sh
mongod --configsvr --replSet <replicaSetName> --bind_ip localhost,<hostname(s)|ip address(es)>
```

**Step 2: Add the new config server to the replica set.**

Connect `mongosh` to the primary of the config server
replica set and use `rs.add()` to add the new member.

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

```javascript
rs.add( { host: "<hostnameNew>:<portNew>", priority: 0, votes: 0 } )
```

The initial sync process copies all the data from one member of the
config server replica set to the new member without restarting.

`mongos` instances automatically recognize the change in the
config server replica set members without restarting.

**Step 3: Update the newly added config server's votes and priority settings.**

a. Ensure that the new member has reached `SECONDARY`
   state. To check the state of the replica set members, run
   `rs.status()`:

   ```javascript
   rs.status()
   ```

#. Reconfigure the replica set to update the votes and priority of
   the new member:

   ```javascript
   var cfg = rs.conf();

   cfg.members[n].priority = 1;  // Substitute the correct array index for the new member
   cfg.members[n].votes = 1;     // Substitute the correct array index for the new member

   rs.reconfig(cfg)
   ```

   where `n` is the array index of the new member in the
   `members` array.

**Warning:**

- The `rs.reconfig()` shell method can force the current
  primary to step down, which causes an election. When the primary steps down, the
  `mongod` closes all client connections. While this
  typically takes 10-20 seconds, try to make these changes during
  scheduled maintenance periods.

- .. include:: /includes/warning-mixed-version-rs-config.rst

**Step 4: Shut down the member to replace.**

If replacing the primary member, step down the primary first before
shutting down.

**Step 5: Remove the member to replace from the config server replica set.**

Upon completion of initial sync of the replacement config server,
from a `mongosh` session that is connected to the
primary, use `rs.remove()` to remove the old member.

```javascript
rs.remove("<hostnameOld>:<portOld>")
```

`mongos` instances automatically recognize the change in the
config server replica set members without restarting.

**Step 6: If necessary, update `mongos` configuration or DNS entry.**

With replica set config servers, the `mongos` instances specify
in the `--configdb` or `sharding.configDB` setting the config
server replica set name and at least one of the replica set members. 

As such, if the `mongos` instance does not specify the
removed replica set member in the `--configdb` or
`sharding.configDB` setting, no further action is necessary.

If, however, a `mongos` instance specified the removed
member in the `--configdb` or `configDB`
setting, either:

- Update the setting for the next time you restart the
  `mongos`, or

- Modify the DNS entry that points to the system that provided the old
  config server, so that the *same* hostname points to the new
  config server.
