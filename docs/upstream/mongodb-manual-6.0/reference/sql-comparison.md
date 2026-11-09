<!-- Converted from reference/sql-comparison.txt (reStructuredText). Includes are inlined. -->

# SQL to MongoDB Mapping Chart

In addition to the charts that follow, you might want to consider the
/faq section for a selection of common questions about MongoDB.

## Terminology and Concepts

The following table presents the various SQL terminology and concepts
and the corresponding MongoDB terminology and concepts.

| SQL Terms/Concepts | MongoDB Terms/Concepts |
|---|---|
| database | database |
| table | collection |
| row | document or BSON document |
| column | field |
| index | index |
| table joins | `$lookup`, embedded documents |
| primary key Specify any unique column or column combination as primary key. | primary key In MongoDB, the primary key is automatically set to the _id field. |
| aggregation (e.g. group by) | aggregation pipeline See the /reference/sql-aggregation-comparison. |
| SELECT INTO NEW_TABLE | `$out` See the /reference/sql-aggregation-comparison. |
| MERGE INTO TABLE | `$merge` See the /reference/sql-aggregation-comparison. |
| UNION ALL | `$unionWith` |
| transactions | transactions For many scenarios, the denormalized data model (embedded documents and arrays) will continue to be optimal for your data and use cases instead of multi-document transactions. That is, for many scenarios, modeling your data appropriately will minimize the need for multi-document transactions. |

## Executables

The following table presents some database executables and the
corresponding MongoDB executables. This table is *not* meant to be
exhaustive.

|  | MongoDB | MySQL | Oracle | Informix | DB2 |
|---|---|---|---|---|---|
| Database Server | `mongod` | `mysqld` | `oracle` | `IDS` | `DB2 Server` |
| Database Client | `mongosh` | `mysql` | `sqlplus` | `DB-Access` | `DB2 Client` |

## Examples

The following table presents the various SQL statements and the
corresponding MongoDB statements. The examples in the table assume the
following conditions:

- The SQL examples assume a table named `people`.

- The MongoDB examples assume a collection named `people` that contain
  documents of the following prototype:

  ```javascript
  {
    _id: ObjectId("509a8fb2f3f4948bd2f983a0"),
    user_id: "abc123",
    age: 55,
    status: 'A'
  }
  ```

### Create and Alter

The following table presents the various SQL statements related to
table-level actions and the corresponding MongoDB statements.

* - SQL Schema Statements

  - MongoDB Schema Statements

* - .. code-block:: sql
       :copyable: false

       CREATE TABLE people (
           id MEDIUMINT NOT NULL
               AUTO_INCREMENT,
           user_id Varchar(30),
           age Number,
           status char(1),
           PRIMARY KEY (id)
       )

  - Implicitly created on first `insertOne()` or
    `insertMany()` operation. The primary key
    `_id` is automatically added if `_id` field is not specified.

    ```javascript
    db.people.insertOne( {
        user_id: "abc123",
        age: 55,
        status: "A"
     } )
    ```

    However, you can also explicitly create a collection:

    ```javascript
    db.createCollection("people")
    ```

* - .. code-block:: sql
       :copyable: false

       ALTER TABLE people
       ADD join_date DATETIME

  - Collections do not describe or enforce the structure of its
    documents; i.e. there is no structural alteration at the
    collection level.

    However, at the document level, `updateMany()`
    operations can add fields to existing documents using the
    `$set` operator.

    ```javascript
    db.people.updateMany(
        { },
        { $set: { join_date: new Date() } }
    )
    ```

* - .. code-block:: sql
       :copyable: false

       ALTER TABLE people
       DROP COLUMN join_date

  - Collections do not describe or enforce the structure of its
    documents; i.e. there is no structural alteration at the collection
    level.

    However, at the document level, `updateMany()`
    operations can remove fields from documents using the
    `$unset` operator.

    ```javascript
    db.people.updateMany(
        { },
        { $unset: { "join_date": "" } }
    )
    ```

* - .. code-block:: sql
       :copyable: false

       CREATE INDEX idx_user_id_asc
       ON people(user_id)

  - .. code-block:: javascript
       :copyable: false
       :emphasize-lines: 1

       db.people.createIndex( { user_id: 1 } )

* - .. code-block:: sql
       :copyable: false

       CREATE INDEX
              idx_user_id_asc_age_desc
       ON people(user_id, age DESC)

  - .. code-block:: javascript
       :copyable: false
       :emphasize-lines: 1

       db.people.createIndex( { user_id: 1, age: -1 } )

* - .. code-block:: sql
       :copyable: false

       DROP TABLE people

  - .. code-block:: javascript
       :copyable: false
       :emphasize-lines: 1

       db.people.drop()

For more information on the methods and operators used, see:

