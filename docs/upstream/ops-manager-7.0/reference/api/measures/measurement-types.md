<!-- Converted from reference/api/measures/measurement-types.txt (reStructuredText). Includes are inlined. -->

# Measurement Types

The `measurements` endpoint returns the available measurement types
for use with the Ops Manager Measurements API resource.

## Host Measurements

* - - `ASSERT_REGULAR`
    - `ASSERT_WARNING`
    - `ASSERT_MSG`
    - `ASSERT_USER`

  - Rate of asserts for a MongoDB process found in the 
    `asserts` document that the
    serverStatus
    command generates.

* - - `BACKGROUND_FLUSH_AVG`

  - Amount of data flushed in the background.

* - - `CACHE_BYTES_READ_INTO`
    - `CACHE_BYTES_WRITTEN_FROM`
    - `CACHE_DIRTY_BYTES`
    - `CACHE_USED_BYTES`
    - `TICKETS_AVAILABLE_READS`
    - `TICKETS_AVAILABLE_WRITE`

  - Amount of bytes in the WiredTiger
    storage engine cache and tickets found in the
    `wiredTiger.cache` and
    `wiredTiger.concurrentTransactions` documents
    that the
    serverStatus
    command generates.

* - - `CONNECTIONS`

  - Number of connections to a MongoDB process found in the
    `connections` document that the
    serverStatus
    command generates.

* - - `CURSORS_TOTAL_OPEN`
    - `CURSORS_TOTAL_TIMED_OUT`

  - Number of cursors for a MongoDB
    process found in the `metrics.cursor` document 
    that the 
    serverStatus
    command generates.

* - - `EXTRA_INFO_PAGE_FAULTS`
    - `GLOBAL_ACCESSES_NOT_IN_MEMORY`
    - `GLOBAL_PAGE_FAULT_EXCEPTIONS_THROWN`

  - Numbers of `Memory Issues` and `Page Faults` for a MongoDB
    process.

* - - `GLOBAL_LOCK_CURRENT_QUEUE_TOTAL`
    - `GLOBAL_LOCK_CURRENT_QUEUE_READERS`
    - `GLOBAL_LOCK_CURRENT_QUEUE_WRITERS`

  - Number of operations waiting on locks for the MongoDB process
    that the 
    serverStatus 
    command generates. Ops Manager computes these values based on the
    type of storage engine.

* - - `INDEX_COUNTERS_BTREE_ACCESSES`
    - `INDEX_COUNTERS_BTREE_HITS`
    - `INDEX_COUNTERS_BTREE_MISSES`
    - `INDEX_COUNTERS_BTREE_MISS_RATIO`

  - Number of index btree operations.

* - - `JOURNALING_COMMITS_IN_WRITE_LOCK`
    - `JOURNALING_MB`
    - `JOURNALING_WRITE_DATA_FILES_MB`

  - Number of journaling operations.

* - - `MEMORY_RESIDENT`
    - `MEMORY_VIRTUAL`
    - `MEMORY_MAPPED`
    - `COMPUTED_MEMORY`

  - Amount of memory for a MongoDB process found in the
    `mem` document that the
    serverStatus command collects.

* - - `NETWORK_BYTES_IN`
    - `NETWORK_BYTES_OUT`
    - `NETWORK_NUM_REQUESTS`

  - Amount of throughput for MongoDB process found in the
    `network` document that the 
    serverStatus command collects.

* - - `OPLOG_REPLICATION_LAG_TIME`
    - `OPLOG_RATE_GB_PER_HOUR`
    - `OPLOG_MASTER_TIME`
    - `OPLOG_MASTER_LAG_TIME_DIFF`

  - Durations and throughput of the MongoDB process'
    oplog.
    The `OPLOG_SLAVE_LAG_MASTER_TIME` metric is deprecated in the
    measurement API. Use the `OPLOG_REPLICATION_LAG_TIME` metric
    instead. It returns decimal values (seconds and milliseconds).
    For example, the value 2.75 means 2 seconds and 750 milliseconds.

* - - `DB_STORAGE_TOTAL`

  - Sum total of the compressed on-disk storage space allocated for 
    document storage across all databases.

* - - `DB_INDEX_SIZE_TOTAL`

  - Sum total of the logical size in bytes (including prefix compression) of 
    the index data across all databases.

* - - `DB_DATA_SIZE_TOTAL`

  - Sum total of the uncompressed document data in bytes (including 
    the padding factor) across all databases including system databases.

* - - `DB_DATA_SIZE_TOTAL_WO_SYSTEM`

  - Sum total of the uncompressed document data in bytes (including 
    the padding factor) across non-system databases.

* - - `OPCOUNTER_CMD`
    - `OPCOUNTER_QUERY`
    - `OPCOUNTER_UPDATE`
    - `OPCOUNTER_DELETE`
    - `OPCOUNTER_GETMORE`
    - `OPCOUNTER_INSERT`

  - Rate of database operations on a MongoDB process since the
    process last started found in the `opcounters` document that the 
    serverStatus command collects.

