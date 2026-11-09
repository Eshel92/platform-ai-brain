<!-- Converted from reference/config-database.txt (reStructuredText). Includes are inlined. -->

# Config Database

The collections in the `config` database support:

- Sharded cluster operations

- Causally consistent sessions for standalones,
  replica sets, and sharded clusters and retryable writes for replica
  sets and sharded clusters.

**Note:**

Sharded clusters may show different collections in the
`config` database, depending on whether you connect to
`mongos` or `mongod`:

- On `mongos`, the `config` database shows collections
  located on the config servers, such as
  `collections` or `chunks`.

- On `mongod`, the `config` database shows
  collections specific to the given shard, such as
  `migrationCoordinators` or
  `rangeDeletions`.

When a config server and a shard are hosted on the same node,
`mongos` may have access to some shard-local
collections in the `config` database.

## Restrictions

Starting in MongoDB 5.0, non-transaction reads are not allowed on 
the `config.transactions` collection with the following
read concerns and options:

- `"snapshot"`
- `"majority"` and the 
  afterClusterTime option is set
- When using a `MongoDB Driver`  
  and `"majority"`
  within a causally consistent session

**Important:** The schema of the `config` database is

*internal* and may change between releases of MongoDB. The
`config` database is not a dependable API, and users should not
write data to the `config` database in the course of normal
operation or maintenance.

**Note:**

You cannot perform read/write operations to the collections in the
`config` database inside a multi-document transaction.

## Collections to Support Sharded Cluster Operations

To access the `config` database and view the list of collections that
support sharding operations, connect `mongosh` to a
`mongos` instance in a sharded cluster and issue the following:

```javascript
use config

show collections
```

**Note:**

If running with access control, ensure you have privileges that
grant `listCollections` action on the database.

The config database is mainly for internal use, and during normal
operations you should never manually insert or store data in it.
However, if you need to verify the write availability of the config
server for a sharded cluster, you can insert a document into a test
collection (after making sure that no collection of that name already
exists):

**Warning:** Modification of the `config` database on a functioning

system may lead to instability or inconsistent data sets. If you
must modify the `config` database, use `mongodump` to
create a full backup of the `config` database.

```javascript
db.testConfigServerWriteAvail.insertOne( { a : 1 } )
```

If the operation succeeds, the config server is available to process
writes.

Future releases of the server may include different collections in
the config database, so be careful when selecting a name for your
test collection.

MongoDB uses the following collections in the `config` database
to support sharding:

**`config.changelog`**

**Tip:** Internal MongoDB Metadata

The config database is internal. Applications and
administrators should not modify or depend on its content during normal 
operation.

The `changelog` collection stores a document for each change to
the metadata of a sharded collection.

**Example:**

The following example displays a single record of a chunk split
from a `changelog` collection:

```javascript
{
 "_id" : "<hostname>-<timestamp>-<increment>",
 "server" : "<hostname><:port>",
 "clientAddr" : "127.0.0.1:63381",
 "time" : ISODate("2012-12-11T14:09:21.039Z"),
 "what" : "split",
 "ns" : "<database>.<collection>",
 "details" : {
    "before" : {
       "min" : {
          "<database>" : { $minKey : 1 }
       },
       "max" : {
          "<database>" : { $maxKey : 1 }
       },
       "lastmod" : Timestamp(1000, 0),
       "lastmodEpoch" : ObjectId("000000000000000000000000")
    },
    "left" : {
       "min" : {
          "<database>" : { $minKey : 1 }
       },
       "max" : {
          "<database>" : "<value>"
       },
       "lastmod" : Timestamp(1000, 1),
       "lastmodEpoch" : ObjectId(<...>)
    },
    "right" : {
       "min" : {
          "<database>" : "<value>"
       },
       "max" : {
          "<database>" : { $maxKey : 1 }
       },
       "lastmod" : Timestamp(1000, 2),
       "lastmodEpoch" : ObjectId("<...>")
    },
    "owningShard" : "<value>"
 }
}
```

Each document in the `changelog` collection contains the
following fields:

**`config.changelog._id`**

The value of `changelog._id` is:
`<hostname>-<timestamp>-<increment>`.

**`config.changelog.server`**

The hostname of the server that holds this data.

**`config.changelog.clientAddr`**

A string that holds the address of the client, a
`mongos` instance that initiates this change.

**`config.changelog.time`**

A ISODate timestamp that reflects when the change
occurred.

**`config.changelog.what`**

The type of change recorded. Possible values include:

- `dropCollection`
- `dropCollection.start`
- `dropDatabase`
- `dropDatabase.start`
- `moveChunk.start`
- `moveChunk.commit`
- `split`
- `multi-split`

**`config.changelog.ns`**

Namespace where the change occurred.

**`config.changelog.details`**

A document that contains additional details for
the change. The structure of the `details`
document depends on the type of change.

**`config.chunks`**

**Tip:** Internal MongoDB Metadata

