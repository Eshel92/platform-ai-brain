<!-- Converted from reference/command/createIndexes.txt (reStructuredText). Includes are inlined. -->

# createIndexes (database command)

## Definition

**`createIndexes`**

Builds one or more indexes on a collection.

   `db.collection.createIndexes()` helper methods

**Tip:**

In `mongosh`, this command can also be run through the `db.collection.createIndex()` and.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

## Compatibility

This command is available in deployments hosted in the following environments: 

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

The `createIndexes` command takes the following form:

```javascript
db.runCommand(
   {
     createIndexes: <collection>,
     indexes: [
         {
             key: {
                 <key-value_pair>,
                 <key-value_pair>,
                 ...
             },
             name: <index_name>,
             <option1>,
             <option2>,
             ...
         },
         { ... },
         { ... }
     ],
     writeConcern: { <write concern> },
     commitQuorum: <int|string>,
     comment: <any>
   }
 )
```

 

### Command Fields

The `createIndexes` command takes the following fields:

* - Field

  - Type

  - Description

* - `createIndexes`

  - string

  - The collection for which to create indexes.

* - `indexes`

  - array

  - Specifies the indexes to create. Each document in the array specifies a
    separate index.

* - `writeConcern`

  - document

  - Optional. A document expressing the write concern. Omit to use the default write concern.

* - `commitQuorum`

  - integer or string

  - .. _createIndexes-cmd-commitQuorum:

    Optional. The minimum number of data-bearing replica
    set members (i.e. commit quorum), including the primary, that
    must report a successful index build before the primary
    marks the `indexes` as ready. 

    You can resume some
    interrupted index builds
    when the commit quorum is set to the default
    `"votingMembers"`. See `setIndexCommitQuorum`.

    Replica set nodes in a commit quorum must have `members[n].buildIndexes` 
    set to `true`. If any voting nodes have 
    `members[n].buildIndexes` set to `false`, you can't use the 
    default `"votingMembers"` commit quorum. Either configure all 
    nodes with `members[n].buildIndexes` set to `true`, or 
    select a different commit quorum.  

    Supports the following values:

    - `"votingMembers"` - all data-bearing voting replica set
      members (*Default*). A "voting" member is any replica set member 
      where `members[n].votes` is greater than `0`.

    - `"majority"` - a simple majority of data-bearing replica set members.

    - `<int>` - a specific number of data-bearing replica set members.

    - `0` - Disables quorum-voting behavior. Members 
      start the index build simultaneously but do *not* 
      vote or wait for quorum before completing the 
      index build. If you start an index build with 
      a commit quorum of `0`, you cannot later modify the 
      commit quorum using `setIndexCommitQuorum`.

    - A replica set tag name.

* - `comment`

  - any

  - .. include:: /includes/extracts/comment-content.rst

Each document in the `indexes` array can take the following fields:

* - Field

  - Type

  - Description

* - `key`

  - document

  - Specifies the index's fields. For each field, specify a 
    key-value pair in which the key is the name of the field to 
    index and the value is either the index direction or index 
    type. If specifying direction, specify `1` for 
    ascending or `-1` for descending.

    MongoDB supports several different index types, including:

    - text 
    - geospatial 
    - hashed indexes

    See index types for more information.

    Wildcard indexes support workloads where
    users query against custom fields or a large variety of fields in a
    collection:

    - You can create a wildcard index on a specific field and its
      subpaths or on all of the fields in a document.

      For details see, wildcard-index-core.

* - `name`

  - string

  - A name that uniquely identifies the index.

* - `unique`

  - boolean

  - Optional. Creates a unique index so that the collection will not accept
    insertion or update of documents where the index key value matches an existing
    value in the index.

    Specify `true` to create a unique index. The
    default value is `false`.

    The option is *unavailable* for hashed
    indexes.

* - `partialFilterExpression`

  - document

  - Optional. If specified, the index only references documents that match the
    filter expression. See /core/index-partial for more information.

    A filter expression can include:

    - equality expressions (i.e. `field: value` or using the `$eq`
      operator)

    - `$exists: true` expression

    - `$gt`, `$gte`, `$lt`, `$lte` expressions

    - `$type` expressions

    - `$and` operator

    - `$or` operator

    - `$in` operator

    - `$geoWithin` operator

    - `$geoIntersects` operator

    If you are using Client-Side Field Level Encryption or Queryable Encryption, a `partialFilterExpression` cannot reference an
    encrypted field.

    You can specify a `partialFilterExpression` option for all MongoDB
    index types.

