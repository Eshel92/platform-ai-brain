<!-- Converted from administration/connection-pool-overview.txt (reStructuredText). Includes are inlined. -->

# Connection Pool Overview

This document describes how to use a connection pool to manage 
connections between applications and MongoDB instances. 

## What is a Connection Pool?

### Definition

A connection pool is a cache of open, ready-to-use database connections
maintained by the `driver`. Your application can get
connections from the pool, perform operations, and return connections
to the pool. Connection pools are thread-safe.

### Benefits of a Connection Pool

A connection pool reduces application latency and the number of new
connections created. The pool creates connections at startup, and
connections return to the pool automatically — applications do not
need to return them manually. Some connections are active and some
are available. If your application requests a connection and one is
available in the pool, a new connection does not need to be created.

## Create and Use a Connection Pool

### Use an Instance of Your Driver's `MongoClient` Object

Most `drivers` provide an object of type `MongoClient`.

Use one `MongoClient` instance per application unless the
application is connecting to many separate clusters. Each 
`MongoClient` instance manages its own connection pool to the 
MongoDB cluster or node specified when the `MongoClient` is created.
`MongoClient` objects are thread-safe in most drivers.

**Note:**

Store your `MongoClient` instance in a place that is globally
available to your application.

### Authentication

To use a connection pool with LDAP, see
LDAP Connection Pool Behavior.

## Sharded Cluster Connection Pooling

`mongos` routers have connection pools for each node in the 
cluster. The availability of connections to individual nodes within a 
sharded cluster affects latency. Operations must wait for a connection
to be established.

## Connection Pool Configuration Settings

You can specify connection pool settings in these locations:

- The MongoDB URI

- Your application's `MongoClient` instance

- Your application framework's configuration files

### Settings

| Setting | Description |
|---|---|
| `connectTimeoutMS` | Most drivers default to never time out. Some versions of the Java drivers (for example, version 3.7) default to `10`. *Default:* `0` for most drivers. See your `driver` documentation. |
| `maxConnecting` | Maximum number of connections a pool may be establishing concurrently. `maxConnecting` is supported for all drivers **except** the `Rust Driver`. Raising the value of `maxConnecting` allows the client to establish connection to the server faster, but increases the chance of connection storms. If the value of `maxConnecting` is too low, your connection pool may experience heavy throttling and increased tail latency for clients checking out connections. *Default:* `2` |
| `maxIdleTimeMS` | The maximum number of milliseconds that a connection can remain idle in the pool before being removed and closed. *Default:* See your `driver` documentation. |
| `maxPoolSize` | .. _maxpoolsize-cp-setting: Maximum number of connections opened in the pool. When the connection pool reaches the maximum number of connections, new connections wait up to the value of `waitQueueTimeoutMS`. *Default:* `100` |
| `minPoolSize` | .. _minpoolsize-cp-setting: Minimum number of connections opened in the pool. The value of `minPoolSize` must be less than the value of `maxPoolSize`. *Default*: `0` |
| `socketTimeoutMS` | Number of milliseconds to wait before timeout on a TCP connection. Do *not* use `socketTimeoutMS` as a mechanism for preventing long-running server operations. Setting low socket timeouts may result in operations that error before the server responds. *Default*: `0`, which means no timeout. |
| `waitQueueTimeoutMS` | Maximum wait time in milliseconds that a thread can wait for a connection to become available. A value of `0` means there is no limit. *Default*: `0` |
