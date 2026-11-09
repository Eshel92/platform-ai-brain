<!-- Converted from reference/local-database.txt (reStructuredText). Includes are inlined. -->

# The `local` Database

## Overview

Every `mongod` instance has its own `local` database, which
stores data used in the replication process and other instance-specific
data. Collections in the `local` database are not replicated.

## Collections on all `mongod` Instances

**`local.startup_log`**

On startup, each `mongod` instance inserts a document into
`startup_log` with diagnostic information about the
`mongod` instance itself and host
information. `startup_log` is a capped
collection. This information is primarily useful for diagnostic
purposes.

For example, the following is a prototype of a document from the
`startup_log` collection:

```javascript
{
  "_id" : "<string>",
  "hostname" : "<string>",
  "startTime" : ISODate("<date>"),
  "startTimeLocal" : "<string>",
  "cmdLine" : {
        "dbpath" : "<path>",
        "<option>" : <value>
  },
  "pid" : <number>,
  "buildinfo" : {
        "version" : "<string>",
        "gitVersion" : "<string>",
        "sysInfo" : "<string>",
        "loaderFlags" : "<string>",
        "compilerFlags" : "<string>",
        "allocator" : "<string>",
        "versionArray" : [ <num>, <num>, <...> ],
        "javascriptEngine" : "<string>",
        "bits" : <number>,
        "debug" : <boolean>,
        "maxBsonObjectSize" : <number>
  }
}
```

Documents in the `startup_log` collection contain the
following fields:

**`local.startup_log._id`**

Includes the system hostname and a millisecond epoch value.

**`local.startup_log.hostname`**

The system's hostname.

**`local.startup_log.startTime`**

A UTC ISODate value that reflects when the server started.

**`local.startup_log.startTimeLocal`**

A string that reports the `startTime`
in the system's local time zone.

**`local.startup_log.cmdLine`**

An embedded document that reports the `mongod` runtime
options and their values.

**`local.startup_log.pid`**

The process identifier for this process.

**`local.startup_log.buildinfo`**

An embedded document that reports information about the build
environment and settings used to compile this
`mongod`. This is the same output as
`buildInfo`. See `buildInfo`.

## Collections on Replica Set Members

**`local.system.replset`**

`local.system.replset` holds the replica set's configuration
object as its single document. To view the object's configuration
information, issue `rs.conf()` from `mongosh`.
You can also query this collection directly.

**`local.oplog.rs`**

`local.oplog.rs` is the capped collection that holds the
oplog. You set its size at creation using the
`oplogSizeMB` setting. To resize the oplog
after replica set initiation, use the
/tutorial/change-oplog-size procedure. For additional
information, see the replica-set-oplog-sizing section.

The oplog can grow past its configured size
limit to avoid deleting the `majority commit point`.

Starting in MongoDB 5.0, manual write operations to the oplog are
restricted. For details, see oplog-coll-behavior.

**`local.replset.minvalid`**

This contains an object used internally by replica sets to track replication
status.

## Restrictions

Multi-Document Transactions on `local`
  You cannot perform read/write operations to the collections in the
  `local` database inside a 
  multi-document transaction.

Retryable Writes against `local`
  You cannot perform write operations to collections in the `local`
  database with retryable writes enabled.

  **Important:**

  The official MongoDB drivers enable retryable writes by
  default. Applications that write to the `local` database
  encounter write errors *unless* retryable writes are explicitly 
  disabled.

  To disable retryable writes, specify
  `retryWrites=false` in the 
  connection string for the MongoDB cluster.
