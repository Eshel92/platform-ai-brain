<!-- Converted from reference/method/db.collection.createIndex.txt (reStructuredText). Includes are inlined. -->

# db.collection.createIndex()

This page documents a `mongosh` method. To see the equivalent
method in a MongoDB driver, see the corresponding page for your
programming language:

**`https://www.mongodb.com/docs/drivers/java/sync/current/fundamentals/indexes/`**

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

**`https://www.mongodb.com/docs/languages/cpp/cpp-driver/current/tutorial/#create-indexes`**

**`https://mongodb.github.io/mongo-swift-driver/docs/current/MongoSwift/Structs/MongoCollection.html#/s:10MongoSwift0A10CollectionV11createIndex_7options7sessionSSAA0E5ModelV_AA06CreateE7OptionsVSgAA13ClientSessionCSgtYaKF`**

## Definition

**`db.collection.createIndex(keys, options, commitQuorum)`**

Creates indexes on collections.

## Compatibility

This method is available in deployments hosted in the following 
environments:

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

The `createIndex()` method has the following
form:

```javascript
db.collection.createIndex( <keys>, <options>, <commitQuorum>)
```

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
operation will fail.

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
      operator),

    - `$exists: true` expression,

    - `$gt`, `$gte`, `$lt`, `$lte` expressions,

    - `$type` expressions,

    - `$and` operator,

    - `$or` operator, 

    - `$in` operator 

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

    **Tip:**

    Partial indexes offer a superset of the 
    functionality of sparse indexes.  Unless your application has a
    specific requirement, use partial indexes instead of sparse indexes.

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

### Option for Collation

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

- text indexes, 

- 2d indexes, and 

- geoHaystack indexes.

**Tip:**

To create a `text`, a `2d`, or a `geoHaystack` index on a
collection that has a non-simple collation, you must explicitly
specify `{collation: {locale: "simple"} }` when creating the
index.

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

### Options for `text` Indexes

The following options are available for text
indexes only:

| Parameter | Type | Description |
|---|---|---|
| `weights` | document | Optional. For text indexes, a document that contains field and weight pairs. The weight is an integer ranging from 1 to 99,999 and denotes the significance of the field relative to the other indexed fields in terms of the score. You can specify weights for some or all the indexed fields. See /tutorial/control-results-of-text-search to adjust the scores. The default value is `1`. Starting in MongoDB 5.0, the weights option is only allowed for text indexes. |
| `default_language` | string | Optional. For text indexes, the language that determines the list of stop words and the rules for the stemmer and tokenizer. See text-search-languages for the available languages and /tutorial/specify-language-for-text-index for more information and examples. The default value is `english`. |
| `language_override` | string | Optional. For text indexes, the name of the field, in the collection's documents, that contains the override language for the document. The default value is `language`. See specify-language-field-text-index-example for an example. |
| `textIndexVersion` | integer | Optional. The `text` index version number. Users can use this option to override the default version number. For available versions, see text-versions. |

       

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
| `min` | number | Optional. For 2d indexes, the lower inclusive boundary for the longitude and latitude values. The default value is `-180.0`. |
| `max` | number | Optional. For 2d indexes, the upper inclusive boundary for the longitude and latitude values. The default value is `180.0`. |

       
       

### Options for `geoHaystack` Indexes

The following option is available for geoHaystack
indexes only:

| Parameter | Type | Description |
|---|---|---|
| `bucketSize` | number | For geoHaystack indexes, specify the number of units within which to group the location values; i.e. group in the same bucket those location values that are within the specified number of units to each other. The value must be greater than 0. |

**Note:** Removed in MongoDB 5.0

MongoDB 5.0 removes the deprecated geoHaystack index and `geoSearch` command. Use a
2d index with `$geoNear` or one of the
supported geospatial query operators
instead.

Upgrading your MongoDB instance to 5.0 and setting
featureCompatibilityVersion to `5.0` will delete any
pre-existing geoHaystack indexes.

### Options for `wildcard` indexes

The following option is available for
wildcard indexes only:

* - Parameter

  - Type

  - Description

* - `wildcardProjection`

  - document

  - Optional. Allows users to include or exclude specific field paths from
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

       
       
       

## Behaviors

### Concurrency

**Changed in version:** 4.2

