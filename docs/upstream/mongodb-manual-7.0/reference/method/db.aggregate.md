<!-- Converted from reference/method/db.aggregate.txt (reStructuredText). Includes are inlined. -->

# db.aggregate() (mongosh method)

## Definition

**`db.aggregate()`**

Runs a specified admin/diagnostic pipeline which does not require an 
underlying collection. For aggregations on collection data, see
`db.collection.aggregate()`.

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `aggregate` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

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

The `db.aggregate()` method has the following syntax:

```javascript
db.aggregate( [ <pipeline> ], { <options> } )
```

**Note:**

`db.aggregate()` can accept the pipeline stages as separate
arguments instead of as elements in an array. If you do
not specify the `pipeline` as an array, you cannot specify the
`options` parameter.

The `pipeline` parameter is an array of stages to execute. 
The pipeline must start with a compatible stage that does 
not require an underlying collection, such as `$currentOp` 
or `$listLocalSessions`.

The `options` document can contain the following fields:

* - Field
  - Type
  - Description

* - `explain`
  - boolean
  - Optional. Specifies whether the method returns
    information on the pipeline processing. 

    See example-aggregate-method-explain-option for an example.

    IMPORTANT: This option is not available in multi-document transactions.

* - `allowDiskUse`
  - boolean
  - Optional. Enables writing to temporary files. When set to `true`, aggregation
    operations write data to the `_tmp` subdirectory in the
    `dbPath` directory. See
    example-aggregate-method-external-sort for an example.

    The profiler log messages and diagnostic log
    messages includes a `usedDisk`
    indicator if any aggregation stage wrote data to temporary files due
    to memory restrictions.

* - `cursor`
  - document
  - Optional. Specifies the *initial* batch size for the cursor. The value of the `cursor`
    field is a document with the field `batchSize`. See
    example-aggregate-method-initial-batch-size for syntax and an example.

* - `maxTimeMS`
  - non-negative integer
  - Optional. Specifies a time limit in milliseconds for processing
    operations on a cursor. If you do not specify a value for maxTimeMS,
    operations do not time out. A value of `0` explicitly
    specifies the default unbounded behavior.

    MongoDB terminates operations that exceed their allotted time limit
    using the same mechanism as `db.killOp()`. MongoDB only
    terminates an operation at one of its designated interrupt 
    points.

* - `bypassDocumentValidation`
  - boolean
  - Optional. Applicable only if you specify the `$out` or `$merge` aggregation
    stages.

    Enables `db.collection.aggregate` to bypass schema validation
    during the operation. This lets you insert documents that do not
    meet the validation requirements.

* - `readConcern`
  - document
  - Optional. Specifies the read concern.

    The `readConcern` option has the following syntax: 
    `readConcern: { level: <value> }`

    Possible read concern levels are:

    - `"local"`. This is the default read concern level for
      read operations against the primary and secondaries.

    - `"available"`. Available for read operations against
      the primary and secondaries. `"available"` behaves the 
      same as `"local"` against the primary and non-sharded
      secondaries. The query returns the instance's most recent data.

    - `"majority"`. Available for replica sets that use
      WiredTiger storage engine.

    - `"linearizable"`. Available for read operations on the
      `primary` only.

    - `"snapshot"`. Available for multi-document
      transactions and certain read operations outside of 
      multi-document transactions.

    For more formation on the read concern levels, see
    read-concern-levels.

    The `$out` stage cannot be used in conjunction with read concern 
    `"linearizable"`. If you specify `"linearizable"` 
    read concern for `db.collection.aggregate()`, you cannot include the
    `$out` stage in the pipeline.

    The `$merge` stage cannot be used in conjunction with read
    concern `"linearizable"`. That is, if you specify
    `"linearizable"` read concern for
    `db.collection.aggregate()`, you cannot include the
    `$merge` stage in the pipeline.

* - `collation`
  - document
  - Optional. 

    Optional. Specifies the collation  to use for the operation.

    Collation allows users to specify
    language-specific rules for string comparison, such as rules for
    lettercase and accent marks.

    The collation option has the following syntax:

    ```none
    collation: {
       locale: <string>,
       caseLevel: <boolean>,
       caseFirst: <string>,
       strength: <int>,
       numericOrdering: <boolean>,
       alternate: <string>,
       maxVariable: <string>,
       backwards: <boolean>
    }
    ```

    When specifying collation, the `locale` field is mandatory; all
    other collation fields are optional. For descriptions of the fields,
    see collation-document-fields.

    If the collation is unspecified but the collection has a
    default collation (see `db.createCollection()`), the
    operation uses the collation specified for the collection.

    If no collation is specified for the collection or for the
    operations, MongoDB uses the simple binary comparison used in prior
    versions for string comparisons.

    You cannot specify multiple collations for an operation. For
    example, you cannot specify different collations per field, or if
    performing a find with a sort, you cannot use one collation for the
    find and another for the sort.

* - `hint`
  - string or document
  - Optional. The index to use for the aggregation. The index is on the initial
    collection/view against which the aggregation is run.

    Specify the index either by the index name or by the index
    specification document.

    IMPORTANT: The `hint` does not apply to `$lookup` and
    `$graphLookup` stages.

* - `comment`
  - string
  - Optional. Users can specify an arbitrary string to help trace the operation 
    through the database profiler, currentOp, and logs.

* - `writeConcern`
  - document
  - Optional. A document that expresses the write concern
    to use with the `$out` or `$merge` stage. 

    Omit this parameter to use the default write concern with the `$out` or
    `$merge` stage.
                    

## Example

### Pipeline with `$currentOp`

The following example runs a pipeline with two stages. The first stage 
runs the `$currentOp` operation and the second stage filters the
results of that operation. 

```javascript
use admin
db.aggregate( [ { 
   $currentOp : { allUsers: true, idleConnections: true } }, { 
   $match : { shard: "shard01" } 
   }
] )
```