The config database is internal. Applications and
administrators should not modify or depend on its content during normal 
operation.

The `config.chunks` collection stores a document for each
chunk in the cluster. The following example shows a document:

```javascript
{
   _id: ObjectId('65a954c0de11596e08e7c1dc'),
   uuid: UUID('a4479215-a38d-478f-a82b-e5e95d455e55'),
   min: { a: Long('121204345') },
   max: { a: Long('993849349') },
   shard: 'shard01',
   lastmod: Timestamp({ t: 1, i: 0 }),
   history: [
      {
         validAfter: Timestamp({ t: 1705596095, i: 14 }),
         shard: 'shard01'
      }
   ]
}
```

In the document:

- `_id` is the chunk identifier.
- `min` and `max` are the range of values for the chunk's shard
  key.
- `shard` is the name of the shard that stores the chunk in the
  cluster.

**Tip:**

To find the chunks in a collection, retrieve the collection's
`uuid` identifier from the `config.collections`
collection. Then, use `uuid` to retrieve the matching document
with the same `uuid` from the `config.chunks` collection.

**`config.collections`**

**Tip:** Internal MongoDB Metadata

The config database is internal. Applications and
administrators should not modify or depend on its content during normal 
operation.

The `collections` collection stores a document for each sharded collection
in the cluster. Given a collection named `pets`
in the `records` database, a document in the `collections`
collection would resemble the following:

```javascript
{
   "_id" : "records.pets",
   "lastmod" : ISODate("2021-07-21T15:48:15.193Z"),
   "timestamp": Timestamp(1626882495, 1),
   "key" : {
         "a" : 1
   },
   "unique" : false,
   "lastmodEpoch" : ObjectId("5078407bd58b175c5c225fdc"),
   "uuid" :  UUID("f8669e52-5c1b-4ea2-bbdc-a00189b341da")
}
```

**`config.databases`**

**Tip:** Internal MongoDB Metadata

The config database is internal. Applications and
administrators should not modify or depend on its content during normal 
operation.

The `databases` collection stores a document for each
database in the cluster.

For each database, the corresponding document displays the name, the
database's primary shard , the database's
sharding enabled status, and a version.

```javascript
{ "_id" : "test", "primary" : "shardA", "partitioned" : true, "version" : { "uuid" : UUID("516a5f79-5eb9-4844-8ee9-b8e9de91b760"), "timestamp" : Timestamp(1626894204, 1), "lastMod" : 1 } }
{ "_id" : "hr", "primary" : "shardA", "partitioned" : false, "version" : { "uuid" : UUID("8e39d61d-6259-4c33-a5ed-bcd2ae317b6f"), "timestamp" : Timestamp(1626895015, 1), "lastMod" : 1 } }
{ "_id" : "reporting", "primary" : "shardB", "partitioned" : false, "version" : { "uuid" : UUID("07c63242-51b3-460c-865f-a67b3372d792"), "timestamp" : Timestamp(1626895826, 1), "lastMod" : 1 } }
```

The method `sh.status()` returns this information in the
sharding-status-databases-fields section.

**`config.migrationCoordinators`**

The `migrationCoordinators` collection exists on each
shard and stores a document for each in-progress chunk
migration from this shard to another shard. The chunk migration fails
if the document cannot be written to a majority of the members of the
shard's replica set.

When a migration is complete, the document describing the migration
is deleted from the collection.

**`config.mongos`**

**Tip:** Internal MongoDB Metadata

The config database is internal. Applications and
administrators should not modify or depend on its content during normal 
operation.

The `mongos` collection stores a document for each
`mongos` instance affiliated with the cluster. The
cluster maintains this collection for reporting purposes.

Each document in the `mongos` collection contains these
fields:

* - Field
  - Data Type
  - Description

* - `_id`
  - String
  - The hostname and port where the
    `mongos` is running. The `_id` is formatted as
    `<hostname>:<port>`.

* - `advisoryHostFQDNs`
  - Array of strings
  - Array of the `mongos`'s fully qualified domain
    names (FQDNs).

* - `created`
  - Date
  - When the `mongos` was started.

    **New in version:** 5.2

* - `mongoVersion`
  - String
  - Version of MongoDB that the `mongos` is running.

* - `ping`
  - Date
  - `mongos` instances send pings to the
    config server every 30
    seconds. This field indicates the last ping time.

* - `up`
  - NumberLong
  - Number of seconds the `mongos` has been up as of
    the last ping.

* - `waiting`
  - Boolean
  - This field is always `true` and is only included for backward 
    compatibility.

The following document shows the status of the `mongos`
running on `example.com:27017`.

```javascript
[
   {
     _id: 'example.com:27017',
     advisoryHostFQDNs: [ "example.com" ],
     created: ISODate("2021-11-22T16:32:13.708Z"),
     mongoVersion: "5.2.0",
     ping: ISODate("2021-12-15T22:09:23.161Z"),
     up: Long("2007429"),
     waiting: true
   }
]
```

