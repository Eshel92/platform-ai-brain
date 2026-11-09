<!-- Converted from faq/diagnostics.txt (reStructuredText). Includes are inlined. -->

# FAQ: Self-Managed MongoDB Diagnostics

This document provides answers to common diagnostic questions and
issues.

If you don't find the answer you're looking for, check
the complete list of FAQs or post your question to the
[MongoDB Community](https://community.mongodb.com/).

## Where can I find information about a `mongod` process that stopped running unexpectedly?

If `mongod` shuts down unexpectedly on a UNIX or UNIX-based
platform, and if `mongod` fails to log a shutdown or error
message, then check your system logs for messages pertaining to MongoDB.
For example, for logs located in `/var/log/messages`, use the
following commands:

```bash
sudo grep mongod /var/log/messages
sudo grep score /var/log/messages
```

## Does TCP `keepalive` time affect MongoDB Deployments?

If you experience network timeouts or socket errors in communication
between clients and servers, or between members of a sharded cluster or
replica set, check the *TCP keepalive value* for the affected systems.

Many operating systems set this value to `7200` seconds (two hours) by
default. For MongoDB, you will generally experience better results with
a shorter keepalive value, on the order of `120` seconds (two
minutes).

If your MongoDB deployment experiences keepalive-related issues, you
must alter the keepalive value on *all* affected systems. This includes
all machines running `mongod` or `mongos`
processes and all machines hosting client processes that connect to
MongoDB.

### Adjusting the TCP keepalive value:

**linux-keepalive:**

- To view the keepalive setting on Linux, use one of the following
  commands:

  ```bash
  sysctl net.ipv4.tcp_keepalive_time
  ```

  Or:

  ```bash
  cat /proc/sys/net/ipv4/tcp_keepalive_time
  ```

  The value is measured in seconds.

  **Note:**

  Although the setting name includes `ipv4`, the
  `tcp_keepalive_time` value applies to both IPv4 and IPv6.

- To change the `tcp_keepalive_time` value, you can use one of the
  following commands, supplying a *<value>* in seconds:

  ```bash
  sudo sysctl -w net.ipv4.tcp_keepalive_time=<value>
  ```

  Or:

  ```bash
  echo <value> | sudo tee /proc/sys/net/ipv4/tcp_keepalive_time
  ```

  These operations do not persist across system reboots. To persist
  the setting, add the following line to `/etc/sysctl.conf`,
  supplying a *<value>* in seconds, and reboot the machine:

  ```bash
  net.ipv4.tcp_keepalive_time = <value>
  ```

  Keepalive values greater than `300` seconds,
  (5 minutes) will be overridden on `mongod` and
  `mongos` sockets and set to `300` seconds.

**windows-keepalive:**

- To view the keepalive setting on Windows, issue the following command:

  ```powershell
  reg query HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters /v KeepAliveTime
  ```

  The registry value is not present by default. The system default,
  used if the value is absent, is `7200000` milliseconds or
  `0x6ddd00` in hexadecimal.

  |

- To change the `KeepAliveTime` value, use the following command in
  an Administrator Command Prompt, where `<value>` is
  expressed in hexadecimal (e.g. `120000` is `0x1d4c0`):

  ```powershell
  reg add HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\ /t REG_DWORD /v KeepAliveTime /d <value>
  ```

  Windows users should consider the [Windows Server Technet Article on KeepAliveTime](https://technet.microsoft.com/en-us/library/cc957549.aspx) for
  more information on setting keepalive for MongoDB deployments on
  Windows systems. Keepalive values greater than or equal to
  *600000* milliseconds (10 minutes) will be ignored by
  `mongod` and `mongos`.

**macos-keepalive:**

- To view the keepalive setting on macOS, issue the following command:

  ```bash
  sysctl net.inet.tcp.keepidle
  ```

  The value is measured in milliseconds.

  |

- To change the `net.inet.tcp.keepidle` value, you can use the
  following command, supplying a *<value>* in milliseconds:

  ```bash
  sudo sysctl net.inet.tcp.keepidle=<value>
  ```

  This operation does not persist across system reboots, and must be
  set each time your system reboots. See your operating system's
  documentation for instructions on setting this value persistently.
  Keepalive values greater than or equal to `600000` milliseconds
  (10 minutes) will be ignored by `mongod` and
  `mongos`.

  **Note:**

  In macOS 10.15 Catalina, Apple no longer allows for configuration
  of the `net.inet.tcp.keepidle` option.

You will need to restart `mongod` and `mongos`
processes for new system-wide keepalive settings to take effect.

## Do TCP Retransmission Timeouts affect MongoDB Deployments?

If you experience long stalls (stalls greater than two minutes) followed
by network timeouts or socket errors between clients and server
or between members of a sharded cluster or replica set, 
check the `tcp_retries2` value for the affected systems.

Most Linux operating systems set this value to `15` by default, while
Windows sets it to `5`.  For MongoDB, you experience better results
with a lower `tcp_retries2` value, on the order of `5` (12 seconds)
or lower.

If your MongoDB deployment experiences TCP retransmission timeout-related 
issues, change the `tcp_retries2` value (`TcpMaxDataRetransmission` 
on Windows) for *all* affected systems. This includes all machines running 
`mongod` or `mongos` processes and 
all machines hosting client processes that connect to MongoDB.

### Adjust the TCP Retransmission Timeout

**linux:**

On most Linux operating systems, control the TCP retransmission
by adjusting the `net.ipv4.tcp_retries2` sysctl setting.

**Note:**

Although the setting name includes `ipv4`, the `tcp_retries2` setting
applies to both IPv4 and IPv6.

- To view the current setting, use the `sysctl` command:

  ```bash
  sysctl net.ipv4.tcp_retries2
  ```

  Output:

  ```bash
  net.ipv4.tcp_retries = 15
  ```

- To change the `tcp_retries2` setting at runtime, use the `sysctl` command:

  ```bash
  sysctl -w net.ipv4.tcp_retries2=8
  ```

- To make the change permanent, edit the configuration file:

  #. Open `/etc/sysctl.conf` in your preferred text editor:

     ```bash
     vi /etc/sysctl.conf
     ```

  #. Configure the `net.ipv4.tcp_retries2` setting:

     ```conf
     net.ipv4.tcp_retries2 = 8
     ```

  #. Restart the system. 

  Your system now uses the new `tcp_retries2` setting.

**windows:**

On Windows, control TCP Retransmission by adjusting the 
`TcpMaxDataRetransmissions` parameter.

- To view the `TcpMaxDataRetransmissions` setting on Windows, issue the 
  following command:

  ```powershell
  reg query HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters /v TcpMaxDataRetransmissions
  ```

  By default, the parameter is not set. The system default,
  used if the value is absent, is `5` retries.

- To change the `TcpMaxDataRetransmissions` value, use the following command 
  in an Administrator Command Prompt, where `<value>` is an integer: 

  ```powershell
  reg add HKLM\SYSTEM\CurrentControlSet\Services\Tcpip\Parameters\ /t REG_DWORD /v TcpMaxDataRetransmission /d <value>
  ```

## Why does MongoDB log so many "Connection Accepted" events?

If you see a very large number of connection and re-connection messages
in your MongoDB log, then clients are frequently connecting and
disconnecting to the MongoDB server. This is normal behavior for
applications that do not use request pooling, such as CGI. Consider
using FastCGI, an Apache Module, or some other kind of persistent
application server to decrease the connection overhead.

If these connections do not impact your performance you can use the
run-time `quiet` option or the command-line option
`--quiet` to suppress these messages from the
log.

## What tools are available for monitoring MongoDB?

The [MongoDB Cloud Manager](https://www.mongodb.com/products/tools/cloud-manager) and
Ops Manager, an on-premises solution available in MongoDB
Enterprise Advanced include
monitoring functionality, which collects data from running MongoDB
deployments and provides visualization and alerts based on that data.

For more information, see also the `MongoDB Cloud Manager documentation` and
`Ops Manager documentation`.

A full list of third-party tools is available as part of the
/administration/monitoring/ documentation.

## Memory Diagnostics for the WiredTiger Storage Engine

### Must my working set size fit RAM?

No.

If the cache does not have enough space to load additional data,
WiredTiger evicts pages from the cache to free up space.

**Note:**

The `storage.wiredTiger.engineConfig.cacheSizeGB` limits the size of the WiredTiger internal
cache. The operating system uses the available free memory
for filesystem cache, which allows the compressed MongoDB data
files to stay in memory. In addition, the operating system 
uses any free RAM to buffer file system blocks and file system
cache.

To accommodate the additional consumers of RAM, you may have to
decrease WiredTiger internal cache size.

The default WiredTiger internal cache size value assumes that there is a
single `mongod` instance per machine. If a single machine
contains multiple MongoDB instances, then you should decrease the setting to
accommodate the other `mongod`
instances.

If you run `mongod` in a container (for example, `lxc`,
`cgroups`, Docker, etc.) that does *not* have access to all of the
RAM available in a system, you must set `storage.wiredTiger.engineConfig.cacheSizeGB` 
to a value less than the amount of RAM available in the container. The exact
amount depends on the other processes running in the container. See
`memLimitMB`.

To see statistics on the cache and eviction, use the
`serverStatus` command. The
`wiredTiger.cache` field holds the information on
the cache and eviction.

```none
...
"wiredTiger" : {
   ...
   "cache" : {
      "tracked dirty bytes in the cache" : <num>,
      "bytes currently in the cache" : <num>,
      "maximum bytes configured" : <num>,
      "bytes read into cache" :<num>,
      "bytes written from cache" : <num>,
      "pages evicted by application threads" : <num>,
      "checkpoint blocked page eviction" : <num>,
      "unmodified pages evicted" : <num>,
      "page split during eviction deepened the tree" : <num>,
      "modified pages evicted" : <num>,
      "pages selected for eviction unable to be evicted" : <num>,
      "pages evicted because they exceeded the in-memory maximum" : <num>,,
      "pages evicted because they had chains of deleted items" : <num>,
      "failed eviction of pages that exceeded the in-memory maximum" : <num>,
      "hazard pointer blocked page eviction" : <num>,
      "internal pages evicted" : <num>,
      "maximum page size at eviction" : <num>,
      "eviction server candidate queue empty when topping up" : <num>,
      "eviction server candidate queue not empty when topping up" : <num>,
      "eviction server evicting pages" : <num>,
      "eviction server populating queue, but not evicting pages" : <num>,
      "eviction server unable to reach eviction goal" : <num>,
      "pages split during eviction" : <num>,
      "pages walked for eviction" : <num>,
      "eviction worker thread evicting pages" : <num>,
      "in-memory page splits" : <num>,
      "percentage overhead" : <num>,
      "tracked dirty pages in the cache" : <num>,
      "pages currently held in the cache" : <num>,
      "pages read into cache" : <num>,
      "pages written from cache" : <num>,
   },
   ...
```

For an explanation of some key cache and eviction statistics, such
as `wiredTiger.cache.bytes currently in the
cache` and `wiredTiger.cache.tracked dirty bytes
in the cache`, see `wiredTiger.cache`.

To adjust the size of the WiredTiger internal cache, see
`storage.wiredTiger.engineConfig.cacheSizeGB` and
`--wiredTigerCacheSizeGB`. Avoid increasing the WiredTiger
internal cache size above its default value.

### How do I calculate how much RAM I need for my application?

With WiredTiger, MongoDB utilizes both the WiredTiger internal cache
and the filesystem cache.

#### Cache Configuration Settings

The default WiredTiger internal cache size is the larger of either:

- 50% of (RAM - 1GB), or

- 0.256 GB.

For example, on a system with a total of 4GB of RAM the
WiredTiger cache uses 1.5GB of RAM (``0.5 * (4GB - 1GB) =
1.5 GB``). When providing a specific cache size ensure the RAM does not 
exceed the bounds of 0.256GB to 10000GB. 

**Note:**

In some instances, such as when running in a container that is configured
to use less RAM than the amount of memory provisioned for the host, you
must account for the limits. You may need to configure the WiredTiger cache
to an appropriate value, as WiredTiger may not account for the memory 
limits of the specific container in certain cases. 

To view the `memory limit`, the value
that WiredTiger utilizes as the maximum amount of RAM available use the
`hostInfo` command. 

By default, WiredTiger uses Snappy block compression for all collections
and prefix compression for all indexes. Compression defaults are configurable
at a global level and can also be set on a per-collection and per-index
basis during collection and index creation.

Different representations are used for data in the WiredTiger internal cache
versus the on-disk format:

- Data in the filesystem cache is the same as the on-disk format, including
  benefits of any compression for data files. The filesystem cache is used
  by the operating system to reduce disk I/O.
- Indexes loaded in the WiredTiger internal cache have a different data
  representation to the on-disk format, but can still take advantage of
  index prefix compression to reduce RAM usage. Index prefix compression
  deduplicates common prefixes from indexed fields.
- Collection data in the WiredTiger internal cache is uncompressed
  and uses a different representation from the on-disk format. Block
  compression can provide significant on-disk storage savings, but
  data must be uncompressed to be manipulated by the server.

With the filesystem cache, MongoDB automatically uses all free memory
that is not used by the WiredTiger cache or by other processes.

To adjust the size of the WiredTiger internal cache, see
`storage.wiredTiger.engineConfig.cacheSizeGB` and
`--wiredTigerCacheSizeGB`. Avoid increasing the WiredTiger
internal cache size above its default value.

**Note:**

The `storage.wiredTiger.engineConfig.cacheSizeGB` limits the size of the WiredTiger internal
cache. The operating system uses the available free memory
for filesystem cache, which allows the compressed MongoDB data
files to stay in memory. In addition, the operating system 
uses any free RAM to buffer file system blocks and file system
cache.

To accommodate the additional consumers of RAM, you may have to
decrease WiredTiger internal cache size.

The default WiredTiger internal cache size value assumes that there is a
single `mongod` instance per machine. If a single machine
contains multiple MongoDB instances, then you should decrease the setting to
accommodate the other `mongod`
instances.

If you run `mongod` in a container (for example, `lxc`,
`cgroups`, Docker, etc.) that does *not* have access to all of the
RAM available in a system, you must set `storage.wiredTiger.engineConfig.cacheSizeGB` 
to a value less than the amount of RAM available in the container. The exact
amount depends on the other processes running in the container. See
`memLimitMB`.

To view statistics on the cache and eviction rate, see the
`wiredTiger.cache` field
returned from the `serverStatus` command.

## Sharded Cluster Diagnostics

The two most important factors in maintaining a successful sharded cluster are:

- choosing an appropriate shard key and

- sufficient capacity to support current and future operations.

While you can change your shard key later,
it is important to carefully consider your shard key choice to avoid
scalability and performance issues. Continue reading for specific issues
you may encounter in a production environment.

### In a new sharded cluster, why does all data remain on one shard?

Your cluster must have sufficient data for sharding to make
sense. Sharding works by migrating chunks between the shards until
each shard has roughly the same number of chunks.

The default chunk size is 128 megabytes. MongoDB will not begin
migrations until the imbalance of chunks in the cluster exceeds the
migration threshold. This
behavior helps prevent unnecessary chunk migrations, which can degrade
the performance of your cluster as a whole.

If you have just deployed a sharded cluster, make sure that you have
enough data to make sharding effective. If you do not have sufficient
data to create more than eight 128 megabyte chunks, then all data will
remain on one shard. Either lower the chunk size setting, or add more data to the cluster.

As a related problem, the system will split chunks only on
inserts or updates, which means that if you configure sharding and do not
continue to issue insert and update operations, the database will not
create any chunks. You can either wait until your application inserts
data *or* split chunks manually.

Finally, if your shard key has a low cardinality, MongoDB may not be able to create
sufficient splits among the data.

### Why would one shard receive a disproportionate amount of traffic in a sharded cluster?

In some situations, a single shard or a subset of the cluster will
receive a disproportionate portion of the traffic and workload. In
almost all cases this is the result of a shard key that does not
effectively allow write scaling.

It's also possible that you have "hot chunks." In this case, you may
be able to solve the problem by splitting and then migrating parts of
these chunks.

You may have to consider resharding your collection with a different shard key to correct this pattern.

### What can prevent a sharded cluster from balancing?

If you have just deployed your sharded cluster, you may want to
consider the troubleshooting suggestions for a new cluster where
data remains on a single shard.

If the cluster was initially balanced, but later developed an uneven
distribution of data, consider the following possible causes:

- You have deleted or removed a significant amount of data from the
  cluster. If you have added additional data, it may have a
  different distribution with regards to its shard key.

- Your shard key has low cardinality
  and MongoDB cannot split the chunks any further.

- Your data set is growing faster than the balancer can distribute
  data around the cluster. This is uncommon and
  typically is the result of:

  - a balancing window that
    is too short, given the rate of data growth.

  - an uneven distribution of write operations that requires more data
    migration. You may have to choose a different shard key to resolve
    this issue.

  - poor network connectivity between shards, which may lead to chunk
    migrations that take too long to complete. Investigate your
    network configuration and interconnections between shards.

### Why do chunk migrations affect sharded cluster performance?

If migrations impact your cluster or application's performance,
consider the following options, depending on the nature of the impact:

#. If migrations only interrupt your clusters sporadically, you can
   limit the balancing window to prevent balancing activity
   during peak hours. Ensure that there is enough time remaining to
   keep the data from becoming out of balance again.

#. If the balancer is always migrating chunks to the detriment of
   overall cluster performance:

   - You may want to attempt decreasing the chunk size
     to limit the size of the migration.

   - Your cluster may be over capacity, and you may want to attempt to
     add one or two shards to
     the cluster to distribute load.

It's also possible that your shard key causes your
application to direct all writes to a single shard. This kind of
activity pattern can require the balancer to migrate most data soon after writing
it. You may have to consider resharding your collection with a different shard key that provides better write
scaling.
