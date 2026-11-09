<!-- Converted from reference/operator/aggregation/skip.txt (reStructuredText). Includes are inlined. -->

# $skip (aggregation)

## Definition

**`$skip`**

Skips over the specified number of documents that
pass into the stage and passes the remaining documents to the next
stage in the pipeline.

The `$skip` stage has the following prototype form:

```javascript
{ $skip: <positive 64-bit integer> }
```

`$skip` takes a positive integer that specifies the
maximum number of documents to skip.

**Note:**

Starting in MongoDB 5.0, the `$skip` pipeline aggregation
has a 64-bit integer limit. Values passed to the pipeline which
exceed this limit will return a invalid argument error.

## Behavior

### Using $skip with Sorted Results

If using the `$skip` stage with any of:

- the `$sort` aggregation stage,
- the `sort()` method, or
- the `sort` field to the `findAndModify` command or the
  `findAndModify()` shell method,

be sure to include at least one field in your sort that contains
unique values, before passing results to the `$skip` stage.

Sorting on fields that contain duplicate values may return a different
sort order for those duplicate fields over multiple executions,
especially when the collection is actively receiving writes.

The easiest way to guarantee sort consistency is to include the
`_id` field in your sort query.

See the following for more information on each:

- Consistent sorting with $sort (aggregation)
- Consistent sorting with the sort() shell method
- Consistent sorting with the findAndModify command
- Consistent sorting with the findAndModify() shell method

## Examples

**shell:**

Consider the following example:

```javascript
db.article.aggregate([
    { $skip : 5 }
]);
```

This operation skips the first 5 documents passed to it by the
pipeline. `$skip` has no effect on the content of the
documents it passes along the pipeline.

**csharp:**

To use the MongoDB {+csharp-driver-short+} to add a `$skip` stage to an aggregation
pipeline, call the [Skip()](https://mongodb.github.io/mongo-csharp-driver/3.3.0/api/MongoDB.Driver/MongoDB.Driver.PipelineStageDefinitionBuilder.Skip.html) method on a `PipelineDefinition` object.

The following example creates a pipeline stage that skips the first five documents in the input and passes
the remaining documents to the next stage in the pipeline:

```csharp
var pipeline = new EmptyPipelineDefinition<Movie>()
    .Skip(5);
```

**See also:**

- /tutorial/aggregation-zip-code-data-set
- /tutorial/aggregation-with-user-preference-data