MongoDB uses an optimized build process that obtains and holds an exclusive 
lock on the specified collection at the start and end of the index build. All
subsequent operations on the collection must wait until `createIndex` releases
the exclusive lock. `createIndex` allows interleaving read and write
operations during the majority of the index build.

For more information on the locking behavior of `createIndex`, see
index-operations.

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

## Examples

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

The following example creates a compound index on the
`orderDate` field (in ascending order) and the `zipcode`
field (in descending order.)

```javascript
db.collection.createIndex( { orderDate: 1, zipcode: -1 } )
```

Compound indexes can include a single hashed field. 
Compound hashed indexes require featureCompatibilityVersion 
set to at least `5.0`.
   
The following example creates a compound index on the `state` field
(in ascending order) and the `zipcode` field (hashed):

```javascript
db.collection.createIndex( { "state" : 1, "zipcode" : "hashed" } )
```

The order of fields in a compound index is important for supporting
`sort()` operations using the index.

**See also:**

- sort-on-multiple-fields
- sort-index-prefix

### Create Indexes with Collation Specified

The following example creates an index named `category_fr`. The
example creates the index with the collation that specifies the locale `fr` and
comparison strength `2`:

```javascript
db.restaurants.createIndex(
   { category: 1 },
   { name: "category_fr", collation: { locale: "fr", strength: 2 } }
)
```

The following example creates a compound index named
`date_category_fr` with a collation.
The collation applies only to the index keys with string values.

```javascript
db.collection.createIndex(
   { orderDate: 1, category: 1 },
   { name: "date_category_fr", collation: { locale: "fr", strength: 2 } }
)
```

The collation applies to the indexed keys whose values are string.

For queries or sort operations on the indexed keys that uses the same
collation rules, MongoDB can use the index. The indexes use collation of
`strength: 2`, which results in case-insensitive queries when the
index is used. For details, see createIndex-collation-index-use.

### Create a Wildcard Index

**New in version:** 4.2

The `mongod` 
featureCompatibilityVersion must be `4.2` to
create wildcard indexes. For instructions on setting the fCV, see 
set-fcv.

- .. include:: /includes/extracts/wildcard-index-id.rst

- .. include:: /includes/extracts/wildcard-index-restrictions.rst

  For complete documentation on wildcard index restrictions, see 
  wildcard-index-restrictions.

For complete documentation on Wildcard Indexes, see 
wildcard-index-core.

The following lists examples of wildcard index creation:

- createIndex-method-wildcard-onepath
- createIndex-method-wildcard-allpaths
- createIndex-method-wildcard-inclusion
- createIndex-method-wildcard-exclusion

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
db.products_catalog.createIndex( { "product_attributes.$**" : 1 } )
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
db.products_catalog.find( { "product_attributes.elements" : { $eq: "water" } } )
```

**Note:**

Wildcard indexes omit the `_id` field by default. To include the
`_id` field in the wildcard index, you must explicitly include it
in the `wildcardProjection` document. See parameter documentation for
more information.

#### Include Specific Fields in Wildcard Index Coverage

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
db.products_catalog.createIndex(
  { "$**" : 1 },
  {
    "wildcardProjection" : {
      "product_attributes.elements" : 1,
      "product_attributes.resistance" : 1
    }
  }
)
```

While the key pattern `"$**"` covers all fields in the document, the
`wildcardProjection` field limits the index to only the included
fields. For complete documentation on `wildcardProjection`, see 
createIndex-method-wildcard-option.

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

#### Omit Specific Fields from Wildcard Index Coverage

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
db.products_catalog.createIndex(
  { "$**" : 1 },
  {
    "wildcardProjection" : {
      "product_attributes.elements" : 0,
      "product_attributes.resistance" : 0
    }
  }
)
```

While the key pattern `"$**"` covers all fields in the document, the
`wildcardProjection` field excludes the specified fields from the
index. For complete documentation on `wildcardProjection`, see 
createIndex-method-wildcard-option.

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

Specify the commitQuorum
parameter to the `createIndex()` operation to set
the minimum number of data-bearing voting members (i.e commit
quorum), including the primary, which must complete the
index build before the primary marks the indexes as ready. The default
commit quorum is `votingMembers`, or all data-bearing voting replica
set members.

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

- /core/index-text for details on creating `text`
  indexes.

- index-feature-geospatial for geospatial queries.

- index-feature-ttl for expiration of data.
