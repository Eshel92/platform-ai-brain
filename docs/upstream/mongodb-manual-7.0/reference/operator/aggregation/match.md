<!-- Converted from reference/operator/aggregation/match.txt (reStructuredText). Includes are inlined. -->

# $match (aggregation stage)

## Definition

**`$match`**

Filters documents based on a specified query predicate.
Matched documents are passed to the next pipeline stage.

## Compatibility

You can use `$match` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

```javascript
{ $match: { <query predicate> } }
```

The syntax for the `$match` query predicate is identical to the syntax
used in the query argument of a
`find()` command.

## Behavior

### Pipeline Optimization

- Place the `$match` as early in the aggregation
  pipeline as possible. Because `$match` limits
  the total number of documents in the aggregation pipeline,
  earlier `$match` operations minimize the amount of
  processing down the pipe.

- If you place a `$match` at the very beginning of a
  pipeline, the query can take advantage of indexes like any other `db.collection.find()`
  or `db.collection.findOne()`.

### Expressions in Query Predicates

To include expressions in a query
predicate, use the `$expr` operator.

### 0, Null, False or Missing Values

A `$match` stage filters out a document from pipeline results if one
of the following conditions applies:

- The `$match` query predicate returns a `0`, `null`, or `false`
  value on that document.
- The `$match` query predicate uses a field that is missing from
  that document.

### Restrictions

- You cannot use `$where` in a `$match` stage.

- You cannot use `$near` or `$nearSphere` in a `$match`
  stage. As an alternative, you can either:

  - Use the `$geoNear` stage instead of the `$match`
    stage.

  - Use the `$geoWithin` query predicate operator with
    `$center` or `$centerSphere` in the `$match`
    stage.

- To use `$text` in a `$match` stage, the
  `$match` stage has to be the first stage of the pipeline.

  Views do not support `$text`.

  **Note:**

  `$text` provides text query capabilities for self-managed
  (non-Atlas) deployments. For data hosted on MongoDB Atlas, MongoDB
  offers an improved full-text query solution, Atlas Search.

### Filter Data on Atlas by Using Atlas Search

For data stored in MongoDB Atlas,
you can use the Atlas Search
compound-ref operator `filter` option to match or filter
documents when running `$search` queries. Running
`$match` after `$search` is less performant
than running `$search` with the compound-ref
operator `filter` option.

To learn more about the `filter` option, see compound-ref
in the Atlas documentation.

## Examples

**shell:**

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Equality Match

The following operation uses `$match` to perform an
equality match on the `rated` field. The `runtime` filter
limits the result to a small, representative set:

```javascript
db.movies.aggregate(
    [ { $match : { rated : "TV-PG", runtime : { $gt: 1000 } } } ]
)
```

The `$match` selects the documents where the `rated`
field equals `"TV-PG"` and `runtime` is greater than `1000`.

### Perform a Count

The following example selects documents to process using the
`$match` pipeline operator and then pipes the results
to the `$group` pipeline operator to compute a count of
the documents:

```javascript
```

Output:

```javascript
```

In the aggregation pipeline, `$match` selects the
documents where either the `runtime` is greater than `1000`
or the `year` is earlier than `1910`. These documents are
then sent to the `$group` to perform a count.

### Match Array Elements

To filter documents based on elements in an array field,
use the `$elemMatch` operator in the query predicate
of the `$match` stage:

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
```

Output:

```json
```

**nodejs:**

The Node.js examples on this page use the `sample_mflix` database from the
Atlas sample datasets. To learn how to create a free
MongoDB Atlas cluster and load the sample datasets, see `Get Started` in the MongoDB Node.js driver documentation.

To use the MongoDB Node.js driver to add a `$match` stage to an aggregation
pipeline, use the `$match` operator in a pipeline object.

The following example creates a pipeline stage that matches all `movie` documents where the `title` field is equal to
`"The Shawshank Redemption"`. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [
  {
    $match: {
      title: "The Shawshank Redemption"
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

## Learn More

Refer to the aggregation-complete-examples for more information
and use cases on aggregation.
