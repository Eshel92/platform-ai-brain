<!-- Converted from reference/operator/aggregation/skip.txt (reStructuredText). Includes are inlined. -->

# $skip (aggregation stage)

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

(Text shared from another MongoDB docs repo, not available offline: dbx/csharp/aggregation/rst-files/sample-data-mflix-intro.rst)

The following `Movie` class models the documents in the
`sample_mflix.movies` collection:

```csharp
[BsonIgnoreExtraElements]
public class Movie
{
    [BsonId]
    public ObjectId Id { get; set; }
    [BsonElement("title")]
    public string Title { get; set; } = null!;
    [BsonElement("year")]
    public int? Year { get; set; }
    [BsonElement("runtime")]
    public int? Runtime { get; set; }
    [BsonElement("rated")]
    public string? Rated { get; set; }
    [BsonElement("metacritic")]
    public int Metacritic { get; set; }
    [BsonElement("plot")]
    public string? Plot { get; set; }
    [BsonElement("type")]
    public string? Type { get; set; }
    [BsonElement("cast")]
    public string[]? Cast { get; set; }
    [BsonElement("directors")]
    public string[]? Directors { get; set; }
    [BsonElement("writers")]
    public string[]? Writers { get; set; }
    [BsonElement("imdb")]
    public ImdbData? Imdb { get; set; }
}
```

(Text shared from another MongoDB docs repo, not available offline: dbx/csharp/aggregation/rst-files/method-intro.rst)

```csharp
```

Output:

```json
```

**nodejs:**

To use the MongoDB Node.js driver to add a `$skip` stage to an aggregation
pipeline, use the `$skip` operator in a pipeline object.

The following example creates a pipeline stage that skips the first five documents in the input collection and passes
the remaining documents to the next stage in the pipeline. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [{ $skip: 5 }];

const cursor = collection.aggregate(pipeline);
return cursor;
```

## Learn More

To see full aggregation examples that use the `$skip` stage, see the
aggregation-complete-examples.
