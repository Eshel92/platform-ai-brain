<!-- Converted from reference/command/collMod.txt (reStructuredText). Includes are inlined. -->

# collMod (database command)

## Definition

**`collMod`**

`collMod` makes it possible to add options to a 
collection or to modify view definitions.

   `unhideIndex` helper methods

**Tip:**

In `mongosh`, this command can also be run through the `hideIndex` and.

Helper methods are convenient for `mongosh` users, but they may not
return the same level of information as database commands.  In cases where
the convenience is not needed or the additional return fields are required,
use the database command.

**Note:**

The view modified by `collMod` does not refer to materialized
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

The command has the following syntax:

```javascript
db.runCommand( 
   { 
     collMod: <collection or view>, 
     <option1>: <value1>, 
     <option2>: <value2>,
     ... 
   } 
)
```

For the `<collection or view>`, specify the name of a collection
or view in the current database.

## Options

### Change Index Properties

To change index options, specify either the key pattern or name of the
existing index options you want to change:

```javascript
db.runCommand( {
   collMod: <collection>,
   index: {
      keyPattern: <index_spec> | name: <index_name>,
      expireAfterSeconds: <number>,  // Set the TTL expiration threshold
      hidden: <boolean>,             // Change index visibility in the query planner
      prepareUnique: <boolean>,      // Reject new duplicate index entries 
      unique: <boolean>              // Convert an index to a unique index
   },
   dryRun: <boolean>
} )
```

If the index does not exist, the command errors with the message
`"cannot find index <name|keyPattern> for ns <db.collection>"`.

**`index`**

The `index` option can change the following properties of
an **existing** index:

* - Index Property
  - Description

* - `expireAfterSeconds`
  - The number of seconds that determines the expiration
    threshold of a TTL Collection.

    If successful, the command returns a document that contains:

    - `expireAfterSeconds_new`, the new value for
      `expireAfterSeconds`
    - `expireAfterSeconds_old`, the old value for
      `expireAfterSeconds`, if the index had a value for
      `expireAfterSeconds` before.

    Modifying the index option `expireAfterSeconds` resets the
    `$indexStats` for the index.

    If you use TTL indexes created before MongoDB 5.0, or if you want to
    sync data created in MongDB 5.0 with a pre-5.0 installation, see
    expireData-warning to avoid misconfiguration issues.

    (Include not available offline: includes/expireAfterSeconds-range.rst)

* - `hidden`
  - A boolean that determines whether the index is hidden or not from the query planner.

    If the `hidden` value changes, the command returns a
    document that contains both the old and new values for the
    changed property: `hidden_old` and `hidden_new`.

    However, if the `hidden` value has not changed (i.e. hiding
    an already hidden index or unhiding an already unhidden
    index), the command omits the `hidden_old` and
    `hidden_new` fields from the output.

    To hide an index, you must have
    featureCompatibilityVersion set to `4.4`
    or greater.

    Modifying the index option `hidden` resets the
    `$indexStats` for the index if the value changes.

* - `prepareUnique`
  - A boolean that determines whether the index will accept
    new duplicate entries.

    New duplicate entries fail with DuplicateKey errors when
    `prepareUnique` is `true`. The resulting index can be
    converted to a unique index. To convert the index, use
    `collMod` with the `unique` option.

    If an existing index is updated so that `prepareUnique` is
    `true`, the index is not checked for pre-existing,
    duplicate index entries.

    **New in version:** 6.0

* - `unique`
  - A boolean that determines whether the index is unique.

    A value of `false` is not supported.

    When `unique` is `true`, `collMod` scans the
    `keyPattern` index for duplicates and then converts it to
    a unique index if there are no duplicate index entries.

    If duplicates are detected during the initial scan,
    `collMod` returns `CannotConvertIndexToUnique` and a list
    of conflicting documents. To convert an index with duplicate
    entries to a unique index, correct any reported conflicts and
    rerun `collMod`.

    To end a conversion, set `prepareUnique` to `false`.

    To see an example of how to convert a non-unique index to a
    unique index, see index-convert-to-unique.

    **New in version:** 6.0

**`dryRun`**

*Default value:* `false`

Only used when `index.unique` is `true`.

Before you convert a non-unique index to a unique index, you can run
the `collMod` command with `dryRun: true`. If you do, MongoDB
checks the collection for duplicate keys and returns any violations.

Use `dryRun: true` to confirm that you can convert an index to be
unique without any errors.

**Note:**

If the response containing all conflicting document `_id` values
exceeds 8MB, MongoDB returns the following error message instead of
listing the specific violations:

