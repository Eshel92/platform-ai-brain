<!-- Converted from reference/operator/aggregation/unionWith.txt (reStructuredText). Includes are inlined. -->

# $unionWith (aggregation stage)

## Definition

**`$unionWith`**

Combines two aggregations into a single result set. `$unionWith`
outputs the combined result set (including duplicates) to the next
stage.

The order in which the combined result set documents are output is
unspecified.

## Syntax

The `$unionWith` stage has the following syntax:

```javascript
{ $unionWith: { coll: "<collection>", pipeline: [ <stage1>, ... ] } }
```

To include all documents from the specified collection without any
processing, you can use the simplified form:

```javascript
{ $unionWith: "<collection>" }  // Include all documents from the specified collection
```

The `$unionWith` stage takes a document with the following fields:

* - Field
  - Necessity
  - Description

* - coll

  - Required if `pipeline` is omitted. Otherwise optional.

  - ..  _unionWith-coll:

    The collection or view whose pipeline
    results you want to include in the result set.

    If you omit the `coll` field, you must specify a `pipeline`
    field with a first stage of `$documents`.

* - pipeline

  - Required if `coll` is omitted. Otherwise optional.

  - ..  _unionWith-pipeline:

    An aggregation pipeline to apply to the input documents.

    - If you specify `coll`, the pipeline applies to the documents
      in `coll`.

    - If you omit `coll`, the pipeline applies to the documents in
      the pipeline's `$documents` stage. For an example, see
      unionWith-example-specified-docs.

    The pipeline cannot include the `$out` and
    `$merge` stages. Starting in v6.0, the `pipeline`
    can contain the Atlas Search
    `$search` stage as the first stage inside the pipeline.
    To learn more, see fts-unionwith-behavior.

The `$unionWith` operation would correspond to the following
SQL statement:

```sql
SELECT *
FROM Collection1
WHERE ...
UNION ALL
SELECT *
FROM Collection2
WHERE ...
```

## Considerations

### Duplicate Results

The combined results from the previous stage and the
`$unionWith` stage can include duplicates.

For example, the following aggregation combines the `title` field
projection results from two queries on the `movies` collection. The
result set contains duplicates:

```javascript
```

Output:

```javascript
```

To remove the duplicates, you can include a `$group` stage to
group by the `title` field. The result set no longer contains
duplicates:

```javascript
```

Output:

```javascript
```

### Collation

If the `db.collection.aggregate()` includes a `collation`
document, the operation uses that collation and ignores any other
collations.

If the `db.collection.aggregate()` does not include a
`collation` document, the `db.collection.aggregate()` method
uses the collation for the top-level collection/view on which the
`db.collection.aggregate()` is run:

- If the $unionWith coll is a collection, its
  collation is ignored.

- If the $unionWith coll is a view, then its collation must match that of the
  top-level collection/view. Otherwise, the operation errors.

### Atlas Search Support

Starting in MongoDB 6.0, you can specify the Atlas Search `$search` or `$searchMeta` stage
in the `$unionWith` pipeline to search collections on the Atlas
cluster. The `$search` or the `$searchMeta` stage
must be the first stage inside the `$unionWith` pipeline.

**search:**

```
[{
  "$unionWith": {
    "coll": <collection-name>,
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
  "$unionWith": {
    "coll": <collection-name>,
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

To see an example of `$unionWith` with `$search`,
see the Atlas Search tutorial Run a Atlas Search $search Query
Using $unionWith.

### Restrictions

| Restrictions | Description |
|---|---|
| transactions | An aggregation pipeline cannot use `$unionWith` inside transactions. |
| `$out` | The $unionWith pipeline cannot include the `$out` stage. |
| `$merge` | The $unionWith pipeline cannot include the `$merge` stage. |

## Examples

**shell:**

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Create Movie Reports from the Union of Movie Data

The following examples use the `$unionWith` stage to
combine data and return results from the `movies` collection.

### Report 1: All Movies by Category and Year

The following aggregation creates a movie report that lists movies
by category. The pipeline uses `$unionWith` to combine
documents from the `movies` collection:

```javascript
```

Output:

```javascript
```

Specifically, the aggregation pipeline uses:

- A `$match` stage to select movies released before
  `1910`.

- A `$set` stage to add a `category` field with the
  value `Early Cinema`.

- A `$unionWith` stage to combine documents from the
  `movies` collection, filtered to movies with a `runtime`
  greater than `1000` and tagged with the `Long Runtime`
  category.

- A `$project` stage to return only the `title`,
  `year`, and `category` fields.

- A `$sort` stage to sort by the `category`, the
  `year`, and the `title`.

### Report 2: Aggregated Runtime by Genre

The following aggregation creates a movie report that lists the
total runtime per genre. The pipeline uses `$unionWith`
to combine documents from the `movies` collection:

```javascript
```

Output:

```javascript
```

- The `$match` and `$unionWith` stages retrieve
  documents from the `movies` collection into the pipeline.

- The `$group` stage groups by the `genres` field and
  uses `$sum` to calculate the total `runtime` per
  `genres` value.

- The `$sort` stage orders the documents by descending
  `totalRuntime`.

### Create a Union with Specified Documents

You can use `$unionWith` to perform a union with documents that you
specify in the `pipeline` field. When you specify a
`$documents` stage in the `pipeline` field, you perform a
union with documents that aren't stored in a separate collection.

The following `$unionWith` operation performs a union with documents
specified in the `pipeline` `$documents` field:

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

To use the MongoDB Node.js driver to add a `$unionWith` stage to an aggregation
pipeline, use the `$unionWith` operator in a pipeline object.

The following example creates a pipeline stage that combines the incoming documents from the `sample_mflix.movies` collection
with the `movie` documents in the `sample_mflix.movies` collection. The
example then runs the aggregation pipeline:

```javascript
const db = client.db("sample_mflix");
const collection = db.collection("movies");

const pipeline = [{ $unionWith: { coll: "Movies" } }];

const cursor = collection.aggregate(pipeline);
return cursor;
```
