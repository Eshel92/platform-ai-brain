<!-- Converted from tutorial/perform-maintenance-on-replica-set-members.txt (reStructuredText). Includes are inlined. -->

# Perform Maintenance on Self-Managed Replica Set Members

## Overview

Replica sets allow a MongoDB deployment to
remain available during the majority of a maintenance window.

This document outlines the basic procedure for performing maintenance on
each of the members of a replica set. Furthermore, this particular
sequence strives to minimize the amount of time that the
primary is unavailable and control the impact on the
entire deployment.

Use these steps as the basis for common replica set operations,
particularly for procedures such as upgrading to the latest
version of MongoDB. 

## Procedure

For each member of a replica set, starting with a secondary member,
perform the following sequence of events, ending with the primary:

- Restart the `mongod` instance as a standalone.

- Perform the task on the standalone instance.

- Restart the `mongod` instance as a member of the replica
  set.

**Step 1: Stop a secondary.**

In `mongosh`, shut down the `mongod` instance:

```javascript
db.shutdownServer()
```

**Step 2: Restart the secondary as a standalone on a different port.**

At the operating system shell prompt restart `mongod`
as a standalone instance.

tabs:
   - id: config-file
     name: Configuration File
     content: |

        If you are using a configuration file, make the following
        configuration updates:

        - Comment out the `replication.replSetName` option.

        - Change the `net.port` to a different port.
          Make a note of the original port setting as a comment.

        - Set parameter `disableLogicalSessionCacheRefresh` to
          `true` in the `setParameter` section.

        - If the `mongod` is a shard or
          config server member, you must also:

          - Comment out the `sharding.clusterRole` option.

          - Set parameter `skipShardingConfigurationChecks`
            to `true` in the `setParameter` section.

        For example, if performing maintenance on a shard/config
        server replica set member for maintenance, the updated
        configuration file will include content like the
        following example:

        ```yaml
        net:
           bindIp: localhost,<hostname(s)|ip address(es)>
           port: 27218
        #   port: 27018
        #replication:
        #   replSetName: shardA
        #sharding:
        #   clusterRole: shardsvr
        setParameter:
           skipShardingConfigurationChecks: true
           disableLogicalSessionCacheRefresh: true
        ```

   - id: command-line
     name: Command-line Options
     content: |

        If using command-line options, make the following
        configuration updates to restart:

        - Remove `--replSetName`.

        - Modify `--port` to a different port.

        - Set parameter `disableLogicalSessionCacheRefresh` to
          `true` in the `--setParameter` option.

        - If the `mongod` is a shard or
          config server member, you must also:

          - Remove `--shardsvr` if a
            shard member and `--configsvr` if a config server member.

          - Set parameter
            `skipShardingConfigurationChecks` to
            `true` in the `setParameter` section.

        For example, to restart a replica set member that is not part of a sharded cluster:

        ```bash
        mongod --port 27218 --dbpath /srv/mongodb --bind_ip localhost,<hostname(s)|ip address(es)> --setParameter disableLogicalSessionCacheRefresh=true
        ```

        For example, to restart a shard/config server replica set member for maintenance:

        ```bash
        mongod --port 27218 --dbpath /srv/mongodb --bind_ip localhost,<hostname(s)|ip address(es)> --setParameter skipShardingConfigurationChecks=true --setParameter disableLogicalSessionCacheRefresh=true
        ```

**Warning:**

Before you bind your instance to a publicly-accessible IP address,
you must secure your cluster from unauthorized access. For a complete
list of security recommendations, see
security-checklist. At minimum, consider
enabling authentication and hardening
network infrastructure.

Always start `mongod` with the same user, even when
restarting a replica set member as a standalone instance.

**Step 3: Perform maintenance operations on the secondary.**

While the member is a standalone, use `mongosh` to
perform maintenance:

```sh
mongo --port 27218
```

**Important:**

While the member is a standalone, no writes are replicated to
this member nor are writes on this member replicated to the other
members of the replica set.

Ensure that any writes on this standalone do not conflict with
oplog writes that will be applied to the member when it rejoins
the replica set.

**Step 4: Restart `mongod` as a member of the replica set.**

After performing all maintenance tasks, use the following procedure
to restart the `mongod` as a member of the replica set
on its usual port.

From `mongosh`, shut down the standalone
server after completing the maintenance:

```javascript
use admin
db.shutdownServer()
```