* - - `OPCOUNTER_REPL_CMD`
    - `OPCOUNTER_REPL_UPDATE`
    - `OPCOUNTER_REPL_DELETE`
    - `OPCOUNTER_REPL_INSERT`

  - Rate of database operations on MongoDB
    secondaries found in the
    `opcountersRepl` document that the
    serverStatus
    command collects.

* - - `DOCUMENT_METRICS_RETURNED`
    - `DOCUMENT_METRICS_INSERTED`
    - `DOCUMENT_METRICS_UPDATED`
    - `DOCUMENT_METRICS_DELETED`

  - Average rate of documents returned, inserted, updated, or
    deleted per second during a selected time period.

* - - `OPERATIONS_SCAN_AND_ORDER`

  - Average rate for operations per second during a selected time
    period that perform a sort but cannot perform the sort using an
    index.

* - - `OP_EXECUTION_TIME_READS`
    - `OP_EXECUTION_TIME_WRITES`
    - `OP_EXECUTION_TIME_COMMANDS`

  - Average execution time in milliseconds per read, write, or
    command operation during a selected time period.

    *Available to hosts running MongoDB 3.4 or later.*

* - - `RESTARTS_IN_LAST_HOUR`

  - Number of times the host restarted within the previous hour.

* - - `SYSTEM_MEMORY_USED`
    - `SYSTEM_MEMORY_FREE`
    - `SYSTEM_MEMORY_AVAILABLE`

  - Physical memory usage, in bytes.

* - - `SYSTEM_NETWORK_BYTES_IN`
    - `SYSTEM_NETWORK_BYTES_OUT`

  - Network throughput in bytes per second.

* - - `SWAP_USAGE_USED`
    - `SWAP_USAGE_FREE`

  - Total amount swap space in use.

|  |  |
|---|---|
| - `QUERY_EXECUTOR_SCANNED` | Average rate per second to scan index items during queries and query-plan evaluations found in the value of `totalKeysExamined` from the explain command. |
| - `QUERY_EXECUTOR_SCANNED_OBJECTS` | Average rate of documents scanned per second during queries and query-plan evaluations found in the value of `totalDocsExamined` from the explain command. |
| - `QUERY_TARGETING_SCANNED_PER_RETURNED` | Ratio of the number of index items scanned to the number of documents returned. |
| - `QUERY_TARGETING_SCANNED_OBJECTS_PER_RETURNED` | Ratio of the number of documents scanned to the number of documents returned. |

## Process Measurements

* - - `PROCESS_CPU_USER`
    - `MAX_PROCESS_CPU_USER` 
    - `PROCESS_CPU_KERNEL`
    - `MAX_PROCESS_CPU_KERNEL`
    - `PROCESS_CPU_CHILDREN_USER`
    - `MAX_PROCESS_CPU_CHILDREN_USER`
    - `PROCESS_CPU_CHILDREN_KERNEL`
    - `MAX_PROCESS_CPU_CHILDREN_KERNEL`

  - MongoDB CPU usage. For hosts with more than one CPU core,
    these values can exceed 100%.

    Requires Ops Manager Automation.

* - - `PROCESS_NORMALIZED_CPU_USER`
    - `MAX_PROCESS_NORMALIZED_CPU_USER` 
    - `PROCESS_NORMALIZED_CPU_KERNEL`
    - `MAX_PROCESS_NORMALIZED_CPU_KERNEL`
    - `PROCESS_NORMALIZED_CPU_CHILDREN_USER`
    - `MAX_PROCESS_NORMALIZED_CPU_CHILDREN_USER`
    - `PROCESS_NORMALIZED_CPU_CHILDREN_KERNEL`
    - `MAX_PROCESS_NORMALIZED_CPU_CHILDREN_KERNEL`

  - MongoDB CPU usage scaled to a range of 0% to 100% by dividing
    by the number of CPU cores.

    Requires Ops Manager Automation.

## System Measurements

* - - `SYSTEM_CPU_USER`
    - `MAX_SYSTEM_CPU_USER` 
    - `SYSTEM_CPU_KERNEL`
    - `MAX_SYSTEM_CPU_KERNEL`
    - `SYSTEM_CPU_NICE`
    - `MAX_SYSTEM_CPU_NICE`
    - `SYSTEM_CPU_IOWAIT`
    - `MAX_SYSTEM_CPU_IOWAIT`
    - `SYSTEM_CPU_IRQ`
    - `MAX_SYSTEM_CPU_IRQ`
    - `SYSTEM_CPU_SOFTIRQ`
    - `MAX_SYSTEM_CPU_SOFTIRQ`
    - `SYSTEM_CPU_GUEST`
    - `MAX_SYSTEM_CPU_GUEST`
    - `SYSTEM_CPU_STEAL`
    - `MAX_SYSTEM_CPU_STEAL`

  - CPU usage of processes on the host. For hosts with more
    than one CPU core, this value can exceed 100%.

    Requires Ops Manager Automation.