- `db.collection.insertOne()`
- `db.collection.insertMany()`
- `db.createCollection()`
- `db.collection.updateMany()`
- `db.collection.createIndex()`
- `db.collection.drop()`
- `$set`
- `$unset`

**See also:**

- /core/databases-and-collections
- /core/document
- Indexes
- /core/data-models.

### Insert

The following table presents the various SQL statements related to
inserting records into tables and the corresponding MongoDB statements.

| SQL INSERT Statements | MongoDB insertOne() Statements |
|---|---|
| .. code-block:: sql :copyable: false INSERT INTO people(user_id, age, status) VALUES ("bcd001", 45, "A") | .. code-block:: javascript :copyable: false :emphasize-lines: 2 db.people.insertOne( { user_id: "bcd001", age: 45, status: "A" } ) |

For more information, see `db.collection.insertOne()`.

**See also:**

- /tutorial/insert-documents
- `db.collection.insertMany()`
- /core/databases-and-collections
- /core/document

### Select

The following table presents the various SQL statements related to
reading records from tables and the corresponding MongoDB statements.

**Note:**

The `find()` method always includes the `_id`
field in the returned documents unless specifically excluded through
projection. Some of the SQL queries below may include an
`_id` field to reflect this, even if the field is not included in the
corresponding `find()` query.

* - SQL SELECT Statements

  - MongoDB find() Statements

* - .. code-block:: sql
       :copyable: false

       SELECT *
       FROM people

  - .. code-block:: javascript
       :copyable: false

       db.people.find()

* - .. code-block:: sql
       :copyable: false

       SELECT id,
              user_id,
              status
       FROM people

  - .. code-block:: javascript
       :emphasize-lines: 3
       :copyable: false

       db.people.find(
           { },
           { user_id: 1, status: 1 }
       )

* - .. code-block:: sql
       :copyable: false

       SELECT user_id, status
       FROM people

  - .. code-block:: javascript
       :emphasize-lines: 3
       :copyable: false

       db.people.find(
           { },
           { user_id: 1, status: 1, _id: 0 }
       )

* - .. code-block:: sql
       :copyable: false

       SELECT *
       FROM people
       WHERE status = "A"

  - .. code-block:: javascript
       :emphasize-lines: 2
       :copyable: false

       db.people.find(
           { status: "A" }
       )

* - .. code-block:: sql
       :copyable: false

       SELECT user_id, status
       FROM people
       WHERE status = "A"

  - .. code-block:: javascript
       :copyable: false

       db.people.find(
           { status: "A" },
           { user_id: 1, status: 1, _id: 0 }
       )

* - .. code-block:: sql
       :copyable: false

       SELECT *
       FROM people
       WHERE status != "A"

  - .. code-block:: javascript
       :copyable: false

       db.people.find(
           { status: { $ne: "A" } }
       )

* - .. code-block:: sql
       :copyable: false

       SELECT *
       FROM people
       WHERE status = "A"
       AND age = 50

  - .. code-block:: javascript
       :copyable: false

       db.people.find(
           { status: "A",
             age: 50 }
       )

* - .. code-block:: sql
       :copyable: false

       SELECT *
       FROM people
       WHERE status = "A"
       OR age = 50

  - .. code-block:: javascript
       :copyable: false

       db.people.find(
           { $or: [ { status: "A" } , { age: 50 } ] }
       )

* - .. code-block:: sql
       :copyable: false

       SELECT *
       FROM people
       WHERE age > 25

  - .. code-block:: javascript
       :copyable: false

       db.people.find(
           { age: { $gt: 25 } }
       )

* - .. code-block:: sql
       :copyable: false

       SELECT *
       FROM people
       WHERE age < 25

  - .. code-block:: javascript
       :copyable: false

       db.people.find(
          { age: { $lt: 25 } }
       )

* - .. code-block:: sql
       :copyable: false

       SELECT *
       FROM people
       WHERE age > 25
       AND   age <= 50

  - .. code-block:: javascript
       :copyable: false

       db.people.find(
          { age: { $gt: 25, $lte: 50 } }
       )

* - .. code-block:: sql
       :copyable: false

       SELECT *
       FROM people
       WHERE user_id like "%bc%"

  - .. code-block:: javascript
       :copyable: false

       db.people.find( { user_id: /bc/ } )

    \-or-

    ```javascript
    db.people.find( { user_id: { $regex: /bc/ } } )
    ```

* - .. code-block:: sql
       :copyable: false

       SELECT *
       FROM people
       WHERE user_id like "bc%"

  - .. code-block:: javascript
       :copyable: false

       db.people.find( { user_id: /^bc/ } )

    \-or-

    ```javascript
    db.people.find( { user_id: { $regex: /^bc/ } } )
    ```

