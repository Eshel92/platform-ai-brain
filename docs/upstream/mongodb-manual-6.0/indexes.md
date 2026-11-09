<!-- Converted from indexes.txt (reStructuredText). Includes are inlined. -->

# Indexes

Indexes support efficient execution of queries in MongoDB. Without
indexes, MongoDB must scan every document in a collection to return
query results. If an appropriate index exists for a query, MongoDB uses
the index to limit the number of documents it must scan.

Although indexes improve query performance, adding an index has negative
performance impact for write operations. For collections with a high
write-to-read ratio, indexes are expensive because each insert must also
update any indexes.

## Use Cases

If your application is repeatedly running queries on the same fields,
you can create an index on those fields to improve performance. For
example, consider the following scenarios:

| Scenario | Index Type |
|---|---|
| A human resources department often needs to look up employees by employee ID. You can create an index on the employee ID field to improve query performance. | Single Field Index |
| A salesperson often needs to look up client information by location. Location is stored in an embedded object with fields like `state`, `city`, and `zipcode`. You can create an index on the `location` object to improve performance for queries on that object. When you create an index on an embedded document, only queries that specify the entire embedded document use the index. Queries on a specific field within the document do not use the index. | Single Field Index on an embedded document |
| A grocery store manager often needs to look up inventory items by name and quantity to determine which items are low stock. You can create a single index on both the `item` and `quantity` fields to improve query performance. | Compound Index |

## Get Started

You can create and manage indexes in [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server), with a driver
method, or with the MongoDB Shell. MongoDB Atlas is the fully
managed service for MongoDB deployments in the cloud.

### Create and Manage Indexes in MongoDB Atlas

For deployments hosted in MongoDB Atlas, you can create
and manage indexes with the MongoDB Atlas UI or the Atlas CLI. MongoDB Atlas
also includes a Performance Advisor that recommends indexes to improve
slow queries, ranks suggested indexes by impact, and recommends which
indexes to drop.

To learn how to create and manage indexes the MongoDB Atlas UI or the Atlas
CLI, see Create, View, Drop, and Hide Indexes.

To learn more about the MongoDB Atlas Performance Advisor, see
Monitor and Improve Slow Queries.

### Create and Manage Indexes with a Driver Method or the MongoDB Shell

You can create and manage indexes with a driver method or the MongoDB
Shell. To learn more, see the resources on this page.

## Details

Indexes are special data structures that store a small portion of the
collection's data set in an easy-to-traverse form. MongoDB indexes use a
B-tree data structure.

The index stores the value of a specific field or set of fields, ordered
by the value of the field. The ordering of the index entries supports
efficient equality matches and range-based query operations. In
addition, MongoDB can return sorted results by using the ordering in
the index.

The following diagram illustrates a query that selects and orders the
matching documents using an index:

(Figure: /images/index-for-sort.bakedsvg.svg)

Fundamentally, indexes in MongoDB are similar to indexes in other
database systems. MongoDB defines indexes at the collection
level and supports indexes on any field or sub-field of the documents
in a MongoDB collection.

## Default `_id` Index

MongoDB creates a unique index on the
_id field during the creation of a
collection. The `_id` index prevents clients from inserting two
documents with the same value for the `_id` field. You cannot drop
this index on the `_id` field.

**Note:**

In sharded clusters, if you do *not* use
the `_id` field as the shard key, then your application
**must** ensure the uniqueness of the values in the `_id` field
to prevent errors.  This is most-often done by using a standard
auto-generated ObjectId.

## Create an Index

----------

→ Use the **Select your language** drop-down menu in the
upper-right to set the language of the examples on this page.

----------

