<!-- Converted from reference/operator/aggregation/lookup.txt (reStructuredText). Includes are inlined. -->

# $lookup (aggregation stage)

## Definition

**`$lookup`**

**Changed in version:** 5.1

Performs a left outer join to a collection in the *same* database to
filter in documents from the foreign collection for processing. The
`$lookup` stage adds a new array field to each input
document. The new array field contains the matching documents from
the foreign collection. The `$lookup` stage passes these
reshaped documents to the next stage.

Starting in MongoDB 5.1, you can use `$lookup` with sharded
collections.

To combine elements from two different collections, use the
`$unionWith` pipeline stage.

**Important:**

`$lookup` performance, as with any other query performance,
depends on the operation type and whether the foreign field is
indexed. Unindexed or correlated-subquery `$lookup` operations
on large collections can slow down query performance. To reduce
reliance on `$lookup`, consider an embedded data model to store related data in a single
collection.

For details on `$lookup` performance by operation type, see
lookup-performance-considerations.

## Compatibility

You can use `$lookup` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$lookup` stage syntax:

```none
{
   $lookup:
     {
       from: <collection to join>,
       localField: <field from the input documents>,
       foreignField: <field from the documents of the "from" collection>,
       let: { <var_1>: <expression>, …, <var_n>: <expression> },
       pipeline: [ <pipeline to run> ],
       as: <output array field>
     }
}
```

The `$lookup` accepts a document with these fields:

* - Field
  - Necessity
  - Description

* - from

  - Required

  - .. _lookup-subquery-from:

    Specifies the foreign collection in the *same* database to join
    to the local collection.

    It is possible in some edge cases to subsitute `from` with `pipeline` with
    `$documents` as the first stage. For an example, see 
    Use a $documents Stage in a $lookup Stage.

    Starting in MongoDB 5.1, the `from` collection can be sharded.

* - localField

  - Optional if `pipeline` is specified

  - .. _lookup-subquery-localField:

    Specifies the field from the documents input to the
    `$lookup` stage. `$lookup` performs an
    equality match on the `localField` to the
    `foreignField` from the documents of the `from`
    collection. If an input document does not contain the
    `localField`, the `$lookup` treats the
    field as having a value of `null` for matching purposes.

* - foreignField

  - Optional if `pipeline` is specified

  - .. _lookup-subquery-foreignField:

    Specifies the foreign documents' `foreignField` to perform an
    equality match with the local documents' `localField`.

    If a foreign document does not contain a `foreignField` value,
    the `$lookup` uses a `null` value for the match.

* - let

  - Optional

  - .. _lookup-subquery-let:

    Specifies variables to use in the pipeline stages. Use the variable expressions to
    access the fields from the local collection's documents that are
    input to the `pipeline`.

    To reference variables in pipeline
    stages, use the `"$$<variable>"` syntax.

    The let variables can be accessed by the
    stages in the pipeline, including
    additional `$lookup` stages nested in the `pipeline`.

    - A `$match` stage requires the use of an
      `$expr` operator to access the variables. The `$expr`
      operator allows the use of aggregation expressions inside of the
      `$match` syntax.

      The `$eq`, `$lt`, `$lte`,
      `$gt`, and `$gte` comparison operators placed in
      an `$expr` operator can use an index on the `from` collection
      referenced in a `$lookup` stage. Limitations:

      - Indexes can only be used for comparisons between fields and constants, so the
        `let` operand must resolve to a constant.

        For example, a comparison between `$a` and a constant 
        value can use an index, but a comparison between `$a` and `$b` 
        cannot.

      - Indexes are not used for comparisons where the `let` operand resolves to an
        empty or missing value.

      - Multikey, partial, or 
        sparse indexes are not used.

    - Other (non-`$match`) stages in the pipeline
      do not require an `$expr` operator to access the variables.

* - pipeline

  - Optional if `localField` and `foreignField` are specified 

  - .. _lookup-subquery-pipeline:

    Specifies the `pipeline` to run on the foreign collection. The
    `pipeline` returns documents from the foreign collection. To
    return all documents, specify an empty `pipeline: []`.

    The `pipeline` cannot include the `$out` or
    `$merge` stages. Starting in v6.0, the `pipeline` 
    can contain the Atlas Search 
    `$search` stage as the first stage inside the 
    pipeline. To learn more, see fts-lookup-behavior.

    The `pipeline` cannot access fields from input documents.
    Instead, define variables for the document fields using the
    let option and
    then reference the variables in the `pipeline` stages.

    To reference variables in pipeline
    stages, use the `"$$<variable>"` syntax.

    The let variables can be accessed by the
    stages in the pipeline, including
    additional `$lookup` stages nested in the `pipeline`.

    - A `$match` stage requires the use of an
      `$expr` operator to access the variables. The `$expr`
      operator allows the use of aggregation expressions inside of the
      `$match` syntax.

      The `$eq`, `$lt`, `$lte`,
      `$gt`, and `$gte` comparison operators placed in
      an `$expr` operator can use an index on the `from` collection
      referenced in a `$lookup` stage. Limitations:

      - Indexes can only be used for comparisons between fields and constants, so the
        `let` operand must resolve to a constant.

        For example, a comparison between `$a` and a constant 
        value can use an index, but a comparison between `$a` and `$b` 
        cannot.

      - Indexes are not used for comparisons where the `let` operand resolves to an
        empty or missing value.

      - Multikey, partial, or 
        sparse indexes are not used.

    - Other (non-`$match`) stages in the pipeline
      do not require an `$expr` operator to access the variables.

* - as

  - Required

  - .. _lookup-subquery-as:

    Specifies the name of the new array field to add to the input
    documents. The new array field contains the matching
    documents from the `from` collection. If the specified name
    already exists in the input document, the existing field is
    *overwritten*.

### Equality Match with a Single Join Condition

To perform an equality match between a field from the input documents
with a field from the documents of the foreign collection, the
`$lookup` stage has this syntax:

```none
{
   $lookup:
     {
       from: <collection to join>,
       localField: <field from the input documents>,
       foreignField: <field from the documents of the "from" collection>,
       pipeline: [ <pipeline to run> ],
       as: <output array field>
     }
}
```

**Note:**

In this example, `pipeline` is optional and runs after
the local and foreign equality stage. 

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, (
   SELECT ARRAY_AGG(*)
   FROM <collection to join>
   WHERE <foreignField> = <collection.localField>
) AS <output array field>
FROM collection;
```