* - `sparse`

  - boolean

  - Optional. If `true`, the index only references documents with the specified
    field. These indexes use less space but behave differently in some
    situations (particularly sorts). The default value is `false`.
    See /core/index-sparse for more information.

    The following index types are sparse by default and ignore
    this option:

    - 2dsphere
    - 2d
    - Text

    For a compound index that includes `2dsphere` index key(s)
    along with keys of other types, only the `2dsphere` index
    fields determine whether the index references a document.

    MongoDB provides the option to create
    partial indexes. These
    offer a superset of the functionality of sparse indexes
    and are preferred instead.

* - `expireAfterSeconds`

  - integer

  - .. include:: /includes/indexes/expireAfterSeconds-config-option.rst

    If you use TTL indexes created before MongoDB 5.0, or if you want to
    sync data created in MongDB 5.0 with a pre-5.0 installation, see
    expireData-warning to avoid misconfiguration issues.

    (Include not available offline: includes/expireAfterSeconds-range.rst)

* - hidden

  - boolean

  - .. _cmd-createIndexes-hidden:

    Optional. A flag that determines whether the index is
    hidden from the query planner. A
    hidden index is not evaluated as part of query plan
    selection.

    Default is `false`.

* - `storageEngine`

  - document

  - Optional. Allows users to configure the storage engine on a
    per-index basis when creating an index.

    The `storageEngine` option should take the following form:

    ```javascript
    storageEngine: { <storage-engine-name>: <options> }
    ```

    Storage engine configuration options specified when creating indexes are
    validated and logged to the oplog during replication to
    support replica sets with members that use different storage
    engines.

* - `weights`

  - document

  - Optional. For text indexes, a document that contains
    field and weight pairs. The weight is an integer ranging from 1 to
    99,999 and denotes the significance of the field relative to the
    other indexed fields in terms of the score. You can specify weights
    for some or all the indexed fields. See
    control-text-search-results to adjust the scores.
    The default value is `1`.

* - `default_language`

  - string

  - .. _createIndexes-default-language:

    Optional. For text indexes, the language that
    determines the list of stop words and the rules for the stemmer and
    tokenizer. See text-search-languages for the available
    languages and 
    /core/indexes/index-types/index-text/specify-text-index-language 
    for more information and examples. The default value is `english`.

* - `language_override`

  - string

  - Optional. For text indexes, the name of the field, in
    the collection's documents, that contains the override language for
    the document. The default value is `language`. See
    specify-language-field-text-index-example for an example.

* - `textIndexVersion`

  - integer

  - Optional. The `text` index version number. Users can use this option to
    override the default version number.

    For available versions, see text-index-versions.

* - `2dsphereIndexVersion`

  - integer

  - Optional. The `2dsphere` index version number. Users can use this option to
    override the default version number.

    For the available versions, see 2dsphere-v2.

* - `bits`

  - integer

  - Optional. For 2d indexes, the number of precision of the
    stored geohash value of the location data.

    The `bits` value ranges from 1 to 32 inclusive. The default value
    is `26`.

* - `min`

  - number

  - Optional. For 2d indexes, the lower inclusive boundary for
    the longitude and latitude values. The default value is `-180.0`.

* - `max`

  - number

  - Optional. For 2d indexes, the upper inclusive boundary for
    the longitude and latitude values. The default value is
    `180.0`.

* - `collation`

  - document

  - Optional. Specifies the collation for the index.

    Collation allows users to specify
    language-specific rules for string comparison, such as rules for
    lettercase and accent marks.

    If you have specified a collation at the collection level, then:

    - If you do not specify a collation when creating the index, MongoDB
      creates the index with the collection's default collation.

    - If you do specify a collation when creating the index, MongoDB
      creates the index with the specified collation.

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

