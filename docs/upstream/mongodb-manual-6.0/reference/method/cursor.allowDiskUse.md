<!-- Converted from reference/method/cursor.allowDiskUse.txt (reStructuredText). Includes are inlined. -->

# cursor.allowDiskUse()

## Definition

**`cursor.allowDiskUse()`**

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for a language-specific driver, such as Node.js.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

Use `allowDiskUse()` to either allow or prohibit 
writing temporary files on disk when a pipeline stage exceeds 
the 100 megabyte limit. Starting in MongoDB 6.0, operations that 
require greater than 100 megabytes of memory automatically write 
data to temporary files by default.

`allowDiskUse()` has the following form:

```javascript
db.collection.find(<match>).sort(<sort>).allowDiskUse()
```

See sort-index-use for more information on in-memory sort
operations.

## Compatibility

This method is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Note:**

This command is supported in all MongoDB Atlas clusters.
For information on Atlas support for all commands, see 
Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Behavior

### Interaction with `allowDiskUseByDefault`

Starting in MongoDB 6.0, pipeline stages that require more than 100 
megabytes of memory to execute write temporary files to disk by 
default. 

**Note:**

Prior to MongoDB 6.0, `.allowDiskUse(false)` and                      
`.allowDiskUse(true)` have the same effect. In MongoDB 6.0, both   
`mongosh` and the legacy `mongo` shell behave the following way: 

If `allowDiskUseByDefault` is `true` (this is the default):

- `.allowDiskUse()` has no additional effect 
- `.allowDiskUse(true)` has no additional effect
- `.allowDiskUse(false)` prohibits the query from writing temporary
  files to disk

If `allowDiskUseByDefault` is `false`:

- `.allowDiskUse()` enables writing temporary files to disk
- `.allowDiskUse(true)` enables writing temporary files to disk
- `.allowDiskUse(false)` has no additional effect

### Supports Large Non-Indexed Sorts Only

`cursor.allowDiskUse()` has no effect on sort operations
answered using an index *or* non-indexed ("in-memory") sort operations
which require less than 100 megabytes of memory. For more complete
documentation on in-memory sorts and sort index use, see
sort-index-use.

To check if MongoDB must perform an in-memory sort, append
`cursor.explain()` to the query and check the 
explain results. If the query plan 
contains a `SORT` stage, then MongoDB must perform an 
in-memory sort operation subject to the 100 megabyte memory limit.

## Example

Consider a collection `sensors` with only the default index on 
`_id`. The collection contains documents similar to the
following:

```json
{
  "sensor-name" : "TEMP-21425",
  "sensor-location" : "Unit 12",
  "reading" : {
    "timestamp" : Timestamp(1580247215, 1),
    "value" : 212,
    "unit" : "Fahrenheit"
  }
}
```

The following operation includes a `cursor.sort()` on the
field `reading.timestamp`. The operation also passes `false` to
`cursor.allowDiskUse()` to prohibit the query from writing temporary
files to disk.

```javascript
db.sensors.find({"sensor-location" : "Unit 12"}).
  sort({"reading.timestamp" : 1}).
  allowDiskUse(false)
```

Since `reading.timestamp` is not included in an index, MongoDB
must perform an in-memory sort operation to return results in the 
requested sort order. By specifying `cursor.allowDiskUse(false)`,
MongoDB cannot process the sort operation if it requires more than
100 megabytes of system memory. If the operation requires more than 100 megabytes of
system memory, MongoDB would return an error.
