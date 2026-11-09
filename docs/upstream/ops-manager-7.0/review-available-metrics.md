<!-- Converted from review-available-metrics.txt (reStructuredText). Includes are inlined. -->

# Review Available Metrics

You can review the following metrics to monitor your 
deployments. All hardware metrics include metrics or 
individual charts for maximum values.

**Note:**

Ops Manager collects hardware metrics only if automation manages the process. 
A monitoring agent can only collect database metrics.

**Important:**

The metrics available depend on your user role and 
deployment type.

* - Metric

  - Description

* - Asserts

  - Displays the following information:

    - regular displays the average rate of 
      regular asserts raised per second over the selected sample 
      period. 

    - warning displays the average rate of 
      warnings per second over the selected sample period.

    - msg displays the average rate of message 
      asserts per second over the selected sample period. These 
      internal server errors have a well-defined text string. 
      MongoDB Atlas logs stack traces for these.

    - user displays the average rate of user 
      asserts per second over the selected sample period. This 
      metric includes asserts that a user generates, such as out of 
      disk space or duplicate key errors.

    Monitor asserts to track how many errors occur while trying to 
    read or write data. Check the server logs to identify the source 
    of any errors.

* - Avg Object Size

  - Displays the average object size across all collections in the 
    database.

    Monitor object size to track the size of your objects and better 
    understand your database space.

* - Background Flush Avg

  - Displays the average time of background flushes in seconds. 	
    `mongod` writes to and flushes (fsyncs) journal 
    files immediately. By default, all other data files are flushed 
    every 60 seconds in the background.

    Monitor the background flush average to determine whether this 
    statistic is a significant percentage of 60 seconds. If so, this 
    statistic could indicate that the server is bottlenecked on 
    these writes. You might have a large number of random writes 
    occurring. The operating system might flush data faster than 
    every 60 seconds. In that case, this statistic will be a very 
    small value even if the writing is a bottleneck.

* - Catalog

  - Displays the following information:

    - total databases displays the total number of 
      non-system databases.

    - total collections displays the total number of 
      collections across all non-system databases.

    - total views displays the total number of views 
      across all non-system databases.

    - total indexes displays the total number of indexes 
      across all non-system collections.

    Monitor catalog counts to prevent an excessive number of 
    databases, collections, views, or indexes from causing startup 
    failures.

* - Collections

  - Displays the number of collections in the database.

    Monitor collections to determine restart times, continuous 
    backup performance, and stability.

* - Connections

  - Displays the total number of active connections to the 
    deployment.

    Monitor connections to determine whether the current connection 
    limits are sufficient.

* - Cursors

  - Displays the following information:

    - totalOpen displays the number of cursors that the 
      server is maintaining for clients. Since MongoDB exhausts 
      unused cursors, this value is usually small or zero. However, 
      if there is a queue, stale tailable cursors, or a large number 
      of operations, this value might rise.

    - timedOut displays the average rate of cursors 
      that have timed out per second over the selected sample period.

    Monitor cursors to close unnecessary cursors and reduce the 
    timeout configuration in the application.

* - Data Size

  - Displays the actual size of the data files in the database.

    Monitor data size to ensure that database is not using too much 
    memory or CPU.

* - DB Storage

  - Displays the following information:

    - storageSize displays the sum 
      total amount of on-disk storage space allocated for document 
      storage across all databases.

    - dataSize displays the amount 
      of storage space in bytes that your stored data uses.

    - indexSize displays the sum total 
      size in bytes of the index data across all databases.

    Monitor storage space to determine whether to manually increase 
    the disk size.

* - Disk IOPS

  - Displays input operations per second.

    Monitor whether disk IOPS approaches the maximum provisioned 
    IOPS. Determine whether the deployment can handle future 
    workloads.

* - Disk Latency

  - Displays the following information:

    - read latency displays the average amount of time 
      to read from disk.

    - write latency displays the average amount of time 
      to write to disk.

    Monitor disk latency to track the efficiency of reading from and 
    writing to disk.

* - Disk Queue Depth

  - Displays the average length of the queue of requests issued 
    to the disk partition that stores MongoDB data.

    Monitor disk queue depth to identify potential issues and bottlenecks.

* - Disk Space Free

  - Displays the total amount of free space remaining on disk.

    Monitor free disk space to determine whether to use disk 
    auto-scaling or manually increase the disk size.

* - Disk Space Percent Free

  - Displays the total amount of free space remaining on disk as a 
    percentage of the total disk space.

    Monitor the percentage of free disk space to determine whether 
    to use disk auto-scaling or manually increase the disk size.