* - `wildcardProjection`

  - document

  - Optional. 

    Allows users to include or exclude specific field paths from
    a wildcard index using the
    `{ "$**" : 1}` key pattern. This option is only 
    valid if creating a wildcard index on
    all document fields. You cannot specify this option if creating
    a wildcard index on a specific field path and its subfields, e.g.
    `{ "path.to.field.$**" : 1 }`

    The `wildcardProjection` option takes the following form:

    ```javascript
    wildcardProjection: {
      "path.to.field.a" : <value>,
      "path.to.field.b" : <value>
    }
    ```

    The `<value>` can be either of the following:

    - `1` or `true` to include the field in the wildcard index.

    - `0` or `false` to exclude the field from the wildcard index. 

    Wildcard indexes omit the `_id` field by default. To include the
    `_id` field in the wildcard index, you must explicitly include it
    in the `wildcardProjection` document:

    ```json
    {
      "wildcardProjection" : {
        "_id" : 1,
        "<field>" : 0|1
      }
    }
    ```

    All of the statements in the `wildcardProjection` document must be
    either inclusion or exclusion statements. You can also include the
    `_id` field with exclusion statements. This is the only exception to
    the rule. 

       
       
       

`mongosh` provides the methods
`db.collection.createIndex()` and
`db.collection.createIndexes()` as wrappers for the
`createIndexes` command.

## Considerations

MongoDB disallows the creation of version 0 indexes. 

### Index Names

The `createIndexes` command and
`mongosh` helpers
`db.collection.createIndex()` and
`db.collection.createIndexes()` report an error if you
create an index with one name, and then try to create the same index
again but with another name.

```javascript
{
   "ok" : 0,
   "errmsg" : "Index with name: x_1 already exists with a different name",
   "code" : 85,
   "codeName" : "IndexOptionsConflict"
}
```

In previous versions, MongoDB did not create the index again, but
would return a response object with `ok` value of `1` and a note
that implied that the index was not recreated. For example:

```javascript
{
   "numIndexesBefore" : 2,
   "numIndexesAfter" : 2,
   "note" : "all indexes already exist",
   "ok" : 1
}
```

### Replica Sets and Sharded Clusters

**Note:** Requires `featureCompatibilityVersion` 4.4+

Each `mongod` in the replica set or sharded cluster
*must* have featureCompatibilityVersion set to at
least `4.4` to start index builds simultaneously across 
replica set members.

Index builds on a replica set or sharded cluster build simultaneously across 
all data-bearing replica set members. For sharded clusters, the index build 
occurs only on shards containing data for the collection being indexed. 
The primary requires a minimum number of data-bearing `voting` members (i.e commit quorum), including itself,
that must complete the build before marking the index as ready for
use. See index-operations-replicated-build for more
information.

To start an index build with a non-default commit quorum, specify the
commitQuorum.

Use the `setIndexCommitQuorum` command to modify the commit quorum 
of an in-progress index build. 

### Collation and Index Types

The following indexes only support simple binary comparison and do
not support collation:

- Text indexes

- 2d indexes

**Tip:**

To create a `text` or `2d` index on a collection that has a
non-simple collation, you must explicitly specify ``{collation:
{locale: "simple"} }`` when creating the index.

### Stable API

When using Stable API V1:

- You cannot specify any of the following fields in the `indexes` array:

  - `background`
  - `bucketSize`
  - `sparse`
  - `storageEngine`

- You cannot create text indexes.

- The above unsupported index types are ignored by the 
  query planner in 
  strict mode. For example, 
  attempting to use a `sparse` index with `cursor.hint()` 
  will result in the following `BadValue` error:

  ```
  planner returned error :: caused by :: hint provided does not 
  correspond to an existing index
  ```

## Behavior

### Concurrency

For featureCompatibilityVersion `"4.2"`, `createIndexes`
uses an optimized build process that obtains and holds an exclusive lock on
the specified collection at the start and end of the index build. All
subsequent operations on the collection must wait until `createIndexes` releases
the exclusive lock. `createIndexes` allows interleaving read and write
operations during the majority of the index build.

For featureCompatibilityVersion `"4.0"`, `createIndexes`
uses the pre-4.2 index build process which by default obtains an exclusive
lock on the parent database for the entire duration of the build process. The
pre-4.2 build process blocks all operations on the database *and* all its
collections until the operation completed. `background` indexes do not take
an exclusive lock.

