<!-- Converted from reference/command/create.txt (reStructuredText). Includes are inlined. -->

# create (database command)

## Definition

**`create`**

Explicitly creates a collection or view.

**Note:**

The view created by this command does not refer to materialized
views. For discussion of on-demand materialized views, see
`$merge` instead.

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

The `create` command has the following syntax:

**Note:**

MongoDB 6.3 adds the `bucketMaxSpanSeconds` and
`bucketRoundingSeconds` parameters. To downgrade below 6.3, you
must either drop all collections with these parameters, or modify
them to use the corresponding `granularity`, if possible. For 
details see `collMod`.

```javascript
db.runCommand(
   {
     create: <collection or view name>,
     capped: <true|false>,
     timeseries: {
        timeField: <string>,
        metaField: <string>,
        granularity: <string>,
        bucketMaxSpanSeconds: <timespan>,  // Added in MongoDB 6.3
        bucketRoundingSeconds: <timespan>  // Added in MongoDB 6.3
     },
     expireAfterSeconds: <number>,
     clusteredIndex: <document>,  // Added in MongoDB 5.3
     changeStreamPreAndPostImages: <document>,  // Added in MongoDB 6.0
     autoIndexId: <true|false>,
     size: <max_size>,
     max: <max_documents>,
     storageEngine: <document>,
     validator: <document>,
     validationLevel: <string>,
     validationAction: <string>,
     indexOptionDefaults: <document>,
     viewOn: <source>,
     pipeline: <pipeline>,
     collation: <document>,
     writeConcern: <document>,
     encryptedFields: <document>,
     comment: <any>
   }
```

    

### Command Fields

The `create` command has the following fields:

* - Field
  - Type
  - Description

* - `create`
  - string
  - The name of the new collection or view. See
    restrictions-on-db-names. If you try to create a
    collection or view that already exists and you provide identical
    options for that existing collection or view, no action is taken
    and success is returned.

* - `capped`
  - boolean
  - Optional. To create a capped collection,
    specify `true`. If you specify `true`, you must also set a maximum
    size in the `size` field.

* - `timeseries.timeField`
  - string
  - Required when creating a time series collection. The
    name of the field which contains the date in each time series
    document. Documents in a time series collection must have a
    valid BSON date as the value for the `timeField`.

* - `timeseries.metaField`
  - string
  - Optional. The name of the field which contains metadata in
    each time series document. The metadata in the specified field
    should be data that is used to label a unique series of
    documents. The metadata should rarely, if ever, change.

    The name of the specified field may not be `_id` or the same
    as the `timeseries.timeField`. The field can be of any type
    except array.

* - `timeseries.granularity`

  - string

  - Optional, do not use if setting `bucketRoundingSeconds` and 
    `bucketMaxSpanSeconds`. Possible values are `seconds` (default), `minutes`, and `hours`.

    Set `granularity` to the value that most closely matches 
    the time between consecutive incoming timestamps. This improves 
    performance by optimizing how MongoDB internally stores data in 
    the collection.

    For more information on granularity and bucket intervals, see 
    timeseries-granularity.

* - `timeseries.bucketMaxSpanSeconds`

  - integer

  - Optional, used with `bucketRoundingSeconds` as an alternative
    to `granularity`. Sets the maximum time between timestamps in
    the same bucket. Possible values are 1-31536000. If you set
    `bucketMaxSpanSeconds`, you must set `bucketRoundingSeconds`
    to the same value.

    To downgrade below MongoDB 6.3, you must either modify the
    collection to use the corresponding `granularity` value, or
    drop the collection. For details, see `collMod`.

* - `timeseries.bucketRoundingSeconds`

  - integer

  - Optional, used with `bucketMaxSpanSeconds` as an alternative to
    `granularity`. Sets the number of seconds to round down by when
    MongoDB sets the minimum timestamp for a new bucket. Must be
    equal to `bucketMaxSpanSeconds`

    For example, setting both parameters to `1800` rounds new
    buckets down to the nearest 30 minutes. If a document with a time
    of `2023-03-27T18:24:35Z` does not fit an
    existing bucket, MongoDB creates a new bucket with a minimum time
    of `2023-03-27T18:00:00Z` and a maximum time of `2023-03-27T18:30:00Z`.