**`config.rangeDeletions`**

The `rangeDeletions` collection exists on each shard
and stores a document for each chunk range that contains orphaned
documents. The chunk migration fails if the document cannot be
written to a majority of the members of the shard's replica set.

When the orphaned chunk range is cleaned up, the document
describing the range is deleted from the collection.

**`config.settings`**

**Tip:** Internal MongoDB Metadata

The config database is internal. Applications and
administrators should not modify or depend on its content during normal 
operation.

The `settings` collection holds the following
sharding configuration settings:

- Range size. To change range size,
  see Modify Range Size in a Sharded Cluster. The specified `chunksize` value 
  is in megabytes.

- Balancer settings. To change the balancer settings, including
  balancer status, see
  /tutorial/manage-sharded-cluster-balancer.

- Autosplit:

  Starting in MongoDB 6.0.3, automatic chunk splitting is not performed. 
  This is because of balancing policy improvements. Auto-splitting commands 
  still exist, but do not perform an operation. For details, see
  release-notes-6.0-balancing-policy-changes.

  In MongoDB versions earlier than 6.0:

  - `balancerStart` also enables auto-splitting for the
    sharded cluster.

  - `balancerStop` also disables auto-splitting for the
    sharded cluster.

  - To enable or disable the autosplit flag, use the corresponding
    `sh.enableAutoSplit()` method or
    `sh.disableAutoSplit()` method.

Example documents in the `settings` collection:

```javascript
{ "_id" : "chunksize", "value" : 64 }
{ "_id" : "balancer", "mode" : "full", "stopped" : false }
```

**`config.shards`**

**Tip:** Internal MongoDB Metadata

The config database is internal. Applications and
administrators should not modify or depend on its content during normal 
operation.

The `shards` collection represents each shard in the cluster
in a separate document, as in the following:

```javascript
{ "_id" : "shard0000", "host" : "localhost:30000", "state" : 1 }
```

If the shard is a replica set, the
`host` field displays the name of the replica set, then a slash, then
a comma-separated list of the hostnames of each member of the replica set,
as in the following example:

```javascript
{ "_id" : "shard0001", "host" : "shard0001/localhost:27018,localhost:27019,localhost:27020", "state" : 1 }
```

If the shard has zones assigned, this
document has a `tags` field, that holds an array of the zones
to which it is assigned, as in the following example:

```javascript
{ "_id" : "shard0002", "host" : "localhost:30002", "state" : 1, "tags": [ "NYC" ] }
```

**`config.tags`**

**Tip:** Internal MongoDB Metadata

The config database is internal. Applications and
administrators should not modify or depend on its content during normal 
operation.

The `tags` collection holds documents for each zone
range in the cluster. The documents in the
`tags` collection resemble the following:

```javascript
{
    "_id" : { "ns" : "records.users", "min" : { "zipcode" : "10001" } },
    "ns" : "records.users",
    "min" : { "zipcode" : "10001" },
    "max" : { "zipcode" : "10281" },
    "tag" : "NYC"
}
```

**`config.version`**

**Tip:** Internal MongoDB Metadata

The config database is internal. Applications and
administrators should not modify or depend on its content during normal 
operation.

The `version` collection holds the current metadata version number. This
collection contains only one document. For example:

```javascript
{ "_id" : 1, "minCompatibleVersion" : 5, "currentVersion" : 6, "clusterId" : ObjectId("5d8bc01a690d8abbd2014ddd") }
```

To access the `version` collection, you must use the
`db.getCollection()` method. For example, to retrieve the
collection's document:

```javascript
db.getCollection("version").find()
```

   

## Collections to Support Sessions

The `config` database contains the
*internal* collections to support causally consistent sessions for standalones, replica sets, and sharded clusters and
retryable writes and transactions for
replica sets and sharded clusters.

**Warning:**

Do not manually modify or drop these collections.

To access these collections for a `mongod` or
`mongos` instance, connect `mongosh` to the
instance.

**`config.system.sessions`**

The `system.sessions` collection stores session records that are
available to all members of the deployment.

When a user creates a session on a `mongod` or
`mongos` instance, the record of the session initially
exists only in-memory on the instance. Periodically, the instance
will sync its cached sessions to the `system.sessions` collection;
at which time, they are visible to all members of the deployment.

To view records in the `system.sessions` collection, use
`$listSessions`.

**Warning:**

Do not manually modify or drop the `system.sessions` collection.

In a sharded cluster, the `system.sessions` collection is sharded.

When adding a shard to the sharded cluster, if the shard to add
already contains its own `system.sessions` collection, MongoDB
drops the new shard's `system.sessions` collection during the
add process.

**`config.transactions`**

The `transactions` collection stores records used to support
retryable writes and transactions for replica sets and sharded clusters.

**Warning:**

Do not manually modify or drop the `transactions` collection.
