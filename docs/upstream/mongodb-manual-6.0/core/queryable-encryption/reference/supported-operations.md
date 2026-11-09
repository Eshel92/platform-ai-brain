<!-- Converted from core/queryable-encryption/reference/supported-operations.txt (reStructuredText). Includes are inlined. -->

# Supported Operations for Queryable Encryption

This page documents the specific commands, query operators, update
operators, aggregation stages, and aggregation expressions supported by
MongoDB version 6.0 or later compatible drivers configured for automatic encryption.

**Note:** Enterprise Feature

Automatic encryption is available in MongoDB Enterprise and MongoDB Atlas
using MongoDB version 6.0 or later.

## Operations Using `BinData`

MongoDB stores Queryable Encryption encrypted fields as a `BinData` blob.
Read and write operations issued against the encrypted `BinData` value may have
unexpected or incorrect behavior as compared to issuing that same operation against
the decrypted value. Certain operations have strict BSON type support where issuing
them against a `BinData` value returns an error. Official drivers compatible with MongoDB
version 6.0 or later using Automatic Encryption with Queryable Encryption parse read and write
operations for operators or expressions that do not support `BinData` values
or that have abnormal behavior when issued against `BinData` values.

Applications using explicit Queryable Encryption may use this page as guidance for issuing
read and write operations against encrypted fields.

## Supported Read and Write Commands

Official drivers for MongoDB version 6.0 or later support automatic encryption with the
following commands:

- `aggregate`
- `count`
- `delete`
- `explain`
- `find`
- `findAndModify`
- `insert`
- `update`

For any supported command, Queryable Encryption compatible drivers return an error if
the command uses an unsupported operator, aggregation stage, or aggregation
expression. For a complete list of the supported operators, stages, and
expressions, see the following sections of this page:

- Supported Query Operators
- Supported Update Operators
- Supported Aggregation Stages
- Supported Aggregation Expressions

The following commands do not require automatic encryption. Official drivers
configured for Automatic Encryption pass these commands directly to the
`mongod`:

- `getMore` [#]_
- `authenticate`
- `getnonce`
- `hello`
- `logout`
- `abortTransaction`
- `commitTransaction`
- `endSessions`
- `startSession`
- `create`
- `createIndexes`
- `drop`
- `dropDatabase`
- `dropIndexes`
- `killCursors`
- `listCollections`
- `listDatabases`
- `listIndexes`
- `renameCollection`
- `ping`

Issuing any other command through a compatible driver configured for automatic
encryption returns an error.

## Supported Query Operators

Drivers configured for automatic encryption support the following query operators when
issued against an encrypted queryable field:

- `$eq`
- `$ne`
- `$in`
- `$nin`
- `$and`
- `$or`
- `$not`
- `$nor`

**Important:** Comparison Support

Comparison of one encrypted field to another encrypted field will fail.

```json
{$expr: {$eq: ["$encrypted1", "$encrypted2"]}}
```

Comparison of an encrypted field to a plaintext value is supported.

```json
{$expr: {$eq: ["$encrypted1", "plaintext_value"]}}
```

Queries that compare an encrypted field to `null` or a regular expression
*always* throw an error, even if using a supported query operator.

The `$exists` operator has normal behavior when issued against
encrypted fields.

Queries specifying any other query operator against an encrypted field return an error.
The following query operators throw an error even if not issued against an encrypted field
when using a MongoClient configured for Queryable Encryption:

- `$text`
- `$where`
- `$jsonSchema`

## Supported Update Operators

Drivers configured for automatic encryption support the following update operators
when issued against encrypted fields:

- `$set`
- `$unset`

Updates specifying any other update operator against an encrypted field
return an error.

Update operations with the following behavior throw an error even if
using a supported operator:

- The update operation produces an array inside of an encrypted path.
- The update operation uses aggregation expression syntax.

For update operations specifying a query filter
on encrypted fields, the query filter must use only supported operators on those fields.

## Replacement-style Updates

Replacement-style updates are supported, however, if the replacement document
contains a `Timestamp(0,0)` inside a top-level encrypted field,
Queryable Encryption will error. The `(0,0)` value indicates that the
`mongod` should generate the Timestamp.  `mongod`
cannot generate encrypted fields.

## Unsupported Insert Operations

Compatible drivers configured for automatic encryption do not support insert
commands with the following behavior:

- Inserting a document with `Timestamp(0,0)` associated to an encrypted field.
  The `(0,0)` value indicates that the `mongod` should
  generate the Timestamp. Since the `mongod` cannot generate
  encrypted fields, the resulting timestamp would be unencrypted.

## Unsupported Aggregation Stages

Automatic encryption will not support aggregation stages that read from or
write to additional collections. These stages are:

- `$out`
- `$merge`

## Supported Aggregation Stages

Compatible drivers configured for automatic encryption support the following
aggregation pipeline stages:

- `$addFields`
- `$bucket`
- `$bucketAuto`
- `$collStats`
- `$count`
- `$geoNear`
- `$group` on unencrypted fields
- `$indexStats`
- `$limit`
- `$lookup` and `$graphLookup` (For usage
  requirements, see csfle-lookup-graphLookup-behavior)
- `$match`
- `$project`
- `$redact`
- `$replaceRoot`
- `$sample`
- `$skip`
- `$sort`
- `$sortByCount`
- `$unwind`

Aggregation pipelines operating on collections configured for automatic
encryption that specify any other stage return an error.

For each supported pipeline stage, MongoDB tracks fields that *must* be
encrypted as they pass through the supported pipelines and marks them
for encryption.

Each supported stage must specify only supported
query operators and
aggregation expressions.

### `$lookup` and `$graphLookup` Behavior

Automatic encryption supports the `$lookup` and
`$graphLookup` *only if* the `from` collection matches the
collection  the aggregation runs against.
`$lookup` and `$graphLookup` stages that reference a different `from`
collection return an error.

Automatic encryption does not support “connectionless” aggregation metadata
sources, which read metadata that doesn’t pertain to a particular
collection, such as:

- `$currentOp`
- changeStreams for watching a database or the whole cluster
- `$listSessions`
- `$listLocalSessions`

Automatic Encryption does not support the `$planCacheStats` stage
as the result may contain sensitive information.

## Supported Aggregation Expressions

Compatible drivers configured for automatic encryption support the following
expressions against any equality query type encrypted fields:

- `$cond`
- `$eq`
- `$ifNull`
- `$in`
- `$let`
- `$literal`
- `$ne`
- `$switch`

All other aggregation expressions return an error if issued against
encrypted fields.

Aggregation stages with the following behavior return an error
*even if* using a supported aggregation expression:

* - Expressions
  - Rejected Behavior
  - Example

* - `$cond`

    `$switch`
  - The expression specifies a field whose encryption properties
    cannot be known until runtime *and* a subsequent aggregation
    stage includes an expression referencing that field.
  - .. code-block:: javascript
       :copyable: false

       $addFields : {
         "valueWithUnknownEncryption" : {
           $cond : {
             if : { "$encryptedField" : "value" },
             then : "$encryptedField",
             else: "unencryptedValue"
           }
         }
       },
       {
         $match : {
           "valueWithUnknownEncryption" : "someNewValue"
         }
       }

* - `$eq`

    `$ne`
  - The expression creates a new field that references an
    encrypted field *and* operates on that new field in the same
    expression.
  - .. code-block:: javascript
       :copyable: false

       {
         $eq : [
           {"newField" : "$encryptedField"},
           {"newField" : "value"
         ]
       }

* - `$eq`

    `$ne`
  - The expression references the prefix of an encrypted field
    within the comparison expression.
  - .. code-block:: javascript
       :copyable: false

       { $eq : [ "$prefixOfEncryptedField" , "value"] }

* - `$eq`

    `$ne`
  - The result of the expression is compared to an encrypted field.
  - .. code-block:: javascript
       :copyable: false

       {
         $eq : [
             "$encryptedField" ,
             { $ne : [ "field", "value" ] }
         ]
       }

* - `$let`
  - The expression binds a variable to an encrypted
    field or attempts to rebind `$$CURRENT`.
  - .. code-block:: javascript
       :copyable: false

       {
         $let: {
           "vars" : {
             "newVariable" : "$encryptedField"
           }
         }
       }

* - `$in`
  - The first argument to the expression *is* an encrypted field,
    *and*

    - The second argument to the expression is *not* an array literal

      *-OR-*

    - The second argument to the expression is an encrypted field.
  - .. code-block:: javascript
       :copyable: false

       {
         $in : [
           "$encryptedField" ,
           "$otherEncryptedField"
         ]
       }

## Unsupported Field Types

Drivers configured for automatic encryption do *not* support any
read or write operation that requires encrypting the following value
types:

- `MaxKey`
- `MinKey`
- `null`
- `undefined`

Queryable Encryption does not adequately hide the type information for these values.

Queryable Encryption does not support read or write operations on an
encrypted field where the operation compares the encrypted field to the
following value types:

- `array`
- `decimal128`
- `double`
- `object`