* - `expireAfterSeconds`

  - integer

  - Optional. Specifies the seconds after which documents in a
    time series collection or clustered collection
    expire. MongoDB deletes expired documents automatically.

* - `clusteredIndex`
  - document
  - .. _create.clusteredIndex:

    Starting in MongoDB 5.3, you can create a collection with a **clustered
    index**. Clustered indexes are stored in the same WiredTiger file as the collection. The resulting collection
    is called a clustered collection.

    The `clusteredIndex` field has the following syntax:

    ```javascript
    clusteredIndex: {
       key: <object>,
       unique: <boolean>,
       name: <string>
    }
    ```

    `key`
       Required. The clustered index key field. Must be set to ``{ _id:
       1 }`. The default value for the `_id`` field is an
       automatically generated unique object identifier, but you can set your own clustered index key
       values.

    `unique`
       Required. Must be set to `true`. A unique index indicates the
       collection will not accept inserted or updated documents where
       the clustered index key value matches an existing value in the
       index.

    `name`
       Optional. A name that uniquely identifies the clustered index.

    **New in version:** 5.3

* - `changeStreamPreAndPostImages`
  - document
  - .. _create.changeStreamPreAndPostImages:

    Optional.

    Starting in MongoDB 6.0, you can use change stream events to output the version of a document before and
    after changes (the document pre- and post-images):

    - The pre-image is the document before it was replaced, updated, or
      deleted. There is no pre-image for an inserted document.

    - The post-image is the document after it was inserted, replaced, or
      updated. There is no post-image for a deleted document.

    - Enable `changeStreamPreAndPostImages` for a collection using
      `db.createCollection()`, `create`, or
      `collMod`. For example, when using the `collMod` command: 

      ```javascript
      db.runCommand( { 
         collMod: <collection>,
         changeStreamPreAndPostImages: { enabled: true }
      } )
      ```

    To check the current `changeStreamPreAndPostImages` setting for a
    collection, run `db.getCollectionInfos()`:

    ```javascript
    db.getCollectionInfos( {
      name: "<collection>"
    } )[0].options.changeStreamPreAndPostImages
    ```

    Output:

    ```javascript
    { changeStreamPreAndPostImages: { enabled: true } }
    ```

    `changeStreamPreAndPostImages` has the following syntax:

    ```javascript
    changeStreamPreAndPostImages: {
       enabled: <boolean>
    }
    ```

    To enable change stream pre- and post-images for the collection, set `enabled`
    to `true`.

    For complete examples with the change stream output, see
    db.collection.watch-change-streams-pre-and-post-images-example.

    For a `create` example on this page, see
    create-change-stream-pre-and-post-images-example.

    **New in version:** 6.0

* - `size`
  - integer
  - Optional. Specify a maximum size in bytes for a capped collection. Once a
    capped collection reaches its maximum size, MongoDB removes the older
    documents to make space for the new documents. The `size` field is
    required for capped collections and ignored for other collections.

* - `max`
  - integer
  - Optional. The maximum number of documents allowed in the capped collection. The
    `size` limit takes precedence over this limit. If a capped
    collection reaches the `size` limit before it reaches the maximum
    number of documents, MongoDB removes old documents. If you prefer to
    use the `max` limit, ensure that the `size` limit, which is
    required for a capped collection, is sufficient to contain the
    maximum number of documents.

* - `storageEngine`
  - document
  - Optional. Available for the WiredTiger storage engine only.

    Allows users to specify configuration to the storage engine on a
    per-collection basis when creating a collection. The value of the
    `storageEngine` option should take the following form:

    ```javascript
    { <storage-engine-name>: <options> }
    ```

    Storage engine configuration specified when creating collections are
    validated and logged to the oplog during replication to
    support replica sets with members that use different storage
    engines.

    Starting in MongoDB 7.2 (and 7.0.5), you can't specify `wiredTiger` storage
    engine encryption options when you create a collection with 
    `db.createCollection()`. To configure encryption for 
    the WiredTiger storage engine, see security-encryption-at-rest. 

    For more information, see create-command-collection-storage-engine-options.