Restart the `mongod` instance as a replica set
member with its original configuration; that is, undo the
configuration changes made when starting as a standalone.

**Tip:**

Be sure to remove the `disableLogicalSessionCacheRefresh`
parameter.

For shard or config server members, be sure to remove the
`skipShardingConfigurationChecks` parameter.

When it has started, connect `mongosh` to the
restarted instance.

The secondary takes time to catch up to the primary. From `mongosh`, use the
following command to verify that the member has caught up from the
`RECOVERING` state to the `SECONDARY` state.

```javascript
rs.status()
```

**Step 5: Perform maintenance on the primary last.**

a. To perform maintenance on the primary after completing
   maintenance tasks on all secondaries, connect
   `mongosh` to the primary and use
   `rs.stepDown()` to step down the primary and allow one of
   the secondaries to be elected the new primary. Specify a 300
   second waiting period to prevent the member from being elected
   primary again for five minutes:

   ```javascript
   rs.stepDown(300)
   ```

   After the primary steps down, the replica set will elect a
   new primary.

b. Restart `mongod` as a standalone instance, making
   the following configuration updates.

tabs:
   - id: config-file
     name: Configuration File
     content: |

        If you are using a configuration file, make the following
        configuration updates:

        - Comment out the `replication.replSetName` option.

        - Change the `net.port` to a different port.
          Make a note of the original port setting as a comment.

        - Set parameter `disableLogicalSessionCacheRefresh` to
          `true` in the `--setParameter` option.

        - If the `mongod` is a shard or
          config server member, you must also:

          - Comment out the `sharding.clusterRole` option.

          - Set parameter `skipShardingConfigurationChecks`
            to `true` in the `setParameter` section.

        For example, if performing maintenance on a shard/config
        server replica set member for maintenance, the updated
        configuration file will include content like the
        following example:

        ```yaml
        net:
           bindIp: localhost,<hostname(s)|ip address(es)>
           port: 27218
        #   port: 27018
        #replication:
        #   replSetName: shardA
        #sharding:
        #   clusterRole: shardsvr
        setParameter:
           skipShardingConfigurationChecks: true
           disableLogicalSessionCacheRefresh: true
        ```

        **Warning:**

        Before you bind your instance to a publicly-accessible IP address,
        you must secure your cluster from unauthorized access. For a complete
        list of security recommendations, see
        security-checklist. At minimum, consider
        enabling authentication and hardening
        network infrastructure.

   - id: command-line
     name: Command-line Options
     content: |

        If using command-line options, make the following
        configuration updates:

        - Remove `--replSetName`.

        - Modify `--port` to a different port.

        - Set parameter `disableLogicalSessionCacheRefresh` to
          `true` in the `--setParameter` option.

        - If the `mongod` is a shard or
          config server member, you must also:

          - Remove `--shardsvr` if a
            shard member and `--configsvr` if a config server member.

          - Set parameter
            `skipShardingConfigurationChecks` to
            `true` in the `setParameter` section.

        For example, to restart a replica set member that is not part of a sharded cluster:

        ```bash
        mongod --port 27218 --dbpath /srv/mongodb --bind_ip localhost,<hostname(s)|ip address(es)> --setParameter disableLogicalSessionCacheRefresh=true
        ```

        For example, to restart a shard/config server replica set member for maintenance:

        ```bash
        mongod --port 27218 --dbpath /srv/mongodb --bind_ip localhost,<hostname(s)|ip address(es)> --setParameter skipShardingConfigurationChecks=true --setParameter disableLogicalSessionCacheRefresh=true
        ```

        **Warning:**

        Before you bind your instance to a publicly-accessible IP address,
        you must secure your cluster from unauthorized access. For a complete
        list of security recommendations, see
        security-checklist. At minimum, consider
        enabling authentication and hardening
        network infrastructure.

c. Perform maintentance task on the now standalone.

   **Important:**

   While the member is a standalone, no writes are replicated to
   this member nor are writes on this member replicated to the other
   members of the replica set.

   Ensure that any writes on this standalone do not conflict with
   oplog writes that will be applied to the member when it rejoins
   the replica set.

d. After performing all maintenance tasks, restart the
   `mongod` instance as a replica set member with its
   original configuration; that is, undo the configuration changes made
   when starting as a standalone.

   **Tip:**

   Be sure to remove the `disableLogicalSessionCacheRefresh`
   parameter.

   For shard or config server members, be sure to remove the
   `skipShardingConfigurationChecks` parameter.
