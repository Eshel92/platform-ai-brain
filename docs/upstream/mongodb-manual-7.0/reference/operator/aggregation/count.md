<!-- Converted from reference/operator/aggregation/count.txt (reStructuredText). Includes are inlined. -->

# $count (aggregation stage)

## Definition

**`$count`**

Passes a document to the next stage that contains a count of the
number of documents input to the stage.

**Note:** Disambiguation

This page describes the `$count` aggregation pipeline stage. You
can also use `$count` in these other contexts:

- `$count (accumulator)`, which returns the number of
  documents in a group.
- `$count (window function)`, which is used in
  the `$setWindowFields` stage to return the number of
  documents in a particular window.

## Compatibility

You can use `$count` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

`$count` has the following syntax:

```javascript
{ $count: <string> }
```

`<string>` is the name of the output field which has the count
as its value. `<string>` must be a non-empty string, must not
start with `$` and must not contain the `.` character.

## Behavior

The return type is represented by the smallest type that can store
the final value of count: `integer` →
`long` → `double`

The `$count` stage is equivalent to the following
`$group` and `$project` sequence:

```javascript
db.collection.aggregate( [
   { $group: { _id: null, myCount: { $sum: 1 } } },
   { $project: { _id: 0 } }
] )
```

`myCount` is the output field that stores the count.
You can specify another name for the output field.

If the input dataset is empty, `$count` doesn't return a result.

**See also:**

`db.collection.countDocuments()` wraps the `$group` 
aggregation stage with a `$sum` expression.

## Examples

**shell:**

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following aggregation operation has two stages:

#. The `$match` stage filters for documents where
   `metacritic` equals `100` to pass along only those
   documents to the next stage.

#. The `$count` stage returns a count of the remaining
   documents in the aggregation pipeline and assigns the value
   to a field called `perfect_score_count`.

```javascript
```

Output:

```javascript
```

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
var pipeline = new EmptyPipelineDefinition<Movie>()
    .Match(Builders<Movie>.Filter.Eq(m => m.Metacritic, 100))
    .Count();
```

**nodejs:**

The Node.js examples on this page use the `sample_mflix` database from the
Atlas sample datasets. To learn how to create a free
MongoDB Atlas cluster and load the sample datasets, see `Get Started` in the MongoDB Node.js driver documentation.

To use the MongoDB Node.js driver to add a `$count` stage to an aggregation
pipeline, use the `$count` operator in a pipeline object.

The following example creates a pipeline stage that counts the number of input documents from the
`sample_mflix.movies` collection and returns a document containing
the count. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [{ $count: "movies" }];

const cursor = collection.aggregate(pipeline);
return cursor;
```

         

## Learn More

- `db.collection.countDocuments()`
- `$collStats`
- `db.collection.estimatedDocumentCount()`
- `count`
- `db.collection.count()`