**Note:**

The SQL statements on this page are included for comparison to the
MongoDB aggregation pipeline syntax. The SQL statements aren't
runnable.

For MongoDB examples, see these pages:

- lookup-single-equality-example
- unwind-example
- lookup-mergeObjects

### Join Conditions and Subqueries on a Foreign Collection

MongoDB supports:

- Executing a pipeline on a foreign collection.

- Multiple join conditions.

- Correlated and uncorrelated subqueries.

In MongoDB, an uncorrelated subquery means that every input document returns
the same result. A correlated subquery is a pipeline in a `$lookup` stage that uses the local
or `input` collection's fields to return results correlated to each incoming
document.

**Note:**

Starting in MongoDB 5.0, for an uncorrelated subquery in a
`$lookup` pipeline stage containing a `$sample`
stage, the `$sampleRate` operator, or the
`$rand` operator, the subquery is always run again if
repeated. Previously, depending on the subquery output size, either the
subquery output was cached or the subquery was run again.

MongoDB correlated subqueries are comparable to SQL correlated
subqueries, where the inner query references outer query values. An
SQL uncorrelated subquery does not reference outer query values.

MongoDB 5.0 also supports concise correlated subqueries.

To perform correlated and uncorrelated subqueries with two collections,
and perform other join conditions besides a single equality match, use
this `$lookup` syntax:

