<!-- Converted from tutorial/build-indexes-on-replica-sets.txt (reStructuredText). Includes are inlined. -->

# Create a Rolling Index Build on Replica Sets

## About this Task

Rolling index builds are an alternative to default index builds.

Only use a rolling index build if your
deployment matches one of the following cases:

- If your average CPU utilization exceeds (N-1)/N-10% where where N is
  the number of CPU threads available to mongod
- If your WiredTiger cache fill ratio regularly exceeds 90%

**Warning:**

Avoid performing rolling index and replicated index build processes
concurrently as it might lead to unexpected issues, such as broken 
builds and crash loops.

**Note:**

If your deployment does not meet this criteria, use the
default index build. 

**Tip:**

With Atlas, you can temporarily [scale](https://www.mongodb.com/docs/atlas/scale-cluster/)
your cluster to meet the requirements for a traditional index build. However, 
Atlas charges to scale your cluster. See [Cluster Configuration Costs](https://www.mongodb.com/docs/atlas/billing/cluster-configuration-costs/) 
for more information. 

**Important:**

This feature is not supported on Atlas Infinite clusters.

## Considerations

### Unique Indexes

To create unique indexes using the following
procedure, you must stop all writes to the collection during this
procedure.

If you cannot stop all writes to the collection during this procedure,
do not use the procedure on this page. Instead, build your unique index
on the collection by issuing `db.collection.createIndex()` on
the primary for a replica set.

### Oplog Size

Ensure that your oplog is large enough to permit the indexing
or re-indexing operation to complete without falling too far behind to
catch up. See the oplog sizing
documentation for additional information. 

Rolling index builds lower the resiliency of your cluster and increase build 
duration.

## Prerequisites

For building unique indexes
   To create unique indexes using the
   following procedure, you must stop all writes to the collection
   during the index build. Otherwise, you may end up with inconsistent
   data across the replica set members. 

   **Warning:**

   If you cannot stop all writes to the collection, do not use the
   following procedure to create unique indexes.

## Procedure

**Important:**

The following procedure to build indexes in a rolling fashion
applies to replica set deployments, and not sharded clusters. For
the procedure for sharded clusters, see
/tutorial/build-indexes-on-sharded-clusters instead.

### 1. Hide and Restart One Secondary.

Run the following commands on your primary node to hide the secondary
that will build the new index.

In this example, the secondary that will build the new index is the
third node in `cfg.members`.

```bash
var cfg = rs.conf();
// Record originalPriority so that you can reset it later.
var originalPriority = cfg.members[2].priority;
cfg.members[2].priority = 0;
cfg.members[2].hidden = 1;
rs.reconfig(cfg);
```

### 2. Stop One Secondary and Restart as a Standalone.

Stop the `mongod` process associated with a secondary.
Restart after making the following configuration updates:

tabs:
   - id: config-file
     name: Configuration File
     content: |

       If you are using a configuration file, make the following
       configuration updates:

       - Comment out the `replication.replSetName` option.

       - Change the `net.port` to a different port. [#different-port]_
         Make a note of the original port setting as a comment.

       - Set parameter `disableLogicalSessionCacheRefresh` to
         `true` in the `setParameter` section.

       For example, the updated configuration file for a replica
       set member will include content like the following example:

       ```yaml
       net:
          bindIp: localhost,<hostname(s)|ip address(es)>
          port: 27217
       #   port: 27017
       #replication:
       #   replSetName: myRepl
       setParameter:
          disableLogicalSessionCacheRefresh: true
       ```

       Other settings (e.g. `storage.dbPath`, etc.) remain the same.

       And restart:

       ```bash
       mongod --config <path/To/ConfigFile>
       ```

   - id: command-line
     name: Command-line Options
     content: |

       If using command-line options, make the following
       configuration updates:

       - Remove `--replSet`.

       - Modify `--port` to a different port. [#different-port]_

       - Set parameter `disableLogicalSessionCacheRefresh`
         to `true` in the `--setParameter` option.

       For example, if your replica set member *normally* runs
       with on the default port of `27017` and the
       `--replSet` option, you would
       specify a different port, omit the `--replSet` option,
       and set `disableLogicalSessionCacheRefresh` parameter
       to true:

       ```bash
       mongod --port 27217 --setParameter disableLogicalSessionCacheRefresh=true
       ```

       Other settings (e.g. `--dbpath`, etc.) remain the same.

### 3. Build the Index.

Connect directly to the `mongod` instance running as a
standalone on the new port and create the new index for this
instance.

For example, connect `mongosh` to the instance, and
use the `createIndex()` to create an ascending
index on the `username` field of the `records` collection:

```bash
db.records.createIndex( { username: 1 } )
```

### 4. Restart the Program `mongod` as a Replica Set Member.

When the index build completes, shutdown the `mongod`
instance. To return the node to its original configuration, undo the
configuration changes that you made when you started the node as a
standalone. Then, restart the node as a member of the replica set.

**Important:**

Be sure to remove the `disableLogicalSessionCacheRefresh`
parameter.

   
For example, to restart your replica set member:

tabs:
   - id: config-file
     name: Configuration File
     content: |

       If you are using a configuration file:

       - Revert to the original port number.

       - Uncomment the `replication.replSetName`.

       - Remove parameter `disableLogicalSessionCacheRefresh`
         in the `setParameter` section.

       For example:

       ```yaml
       net:
          bindIp: localhost,<hostname(s)|ip address(es)>
          port: 27017
       replication:
          replSetName: myRepl
       ```

       Other settings (e.g. `storage.dbPath`, etc.) remain the same.

       And restart:

       ```bash
       mongod --config <path/To/ConfigFile>
       ```

   - id: command-line
     name: Command-line Options
     content: |

       If you are using command-line options, 

       - Revert to the original port number

       - Include the `--replSet`
         option.

       - Remove parameter `disableLogicalSessionCacheRefresh`.

       For example:

       ```bash
       mongod --port 27017 --replSet myRepl
       ```

       Other settings (e.g. `--dbpath`, etc.) remain the same.

**Important:**

Allow replication to catch up on this member before you begin the
next step. 

### 5. Unhide the Secondary.

Run the following command on your primary to unhide the secondary node
that built the index. In this example, the secondary node that built the
index is the third node in `cfg.members`. 

```bash
var cfg = rs.conf();
cfg.members[2].priority = originalPriority;
cfg.members[2].hidden = false;
rs.reconfig(cfg);
```

### 6. Repeat the Procedure for the Remaining Secondaries.

Once the member catches up with the other members of the set, repeat
the procedure one member at a time for the remaining secondary members:

A. Hide and restart one secondary.

B. Build the index.

C. Restart the Program mongod as a replica set member.

### 7. Build the Index on the Primary.

When all the secondaries have the new index, step down the primary,
restart it as a standalone using the procedure described above, 
and build the index on the former primary:

A. Use the `rs.stepDown()` method in `mongosh`
   to step down the primary. Upon successful stepdown, the current primary
   becomes a secondary and the replica set members elect a new primary.

B. Hide and restart one secondary.

C. Build the index.

D. Restart the Program mongod as a replica set member.
