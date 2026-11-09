<!-- Converted from reference/command/split.txt (reStructuredText). Includes are inlined. -->

# split (database command)

## Definition

**`split`**

Splits a chunk in a sharded cluster into two chunks.
Shards manage and split chunks based on the chunk size statistics they 
maintain.

For exceptional circumstances the `split` command does
allow administrators to manually create splits. See
/tutorial/split-chunks-in-sharded-cluster for information on
these circumstances, and on the MongoDB shell commands that wrap
`split`.

The `split` command must be run in the `admin` database.

   helper methods

**Tip:**

In `mongosh`, this command can also be run through the `sh.splitAt` and `sh.splitFind`.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

                

## Syntax

The command has the following syntax:

```javascript
db.adminCommand( 
   { 
     split: <database>.<collection>, <find|middle|bounds> 
   } 
)
```

## Command Fields

The command takes the following fields:

| Field | Type | Description |
|---|---|---|
| `split` | string | The name of the collection where the chunk exists. Specify the collection's full namespace, including the database name. |
| `find` | document | An query statement that specifies an equality match on the shard key. The match selects the chunk that contains the specified document. You must specify only one of the following: `find`, `bounds`, or `middle`. You cannot use the `find` option on an empty collection. |
| `bounds` | array | `bounds` applies to chunks in collections partitioned using a hashed shard key. The parameter's array must consist of two documents specifying the lower and upper shard-key values of the chunk. The values must match the minimum and maximum values of an existing chunk. Specify only one of the following: `find`, `bounds`, or `middle`. You cannot use the `bounds` option on an empty collection. |
| `middle` | document | The document to use as the split point to create two chunks. `split` requires one of the following options: `find`, `bounds`, or `middle`. |

           

## Considerations

When used with either the `find` or the `bounds` option, the
`split` command splits the chunk along the median. As such,
the command cannot use the `find` or the `bounds` option to split
an empty chunk since an empty chunk has no median.

To create splits in empty chunks, use either the `middle` option with
the `split` command or use the `sh.splitAt()` command.

## Command Formats

To create a chunk split, connect to a `mongos` instance, and
issue the following command to the `admin` database:

```javascript
db.adminCommand( { split: <database>.<collection>,
                   find: <document> } )
```

Or:

```javascript
db.adminCommand( { split: <database>.<collection>,
                   middle: <document> } )
```

Or:

```javascript
db.adminCommand( { split: <database>.<collection>,
                   bounds: [ <lower>, <upper> ] } )
```

To create a split for a collection that uses a hashed shard key,
use the `bounds` parameter. Do *not* use the `middle` parameter for
this purpose.

**Warning:**

Be careful when splitting data in a sharded collection to create
new chunks. When you shard a collection that has existing data,
MongoDB automatically creates chunks to evenly distribute the
collection. To split data effectively in a sharded cluster you must
consider the number of documents in a chunk and the average
document size to create a uniform chunk size. When chunks have
irregular sizes, shards may have an equal number of chunks but have
very different data sizes. Avoid creating splits that lead to a
collection with differently sized chunks.

**See also:**

- `moveChunk`
- `moveRange`
- `sh.moveChunk()`
- `sh.splitAt()`
- `sh.splitFind()`
- `split`

## Examples

The following sections provide examples of the `split` command.

### Split a Chunk in Half

```javascript
db.adminCommand( { split : "test.people", find : { _id : 99 } } )
```

The `split` command identifies the chunk in the `people`
collection of the `test` database, that holds documents that match ``{
_id : 99 }``. `split` does not require that a match exist, in order
to identify the appropriate chunk. Then the command splits it into two
chunks of equal size.

**Note:**

`split` creates two equal chunks by range as
opposed to size, and does not use the selected point as a boundary for
the new chunks.

### Define an Arbitrary Split Point

To define an arbitrary split point, use the following form:

```javascript
db.adminCommand( { split : "test.people", middle : { _id : 99 } } )
```

The `split` command identifies the chunk in the `people`
collection of the `test` database, that would hold documents
matching the query `{ _id : 99 }`. `split` does not
require that a match exist, in order to identify the appropriate
chunk. Then the command splits it into two chunks, with the matching
document as the lower bound of one of the split chunks.

This form is typically used when pre-splitting data in a
collection.

### Split a Chunk Using Values of a Hashed Shard Key

This example uses the hashed shard key `userid` in a
`people` collection of a `test` database. The following command
uses an array holding two single-field documents to represent the
minimum and maximum values of the hashed shard key to split the chunk:

```javascript
db.adminCommand( { split: "test.people",
                  bounds : [ { userid: Long("-5838464104018346494") },
                             { userid: Long("-5557153028469814163") }
             ] } )
```

**Note:** MongoDB uses the 64-bit NumberLong

type to represent the hashed value.

Use `sh.status()` to see the existing bounds of the shard keys.

## Metadata Lock Error

If another process, such as a balancer
process, changes metadata while `split` is running, you may
see a `metadata lock error`.

```none
errmsg: "The collection's metadata lock is already taken."
```

This message indicates that the split has failed with no side
effects. Retry the `split` command.
