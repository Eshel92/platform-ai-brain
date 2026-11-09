<!-- Converted from reference/command/createIndexes.txt (reStructuredText). Includes are inlined. -->

# createIndexes

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

    Starting in MongoDB v5.0, you can resume some
    interupted index builds
    when the
    `commit quorum is set` to
    `"votingMembers"`. 

    Replica set nodes in a commit quorum must have `members[n].buildIndexes` 
    set to `true`. If any voting nodes have `members[n].buildIndexes` 
    set to `false`, you can't use the default `"votingMembers"` commit 
    quorum. Either configure all nodes with `members[n].buildIndexes` 
    set to `true`, or select a different commit quorum.  

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

  - 
    Specifies the index's fields. For each field, specify a key-value pair
    in which the key is the name of the field to index and the value is
    either the index direction or index type. If
    specifying direction, specify `1` for ascending or `-1` for
    descending.

    MongoDB supports several different index types including
    text, geospatial, and hashed indexes. See index types
    for more information.

    **Changed in version:** 4.2

    MongoDB 4.2 wildcard indexes
    support workloads where users query against custom fields or a
    large variety of fields in a collection:

    - To create a wildcard index on all fields and subfields in a 
      document, specify `{ "$**" : 1 }` as the index key. You
      cannot specify a descending index key when creating a wildcard
      index.

      You can also either include *or* exclude specific fields and
      their subfields from the index using the optional
      `wildcardProjection` parameter.

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

      With the exception of explicitly including  `_id` field, you cannot
      combine inclusion and exclusion statements in the
      `wildcardProjection` document.

    - You can create a wildcard index on a specific field
      and its subpaths by specifying the full path to that field as the
      index key and append `"$**"` to the path:

      `{ "path.to.field.$**" : 1 }` 

      You cannot specify a descending index key when creating a
      wildcard index.

      The path-specific wildcard index syntax is incompatible with the
      `wildcardProjection` option. You cannot specify additional
      inclusions or exclusions on the specified path.

    The wildcard index key **must** use one of the syntaxes listed
    above. For example, you cannot specify a
    compound index key.  For more 
    complete documentation on wildcard indexes, including restrictions 
    on their creation, see wildcard-index-restrictions.

    The `mongod` 
    featureCompatibilityVersion must be `4.2` to
    create wildcard indexes. For instructions on setting the fCV, see 
    set-fcv.

    For examples of wildcard index creation, see 
    createIndexes-command-wildcard-examples.

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
      operator),

    - `$exists: true` expression,

    - `$gt`, `$gte`, `$lt`, `$lte` expressions,

    - `$type` expressions,

    - `$and` operator,

    - `$or` operator, 

    - `$in` operator 

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
    - geoHaystack
    - text

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
    /tutorial/control-results-of-text-search to adjust the scores.
    The default value is `1`.

* - `default_language`

  - string

  - Optional. For text indexes, the language that
    determines the list of stop words and the rules for the stemmer and
    tokenizer. See text-search-languages for the available
    languages and /tutorial/specify-language-for-text-index for
    more information and examples. The default value is `english`.

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

    For available versions, see text-versions.

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
    the longitude and latitude values. The default value is `180.0`.

* - `bucketSize`

  - number

  - For geoHaystack indexes, specify the
    number of units within which to group the location values; i.e. group
    in the same bucket those location values that are within the
    specified number of units to each other.

    The value must be greater than 0.

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

    With the exception of explicitly including  `_id` field, you cannot
    combine inclusion and exclusion statements in the
    `wildcardProjection` document.

       
       
       

`mongosh` provides the methods
`db.collection.createIndex()` and
`db.collection.createIndexes()` as wrappers for the
`createIndexes` command.

## Considerations

MongoDB disallows the creation of version 0 indexes. 

### Index Names

**Note:** Changed in MongoDB 4.2

MongoDB removes the index name length limit of 127 byte maximum. 

Starting in version 4.2, the `createIndexes` command and
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

- text indexes, 

- 2d indexes, and 

- geoHaystack indexes.

**Tip:**

To create a `text`, a `2d`, or a `geoHaystack` index on a
collection that has a non-simple collation, you must explicitly
specify `{collation: {locale: "simple"} }` when creating the
index.

### Stable API

When using Stable API V1:

- You cannot specify any of the following fields in the `indexes` array:

  - `background`
  - `bucketSize`
  - `sparse`
  - `storageEngine`