* - Disk Space Used

  - Displays the total bytes of used disk space on the partition 
    that runs MongoDB.

    Monitor the used disk space to determine whether to manually 
    increase the disk size.

* - Document Metrics

  - Displays the following information:

    - returned displays the documents per second 
      returned.

    - inserted displays the documents per second 
      inserted.

    - updated displays the documents per second updated.

    - deleted displays the documents per second deleted.

    Monitor document metrics to measure the work MongoDB completes.

* - File Size

  - Displays the total size of all the data files in the database.

    Monitor file size to deternine whether files are consuming 
    excessive disk space.

* - Index Size

  - Displays the total size of all indexes in the database. This 
    metric includes the overhead incurred by indexes on top of the 
    actual document data on which the indexes are based.

    Monitor the index size to manage your indexes. To learn more, 
    see Indexing Strategies. 

* - Indexes

  - Displays the total number of indexes in the database.

    Monitor indexes to manage them. To learn more, 
    see Indexing Strategies.

* - Max Disk IOPS

  - Displays the following maximum disk IOPS values over the time 
    period specified by the metric granularity:

    - max read iops maximum disk read input operations 
      per second.

    - max write iops maximum disk write input operations 
      per second.

    Monitor whether disk IOPS approaches the maximum provisioned 
    IOPS. Determine whether the deployment can handle future 
    workloads.

* - Max Disk Queue Depth
  - Displays the maximum disk queue depth values over the time 
    period specified by the metric granularity. Disk queue depth 
    is the average length of the queue of requests issued to the 
    disk partition that stores MongoDB data.

    Monitor disk queue depth to identify potential issues and bottlenecks.

* - Max Normalized System CPU

  - Displays the maximum CPU usage values of all processes on the 
    node, scaled to a range of 0-100% by dividing by the number of 
    CPU cores.

    Monitor CPU usage to determine whether data is retrieved from 
    disk instead of memory.

* - Max Process CPU

  - Displays the following maximum process CPU values over the time 
    period specified by the metric granularity:

    - max user displays the maximum percentage of time 
      that the CPU spent servicing the MongoDB process.

    - max kernel displays the maximum percentage of time 
      the CPU spent servicing operating system calls for the MongoDB 
      process.

    Monitor CPU usage to determine whether data is retrieved from 
    disk instead of memory.

* - Max System CPU

  - Displays the maximum CPU usage values of all processes on the 
    node.

    Monitor CPU usage to determine whether data is retrieved from 
    disk instead of memory.

* - Max System Memory

  - Displays the maximum system memory values in bytes.

    Monitor memory to determine whether your currrent deployment 
    meets your memory needs.

* - Memory

  - Displays the total consumption of memory in megabytes at a 
    particular point in time:

    - resident displays the memory that the MongoDB 
      process running on a node consumes. This metric excludes the 
      consumption of other processes and does not represent the 
      total memory that the node consumes.

    - virtual displays the memory reserved in disk to 
      act as swap space.

    - mapped displays the number of MMAPv1 memory maps 
      of all the data files. This number is likely similar to your 
      total database(s) size. WiredTiger does not use memory mapped 
      files, so this should be 0.

    Monitor memory to determine whether your currrent deployment 
    meets your memory needs.

* - Network

  - Displays the following information:

    - bytesIn displays the average rate of physical 
      bytes (after any wire compression) sent to this database 
      server per second over the selected sample period.

    - bytesOut displays the average rate of physical  
      bytes (after any wire compression) sent from this database 
      server per second over the selected sample period.

    - numRequests displays the average rate of requests 
      sent to this database server per second over the selected 
      sample period.

    Monitor network metrics to track network performance.

* - Non-Mapped Virtual Memory

  - Displays the amount of virtual memory that the memory mapping of 
    data files doesn't take into account.

    Monitor non-mapped virtual memory to determine whether aspects 
    other than memory mapping files use excessive memory. For 
    example, this could indicate too many connections to the 
    database. Each connection has a thread stack and the memory for 
    those stacks can add up to a considerable amount. Keep this 
    statistic reasonably low because the memory used here is 
    unavailable for caching.

* - Normalized Process CPU

  - Displays the following information:

    - user displays the percentage of time that the CPU 
      spent servicing the MongoDB process, scaled to a range of 
      0-100% by dividing by the number of CPU cores.

    - kernel displays the percentage of time the CPU 
      spent servicing operating system calls for the MongoDB 
      process, scaled to a range of 0-100% by dividing by the number 
      of CPU cores.

    Monitor CPU usage to determine whether data is retrieved from 
    disk instead of memory.

