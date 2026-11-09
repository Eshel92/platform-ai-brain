<!-- Converted from reference/operator/aggregation/limit.txt (reStructuredText). Includes are inlined. -->

# $limit (aggregation stage)

## Definition

**`$limit`**

Limits the number of documents passed to the next stage in the
pipeline.

## Compatibility

You can use `$limit` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$limit` stage has the following prototype form:

```javascript
{ $limit: <positive 64-bit integer> }
```

`$limit` takes a positive integer that specifies the
maximum number of documents to pass along.

**Note:**

The `$limit` pipeline aggregation has a 64-bit integer
limit. MongoDB returns an invalid argument error when values exceed
this limit.

## Behavior

### Using $limit with Sorted Results

If using the `$limit` stage with any of:

- the `$sort` aggregation stage,
- the `sort()` method, or
- the `sort` field to the `findAndModify` command or the
  `findAndModify()` shell method,

be sure to include at least one field in your sort that contains
unique values, before passing results to the `$limit` stage.

Sorting on fields that contain duplicate values may return an
inconsistent sort order for those duplicate fields over multiple
executions, especially when the collection is actively receiving writes.

The easiest way to guarantee sort consistency is to include the
`_id` field in your sort query.

See the following for more information on each:

- Consistent sorting with $sort (aggregation)
- Consistent sorting with the sort() shell method
- Consistent sorting with the findAndModify command
- Consistent sorting with the findAndModify() shell method

## Examples

**shell:**

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

Consider the following example:

```javascript
db.movies.aggregate([
   { $limit : 5 }
])
```

This operation returns only the first 5 documents passed to it
by the pipeline. `$limit` has no effect on the content
of the documents it passes.

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

To use the MongoDB Node.js driver to add a `$limit` stage to an aggregation
pipeline, use the `$limit` operator in a pipeline object.

The following example creates a pipeline stage that limits the number of returned documents to `10`. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [{ $limit: 10 }];

const cursor = collection.aggregate(pipeline);
return cursor;
```

**Note:**

When a `$sort` precedes a `$limit` and there are no
intervening stages that modify the number of documents, the optimizer can
coalesce the `$limit` into the `$sort`. This allows
the `$sort` operation to only
maintain the top `n` results as it progresses, where `n` is the
specified limit, and ensures that MongoDB only needs to store `n` items in memory.
This optimization still applies when `allowDiskUse` is `true` and
the `n` items exceed the aggregation memory limit.

## Learn More

To learn how to use `$limit` in a full example, see the agg-example-filter-data tutorial.
