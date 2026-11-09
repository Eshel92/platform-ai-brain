<!-- Converted from reference/method/db.collection.createIndex.txt (reStructuredText). Includes are inlined. -->

# db.collection.createIndex() (mongosh method)

This page documents a `mongosh` method. To see the equivalent
method in a MongoDB driver, see the corresponding page for your
programming language:

**`https://www.mongodb.com/docs/drivers/java/sync/current/indexes/`**

**`https://www.mongodb.com/docs/drivers/csharp/current/fundamentals/indexes/`**

**`https://www.mongodb.com/docs/languages/python/pymongo-driver/current/work-with-indexes/`**

**`https://www.mongodb.com/docs/drivers/node/current/fundamentals/indexes/`**

**`https://www.mongodb.com/docs/drivers/go/current/fundamentals/indexes/`**

**`https://www.mongodb.com/docs/php-library/current/reference/method/MongoDBCollection-createIndex/`**

**`https://www.mongodb.com/docs/languages/c/c-driver/current/libmongoc/guides/manage-collection-indexes/`**

**`https://www.mongodb.com/docs/languages/scala/scala-driver/current/tutorials/indexes/`**

**`https://www.mongodb.com/docs/drivers/kotlin/coroutine/current/fundamentals/indexes/`**

**`https://motor.readthedocs.io/en/stable/api-tornado/motor_collection.html#motor.motor_tornado.MotorCollection.create_index`**

**`https://www.mongodb.com/docs/languages/kotlin/kotlin-sync-driver/current/work-with-indexes/`**

**`https://www.mongodb.com/docs/drivers/rust/current/fundamentals/indexes/`**

**`https://www.mongodb.com/docs/mongoid/current/reference/indexes/`**

**`https://www.mongodb.com/docs/languages/java/reactive-streams-driver/current/tutorials/indexes/`**

**`https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/indexes/`**

**`https://mongodb.github.io/mongo-swift-driver/docs/current/MongoSwift/Structs/MongoCollection.html#/s:10MongoSwift0A10CollectionV11createIndex_7options7sessionSSAA0E5ModelV_AA06CreateE7OptionsVSgAA13ClientSessionCSgtYaKF`**

## Definition

**`db.collection.createIndex(keys, options, commitQuorum)`**

Creates indexes on collections.

## Compatibility

This method is available in deployments hosted in the following 
environments:

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

The `createIndex()` method has the following
form:

```javascript
db.collection.createIndex( <keys>, <options>, <commitQuorum>)
```

### Parameters

The `createIndex()` method takes the following
parameters:

* - Parameter
  - Type
  - Description

* - `keys`
  - document
  - A document that contains the field and value pairs where the
    field is the index key and the value describes the type of
    index for that field.

    For an ascending index on a field, specify a value of `1`.
    For descending index, specify a value of `-1`.

    An asterisk (`*`) is not a valid index name.

    MongoDB supports several different index types, including:

    - text 
    - geospatial 
    - hashed indexes

    See index types for more information.

    Wildcard indexes
    support workloads where users query against custom fields or a
    large variety of fields in a collection.

    - You can create a wildcard index on a specific field and its
      subpaths or on all of the fields in a document.

      For details, see wildcard-index-core.

* - `options`
  - document
  - Optional. A document that contains a set of options that controls the creation
    of the index. See ensureIndex-options for details.

* - commitQuorum
  - integer or string
  - .. _createIndex-method-commitQuorum:

    Optional. The minimum number of data-bearing voting replica
    set members (i.e. commit quorum), including the primary, that
    must report a successful index build before the primary
    marks the `indexes` as ready. A "voting" member is any
    replica set member where `members[n].votes` is greater
    than `0`.

    Supports the following values:

    - `"votingMembers"` - all data-bearing voting replica set
      members (*Default*).

    - `"majority"` - a simple majority of data-bearing voting
      replica set members.

    - `<int>` - a specific number of data-bearing voting 
      replica set members.

    - `0` - Disables quorum-voting behavior. Members 
      start the index build simultaneously but do *not* 
      vote or wait for quorum before completing the 
      index build. If you start an index build with 
      a commit quorum of `0`, you cannot later modify the 
      commit quorum using `setIndexCommitQuorum`.

    - A replica set tag name.

## Options

The `options` document contains a set of options that controls the
creation of the index. Different index types can have additional
options specific for that type.

