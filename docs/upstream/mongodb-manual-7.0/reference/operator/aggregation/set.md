<!-- Converted from reference/operator/aggregation/set.txt (reStructuredText). Includes are inlined. -->

# $set (aggregation stage)

## Definition

**Note:** Disambiguation

The following page refers to the aggregation stage
`$set`. For the update operator `$set`, see `$set`.

**`$set`**

Adds new fields to documents. `$set` outputs documents that
contain all existing fields from the input documents and newly
added fields.

The `$set` stage is an alias for `$addFields`.

Both stages are equivalent to a `$project` stage that
explicitly specifies all existing fields in the input documents and
adds the new fields.

## Compatibility

You can use `$set` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

`$set` has the following form:

```javascript
{ $set: { <newField>: <expression>, ... } }
```

Specify the name of each field to add and set its value to an
aggregation expression or an empty object.
For more information on expressions, see aggregation-expressions.

**Important:**

If the name of the new field is the same as an existing field name
(including `_id`), `$set` overwrites the existing value
of that field with the value of the specified expression.

## Behavior

- `$set` appends new fields to existing documents. You can
  include one or more `$set` stages in an aggregation operation.

- `$set` accepts the embedding of objects where you can set a value to
  an aggregation expression or to an empty object. For example, the following
  nested objects are accepted:

  ```javascript
  {$set: { a: { b: { } } } }
  ```

  To add a field or fields to embedded documents (including documents in
  arrays) use the dot notation. See example.

- To add an element to an existing array field with `$set`, use
  with `$concatArrays`. See example.

## Examples

**shell:**

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Using Two `$set` Stages

The following operation uses two `$set` stages to
include three new fields in the output documents:

```javascript
```

Output:

```javascript
```

First Stage (`$set`):
   The first `$set` stage adds two fields:
   `imdbScoreScaled`, which multiplies the IMDB rating by
   `10`, and `runtimeHours`, which divides the runtime by
   `60` and rounds down to the nearest integer.

Second Stage (`$set`):
   The second `$set` stage adds `totalScore`,
   which sums `imdbScoreScaled` and `runtimeHours`
   computed in the previous stage.

### Adding Fields to an Embedded Document

Use dot notation to add new fields to embedded documents.

The following aggregation operation adds a new field
`normalizedRating` to the embedded document `imdb`:

```javascript
```

Output:

```javascript
```

### Overwriting an Existing Field

Specifying an existing field name in a `$set` operation
causes the original field to be replaced.

The following `$set` operation overrides the `rated`
field:

```javascript
```

Output:

```javascript
```

It is possible to replace one field with another. In the
following example, the `title` field substitutes for the
`_id` field.

The following aggregation operation uses `$set` to replace
the `_id` field of each document with the value of the
`title` field and replaces the `title` field with the
string `"movie"`:

```javascript
```

Output:

```javascript
```

### Add Element to an Array

You can use `$set` with a `$concatArrays`
expression to add an element to an existing array field. The
following operation uses `$set` to replace the
`genres` field with a new array whose elements are the
current `genres` array concatenated with another array
containing a new genre `[ "Classic" ]`:

```javascript
```

Output:

```javascript
```

### Creating a New Field with Existing Fields

The following aggregation operation adds a new field
`titleWithYear` to each document that concatenates the
movie title with its release year:

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

To use the MongoDB Node.js driver to add a `$set` stage to an aggregation
pipeline, use the `$set` operator in a pipeline object.

The following example creates a pipeline stage that sets the value of the `lastupdated` field in each `movie`
document to the value of the `Date` object. The
example then runs the aggregation pipeline:

```javascript
const command = {
  setQuerySettings: {
    find: "movies",
    filter: { year: { $gt: 2011 } },
    sort: { title: 1 },
    $db: "sample_mflix"
  },
  settings: {
    indexHints: {
      ns: { db: "sample_mflix", coll: "movies" },
      allowedIndexes: [ "year_1" ]
    },
    queryFramework: "classic",
    comment: "Index hint for year_1 index to improve query performance"
  }
};

const adminDb = client.db("admin");
const result = adminDb.command(command);
```

## Learn More

To learn more about related pipeline stages, see the `$addFields`
guide.