For more information on the locking behavior of `createIndexes`, see
index-operations.

### Memory Usage Limit

`createIndexes` supports building one or more indexes on a collection.
`createIndexes` uses a combination of memory and temporary files on disk to 
build indexes. The default memory limit is 200 megabytes per `createIndexes` 
command, shared equally among all indexes built in that command. For example, if you 
build 10 indexes with one `createIndexes` command, MongoDB allocates each index 
20 megabytes for the index build process when using the default memory limit of 200. 
When you reach the memory limit, MongoDB creates temporary files in the `_tmp` subdirectory 
within `--dbpath` to complete the build.

Adjust the memory limit with the
`maxIndexBuildMemoryUsageMegabytes` parameter.
Increasing this parameter is only necessary in rare cases, such as when you run many
simultaneous index builds with a single `createIndexes` command
or when you index a data set larger than 500GB.

Each `createIndexes` command has a limit of `maxIndexBuildMemoryUsageMegabytes`.
When using the default `maxNumActiveUserIndexBuilds` of 3, the 
total memory usage for all concurrent index builds can reach up 
to 3 times the value of `maxIndexBuildMemoryUsageMegabytes`.

### Index Options

#### Non-Hidden Option

The hidden option can be changed
without dropping and recreating the index. See
createIndexes-hidden-option.

#### Changing Index Options

Collation options on an existing index can be updated. To change other 
index options, drop the existing index with 
`db.collection.dropIndex()` then run `createIndexes`
with the new options.

#### Collation Option

You can create multiple indexes on the same key(s) with different 
collations. To create indexes with the same key pattern but different
collations, you must supply unique index names.

If you have specified a collation at the collection level, then:

- If you do not specify a collation when creating the index, MongoDB
  creates the index with the collection's default collation.

- If you do specify a collation when creating the index, MongoDB
  creates the index with the specified collation.

**Tip:**

By specifying a collation `strength` of `1` or `2`, you can
create a case-insensitive index. Index with a collation `strength`
of `1` is both diacritic- and case-insensitive.

To use an index for string comparisons, an operation must also
specify the same collation. That is, an index with a collation
cannot support an operation that performs string comparisons on the
indexed fields if the operation specifies a different collation.

**Warning:**

Collation-aware index keys might be larger than index keys for indexes 
without collation because indexes that are configured with collation use 
ICU collation keys to achieve sort order.

#### Hidden Option

To change the `hidden` option for existing indexes, you can use the
following `mongosh` methods:

- `db.collection.hideIndex()`

- `db.collection.unhideIndex()`

For example,

- To change the `hidden` option for an index to `true`, use the
  `db.collection.hideIndex()` method:

  ```javascript
  db.restaurants.hideIndex( { borough: 1, ratings: 1 } );
  ```

- To change the `hidden` option for an index to `false`, use the
  `db.collection.unhideIndex()` method:

  ```javascript
  db.restaurants.unhideIndex( { borough: 1, city: 1 } );
  ```

**See also:**

/core/index-hidden

### Wildcard Indexes

- .. include:: /includes/extracts/wildcard-index-id.rst

- .. include:: /includes/indexes/wildcard-restrictions.rst

To learn more, see:

- About Wildcard Indexes
- Wildcard Index Examples
- Wildcard Index Restrictions

### Transactions

You can create collections and indexes inside a distributed 
transaction if the
transaction is not a cross-shard write transaction.

To use `createIndexes` in a transaction, the transaction must use read
concern `"local"`. If you specify a read concern level
other than `"local"`, the transaction fails.

**See also:**

transactions-create-collections-indexes

### Commit Quorum Contrasted with Write Concern

There are important differences between commit quorums and write concerns:

- Index builds use **commit quorums**.
- Write operations use **write concerns**. 

Each data-bearing node in a cluster is a voting member.

The **commit quorum** specifies how many data-bearing voting members, or
which voting members, including the primary, must be prepared to commit
a simultaneous index build
before the primary will execute the commit.

The **write concern** is the level of acknowledgment that the write has
propagated to the specified number of instances.

