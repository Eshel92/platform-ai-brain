<!-- Converted from reference/command/count.txt (reStructuredText). Includes are inlined. -->

# count

## Definition

**`count`**

Counts the number of documents in a collection or a view. Returns a
document that contains this count and as well as the command status.

**Tip:**

In `mongosh`, this command can also be run through the `count`  helper method.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

**Note:**

MongoDB drivers compatible with the 4.0 features deprecate their
respective cursor and collection `count()` APIs (which runs the
`count` command) in favor of new APIs that corresponds to
`countDocuments()` and `estimatedDocumentCount()`. For the
specific API names for a given driver, see the driver API
documentation.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command has limited support in M0, M2, M5, and Flex clusters.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The command has the following syntax:

**Note:**

Starting in version 4.2, MongoDB implements a stricter validation of
the option names for the `count` command. The command now
errors if you specify an unknown option name.

```javascript
db.runCommand(
   {
     count: <collection or view>,
     query: <document>,
     limit: <integer>,
     skip: <integer>,
     hint: <hint>,
     readConcern: <document>,
     maxTimeMS: <integer>,
     collation: <document>,
     comment: <any>
   }
)
```

### Command Fields

`count` has the following fields:

* - Field

  - Type

  - Description

* - `count`

  - string

  - The name of the collection or view to count.

* - `query`

  - document

  - Optional. A query that selects which documents to count in the collection or view.

* - `limit`

  - integer

  - Optional. The maximum number of matching documents to return.

* - `skip`

  - integer

  - Optional. The number of matching documents to skip before returning results.

* - `hint`

  - string or document

  - Optional. The index to use. Specify either the index name as a string or the
    index specification document.

* - `readConcern`

  - document

  - Optional. Specifies the read concern. The option has the following
    syntax:

    ```javascript
    readConcern: { level: <value> }
    ```

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
      transactions, and starting in MongoDB 5.0, certain
      read operations outside of multi-document transactions.

    For more formation on the read concern levels, see
    read-concern-levels.

* - `maxTimeMS`

  - non-negative integer

  - Optional.

    Specifies a time limit in milliseconds. 
    If you do not specify a value for `maxTimeMS`, operations will not time out. 
    A value of `0` explicitly specifies the default unbounded behavior.

    MongoDB terminates operations that exceed their allotted time limit
    using the same mechanism as `db.killOp()`. MongoDB only
    terminates an operation at one of its designated interrupt 
    points.

* - `collation`

  - document

  - Optional. 

    Specifies the collation  to use for the operation.

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

* - `comment`

  - any

  - .. include:: /includes/extracts/comment-content.rst

## Stable API Support

Starting in MongoDB 6.0, the `count` command is included in
Stable API V1. To use the `count` command in the
Stable API, you must connect your driver to a deployment that is running
MongoDB 6.0 or greater.

## Behavior

### Inaccurate Counts Without Query Predicate

When you call `count` without a query predicate, you may
receive inaccurate document counts. Without a query predicate,
`count` commands return results based on the collection's
metadata, which may result in an approximate count. In particular,

- On a sharded cluster, the resulting count will not correctly
  filter out orphaned documents.

- After an unclean shutdown or file copy based initial sync, the count may be
  incorrect.

For counts based on collection metadata, see also
collStats pipeline stage with the count
option.

### Count and Transactions

When you use `count` in a transaction, the resulting count will 
not filter out any uncommitted multi-document transactions.

For details, see Transactions and Count Operations.

### Accuracy and Sharded Clusters

On a sharded cluster, the `count` command when run without a query predicate can result in an *inaccurate* count if
orphaned documents exist or if a
chunk migration is in progress.

To avoid these situations, on a sharded cluster, use the
`db.collection.aggregate()` method:

You can use the `$count` stage to count the documents. For
example, the following operation counts the documents in a collection:

```javascript
db.collection.aggregate( [
   { $count: "myCount" }
])
```

