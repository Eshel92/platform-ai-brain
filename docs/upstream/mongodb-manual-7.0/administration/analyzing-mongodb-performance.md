<!-- Converted from administration/analyzing-mongodb-performance.txt (reStructuredText). Includes are inlined. -->

# MongoDB Performance

As you develop and operate applications with MongoDB, you may need to
analyze the performance of the application and its database.
When you encounter degraded performance, it is often a function of database
access strategies, hardware availability, and the number of open database
connections.

You may experience performance limitations from inadequate or inappropriate
indexing strategies or poor schema design patterns.
analyzing-performance-locks discusses how these can impact
MongoDB's internal locking.

Performance issues may indicate that the database is operating at
capacity and that it is time to add additional capacity to the
database. In particular, the application's working set should fit in
the available physical memory.

In some cases performance issues may be temporary and related to
abnormal traffic load. As discussed in number-of-connections, scaling
can help reduce excessive traffic.

Database profiling can help you understand what operations are
causing degradation.

## Locking Performance

MongoDB uses a locking system to ensure data set consistency. If
certain operations are long-running or a queue forms, performance
degrades as requests and operations wait for the lock.

Lock-related slowdowns can be intermittent. To see if the lock has been
affecting your performance, see the server-status-locks
section and the globalLock section of the
`serverStatus` output.

**Note:**

Some `serverStatus` response fields are not returned on 
MongoDB Atlas Free clusters or Flex clusters. For more information, 
see free-shard-commands-with-limits in the MongoDB Atlas 
documentation.

Dividing `locks.<type>.timeAcquiringMicros` by
`locks.<type>.acquireWaitCount`
can give an approximate average wait time for a particular lock mode.

`locks.<type>.deadlockCount` provides
the number of times the lock acquisitions encountered deadlocks.

If `globalLock.currentQueue.total` is consistently high,
many requests may be waiting for a lock. This indicates a possible
concurrency issue that may be affecting performance.

If `globalLock.totalTime` is
high relative to `uptime`, the database has been
in a locked state for a significant period.

Long queries can result from:

- Ineffective use of indexes
- Non-optimal schema design
- Poor query structure
- System architecture issues
- Insufficient RAM resulting in disk reads

## Number of Connections

In some cases, the number of connections between the applications and the
database can overwhelm the server's ability to handle requests. The
following fields in the `serverStatus` document provide insight:

- `connections` is a container for the following
  two fields:

  - `connections.current` the total number of
    current clients connected to the database instance.

  - `connections.available` the total number of
    unused connections available for new clients.

Many concurrent application requests may overwhelm the server's ability
to keep up with demand. If this is the case,
increase the capacity of your deployment.

For write-heavy applications, deploy sharding and add one or more
shards to a sharded cluster to distribute load among
`mongod` instances.

Spikes in the number of connections can also result from
application or driver errors. All officially supported MongoDB
drivers implement connection pooling, which allows clients to use and
reuse connections more efficiently. An extremely high number of
connections, particularly without corresponding workload, often
indicates a driver or other configuration error.

### Self-Managed Connection Limits

Unless constrained by system-wide limits, the maximum number of
incoming connections supported by MongoDB is configured with the
`maxIncomingConnections` setting. On Unix-based systems,
system-wide limits can be modified using the `ulimit` command, or by
editing your system's `/etc/sysctl` file. See ulimit
for more information.

### MongoDB Atlas Connection Limits

MongoDB Atlas sets the limit for concurrent incoming connections based on 
the cluster tier and class. To learn more, see connection-limits
in the Atlas documentation.
