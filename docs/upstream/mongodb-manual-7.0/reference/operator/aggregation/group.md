<!-- Converted from reference/operator/aggregation/group.txt (reStructuredText). Includes are inlined. -->

# $group (aggregation stage)

## Definition

**`$group`**

The $group stage combines multiple documents with the same field, fields, or
expression into a single document according to a group key. The
result is one document per unique group key.

A group key is often a field, or group of fields. The group key can
also be the result of an expression. Use the `_id` field in the
`$group` pipeline stage to set the group key. See below for
usage examples.

In the `$group` stage output, the `_id` field is set to the
group key for that document.

The output documents can also contain additional fields that are
set using accumulator expressions.

**Note:**

`$group` does *not* order its output documents.

## Compatibility

You can use `$group` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$group` stage has the following prototype form:

```javascript
{
 $group:
   {
     _id: <expression>, // Group key
     <field1>: { <accumulator1> : <expression1> },
     ...
   }
 }
```

| Field | Description |
|---|---|
| `_id` | *Required.* The `_id` expression specifies the group key. If you specify an `_id` value of null, or any other constant value, the `$group` stage returns a single document that aggregates values across all of the input documents. See the Group by Null example. |
| `field` | *Optional.* Computed using the accumulator operators. |

The `_id` and the accumulator operators
can accept any valid `expression`. For more information on
expressions, see aggregation-expressions.

## Considerations

### Performance

`$group` is a blocking stage, which causes the pipeline to wait for all
input data to be retrieved for the blocking stage before processing the
data. A blocking stage may reduce performance because it reduces
parallel processing for a pipeline with multiple stages. A blocking
stage may also use substantial amounts of memory for large data sets.

### Accumulator Operator

The `<accumulator>` operator must be one of the following accumulator
operators:

* - Name
  - Description

* - `$accumulator`

  - Returns the result of a user-defined accumulator function.

* - `$addToSet`

  - Returns an array of *unique* expression values for each group.
    Order of the array elements is undefined.

* - `$avg`

  - Returns an average of numerical values.

* - `$bottom`

  - .. include:: /includes/accumulators/bottom-definition.rst

* - `$bottomN`

  - Returns an aggregation of the bottom `n` fields within a group,
    according to the specified sort order.

* - `$count`

  - Returns the number of documents in a group.

    Distinct from the `$count` pipeline stage.

* - `$first`

  - Returns the result of an expression for the first document in a group.

* - `$firstN`

  - Returns an aggregation of the first `n` elements within a group.
    Only meaningful when documents are in a defined order.
    Distinct from the `$firstN` array operator.

* - `$last`

  - Returns the result of an expression for the last document in a group.

* - `$lastN`

  - Returns the result of evaluating a specified expression over
    the last n elements in a group.

* - `$max`

  - Returns the highest expression value for each group.

* - `$maxN`

  - Returns an aggregation of the `n` maximum valued elements in
    a group.
    Distinct from the `$maxN` array operator.

* - `$median`
  - .. include:: /includes/aggregation/fact-return-median-accumulator.rst

    **New in version:** 7.0

* - `$mergeObjects`

  - Returns a document created by combining the input documents
    for each group.

* - `$min`

  - Returns the lowest expression value for each group.

* - `$minN`

  - Returns an aggregation of the `n` minimum valued elements
    in a group.
    Distinct from the `$minN` array operator.

* - `$percentile`
  - .. include:: /includes/aggregation/fact-return-percentile.rst

    **New in version:** 7.0

* - `$push`

  - Returns an array of expression values for documents in each
    group.

* - `$stdDevPop`

  - Returns the population standard deviation of values from
    documents in a group.

* - `$stdDevSamp`

  - Returns the sample standard deviation of values from documents
    in a group.

* - `$sum`

  - Returns a sum of numerical values. Ignores non-numeric values.

* - `$top`

  - Returns the top element within a group according to the
    specified sort order.

* - `$topN`

  - Returns an aggregation of the top `n` fields within a group,
    according to the specified sort order.

### `$group` and Memory Restrictions

If the `$group` stage exceeds 100 megabytes of RAM, MongoDB writes
data to temporary files. However, if the
allowDiskUse option is set to `false`,
`$group` returns an error. For more information, refer to
aggregation pipeline limits.

This behavior applies to the state of the `$group` stage itself.
Certain accumulators, such as `$push` and `$addToSet`,
can cause a single accumulated object to grow beyond the memory
threshold. These accumulators can't write temporary files to disk. If
the accumulated object exceeds the memory limit, the operation
returns an error even when the `allowDiskUse` option is `true`.

### `$group` Performance Optimizations

This section describes optimizations to improve the performance of
`$group`. There are optimizations that you can make manually
and optimizations MongoDB makes internally.

#### Optimization to Return the First or Last Document of Each Group

If a pipeline `sorts` and `groups`
by the same field and the `$group` stage only uses the `$first`
or `$last` accumulator operator, consider adding an index on the grouped field which matches the sort order. In some
cases, the `$group` stage can use the index to quickly find the first
or last document of each group.

**Example:**

If the `movies` collection contains an index
`{ year: 1, title: 1 }`, the following pipeline can use that
index to find the first document of each group:

```javascript
db.movies.aggregate([
   {
      $sort: { year: 1, title: 1 }
   },
   {
      $group: {
         _id: { year: "$year" },
         title: { $first: "$title" }
      }
   }
])
```

#### Slot-Based Query Execution Engine

**Note:**

Starting in version 7.0.17, the slot-based query execution engine is no longer
enabled by default for patch versions of 7.0. If you want 
your queries to use the slot-based query execution engine, please upgrade to 
version 8.0, where it is enabled by default.

Starting in version 5.2, MongoDB uses the slot-based execution
query engine to execute `$group` stages
if either:

- `$group` is the first stage in the pipeline.

- All preceding stages in the pipeline can also be executed by the
  slot-based execution engine.

For more information, see agg-group-optimization-sbe.

## Examples

**shell:**

### Count the Number of Documents in a Collection

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following aggregation operation uses the `$group`
stage to count the number of documents in the `movies`
collection:

```javascript
```

Output:

```javascript
```

This aggregation operation is equivalent to the following SQL
statement:

```sql
SELECT COUNT(*) AS count FROM movies
```

**See also:**

- `$count`
- `$count (aggregation accumulator)`

### Retrieve Distinct Values

The following aggregation operation uses the `$group`
stage to retrieve the distinct `rated` values from the
`movies` collection:

```javascript
```

Output:

```javascript
```

**Note:**

When you use `$group` to retrieve distinct values in a sharded
collection, if the operation results in a `DISTINCT_SCAN`, the
result might contain orphaned documents.

The only semantically correct pipeline that is impacted is
effectively a logical equivalent of a `distinct` command,
where there is a `$group` stage at or near the beginning of the
pipeline and the `$group` is not preceded by a `$sort`
stage.

For example, `$group` operations of the following form can
result in a `DISTINCT_SCAN`:

```javascript
{ $group : { _id : "$<field>" } }
```

For more information on behavior for retrieving distinct
values, see the
distinct command behavior.

To see whether your operation results in a
`DISTINCT_SCAN`, check your operation's
explain results.

### Group by Rating

The following aggregation operation groups documents by the
`rated` field, calculating the total runtime per rating and
returning only the ratings with a total runtime greater than or
equal to 100000:

```javascript
```

Output:

```javascript
```

First Stage:
  The `$group` stage groups the documents by `rated`
  to retrieve the distinct rating values. This stage returns the
  `totalRuntime` for each rating group.

Second Stage:
  The `$match` stage filters the resulting documents to
  return only ratings with a `totalRuntime` greater than or
  equal to 100000.

This aggregation operation is equivalent to the following SQL
statement:

```sql
SELECT rated,
   Sum(runtime) AS totalRuntime
