<!-- Converted from reference/command/clearJumboFlag.txt (reStructuredText). Includes are inlined. -->

# clearJumboFlag

## Definition

**`clearJumboFlag`**

Clears the jumbo flag for a chunk. To use the
command, issue the `clearJumboFlag` command on a
`mongos` instance.

## Compatibility

This command is available in deployments hosted in the following environments: 

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud

**Important:**

This command is not supported in serverless instances.
For more information, see Unsupported Commands.

- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

Th command has the following syntax:

```javascript
db.adminCommand( 
   {
     clearJumboFlag: "<database>.<collection>",
     bounds: <array>
   } 
)
```

**-OR-**

```javascript
// Cannot use for collections with hashed shard keys

db.adminCommand( 
   {
     clearJumboFlag: "<database>.<collection>",
     find: <query>
   } 
)
```

### Command Fields

The `clearJumboFlag` command takes the following fields as
arguments:

* - Field

  - Type

  - Description

* - clearJumboFlag

  - string

  - .. _clearJumboFlag-namespace:

    The namespace of the sharded collection with the
    jumbo chunk(s).

    Specify the collection's full namespace, including the
    database name (i.e. "<database>.<collection>")

* - bounds

  - array

  - .. _clearJumboFlag-bounds:

    The exact bounds of a specific chunk. The array must consist of two
    documents that specify the lower and upper shard key values of a chunk
    to move:

    `[ { <shardKey> : <minValue> },{ <shardKey> : <maxValue> } ]`

    - Specify either the bounds
      field or the find field but
      not both.

    - If the collection uses a hashed shard key, use the
      bounds field.

* - find

  - document

  - .. _clearJumboFlag-find:

    A specific shard key and its value contained in the jumbo chunk.

    `{ <shardKey> : <value> }`

    - Specify either the bounds
      field or the `find` field but not both.

    - If the collection uses a hashed shard key, do
      **not** use the find field.
      Use bounds instead.

## Access Control

On systems running with `authorization`, the user
must have the `clearJumboFlag` privilege actions on the ``{
db: "", collection: "" }`` resource.

The built-in role `clusterManager` provides the appropriate
privileges.

## Example

### Clear Jumbo Flag for a Chunk (Range-Based Shard Key)

The `sh.status()` includes the following
`sh.status.databases.<collection>.chunk-details` for the
`test.jumbo` collection.

```javascript
... // Content omitted for brevity

test.jumbo
         shard key: { "x" : 1 }
         unique: false
         balancing: true
         chunks:
                  shardA   2
                  shardB   2
         { "x" : { "$minKey" : 1 } } -->> { "x" : 1 } on : shardB Timestamp(3, 0) 
         { "x" : 1 } -->> { "x" : 2 } on : shardA Timestamp(6, 1) jumbo 
         { "x" : 2 } -->> { "x" : 3 } on : shardA Timestamp(5, 1) jumbo 
         { "x" : 3 } -->> { "x" : { "$maxKey" : 1 } } on : shardB Timestamp(6, 0) 
```

The following `clearJumboFlag` command specifies the
bounds of the ``{ "x" : 1 } -->> { "x" :
2 }`` chunk:

```javascript
db.adminCommand( {
   clearJumboFlag: "test.jumbo",
   bounds: [{ "x" : 1 }, { "x" : 2 }]
} )
```

Upon success, the command returns `"ok": 1` in its output:

```javascript
{
   "ok" : 1,
   "operationTime" : Timestamp(1580190080, 5),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1580190080, 5),
      "signature" : {
         "hash" : BinData(0,"0cYT49s72MHUYV1F2WpoEwlyeVs="),
         "keyId" : NumberLong("6786859092951433239")
      }
   }
}
```

The following `clearJumboFlag` command specifies the
find field to find the chunk that
contains the shard key `{ "x" : 2 }` :

```javascript
db.adminCommand( {
   clearJumboFlag: "test.jumbo",
   find: { "x" : 2 }
} )
```

