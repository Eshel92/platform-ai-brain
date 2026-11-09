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

If `mongod` stops unexpectedly, the program can recover everything 
written to the journal. MongoDB will re-apply the write operations on restart 
and maintain a consistent state. By default, the greatest extent of lost writes, 
i.e., those not made to the journal, are those made in the last 100 
milliseconds, plus the time it takes to perform the actual journal writes. See
`commitIntervalMs` for more information on
the default.

## Procedures

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

        #. Update
           `storage.wiredTiger.engineConfig.journalCompressor`
           to the new value.

           If you use command-line options instead of a configuration file, 
           you must update the `--wiredTigerJournalCompressor` command-line option during
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
             file, update `--wiredTigerJournalCompressor` to the new value.

             ```bash
             mongod --wiredTigerJournalCompressor <differentCompressor|none>  ...
             ```

   - id: replset
     name: "Replica Set Member"
     content: |

        Use the following procedure to change the journal compressor
        for a member of a replica set:

        #. Perform a clean shutdown of the `mongod`
           instance. For example, connect `mongosh` to
           the instance and issue `db.shutdownServer()`:

           ```javascript
           db.getSiblingDB('admin').shutdownServer()
           ```

        #. Update
           `storage.wiredTiger.engineConfig.journalCompressor` 
           to the new value.

           If you use command-line options instead of a configuration file, 
           you must update the command-line options during the 
           restart below.

        #. Restart the `mongod` instance:

           - If you are using a configuration file:

             ```bash
             mongod -f <path/to/myconfig.conf>
             ```

           - If you are using command-line options instead of a configuration
             file, update `--wiredTigerJournalCompressor` to the new 
             value.

             ```bash
             mongod --wiredTigerJournalCompressor <differentCompressor|none> ...
             ```

   - id: shardedcluster
     name: "Sharded Cluster Member"
     content: |

        Use the following procedure to change the journal compressor
        for a member of a shard replica set or config server replica set:

        #. Perform a clean shutdown of the `mongod`
           instance. For example, connect `mongosh` to
           the instance and issue `db.shutdownServer()`:

           ```javascript
           db.getSiblingDB('admin').shutdownServer()
           ```

        #. Update 
           `storage.wiredTiger.engineConfig.journalCompressor` 
           to the new value.

           If you use command-line options instead of a configuration file, 
           you must update the command-line options during the 
           restart below.

        #. Restart the `mongod` instance:

           - If you are using a configuration file:

             ```bash
             mongod -f <path/to/myconfig.conf>
             ```

           - If you are using command-line options instead of a configuration
             file, update `--wiredTigerJournalCompressor` to the new value.

             ```bash
             mongod --shardsvr --wiredTigerJournalCompressor <differentCompressor|none> --replSet ...
             ```
