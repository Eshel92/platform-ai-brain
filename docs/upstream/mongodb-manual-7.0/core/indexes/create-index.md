<!-- Converted from core/indexes/create-index.txt (reStructuredText). Includes are inlined. -->

# Create an Index

If your application repeatedly runs queries on the same fields, create
an index on those fields to improve performance.

To create an index, use the `createIndex()` shell
method or equivalent method for your driver. This page shows examples
for the MongoDB Shell and drivers.

## About this Task

When you run a create index command in the MongoDB Shell or a driver,
MongoDB only creates the index if an index of the same specification
does not exist.

Although indexes improve query performance, adding an index has negative
performance impact for write operations. For collections with a high
write-to-read ratio, indexes are expensive because each insert and
update must also update any indexes.

**Warning:**

Do not create indexes on encrypted fields. Creating indexes on
encrypted fields that use Queryable Encryption negatively affect performance. Instead, you can 
create an index on the `__safeContent__` field to support queries on encrypted 
fields.

## Procedure

----------

→ To set the language of the examples on this page, use the
**Select your language** drop-down menu in the right navigation pane.

----------

tabs:
  - id: shell
    content: |

      To create an index in `mongosh`, use
      `db.collection.createIndex()`.

      ```javascript
      db.collection.createIndex( <key and index type specification>, <options> )
      ```

  - id: python
    content: |

      To create an index using the
      [Python driver](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/),
      use the [pymongo.collection.Collection.create_index](https://www.mongodb.com/docs/languages/python/pymongo-driver/current/work-with-indexes/#create-an-index)
      method:

      ```python
      db.collection.create_index([(<key and index type specification>)], <options> )
      ```

  - id: motor
    content: |

      To create an index using the
      [Motor driver](https://motor.readthedocs.io/en/stable/),
      use
      `motor.motor_asyncio.AsyncIOMotorCollection.create_index`.

      ```python
      await db.collection.create_index([(<key and index type specification>)], <options> )
      ```

  - id: java-sync
    content: |

      To create an index using the
      [Java driver](https://mongodb.github.io/mongo-java-driver/),
      use
      [com.mongodb.client.MongoCollection.createIndex](http://mongodb.github.io/mongo-java-driver/3.4/javadoc/?com/mongodb/client/MongoCollection.html#createIndex-org.bson.conversions.Bson-).

      ```java
      collection.createIndex( <key and index type specification>, <options> )å
      ```

  - id: java-async
    content: |

      To create an index using the
      [Async Java driver](http://mongodb.github.io/mongo-java-driver/3.0/driver-async/),
      use
      [com.mongodb.async.client.MongoCollection.createIndex](http://mongodb.github.io/mongo-java-driver/3.4/javadoc/?com/mongodb/async/client/MongoCollection.html#createIndex-org.bson.conversions.Bson-com.mongodb.async.SingleResultCallback-).

      ```java
      collection.createIndex( <key and index type specification>, <options>, <callbackFunction>)
      ```

  - id: nodejs
    content: |

      To create an index using the
      [Node.JS driver](https://www.mongodb.com/docs/drivers/node/current/),
      use `createIndex()`.

      ```javascript
      collection.createIndex( { <key and index type specification> }, function(err, result) {
         console.log(result);
         callback(result);
      } )
      ```

  - id: php
    content: |

      To create an index using the
      [PHP driver](https://www.mongodb.com/docs/php-library/current/), use
      `MongoDBCollection::createIndex()`.

      ```php
      $collection->createIndex(<key and index type specification>, <options>);
      ```

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

  - id: ruby
    content: |

      To create an index using the
      [Ruby driver](https://www.mongodb.com/docs/ruby-driver/current/), use
      [Mongo::Index::View#create_one](http://www.rubydoc.info/github/mongodb/mongo-ruby-driver/Mongo%2FIndex%2FView%3Acreate_one).

      ```ruby
      client[:collection].indexes.create_one({ <key and index type specification> }, {options})
      ```

  - id: scala
    content: |

      To create an index using the
      [Scala driver](http://mongodb.github.io/mongo-scala-driver/),
      use
      [org.mongodb.scala.model.Indexes](https://mongodb.github.io/mongo-scala-driver/1.0/scaladoc/index.html#org.mongodb.scala.model.Indexes$).

      ```scala
      collection.createIndex(<key and index type specification>)
      ```

  - id: csharp
    content: |

      To create an index using the
      [.NET driver](http://mongodb.github.io/mongo-csharp-driver/),
      use
      [MongoCollection.CreateIndex](http://api.mongodb.com/csharp/current/html/Overload_MongoDB_Driver_MongoCollection_CreateIndex.htm).

      ```csharp
      collection.CreateIndex( IndexKeys<collection>.<key and index type specification>, <options> );
      ```

## Example

tabs:
  - id: shell
    content: |

      This example creates a single key ascending index on the
      `name` field:

      ```javascript
      db.collection.createIndex( { name: 1 } )
      ```

  - id: python
    content: |

      This example creates a single key ascending index on the
      `name` field:

      ```python
      collection.create_index([("name", pymongo.ASCENDING)])
      ```

  - id: motor
    content: |

      This example creates a single key ascending index on the
      `name` field:

      ```python
      await collection.create_index([("name", pymongo.ASCENDING)])
      ```

  - id: java-sync
    content: |

      This example creates a single key ascending index on the
      `name` field:

      ```java
      collection.createIndex(Indexes.ascending("name"));
      ```

  - id: java-async
    content: |

      This example creates a single key ascending index on the
      `name` field:

      ```java
      collection.createIndex(Indexes.ascending("name"), someCallbackFunction());
      ```

  - id: nodejs
    content: |

      This example creates a single key ascending index on the
      `name` field:

      ```javascript
       collection.createIndex( { name : 1 }, function(err, result) {
         console.log(result);
         callback(result);
      } )
      ```

  - id: php
    content: |

      This example creates a single key ascending index on the
      `name` field:

      ```php
      $collection->createIndex(['name' => 1]);
      ```

  - id: perl
    content: |

      This example creates a single key ascending index on the
      `name` field:

      ```perl
      my $indexes = $db->get_collection( <collection> )->indexes;
      $indexes->create_one( [ name => 1 ] );
      ```

  - id: ruby
    content: |

      This example creates a single key ascending index on the
      `name` field:

      ```ruby
      client[:collection].indexes.create_one({ name: 1 })
      ```

  - id: scala
    content: |

      This example creates a single key ascending index on the
      `name` field:

      ```scala
      collection.createIndex(ascending("name"))
      ```

  - id: csharp
    content: |

      This example creates a single key ascending index on the
      `name` field:

      ```csharp
      collection.CreateIndex( IndexKeys<collection>.Ascending("name") );
      ```

## Results

Use `mongosh` to monitor index creation.

To see what indexes exist on your collection, including indexes that
are currently being built, run the
`db.collection.getIndexes()` method:

```javascript
db.collection.getIndexes()
```

Output:

```javascript
[
   { v: 2, key: { _id: 1 }, name: '_id_' },
   { v: 2, key: { name: -1 }, name: 'name_-1' }
]    
```

To check whether your index is building, use `$currentOp`
with `db.aggregate()` on the `admin` database.

The following aggregation pipeline uses the `$match` stage
to show an active operation building a descending index on the
`name` field:

```javascript
db.getSiblingDB("admin").aggregate( [
   { $currentOp : { idleConnections: true } },
   { $match : {"command.createIndexes": { $exists: true } } }
] )
```

Output:

```javascript
[
   {
      type: 'op',
      host: 'mongodb.example.net:27017',
      desc: 'conn584',
      connectionId: 584,
      client: '104.30.134.189:12077',
      appName: 'mongosh 2.3.4',
      clientMetadata: { 
         ... 
      },
      active: true,
      currentOpTime: '2024-12-05T16:13:35.571+00:00',
      effectiveUsers: [ { user: jane-doe, db: 'admin' } ],
      isFromUserConnection: true,
      threaded: true,
      opid: ...,
      lsid: { 
         ... 
      },
      secs_running: Long('3'),
      microsecs_running: Long('3920881'),
      op: 'command',
      ns: 'example_db.collection',
      redacted: false,
      command: {
         createIndexes: 'collection',
         indexes: [ { name: 'name_-1', key: { name: -1 } } ],
         apiVersion: '1',
         lsid: { id: UUID('570931be-c692-4963-b9e2-1e279efd9702') },
         '$clusterTime': {
         clusterTime: Timestamp({ t: 1733415063, i: 32 }),
         signature: {
            hash: Binary.createFromBase64('z0zaUHJ5SfhNQyvQLhocsKRFNbo=', 0),
            keyId: Long('7444956895695077380')
         }
         },
         '$db': 'example_db'
      },
      numYields: 0,
      queues: {
         ...
      },
      currentQueue: null,
      locks: {},
      waitingForLock: false,
      lockStats: { ... },
      waitingForFlowControl: false,
      flowControlStats: { acquireCount: Long('3') }
   }, ...
]
```

MongoDB marks index builds in various stages, including waiting on
commit quorum, as an idle connection by setting the `active` field
to `false`. The `idleConnections: true` setting includes these
idle connections in the `$currentOp` output.

To view information on existing indexes using a driver, refer to your
`driver's documentation`.

## Learn More

- To learn how to create indexes in MongoDB Compass, see Manage Indexes in the Compass documentation.

- To see how often your indexes are used, see
  index-measure-index-use.

- To learn how to specify the name of your index, see specify-index-name.

- To learn how MongoDB builds indexes, see index-build-process.