FROM   movies
GROUP  BY rated
HAVING totalRuntime >= 100000
```

**See also:**

`$match`

### Calculate Count, Sum, and Average

#### Group by Year

The following pipeline calculates the total runtime, average
runtime, and movie count for each year before 1910:

```javascript
```

Output:

```javascript
```

First Stage:
  The `$match` stage filters the documents to only
  pass movies released before 1910 to the next stage.

Second Stage:
  The `$group` stage groups the documents by year and
  calculates the total runtime, average runtime, and total count
  of the documents in each group.

Third Stage:
  The `$sort` stage sorts the results by the total
  runtime for each group in descending order.

This aggregation operation is equivalent to the following SQL
statement:

```sql
SELECT year,
       Sum(runtime) AS totalRuntime,
       Avg(runtime) AS averageRuntime,
       Count(*)     AS count
FROM   movies
WHERE  year < 1910
GROUP  BY year
ORDER  BY totalRuntime DESC
```

**See also:**

- `$match`
- `$sort`
- `db.collection.countDocuments()` which wraps the
  `$group` aggregation stage with a
  `$sum` expression.

#### Group by `null`

The following aggregation operation specifies a group `_id` of
`null`, calculating the total runtime, average runtime, and
count of all documents in the collection.

```javascript
```

Output:

```javascript
```

This aggregation operation is equivalent to the following SQL
statement:

```sql
SELECT Sum(runtime) AS totalRuntime,
       Avg(runtime) AS averageRuntime,
       Count(*)     AS count
FROM   movies
```

**See also:**

- `$count`
- `db.collection.countDocuments()` which wraps the
  `$group` aggregation stage with a
  `$sum` expression.

### Pivot Data

#### Group Titles by Year

The following aggregation operation pivots the data in the
`movies` collection to group titles by year:

```javascript
```

Output:

```javascript
```

#### Group Documents by Year

The following aggregation operation groups documents by year:

```javascript
```

Output:

```javascript
```

First Stage:
  `$match` filters the documents to only pass movies
  released before 1910 to the next stage.

Second Stage:
  `$group` uses the `$$ROOT`
  system variable to group the entire documents by year.

Third Stage:
  `$addFields` adds a field to the output containing
  the total runtime of movies for each year.

  **Note:**

  The resulting documents must not exceed the
  `BSON Document Size` limit of 16 mebibytes.

Fourth Stage:
  `$sort` sorts the resulting documents by `_id`
  in ascending order.

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

To use the MongoDB Node.js driver to add a `$group` stage to an aggregation
pipeline, use the `$group` operator in a pipeline object.

The following example creates a pipeline stage that groups documents by the value of their `rated` field. Each output
document contains a `rating` field that stores each group's
rating. Each output document also contains a field named
`totalRuntime` that stores the total runtime of all movies in the
group. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [
  {
    $group: {
      _id: "$rated",
      rating: { $first: "$rated" },
      totalRuntime: { $sum: "$runtime" }
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

## Learn More

The agg-example-group-data tutorial provides an extensive example
of the `$group` operator in a common use case.

To learn more about related pipeline stages, see the `$addFields`
guide.
