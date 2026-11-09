<!-- Converted from administration/connection-pool-overview.txt (reStructuredText). Includes are inlined. -->

# Connection Pool Overview

This document describes how to use a connection pool to manage 
connections between applications and MongoDB instances. 

## What is a Connection Pool?

### Definition

A connection pool is a cache of open,
ready-to-use database connections maintained by the `driver`. 
Your application can seamlessly get connections from the pool, perform 
operations, and return connections back to the pool. Connection pools 
are thread-safe. 

### Benefits of a Connection Pool

A connection pool helps reduce application latency and the number of 
times new connections are created.

A connection pool creates connections at startup. Applications do not 
need to manually return connections to the pool. Instead, connections 
return to the pool automatically.

Some connections are active and some are inactive but available. 
If your application requests a connection and there’s an available 
connection in the pool, a new connection does not need to be created.

## Create and Use a Connection Pool

### Use an Instance of your Driver's `MongoClient` Object

Most `drivers` provide an object of type `MongoClient`.

Use one `MongoClient` instance per application unless the
application is connecting to many separate clusters. Each 
`MongoClient` instance manages its own connection pool to the 
MongoDB cluster or node specified when the `MongoClient` is created.
`MongoClient` objects are thread-safe in most drivers.

**Note:**

Store your `MongoClient` instance in a place that is globally
accessible by your application. 

### Authentication

To use a connection pool with LDAP, see
LDAP Connection Pool Behavior.

## Sharded Cluster Connection Pooling

`mongos` routers have connection pools for each node in the 
cluster. The availability of connections to individual nodes within a 
sharded cluster affects latency. Operations must wait for a connection
to be established.

## Connection Pool Configuration Settings

To configure the connection pool, set the options:

- through the MongoDB URI, 

- programmatically when building the `MongoClient` instance, or

- in your application framework's configuration files.

### Settings

* - Setting
  - Description

* - `maxPoolSize`

  - .. _maxpoolsize-cp-setting:

    Maximum number of connections opened in the pool. When the 
    connection pool reaches the maximum number of connections, new 
    connections wait up until to the value of 
    `waitQueueTimeoutMS`.

    *Default:* `100` 

* - `minPoolSize`

  - .. _minpoolsize-cp-setting:

    Minimum number of connections opened in the pool. 
    The value of `minPoolSize` must be less than 
    the value of `maxPoolSize`.

    *Default*: `0`

* - `connectTimeoutMS`

  - Most drivers default to never time out. Some versions of the 
    Java drivers (for example, version 3.7) default to `10`. 

    *Default:* `0` for most drivers. See your `driver` 
    documentation.

* - `socketTimeoutMS`

  - Number of milliseconds to wait before timeout on a TCP 
    connection.

    Do *not* use `socketTimeoutMS` as a mechanism for 
    preventing long-running server operations.

    Setting low socket timeouts may result in operations that error 
    before the server responds.

    *Default*: `0`, which means no timeout. See your 
    `driver` documentation.

* - `maxIdleTimeMS`

  - The maximum number of milliseconds that a connection can 
    remain idle in the pool before being removed and closed.

    *Default:* See your `driver` documentation.

* - `waitQueueTimeoutMS`

  - Maximum wait time in milliseconds that a thread can wait for 
    a connection to become available. A value of `0` means there
    is no limit. 

    *Default*: `0`. See your `driver` documentation.

* - `ShardingTaskExecutorPoolMinSize` 

  - Minimum number of outbound connections each TaskExecutor 
    connection pool can open to any given `mongod` 
    instance.

    *Default*: `1`. See 
    `ShardingTaskExecutorPoolMinSize`.  

    Parameter only applies to sharded deployments.

* - `ShardingTaskExecutorPoolMinSizeForConfigServers`

  - .. include:: /includes/ShardingTaskExecutorPoolMinSizeForConfigServers-parameter.rst

    *Default*: `-1`

    **New in version:** 6.0

* - `ShardingTaskExecutorPoolMaxSize` 

  - Maximum number of outbound connections each TaskExecutor 
    connection pool can open to any given `mongod` 
    instance.  

    *Default*: 2`64` - 1. See 
    `ShardingTaskExecutorPoolMaxSize`.

    Parameter only applies to sharded deployments.

* - `ShardingTaskExecutorPoolMaxSizeForConfigServers`

  - .. include:: /includes/ShardingTaskExecutorPoolMaxSizeForConfigServers-parameter.rst

    *Default*: `-1`

    **New in version:** 6.0
