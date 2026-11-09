<!-- Converted from core/csfle/reference/supported-operations.txt (reStructuredText). Includes are inlined. -->

# Supported Operations for Automatic Encryption

This page documents the specific commands, query operators, update
operators, aggregation stages, and aggregation expressions supported by
drivers configured for automatic Client-Side Field Level Encryption.

## Supported Read and Write Commands

Drivers using automatic Client-Side Field Level Encryption support the following commands:

- `aggregate`
- `count`
- `delete`
- `distinct`
- `explain`
- `find`
- `findAndModify`
- `insert`
- `update`

For any supported command, drivers return an error if the command uses
an unsupported operator, aggregation stage, or aggregation expression.
For a complete list of the supported operators, stages, and expressions,
see the following sections of this page:

- Supported Query Operators
- Supported Update Operators
- Supported Aggregation Stages
- Supported Aggregation Expressions

The following commands do not require automatic encryption. Drivers
configured for automatic Client-Side Field Level Encryption pass these commands directly to the
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

Issuing any other command through a driver
configured for automatic Client-Side Field Level Encryption returns an error.

## Supported Query Operators

Drivers configured for automatic Client-Side Field Level Encryption allow the following query
operators when issued against deterministically encrypted fields:

- `$eq` 
- `$ne` 
- `$in` 
- `$nin`
- `$and`
- `$or`
- `$not`
- `$nor`

Queries that compare an encrypted field to `null` or a regular
expression always return an error even when using a supported query
operator. Queries issuing these operators against a randomly
encrypted field return an error.

The `$exists` operator has normal behavior when issued against
both deterministically and randomly encrypted fields.

Queries specifying any other query operator against an encrypted field
return an error.

The following query operators return an error *even if* not issued
against an encrypted field:

- `$text`
- `$where`
- `$jsonSchema`

**Warning:** Unexpected Behavior with BinData

MongoDB stores client-side field level encrypted fields as a
`BinData` blob. Read and write operations
issued against the encrypted `BinData` value may have unexpected or
incorrect behavior as compared to issuing that same operation against
the decrypted value. Certain operations have strict BSON type support
where issuing them against a `BinData` value returns an error.

- Drivers using automatic Client-Side Field Level Encryption parse read and write operations
  for operators or expressions that do not support `BinData` values
  *or* that have unexpected behavior when issued against `BinData`
  values.

- Applications using explicit (manual) Client-Side Field Level Encryption *may* use this page
  as guidance for issuing read and write operations against encrypted
  fields.

## Unsupported Insert Operations

Drivers configured for automatic Client-Side Field Level Encryption do *not* support insert
commands with the following behavior: 

- Inserting a document with `Timestamp(0,0)` associated to an
  encrypted field. The `(0,0)` value indicates that the
  `mongod` should generate the Timestamp. When the
  `mongod` cannot generated encrypted fields, the resulting
  timestamp is unencrypted.

- Inserting a document without an encrypted `_id` *if* the configured
  automatic schema specifies an encrypted `_id` field. When the
  `mongod` automatically generates an unencrypted
  ObjectId, omitting `_id` from documents results in
  documents that do not conform to the automatic encryption rules.

- Inserting a document with an array associated to a
  deterministically encrypted
  field. Automatic Client-Side Field Level Encryption does not support deterministically
  encrypting arrays.

## Supported Update Operators

Drivers configured for automatic Client-Side Field Level Encryption allow the following update
operators when issued against deterministically encrypted fields:

- `$set`
- `$unset`
- `$rename`

When you use the `$rename` operator on encrypted fields, the
automatic JSON schema must specify the same encryption metadata for the
source and target field names.

Updates specifying any other update operator against an encrypted field
return an error.

Update operations with the following behavior return an error
*even if* using a supported operator:

- The update operation produces an array inside of an encrypted path. 

- The update operation uses aggregation expression syntax.

For update operations specifying a query filter on deterministically encrypted fields, the query
filter must use only supported operators on those fields.

## Supported Aggregation Stages

Drivers configured for automatic Client-Side Field Level Encryption support the following
aggregation pipeline stages:

- `$addFields`
- `$bucket`
- `$bucketAuto`
- `$collStats`
- `$count`
- `$geoNear`
- `$group` (For usage requirements, see
  csfle-group-behavior)
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

Pipelines operating on collections configured for automatic encryption
that specify any other stage return an error.

For each supported pipeline stage, MongoDB tracks fields that
*must* be encrypted as they pass through the supported pipelines and
marks them for encryption. 

Each supported stage must specify only supported
query operators and
aggregation expressions.

### `$group` Behavior

`$group` has the following behaviors specific to Client-Side Field Level Encryption:

`$group` supports:

- Grouping on deterministically encrypted fields.
- Using `$addToSet` and `$push` accumulators on
  encrypted fields.
  
$group does not support:

- Matching on the array returned by  `$addToSet` and
  `$push` accumulators.
- Arithmetic accumulators on encrypted fields.

### `$lookup` and `$graphLookup` Behavior

Automatic Client-Side Field Level Encryption supports the `$lookup` and
`$graphLookup` *only if* the `from` collection matches the
collection on which the aggregation runs against (specifically,
self-lookup operations).

`$lookup` and `$graphLookup` stages that
reference a different `from` collection return an error.

### Supported Aggregation Expressions

Drivers configured for automatic Client-Side Field Level Encryption allow aggregation stages
using the following expressions against deterministically
encrypted fields:

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

Drivers configured for automatic Client-Side Field Level Encryption (CSFLE) do *not* support any
read or write operation that requires encrypting the following value
types:

- `MaxKey`
- `MinKey`
- `null`
- `undefined`

Encryption does not adequately hide the type information for these
values.

Automatic CSFLE *also* does not support read or write operations on a
deterministically encrypted field where the operation compares the
encrypted field to the following value types:

- `array`
- `bool`
- `decimal128`
- `double`
- `object`