- You cannot create geoHaystack or
  text indexes.

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

**Changed in version:** 4.2

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

`createIndexes` supports building one or more indexes on a
collection. `createIndexes` uses a combination of memory and
temporary files on disk to complete index builds. The default limit on
memory usage for `createIndexes` is 200 megabytes,
shared between all indexes built using a single
`createIndexes` command. Once the memory limit is reached,
`createIndexes` uses temporary disk files in a subdirectory
named `_tmp` within the `--dbpath`
directory to complete the build.

You can override the memory limit by setting the
`maxIndexBuildMemoryUsageMegabytes` server parameter.
Setting a higher memory limit may result in faster completion of index
builds. However, setting this limit too high relative to the unused RAM
on your system can result in memory exhaustion and server shutdown.

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

Because indexes that are configured with collation use ICU
collation keys to achieve sort order, collation-aware index keys
may be larger than index keys for indexes without collation. 

A `restaurants` collection has the following documents:

```javascript
db.restaurants.insertMany( [
   { _id: 1, category: "café", status: "Open" },
   { _id: 2, category: "cafe", status: "open" },
   { _id: 3, category: "cafE", status: "open" }
] )
```

The `restaurants` collection has an index on a string field
`category` with the collation locale `"fr"`.

```javascript
db.restaurants.createIndex( { category: 1 }, { collation: { locale: "fr" } } )
```

The following query, which specifies the same collation as the index,
can use the index:

```javascript
db.restaurants.find( { category: "cafe" } ).collation( { locale: "fr" } )
```

However, the following query operation, which by default uses the
"simple" binary collator, cannot use the index:

```javascript
db.restaurants.find( { category: "cafe" } )
```

For a compound index where the index prefix keys are not strings,
arrays, and embedded documents, an operation that specifies a
different collation can still use the index to support comparisons
on the index prefix keys.

For example, the collection `restaurants` has a compound index on the
numeric fields `score` and `price` and the string field
`category`; the index is created with the  collation locale
`"fr"` for string comparisons:

```javascript
db.restaurants.createIndex(
   { score: 1, price: 1, category: 1 },
   { collation: { locale: "fr" } } )
```

The following operations, which use `"simple"` binary collation
for string comparisons, can use the index:

```javascript
db.restaurants.find( { score: 5 } ).sort( { price: 1 } )
db.restaurants.find( { score: 5, price: { $gt: NumberDecimal( "10" ) } } ).sort( { price: 1 } )
```

The following operation, which uses `"simple"` binary collation
for string comparisons on the indexed `category` field, can use
the index to fulfill only the `score: 5` portion of the query:

```javascript
db.restaurants.find( { score: 5, category: "cafe" } )
```

To confirm whether a query used an index, run the query with the
`explain()` option.

**Important:**

Matches against document keys, including embedded document keys, 
use simple binary comparison. This means that a query for a key  
like "type.café" will not match the key "type.cafe", regardless of
the value you set for the strength parameter.

#### Hidden Option

**Note:**

To hide an index, you must have featureCompatibilityVersion set to `4.4` or greater. However, once hidden, the
index remains hidden even with featureCompatibilityVersion set to `4.2` on MongoDB 4.4 binaries.

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

**New in version:** 4.2

- .. include:: /includes/extracts/wildcard-index-id.rst

- .. include:: /includes/extracts/wildcard-index-fcv.rst

- .. include:: /includes/extracts/wildcard-index-restrictions.rst

  For complete documentation on wildcard index restrictions, see 
  wildcard-index-restrictions.

For examples of wildcard index creation, see
createIndexes-command-wildcard-examples.  For complete 
documentation on Wildcard Indexes, see wildcard-index-core.

### Transactions

You can create collections and indexes inside a distributed 
transaction if the
transaction is not a cross-shard write transaction.

To use `createIndexes` in a transaction, the transaction must use read
concern `"local"`. If you specify a read concern level
other than `"local"`, the transaction fails.

**See also:**

transactions-create-collections-indexes

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

**New in version:** 4.2

The `mongod` 
featureCompatibilityVersion must be `4.2` to
create wildcard indexes. For instructions on setting the fCV, see 
set-fcv.

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

Specify the commitQuorum option
to the `createIndexes` operation to set the minimum
number of data-bearing voting members (i.e commit quorum), including the
primary, which must complete the index build before the
primary marks the indexes as ready. The default commit quorum is
`votingMembers`, or all data-bearing replica set members.

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