Upon success, the command returns `"ok": 1` in its output:

```javascript
{
   "ok" : 1,
   "operationTime" : Timestamp(1580191819, 5),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1580191819, 5),
      "signature" : {
         "hash" : BinData(0,"N6x6drN7HUq5MR5ezUJns1rfeqY="),
         "keyId" : NumberLong("6786859092951433239")
      }
   }
}
```

To verify the operation, run `sh.status()` again. The `jumbo`
flag should no longer appear in its output.

```javascript
... // Content omitted for brevity

test.jumbo
         shard key: { "x" : 1 }
         unique: false
         balancing: true
         chunks:
                  shardA   2
                  shardB   2
         { "x" : { "$minKey" : 1 } } -->> { "x" : 1 } on : shardB Timestamp(3, 0) 
         { "x" : 1 } -->> { "x" : 2 } on : shardA Timestamp(7, 0) 
         { "x" : 2 } -->> { "x" : 3 } on : shardA Timestamp(8, 0) 
         { "x" : 3 } -->> { "x" : { "$maxKey" : 1 } } on : shardB Timestamp(6, 0) 
```

### Clear Jumbo Flag for a Chunk (Hashed Shard Key)

The `sh.status()` includes the following
`sh.status.databases.<collection>.chunk-details` for the
`test.jumboHashed` collection. The collection uses a hashed shard
key.

```javascript
... // Content omitted for brevity

test.jumboHashed
         shard key: { "x" : "hashed" }
         unique: false
         balancing: true
         chunks:
                  shardA   2
                  shardB   2
         { "x" : { "$minKey" : 1 } } -->> { "x" : NumberLong(0) } on : shardA Timestamp(1, 0) 
         { "x" : NumberLong(0) } -->> { "x" : NumberLong("848411777775835583") } on : shardA Timestamp(4, 0) 
         { "x" : NumberLong("848411777775835583") } -->> { "x" : NumberLong("5902408780260971510") } on : shardB Timestamp(4, 1) jumbo 
         { "x" : NumberLong("5902408780260971510") } -->> { "x" : { "$maxKey" : 1 } } on : shardB Timestamp(2, 2) 
```

To clear the `jumbo` flag for a chunk if the collection uses a
hashed shard key, use `clearJumboFlag` with the
bounds field:

```javascript
db.adminCommand( {
   clearJumboFlag: "test.jumboHashed",
   bounds: [{ "x" : NumberLong("848411777775835583") }, { "x" : NumberLong("5902408780260971510") }]
} )
```

Upon success, the command returns `"ok": 1` in its output:

```javascript
{
   "ok" : 1,
   "operationTime" : Timestamp(1580194290, 5),
   "$clusterTime" : {
      "clusterTime" : Timestamp(1580194290, 5),
      "signature" : {
         "hash" : BinData(0,"nWCqOYVrab7NEGHWoo2NYENqHR4="),
         "keyId" : NumberLong("6786875525496307742")
      }
   }
}
```

To verify the operation, run `sh.status()` again. The
`jumbo` flag should no longer appear in its output.

```javascript
... // Content omitted for brevity

test.jumboHashed
         shard key: { "x" : "hashed" }
         unique: false
         balancing: true
         chunks:
                  shardA	2
                  shardB	2
         { "x" : { "$minKey" : 1 } } -->> { "x" : NumberLong(0) } on : shardA Timestamp(1, 0) 
         { "x" : NumberLong(0) } -->> { "x" : NumberLong("848411777775835583") } on : shardA Timestamp(4, 0) 
         { "x" : NumberLong("848411777775835583") } -->> { "x" : NumberLong("5902408780260971510") } on : shardB Timestamp(5, 0) 
         { "x" : NumberLong("5902408780260971510") } -->> { "x" : { "$maxKey" : 1 } } on : shardB Timestamp(2, 2)
```

**See also:**

/tutorial/clear-jumbo-flag