* - `validator`
  - document

  - Optional. Allows users to specify validation rules or
    expressions for the collection.

    The `validator` option takes a document that specifies the
    validation rules or expressions. You can specify the expressions
    using the same operators as the query operators with the exception of `$near`,
    `$nearSphere`, `$text`, and `$where`.

    - Validation occurs during updates and inserts. Existing
      documents do not undergo validation checks until modification.

    - You cannot specify a validator for collections in the `admin`,
      `local`, and `config` databases.

    - You cannot specify a validator for `system.*` collections.

* - `validationLevel`
  - string
  - Optional. Determines how strictly MongoDB applies the
    validation rules to existing documents during an update.

    `"off"`
        No validation for inserts or updates.

    `"strict"`
        **Default** Apply validation rules to all inserts and
        all updates.

    `"moderate"`
        Apply validation rules to inserts and to updates on
        existing *valid* documents. Do not apply rules to
        updates on existing *invalid* documents.

* - `validationAction`
  - string
  - Optional. Determines whether to `error` on invalid documents or just `warn`
    about the violations but allow invalid documents to be inserted.

    Validation of documents only applies to those documents as
    determined by the `validationLevel`.

    `"error"`
        **Default** Documents must pass validation before the
        write occurs. Otherwise, the write operation fails.

    `"warn"`
        Documents do not have to pass validation. If the
        document fails validation, the write operation logs
        the validation failure.

* - `indexOptionDefaults`
  - document
  - Optional. Allows users to specify a default configuration for indexes when
    creating a collection.

    The `indexOptionDefaults` option accepts a `storageEngine`
    document, which should take the following form:

    ```javascript
    { <storage-engine-name>: <options> }
    ```

    Storage engine configuration specified when creating indexes are
    validated and logged to the oplog during replication to
    support replica sets with members that use different storage
    engines.

* - `viewOn`
  - string
  - The name of the source collection or view from which to create the
    view. The name is not the full namespace of the collection or
    view; i.e. does not include the database name and implies the same
    database as the view to create. You must create views in the same
    database as the source collection.

    See also `db.createView()`.

* - `pipeline`
  - array
  - An array that consists of the aggregation pipeline stage(s). `create` creates the view by
    applying the specified `pipeline` to the `viewOn` collection or view.

    A view definition `pipeline` cannot include the `$out` or
    the `$merge` stage. This restriction also applies to
    embedded pipelines, such as pipelines used in `$lookup` or
    `$facet` stages.

    The view definition is public; i.e. `db.getCollectionInfos()`
    and `explain` operations on the view will include the pipeline that
    defines the view. As such, avoid referring directly to sensitive fields
    and values in view definitions.

    See also `db.createView()`.

* - `collation`
  - 
  - Specifies the default collation for the
    collection or the view.

    Collation allows users to specify
    language-specific rules for string comparison, such as rules for
    lettercase and accent marks.

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

    If you specify a collation at the collection level:

    - Indexes on that collection will be created with that collation unless
      the index creation operation explicitly specify a different collation.

    - Operations on that collection use the collection's default
      collation unless they explicitly specify a different collation.

      You cannot specify multiple collations for an operation. For
      example, you cannot specify different collations per field, or if
      performing a find with a sort, you cannot use one collation for the
      find and another for the sort.

    If no collation is specified for the collection or for the
    operations, MongoDB uses the simple binary comparison used in prior
    versions for string comparisons.

    For a view, if no collation is specified, the view's default
    collation is the "simple" binary comparison collator. For a view on
    a collection, the view does not inherit the collection's collation
    settings. For a view on another view, the to be created view must
    specify the same collation settings.

    After you create the collection or the view, you cannot update its
    default collation.

    For an example that specifies the default collation during the
    creation of a collection, see create-collation-example.

* - `writeConcern`

  - document

  - Optional. A document that expresses the write concern
    for the operation. Omit to use the default write
    concern.

    When issued on a sharded cluster, `mongos` converts the
    write concern of the
    `create` command and its helper
    `db.createCollection()` to `"majority"`.