Multiple index options can be specified in the same document. However,
if you specify multiple option documents the `db.collection.createIndex()`
operation fails.

Consider the following `db.collection.createIndex()` operation:

```javascript
db.collection.createIndex(
  {
      "a": 1
  },
  {
      unique: true,
      sparse: true,
      expireAfterSeconds: 3600
  }
)
```

If the options specification had been split into multiple documents
like this:
`{ unique: true }, { sparse: true, expireAfterSeconds: 3600 }`
the index creation operation would have failed.

### Options for All Index Types

The following options are available for all index types unless
otherwise specified:

* - Parameter

  - Type

  - Description

* - `unique`

  - boolean

  - Optional. Creates a unique index so that the collection will not accept
    insertion or update of documents where the index key value
    matches an existing value in the index.

    Specify `true` to create a unique index. The
    default value is `false`.

    The option is *unavailable* for 
    hashed indexes.

* - `name`

  - string

  - Optional. The name of the index. If unspecified, MongoDB generates an index name
    by concatenating the names of the indexed fields and the sort order.

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

    For a compound index that includes `2dsphere` index keys and
    keys for other types, only the `2dsphere` index fields determine
    whether the index references a document.

    Partial indexes have a superset of the
    sparse index functionality. Unless your application has a specific
    requirement, use partial indexes instead of sparse indexes.

* - `expireAfterSeconds`

  - integer

  - .. include:: /includes/indexes/expireAfterSeconds-config-option.rst

    If you use TTL indexes created before MongoDB 5.0, or if you want to
    sync data created in MongDB 5.0 with a pre-5.0 installation, see
    expireData-warning to avoid misconfiguration issues.

    (Include not available offline: includes/expireAfterSeconds-range.rst)

* - hidden

  - boolean

  - .. _method-createIndex-hidden:

    Optional. A flag that determines whether the index is
    hidden from the query planner. A
    hidden index is not evaluated as part of the query plan
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

### Options for Collation

* - Parameter

  - Type

  - Description

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

       

The following indexes only support simple binary comparison and do
not support collation:

- Text indexes

- 2d indexes

**Tip:**

To create a `text` or `2d` index on a collection that has a
non-simple collation, you must explicitly specify ``{collation:
{locale: "simple"} }`` when creating the index.

#### Collation and Index Use

If you have specified a collation at the collection level, then:

- If you do not specify a collation when creating the index, MongoDB
  creates the index with the collection's default collation.

- If you do specify a collation when creating the index, MongoDB
  creates the index with the specified collation.

**Tip:**

By specifying a collation `strength` of `1` or `2`, you can
create a case-insensitive index. Index with a collation `strength`
of `1` is both diacritic- and case-insensitive.

You can create multiple indexes on the same key(s) with different 
collations. To create indexes with the same key pattern but different
collations, you must supply unique index names.

To use an index for string comparisons, an operation must also
specify the same collation. That is, an index with a collation
cannot support an operation that performs string comparisons on the
indexed fields if the operation specifies a different collation.

**Warning:**

Collation-aware index keys might be larger than index keys for indexes 
without collation because indexes that are configured with collation use 
ICU collation keys to achieve sort order.

### Options for `text` Indexes

The following options are available for text
indexes only:

| Parameter | Type | Description |
|---|---|---|
| `weights` | document | Optional. For text indexes, a document that contains field and weight pairs. The weight is an integer ranging from 1 to 99,999 and denotes the significance of the field relative to the other indexed fields in terms of the score. You can specify weights for some or all the indexed fields. See control-text-search-results to adjust the scores. The default value is `1`. Starting in MongoDB 5.0, the weights option is only allowed for text indexes. |
| `default_language` | string | Optional. For text indexes, the language that determines the list of stop words and the rules for the stemmer and tokenizer. See text-search-languages for the available languages and /core/indexes/index-types/index-text/specify-text-index-language for more information and examples. The default value is `english`. |
| `language_override` | string | Optional. For text indexes, the name of the field, in the collection's documents, that contains the override language for the document. The default value is `language`. See specify-language-field-text-index-example for an example. |
| `textIndexVersion` | integer | Optional. The `text` index version number. Users can use this option to override the default version number. For available versions, see text-index-versions. |

### Options for `2dsphere` Indexes

The following option is available for 2dsphere
indexes only:

