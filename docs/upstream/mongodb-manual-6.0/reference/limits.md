<!-- Converted from reference/limits.txt (reStructuredText). Includes are inlined. -->

# MongoDB Limits and Thresholds

This document provides a collection of hard and soft limitations of
the MongoDB system. The limitations on this page apply to deployments
hosted in all of the following environments unless specified otherwise:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## MongoDB Atlas Limitations

The following limitations apply only to deployments hosted in
MongoDB Atlas. If any of these limits present a problem for your organization, contact Atlas support.

### MongoDB Atlas Cluster Limits

| Component | Limit |
|---|---|
| Shards in multi-region clusters | 12 |
| Shards in single-region clusters | 70 |
| Cross-region network permissions for a multi-region cluster | 40. Additionally, a cluster in any project spans more than 40 regions, you can't create a multi-region cluster in this project. |
| Electable nodes per replica set or shard | 7 |
| Cluster tier for the Config server (minimum and maximum) | `M30` |

### MongoDB Atlas Connection Limits and Cluster Tier

MongoDB Atlas limits concurrent incoming connections
based on the cluster tier and class. 
MongoDB Atlas connection limits apply per node. For
sharded clusters, MongoDB Atlas connection limits apply per
mongos router. The number of
mongos routers is equal to
the number of replica set nodes across all shards. 

Your read preference also
contributes to the total number of connections that MongoDB Atlas can
allocate for a given query.

MongoDB Atlas has the following connection limits for the specified cluster
tiers:

**aws:**

**general-class:**

| MongoDB Atlas Cluster Tier | Maximum Connections Per Node |
|---|---|
| `M0` | 500 |
| `M2` | 500 |
| `M5` | 500 |
| `M10` | 1500 |
| `M20` | 3000 |
| `M30` | 3000 |
| `M40` | 6000 |
| `M50` | 16000 |
| `M60` | 32000 |
| `M80` | 96000 |
| `M140` | 96000 |
| `M200` | 128000 |
| `M300` | 128000 |

**low-cpu-class:**

| MongoDB Atlas Cluster Tier | Maximum Connections Per Node |
|---|---|
| `M40` | 4000 |
| `M50` | 16000 |
| `M60` | 32000 |
| `M80` | 64000 |
| `M140` | 96000 |
| `M200` | 128000 |
| `M300` | 128000 |
| `M400` | 128000 |
| `M700` | 128000 |

**other:**

| MongoDB Atlas Cluster Tier | Maximum Connections Per Node |
|---|---|
| `M0` | 500 |
| `M2` | 500 |
| `M5` | 500 |
| `M10` | 1500 |
| `M20` | 3000 |
| `M30` | 3000 |
| `M40` | 6000 |
| `M50` | 16000 |
| `M60` | 32000 |
| `M80` | 64000 |
| `M140` | 96000 |
| `M200` | 128000 |
| `M300` | 128000 |

**Note:**

MongoDB Atlas reserves a small number of connections to each cluster for
supporting MongoDB Atlas services.

### MongoDB Atlas Multi-Cloud Connection Limitation

If you're connecting to a multi-cloud MongoDB Atlas deployment through a 
private connection, you can access only
the nodes in the same cloud provider that you're connecting from. This 
cloud provider might not have the primary node in its region. 
When this happens, you must specify the 
secondary read preference mode in the
connection string to access the deployment.

If you need access to all nodes for your multi-cloud MongoDB Atlas
deployment from your current provider through a private connection, you
must perform one of the following actions:

- Configure a VPN in the current provider to each of the remaining 
  providers.
- Configure a private endpoint to MongoDB Atlas
  for each of the remaining providers.

### MongoDB Atlas Collection and Index Limits

While there is no hard limit on the number of collections in a single 
MongoDB Atlas cluster, the performance of a cluster might degrade if it
serves a large number of collections and indexes. Larger collections
have a greater impact on performance.

The recommended maximum combined number of collections and indexes by
MongoDB Atlas cluster tier are as follows:

| MongoDB Atlas Cluster Tier | Recommended Maximum |
|---|---|
| `M10` | 5,000 collections and indexes |
| `M20` / `M30` | 10,000 collections and indexes |
| `M40`/+ | 100,000 collections and indexes |

