<!-- Converted from core/aggregation-pipeline.txt (reStructuredText). Includes are inlined. -->

# Aggregation Pipeline

An aggregation pipeline consists of one or more stages that process documents:

- Each stage performs an operation on the input documents.
  For example, a stage can filter documents, group documents, and
  calculate values.

- The documents that are output from a stage are passed to the next
  stage.

- An aggregation pipeline can return results for groups of documents.
  For example, return the total, average, maximum, and minimum values.

You can update documents with an aggregation pipeline if you use the stages 
shown in updates-agg-pipeline.

**Note:**

Aggregation pipelines run with the
`db.collection.aggregate()` method do not modify documents in
a collection, unless the pipeline contains a `$merge` or
`$out` stage.

You can run aggregation pipelines in the UI for deployments hosted in [MongoDB Atlas](https://www.mongodb.com/docs/atlas).

When you run aggregation pipelines on MongoDB Atlas deployments in the
MongoDB Atlas UI, you can preview the results at each stage.

## Complete Aggregation Pipeline Examples

The aggregation-complete-examples section contains step-by-step
tutorials for common aggregation tasks, with examples for MongoDB Shell
and each of the `official MongoDB drivers`.

## Run an Aggregation Pipeline

To run an aggregation pipeline, use:

- `db.collection.aggregate()` or

- `aggregate`

## Additional Aggregation Pipeline Stage Details

An aggregation pipeline consists of one or more stages that process documents:

- A stage does not need to output one document for every input
  document. Some stages produce new documents or filter documents out.
- The same stage can appear multiple times in a pipeline, except for
  `$out`, `$merge`, and `$geoNear`.

For all aggregation stages, see
aggregation-pipeline-operator-reference.

### Expressions and Operators

In aggregation pipelines, expressions define how the stage processes  
each input document in the pipeline. For example, expressions can define 
which documents to include, how to reshape fields, or how to compute new values.

Some aggregation pipeline stages accept expressions. Operators calculate values based on input expressions.

In the MongoDB Query Language, you can build expressions from the
following components:

| Component | Example |
|---|---|
| Constants | `3` |
| Operators | `$add` |
| Field path expressions | `"$<path.to.field>"` |

For example, `{ $add: [ 3, "$inventory.total" ] }` is an expression
that consists of the `$add` operator and two operands:

- The constant `3`
- The field path expression
  `"$inventory.total"`

The expression returns the result of adding 3 to the value at path
`inventory.total` of the input document.

### Field Paths

Field path expressions access fields in input
documents. Prefix the field name with a dollar sign `$`. For example,
`"$user"` references the `user` field, and `"$user.name"`
references the embedded `user.name` field.

For more examples, see agg-field-paths.

## Update Documents Using an Aggregation Pipeline

To update documents with an aggregation pipeline, use:

| Command | `mongosh` Methods |
|---|---|
| `findAndModify` | \| db.collection.findOneAndUpdate() \| db.collection.findAndModify() |
| `update` | \| db.collection.updateOne() \| db.collection.updateMany() \| Bulk.find.update() \| Bulk.find.updateOne() \| Bulk.find.upsert() |

## Other Considerations

### Aggregation Pipeline Limitations

For limits on value types and result size, see
agg-pipeline-limits.

### Aggregation Pipelines and Sharded Collections

Aggregation pipelines support operations on sharded collections. See
aggregation-pipeline-sharded-collection.

**Important:** Aggregation Pipelines as an Alternative to Map-Reduce

Starting in MongoDB 5.0, map-reduce is deprecated. 

For examples of aggregation pipeline alternatives to map-reduce, see:

- /reference/map-reduce-to-aggregation-pipeline

- /tutorial/map-reduce-examples

## Learn More

To learn more about aggregation pipelines, see:

- aggregation-expression-operators

- aggregation-pipeline-operator-reference