| Parameter | Type | Description |
|---|---|---|
| `2dsphereIndexVersion` | integer | Optional. The `2dsphere` index version number. Users can use this option to override the default version number. For the available versions, see 2dsphere-v2. |

### Options for `2d` Indexes

The following options are available for 2d indexes
only:

| Parameter | Type | Description |
|---|---|---|
| `bits` | integer | Optional. For 2d indexes, the number of precision of the stored geohash value of the location data. The `bits` value ranges from 1 to 32 inclusive. The default value is `26`. |
| `min` | number | Optional. For `2d` indexes, the lower inclusive boundary for the longitude and latitude values. The default value is `-180.0`. |
| `max` | number | Optional. For `2d` indexes, the upper inclusive boundary for the longitude and latitude values. The default value is `180.0`. |

### Options for `wildcard` indexes

Wildcard indexes can use the
`wildcardProjection` option.

* - Parameter

  - Type

  - Description

* - `wildcardProjection`

  - document

  - Optional. Allows users to include or exclude specific field paths
    from a wildcard index.

    This option is only valid when you create a wildcard index on all document fields. You cannot specify
    the `wildcardProjection` option when you create a wildcard
    index on a specific field path and its subfields.

    `wildcardProjection` works with specifications like:

    ```javascript
    { "$**": 1 }  
    { "userID":, "$**": 1 }  
    ```

    However, you can't define an index that includes the same field in the
    wildcard fields and the regular (non-wildcard) fields. To define the
    index correctly, use a `wildcardProjection` to exclude duplicated
    fields from the wildcard pattern.

    `wildcardProjection` does not work with a specification like:

    ```javascript
     ``{ "path.to.field.$**" : 1 }``  
    ```

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

To learn more, see:

- About Wildcard Indexes
- Wildcard Index Restrictions
   

## Behaviors

### Recreating an Existing Index

If you call `db.collection.createIndex()` for an index that
already exists, MongoDB does not recreate the index.

### Index Options

#### Non-Collation and Non-Hidden Options

With the exception of the collation option, if you create an index with one
set of index options and then try to recreate the same index but with
different index options, MongoDB will not change the options nor
recreate the index.

The hidden option can be changed
without dropping and recreating the index. See
method-createIndex-hidden-option.

To change the other index options, drop the existing index with
`db.collection.dropIndex()` before running
`db.collection.createIndex()` with the new options.

#### Collation Option

You can create multiple indexes on the same key(s) with different 
collations. To create indexes with the same key pattern but different
collations, you must supply unique index names.

#### Hidden Option

To hide or unhide existing indexes, you can use the following
`mongosh` methods:

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

### Transactions

You can create collections and indexes inside a distributed 
transaction if the
transaction is not a cross-shard write transaction.

To use `db.collection.createIndex()` in a transaction, the transaction must use read
concern `"local"`. If you specify a read concern level
other than `"local"`, the transaction fails.

**See also:**

transactions-create-collections-indexes

#### Commit Quorum

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
`createIndex()` to specify the `commitQuorum` value.

`commitQuorum` specifies how many data-bearing voting members, or
which voting members, including the primary, must be prepared to commit
the index build before the primary will execute the commit. The default
commit quorum is `votingMembers`, which means all data-bearing
members.

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

**Note:**

Documents in the `movies` collection contain additional fields not 
shown here.

### Create an Ascending Index on a Single Field

The following example creates an ascending index on the field
`orderDate`.

```javascript
db.collection.createIndex( { orderDate: 1 } )
```

If the `keys` document specifies more than one field, then
`createIndex()` creates a compound
index.

### Create an Index on a Multiple Fields

The following example creates a compound index on the `year`, `runtime`, and
`title` fields:

```javascript
db.movies.createIndex( { year: 1, runtime: 1, title: 1 } )
```

   
The following example creates a compound index on the `state` field
(in ascending order) and the `zipcode` field (hashed):

```javascript
db.collection.createIndex( { "state" : 1, "zipcode" : "hashed" } )
```

For more information on hashed indexes, see index-type-hashed.

### Create Indexes with Collation

Use the following code to create an index on the `movies` collection of the
`sample_mflix` database with the collation locale `"fr"` for string 
comparisons:

```javascript
db.movies.createIndex( { title: 1 }, { collation: { locale: "fr" } } )
```