### MongoDB Atlas Organization and Project Limits

MongoDB Atlas deployments have the following organization and project
limits: 

| Component | Limit |
|---|---|
| Database users per MongoDB Atlas project | 100 |
| Atlas users per MongoDB Atlas project | 500 |
| Atlas users per MongoDB Atlas organization | 500 |
| API Keys per MongoDB Atlas organization | 500 |
| Access list entries per MongoDB Atlas Project | 200 |
| Users per MongoDB Atlas team | 250 |
| Teams per MongoDB Atlas project | 100 |
| Teams per MongoDB Atlas organization | 250 |
| Teams per MongoDB Atlas user | 100 |
| Organizations per MongoDB Atlas user | 250 |
| Linked organizations per MongoDB Atlas user | 50 |
| Clusters per MongoDB Atlas project | 25 |
| Projects per MongoDB Atlas organization | 250 |
| Custom MongoDB roles per MongoDB Atlas project | 100 |
| Assigned roles per database user | 100 |
| Hourly billing per MongoDB Atlas organization | $50 |
| Federated database instances per MongoDB Atlas project | 25 |
| Total Network Peering Connections per MongoDB Atlas project | 50. Additionally, MongoDB Atlas limits the number of nodes per Network Peering connection based on the CIDR block and the region selected for the project. |
| Pending network peering connections per MongoDB Atlas project | 25 |
| AWS Private Link addressable targets per region | 50 |
| Azure PrivateLink addressable targets per region | 150 |
| Unique shard keys per MongoDB Atlas-managed Global Cluster project | 40. This applies only to Global Clusters with Atlas-Managed Sharding. There are no limits on the number of unique shard keys per project for Global Clusters with Self-Managed Sharding. |
| [Atlas Data Lake](https://www.mongodb.com/docs/datalake/) pipelines per MongoDB Atlas project | 25 |
| `M0` clusters per MongoDB Atlas project | 1 |

### MongoDB Atlas Service Account Limits

MongoDB Atlas service accounts have the following organization and project
limits: 

| Component | Limit |
|---|---|
| Atlas service accounts per MongoDB Atlas organization | 200 |
| Access list entries per MongoDB Atlas service account | 200 |
| Secrets per MongoDB Atlas service account | 2 |
| Active tokens per MongoDB Atlas service account | 100 |

### MongoDB Atlas Label Limits

MongoDB Atlas limits the length and enforces ReGex requirements for the
following component labels:

| Component | Character Limit | RegEx Pattern |
|---|---|---|
| Cluster Name | 64 [1]_ | `^([a-zA-Z0-9]([a-zA-Z0-9-]){0,21}(?<!-)([\w]{0,42}))$` [2]_ |
| Project Name | 64 | `^[\p{L}\p{N}\-_.(),:&@+']{1,64}$` [3]_ |
| Organization Name | 64 | `^[\p{L}\p{N}\-_.(),:&@+']{1,64}$` [3]_ |
| API Key Description | 250 |  |

### Serverless Instance, Free Cluster, M2 and M5 Cluster, and Flex Cluster Limitations

Additional limitations apply to MongoDB Atlas serverless instances,
free clusters, M2, M5, and Flex clusters. To learn more, 
see the following resources:

- Serverless Instance Limitations
- Atlas M0 (Free Cluster), M2, and M5 Limitations
- Atlas Flex Limitations

### MongoDB Atlas Command Limitations

Some MongoDB commands are unsupported in MongoDB Atlas. Additionally, some
commands are supported only in MongoDB Atlas free clusters. To learn more,
see the following resources:

- Unsupported Commands in Atlas
- Commands Available Only in Free Clusters

## BSON Documents

**`BSON Document Size`**

The maximum BSON document size is 16 mebibytes.

The maximum document size helps ensure that a single document cannot use an
excessive amount of RAM or, during transmission, an excessive amount of
bandwidth. To store documents larger than the maximum size, MongoDB provides the
GridFS API. For more information about GridFS, see `mongofiles` and
the documentation for your `driver` 

**`Nested Depth for BSON Documents`**

MongoDB supports no more than 100 levels of nesting for BSON
documents. Each object or array adds a level.

## Naming Restrictions

**`Use of Case in Database Names`**

Do not rely on case to distinguish between databases. For example,
you cannot use two databases with names like, `salesData` and
`SalesData`.

After you create a database in MongoDB, you must use consistent
capitalization when you refer to it. For example, if you create the
`salesData` database, do not refer to it using alternate
capitalization such as `salesdata` or `SalesData`.

**`Restrictions on Database Names for Windows`**

For MongoDB deployments running on Windows, database names cannot
contain any of the following characters:

```none
/\. "$*<>:|?
```

Also database names cannot contain the null character.

**`Restrictions on Database Names for Unix and Linux Systems`**

For MongoDB deployments running on Unix and Linux systems, database
names cannot contain any of the following characters:

```none
/\. "$
```

Also database names cannot contain the null character.

**`Length of Database Names`**

Database names cannot be empty and must be less than 64 bytes.

**`Restriction on Collection Names`**

Collection names should begin with an underscore or a letter
character, and *cannot*:

- contain the `$`.

- be an empty string (e.g. `""`).

- contain the null character.

- begin with the `system.` prefix. (Reserved for internal use.)

- contain `.system.`. 

If your collection name includes special characters, such as the
underscore character, or begins with numbers, then to access the
collection use the `db.getCollection()` method in
`mongosh` or a `similar method for your driver`.

Namespace Length:

The namespace length limit for unsharded collections and views is 255 bytes, 
and 235 bytes for sharded collections. For a collection or a view, the namespace 
includes the database name, the dot (`.`) separator, and the collection/view 
name (e.g. `<database>.<collection>`).

**`Restrictions on Field Names`**

- Field names **cannot** contain the `null` character.

- The server permits storage of field names that contain dots (`.`)
  and dollar signs (`$`).

- MongodB 5.0 adds improved support for the use of (`$`) and (`.`)
  in field names. There are some restrictions. See
  Field Name Considerations for more details.

**`Restrictions on _id`**

The field name `_id` is reserved for use as a primary key; its value
must be unique in the collection, is immutable, and may be of any type
other than an array or regex. If the `_id` contains subfields, the 
subfield names cannot begin with a (`$`) symbol.

## Naming Warnings

**Warning:**

Use caution, the issues discussed in this section could lead to data
loss or corruption.  

### MongoDB does not support duplicate field names

The MongoDB Query Language doesn't support documents with duplicate
field names:

- Although some BSON builders may support creating a BSON document with
  duplicate field names, inserting these documents into MongoDB isn't
  supported even if the insert succeeds, or appears to succeed.

- For example, inserting a BSON document with duplicate field names
  through a MongoDB driver may result in the driver silently dropping
  the duplicate values prior to insertion, or may result in an invalid
  document being inserted that contains duplicate fields. Querying those
  documents leads to inconsistent results. 

- Updating documents with duplicate field names isn't
  supported, even if the update succeeds or appears to succeed.

Starting in MongoDB 6.1, to see if a document has duplicate field names,
use the `validate` command with the `full` field set to
`true`. In any MongoDB version, use the `$objectToArray`
aggregation operator to see if a document has duplicate field names.

### Avoid Ambiguous Field Names

Do not use a field name that is the same as the 
dot notation for an 
embedded field. If you have a document with an embedded field 
`{ "a" : { "b": ... } }`, other documents in that collection should 
**not** have a top-level field `"a.b"`.

If you can reference an embedded field and a top-level field in the same 
way, indexing and sharding operations happen on the embedded field. 
You cannot index or shard on the top-level field `"a.b"` while the 
collection has an embedded field that you reference in the same way. 

For example, if your collection contains documents with both an embedded 
field `{ "a" : { "b": ... } }` and a top-level field `"a.b"`, 
indexing and sharding operations happen on the embedded field. It is not 
possible to index or shard on the top-level field `"a.b"` when your 
collection also contains an embedded field `{ "a" : { "b": ... } }`.

### Import and Export Concerns With Dollar Signs (`$`) and Periods (`.`)

Starting in MongoDB 5.0, document field names can be dollar (`$`)
prefixed and can contain periods (`.`). However,
`mongoimport` and `mongoexport` may not work
as expected in some situations with field names that make use of these
characters.

MongoDB Extended JSON v2
cannot differentiate between type wrappers and fields that happen to
have the same name as type wrappers. Do not use Extended JSON
formats in contexts where the corresponding BSON representations
might include dollar (`$`) prefixed keys. The
DBRef mechanism is an exception to this
general rule. 

There are also restrictions on using `mongoimport` and
`mongoexport` with periods (`.`) in field names. Since
CSV files use the period (`.`) to represent data hierarchies, a
period (`.`) in a field name will be misinterpreted as a level of
nesting.

### Possible Data Loss With Dollar Signs (`$`) and Periods (`.`)

There is a small chance of data loss when using dollar (`$`) prefixed
field names or field names that contain periods (`.`) if these
field names are used in conjunction with unacknowledged writes
(write concern `w=0`) on servers
that are older than MongoDB 5.0.

When running insert,
update, and
findAndModify
commands, drivers that are 5.0 compatible remove restrictions on
using documents with field names that are dollar (`$`) prefixed or
that contain periods (`.`). These field names generated a client-side
error in earlier driver versions.

The restrictions are removed regardless of the server version the
driver is connected to. If a 5.0 driver sends a document to an older
server, the document will be rejected without sending an error.

## Namespaces

**`Namespace Length`**

The namespace length limit for unsharded collections and views is 255 bytes, 
and 235 bytes for sharded collections. For a collection or a view, the namespace 
includes the database name, the dot (`.`) separator, and the collection/view 
name (e.g. `<database>.<collection>`).

**See also:**

faq-restrictions-on-collection-names

## Indexes

**`Number of Indexes per Collection`**

A single collection can have *no more* than 64 indexes.

**`Number of Indexed Fields in a Compound Index`**

There can be no more than 32 fields in a compound index.

**`Queries cannot use both text and Geospatial Indexes`**

You cannot combine the `$text` query, which requires a
special text index, with a query operator
that requires a different type of special index. For example you
cannot combine `$text` query with the `$near` operator.

**`Fields with 2dsphere Indexes can only hold Geometries`**

Fields with 2dsphere indexes must hold geometry
data in the form of coordinate pairs
or GeoJSON data. If you attempt to insert a document with
non-geometry data in a `2dsphere` indexed field, or build a
`2dsphere` index on a collection where the indexed field has
non-geometry data, the operation will fail.

**See also:**

The unique indexes limit in limits-sharding-operations.

**`Limited Number of 2dsphere index keys`**

To generate keys for a 2dsphere index, `mongod` maps
GeoJSON shapes to an internal
representation. The resulting internal representation may be a large
array of values.

When `mongod` generates index keys on a field that holds an
array, `mongod` generates an index key for each array element.
For compound indexes, `mongod` calculates the cartesian
product of the sets of keys that are generated for each field. If both
sets are large, then calculating the cartesian product could cause the
operation to exceed memory limits.

`indexMaxNumGeneratedKeysPerDocument` limits the maximum
number of keys generated for a single document to prevent out of
memory errors. The default is 100000 index keys per document. It is
possible to raise the limit, but if an operation requires more keys
than the `indexMaxNumGeneratedKeysPerDocument` parameter
specifies, the operation will fail.

**`NaN values returned from Covered Queries by the WiredTiger Storage Engine are always of type double`**

If the value of a field returned from a query that is covered
by an index is `NaN`, the type of that `NaN`
value is *always* `double`.

**`Multikey Index`**

Multikey indexes cannot cover queries 
over array field(s).

**`Geospatial Index`**

Geospatial indexes cannot
cover a query.

**`Memory Usage in Index Builds`**

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

- For feature compatibility version (fcv) `"4.2"`
  and later, the index build memory limit applies to all index builds.

Index builds may be initiated either by a user command
such as Create Index
or by an administrative process such as an
initial sync.
Both are subject to the limit set by
`maxIndexBuildMemoryUsageMegabytes`.

An initial sync operation populates
only one collection at a time and has no risk of exceeding the memory
limit. However, it is possible for a user to start index
builds on multiple collections in multiple databases simultaneously
and potentially consume an amount of memory greater than the limit
set in `maxIndexBuildMemoryUsageMegabytes`.

**Tip:**

To minimize the impact of building an index on replica sets and
sharded clusters with replica set shards, use a rolling index build
procedure as described on
/tutorial/build-indexes-on-replica-sets.

**`Collation and Index Types`**

The following index types only support simple binary comparison and
do not support collation:

- text indexes, 

- 2d indexes, and 

- geoHaystack indexes.

**Tip:**

To create a `text`, a `2d`, or a `geoHaystack` index on a
collection that has a non-simple collation, you must explicitly
specify `{collation: {locale: "simple"} }` when creating the
index.

**`Hidden Indexes`**

- You cannot hide the `_id` index.

- You cannot use `hint()` on a hidden index.

## Sorts

**`Maximum Number of Sort Keys`**

- You can sort on a maximum of 32 keys.
- Providing a sort pattern with duplicate fields causes an error. 

## Data

**`Maximum Number of Documents in a Capped Collection`**

If you specify the maximum number of documents in a capped
collection with `create`'s `max` parameter, the value
must be less than 2`31` documents. 

If you do not specify a maximum number of documents when creating a 
capped collection, there is no limit on the number of documents.

## Replica Sets

**`Number of Members of a Replica Set`**

Replica sets can have up to 50 members.

**`Number of Voting Members of a Replica Set`**

Replica sets can have up to 7 voting members. For replica sets with
more than 7 total members, see replica-set-non-voting-members.

**`Maximum Size of Auto-Created Oplog`**

If you do not explicitly specify an oplog size (i.e. with
`oplogSizeMB` or `--oplogSize`) MongoDB will create an oplog that is no
larger than 50 gigabytes. [#oplog]_

## Sharded Clusters

Sharded clusters have the restrictions and thresholds described here.

### Sharding Operational Restrictions

**`Operations Unavailable in Sharded Environments`**

`$where` does not permit references to the `db` object
from the `$where` function. This is uncommon in
un-sharded collections.

The `geoSearch` command is not supported in sharded
environments.

In MongoDB 5.0 and earlier, you cannot specify sharded collections in the `from` parameter of `$lookup` stages.

**`Covered Queries in Sharded Clusters`**

When run on `mongos`, indexes can only cover queries on 
sharded collections if the index contains
the shard key.

**`Single Document Modification Operations in Sharded Collections`**

To use `update` and `remove()` operations for a sharded
collection that specify the `justOne` or `multi: false` option: 

- If you only target one shard, you can use a partial shard key in the query specification or,

- You can provide the shard key or the `_id` field in the query
  specification.

**`Unique Indexes in Sharded Collections`**

MongoDB does not support unique indexes across shards, except when
the unique index contains the full shard key as a prefix of the
index. In these situations MongoDB will enforce uniqueness across
the full key, not a single field.

**See also:**

shard-key-arbitrary-uniqueness for an alternate approach.

**`Maximum Number of Documents Per Range to Migrate`**

By default, MongoDB cannot move a range if the number of documents in
the range is greater than 2 times the result of dividing the
configured range size by the average
document size. If MongoDB can move a sub-range of a chunk and reduce the 
size to less than that, the balancer does so by migrating a range.
`db.collection.stats()` includes the `avgObjSize` field, 
which represents the average document size in the collection.       

For chunks that are too large to migrate:

- The balancer setting `attemptToBalanceJumboChunks` allows the
  balancer to migrate chunks too large to move as long as the chunks
  are not labeled jumbo. See
  balance-chunks-that-exceed-size-limit for details.

  When issuing `moveRange` and `moveChunk` 
  commands, it's possible to specify the forceJumbo option to allow for the migration of ranges 
  that are too large to move. The ranges may or may not be labeled 
  jumbo.

### Shard Key Limitations

**`Shard Key Index Type`**

A shard key index can be an ascending index on the shard
key, a compound index that starts with the shard key and specifies
ascending order for the shard key, or a hashed index.

A shard key index *cannot* be:

- A descending index on the shard key
- A partial index 
- Any of the following index types: 

  - Geospatial
  - Multikey
  - Text
  - Wildcard

**`Shard Key Selection`**

Your options for changing a shard key depend on the version of
MongoDB that you are running:

- Starting in MongoDB 5.0, you can reshard a collection by changing a document's shard key.
- You can refine a shard key by adding a suffix 
  field or fields to the existing shard key.

**`Monotonically Increasing Shard Keys Can Limit Insert Throughput`**

For clusters with high insert volumes, a shard key with
monotonically increasing and decreasing keys can affect insert
throughput. If your shard key is the `_id` field, be aware that
the default values of the `_id` fields are ObjectIds which have generally increasing values.

When inserting documents with monotonically increasing shard keys, all inserts
belong to the same chunk on a single shard. The system
eventually divides the chunk range that receives all write operations and
migrates its contents to distribute data more evenly. However, at any moment
the cluster directs insert operations only to a single shard, which creates an
insert throughput bottleneck.

If the operations on the cluster are predominately read operations
and updates, this limitation may not affect the cluster.

To avoid this constraint, use a hashed shard key or select a field that does not
increase or decrease monotonically.

Hashed shard keys and hashed
indexes store hashes of keys with ascending values.

## Operations

**`Sort Operations`**

If MongoDB cannot use an index or indexes to obtain the sort order,
MongoDB must perform an in-memory sort operation on the data. 

For more information on sorts and index use, see
sort-index-use.

**`Aggregation Pipeline Stages`**

MongoDB limits the number of aggregation pipeline stages allowed in a single 
pipeline to 1000. 

If an aggregation pipeline exceeds the stage limit before or after being parsed, 
you receive an error. 

**`Aggregation Pipeline Memory`**

Starting in MongoDB 6.0, the `allowDiskUseByDefault` 
parameter controls whether pipeline stages that require more than 100 
megabytes of memory to execute write temporary files to disk by 
default.

- If `allowDiskUseByDefault` is set to `true`, pipeline
  stages that require more than 100 megabytes of memory to execute 
  write temporary files to disk by default. You can disable writing 
  temporary files to disk for specific `find` or `aggregate` 
  commands using the `{ allowDiskUse: false }` option.

- If `allowDiskUseByDefault` is set to `false`, pipeline
  stages that require more than 100 megabytes of memory to execute 
  raise an error by default. You can enable writing temporary files to 
  disk for specific `find` or `aggregate` using 
  the `{ allowDiskUse: true }` option.

The `$search` aggregation stage is not restricted to 
100 megabytes of RAM because it runs in a separate process.

Examples of stages that can write temporary files to disk when 
allowDiskUse is `true` are:

- `$bucket`
- `$bucketAuto`
- `$group`
- `$setWindowFields`
- `$sort` when the sort operation is not supported by an
  index
- `$sortByCount`

**Note:**

Pipeline stages operate on streams of documents with each pipeline
stage taking in documents, processing them, and then outputing the
resulting documents.

Some stages can't output any documents until they have processed all
incoming documents. These pipeline stages must keep their stage
output in RAM until all incoming documents are processed. As a
result, these pipeline stages may require more space than the 100 MB
limit.

If the results of one of your `$sort` pipeline stages exceed
the limit, consider adding a $limit stage.

The profiler log messages and diagnostic log
messages includes a `usedDisk`
indicator if any aggregation stage wrote data to temporary files due
to memory restrictions.

**`Aggregation and Read Concern`**

- .. include:: /includes/extracts/4.2-changes-out-linearizable.rst

- .. include:: /includes/extracts/4.2-changes-linearizable-merge-restriction.rst

**`2d Geospatial queries cannot use the $or operator`**

**See also:**

- `$or`

- /core/geospatial-indexes

**`Geospatial Queries`**

For spherical queries, use the `2dsphere` index result.

The use of `2d` index for spherical queries may lead to incorrect
results, such as the use of the `2d` index for spherical queries
that wrap around the poles.

**`Geospatial Coordinates`**

- Valid longitude values are between `-180` and `180`, both
  inclusive.

- Valid latitude values are between `-90` and `90`, both
  inclusive.

**`Area of GeoJSON Polygons`**

For `$geoIntersects` or `$geoWithin`, if you specify a single-ringed polygon that
has an area greater than a single hemisphere, include `the
custom MongoDB coordinate reference system in the $geometry` expression; otherwise, `$geoIntersects` or `$geoWithin` queries for
the complementary geometry. For all other GeoJSON polygons with areas
greater than a hemisphere, `$geoIntersects` or `$geoWithin` queries for the
complementary geometry.

**`Multi-document Transactions`**

For multi-document transactions:

- You can create collections and indexes in transactions. For
  details, see transactions-create-collections-indexes

- The collections used in a transaction can be in different
  databases.

  **Note:**

  You cannot create new collections in cross-shard write transactions.
  For example, if you write to an existing collection in one shard and
  implicitly create a collection in a different shard, MongoDB cannot
  perform both operations in the same transaction.

- You cannot write to capped
  collections.

- You cannot use read concern `"snapshot"` when reading
  from a capped collection.
  (Starting in MongoDB 5.0)

- You cannot read/write to collections in the `config`, `admin`,
  or `local` databases.

- You cannot write to `system.*` collections.

- You cannot return the supported operation's query plan using 
  `explain` or similar commands.

- For cursors created outside of a transaction, you cannot call
  `getMore` inside the transaction.

- For cursors created in a transaction, you cannot call
  `getMore` outside the transaction.

- .. include:: /includes/extracts/transactions-killop-change.rst

The following operations are not allowed in transactions:

- Creating new collections in cross-shard write transactions. For
  example, if you write to an existing collection in one shard and
  implicitly create a collection in a different shard, MongoDB cannot
  perform both operations in the same transaction.

- Explicit creation of collections, e.g.
  `db.createCollection()` method, and indexes, e.g.
  `db.collection.createIndexes()` and
  `db.collection.createIndex()` methods, when using a read
  concern level other than `"local"`.

- The `listCollections` and `listIndexes`
  commands and their helper methods.

- Other non-CRUD and non-informational operations, such as
  `createUser`, `getParameter`,
  `count`, etc. and their helpers.

Transactions have a lifetime limit as specified by
`transactionLifetimeLimitSeconds`. The default is 60 seconds.

**`Write Command Batch Limit Size`**

`100,000` writes are
allowed in a single batch operation, defined by a single request to
the server.

The `Bulk()` operations in `mongosh` and
comparable methods in the drivers do not have this limit.

**`Views`**

A view definition `pipeline` cannot include the `$out` or
the `$merge` stage. This restriction also applies to
embedded pipelines, such as pipelines used in `$lookup` or
`$facet` stages.

Views have the following operation restrictions:

- Views are read-only.

- .. include:: /includes/extracts/views-unsupported-rename.rst

- .. include:: /includes/extracts/views-unsupported-projection-operators.rst

- .. include:: /includes/extracts/views-unsupported-text-search.rst

- .. include:: /includes/extracts/views-unsupported-mapReduce.rst

**`Projection Restrictions`**

`$`-Prefixed Field Path Restriction

   The `find` and `findAndModify` projection cannot project a field that starts with 
   `$` with the exception of the DBRef fields.

   For example, the following operation is invalid:

   ```javascript
   db.inventory.find( {}, { "$instock.warehouse": 0, "$item": 0, "detail.$price": 1 } )
   ```

`$` Positional Operator Placement Restriction

   The `$` projection operator can only appear at the end of the 
   field path, for example `"field.$"` or `"fieldA.fieldB.$"`.

   For example, the following operation is invalid:

   ```javascript
   db.inventory.find( { }, { "instock.$.qty": 1 } )
   ```

   To resolve, remove the component of the field path that follows the
   `$` projection operator.

Empty Field Name Projection Restriction

   `find` and `findAndModify` projection cannot include a projection of an empty field 
   name. 

   For example, the following operation is invalid:

   ```javascript
   db.inventory.find( { }, { "": 0 } ) 
   ```

   In previous versions, MongoDB treats the inclusion/exclusion of the
   empty field as it would the projection of non-existing fields.

Path Collision: Embedded Documents and Its Fields

   You cannot project an embedded document with any of the embedded 
   document's fields.

   For example, consider a collection `inventory` with documents that
   contain a `size` field:

   ```javascript
   { ..., size: { h: 10, w: 15.25, uom: "cm" }, ... }
   ```

   The following operation fails with a `Path collision` error because it 
   attempts to project both `size` document and the `size.uom` field:

   ```javascript
   db.inventory.find( {}, { size: 1, "size.uom": 1 } ) 
   ```

   In previous versions, lattermost projection between the embedded
   documents and its fields determines the projection:

   - If the projection of the embedded document comes after any and all
     projections of its fields, MongoDB projects the embedded document.
     For example, the projection document `{ "size.uom": 1, size: 1 }`
     produces the same result as the projection document `{ size: 1 }`.

   - If the projection of the embedded document comes before the
     projection any of its fields, MongoDB projects the specified field or
     fields. For example, the projection document ``{ "size.uom": 1, size:
     1, "size.h": 1 }`` produces the same result as the projection
     document `{ "size.uom": 1, "size.h": 1 }`.

Path Collision: `$slice` of an Array and Embedded Fields

   `find` and `findAndModify` projection cannot contain both a `$slice` of an 
   array and a field embedded in the array. 

   For example, consider a collection `inventory` that contains an array
   field `instock`:

   ```javascript
   { ..., instock: [ { warehouse: "A", qty: 35 }, { warehouse: "B", qty: 15 }, { warehouse: "C", qty: 35 } ], ... }
   ```

   The following operation fails with a ``Path
   collision`` error:

   ```javascript
   db.inventory.find( {}, { "instock": { $slice: 1 }, "instock.warehouse": 0 } ) 
   ```

   In previous versions, the projection applies both projections and
   returns the first element (`$slice: 1`) in the `instock` array
   but suppresses the `warehouse` field in the projected element.
   Starting in MongoDB 4.4, to achieve the same result, use the
   `db.collection.aggregate()` method with two separate
   `$project` stages.

`$` Positional Operator and `$slice` Restriction

   `find` and `findAndModify` projection cannot include `$slice` projection 
   expression as part of a `$` projection expression. 

   For example, the following operation is invalid:

   ```javascript
   db.inventory.find( { "instock.qty": { $gt: 25 } }, { "instock.$": { $slice: 1 } } ) 
   ```

   In previous versions, MongoDB returns the first element
   (`instock.$`) in the `instock` array that matches the query
   condition; i.e. the positional projection `"instock.$"` takes
   precedence and the `$slice:1` is a no-op. The ``"instock.$": {
   $slice: 1 }`` does not exclude any other document field.

    

## Sessions

**`Sessions and $external Username Limit`**

To use sessions with `$external` authentication users
(Kerberos, LDAP, or X.509 users), usernames cannot be greater
than 10k bytes.

**`Session Idle Timeout`**

Sessions that receive no read or write operations for 30 minutes *or*
that are not refreshed using `refreshSessions` within this
threshold are marked as expired and can be closed by the MongoDB
server at any time. Closing a session kills any in-progress
operations and open cursors associated with the session. This
includes cursors configured with `noCursorTimeout` or
a `maxTimeMS` greater than 30 minutes.

Consider an application that issues a `db.collection.find()`.
The server returns a cursor along with a batch of documents defined
by the `cursor.batchSize()` of the
`find()`. The session refreshes each time the
application requests a new batch of documents from the server.
However, if the application takes longer than 30 minutes to process
the current batch of documents, the session is marked as expired and
closed. When the application requests the next batch of documents,
the server returns an error as the cursor was killed when the session
was closed.

For operations that return a cursor, if the cursor may be idle for
longer than 30 minutes, issue the operation within an explicit
session using `Mongo.startSession()` and periodically
refresh the session using the `refreshSessions` command.
For example:

```bash
var session = db.getMongo().startSession()
var sessionId = session
sessionId  // show the sessionId

var cursor = session.getDatabase("examples").getCollection("data").find().noCursorTimeout()
var refreshTimestamp = new Date() // take note of time at operation start

while (cursor.hasNext()) {

  // Check if more than 5 minutes have passed since the last refresh
  if ( (new Date()-refreshTimestamp)/1000 > 300 ) { 
    print("refreshing session")
    db.adminCommand({"refreshSessions" : [sessionId]})
    refreshTimestamp = new Date()
  }

  // process cursor normally

}
```

In the example operation, the `db.collection.find()` method
is associated with an explicit session. The cursor is configured with
`noCursorTimeout()` to prevent the server from
closing the cursor if idle. The `while` loop includes a block that
uses `refreshSessions` to refresh the session every 5
minutes. Since the session will never exceed the 30 minute idle
timeout, the cursor can remain open indefinitely.

For MongoDB drivers, defer to the `driver documentation` for instructions and syntax for creating sessions.