The **commit quorum** specifies how many nodes must be *ready* to finish
the index build before the primary commits the index build. In contrast,
when the primary has committed the index build, the **write concern**
specifies how many nodes must *finish* the index build before the
command returns.

## Example

The following command builds two indexes on the `inventory` collection of
the `products` database:

```javascript
db.getSiblingDB("products").runCommand(
  {
    createIndexes: "inventory",
    indexes: [
        {
            key: {
                item: 1,
                manufacturer: 1,
                model: 1
            },
            name: "item_manufacturer_model",
            unique: true
        },
        {
            key: {
                item: 1,
                supplier: 1,
                model: 1
            },
            name: "item_supplier_model",
            unique: true
        }
    ],
    writeConcern: { w: "majority" }
  }
)
```

When the indexes successfully finish building, MongoDB returns a results
document that includes a status of `"ok" : 1`.

### Create a Wildcard Index

**Note:**

For complete documentation on Wildcard Indexes, see
wildcard-index-core.

The following lists examples of wildcard index creation:

- createIndexes-command-wildcard-onepath
- createIndexes-command-wildcard-allpaths
- createIndexes-command-wildcard-inclusion
- createIndexes-command-wildcard-exclusion

#### Create a Wildcard Index on a Single Field Path

Consider a collection `products_catalog` where documents may contain a
`product_attributes` field. The `product_attributes` field can
contain arbitrary nested fields, including embedded 
documents and arrays: 

```javascript
db.products_catalog.insertMany( [
  {
    _id : ObjectId("5c1d358bf383fbee028aea0b"),
    product_name: "Blaster Gauntlet",
    product_attributes: {
      price: {
        cost: 299.99,
        currency: "USD"
      }
    }
  },
  {
    _id: ObjectId("5c1d358bf383fbee028aea0c"),
    product_name: "Super Suit",
    product_attributes: {
      superFlight: true,
      resistance: [ "Bludgeoning", "Piercing", "Slashing" ]
    }
  }
] )
```

The following operation creates a wildcard index on the 
`product_attributes` field:

```bash
use inventory
db.runCommand(
  {
    createIndexes: "products_catalog",
    indexes: [
      {
        key: { "product_attributes.$**" : 1 },
        name: "wildcardIndex"
      }
    ]
  }
)
```

With this wildcard index, MongoDB indexes all scalar values of
`product_attributes`. If the field is a nested document or array, the
wildcard index recurses into the document/array and indexes all scalar
fields in the document/array.

The wildcard index can support arbitrary single-field queries on 
`product_attributes` or one of its nested fields:

```bash
db.products_catalog.find( { "product_attributes.superFlight" : true } )
db.products_catalog.find( { "product_attributes.maxSpeed" : { $gt : 20 } } )
db.products_catalog.find( { "product_attributes.elements" : { $eq: "water" } } )
```

**Note:**

The path-specific wildcard index syntax is incompatible with the
`wildcardProjection` option. See the parameter documentation for more
information.

#### Create a Wildcard Index on All Field Paths

Consider a collection `products_catalog` where documents may contain a
`product_attributes` field. The `product_attributes` field can
contain arbitrary nested fields, including embedded 
documents and arrays: 

```javascript
db.products_catalog.insertMany( [
  {
    _id : ObjectId("5c1d358bf383fbee028aea0b"),
    product_name: "Blaster Gauntlet",
    product_attributes: {
      price: {
        cost: 299.99,
        currency: "USD"
      }
    }
  },
  {
    _id: ObjectId("5c1d358bf383fbee028aea0c"),
    product_name: "Super Suit",
    product_attributes: {
      superFlight: true,
      resistance: [ "Bludgeoning", "Piercing", "Slashing" ]
    }
  }
] )
```

The following operation creates a wildcard index on all scalar fields
(excluding the `_id` field):

```bash
use inventory
db.runCommand(
  {
    createIndexes: "products_catalog",
    indexes: [
      {
        key: { "$**" : 1 },
        name: "wildcardIndex"
      }
    ]
  }
)
```

With this wildcard index, MongoDB indexes all scalar fields for each
document in the collection. If a given field is a nested document or
array, the wildcard index recurses into the document/array and indexes
all scalar fields in the document/array.

The created index can support queries on any arbitrary field 
within documents in the collection:

```bash
db.products_catalog.find( { "product_price" : { $lt : 25 } } )
db.products_catalog.find( { "product_attributes.elements" : { $eq: "water" } } )
```

**Note:**

Wildcard indexes omit the `_id` field by default. To include the
`_id` field in the wildcard index, you must explicitly include it
in the `wildcardProjection` document. See parameter documentation for
more information.

#### Create a Wildcard Index on Multiple Specific Field Paths

Consider a collection `products_catalog` where documents may contain a
`product_attributes` field. The `product_attributes` field can
contain arbitrary nested fields, including embedded 
documents and arrays: 

```javascript
db.products_catalog.insertMany( [
  {
    _id : ObjectId("5c1d358bf383fbee028aea0b"),
    product_name: "Blaster Gauntlet",
    product_attributes: {
      price: {
        cost: 299.99,
        currency: "USD"
      }
    }
  },
  {
    _id: ObjectId("5c1d358bf383fbee028aea0c"),
    product_name: "Super Suit",
    product_attributes: {
      superFlight: true,
      resistance: [ "Bludgeoning", "Piercing", "Slashing" ]
    }
  }
] )
```

The following operation creates a wildcard index and uses
the `wildcardProjection` option to include only scalar values of the
`product_attributes.elements` and `product_attributes.resistance`
fields in the index. 

```bash
use inventory
db.runCommand(
  {
    createIndexes: "products_catalog",
    indexes: [
      {
        key: { "$**" : 1 },
        "wildcardProjection" : {
          "product_attributes.elements" : 1,
          "product_attributes.resistance" : 1
        },
        name: "wildcardIndex"
      }
    ]
  }
)
```

While the key pattern `"$**"` covers all fields in the document, the
`wildcardProjection` field limits the index to only the included
fields and their nested fields.

If a field is a nested document or array, the wildcard
index recurses into the document/array and indexes all scalar fields in 
the document/array.

The created index can support queries on any scalar field
included in the `wildcardProjection`:

```bash
db.products_catalog.find( { "product_attributes.elements" : { $eq: "Water" } } )
db.products_catalog.find( { "product_attributes.resistance" : "Bludgeoning" } )
```

**Note:**

Wildcard indexes do not support mixing inclusion and exclusion
statements in the `wildcardProjection` document *except* when
explicitly including the `_id` field. For more information on
`wildcardProjection`, see the parameter documentation.

#### Create a Wildcard Index that Excludes Multiple Specific Field Paths

Consider a collection `products_catalog` where documents may contain a
`product_attributes` field. The `product_attributes` field can
contain arbitrary nested fields, including embedded 
documents and arrays: 

```javascript
db.products_catalog.insertMany( [
  {
    _id : ObjectId("5c1d358bf383fbee028aea0b"),
    product_name: "Blaster Gauntlet",
    product_attributes: {
      price: {
        cost: 299.99,
        currency: "USD"
      }
    }
  },
  {
    _id: ObjectId("5c1d358bf383fbee028aea0c"),
    product_name: "Super Suit",
    product_attributes: {
      superFlight: true,
      resistance: [ "Bludgeoning", "Piercing", "Slashing" ]
    }
  }
] )
```

The following operation creates a wildcard index and uses
the `wildcardProjection` document to index all scalar fields
for each document in the collection, *excluding* the 
`product_attributes.elements` and `product_attributes.resistance`
fields:

```bash
use inventory
db.runCommand(
  {
    createIndexes: "products_catalog",
    indexes: [
      {
        key: { "$**" : 1 },
        "wildcardProjection" : {
           "product_attributes.elements" : 0,
           "product_attributes.resistance" : 0
        },
        name: "wildcardIndex"
      }
    ]
  }
)
```

While the key pattern `"$**"` covers all fields in the document, the
`wildcardProjection` field excludes the specified fields from the
index.

If a field is a nested document or array, the wildcard
index recurses into the document/array and indexes all scalar fields in 
the document/array.

The created index can support queries on any scalar field **except**
those excluded by `wildcardProjection`:

```bash
db.products_catalog.find( { "product_attributes.maxSpeed" : { $gt: 25 } } )
db.products_catalog.find( { "product_attributes.superStrength" : true } )
```

