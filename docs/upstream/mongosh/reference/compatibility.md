<!-- Converted from reference/compatibility.txt (reStructuredText). Includes are inlined. -->

# Compatibility Changes with Legacy mongo Shell

This page describes differences between `mongosh` and the legacy
`mongo` shell. In addition to the alternatives listed here, you can
use the [mongocompat](https://github.com/mongodb-labs/mongosh-snippets/blob/main/snippets/mongocompat/)
snippet to access to legacy `mongo` shell APIs. Snippets are an
experimental feature, for more information, see snip-overview.

```shell
snippet install mongocompat
```

## Deprecated Methods

The following shell methods are deprecated in `mongosh`. Instead, use
the methods listed in the Alternative Resources column.

* - Deprecated Method
  - Alternative Resources
* - `db.collection.copyTo()`
  -   Aggregation stage: `$out`
* - `db.collection.count()`
  - - `db.collection.countDocuments()`
    - `db.collection.estimatedDocumentCount()`
* - `db.collection.insert()`
  - - `db.collection.insertOne()`
    - `db.collection.insertMany()`
    - `db.collection.bulkWrite()`
* - `db.collection.remove()`
  - - `db.collection.deleteOne()`
    - `db.collection.deleteMany()`
    - `db.collection.findOneAndDelete()`
    - `db.collection.bulkWrite()`
* - `db.collection.save()`
  - - `db.collection.insertOne()`
    - `db.collection.insertMany()`
    - `db.collection.updateOne()`
    - `db.collection.updateMany()`
    - `db.collection.findOneAndUpdate()`
* - `db.collection.update()`
  - - `db.collection.updateOne()`
    - `db.collection.updateMany()`
    - `db.collection.findOneAndUpdate()`
    - `db.collection.bulkWrite()`
* - `DBQuery.shellBatchSize`
  - - config.set("displayBatchSize", "<value>")
    - cursor.batchSize()
* - `Mongo.getSecondaryOk`
  - `Mongo.getReadPrefMode`
* - `Mongo.isCausalConsistency`
  - `Session.getOptions()`
* - `Mongo.setSecondaryOk`
  - `Mongo.setReadPref`
* - `rs.secondaryOk`
  - No longer required. See
    Read Operations on a Secondary Node.

### Display Batch Size

`DBQuery.shellBatchSize` is a deprecated setting from the legacy
`mongo` shell. The `mongosh` setting `displayBatchSize` replaces
it and sets the number of items that `mongosh` displays per cursor
iteration. The default value is `20`.

To set `displayBatchSize`, use one of these methods:

- In the current `mongosh` session, use the
  config API. The following example sets 
  the `displayBatchSize` to 50 by using the `config` API:

  ```javascript
  config.set( "displayBatchSize", 50 )
  ```

- For all future sessions, set the value in a
  configuration file. The following 
  example sets the `displayBatchSize` to 50 by using a configuration
  file:

  ```yaml
  mongosh:
    displayBatchSize: 50
  ```

`displayBatchSize` controls how many results `mongosh` displays and 
does not affect how many documents MongoDB returns. To control how many documents 
MongoDB returns in each batch for a specific 
query, use cursor.batchSize().

## Read Preference Behavior

### Read Operations on a Secondary Node

When using the legacy mongo shell to connect directly to 
secondary replica set member, you must run 
`mongo.setReadPref()` to enable secondary reads.

When using `mongosh` to connect directly to a secondary 
replica set member, you can read from that member if you specify a 
read preference of either:

- `primaryPreferred`
- `secondary`
- `secondaryPreferred`

To specify a read preference, you can use either:

- The `readPreference` connection string option when
  connecting to the node.

- The `Mongo.setReadPref()` method.

When using `mongosh` to connect directly to a secondary 
replica set member, if your read preference is set to 
`primaryPreferred`, `secondary` or 
`secondaryPreferred` it is *not* required to run
`rs.secondaryOk()`.

### show Helper Methods

The following `show` helper methods always use a read preference of
`primaryPreferred`, even when a different read preference has been
specified for the operation:

- `show dbs`
- `show databases`
- `show collections`
- `show tables`

In the legacy `mongo` shell, these operations use the specified read
preference.

## Write Preference Behavior

Retryable writes are enabled by default in
`mongosh`. Retryable writes were disabled by default in the
legacy `mongo` shell. To disable retryable writes, use 
`--retryWrites=false`.

## ObjectId Methods and Attributes

These ObjectId() methods work differently
in `mongosh` than in the legacy `mongo` shell.

| Method or Attribute | `mongo` Behavior | `mongosh` Behavior |
|---|---|---|
| `ObjectId.str` | \| Returns a hexadecimal string: \| `6419ccfce40afaf9317567b7` | \| Undefined \| (Not available) |
| `ObjectId.valueOf()` | \| Returns the value of `ObjectId.str`: \| `6419ccfce40afaf9317567b7` | \| Returns a formatted string: \| `ObjectId("6419ccfce40afaf9317567b7")` |
| `ObjectId.toString()` | \| Returns a formatted string: \| `ObjectId("6419ccfce40afaf9317567b7")` | \| Returns a hexadecimal formatted string: \| `6419ccfce40afaf9317567b7` |

## Numeric Values

The legacy `mongo` shell stored numerical values as `doubles` by
default. In `mongosh` numbers are stored as 32 bit integers,
`Int32`, or else as `Double` if the value cannot be stored as an
`Int32`. 

MongoDB Shell continues to support the numeric types that are supported
in `mongo` shell. However, the preferred types have been updated to
better align with the MongoDB `drivers`. See
mongosh Data Types for more information.

The preferred types for numeric variables are different in MongoDB 
Shell than the types suggested in the legacy `mongo` shell. The types
in `mongosh` better align with the types used by the MongoDB Drivers.

| `mongo` type | `mongosh` type |
|---|---|
| `NumberInt` | `Int32` |
| `NumberLong` | `Long` |
| `NumberDecimal` | `Decimal128` |

**Warning:**

Data types may be stored inconsistently if you connect to the same
collection using both `mongosh` and the legacy `mongo` shell. 

**See also:**

For more information on managing types, refer to the
schema validation overview.

## Undefined Values

The undefined BSON type is [deprecated](https://bsonspec.org/spec.html). 
If you try to insert a document with the undefined JS type in
`mongosh`, your deployment replaces the undefined value in your 
document with the BSON null value. There is no supported way of inserting undefined
values into your database using `mongosh`.

For example, consider running the following code to insert a document in
`mongosh`:

```javascript
db.people.insertOne( { name : "Sally", age : undefined } )
```

When you run this code in `mongosh`, the shell inserts 
the following document: 

```javascript
"copyable: false

{ name : "Sally", age : null }
```

`mongosh` represents any BSON undefined values stored using other tools, such as 
the [Go Driver](https://www.mongodb.com/docs/drivers/go/current/) or the 
legacy `mongo` shell, as null.

## Object Quoting Behavior

`mongosh` does not quote object keys in its output, and places single 
quotes on values. To reproduce the output of the legacy
`mongo` shell, which wraps both the keys and string values in double quotes, 
use `mongosh --eval` with EJSON.stringify().

For example, the following command returns the items in the `sales`
collection on the `test` database with double quotes and indentation:

```shell
mongosh --eval "EJSON.stringify(db.sales.findOne().toArray(), null, 2)"
```

The output looks like the following:

```javascript
{
     "_id": {
          "$oid": "64da90c1175f5091debcab26"
     },
     "custId": 345,
     "purchaseDate": {
          "$date": "2023-07-04T00:00:00Z"
     },
     "quantity": 4,
     "cost": {
          "$numberDecimal": "100.60"
     }
}
```

## Limitations on Database Calls

The results of database queries cannot be passed inside the following
contexts:

- Class constructor functions
- Non-async generator functions
- Callbacks to `.sort()` on an array
- JavaScript setters in classes

To access to the results of database calls, use [async functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/async_function),
[async generator functions](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Statements/for-await...of),
or `.map()`.

### Constructors

The following constructors do not work: 

```javascript
// This code will fail
class FindResults {
   constructor() {
      this.value = db.students.find();
   }
}

// This code will fail
function listEntries() { return db.students.find(); }
class FindResults {
   constructor() {
      this.value = listEntries();
   }
}
```

Use an `async` function instead:

```javascript
class FindResults {
   constructor() {
      this.value = ( async() => {
         return db.students.find();
      } )();
   }
}
```

**Note:**

You can also create a method that performs a database operation
inside a class as an alternative to working with asynchronous
JavaScript.

```
class FindResults {
   constructor() { }

   init() { this.value = db.students.find(); }
 }
```

To use this class, first construct a class instance then call the
`.init()` method.

### Generator Functions

The following generator functions do not work: 

```javascript
// This code will fail
function* FindResults() {
   yield db.students.findOne();
}

// This code will fail
function listEntries() { return db.students.findOne(); }
function* findResults() {
   yield listEntries();
}
```

Use an `async generator function` instead: 

```javascript
function listEntries() { return db.students.findOne(); }
async function* findResults() {
   yield listEntries();
}
```

### Array Sort

The following array sort does not work: 

```javascript
// This code will fail
db.getCollectionNames().sort( ( collectionOne, collectionTwo ) => {
  return db[ collectionOne ].estimatedDocumentCount() - db[ collectionOne ].estimatedDocumentCount() )
} );
```

Use `.map()` instead. 

```javascript
db.getCollectionNames().map( collectionName => {
   return { collectionName, size: db[ collectionName ].estimatedDocumentCount() };
} ).sort( ( collectionOne, collectionTwo ) => {
   return collectionOne.size - collectionTwo.size;
} ).map( collection => collection.collectionName);
```

This approach to array sort is often more performant than the
equivalent unsupported code.

### JavaScript Setters

The following JavaScript setter does not work: 

```javascript
// This code will fail
class TestClass {
  value = 1;

  get property() {
    return this.value;
  }

  // does not work:
  set property(value) {
    this.value = db.test.findOne({ value });
  }
}
```

## Command Exceptions

For commands whose output includes `{ ok: 0 }`, `mongosh` returns a
consistent exception and omits the server raw output. The legacy
`mongo` shell returns output that varies for each command.

For details, see run-commands.

## Shell Configuration

The legacy `mongo` shell uses a configuration file named
`.mongorc.js`.

If `mongosh` finds `.mongorc.js` on startup but doesn't find
`.mongoshrc.js`, `mongosh` doesn't load the legacy `.mongorc.js`
file and states you should rename `.mongorc.js` to `.mongoshrc.js`.

For details, see mongoshrc-js.

## Data Types

MongoDB stores data using BSON, which
supports additional data types that aren't available in JSON.
The `mongosh` shell has better data type support for
`drivers` than the legacy `mongo` shell.

For details, see mongo-shell-data-types.

## Methods

The legacy `mongo` shell cannot access a script's file name or
directory in the `load()` method.

For details, see load().

## Retryable Writes

By default, retryable writes are:

- enabled in `mongosh`
- disabled in the legacy `mongo` shell

To disable retryable writes, use `--retryWrites=false`.

For details, see `--retryWrites`.

## Legacy Output

The `mongosh` shell returns output that differs from the legacy
`mongo` shell. If you have scripts that require the output to be
formatted in a similar way to the legacy `mongo` shell, try
reformatting the `mongosh` output with EJSON.stringify().

For details, see mongosh-ejson-stringify-legacy-output.

## Code Snippets

Working with code snippets is different for the legacy `mongo` shell.

For details, see snip-get-help.