The following query, which specifies the same collation as the index,
can use the index:

```javascript
db.movies.find( 
    { title: "Les Misèrables" },
    { title: 1, year: 1 }
).collation( { locale: "fr" } )
```

However, the following query operation, which by default uses the
"simple" binary collator, cannot use the index and requires a `COLLSCAN`.

```javascript
db.movies.find( { title: "Les Misèrables" }, { title: 1 , year: 1 } )
```

For a compound index where the index prefix keys are not strings,
arrays, and embedded documents, an operation that specifies a
different collation can still use the index to support comparisons
on the index prefix keys.

For example, you can use the following code to create a compound index on the
`movies` collection of the `sample_mflix` database specifying the 
numeric fields `year` and `metacritic` and the string field `title`. 
The index also specifies the collation locale `"fr"` for string 
comparisons:

```javascript
db.movies.createIndex(
    { year: 1, metacritic: 1, title: 1 },
    { collation: { locale: "fr" } }
)
```

The following operations, which use `"simple"` binary collation
for string comparisons, can use the index:

```javascript
db.movies.find( 
    { year: 2012 }, 
    { title: 1, year: 1, metacritic: 1 } 
).sort( { title: 1 } )
```

```javascript
db.movies.find( 
    { year: 2012, metacritic: { $gt: Decimal128( "50" ) } },
    { title: 1, year: 1, metacritic: 1 }
).sort( { title: 1 } )
```

The following operation, which uses `"simple"` binary collation
for string comparisons on the indexed `title` field, can use
the index to fulfill only the `year: 2012` portion of the query:

```javascript
db.movies.find( { year: 2012, title: "Les Misèrables" }, { year: 1, title: 1 } )
```

To confirm whether a query used an index, run the query with the
`explain()` option.

**Important:**

Matches against document keys, including embedded document keys, 
use simple binary comparison. This means that a query for a key  
like "type.café" will not match the key "type.cafe", regardless of
the value you set for the strength parameter.

### Create a Wildcard Index on a Single Field Path

```javascript
db.products_catalog.insertMany( [
  {
    _id : ObjectId("5c1d358bf383fbee028aea0b"),
    product_name: "Jeans",
    product_attributes: {
      price: {
        cost: 29.99,
        currency: "USD"
      }
    }
  },
  {
    _id: ObjectId("5c1d358bf383fbee028aea0c"),
    product_name: "Sweater",
    product_attributes: {
      washable: true,
      size: [ "small", "medium", "large" ]
    }
  }
] )
```

The following operation creates a wildcard index on the 
`product_attributes` field:

```bash
use inventory
db.products_catalog.createIndex( { "product_attributes.$**" : 1 } )
```

With this wildcard index, MongoDB indexes all scalar values of
`product_attributes`. If the field is a nested document or array, the
wildcard index recurses into the document/array and indexes all scalar
fields in the document/array.

The wildcard index can support arbitrary single-field queries on 
`product_attributes` or one of its nested fields:

```javascript
db.products_catalog.find( { "product_attributes.washable" : true } )
db.products_catalog.find( { "product_attributes.maxSize" : { $gt : 20 } } )
db.products_catalog.find( { "product_attributes.colors" : { $eq: "blue" } } )
```

### Create a Wildcard Index on All Field Paths

```javascript
db.products_catalog.insertMany( [
  {
    _id : ObjectId("5c1d358bf383fbee028aea0b"),
    product_name: "Jeans",
    product_attributes: {
      price: {
        cost: 29.99,
        currency: "USD"
      }
    }
  },
  {
    _id: ObjectId("5c1d358bf383fbee028aea0c"),
    product_name: "Sweater",
    product_attributes: {
      washable: true,
      size: [ "small", "medium", "large" ]
    }
  }
] )
```

The following operation creates a wildcard index on all scalar fields
(excluding the `_id` field):

```bash
use inventory
db.products_catalog.createIndex( { "$**" : 1 } )
```

With this wildcard index, MongoDB indexes all scalar fields for each
document in the collection. If a given field is a nested document or
array, the wildcard index recurses into the document/array and indexes
all scalar fields in the document/array.

The created index can support queries on any arbitrary field 
within documents in the collection:

```bash
db.products_catalog.find( { "product_price" : { $lt : 25 } } )
db.products_catalog.find( { "product_attributes.colors" : { $eq: "blue" } } )
```

