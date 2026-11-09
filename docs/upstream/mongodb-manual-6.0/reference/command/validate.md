<!-- Converted from reference/command/validate.txt (reStructuredText). Includes are inlined. -->

# validate

## Definition

**`validate`**

The `validate` command checks a collection's data and
indexes for correctness and returns the results.

**Tip:**

In `mongosh`, this command can also be run through the `validate` helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

**Changed in version:** 5.0

Starting in version 5.0, the `validate` command can also
find inconsistencies in the collection and fix them if possible.

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

**Note:**

The `validate` command does not support views and raises an error when run against a view.

The `db.collection.validate()` method in
`mongosh` provides a wrapper around
`validate`.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in M0, M2, M5, and Flex clusters or in serverless instances.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

**Changed in version:** 5.0

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     validate: <string>,          // Collection name
     full: <boolean>,             // Optional
     repair: <boolean>,           // Optional, added in MongoDB 5.0
     metadata: <boolean>          // Optional, added in MongoDB 5.0.4
   } 
)
```

## Command Fields

The command takes the following fields:

* - Field
  - Type
  - Description

* - `validate`
  - string
  - The name of the collection to validate.

* - full
  - boolean
  - .. _cmd-validate-full:

    Optional. A flag that determines whether the command
    performs a slower but more thorough check or a faster but less thorough check.

    - If `true`, performs a more thorough check with the following
      exception:

      - Full validation on the `oplog` for WiredTiger skips the more 
        thorough check. The `validate.warnings` includes a notice of 
        the behavior.

    - If `false`, omits some checks for a faster but less
      thorough check.

    The default is `false`.

    For the WiredTiger storage engine, only the `full` validation process will 
    force a checkpoint and flush all in-memory data to disk before verifying the 
    on-disk data.

* - repair
  - boolean
  - .. _cmd-validate-repair:

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
      index that is not a multikey index, the
      index is changed to a multikey index.

    - If multikey documents are found that are
      not specified by an index's multikey
      paths, the index's multikey paths are
      updated.

    - If corrupt documents with invalid BSON data are found, the documents
      are removed.

    For more information, see the `--repair` option
    for `mongod`

    **New in version:** 5.0

* - metadata
  - boolean
  - .. _cmd-validate-metadata:

    *Optional*. A flag which allows users to perform a quick validation to 
    detect invalid index options without scanning all of the documents and 
    indexes.

    - If `true`, a metadata validation scan is performed.

    - If `false`, no metadata validation scan is not performed.

    The default is `false`.

    Running the validate command with `{ metadata: true }` is not 
    supported with any other `validate` options.

    The `metadata` validation option:

    - Provides you a faster way of identifying invalid indexes by scanning 
      only collections metadata.

    - Provides an alternative to dropping and recreating multiple invalid 
      indexes when used with the collMod 
      command.

    The `metadata` validation option only scans collection metadata to 
    find invalid indexes more quickly.

    If there is an invalid index detected, the validate command will prompt
    you to use the `collMod` command to remove invalid indexes.

    ```javascript
    db.runCommand( { collMod: <collectionName> } )
    ```

    **New in version:** 5.0.4

## Behavior

### Performance

The `validate` command can be slow, particularly on
larger data sets.

The `validate` command obtains an exclusive lock `W` on
the collection. This will block all reads and writes on the collection
until the operation finishes. When run on a secondary, the
`validate` operation can block all other operations on that
secondary until it finishes.

**Warning:**

Due to the performance impact of validation, consider running
`validate` only on secondary replica set nodes.
You can use `rs.stepDown()` to instruct the current
primary node to become a secondary to avoid impacting a live
primary node.

### Data Throughput Metrics

The `$currentOp` and the `currentOp` command
include `dataThroughputAverage` and
`dataThroughputLastSecond` information for
validate operations in progress.

The log messages for validate operations include
`dataThroughputAverage` and `dataThroughputLastSecond`
information.

### Restrictions

The `validate` command no longer supports afterClusterTime. As such, `validate` cannot be
associated with causally consistent sessions.

### Index Key Format

Starting in MongoDB 6.0, the `validate` command returns a message if a
unique index has a key format that is
incompatible. The message indicates an old format is used.

## Examples

- To validate a collection `myCollection` using the default validation
  setting (specifically, full: false):

  ```javascript
  db.runCommand( { validate: "myCollection" } )
  ```

- To perform a full validation of collection `myCollection`, specify
  full: true:

  ```javascript
  db.runCommand( { validate: "myCollection", full: true } )
  ```

    
- To repair collection `myCollection`, specify
  repair: true:

  ```javascript
  db.runCommand( { validate: "myCollection", repair: true } )
  ```

- To validate the metadata in the `myCollection` collection, 
  specify metadata: true:

  ```javascript
  db.runCommand( { validate: "myCollection", metadata: true } )
  ```

## Validate Output

**Note:**

The output may vary depending on the version and specific
configuration of your MongoDB instance.

Specify full: true for more detailed output.

**`validate.nInvalidDocuments`**

The number of invalid documents in the collection. Invalid documents
are those that are not readable, which means the BSON
document is corrupt and has an error or a size mismatch.

**`validate.nNonCompliantDocuments`**

The number of documents not conforming to the collection's schema.
Non-compliant documents are not counted as invalid in
`nInvalidDocuments`.

**`validate.nrecords`**

The number of documents in the collection.

**`validate.nIndexes`**

The number of indexes on the collection that were validated.

**`validate.keysPerIndex`**

A document that contains the name and index entry count for each
index on the collection.

```javascript
"keysPerIndex" : {
   "_id_" : <num>,
   "<index2_name>" : <num>,
   ...
}
```

`keysPerIndex` identifies the index by its name only. 

**`validate.indexDetails`**

A document that contains the status of the index validation for each
index.

```javascript
"indexDetails" : {
   "_id_" : {
      "valid" : <boolean>
   },
   "<index2_name>" : {
      "valid" : <boolean>  
   },
   ...
}
```

- `indexDetails` identifies the specific index (or
  indexes) that is invalid. Earlier versions of MongoDB would mark
  all indexes as invalid, if any of the indexes were invalid.

- `indexDetails` identifies the index by its name
  only. Earlier versions of MongoDB displayed the full namespace of
  the index; i.e. `<db>.<collection>.$<index_name>`.

**`validate.ns`**

The full namespace name of the collection. Namespaces include the
database name and the collection name in the form
`database.collection`.

**`validate.valid`**

A boolean that is `true` if `validate` determines that
all aspects of the collection are valid. When `false`, see the
`errors` field for more information.

**`validate.repaired`**

A boolean that is `true` if `validate` repaired the
collection.

**`validate.warnings`**

An array that contains warning messages, if any, regarding the
validate operation itself. The warning messages do not indicate that
the collection is itself invalid. For example:

```javascript
"warnings" : [
   "Could not complete validation of table:collection-28-6471619540207520785. This is a transient issue as the collection was actively in use by other operations."
],
```

**`validate.errors`**

If the collection is not valid (i.e
`valid` is false), this field will contain a message
describing the validation error.

**`validate.extraIndexEntries`**

An array that contains information for each index entry that points
to a document that does not exist in the collection.

```javascript
"extraIndexEntries" : [
   {
      "indexName" : <string>,
      "recordId" : <NumberLong>,  // for the non-existent document
      "indexKey" : {
         "<key1>" : <value>,
         ...
      }
   }
   ...
]
```

**Note:**

For the `extraIndexEntries` array, the sum of all
the `indexKey` field sizes has a limit of 1MB where the sizes
include both the keys and values for the `indexKey`. If
the sum exceeds this size, the warning field displays a message.

**`validate.missingIndexEntries`**

An array that contains information for each document that is missing
the corresponding index entry.

```javascript
"missingIndexEntries" : [
   {
      "indexName" : <string>,
      "recordId" : <NumberLong>,
      "idKey" : <_id key value>,     // The _id value of the document. Only present if an ``_id`` index exists.
      "indexKey" : {                 // The missing index entry
         "<key1>" : <value>,
         ...
      }
   }
   ...
 ]
```

**Note:**

For the `missingIndexEntries` array, the sum of
the `idKey` field size and all its `indexKey` field sizes has
a limit of 1MB where the field sizes include both the keys and
values for the `idKey` and `indexKey`. If the sum
exceeds this size, the warning field displays a message.

**`validate.corruptRecords`**

An array of `RecordId` values for documents that are unreadable,
possibly because the data is damaged. These documents are reported as
corrupt during validation. A `RecordId` is a 64-bit integer
internal key that uniquely identifies a document in a collection.

```javascript
"corruptRecords" : [
   NumberLong(1),  // RecordId 1
   NumberLong(2)   // RecordId 2
]
```

**New in version:** 5.0

**`validate.ok`**

An integer with the value `1` when the command succeeds. If the
command fails the `ok` field has a value of `0`.