tabs:
  - id: shell
    content: |
      To create an index in the
      Mongo Shell, use
      `db.collection.createIndex()`.

      ```javascript
      db.collection.createIndex( <key and index type specification>, <options> )
      ```

      The following example creates a single key descending index on
      the `name` field:

      ```javascript
      db.collection.createIndex( { name: -1 } )
      ```

      The `db.collection.createIndex` method only
      creates an index if an index of the same specification does
      not already exist.

  - id: compass
    content: |

      **Important:**

      To create an index on a collection in MongoDB Compass,
      the collection must contain documents.

      To create an index in
      MongoDB Compass:

      **Step 1: Navigate to the collection for which you wish to create the index.**

      a. In the left-hand MongoDB Compass navigation pane, click the
         database that contains your desired collection.

      #. From the database view, click the target collection name.

      **Step 2: Click the Create Index button.**

      From the Indexes tab, click the
      Create Index button to bring up the
      Create Index dialog.

      **Step 3: Optional. Enter the index name.**

      In the dialog, enter the name of the index to create, or leave blank
      to have MongoDB create a default name for the index.

      **Step 4: Add fields to index.**

      To specify a key for the index, select the field and the index type.
      To index additional fields, click Add Another Field.

      **Step 5: Optional. Specify the index options.**

      Compass supports the following index options:

      * - Option
        - Description
        - More Information

      * - Build index in the background

        - If checked, ensure that the MongoDB deployment remains
          available during the index build operation.

        - Background Construction

      * - Create unique index

        - If checked, ensure that the indexed fields do not
          store duplicate values.

        - Unique Indexes

      * - Create TTL (Time to Live)

        - If checked, automatically delete documents after a
          specified number of seconds since the indexed field value.

        - TTL Indexes

      * - Partial filter expression

        - If checked, only index documents which match the specified
          filter expression.

          For example, the following partial filter expression only
          indexes documents where the `timezone` field exists:

          ```js
          { "timezone": { "$exists": true } } 
          ```

        - Partial Indexes

      * - Use custom collation

        - If checked, create a custom collation for the index
          using the options provided in Compass.

        - Collation Document

      * - Wildcard projection

        - If checked, support unknown or arbitrary fields
          which match the specified projection in the index.

        - wildcard-index-core

      **Step 6: Click Create to create the index.**

  - id: python
    content: |
      To create an index using the
      [PyMongo Python driver](https://pymongo.readthedocs.io/en/stable/index.html),
      use `pymongo.collection.Collection.create_index`.

      ```python
      db.collection.create_index([(<key and index type specification>)], <options> )
      ```

      The following example creates a single key descending index on
      the `name` field:

      ```python
      collection.create_index([("name", pymongo.DESCENDING)])
      ```

      The `pymongo.collection.Collection.create_index`
      method only creates an index if an index of the same
      specification does not already exist.

  - id: motor
    content: |
      To create an index using the
      [Motor driver](https://motor.readthedocs.io/en/stable/),
      use
      `motor.motor_asyncio.AsyncIOMotorCollection.create_index`.

      ```python
      await db.collection.create_index([(<key and index type specification>)], <options> )
      ```

      The following example creates a single key descending index on
      the `name` field:

      ```python
      await collection.create_index([("name", pymongo.DESCENDING)])
      ```

      The `motor.motor_asyncio.AsyncIOMotorCollection.create_index`
      method only creates an index if an index of the same
      specification does not already exist.

  - id: java-sync
    content: |
      To create an index using the
      [Java driver](https://mongodb.github.io/mongo-java-driver/),
      use
      [com.mongodb.client.MongoCollection.createIndex](http://mongodb.github.io/mongo-java-driver/3.4/javadoc/?com/mongodb/client/MongoCollection.html#createIndex-org.bson.conversions.Bson-).

      ```java
      collection.createIndex( <key and index type specification>, <options> )
      ```

      The following example creates a single key descending index on
      the `name` field:

      ```java
      collection.createIndex(Indexes.descending("name"));
      ```

      The [com.mongodb.client.MongoCollection.createIndex](http://mongodb.github.io/mongo-java-driver/3.4/javadoc/?com/mongodb/client/MongoCollection.html#createIndex-org.bson.conversions.Bson-).
      method only creates an index if an index of the same
      specification does not already exist.

  - id: java-async
    content: |
      To create an index using the
      [Async Java driver](http://mongodb.github.io/mongo-java-driver/3.0/driver-async/),
      use
      [com.mongodb.async.client.MongoCollection.createIndex](http://mongodb.github.io/mongo-java-driver/3.4/javadoc/?com/mongodb/async/client/MongoCollection.html#createIndex-org.bson.conversions.Bson-com.mongodb.async.SingleResultCallback-).

      ```java
      collection.createIndex( <key and index type specification>, <options>, <callbackFunction>)
      ```

      The following example creates a single key descending index on
      the `name` field:

      ```java
      collection.createIndex(Indexes.descending("name"), someCallbackFunction());
      ```

      The [com.mongodb.async.client.MongoCollection.createIndex](http://mongodb.github.io/mongo-java-driver/3.4/javadoc/?com/mongodb/async/client/MongoCollection.html#createIndex-org.bson.conversions.Bson-com.mongodb.async.SingleResultCallback-)
      method only creates an index if an index of the same
      specification does not already exist.

  - id: nodejs
    content: |
      To create an index using the
      [Node.JS driver](https://www.mongodb.com/docs/drivers/node/current/),
      use `createIndex()`.

      ```javascript
      collection.createIndex( { <key and index type specification> }, function(err, result) {
         console.log(result);
         callback(result);
      }
      ```

      The following example creates a single key descending index on
      the `name` field:

      ```javascript
       collection.createIndex( { name : -1 }, function(err, result) {
         console.log(result);
         callback(result);
      }
      ```

      The `createIndex()` method only creates an index if an index
      of the same specification does not already exist.

  - id: php
    content: |
      To create an index using the
      [PHP driver](https://www.mongodb.com/docs/php-library/current/), use
      `MongoDBCollection::createIndex()`.

      ```php
      $collection->createIndex(<key and index type specification>, <options>);
      ```

      The following example creates a single key descending index on
      the `name` field:

      ```php
      $collection->createIndex(['name' => -1]);
      ```

      The `MongoDBCollection::createIndex()`
      method only creates an index if an index of the same
      specification does not already exist.

  - id: perl
    content: |
      To create an index using the
      [Perl driver](http://search.cpan.org/dist/MongoDB/lib/MongoDB.pm),
      use
      [create_one()](https://metacpan.org/pod/MongoDB::Examples#CREATE-INDEX-myindexname-ON-users(name)).

      ```perl
      my $indexes = $db->get_collection( <collection> )->indexes;
      $indexes->create_one( [ <key and index type specification> ] );
      ```

      The following example creates a single key descending index on
      the `name` field:

      ```perl
      my $indexes = $db->get_collection( <collection> )->indexes;
      $indexes->create_one( [ name => -1 ] );
      ```

      The [create_one()](https://metacpan.org/pod/MongoDB::Examples#CREATE-INDEX-myindexname-ON-users(name))
      method only creates an index if an index of the same
      specification does not already exist.

  - id: ruby
    content: |
      To create an index using the
      [Ruby driver](https://www.mongodb.com/docs/ruby-driver/current/), use
      [Mongo::Index::View#create_one](http://www.rubydoc.info/github/mongodb/mongo-ruby-driver/Mongo%2FIndex%2FView%3Acreate_one).

      ```ruby
      client[:collection].indexes.create_one({ <key and index type specification> }, {options})
      ```

      The following example creates a single key descending index on
      the `name` field:

      ```ruby
      client[:collection].indexes.create_one({ name: -1 })
      ```

      The [Mongo::Index::View#create_one](http://www.rubydoc.info/github/mongodb/mongo-ruby-driver/Mongo%2FIndex%2FView%3Acreate_one)
      method only creates an index if an index of the same
      specification does not already exist.

  - id: scala
    content: |
      To create an index using the
      [Scala driver](http://mongodb.github.io/mongo-scala-driver/),
      use
      [org.mongodb.scala.model.Indexes](https://mongodb.github.io/mongo-scala-driver/1.0/scaladoc/index.html#org.mongodb.scala.model.Indexes$).

      ```scala
      collection.createIndex(<key and index type specification>)
      ```

      The following example creates a single key descending index on
      the `name` field:

      ```scala
      collection.createIndex(descending("name"))
      ```

      The [org.mongodb.scala.model.Indexes](https://mongodb.github.io/mongo-scala-driver/1.0/scaladoc/index.html#org.mongodb.scala.model.Indexes$)
      method only creates an index if an index of the same
      specification does not already exist.

  - id: csharp
    content: |
      To create an index using the
      [.NET driver](http://mongodb.github.io/mongo-csharp-driver/),
      use
      [MongoCollection.CreateIndex](http://api.mongodb.com/csharp/current/html/Overload_MongoDB_Driver_MongoCollection_CreateIndex.htm).

      ```csharp
      collection.CreateIndex( IndexKeys<collection>.<key and index type specification>, <options> );
      ```

      The following example creates a single key descending index on
      the `name` field:

      ```csharp
      collection.CreateIndex( IndexKeys<collection>.Descending("name") );
      ```

      The [MongoCollection.CreateIndex](http://api.mongodb.com/csharp/current/html/Overload_MongoDB_Driver_MongoCollection_CreateIndex.htm)
      method only creates an index if an index of the same
      specification does not already exist.

### Index Names

The default name for an index is the concatenation of the indexed keys
and each key's direction in the index ( i.e. 1 or -1) using underscores
as a separator. For example, an index created on 
`{ item : 1, quantity: -1 }` has the name `item_1_quantity_-1`.

You can create indexes with a custom name, such as one that is more 
human-readable than the default. For example, consider an application
that frequently queries the `products` collection to populate data on
existing inventory. The following `createIndex()`
method creates an index on `item` and `quantity` named ``query for
inventory``:

```javascript
db.products.createIndex( 
  { item: 1, quantity: -1 } , 
  { name: "query for inventory" } 
)
```

You can view index names using the `db.collection.getIndexes()`
method. You cannot rename an index once created. Instead, you must
drop and re-create the index with a new name. 

## Index Types

MongoDB provides a number of different index types to support specific
types of data and queries.

### Single Field

In addition to the MongoDB-defined `_id` index, MongoDB supports the
creation of user-defined ascending/descending indexes on a single
field of a document.

(Figure: /images/index-ascending.bakedsvg.svg)

For a single-field index and sort operations, the sort order (i.e.
ascending or descending) of the index key does not matter because
MongoDB can traverse the index in either direction.

See /core/index-single and sort-results-single-field for
more information on single-field indexes.

### Compound Index

MongoDB also supports user-defined indexes on multiple fields, i.e.
compound indexes.

The order of fields listed in a compound index has significance. For
instance, if a compound index consists of `{ userid: 1, score: -1 }`,
the index sorts first by `userid` and then, within each `userid`
value, sorts by `score`.

(Figure: /images/index-compound-key.bakedsvg.svg)

For compound indexes and sort operations, the sort order (i.e.
ascending or descending) of the index keys can determine whether the
index can support a sort operation. See
index-ascending-and-descending for more information on the
impact of index order on results in compound indexes.

See also:

- index-type-compound,
- sort-on-multiple-fields, and
- esr-indexing-rule 

### Multikey Index

MongoDB uses multikey indexes to index the
content stored in arrays. If you index a field that holds an array
value, MongoDB creates separate index entries for *every unique* element
of the array. These multikey indexes allow
queries to select documents that contain arrays by matching on element
or elements of the arrays. MongoDB automatically determines whether to
create a multikey index if the indexed field contains an array value;
you do not need to explicitly specify the multikey type.

(Figure: /images/index-multikey.bakedsvg.svg)

See /core/index-multikey and /core/multikey-index-bounds
for more information on multikey indexes.

### Geospatial Index

To support efficient queries of geospatial coordinate data, MongoDB
provides two special indexes: 2d indexes that uses
planar geometry when returning results and 2dsphere indexes that use spherical geometry to return results.

This index is a sparse index. If you want to
use a sparse index to create a compound index, first review the special considerations of using 
sparse compound indexes.

See index-feature-geospatial for a high level introduction to
geospatial indexes.

### Text Search Indexes

For data hosted on MongoDB Atlas, you can support full-text search with
Atlas Search indexes. To learn more, see Create an Atlas Search
Index.

For self-managed (non-Atlas) deployments, MongoDB provides a `text`
index type that supports searching for string content in a collection.
To learn more about self-managed text indexes, see
index-feature-text.

This index is a sparse index. If you want to
use a sparse index to create a compound index, first review the special considerations of using 
sparse compound indexes.

### Hashed Indexes

To support hash based sharding,
MongoDB provides a hashed index type,
which indexes the hash of the value of a field. These indexes have a
more random distribution of values along their range, but *only*
support equality matches and cannot support range-based queries.

### Clustered Indexes

Starting in MongoDB 5.3, you can create a collection with a
clustered index. Collections
created with a clustered index are called clustered collections.

See clustered-collections.

### Wildcard Indexes

Starting in MongoDB 4.2, you can use wildcard indexes to support
queries against multiple, arbitrary, or unknown fields. When you create
a wildcard index, you specify `$**` to represent all fields or all
values, allowing you to index any of the following with a single
command:

- All values of a field
- All fields in a document
- All fields in a document except specific field paths
- Multiple specific fields in a document

To learn more, see wildcard-index-core.

## Index Properties

### Unique Indexes

The unique property for an index causes
MongoDB to reject duplicate values for the indexed field. Other than
the unique constraint, unique indexes are functionally interchangeable
with other MongoDB indexes.

### Partial Indexes

Partial indexes only index the documents in
a collection that meet a specified filter expression. By indexing a
subset of the documents in a collection, partial indexes have lower
storage requirements and reduced performance costs for index creation
and maintenance.

Partial indexes offer a superset of the functionality of sparse indexes
and should be preferred over sparse indexes.

### Sparse Indexes

The sparse property of an index ensures
that the index only contain entries for documents that have the indexed
field. The index skips documents that *do not* have the indexed field.

You can combine the sparse index option with the unique index option
to prevent inserting documents that have duplicate values for the indexed
field(s) and skip indexing documents that lack the indexed field(s).

### TTL Indexes

TTL indexes are special indexes that MongoDB
can use to automatically remove documents from a collection after a
certain amount of time. This is ideal for certain types of information
like machine generated event data, logs, and session information that
only need to persist in a database for a finite amount of time.

See: /tutorial/expire-data for implementation instructions.

### Hidden Indexes

**New in version:** 4.4

Hidden indexes are not visible to the
query planner and cannot be used to support
a query.

By hiding an index from the planner, users can evaluate the potential
impact of dropping an index without actually dropping the index. If the
impact is negative, the user can unhide the index instead of having to
recreate a dropped index. And because indexes are fully maintained
while hidden, the indexes are immediately available for use once
unhidden.

Except for the `_id` index, you can hide any indexes.

## Index Use

Indexes can improve the efficiency of read operations. The
/tutorial/analyze-query-plan tutorial provides an example of the
execution statistics of a query with and without an index.

For information on how MongoDB chooses an index to use, see query
optimizer.

## Indexes and Collation

(Include not available offline: /includes/extracts/collation-versionadded.rst)

tabs:

  - id: shell
    content: |

  - id: compass
    content: |

      **Note:**

      The following examples illustrate indexes and collation in
      `mongosh`.

      Refer to the
      `MongoDB Compass Documentation` for instructions on using
      custom collation with indexes in Compass.

  - id: python
    content: |

      **Note:**

      The following examples illustrate indexes and collation in
      `mongosh`.

      Refer to your `driver documentation` for
      instructions on creating indexes with collation in your specific
      driver.

  - id: motor
    content: |

      **Note:**

      The following examples illustrate indexes and collation in
      `mongosh`.

      Refer to your `driver documentation` for
      instructions on creating indexes with collation in your specific
      driver.

  - id: java-sync
    content: |

      **Note:**

      The following examples illustrate indexes and collation in
      `mongosh`.

      Refer to your `driver documentation` for
      instructions on creating indexes with collation in your specific
      driver.

  - id: java-async
    content: |

      **Note:**

      The following examples illustrate indexes and collation in
      `mongosh`.

      Refer to your `driver documentation` for
      instructions on creating indexes with collation in your specific
      driver.

  - id: nodejs
    content: |

      **Note:**

      The following examples illustrate indexes and collation in
      `mongosh`.

      Refer to your `driver documentation` for
      instructions on creating indexes with collation in your specific
      driver.

  - id: php
    content: |

      **Note:**

      The following examples illustrate indexes and collation in
      `mongosh`.

      Refer to your `driver documentation` for
      instructions on creating indexes with collation in your specific
      driver.

  - id: perl
    content: |

      **Note:**

      The following examples illustrate indexes and collation in
      `mongosh`.

      Refer to your `driver documentation` for
      instructions on creating indexes with collation in your specific
      driver.

  - id: ruby
    content: |

      **Note:**

      The following examples illustrate indexes and collation in
      `mongosh`.

      Refer to your `driver documentation` for
      instructions on creating indexes with collation in your specific
      driver.

  - id: scala
    content: |

      **Note:**

      The following examples illustrate indexes and collation in
      `mongosh`.

      Refer to your `driver documentation` for
      instructions on creating indexes with collation in your specific
      driver.

  - id: csharp
    content: |

      **Note:**

      The following examples illustrate indexes and collation in
      `mongosh`.

      Refer to your `driver documentation` for
      instructions on creating indexes with collation in your specific
      driver.

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

For more information on collation, see the collation reference
page.

The following indexes only support simple binary comparison and do
not support collation:

- text indexes, 

- 2d indexes, and 

- geoHaystack indexes.

## Covered Queries

When the query criteria and the projection of a query include
*only* the indexed fields, MongoDB returns results directly from
the index *without* scanning any documents or bringing documents into
memory. These covered queries can be *very* efficient.

(Figure: /images/index-for-covered-query.bakedsvg.svg)

For more information on covered queries, see
read-operations-covered-query.

## Index Intersection

MongoDB can use the intersection of indexes to fulfill queries. For queries that
specify compound query conditions, if one index can fulfill a part of a
query condition, and another index can fulfill another part of the
query condition, then MongoDB can use the intersection of the two
indexes to fulfill the query. Whether the use of a compound index or
the use of an index intersection is more efficient depends on the
particular query and the system.

For details on index intersection, see /core/index-intersection.

## Restrictions

Certain restrictions apply to indexes, such as the length of the index
keys or the number of indexes per collection. See Index
Limitations for details.

## Additional Considerations

Although indexes can improve query performances, indexes also present
some operational considerations. See Operational Considerations
for Indexes for more information.

During index builds, applications may encounter reduced performance or
limited read/write access to the collection being indexed.

For more information on the index build process, see
index-operations, especially the
index-operations-replicated-build section.

Some drivers use `NumberLong(1)` instead of `1` to specify the index
order. The resulting indexes are the same.