* - `encryptedFields`    
  - document
  - Optional. A document that configures Queryable Encryption for the collection being created.

    To use encrypted fields in a collection, specify a new configuration
    option. You must have permissions to create and modify a collection to
    set this configuration during collection creation. After you create a
    collection, the `encryptedFields` value is immutable.

    The configuration includes a list of fields and their corresponding key 
    identifiers, types, and supported queries.

    ```javascript
    encryptedFieldsConfig = {
        "fields": [
          {
            "keyId": UUID,                    // required
            "path": String,                   // path to field, required
            "bsonType": "string" | "int" ..., // required
            "queries":                        // optional
            [ 
              { "queryType": "equality" },
            ]
          }
        ]
    }
    ```

    For details, see qe-tutorials.

* - `comment`
  - any
  - .. include:: /includes/extracts/comment-content.rst
 
The `db.createCollection()` method and the
`db.createView()` method wrap the `create`
command.

## Behavior

`create` has the following behavior:

### Resource Locking

`create` obtains an exclusive lock on the
specified collection or view for the duration of the operation. All
subsequent operations on the collection must wait until 
`create` releases the lock. `create` typically holds
this lock for a short time. 

Creating a view requires obtaining an additional exclusive lock
on the `system.views` collection in the database. This lock blocks
creation or modification of views in the database until the command
completes.

### Transactions

You can create collections and indexes inside a distributed 
transaction if the
transaction is not a cross-shard write transaction.

To use `create` in a transaction, the transaction must use read
concern `"local"`. If you specify a read concern level
other than `"local"`, the transaction fails.

**See also:**

transactions-create-collections-indexes

### Collection or View with Same Name and Options

If you run `create` with the same name and options as an existing 
collection or view, `create` returns success.

### Stable API

**Changed in version:** 5.0

When using Stable API V1, you cannot specify
the following fields in a `create` command:

- `autoIndexId`
- `capped`
- `indexOptionDefaults`
- `max`
- `size`
- `storageEngine`

## Access Control

If the deployment enforces 
authentication/authorization, 
`create` requires the following privileges:

* - Task

  - Required Privileges

* - Create a non-capped collection

  - `createCollection` on the database, **or**

    `insert` on the collection to create

* - Create a capped collection

  - `convertToCapped` for the collection

    `createCollection` on the database

* - Create a view

  - `createCollection` on the database.

    However, if the user has the `createCollection` on
    the database *and* `find` on the view to create,
    the user must *also* have the following additional permissions:

    - `find` on the source collection or view.

    - `find` on any other collections or views
      referenced in the `pipeline`, if any.

A user with the `readWrite` built in role on the database
has the required privileges to run the listed operations. Either
create a user with the required role
or grant the role to an existing user.

## Examples

### Create a Capped Collection

To create a capped collection limited to 64 kilobytes, issue
the command in the following form:

```javascript
db.runCommand( { create: "collection", capped: true, size: 64 * 1024 } )
```

### Create a Time Series Collection

To create a time series collection that captures weather data
for the past 24 hours, issue this command:

```javascript
db.createCollection(
    "weather24h",
    {
       timeseries: {
          timeField: "timestamp",
          metaField: "data",
          granularity: "hours"
       },
       expireAfterSeconds: 86400
    }
)
```

Alternately, to create the same collection but limit each bucket to
timestamp values within the same hour, issue this command:

```javascript
db.createCollection(
    "weather24h",
    {
       timeseries: {
          timeField: "timestamp",
          metaField: "data",
          bucketMaxSpanSeconds: 3600,
          bucketRoundingSeconds: 3600
       },
       expireAfterSeconds: 86400
    }
)
```

**Note:**

In this example `expireAfterSeconds` is specified as `86400`
which means documents expire `86400` seconds after the
`timestamp` value. See manual-timeseries-automatic-removal.

### Create a Clustered Collection

The following `create` example adds a clustered
collection named `products`:

```javascript
db.runCommand( {
   create: "products",
   clusteredIndex: { "key": { _id: 1 }, "unique": true, "name": "products clustered key" }
} )
```

In the example, clusteredIndex
specifies:

- `"key": { _id: 1 }`, which sets the clustered index key to the
  `_id` field.

- `"unique": true`, which indicates the clustered index key value must
  be unique.