```none
Cannot convert the index to unique. Too many conflicting documents
were detected. Please resolve them and rerun collMod.
```

In this case, resolve duplicate entries until the response
is under 8MB, then run `collMod` again to see the remaining
violations.

### Validate Documents

**`validator`**

`validator` allows users to specify validation rules
or expressions for a collection.

The `validator` option takes a document that specifies the
validation rules or expressions. You can specify the expressions
using the same operators as the query operators with the exception of `$near`,
`$nearSphere`, `$text`, and `$where`.

**Note:**

- Validation occurs during updates and inserts. Existing
  documents do not undergo validation checks until modification.

- You cannot specify a validator for collections in the `admin`,
  `local`, and `config` databases.

- You cannot specify a validator for `system.*` collections.

**`validationLevel`**

The `validationLevel` determines how strictly MongoDB applies the
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

To see an example that uses `validationLevel`, see
schema-specify-validation-level.

**`validationAction`**

The `validationAction` option determines whether to `error` on
invalid documents or just `warn` about the violations but allow
invalid documents.

**Important:**

Validation of documents only applies to those documents as
determined by the `validationLevel`.

To see an example that uses `validationAction`, see
schema-validation-handle-invalid-docs.

### Modify Views

**Note:**

The view modified by this command does not refer to materialized
views. For discussion of on-demand materialized views, see
`$merge` instead.

**`viewOn`**

The underlying source collection or view. The view definition is determined by applying
the specified `pipeline` to this source.

Required if modifying a view on a MongoDB deployment that is running
with access control.

**`pipeline`**

The aggregation pipeline that defines
the view.

**Note:**

A view definition `pipeline` cannot include the `$out` or
the `$merge` stage. This restriction also applies to
embedded pipelines, such as pipelines used in `$lookup` or
`$facet` stages.

Required if modifying a view on a MongoDB deployment that is running
with access control.

The view definition is public; i.e. `db.getCollectionInfos()`
and `explain` operations on the view will include the pipeline that
defines the view. As such, avoid referring directly to sensitive fields
and values in view definitions.

```javascript
db.runCommand( {
   collMod: "myView",
   viewOn: "activities",
   pipeline: [
     { $match: { status: "Q" } },
     { $project: { user: 1, date: 1, description: 1} } ]
} )
```

### Modify Time Series Collections

**`expireAfterSeconds`**

**Note:**

This is distinct from using the `index` option with the
`expireAfterSeconds` property to change the expiration time
for a TTL Collection.

To enable automatic document removal or modify the current 
expiration interval for a time series collection, change the `expireAfterSeconds`
value:

```javascript
db.runCommand( {
   collMod: <collection>,
   expireAfterSeconds: <number> | "off"
} )
```

Set `expireAfterSeconds` to `"off"` to disable automatic removal,
or a non-negative decimal number (`>=0`) to specify the number of
seconds after which documents expire.

**See also:**

manual-timeseries-automatic-removal

**`granularity`**

To modify the granularity of a time 
series collection, you can increase `timeseries.granularity` from a shorter unit of time to a longer one:

```javascript
db.runCommand( {
   collMod: "weather24h",
   timeseries: { granularity: "seconds" | "minutes" | "hours" }
} )
```

To update the custom bucketing parameters `bucketRoundingSeconds`
and `bucketMaxSpanSeconds` instead of `granularity`, include both
custom parameters in the `collMod` command and set them to the 
same value:

```javascript
db.runCommand( {
   collMod: "weather24h",
   timeseries: { 
      bucketRoundingSeconds: 86400,
      bucketMaxSpanSeconds: 86400 
   }
} )
```

You cannot decrease the granularity interval or the custom bucketing
values.

**Important:**

You cannot downgrade below MongoDB 6.3 if any time series 
collections explicitly specify the custom bucketing parameters 
`bucketMaxSpanSeconds` and `bucketRoundingSeconds`. If 
possible, convert to the corresponding `granularity`. If you 
cannot, you must drop the collection before downgrading.

To convert a collection from custom bucketing to a `granularity`,
value, both `bucketMaxSpanSeconds` and `bucketRoundingSeconds`
must be less than or equal to the `granularity` equivalent:

| `granularity` | `bucketRoundingSeconds` limit (inclusive) | `bucketMaxSpanSeconds` limit (inclusive) |
|---|---|---|
| `seconds` | 60 | 3600 |
| `minutes` | 3600 | 86400 |
| `hours` | 86400 | 2592000 |

**See also:**

timeseries-granularity

### Resize a Capped Collection

