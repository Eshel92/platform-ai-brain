<!-- Converted from tutorial/manage-journaling.txt (reStructuredText). Includes are inlined. -->

# Configure Journaling for Self-Managed Deployments

MongoDB uses *write ahead logging* to an on-disk journal to
guarantee write operation durability.

The WiredTiger storage engine does not require journaling to guarantee
a consistent state after a crash. The database will be restored to the
last consistent checkpoint
during recovery.  However, if MongoDB exits unexpectedly in between
checkpoints, journaling is required to recover writes that occurred
after the last checkpoint.

**Note:**

You cannot specify `--nojournal` option or `storage.journal.enabled: false` 
for replica set members that use the WiredTiger storage engine.

With journaling enabled, if `mongod` stops unexpectedly, the
program can recover everything written to the journal. MongoDB will
re-apply the write operations on restart and maintain a consistent
state. By default, the greatest extent of lost writes, i.e., those not
made to the journal, are those made in the last 100 milliseconds, plus
the time it takes to perform the actual journal writes. See
`commitIntervalMs` for more information on
the default.

## Procedures

### Disable Journaling

**Warning:**

Do not disable journaling on production systems.

- .. include:: /includes/wiredtiger-node-nojournal.rst

To disable journaling for a standalone deployment, start
`mongod` with the `--nojournal` command line option.

### Get Commit Acknowledgement

You can get commit acknowledgment with the write-concern and
the `j` option. For details, see
write-concern-operation.

### Monitor Journal Status

The `serverStatus` command/`db.serverStatus()`
method returns `wiredTiger.log`, which contains
statistics on the journal.

### Recover Data After Unexpected Shutdown

On a restart after a crash, MongoDB replays all journal files in the
journal directory before the server becomes available. If MongoDB must
replay journal files, `mongod` notes these events in the log
output.

There is no reason to run `--repair`.

### Change WiredTiger Journal Compressor

With the WiredTiger storage engine, MongoDB, by default, uses the
`snappy` compressor for the journal. To specify a different
compressions algorithm or no compression for a `mongod`
instance:

**Tip:**

If you encounter an unclean shutdown for a `mongod`
during this procedure, you must use the old compressor settings to
recover using the journal files. Once recovered, you can retry the
procedure.

