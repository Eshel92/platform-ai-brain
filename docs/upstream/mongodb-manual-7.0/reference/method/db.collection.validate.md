<!-- Converted from reference/method/db.collection.validate.txt (reStructuredText). Includes are inlined. -->

# db.collection.validate() (mongosh method)

(Include not available offline: includes/wayfinding/mongosh-method-validate.rst)

## Description

**Changed in version:** 6.2

**`db.collection.validate(<documents>)`**

Validates a collection. The method scans a collection data and
indexes for correctness and returns the result. For details of the
output, see validate-output.

Starting in version 5.0, the `db.collection.validate()`
method can also fix inconsistencies in the collection.

Index inconsistencies include:

- An index is multikey but there are
  no multikey fields.
- An index has multikeyPaths covering 
  fields that are not multikey.
- An index does not have 
  multikeyPaths but
  there are multikey documents (for indexes built before 3.4).

If any inconsistencies are detected by the 
`db.collection.validate()` command, a warning is returned 
and the repair flag on the index is set to `true`.

`db.collection.validate()` also validates any documents that
violate the collection's 
schema validation rules.

The `db.collection.validate()` method is a wrapper around
the `validate` command.

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

## Syntax

The `db.collection.validate()` method has the following syntax:

```javascript
db.collection.validate( { 
   full: <boolean>,  // Optional
   repair: <boolean>,  // Optional, added in MongoDB 5.0
   checkBSONConformance: <boolean>  // Optional, added in MongoDB 6.2
} )
```

### Parameters

The `db.collection.validate()` method can take the
following optional document parameter with the fields:

* - Field
  - Type
  - Description

* - full
  - boolean

  - .. _method-validate-full:

    *Optional*. A flag that determines whether the command performs
    a slower but more thorough check or a faster but less thorough
    check.

    - If `true`, performs a more thorough check with the following
      exception:

      - Full validation on the `oplog` for WiredTiger skips the more 
        thorough check.

    - If `false`, omits some checks for a faster but less
      thorough check.

    The default is `false`.

    For the WiredTiger storage engine, only the `full` validation process will 
    force a checkpoint and flush all in-memory data to disk before verifying the 
    on-disk data.

* - repair
  - boolean

  - .. _method-validate-repair:

    *Optional*. A flag that determines whether the command performs a
    repair.

    - If `true`, a repair is performed.

    - If `false`, no repair is performed.

    The default is `false`.

    A repair can only be run on a standalone node.

    The repair fixes these issues:

    - If missing index entries are found, the missing keys are inserted into
      the index.

    - If extra index entries are found, the extra keys are removed from the
      index.

    - If multikey documents are found for an
      index that is not a multikey index, the index is changed to a multikey
      index.

    - If multikey documents are found that are
      not specified by an index's multikey paths, the index's multikey paths
      are updated.

    - If corrupt documents with invalid BSON data are found, the documents
      are removed.

    For more information, see the `--repair` option
    for `mongod`

    **New in version:** 5.0

* - checkBSONConformance
  - boolean
  - .. _method-validate-checkBSONConformance:

    *Optional*. If `true`, the collection is checked to ensure the
    BSON documents conform to the BSON
    specifications. The checks increase the time to complete the validation
    operation. Any issues are returned as a warning.

    `checkBSONConformance`:

    - Default is `false`.
    - Is enabled when `full` is set to `true`.
    - Cannot be used with:

      - `repair` set to `true`.
      - `metadata` set to `true`.

    **New in version:** 6.2

## Behavior

### Performance

The `db.collection.validate()` method is potentially resource
intensive and may impact the performance of your MongoDB instance,
particularly on larger data sets.

The `db.collection.validate()` method obtains an exclusive lock
on the collection. This will block all reads and writes on the
collection until the operation finishes. When run on a secondary, the
operation can block all other operations on that secondary until it
finishes.

**Warning:**

Validation has exclusive lock requirements that affect performance
on primaries and on secondaries that are servicing reads. Consider
only running `db.collection.validate()` on nodes that are
not servicing reads or writes.

To minimize impact on the primary, the majority of the data-bearing
(non-arbiter), voting members in the cluster must be available and
must not have significant replication lag.

To minimize the impact of the validation operation on client
applications, run `db.collection.validate()` on a secondary
node that is not servicing read requests. You can convert the
current primary node to a secondary node, by running the
`rs.stepDown()` method.

To completely isolate the `db.collection.validate()`
operation from client traffic, choose one of the following options:

- Isolate a replica set member by following the rolling
  maintenance procedure to
  temporarily remove it from the cluster.
- Convert a secondary node to a replica set
  hidden member and perform the
  validation on the hidden node.

### Data Throughput Metrics

The `$currentOp` and the `currentOp` command
include `dataThroughputAverage` and
`dataThroughputLastSecond` information for
validate operations in progress.

The log messages for validate operations include
`dataThroughputAverage` and `dataThroughputLastSecond`
information.

### Collection Validation Improvements

Starting in MongoDB 6.2, the `validate` command and
`db.collection.validate()` method:

- Check collections to ensure the
  BSON documents conform to the BSON
  specifications.
- Check time series collections
  for internal data inconsistencies.
- Have a new option `checkBSONConformance` that enables comprehensive
  BSON checks.

## Examples

- To validate a collection `myCollection` using the default validation
  setting (specifically, full: false):

  ```javascript
  db.myCollection.validate()

  db.myCollection.validate({ })

  db.myCollection.validate( { full: false } )
  ```

- To perform a full validation of collection `myCollection`, specify
  full: true:

  ```javascript
  db.myCollection.validate( { full: true } )
  ```

- To repair collection `myCollection`, specify
  repair: true:

  ```javascript
  db.myCollection.validate( { repair: true } )
  ```

- To perform additional BSON conformance checks in `myCollection`,
  specify checkBSONConformance: true:

  ```javascript
  db.myCollection.validate( { checkBSONConformance: true } )
  ```

For details of the output, see validate-output.
