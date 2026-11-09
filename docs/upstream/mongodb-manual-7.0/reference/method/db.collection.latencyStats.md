<!-- Converted from reference/method/db.collection.latencyStats.txt (reStructuredText). Includes are inlined. -->

# db.collection.latencyStats() (mongosh method)

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `latencyStats` field returned by the.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Definition

**`db.collection.latencyStats(options)`**

   `collStats` command

`db.collection.latencyStats()` returns latency
statistics for a given collection. It is a wrapper around
`$collStats`.

This method has the form:

```javascript
db.collection.latencyStats( { histograms: <boolean> } )
```

The `histograms` argument is an optional boolean. If
`histograms: true` then `latencyStats()` adds
latency histograms to the return document.

**See also:**

`$collStats`

## Compatibility

This method is available in deployments hosted in the following environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Output

`latencyStats()` returns a document containing
a field `latencyStats`, containing the following fields:

| Field Name | Description |
|---|---|
| `reads` | Latency statistics for read requests. |
| `writes` | Latency statistics for write requests. |
| `commands` | Latency statistics for database commands. |
| `transactions` | Latency statistics for database transactions. |

Each of these fields contains an embedded document bearing the
following fields:

* - Field Name
  - Description

* - `latency`
  - A 64-bit integer giving the total combined
    latency in microseconds.

* - `ops`
  - A 64-bit integer giving the total number of
    operations performed on the collection since startup.

* - `histogram`
  - An array of embedded documents, each representing a latency range.
    Each document covers twice the previous document's range. For
    lower values between 2048 microseconds and roughly 1 second,
    the histogram includes half-steps.

    This field only exists given the
    `latencyStats: { histograms: true }` option. Empty ranges with
    a zero `count` are omitted from the output.

    Each document bears the following fields:

    |  |  |
    |---|---|
    | Field Name | Description |
    | `micros` | A 64-bit integer giving the inclusive lower time bound of the current latency range in microseconds. The document's range spans between the previous document's `micros` value, exclusive, and this document's `micros` value, inclusive. |
    | `count` | A 64-bit integer giving the number of operations with latency less than or equal to `micros`. |

    For example, if `collStats` returns the following histogram:

    ```javascript
    histogram: [
      { micros: Long(0), count: Long(10) },
      { micros: Long(2), count: Long(1) },
      { micros: Long(4096), count: Long(1) },
      { micros: Long(16384), count: Long(1000) },
      { micros: Long(49152), count: Long(100) }
    ]
    ```

    This indicates that there were [#inclusive_symbols]_:

    - 10 operations taking 2 microsecond or less
    - 1 operation in the range [2, 4) microseconds
    - 1 operation in the range [4096, 6144) microseconds
    - 1000 operations in the range [16384, 24576) microseconds
    - 100 operations in the range [49152, 65536) microseconds

## Examples

You can run `latencyStats()` in
`mongosh` as follows:

```javascript
db.data.latencyStats( { histograms: true } ).pretty()
```

`latencyStats()` returns a document such as
the following:

```javascript
{
  "ns" : "test.data",
  "localTime" : ISODate("2016-11-01T21:56:28.962Z"),
  "latencyStats" : {
    "reads" : {
      "histogram" : [
        {
          "micros" : Long(16),
          "count" : Long(6)
        },
        {
          "micros" : Long(512),
          "count" : Long(1)
        }
      ],
      "latency" : Long(747),
      "ops" : Long(7)
    },
    "writes" : {
      "histogram" : [
        {
          "micros" : Long(64),
          "count" : Long(1)
        },
        {
          "micros" : Long(24576),
          "count" : Long(1)
        }
      ],
      "latency" : Long(26845),
      "ops" : Long(2)
    },
    "commands" : {
      "histogram" : [ ],
      "latency" : Long(0),
      "ops" : Long(0)
    }
  }
}
```
