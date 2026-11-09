<!-- Converted from reference/aggregation-commands-comparison.txt (reStructuredText). Includes are inlined. -->

# Aggregation Commands Comparison

**Note:** Aggregation Pipeline as Alternative to Map-Reduce

Starting in MongoDB 5.0, map-reduce is
deprecated:

- Instead of map-reduce, you should use an
  aggregation pipeline. Aggregation
  pipelines provide better performance and usability than map-reduce.

- You can rewrite map-reduce operations using aggregation
  pipeline stages, such as
  `$group`, `$merge`, and others. 

- For map-reduce operations that require custom functionality, you can
  use the `$accumulator` and `$function` aggregation
  operators. You can use those
  operators to define custom aggregation expressions in JavaScript.

For examples of aggregation pipeline alternatives to map-reduce, see:

- /reference/map-reduce-to-aggregation-pipeline

- /tutorial/map-reduce-examples

## Aggregation Commands Comparison Table

The following table provides a brief overview of the features of the
MongoDB aggregation commands.

* -  

  - `aggregate` / `db.collection.aggregate()`

  - `mapReduce` / `db.collection.mapReduce()`

* - Description

  - 
    Designed with specific goals of improving performance and
    usability for aggregation tasks.

    Uses a "pipeline" approach where objects are transformed as they
    pass through a series of pipeline operators such as
    `$group`, `$match`, and `$sort`.

    See /reference/operator/aggregation for more information
    on the pipeline operators.

  - Implements the Map-Reduce aggregation for processing large data sets.

* - Key Features

  - Pipeline operators can be repeated as needed.

    Pipeline operators need not produce one output document for every
    input document.

    Can also generate new documents or filter out documents.

    Using the `$merge` stage, you can create on-demand materialized 
    views, where the content of the output collection can be updated 
    incrementally the pipeline is run. `$merge` can incorporate 
    results (insert new documents, merge documents, replace documents, keep 
    existing documents, fail the operation, process documents with a custom
    update pipeline) into an existing collection.

  - In addition to grouping operations, can perform complex
    aggregation tasks as well as perform incremental aggregation on
    continuously growing datasets.

    See /tutorial/map-reduce-examples/ and
    /tutorial/perform-incremental-map-reduce/.

* - Flexibility

  - You can define custom aggregation expressions with `$accumulator` 
    and `$function`.

    You can also add computed fields, create new virtual sub-objects, and 
    extract sub-fields into the top-level of results by using the 
    `$project` pipeline operator.

    See `$project` for more information as well as
    /reference/operator/aggregation for more information on all
    the available pipeline operators.

  - Custom `map`, `reduce` and `finalize` JavaScript
    functions offer flexibility to aggregation logic.

    See `mapReduce` for details and restrictions
    on the functions.

* - Output Results

  - Returns results as a cursor. If the pipeline includes the
    `$out` stage or `$merge` stage, the cursor
    is empty.

    With `$out`, you can replace an existing output
    collection completely or output to a new collection. See
    `$out` for details.

    With `$merge`, you can output to a new or existing
    collection. For existing cllections, you can specify how to
    incorporate the results into the output collection (insert new
    documents, merge documents, replace documents, keep existing
    documents, fail the operation, process documents with a custom
    update pipeline). See `$merge` for details.

  - Returns results in various options (inline, new collection, merge,
    replace, reduce). See `mapReduce` for details on the
    output options.

* - Sharding

  - Supports non-sharded and sharded input collections.

    `$merge` can output to a non-sharded or sharded
    collection.

  - Supports non-sharded and sharded input collections.

* - More Information

  - 
    - /core/aggregation-pipeline 
    - `db.collection.aggregate()`
    - `aggregate`

  - 
    - /core/map-reduce
    - `db.collection.mapReduce()` 
    - `mapReduce`.

**See also:**

/reference/map-reduce-to-aggregation-pipeline