The `$count` stage is equivalent to the following
`$group` + `$project` sequence:

```javascript
db.collection.aggregate( [
   { $group: { _id: null, count: { $sum: 1 } } }
   { $project: { _id: 0 } }
] )
```

**See also:**

`$collStats` to return an approximate count based on the
collection's metadata.

### Accuracy after Unexpected Shutdown

After an unclean shutdown of a `mongod` using the Wired Tiger storage engine, count statistics reported by
`count` may be inaccurate.

The amount of drift depends on the number of insert, update, or delete
operations performed between the last checkpoint and the unclean shutdown. Checkpoints
usually occur every 60 seconds. However, `mongod` instances running
with non-default `--syncdelay` settings may have more or less frequent
checkpoints.

Run `validate` on each collection on the `mongod`
to restore statistics after an unclean shutdown.

After an unclean shutdown:

- `validate` updates the count statistic in the `collStats` output with the latest value.

- Other statistics like the number of documents inserted or removed in
  the `collStats` output are
  estimates.

**Note:**

This loss of accuracy only applies to `count`
operations that do *not* include a query document.

### Client Disconnection

Starting in MongoDB 4.2, if the client that issued `count`
disconnects before the operation completes, MongoDB marks `count` 
for termination using `killOp`.

## Examples

The following sections provide examples of the `count`
command.

### Count All Documents

The following operation counts the number of all documents in the
`orders` collection:

```javascript
db.runCommand( { count: 'orders' } )
```

In the result, the `n`, which represents the count, is `26`,
and the command status `ok` is `1`:

```javascript
{ "n" : 26, "ok" : 1 }
```

### Count Documents That Match a Query

The following operation returns a count of the documents in the
`orders` collection where the value of the `ord_dt` field is
greater than `Date('01/01/2012')`:

```javascript
db.runCommand( { count:'orders',
                 query: { ord_dt: { $gt: new Date('01/01/2012') } }
               } )
```

In the result, the `n`, which represents the count, is `13`
and the command status `ok` is `1`:

```javascript
{ "n" : 13, "ok" : 1 }
```

### Skip Documents in Count

The following operation returns a count of the documents in the
`orders` collection where the value of the `ord_dt` field is
greater than `Date('01/01/2012')` and skip the first `10` matching
documents:

```javascript
db.runCommand( { count:'orders',
                 query: { ord_dt: { $gt: new Date('01/01/2012') } },
                 skip: 10 }  )
```

In the result, the `n`, which represents the count, is `3` and
the command status `ok` is `1`:

```javascript
{ "n" : 3, "ok" : 1 }
```

### Specify the Index to Use

The following operation uses the index `{ status: 1 }` to return a
count of the documents in the `orders` collection where the value of
the `ord_dt` field is greater than `Date('01/01/2012')` and the
`status` field is equal to `"D"`:

```javascript
db.runCommand(
   {
     count:'orders',
     query: {
              ord_dt: { $gt: new Date('01/01/2012') },
              status: "D"
            },
     hint: { status: 1 }
   }
)
```

In the result, the `n`, which represents the count, is `1` and
the command status `ok` is `1`:

```javascript
{ "n" : 1, "ok" : 1 }
```

   

### Override Default Read Concern

To override the default read concern level of `"local"`,
use the `readConcern` option.

The following operation on a replica set specifies a
/reference/read-concern of `"majority"` to read the
most recent copy of the data confirmed as having been written to a
majority of the nodes.

**Important:**

- To use the `readConcern` level of `"majority"`, you must specify
  a nonempty `query` condition.

- .. include:: /includes/fact-readConcern-most-recent-data-in-node.rst

```javascript
db.runCommand(
   {
     count: "restaurants",
     query: { rating: { $gte: 4 } },
     readConcern: { level: "majority" }
   }
)
```

To ensure that a single thread can read its own writes, use
`"majority"` read concern and `"majority"`
write concern against the primary of the replica set.
