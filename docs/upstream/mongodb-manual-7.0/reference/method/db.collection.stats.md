<!-- Converted from reference/method/db.collection.stats.txt (reStructuredText). Includes are inlined. -->

# db.collection.stats() (mongosh method)

(Include not available offline: includes/wayfinding/mongosh-method-stats.rst)

**Important:** `mongosh` Method

This page documents a `mongosh` method. This is *not*
the documentation for database commands or language-specific drivers,
such as Node.js. 

For the database command, see the `collStats` command.

For MongoDB API drivers, refer to the language-specific
`MongoDB driver documentation`.

## Definition

**`db.collection.stats(<option>)`**

Returns statistics about the collection.

:returns: A document that contains statistics on the specified
   collection. See `collStats` for a breakdown of the returned
   statistics.

**Note:**

`db.collection.stats()` internally calls the 
`$collStats` aggregation stage by default. 

## Syntax

The method has the following format:
   

```javascript
db.collection.stats({
   scale: <num>,                   // Optional
   indexDetails: <boolean>,        // Optional
   indexDetailsKey: <document>,    // Optional
   indexDetailsName: <string>.     // Optional
})
```

## Fields

| Field | Type | Description |
|---|---|---|
| `scale` | number | Optional. The scale factor for the various size data. The `scale` defaults to 1 to return size data in bytes. To display kilobytes rather than bytes, specify a `scale` value of `1024`. If you specify a non-integer scale factor, MongoDB uses the integer part of the specified factor. For example, if you specify a scale factor of `1023.999`, MongoDB uses `1023` as the scale factor. Starting in version 4.2, the output includes the `scaleFactor` used to scale the size values. |
| `indexDetails` | boolean | Optional. If `true`, `db.collection.stats()` returns `index details` in addition to the collection stats. Only works for WiredTiger storage engine. Defaults to `false`. |
| `indexDetailsKey` | document | Optional. If `indexDetails` is `true`, you can use `indexDetailsKey` to filter index details by specifying the index key specification. Only the index that exactly matches `indexDetailsKey` will be returned. If no match is found, `indexDetails` will display statistics for all indexes. Use `getIndexes()` to discover index keys. You cannot use `indexDetailsKey` with `indexDetailsName`. |
| `indexDetailsName` | string | Optional. If `indexDetails` is `true`, you can use `indexDetailsName` to filter index details by specifying the index `name`. Only the index name that exactly matches `indexDetailsName` will be returned. If no match is found, `indexDetails` will display statistics for all indexes. Use `getIndexes()` to discover index names. You cannot use `indexDetailsName` with `indexDetailsField`. |

To specify just the `scale` factor, MongoDB supports the legacy
format:
   

```javascript
db.collection.stats(<number>)
```

## Compatibility

This method is available in deployments hosted in the following environments:

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

## Behavior

### Scaled Sizes

Unless otherwise specified by the metric name (such as ``"bytes
currently in the cache"``), values related to size are displayed in
bytes and can be overridden by `scale`.

The scale factor rounds the affected size values to whole numbers.

### Storage Engine

Depending on the storage engine, the data returned may differ. For details on
the fields, see output details.

### Accuracy after Unexpected Shutdown

After an unclean shutdown of a `mongod` using the Wired Tiger storage engine, count and size statistics reported by
`db.collection.stats()` may be inaccurate.

The amount of drift depends on the number of insert, update, or delete
operations performed between the last checkpoint and the unclean shutdown. Checkpoints
usually occur every 60 seconds. However, `mongod` instances running
with non-default `--syncdelay` settings may have more or less frequent
checkpoints.

Run `validate` on each collection on the `mongod`
to restore statistics after an unclean shutdown.

After an unclean shutdown:

- `validate` updates the count statistic in the `collStats` output with the latest value.

- Other statistics like the number of documents inserted or removed in
  the `collStats` output are
  estimates.

### Replica Set Member State Restriction

To run on a replica set member, `collStats` operations require the member 
to be in `PRIMARY` or `SECONDARY` state. If the member
is in another state, such as `STARTUP2`, the
operation errors.

### Index Filter Behavior

Filtering on `indexDetails` using either `indexDetailsKey` or
`indexDetailsName` will only return a single matching index.
If no exact match is found, `indexDetails` will show information
on all indexes for the collection.

The `indexDetailsKey` field takes a document of the following form:

```javascript
{ '<string>' : <value>, '<string>' : <value>, ... }
```

Where `<string>>` is the field that is indexed and `<value>` is either
the direction of the index, or the special index type such as `text` or
`2dsphere`. See index types for the full list of
index types.

### Unexpected Shutdown and Count

For MongoDB instances using the WiredTiger
storage engine, after an unclean shutdown, statistics on size and count
may off by up to 1000 documents as reported by `collStats`,
`dbStats`, `count`. To restore the correct
statistics for the collection, run `validate` on the
collection.

### In-Progress Indexes

The `db.collection.stats` includes information on indexes currently 
being built. For details, see:

- `collStats.nindexes`
- `collStats.indexDetails`
- `collStats.indexBuilds`
- `collStats.totalIndexSize`
- `collStats.indexSizes`

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Basic Stats Lookup

The following operation returns stats on the `movies` collection in
the `sample_mflix` database:

```javascript
```

Output:

```javascript
```

If you do not specify a `scale` parameter, all size values are in
`bytes`.

### Stats Lookup With Scale

The following operation returns the size values in `kilobytes`
instead of `bytes` by specifying a `scale` of `1024`:

```javascript
```

Output:

```javascript
```

### Statistics Lookup With Index Details

The following operation returns an `indexDetails` field that
contains information related to each of the indexes within the
collection:

```javascript
```

Output:

```javascript
```

### Statistics Lookup With Filtered Index Details

To filter the indexes in the `indexDetails` field,
specify the index keys with the `indexDetailsKey` option or the
index name with the `indexDetailsName` option. To discover the index
keys and names, use `db.collection.getIndexes()`.

Given the following index:

```javascript
{
   "ns" : "sample_mflix.movies",
   "v" : 2,
   "key" : {
      "_fts" : "text",
      "_ftsx" : 1
   },
   "name" : "cast_text_fullplot_text_genres_text_title_text",
   "weights" : {
      "cast" : 1,
      "fullplot" : 1,
      "genres" : 1,
      "title" : 1
   },
   "default_language" : "english",
   "language_override" : "language",
   "textIndexVersion" : 3
}
```

The following operation filters the `indexDetails` document to a
single index using the `indexDetailsKey` option.

```javascript
db.movies.stats(
   {
      'indexDetails' : true,
      'indexDetailsKey' :
      {
         '_fts' : 'text',
         '_ftsx' : 1
      }
   }
)
```

The following operation filters the `indexDetails` document to a
single index using the `indexDetailsName` option.

```javascript
db.movies.stats(
   {
      'indexDetails' : true,
      'indexDetailsName' : 'cast_text_fullplot_text_genres_text_title_text'
   }
)
```

Both operations return the same output:

```javascript
{
  ok: 1,
  capped: false,
  ns: 'sample_mflix.movies',
  count: 21349,
  nindexes: 2,
  indexDetails: {
    cast_text_fullplot_text_genres_text_title_text: ...
  },
  indexSizes: {
    _id_: ...,
    cast_text_fullplot_text_genres_text_title_text: ...
  },
  scaleFactor: 1
}
```

For an explanation of the output, see
output details.

**See also:**

`$collStats`