```javascript
{
   $lookup:
      {
         from: <foreign collection>,
         let: { <var_1>: <expression>, …, <var_n>: <expression> },
         pipeline: [ <pipeline to run on foreign collection> ],
         as: <output array field>
      }
}
```

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, <output array field>
FROM collection
WHERE <output array field> IN (
   SELECT <documents as determined from the pipeline>
   FROM <collection to join>
   WHERE <pipeline>
);
```

See the following examples:

- lookup-multiple-joins
- lookup-uncorrelated-subquery

### Correlated Subqueries Using Concise Syntax

**New in version:** 5.0

Starting in MongoDB 5.0, you can use a concise syntax for a correlated
subquery. Correlated subqueries reference document fields from a foreign
collection  *and* the "local" collection on which the
`aggregate()` method was run.

The following new concise syntax removes the requirement for an equality
match on the foreign and local fields inside an `$expr`
operator:

```javascript
{
   $lookup:
      {
         from: <foreign collection>,
         localField: <field from local collection's documents>,
         foreignField: <field from foreign collection's documents>,
         let: { <var_1>: <expression>, …, <var_n>: <expression> },
         pipeline: [ <pipeline to run> ],
         as: <output array field>
      }
}
```

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, <output array field>
FROM localCollection
WHERE <output array field> IN (
   SELECT <documents as determined from the pipeline>
   FROM <foreignCollection>
   WHERE <foreignCollection.foreignField> = <localCollection.localField>
   AND <pipeline match condition>
);
```

See this example:

- lookup-concise-correlated-subquery

## Behavior

### Views and Collation

If performing an aggregation that involves multiple views, such as
with `$lookup` or `$graphLookup`, the views must
have the same collation.

### Restrictions

You cannot include the `$out` or the `$merge`
stage in the `$lookup` stage. That is, when specifying a
pipeline for the foreign collection, you cannot include either stage in
the `pipeline` field.

```javascript
{
   $lookup:
   {
      from: <collection to join>,
      let: { <var_1>: <expression>, …, <var_n>: <expression> },
      pipeline: [ <pipeline to execute on the foreign collection> ],  // Cannot include $out or $merge
      as: <output array field>
   }
}
```

### Atlas Search Support

Starting in MongoDB 6.0, you can specify the Atlas Search `$search` or `$searchMeta` stage
in the `$lookup` pipeline to search collections on the Atlas
cluster. The `$search` or the `$searchMeta` stage
must be the first stage inside the `$lookup` pipeline.

For example, when you lookup-syntax-let-pipeline or run
lookup-syntax-concise-correlated-subquery, you can specify
`$search` or `$searchMeta` inside the pipeline as
shown below:

**search:**

```
[{
  "$lookup": {
    "from": <foreign collection>,
    localField: <field from the input documents>,
    foreignField: <field from the documents of the "from" collection>,
    "as": <output array field>,
    "pipeline": [{
      "$search": {
        "<operator>": {
          <operator-specification>
        }
      },
      ...
    }]
  }
}]
```

**searchmeta:**

```
[{
  "$lookup": {
    "from": <foreign collection>,
    localField: <field from the input documents>,
    foreignField: <field from the documents of the "from" collection>,
    "as": <output array field>,
    "pipeline": [{
      "$searchMeta": {
        "<collector>": {
          <collector-specification>
        }
      },
      ...
    }]
  }
}]
```

To see an example of `$lookup` with `$search`,
see the Atlas Search tutorial Run an Atlas Search $search Query
Using $lookup.

### Sharded Collections

Starting in MongoDB 5.1, you can specify sharded collections in the `from` parameter of
`$lookup` stages.

You **cannot** use the `$lookup` stage within a transaction while 
targeting a sharded collection.

### Slot-Based Query Execution Engine

**Note:**

Starting in version 7.0.17, the slot-based query execution engine is no longer
enabled by default for patch versions of 7.0. If you want 
your queries to use the slot-based query execution engine, please upgrade to 
version 8.0, where it is enabled by default.

Starting in version 6.0, MongoDB can use the slot-based execution
query engine to execute `$lookup` stages
if *all* preceding stages in the pipeline can also be executed by the
slot-based execution engine and none of the following conditions are true:

- The `$lookup` operation executes a pipeline on a foreign collection.
  To see an example of this kind of operation, see
  lookup-syntax-let-pipeline.