* - Normalized System CPU

  - Displays the CPU usage of all processes on the node, scaled to a 
    range of 0-100% by dividing by the number of CPU cores.

    Monitor CPU usage to determine whether data is retrieved from 
    disk instead of memory.

* - Num Extents

  - Displays the total number of contiguously allocated chunks of 
    data file space for the database.

    Monitor this metric to better understand your database space.

* - Objects

  - Displays the number of objects in the database.

    Monitor this metric to better understand your database space.

* - OpCounters

  - Displays the number of the following operations per second run 
    on a MongoDB process since the process last started:

    - command (replica set) or cmd (sharded 
      cluster)

    - query

    - insert

    - delete

    - update

    - getmore

    Monitor MongoDB operations to validate performance issues 
    related to high workloads. Confirm the type of operations 
    responsible for the load.

* - Page Faults

  - Displays the average rate of page faults on this process per 
    second over the selected sample period. In non-Windows 
    environments this applies to hard page faults only.

    Monitor page faults to determine whether to increase your memory.

* - Process CPU

  - Displays the following information:

    - user displays the percentage of time that the CPU 
      spent servicing the MongoDB process.

    - kernel displays the percentage of time the CPU 
      spent servicing operating system calls for the MongoDB process.

    Monitor CPU usage to determine whether data is retrieved from 
    disk instead of memory.

* - Queues

  - Displays the following information:

    - total displays the number of operations queued 
      and waiting for any lock. 

    - readers displays the number of operations queued 
      and waiting for a read lock.

    - writers displays the number of operation queued 
      and waiting for a write lock.

    Monitor queues to identify potential issues and bottlenecks.

* - Query Targeting

  - Displays the following information:

    - scanned displays the number of index 
      items scanned per second.

    - scanned objects displays the number of documents 
      scanned per second.

    Monitor query targeting to determine whether you have any 
    inefficient queries.

* - Query Targeting

  - Displays the efficiency of read operations run on MongoDB:

    - scanned / returned displays the number of 
      documents scanned to return one document.

    - scanned objects / returned the ratio of the number 
      of documents scanned to the number of documents returned by 
      queries, since the previous data point for the selected sample 
      period.

    Monitor query targeting to determine read efficiency and 
    optimize queries and indexes.

* - Scan and Order

  - Displays the number of operations per second returning results 
    that required a sort in-memory.

    Monitor this metric to identify whether your queries need 
    indexes.

* - Shard Data Size

  -  Displays the amount of storage space in bytes that your 
     stored data uses on each shard. You can access this chart only 
     for sharded clusters with MongoDB 6.0+.

     Monitor this metric to verify whether you have balanced shards.

* - Shard Document Count

  - Displays the number of documents on each shard. You can access 
    this chart only for sharded clusters with MongoDB 6.0+.

    Monitor this metric to verify whether you have balanced shards.

* - Storage Size

  - Displays the storage size of the database.

    Monitor storage size to determine whether to manually increase 
    the disk size.

* - Swap IO (Internal)

  - Displays the rate at which the operating system swaps memory pages between RAM and disk:

    - swapped pages in / sec shows how many pages per 
      second the operating system reads from swap into memory.

    - swapped pages out / sec shows how many pages per 
      second the operating system writes from memory to swap.

    A high or sustained rate of swap IO can correlate with increased 
    latency and memory pressure on the host. 

    Use this metric to understand how frequently the host performs 
    swap input and output operations.

* - Swap Usage 

  - Displays the following information about swap space on the host:

    - used displays the total amount of swap space currently in use.

    - free displays the total amount of swap space that 
      is still available.

    - max used displays the maximum total amount of swap space 
      in use over the selected time period.

    - max free displays the maximum amount of 
      available swap space over the selected time period.

    Sustained high swap usage can indicate memory pressure on the host.

    Monitor swap usage to identify when the operating system starts 
    moving memory pages to disk.

* - System CPU

  - Displays the CPU usage of all processes on the node.

    Monitor CPU usage to determine whether data is retrieved from 
    disk instead of memory.

* - System Network

  - Displays the following information:

    - network bytes in displays the average rate of 
      physical bytes that the network interface receives per second.

    - network bytes out displays the average rate of 
      physical bytes that the network interface transmits per second.

    - max network bytes in displays the maximum network 
      bytes in values over the time period that the metric 
      granularity specifies.

    - max network bytes out displays the maximum network 
      bytes out values over the time period that the metric 
      granularity specifies. 

    Monitor network metrics to track network performance.