* - - `SYSTEM_NORMALIZED_CPU_USER`
    - `MAX_SYSTEM_NORMALIZED_CPU_USER` 
    - `SYSTEM_NORMALIZED_CPU_KERNEL`
    - `MAX_SYSTEM_NORMALIZED_CPU_KERNEL`
    - `SYSTEM_NORMALIZED_CPU_NICE`
    - `MAX_SYSTEM_NORMALIZED_CPU_NICE`
    - `SYSTEM_NORMALIZED_CPU_IOWAIT`
    - `MAX_SYSTEM_NORMALIZED_CPU_IOWAIT`
    - `SYSTEM_NORMALIZED_CPU_IRQ`
    - `MAX_SYSTEM_NORMALIZED_CPU_IRQ`
    - `SYSTEM_NORMALIZED_CPU_SOFTIRQ`
    - `MAX_SYSTEM_NORMALIZED_CPU_SOFTIRQ`
    - `SYSTEM_NORMALIZED_CPU_GUEST`
    - `MAX_SYSTEM_NORMALIZED_CPU_GUEST`
    - `SYSTEM_NORMALIZED_CPU_STEAL`
    - `MAX_SYSTEM_NORMALIZED_CPU_STEAL`

  - CPU usage of processes on the host scaled to a range of
    0 to 100% by dividing by the number of CPU cores.

    Requires Ops Manager Automation.

* - - `SYSTEM_MEMORY_USED`
    - `MAX_SYSTEM_MEMORY_USED`
    - `SYSTEM_MEMORY_FREE`
    - `MAX_SYSTEM_MEMORY_FREE`
    - `SYSTEM_MEMORY_AVAILABLE`
    - `MAX_SYSTEM_MEMORY_AVAILABLE`

  - Physical memory usage, in bytes.

* - - `SYSTEM_NETWORK_BYTES_IN`
    - `MAX_SYSTEM_NETWORK_IN` 
    - `SYSTEM_NETWORK_BYTES_OUT`
    - `MAX_SYSTEM_NETWORK_OUT`

  - Network throughput in bytes per second.

* - - `SWAP_USAGE_USED`
    - `MAX_SWAP_USAGE_USED`
    - `SWAP_USAGE_FREE`
    - `MAX_SWAP_USAGE_FREE`

  - Total amount swap space in use.

## Disk Measurements

* - - `DISK_PARTITION_IOPS_READ`
    - `MAX DISK_PARTITION_IOPS_READ`
    - `DISK_PARTITION_IOPS_WRITE`
    - `MAX_DISK_PARTITION_IOPS_WRITE`
    - `DISK_PARTITION_IOPS_TOTAL`
    - `MAX_DISK_PARTITION_IOPS_TOTAL`

  - Number of Input/Output operations for the disk partition that
    hosts MongoDB.

    Requires Ops Manager Automation.

* - - `DISK_PARTITION_LATENCY_READ`
    - `MAX_DISK_PARTITION_LATENCY_READ`
    - `DISK_PARTITION_LATENCY_WRITE`
    - `MAX_DISK_PARTITION_LATENCY_WRITE`

  - Latency per operation type of the disk partition that hosts
    MongoDB.

    Requires Ops Manager Automation.

* - - `DISK_PARTITION_SPACE_FREE`
    - `MAX_DISK_PARTITION_SPACE_FREE`
    - `DISK_PARTITION_SPACE_USED`
    - `MAX_DISK_PARTITION_SPACE_USED`
    - `DISK_PARTITION_SPACE_PERCENT_FREE`
    - `MAX_DISK_PARTITION_SPACE_PERCENT_FREE`
    - `DISK_PARTITION_SPACE_PERCENT_USED`
    - `MAX_DISK_PARTITION_SPACE_PERCENT_USED`

  - Measures the free disk space and used disk space on the disk
    partition used by MongoDB. Only available if you use Ops Manager
    Automation.

## Database Measurements

* - - `DATABASE_WRITE_LOCK_PERCENTAGE`

  - Duration that the host is write locked.

* - - `DATABASE_AVERAGE_OBJECT_SIZE`
    - `DATABASE_COLLECTION_COUNT`
    - `DATABASE_DATA_SIZE`
    - `DATABASE_FILE_SIZE`
    - `DATABASE_STORAGE_SIZE`
    - `DATABASE_INDEX_SIZE`
    - `DATABASE_INDEX_COUNT`
    - `DATABASE_EXTENT_COUNT`
    - `DATABASE_OBJECT_COUNT`

  - Amount of disk storage that database uses on-disk storage space
    found from the MongoDB
    dbStats command.

    By default, the Monitoring retrieves database
    measurements every 20 minutes but adjusts frequency when
    necessary to reduce the impact on database performance. To
    disable collecting database statistics in the Ops Manager, click
    Settings, then click Group Settings, and
    then set Collect Database Specific Statistics to
    `No`.