- The `$lookup`'s `localField` or `foreignField` specify numeric
  components. For example: `{ localField: "restaurant.0.review" }`.

- The `from` field of any `$lookup` in the pipeline specifies a view
  or sharded collection.

For more information, see agg-lookup-optimization-sbe.

### Performance Considerations

`$lookup` performance depends on the type of operation performed.
Refer to the following table for performance considerations for
different `$lookup` operations.

* - `$lookup` Operation
  - Performance Considerations

* - Equality Match with a Single Join

  - .. _equality-match-performance:

    - `$lookup` operations that perform equality matches with a
      single join perform better when the foreign collection contains
      an index on the `foreignField`.

      IMPORTANT: If a supporting index on the `foreignField` does
      not exist, a `$lookup` operation that performs an equality match with
      a single join likely has poor performance.

* - Uncorrelated Subqueries

  - .. _uncorrelated-subqueries-performance:

    - `$lookup` operations that contain uncorrelated subqueries
      perform better when the inner pipeline can reference an
      index of the foreign collection.

    - MongoDB only needs to run the `$lookup` subquery once before
      caching the query because there is no relationship between the
      source and foreign collections. The subquery is not based on
      any value in the source collection. This behavior improves
      performance for subsequent executions of the `$lookup`
      operation.

* - Correlated Subqueries

  - .. _correlated-subqueries-performance:

    - `$lookup` operations that contain correlated subqueries
      perform better when the foreign collection contains an index
      on the `foreignField`.

    - If your pipeline passes a large number of documents to the
      `$lookup` query, the following strategies may improve
      performance:

      - Reduce the number of documents that MongoDB passes to the
        `$lookup` query. For example, set a stricter filter
        during the `$match` stage.

      - Reconsider the data's schema to ensure it is optimal for the
        use case.

For general performance strategies, see Indexing Strategies and Query Optimization.

## Examples

**shell:**

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Perform a Single Equality Join with `$lookup`

The following aggregation operation first filters the
`movies` collection to movies with a `runtime` greater
than `1000`, then joins with the `comments` collection
on the `_id` and `movie_id` fields:

```javascript
```

Output:

```javascript
```

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, movie_comments
FROM movies
WHERE movie_comments IN (
   SELECT *
   FROM comments
   WHERE movie_id = movies._id
);
```

For more information, see
Equality Match Performance Considerations.

### Use `$lookup` with an Array

If the `localField` is an array, you can match the array
elements against a scalar `foreignField` without an
`$unwind` stage.

The following aggregation operation joins the `movies`
collection with the `users` collection, matching the
`cast` array field from `movies` against the scalar
`name` field from `users`:

```javascript
```

Output:

```javascript
```

### Use `$lookup` with `$mergeObjects`

The `$mergeObjects` operator combines multiple
documents into a single document.

The following operation uses `$lookup` to join
the `movies` collection with the `comments` collection,
then uses `$mergeObjects` in
`$replaceRoot` to merge the first comment document
with the movie document:

```javascript
```

Output:

```javascript
```

### Use Multiple Join Conditions and a Correlated Subquery

Pipelines can execute on a foreign collection and include
multiple join conditions. The `$expr` operator enables
more complex join conditions including conjunctions and
non-equality matches.

A join condition can reference a field in the local collection
on which the `aggregate()` method was
run and reference a field in the foreign collection. This
allows a correlated subquery between the two collections.

MongoDB 5.0 supports concise correlated subqueries.

The following example:

- Joins the `movies` and `comments` collections using the
  `_id` and `movie_id` fields.

- Filters comments to include only those posted after the
  movie's release year.

```javascript
```

Output:

```javascript
```

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, post_release_comments
FROM movies
WHERE post_release_comments IN (
   SELECT name, date
   FROM comments
   WHERE movie_id = movies._id
   AND YEAR(date) > movies.year
);
```

The `$eq`, `$lt`, `$lte`,
`$gt`, and `$gte` comparison operators placed in
an `$expr` operator can use an index on the `from` collection
referenced in a `$lookup` stage. Limitations:

- Indexes can only be used for comparisons between fields and constants, so the
  `let` operand must resolve to a constant.

  For example, a comparison between `$a` and a constant 
  value can use an index, but a comparison between `$a` and `$b` 
  cannot.

- Indexes are not used for comparisons where the `let` operand resolves to an
  empty or missing value.

- Multikey, partial, or 
  sparse indexes are not used.

For example, if the index `{ movie_id: 1 }` exists on the
`comments` collection:

- The equality match on the `comments.movie_id` field uses
  the index.

**See also:**

- `$expr`
- /reference/aggregation-variables/

### Perform an Uncorrelated Subquery with `$lookup`

An aggregation pipeline `$lookup` stage can execute
a pipeline on the foreign collection, which allows uncorrelated
subqueries. An uncorrelated subquery does not reference the
local document fields.

**Note:**

Starting in MongoDB 5.0, for an uncorrelated subquery in a
`$lookup` pipeline stage containing a `$sample`
stage, the `$sampleRate` operator, or the
`$rand` operator, the subquery is always run again if
repeated. Previously, depending on the subquery output size, either the
subquery output was cached or the subquery was run again.

The following operation joins the `users` collection with
movies that have a runtime greater than 1000 minutes from the
`movies` collection:

```javascript
```

Output:

```javascript
```

The operation corresponds to this pseudo-SQL statement:

```sql
SELECT *, long_movies
FROM users
WHERE long_movies IN (
   SELECT title, year
   FROM movies
   WHERE runtime > 1000
);
```

For more information, see
Uncorrelated Subquery Performance Considerations.

### Perform a Concise Correlated Subquery with `$lookup`

**New in version:** 5.0

Starting in MongoDB 5.0, an aggregation pipeline
`$lookup` stage supports a concise correlated
subquery syntax
that improves joins between collections. The new concise syntax
removes the requirement for an equality match on the foreign and
local fields inside of an `$expr` operator in a
`$match` stage.

The following example:

- Joins the `movies` and `comments` collections by matching
  the localField `_id`
  with the foreignField
  `movie_id`. The match is performed before the `pipeline`
  is run.

- Filters comments to include only those posted after the
  movie's release year, accessed using `$$movie_year` and
  `$date` respectively.

```javascript
```

Output:

```javascript
```

This example uses the older verbose syntax from MongoDB versions
before 5.0 and returns the same results as the previous concise
example:

```javascript
```

Output:

```javascript
```

The previous examples correspond to this pseudo-SQL statement:

```sql
SELECT *, post_release_comments
FROM movies
WHERE post_release_comments IN (
   SELECT *
   FROM comments
   WHERE comments.movie_id = movies._id
   AND YEAR(comments.date) > movies.year
);
```

For more information, see
Correlated Subquery Performance Considerations.

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

The following `Comment` class models the documents in the
`sample_mflix.comments` collection:

```csharp
[BsonIgnoreExtraElements]
public class Comment
{
    [BsonId]
    public ObjectId Id { get; set; }

    [BsonElement("movie_id")]
    public ObjectId MovieId { get; set; }

    [BsonElement("text")]
    public string Text { get; set; } = null!;
}
```

The following `LookupResult` class stores the output of the
`$lookup` stage:

```csharp
[BsonIgnoreExtraElements]
public class LookupResult
{
    [BsonId]
    public ObjectId Id { get; set; }

    [BsonElement("title")]
    public string Title { get; set; } = null!;

    public List<Comment> Comments { get; set; } = [];
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

To use the MongoDB Node.js driver to add a `$lookup` stage to an aggregation
pipeline, use the `$lookup` operator in a pipeline object.

The following example creates a pipeline stage that performs a left outer join between the `movies` and `comments`
collections. The code joins the `_id` field from each `movie`
document to the `movie_id` field in the `comment` documents. The
`comments` field stores the comments for each movie in each
`movie` document. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [
  {
    $lookup: {
      from: "comments",
      localField: "_id",
      foreignField: "movie_id",
      as: "comments"
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```
