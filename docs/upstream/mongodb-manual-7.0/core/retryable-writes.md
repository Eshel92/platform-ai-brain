<!-- Converted from core/retryable-writes.txt (reStructuredText). Includes are inlined. -->

# Retryable Writes

Retryable writes let drivers retry specific write operations once after
network errors or if they cannot find a healthy primary in the
replica set or sharded cluster.

## Compatibility

Retryable writes require:

Deployment Topologies
  A replica set or sharded cluster. Not supported on standalone
  instances.

Storage Engine
  A storage engine with document-level locking, such as
  WiredTiger or in-memory.

MongoDB Drivers
  Drivers compatible with MongoDB 3.6+.

  |  |  |  |
  |---|---|---|
  | Java 3.6+ Python 3.6+ C 1.9+ Go 1.8+ | C# 2.5+ Node 3.0+ Ruby 2.5+ Rust 2.1+ Swift 1.2+ | Perl 2.0+ PHPC 1.4+ Scala 2.2+ C++ 3.6.6+ |

MongoDB Version
  MongoDB 3.6+ and `featureCompatibilityVersion` 3.6+ on all nodes.
  See `setFeatureCompatibilityVersion`.

Write Acknowledgment
  Writes with /reference/write-concern `0` are not retryable.

## Behaviors

### Retryable Writes and Multi-Document Transactions

Transaction commit and abort operations are
retryable. Drivers retry these operations once on error, even if
`retryWrites` is `false`.

Writes inside a transaction are not individually retryable, regardless
of value of `retryWrites`.

For more information on transactions, see /core/transactions.

### Enabling Retryable Writes

MongoDB Drivers

  Drivers compatible with MongoDB 4.2 and higher enable
  retryable-writes by default. Earlier drivers require the
  `retryWrites=true` option. The
  `retryWrites=true` option can be omitted in
  applications that use drivers compatible with MongoDB 4.2 and
  higher.

  |

  To disable retryable writes, applications that use drivers
  compatible with MongoDB 4.2 and higher must include 
  `retryWrites=false` in the connection
  string.

`mongosh`
  `mongosh` enables retryable writes by default. To
  disable, use `--retryWrites=false`:

  ```bash
  mongosh --retryWrites=false
  ```

### Retryable Write Operations

MongoDB retries these operations if they have acknowledged write
concern:

**Note:**

Writes inside transactions are not
individually retryable.

* - Methods
  - Descriptions

* - | `db.collection.insertOne()`
    | `db.collection.insertMany()`
  - Inserts

* - | `db.collection.updateOne()`
    | `db.collection.replaceOne()`
  - Single-document updates

* - | `db.collection.deleteOne()`
    | `db.collection.remove()` where `justOne` is `true`
  - Single-document deletes

* - | `db.collection.findAndModify()`
    | `db.collection.findOneAndDelete()`
    | `db.collection.findOneAndReplace()`
    | `db.collection.findOneAndUpdate()`
  - `findAndModify` operations (always single-document).

* - `db.collection.bulkWrite()` with the following write
    operations:

    - bulkwrite-write-operations-insertOne
    - updateOne
    - bulkwrite-write-operations-replaceOne
    - deleteOne

  - Bulk write operations that only consist of the single-document
    write operations. A retryable bulk operation can include any
    combination of the specified write operations but cannot include
    any multi-document write operations, such as `updateMany`.

* - `Bulk` operations for:

    - `Bulk.find.removeOne()`
    - `Bulk.find.replaceOne()`
    - `Bulk.find.updateOne()`

  - Bulk write operations that only consist of the single-document
    write operations. A retryable bulk operation can include any
    combination of the specified write operations but cannot include
    any multi-document write operations, such as `update` which
    specifies `true` for the `multi` option.

### Persistent Network Errors

By default, MongoDB retries writes **once**. One retry attempts to address
transient network errors and
replica set elections, but not
persistent network errors.

If you set `timeoutMS`, MongoDB may retry writes multiple times. Retries
continue until one of the following conditions is true:

- The operation succeeds.
- The operation fails with a non-retryable error.
- The timeout expires.

### Failover Period

Drivers wait `serverSelectionTimeoutMS` to find a new
primary before retrying. Retryable writes fail if failover takes longer
than this timeout.

**Warning:**

If a client is unresponsive for longer than
`localLogicalSessionTimeoutMinutes`, the write might
retry and apply again when the client recovers.

### Diagnostics

`serverStatus` includes retryable write statistics in the
`transactions` section.

### Retryable Writes Against `local` Database

Official drivers enable retryable writes by default. Writes to the
`local` database fail unless you
disable retryable writes.

To disable, set `retryWrites=false` in the
connection string.

### Error Handling

Starting in MongoDB 6.1, if both the first and second attempt of a
retryable write fail without a single write being performed, MongoDB
returns an error with the `NoWritesPerformed` label.

The `NoWritesPerformed` label differentiates the results of batch
operations like `insertMany()`. In an
`insertMany` operation, one of the following outcomes can occur:

| Outcome | MongoDB Output |
|---|---|
| No documents are inserted. | Error returned with `NoWritesPerformed` label. |
| Partial work done. (At least one document is inserted, but not all.) | Error returned without `NoWritesPerformed` label. |
| All documents are inserted. | Success returned. |

Applications can use the `NoWritesPerformed` label to definitively
determine that no documents were inserted. This error reporting lets the
application maintain an accurate state of the database when handling
retryable writes.

In previous versions of MongoDB, an error is returned when both the
first and second attempts of a retryable write fail. However, there is
no distinction made to indicate that no writes were performed.

## Learn More

retryable-reads