- `"name": "products clustered key"`, which sets the clustered index name.

### Create a Collection with Change Stream Pre- and Post-Images for Documents

Starting in MongoDB 6.0, you can use change stream events to output the version of a document before and
after changes (the document pre- and post-images):

- The pre-image is the document before it was replaced, updated, or
  deleted. There is no pre-image for an inserted document.

- The post-image is the document after it was inserted, replaced, or
  updated. There is no post-image for a deleted document.

- Enable `changeStreamPreAndPostImages` for a collection using
  `db.createCollection()`, `create`, or
  `collMod`. For example, when using the `collMod` command: 

  ```javascript
  db.runCommand( { 
     collMod: <collection>,
     changeStreamPreAndPostImages: { enabled: true }
  } )
  ```

To check the current `changeStreamPreAndPostImages` setting for a
collection, run `db.getCollectionInfos()`:

```javascript
db.getCollectionInfos( {
  name: "<collection>"
} )[0].options.changeStreamPreAndPostImages
```

Output:

```javascript
{ changeStreamPreAndPostImages: { enabled: true } }
```

The following example creates a collection that has
changeStreamPreAndPostImages enabled:

```javascript
db.runCommand( {
   create: "temperatureSensor",
   changeStreamPreAndPostImages: { enabled: true }
} )
```

Pre- and post-images are not available for a change stream event if the images were:

- Not enabled on the collection at the time of a document update or
  delete operation.

- Removed after the pre- and post-image retention time set in
  `expireAfterSeconds`.

  - The following example sets `expireAfterSeconds` to `100`
    seconds on an entire cluster:

    ```javascript
    use admin
    db.runCommand( {
       setClusterParameter:
          { changeStreamOptions: {
             preAndPostImages: { expireAfterSeconds: 100 }
          } }
    } )
    ```

    **Note:**

    The `setClusterParameter` command is not supported in MongoDB 
    Atlas clusters. For information on Atlas support for all commands, see 
    unsupported-commands.

  - The following example returns the current `changeStreamOptions`
    settings, including `expireAfterSeconds`:

    ```javascript
    db.adminCommand( { getClusterParameter: "changeStreamOptions" } )
    ```

  - Setting `expireAfterSeconds` to `off` uses the default retention
    policy: pre- and post-images are retained until the corresponding
    change stream events are removed from the oplog.

  - If a change stream event is removed from the oplog, then the
    corresponding pre- and post-images are also deleted regardless of
    the `expireAfterSeconds` pre- and post-image retention time.

Additional considerations:

- Enabling pre- and post-images consumes storage space and adds
  processing time. Only enable pre- and post-images if you need them.

- Limit the change stream event size to less than 16 mebibytes. To limit
  the event size, you can:

  - Limit the document size to 8 megabytes. You can request pre- and
    post-images simultaneously in the change stream output if other change stream event fields like
    `updateDescription` are not large.

  - Request only post-images in the change stream output for documents
    up to 16 mebibytes if other change stream event fields like
    `updateDescription` are not large.

  - Request only pre-images in the change stream output for documents up
    to 16 mebibytes if:

    - document updates affect only a small fraction of the document
      structure or content, *and*

    - do not cause a `replace` change event. A `replace` event
      always includes the post-image.

- To request a pre-image, you set `fullDocumentBeforeChange` to
  `required` or `whenAvailable` in `db.collection.watch()`.
  To request a post-image, you set `fullDocument` using the same
  method.

- Pre-images are written to the `config.system.preimages` collection.

  - The `config.system.preimages` collection may become large. To
    limit the collection size, you can set `expireAfterSeconds`
    time for the pre-images as shown earlier.

  - To monitor the size of `config.system.preimages`, connect to a
    shard node on a sharded cluster or a `mongod` node
    on a replica set. Then, run the following commands:

    ```javascript
    use config
    db.system.preimages.totalSize()
    db.system.preimages.stats()
    ```

    **Note:**

    You must have the `collStats` privilege action on the
    `config.system.preimages` collection to run these commands.

    To run these commands on an MongoDB Atlas deployment, you must have
    the `atlasAdmin` role.

  - Pre-images are removed asynchronously by a background process.

