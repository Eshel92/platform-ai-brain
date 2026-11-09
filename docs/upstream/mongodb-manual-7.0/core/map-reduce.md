<!-- Converted from core/map-reduce.txt (reStructuredText). Includes are inlined. -->

# Map-Reduce

**Note:** Aggregation Pipeline as Alternative

Starting in MongoDB 5.0, map-reduce is
deprecated:

- Instead of map-reduce, you should use an
  aggregation pipeline. Aggregation
  pipelines provide better performance and usability than map-reduce.

- You can rewrite map-reduce operations using aggregation pipeline
  stages, such as
  `$group`, `$merge`, and others. 

- For map-reduce operations that require custom functionality, you can
  use the `$accumulator` and `$function` aggregation
  operators. You can use those
  operators to define custom aggregation expressions in JavaScript.

For examples of aggregation pipeline alternatives to map-reduce, see:

- /reference/map-reduce-to-aggregation-pipeline

- /tutorial/map-reduce-examples

You can run aggregation pipelines in the UI for deployments hosted in [MongoDB Atlas](https://www.mongodb.com/docs/atlas).

Map-reduce is a data processing paradigm for condensing large volumes
of data into *aggregated* results. To perform map-reduce operations,
MongoDB provides the `mapReduce` database command.

Consider the following map-reduce operation:

(Figure: /images/map-reduce.bakedsvg.svg)

MongoDB applies the *map* phase to each input document (the documents
in the collection that match the query condition). The map function
emits key-value pairs. For keys that have multiple values, MongoDB
applies the *reduce* phase, which collects and condenses the data, and
then stores the results in a collection. The output of the reduce
function can optionally pass through a *finalize* function to further
process the results.

All map-reduce functions in MongoDB are JavaScript and run within the
`mongod` process. Map-reduce operations take a single
collection as input and can apply sorting and limiting before
the map stage. `mapReduce` can return results as a document
or write them to a collection.

**Note:**

Map-reduce is unsupported for MongoDB Atlas Free and Flex clusters.

## Map-Reduce JavaScript Functions

Map-reduce operations use custom JavaScript functions to *map* values
to a key. If a key has multiple values, the operation *reduces* them
to a single object. A map function can emit multiple key-value pairs
or none. An optional finalize function can make further modifications
to the results.

## Map-Reduce Results

A map-reduce operation can write results to a collection or return
them inline. If you write results to a collection, you can run
subsequent map-reduce operations against the same input collection
that replace, merge, or reduce new results with previous results. See
`mapReduce` and incremental-map-reduce for examples.

When returning results *inline*, the result documents must fit within
the `BSON Document Size` limit of 16 mebibytes. For more limits
and restrictions, see `mapReduce`.

## Sharded Collections

MongoDB supports map-reduce operations on sharded collections.

## Views

Views do not support map-reduce operations.
