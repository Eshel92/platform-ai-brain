<!-- Converted from reference/mql/aggregation-stages.txt (reStructuredText). Includes are inlined. -->

# Aggregation Stages

In the `db.collection.aggregate` and
`db.aggregate` methods,
pipeline stages appear in an array.
Documents pass through the stages in sequence. In the Atlas UI,
arrange pipeline stages with the
aggregation pipeline builder.

## db.collection.aggregate() Stages

All stages except the `$out`, `$merge`,
`$geoNear`, `$changeStream`, and
`$changeStreamSplitLargeEvent` stages can appear multiple
times in a pipeline.

**Note:**

For details on a specific command, including syntax and examples,
click on the link to the command's reference page.

```javascript
db.collection.aggregate( [ { <stage> }, ... ] )
```

**Core Stages**

Stages that filter, reshape, group, and combine documents in the
aggregation pipeline.

* - Stage
  - Description

* - `$addFields`

  - Adds new fields to documents. Similar to
    `$project`, `$addFields` reshapes each
    document in the stream; specifically, by adding new fields to
    output documents that contain both the existing fields
    from the input documents and the newly added fields.

    `$set` is an alias for `$addFields`.

* - `$bucket`

  - Categorizes incoming documents into groups, called buckets,
    based on a specified expression and bucket boundaries.

* - `$bucketAuto`

  - Categorizes incoming documents into a specific number of
    groups, called buckets, based on a specified expression.
    Bucket boundaries are automatically determined in an attempt
    to evenly distribute the documents into the specified number
    of buckets.

* - `$count`

  - Returns a count of the number of documents at this stage of
    the aggregation pipeline.

    Distinct from the `$count` aggregation accumulator.

* - `$densify`

  - .. include:: /includes/fact-densify-description.rst

* - `$documents`

  - Returns literal documents from input expressions.

* - `$facet`

  - Processes multiple aggregation pipelines within a single stage on the same set
    of input documents. Enables the creation of multi-faceted
    aggregations capable of characterizing data across multiple
    dimensions, or facets, in a single stage.

* - `$fill`

  - .. include:: /includes/fact-fill-description.rst

* - `$geoNear`

  - .. include:: /includes/extracts/geoNear-stage-toc-description.rst

* - `$graphLookup`

  - Performs a recursive search on a collection. To each output
    document, adds a new array field that contains the traversal
    results of the recursive search for that document.

* - `$group`

  - Groups input documents by a specified identifier expression
    and applies the accumulator expression(s), if specified, to
    each group. Consumes all input documents and outputs one
    document per each distinct group. The output documents only
    contain the identifier field and, if specified, accumulated
    fields.

* - `$limit`

  - Passes the first *n* documents unmodified to the pipeline
    where *n* is the specified limit. For each input document,
    outputs either one document (for the first *n* documents) or
    zero documents (after the first *n* documents).

* - `$lookup`

  - Performs a left outer join to another collection or view in
    the *same* database to filter in documents from the "joined"
    collection or view for processing.

* - `$match`

  - Filters the document stream to allow only matching documents
    to pass unmodified into the next pipeline stage.
    `$match` uses standard MongoDB queries. For each
    input document, outputs either one document (a match) or zero
    documents (no match).

* - `$merge`

  - Writes the resulting documents of the aggregation pipeline to
    a collection. The stage can incorporate (insert new
    documents, merge documents, replace documents, keep existing
    documents, fail the operation, process documents with a
    custom update pipeline) the results into an output
    collection. To use the `$merge` stage, it must be
    the last stage in the pipeline.

* - `$out`

  - Writes the resulting documents of the aggregation pipeline to
    a collection. To use the `$out` stage, it must be
    the last stage in the pipeline.

* - `$project`

  - Reshapes each document in the stream, such as by adding new
    fields or removing existing fields. For each input document,
    outputs one document.

    See also `$unset` for removing existing fields.

* - `$redact`

  - Reshapes each document in the stream by restricting the
    content for each document based on information stored in the
    documents themselves. Incorporates the functionality of
    `$project` and `$match`. Can be used to
    implement field level redaction. For each input document,
    outputs either one or zero documents.

* - `$replaceRoot`

  - Replaces a document with the specified embedded document. The
    operation replaces all existing fields in the input document,
    including the `_id` field. Specify a document embedded in
    the input document to promote the embedded document to the
    top level.

    `$replaceWith` is an alias for
    `$replaceRoot` stage.

* - `$replaceWith`

  - Replaces a document with the specified embedded document. The
    operation replaces all existing fields in the input document,
    including the `_id` field. Specify a document embedded in
    the input document to promote the embedded document to the
    top level.

    `$replaceWith` is an alias for
    `$replaceRoot` stage.

* - `$sample`

  - Randomly selects the specified number of documents from its
    input.