**New in version:** 6.0

Starting in MongoDB 6.0, you can resize a capped collection. To change a
capped collection's maximum size in
bytes, use the `cappedSize` option. To change the maximum number of
documents in an existing capped collection, use the `cappedMax` option.

**Note:**

You can't use these commands to resize the oplog. Use 
`replSetResizeOplog` instead. 

**`cappedSize`**

Specifies a new maximum size, in bytes, for a capped collection. `cappedSize`
must be greater than `0` and less than `1e+15` (1 PB). 

**`cappedMax`**

Specifies a new maximum number of documents in a capped collection. Setting
`cappedMax` less than or equal to `0` implies no limit.

For example, the following command sets the maximum size of a capped collection 
to 100000 bytes and sets the maximum number of documents in the collection to 500:

```javascript
db.runCommand( {
   collMod: <collection>,
   cappedSize: 100000,
   cappedMax: 500
} )
```

### Change Streams with Document Pre- and Post-Images

**New in version:** 6.0

**`changeStreamPreAndPostImages`**

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

To use `collMod` to enable change stream pre- and post-images
for a collection, use the `changeStreamPreAndPostImages` field:

```javascript
db.runCommand( {
   collMod: <collection>,
   changeStreamPreAndPostImages: { enabled: <boolean> }
} )
```

To enable change stream pre- and post-images for a collection, set
`changeStreamPreAndPostImages` to `true`. For example:

```javascript
db.runCommand( {
   collMod: "orders",
   changeStreamPreAndPostImages: { enabled: true }
} )
```

To disable change stream pre- and post-images for a collection, set
`changeStreamPreAndPostImages` to `false`. For example:

```javascript
db.runCommand( {
   collMod: "orders",
   changeStreamPreAndPostImages: { enabled: false }
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

### Attach Comment

**`comment`**

Optional. You can attach a comment to this command. The comment must be
a top-level field and can be any valid BSON type. 
The comment that you specify appears alongside records of this command
in the following locations:  
  
- mongod log messages, in the
  `attr.command.cursor.comment` field. 
- Database profiler output, in the
  `command.comment` field.
- `currentOp` output, in the `command.comment` field.

### Write Concern

**`w`**

Optional. A document expressing the write concern of the `collMod` command.

Omit to use the default write concern.

## Access Control

If the deployment enforces authentication/authorization, you must have
the following privilege to run the `collMod` command:

* - Task
  - Required Privileges

* - Modify a non-capped collection
  - `collMod` in the database

* - Modify a view
  - `collMod` in the database and either:

    - no `find` on the view to modify, **or**
    - both `find` on the view to modify and
      `find` on the source collection/view.

The built-in role `dbAdmin` provides the required privileges.

## Behavior

### Resource Locking

The `collMod` command obtains a collection lock on
the specified collection for the duration of the operation. 

## Examples

### Change Expiration Value for Indexes

The following example updates the `expireAfterSeconds` property of an
existing TTL index `{ lastAccess: 1 }` on a collection named
`user_log`. The current `expireAfterSeconds` property for the index
is set to `1800` seconds (or 30 minutes) and the example changes the
value to `3600` seconds (or 60 minutes).

```javascript
db.runCommand({ 
   collMod: "user_log",
   index: { 
      keyPattern: { lastAccess: 1 },
      expireAfterSeconds: 3600 
   }
})
```

If successful, the operation returns a document that includes both the
old and new value for the changed property:

```javascript
{ "expireAfterSeconds_old" : 1800, "expireAfterSeconds_new" : 3600, "ok" : 1 }
```

### Hide an Index from the Query Planner

**Note:**

To hide an index, you must have featureCompatibilityVersion set to `5.0` or greater.

The following example hides an existing
index on the `orders` collection. Specifically, the operation hides
the index with the specification `{ shippedDate: 1 }` from the query
planner.

```javascript
db.runCommand( {
   collMod: "orders",
   index: {
      keyPattern: { shippedDate: 1 },
      hidden: true
   }
} )
```

If successful, the operation returns a document that includes both the
old and new value for the changed property:

```javascript
{ "hidden_old" : false, "hidden_new" : true, "ok" : 1 }
```

**Note:**

If the operation is successful but the `hidden` value has not
changed (specifically, hiding an already hidden index or unhiding an already
unhidden index), the command omits the `hidden_old` and
`hidden_new` fields from the output.

To hide a text index, you must specify the index by `name` and not by
`keyPattern`.

**See also:**

- index-type-hidden
- `db.collection.hideIndex()`
- `db.collection.unhideIndex()`