tabs:

   - id: standalone
     name: Standalone
     content: |

        Use the following procedure to change the journal compressor
        for a standalone `mongod` instance:

        #. Update the
           `storage.wiredTiger.engineConfig.journalCompressor` setting
           to the new value.

           If you use command-line options instead of a configuration file, you
           will have to update the `--wiredTigerJournalCompressor` command-line option during
           the restart below.

        #. Perform a clean shutdown of the `mongod`
           instance. For example, connect `mongosh` to
           the instance and issue `db.shutdownServer()`:

           ```javascript
           db.getSiblingDB('admin').shutdownServer()
           ```

        #. Once you have confirmed that the process is no longer running,
           restart the `mongod` instance:

           - If you are using a configuration file:

             ```bash
             mongod -f <path/to/myconfig.conf>
             ```

           - If you are using command-line options instead of a configuration
             file, update the `--wiredTigerJournalCompressor` option.

             ```bash
             mongod --wiredTigerJournalCompressor <differentCompressor|none>  ...
             ```

   - id: replset
     name: "Replica Set Member"
     content: |

        Use the following procedure to change the journal compressor
        for a member of a replica set:

        **Note:**

        The following procedure involves restarting the replica member as a
        standalone without the journal.

        #. Perform a clean shutdown of the `mongod`
           instance. For example, connect `mongosh` to
           the instance and issue `db.shutdownServer()`:

           ```javascript
           db.getSiblingDB('admin').shutdownServer()
           ```

        #. Update the configuration file to prepare to restart as a
           standalone:

           - Set `storage.journal.enabled` to `false`.

           - Comment out the replication settings
             for your deployment.

           - Set parameter `disableLogicalSessionCacheRefresh` to
             `true` in the `setParameter` section.

           For example:

           ```none
           storage:
              journal:
                 enabled: false
           #replication:
           #   replSetName: replA
           setParameter:
              disableLogicalSessionCacheRefresh: true
           ```

           If you use command-line options instead of a configuration file, you
           will have to update the command-line option during the restart.

        #. Restart the `mongod` instance:

           - If you are using a configuration file:

             ```bash
             mongod -f <path/to/myconfig.conf>
             ```

           - If you are using command-line options instead of a
             configuration file, 

             - Include the `--nojournal` option

             - Remove any replication command-line options (such as `--replSet`):

             - Set parameter `disableLogicalSessionCacheRefresh`
               to `true` in the `--setParameter` option.

               ```bash
               mongod --nojournal --setParameter disableLogicalSessionCacheRefresh=true  ...
               ```

        #. Perform a clean shutdown of the `mongod` instance:

           ```javascript
           db.getSiblingDB('admin').shutdownServer()
           ```

           Confirm that the process is no longer running.

        #. Update the configuration file to prepare to restart as a replica set
           member with the new journal compressor:

           - Remove the `storage.journal.enabled` setting.

           - Uncomment the replication
             settings for your deployment.

           - Remove the `disableLogicalSessionCacheRefresh`
             parameter.

           - Remove
             `storage.wiredTiger.engineConfig.journalCompressor` setting
             to use the default journal compressor or specify a  new value.

           For example:

           ```none
           storage:
              wiredTiger:
                 engineConfig:
                    journalCompressor: <newValue>
           replication:
              replSetName: replA
           ```

           If you use command-line options instead of a configuration file, you
           will have to update the command-line options during the restart
           below.

        #. Restart the `mongod` instance as a replica set member:

           - If you are using a configuration file:

             ```bash
             mongod -f <path/to/myconfig.conf>
             ```

           - If you are using command-line options instead of a configuration
             file:

             - Remove the `--nojournal` option.

             - Remove the `--wiredTigerJournalCompressor` command-line option to use
               the default journal compressor or update to a new value.

             - Include your replication command-line options as well as any additional
               options for your replica set member.

             - Remove the `disableLogicalSessionCacheRefresh`
               parameter.

             ```bash
             mongod --wiredTigerJournalCompressor <differentCompressor|none> --replSet ...
             ```

   - id: shardedcluster
     name: "Sharded Cluster Member"
     content: |

        Use the following procedure to change the journal compressor
        for a member of a shard replica set or config server replica set:

        **Note:**

        The following procedure involves restarting the replica member as a
        standalone without the journal.

        #. Perform a clean shutdown of the `mongod`
           instance. For example, connect `mongosh` to
           the instance and issue `db.shutdownServer()`:

           ```javascript
           db.getSiblingDB('admin').shutdownServer()
           ```

        #. Update the configuration file to prepare to restart as a
           standalone:

           - Set `storage.journal.enabled` to `false`.

           - Set parameter `skipShardingConfigurationChecks` to true.

           - Set parameter `disableLogicalSessionCacheRefresh` to
             `true` in the `setParameter` section.

           - Comment out the replication
             settings for your deployment.

           - Comment out the `sharding.clusterRole` setting.

           - Set the `net.port` to the member's
             current port, if it is not explicitly set.

           For example:

           ```none
           storage:
              journal:
                 enabled: false
           setParameter:
              skipShardingConfigurationChecks: true
              disableLogicalSessionCacheRefresh: true
           #replication:
           #   replSetName: shardA
           #sharding:
           #   clusterRole: shardsvr
           net:
             port: 27218
           ```

           If you use command-line options instead of a configuration file, you
           will have to update the command-line option during the restart.

        #. Restart the `mongod` instance:

           - If you are using a configuration file:

             ```bash
             mongod -f <path/to/myconfig.conf>
             ```

           - If you are using command-line options instead of a
             configuration file:

             - Include the `--nojournal`
               option.

             - Set parameter `skipShardingConfigurationChecks` to true.

             - Set parameter `disableLogicalSessionCacheRefresh`
               to `true` in the `--setParameter` option.

             - Remove any replication command-line options (such as `--replSet`).

             - Remove `--shardsvr`/`--configsvr` option.

             - Explicitly include `--port` set to
               the instance's current port.

             ```bash
             mongod --nojournal --setParameter skipShardingConfigurationChecks=true --setParameter disableLogicalSessionCacheRefresh=true --port <samePort> ...
             ```

        #. Perform a clean shutdown of the `mongod` instance:

           ```javascript
           db.getSiblingDB('admin').shutdownServer()
           ```

           Confirm that the process is no longer running.

        #. Update the configuration file to prepare to restart with the new journal compressor:

           - Remove the `storage.journal.enabled` setting.

           - Remove the `skipShardingConfigurationChecks` parameter setting.

           - Remove the `disableLogicalSessionCacheRefresh`
             parameter setting.

           - Uncomment the replication
             settings for your deployment.

           - Uncomment the `sharding.clusterRole` setting.

           - Remove
             `storage.wiredTiger.engineConfig.journalCompressor` setting
             to use the default journal compressor or specify a  new value.

           For example:

           ```none
           storage:
              wiredTiger:
                 engineConfig:
                    journalCompressor: <newValue>
           replication:
              replSetName: shardA
           sharding:
              clusterRole: shardsvr
           net:
             port: 27218
           ```

           If you use command-line options instead of a configuration file, you
           will have to update the command-line options during the restart
           below.

        #. Restart the `mongod` instance as a replica set member:

           - If you are using a configuration file:

             ```bash
             mongod -f <path/to/myconfig.conf>
             ```

           - If you are using command-line options instead of a configuration
             file:

             - Remove the `--nojournal` option.

             - Remove the `skipShardingConfigurationChecks` parameter setting.

             - Remove the `disableLogicalSessionCacheRefresh`
               parameter.

             - Remove the `--wiredTigerJournalCompressor` command-line option to use
               the default journal compressor or update to a new value.

             - Include `--shardsvr`/`--configsvr` option.

             - Include your replication command-line options as well as any additional
               options for your replica set member.

             ```bash
             mongod --shardsvr --wiredTigerJournalCompressor <differentCompressor|none> --replSet ...
             ```