**Note:**

Wildcard indexes do not support mixing inclusion and exclusion
statements in the `wildcardProjection` document *except* when
explicitly including the `_id` field. For more information on
`wildcardProjection`, see the parameter documentation.

### Create Index With Commit Quorum

**Note:** Requires `featureCompatibilityVersion` 4.4+

Each `mongod` in the replica set or sharded cluster
*must* have featureCompatibilityVersion set to at
least `4.4` to start index builds simultaneously across 
replica set members.

Index builds on a replica set or sharded cluster build simultaneously across 
all data-bearing replica set members. For sharded clusters, the index build 
occurs only on shards containing data for the collection being indexed. 
The primary requires a minimum number of data-bearing `voting` members (i.e commit quorum), including itself,
that must complete the build before marking the index as ready for
use. See index-operations-replicated-build for more
information.

To set the commit quorum, use
`createIndexes` to specify the `commitQuorum` value.

`commitQuorum` specifies how many data-bearing voting members, or
which voting members, including the primary, must be prepared to commit
the index build before the primary will execute the commit. The default
commit quorum is `votingMembers`, which means all data-bearing
members.

The following operation creates an index with a commit quorum of `"majority"`, or a 
simple majority of data-bearing members:

```javascript
db.getSiblingDB("examples").runCommand(
  { 
    createIndexes: "invoices",
    indexes: [
      { 
        key: { "invoices" : 1 },
        "name" : "invoiceIndex"
      }
    ],
    "commitQuorum" : "majority"
  }
)
```

The primary marks index build as ready only after a simple
majority of data-bearing voting members "vote" to commit the index
build. For more information on index builds and the voting process, see
index-operations-replicated-build.

## Output

The `createIndexes` command returns a document that indicates
the success of the operation. The document contains some but not all of
the following fields, depending on outcome:

**`createIndexes.createdCollectionAutomatically`**

If `true`, then the collection didn't exist and was created in the
process of creating the index.

**`createIndexes.numIndexesBefore`**

The number of indexes at the start of the command.

**`createIndexes.numIndexesAfter`**

The number of indexes at the end of the command.

**`createIndexes.ok`**

A value of `1` indicates the indexes are in place. A value of
`0` indicates an error.

**`createIndexes.note`**

This `note` is returned if an existing index or indexes already
exist. This indicates that the index was not created or changed.

**`createIndexes.errmsg`**

Returns information about any errors.

**`createIndexes.code`**

The error code representing the type of error.

### Output Example

The following code block illustrates an example of the `createIndexes` output on a
sharded cluster. On a sharded cluster, `createIndexes` outputs a `raw` embedded
document which contains a document for each shard the index is built on. The keys of the
`raw` embedded document are concantenations of shard id and the hostname and port of the
individual nodes that make up the shard.

```javascript
{
  raw: {
    'atlas-2m11gv-shard-1/atlas-2m11gv-shard-01-00.cpfgx.mongodb.net:27017,atlas-2m11gv-shard-01-01.cpfgx.mongodb.net:27017,atlas-2m11gv-shard-01-02.cpfgx.mongodb.net:27017': {
      numIndexesBefore: 3,
      numIndexesAfter: 5,
      createdCollectionAutomatically: false,
      commitQuorum: 'votingMembers',
      ok: 1
    },
    'atlas-2m11gv-shard-0/atlas-2m11gv-shard-00-00.cpfgx.mongodb.net:27017,atlas-2m11gv-shard-00-01.cpfgx.mongodb.net:27017,atlas-2m11gv-shard-00-02.cpfgx.mongodb.net:27017': {
      numIndexesBefore: 3,
      numIndexesAfter: 5,
      createdCollectionAutomatically: false,
      commitQuorum: 'votingMembers',
      ok: 1
    }
  },
  ok: 1,
  '$clusterTime': {
    clusterTime: Timestamp({ t: 1743624296, i: 7 }),
    signature: {
      hash: Binary.createFromBase64('22j0GK8SIK806T+0OdCY6qYHocM=', 0),
      keyId: Long('7438621020069560323')
    }
  },
  operationTime: Timestamp({ t: 1743624296, i: 7 })
}  
```