**Important:** Backward-Incompatible Feature

Starting in MongoDB 6.0, if you are using document pre- and post-images
for change streams, you must disable
changeStreamPreAndPostImages for each collection using
the `collMod` command before you can downgrade to an earlier
MongoDB version.

**See also:**

- For change stream events and output, see
  change-stream-output.

- To watch a collection for changes, see
  `db.collection.watch`.

- For complete examples with the change stream output, see
  db.collection.watch-change-streams-pre-and-post-images-example.

### Create a View

**Note:**

The view created by this command does not refer to materialized
views. For discussion of on-demand materialized views, see
`$merge` instead.

A view definition `pipeline` cannot include the `$out` or
the `$merge` stage. This restriction also applies to
embedded pipelines, such as pipelines used in `$lookup` or
`$facet` stages.

To create a view using the `create`
command, use the following syntax:

```javascript
db.runCommand( { create: <view>, viewOn: <source>, pipeline: <pipeline> } )
```

   
or if specifying a collation:

```javascript
db.runCommand( { create: <view>, viewOn: <source>, pipeline: <pipeline>, collation: <collation> } )
```

For example, create a `survey` collection with the following documents:

```javascript
db.survey.insertMany(
   [
      { _id: 1, empNumber: "abc123", feedback: { management: 3, environment: 3 }, department: "A" },
      { _id: 2, empNumber: "xyz987", feedback: { management: 2, environment: 3 }, department: "B" },
      { _id: 3, empNumber: "ijk555", feedback: { management: 3, environment: 4 }, department: "A" }
   ]
)
```

The following operation creates a `managementRatings` view with the
`_id`, `feedback.management`, and `department` fields:

```javascript
db.runCommand ( {
   create: "managementFeedback",
   viewOn: "survey",
   pipeline: [ { $project: { "management": "$feedback.management", department: 1 } } ]
} )
```

**Important:**

The view definition is public; i.e. `db.getCollectionInfos()`
and `explain` operations on the view will include the pipeline that
defines the view. As such, avoid referring directly to sensitive fields
and values in view definitions.

**See also:**

`db.createView()`

### Specify Collation

You can specify collation at the collection or
view level. For example, the following
operation creates a collection, specifying a collation for the
collection (See collation-document-fields for descriptions of
the collation fields):

```javascript
db.runCommand ( {
   create: "myColl",
   collation: { locale: "fr" }
});
```

This collation will be used by indexes and operations that support
collation unless they explicitly specify a different collation. For
example, insert the following documents into `myColl`:

```javascript
{ _id: 1, category: "café" }
{ _id: 2, category: "cafe" }
{ _id: 3, category: "cafE" }
```

The following operation uses the collection's collation:

```javascript
db.myColl.find().sort( { category: 1 } )
```

The operation returns documents in the following order:

```javascript
{ "_id" : 2, "category" : "cafe" }
{ "_id" : 3, "category" : "cafE" }
{ "_id" : 1, "category" : "café" }
```

The same operation on a collection that uses simple binary collation
(i.e. no specific collation set) returns documents in the following order:

```javascript
{ "_id" : 3, "category" : "cafE" }
{ "_id" : 2, "category" : "cafe" }
{ "_id" : 1, "category" : "café" }
```

**See also:**

- create-view-w-collation
- ref-collation-and-views

### Specify Storage Engine Options

You can specify collection-specific storage engine configuration
options when you create a collection with
`db.createCollection()`. Consider the following operation:

```javascript
db.runCommand( {
    create: "users",
    storageEngine: { wiredTiger: { configString: "<option>=<setting>" } }
} )
```

This operation creates a new collection named `users` with a
specific configuration string that MongoDB will pass to the
`wiredTiger` storage engine. See the :wtdocs-v5.0:`WiredTiger documentation of
collection level options </struct_w_t___s_e_s_s_i_o_n.html>`
for specific `wiredTiger` options.

Starting in MongoDB 7.2 (and 7.0.5), you can't specify `wiredTiger` storage
engine encryption options when you create a collection with 
`db.createCollection()`. To configure encryption for 
the WiredTiger storage engine, see security-encryption-at-rest.
