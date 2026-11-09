<!-- Converted from tutorial/upgrade-to-enterprise-sharded-cluster.txt (reStructuredText). Includes are inlined. -->

# Upgrade to MongoDB Enterprise (Sharded Cluster)

MongoDB Enterprise provides various features not available in the
MongoDB Community edition, such as:

- /core/inmemory

- /core/auditing

- /core/kerberos

- /core/security-ldap and /core/security-ldap-external

- /core/security-encryption-at-rest

The following steps outline the procedure to upgrade a sharded cluster
from the MongoDB Community Edition to the MongoDB Enterprise Edition.
For example, the steps can be used to upgrade MongoDB 6.0 Community to 
MongoDB 6.0 Enterprise.

## About This Task

### Upgrade Major Releases

**Warning:**

Do not use these instructions to upgrade to another release version.
To upgrade release versions, refer to the appropriate release
upgrade instructions, such as Upgrade to MongoDB 6.0.

### Ops Manager

With `Ops Manager`, you can automatically upgrade
from MongoDB Community Server to MongoDB Enterprise Server.

For more information, see
`Change MongoDB Version`.

### Rolling Upgrades

When updating the sharded clusters manually, you can perform a
rolling upgrade on the shard replica sets and config servers to
update each MongoDB Community Server to Enterprise edition with
minimal downtime.

In a rolling upgrade, each secondary is taken down and upgraded.
The Enterprise server rejoins the replica set as a
secondary. When all secondaries are upgraded, you can
step down the primary, forcing the replica set to elect
one of the Enterprise servers as the new primary. 

## Steps

To minimize downtime, manually upgrade each from MongoDB
Community Server to Enterprise Edition: 

**Step 1: Stop the balancer**

During an upgrade, the balancer should not attempt to
redistribute data between the shards. To prevent the
balancer from attempting to redistribute data, stop the
balancer for the duration of the upgrade.

To stop the balancer, connect to `mongos` and run
the `sh.stopBalancer` method:

```javascript
sh.stopBalancer()
```

If a balancing round is in progress, the operation waits
for balancing to complete.

To confirm that the balancer is stopped, use the
`sh.getBalancerState` method:

```javascript
sh.getBalancerState()
```

Output:

```javascript
false
```

The command returns `false` when the balancer is stopped.

**Step 2: Upgrade the config servers**

Perform a rolling upgrade of the config servers.

For the procedure, see Upgrade a Replica Set to
MongoDB Enterprise.

**Step 3: Upgrade the shards**

Perform a rolling upgrade on each shard.

For the procedure, see Upgrade a Replica Set to
MongoDB Enterprise.

**Step 4: Upgrade routers (mongos)**

Perform a rolling upgrade of the `mongos`
instances from the Community installation to Enterprise. 

a. Connect to `mongos` and stop the router process:

   ```javascript
   db.getSiblingDB("admin").shutdownServer()
   ```

#. .. include:: /includes/tabs-remove-com-mongos

#. .. include:: /includes/extracts/enterprise-install-binaries.rst

#. To start the router, run Enterprise `mongos` with the
   same configuration as you used for the Community
   `mongos`.

   For example:

   ```bash
   sudo mongos --config /etc/mongos.conf
   ```

**Step 5: Restart the balancer**

To restart the balancer, connect to `mongos` and
use the `sh.startBalancer` method:

```javascript
sh.startBalancer()
```

To confirm that the balancer is running, use the
`sh.getBalancerState` method:

```javascript
sh.getBalancerState()
```

Output:

```javascript
true
```

The command returns `true` when the balancer is running.

**Important:**

Before using any Enterprise features, ensure that all members have
been upgraded to Enterprise edition.