#### Include Specific Fields in Wildcard Index Coverage

```javascript
db.products_catalog.insertMany( [
  {
    _id : ObjectId("5c1d358bf383fbee028aea0b"),
    product_name: "Jeans",
    product_attributes: {
      price: {
        cost: 29.99,
        currency: "USD"
      }
    }
  },
  {
    _id: ObjectId("5c1d358bf383fbee028aea0c"),
    product_name: "Sweater",
    product_attributes: {
      washable: true,
      size: [ "small", "medium", "large" ]
    }
  }
] )
```

The following operation creates a wildcard index and uses
the `wildcardProjection` option to include only scalar values of the
`product_attributes.colors` and `product_attributes.material`
fields in the index. 

```bash
use inventory
db.products_catalog.createIndex(
  { "$**" : 1 },
  {
    "wildcardProjection" : {
      "product_attributes.colors" : 1,
      "product_attributes.material" : 1
    }
  }
)
```

The pattern `"$**"` includes all fields in the document. Use the
`wildcardProjection` field to limit the index to fields you specify.
For complete documentation on `wildcardProjection`, see 
createIndex-method-wildcard-option.

If a field is a nested document or array, the wildcard index recurses
into it and indexes all scalar fields in the document or array.

The wildcard index supports queries on any scalar field included in
the `wildcardProjection`:

```javascript
db.products_catalog.find( { "product_attributes.colors" : { $eq: "Blue" } } )
db.products_catalog.find( { "product_attributes.material" : "Cotton" } )
```

**Note:**

Wildcard indexes do not support mixing inclusion and exclusion
statements in the `wildcardProjection` document *except* when
explicitly including the `_id` field. For more information on
`wildcardProjection`, see the parameter documentation.

#### Omit Specific Fields from Wildcard Index Coverage

```javascript
db.products_catalog.insertMany( [
  {
    _id : ObjectId("5c1d358bf383fbee028aea0b"),
    product_name: "Jeans",
    product_attributes: {
      price: {
        cost: 29.99,
        currency: "USD"
      }
    }
  },
  {
    _id: ObjectId("5c1d358bf383fbee028aea0c"),
    product_name: "Sweater",
    product_attributes: {
      washable: true,
      size: [ "small", "medium", "large" ]
    }
  }
] )
```

This example uses a wildcard index and a `wildcardProjection`
document to index the scalar fields for each document in the collection.

The wildcard index excludes the `product_attributes.colors` and
`product_attributes.material` fields:

```bash
use inventory
db.products_catalog.createIndex(
  { "$**" : 1 },
  {
    "wildcardProjection" : {
      "product_attributes.colors" : 0,
      "product_attributes.material" : 0
    }
  }
)
```

The wildcard pattern `"$**"` includes all of the fields in the
document. However, the `wildcardProjection` field excludes the
specified fields from the index.

For complete documentation on `wildcardProjection`, see 
createIndex-method-wildcard-option.

If a field is a nested document or array, the wildcard
index recurses into the document/array and indexes all scalar fields in 
the document/array.

The index can support queries on any scalar field **except** those
excluded by `wildcardProjection`:

```bash
db.products_catalog.find( { "product_attributes.maxSize" : { $gt: 25 } } )
db.products_catalog.find( { "product_attributes.washable" : true } )
```

**Note:**

Wildcard indexes do not support mixing inclusion and exclusion
statements in the `wildcardProjection` document *except* when
explicitly including the `_id` field. For more information on
`wildcardProjection`, see the parameter documentation.

### Create Index With Commit Quorum

The following operation creates an index with a commit quorum of `"majority"`, or a 
simple majority of data-bearing voting members:

```javascript
db.getSiblingDB("examples").invoices.createIndex(
  { "invoices" : 1 },
  { },
  "majority"
)
```

The primary marks index build as ready only after a simple
majority of data-bearing voting members "vote" to commit the index
build. For more information on index builds and the voting process, see
index-operations-replicated-build.

## Additional Information

- The /indexes section of this manual for full
  documentation of indexes and indexing in MongoDB.

- `db.collection.getIndexes()` to view the specifications of
  existing indexes for a collection.

- index-type-text for details on creating `text`
  indexes.

- index-feature-geospatial for geospatial queries.

- index-feature-ttl for expiration of data.