* - .. code-block:: sql
       :copyable: false

       SELECT *
       FROM people
       WHERE status = "A"
       ORDER BY user_id ASC

  - .. code-block:: javascript
       :copyable: false

       db.people.find( { status: "A" } ).sort( { user_id: 1 } )

* - .. code-block:: sql
       :copyable: false

       SELECT *
       FROM people
       WHERE status = "A"
       ORDER BY user_id DESC

  - .. code-block:: javascript
       :copyable: false

       db.people.find( { status: "A" } ).sort( { user_id: -1 } )

* - .. code-block:: sql
       :copyable: false

       SELECT COUNT(*)
       FROM people

  - .. code-block:: javascript
       :copyable: false

       db.people.count()

    *or*

    ```javascript
    db.people.find().count()
    ```

* - .. code-block:: sql
       :copyable: false

       SELECT COUNT(user_id)
       FROM people

  - .. code-block:: javascript
       :copyable: false

       db.people.count( { user_id: { $exists: true } } )

    *or*

    ```javascript
    db.people.find( { user_id: { $exists: true } } ).count()
    ```

* - .. code-block:: sql
       :copyable: false

       SELECT COUNT(*)
       FROM people
       WHERE age > 30

  - .. code-block:: javascript
       :copyable: false

       db.people.count( { age: { $gt: 30 } } )

    *or*

    ```javascript
    db.people.find( { age: { $gt: 30 } } ).count()
    ```

* - .. code-block:: sql
       :copyable: false

       SELECT DISTINCT(status)
       FROM people

  - .. code-block:: javascript
       :copyable: false

       db.people.aggregate( [ { $group : { _id : "$status" } } ] )

    or, for distinct value sets that do not exceed the BSON size limit

    ```javascript
    db.people.distinct( "status" )
    ```

* - .. code-block:: sql
       :copyable: false

       SELECT *
       FROM people
       LIMIT 1

  - .. code-block:: javascript
       :copyable: false

       db.people.findOne()

    *or*

    ```javascript
    db.people.find().limit(1)
    ```

* - .. code-block:: sql
       :copyable: false

       SELECT *
       FROM people
       LIMIT 5
       SKIP 10

  - .. code-block:: javascript
       :copyable: false

       db.people.find().limit(5).skip(10)

* - .. code-block:: sql
       :copyable: false

       EXPLAIN SELECT *
       FROM people
       WHERE status = "A"

  - .. code-block:: javascript
       :copyable: false

       db.people.find( { status: "A" } ).explain()

For more information on the methods and operators used, see

- `db.collection.find()`
- `db.collection.distinct()`
- `db.collection.findOne()`
- `limit()`
- `skip()`
- `explain()`
- `sort()`
- `count()`
- `$ne`
- `$and`
- `$or`
- `$gt`
- `$lt`
- `$exists`
- `$lte`
- `$regex`

**See also:**

- /tutorial/query-documents
- /reference/operator/query
- /reference/method

### Update Records

The following table presents the various SQL statements related to
updating existing records in tables and the corresponding MongoDB
statements.

| SQL Update Statements | MongoDB updateMany() Statements |
|---|---|
| .. code-block:: sql :copyable: false UPDATE people SET status = "C" WHERE age > 25 | .. code-block:: javascript :copyable: false db.people.updateMany( { age: { $gt: 25 } }, { $set: { status: "C" } } ) |
| .. code-block:: sql :copyable: false UPDATE people SET age = age + 3 WHERE status = "A" | .. code-block:: javascript :copyable: false db.people.updateMany( { status: "A" } , { $inc: { age: 3 } } ) |

For more information on the method and operators used in the examples, see:

- `db.collection.updateMany()`
- `$gt`
- `$set`
- `$inc`

**See also:**

- /tutorial/update-documents
- /reference/operator/update
- `db.collection.updateOne()`
- `db.collection.replaceOne()`

### Delete Records

The following table presents the various SQL statements related to
deleting records from tables and the corresponding MongoDB statements.

| SQL Delete Statements | MongoDB deleteMany() Statements |
|---|---|
| .. code-block:: sql :copyable: false DELETE FROM people WHERE status = "D" | .. code-block:: javascript :copyable: false db.people.deleteMany( { status: "D" } ) |
| .. code-block:: sql :copyable: false DELETE FROM people | .. code-block:: javascript :copyable: false db.people.deleteMany({}) |

For more information, see `db.collection.deleteMany()`.

**See also:**

- /tutorial/remove-documents
- `db.collection.deleteOne()`

## Further Reading

If you are considering migrating your SQL application to MongoDB,
download the [MongoDB Application Modernization Guide](https://www.mongodb.com/modernize?tck=docs_server).

The download includes the following resources:

- Presentation on the methodology of data modeling with MongoDB
- White paper covering best practices and considerations for
  migrating to MongoDB from an RDBMS data model
- Reference MongoDB schema with its RDBMS equivalent
- Application Modernization scorecard