* - `$set`

  - Adds new fields to documents. Similar to
    `$project`, `$set` reshapes each
    document in the stream; specifically, by adding new fields to
    output documents that contain both the existing fields
    from the input documents and the newly added fields.

    `$set` is an alias for `$addFields` stage.

* - `$setWindowFields`

  - Groups documents into windows and applies one or more
    operators to the documents in each window.

    **New in version:** 5.0

* - `$skip`

  - Skips the first *n* documents where *n* is the specified skip
    number and passes the remaining documents unmodified to the
    pipeline. For each input document, outputs either zero
    documents (for the first *n* documents) or one document (if
    after the first *n* documents).

* - `$sort`

  - Reorders the document stream by a specified sort key. Only
    the order changes; the documents remain unmodified. For each
    input document, outputs one document.

* - `$sortByCount`

  - Groups incoming documents based on the value of a specified
    expression, then computes the count of documents in each
    distinct group.

* - `$unionWith`

  - Performs a union of two collections; i.e. combines
    pipeline results from two collections into a single
    result set.

* - `$unset`

  - Removes/excludes fields from documents.

    `$unset` is an alias for `$project` stage
    that removes fields.

* - `$unwind`

  - Deconstructs an array field from the input documents to
    output a document for *each* element. Each output document
    replaces the array with an element value. For each input
    document, outputs *n* documents where *n* is the number of
    array elements and can be zero for an empty array.

**Language Extensions**

Stages that extend the aggregation language with specialized
capabilities, such as Atlas Search and change streams.

* - Stage
  - Description

* - `$changeStream`

  - Returns a Change Stream cursor for the
    collection.  This stage can only occur once in an aggregation
    pipeline and it must occur as the first stage.

* - `$changeStreamSplitLargeEvent`

  - .. include:: /includes/changeStreamSplitLargeEvent-introduction.rst

* - `$search`

  - Performs a full-text search of the field or fields in a
    collection.

    To learn more, see
    Atlas Search Aggregation Pipeline Stages.

* - `$searchMeta`

  - Returns different types of metadata result documents for the
    Atlas Search query against an
    Atlas
    collection.
    To learn more, see Atlas Search Aggregation Pipeline Stages.

* - `$vectorSearch`

  - Performs an ANN (Approximate Nearest Neighbor) or
    ENN (Exact Nearest Neighbor) search on a
    vector in the specified field of an
    Atlas collection.

    `$vectorSearch` is only available for MongoDB Atlas clusters
    running MongoDB v6.0.11 or higher, and is not available for
    self-managed deployments.

    **New in version:** 7.0.2

**Metadata Sources**

Stages that return metadata about the deployment, such as collection
statistics, index information, and active operations.

* - Stage
  - Description

* - `$collStats`

  - Returns statistics regarding a collection or view.

* - `$currentOp`

  - Returns information on active and/or dormant operations for
    the MongoDB deployment.

    Uses the `db.aggregate()` method instead of the
    `db.collection.aggregate()` method.

* - `$indexStats`

  - Returns statistics regarding the use of each index for the
    collection.

* - `$listLocalSessions`

  - Lists all active sessions recently in use on the currently
    connected `mongos` or `mongod`
    instance. These sessions may have not yet propagated to the
    `system.sessions` collection.

    Uses the `db.aggregate()` method instead of the
    `db.collection.aggregate()` method.

* - `$listSampledQueries`

  - Lists sampled queries for all collections or a specific
    collection.

* - `$listSearchIndexes`

  - .. include:: /includes/atlas-search-commands/command-descriptions/getSearchIndexes-description.rst

* - `$listSessions`

  - Lists all sessions that have been active long enough to
    propagate to the `system.sessions` collection.

* - `$planCacheStats`

  - Returns plan cache information for a
    collection.

* - `$queryStats`

  - .. include:: /includes/aggregation/queryStats/description.rst

    WARNING: The `$queryStats` aggregation stage is
    unsupported and is not guaranteed to be stable in a future
    release. Don't build functionality that relies on a specific
    output format of this stage, since the output may change in a
    future release.

* - `$shardedDataDistribution`

  - Returns information on the distribution of data in sharded
    collections.

    Uses the `db.aggregate()` method instead of the
    `db.collection.aggregate()` method.

    **New in version:** 6.0.3

To learn about expressions that you can use in pipeline stages, see
operator-ref-landing.

## Stages Available for Updates

Use the aggregation pipeline for updates in:

| Command | `mongosh` Methods |
|---|---|
| `findAndModify` | \| db.collection.findOneAndUpdate() \| db.collection.findAndModify() |
| `update` | \| db.collection.updateOne() \| db.collection.updateMany() \| Bulk.find.update() \| Bulk.find.updateOne() \| Bulk.find.upsert() |

For updates, the pipeline supports these stages:

- `$addFields` and its alias `$set`

- `$project` and its alias `$unset`

- `$replaceRoot` and its alias `$replaceWith`
