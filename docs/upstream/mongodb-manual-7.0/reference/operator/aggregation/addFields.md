<!-- Converted from reference/operator/aggregation/addFields.txt (reStructuredText). Includes are inlined. -->

# $addFields (aggregation stage)

## Definition

**`$addFields`**

Adds new fields to documents. `$addFields` outputs documents that
contain all existing fields from the input documents and newly
added fields.

The `$addFields` stage is equivalent to a
`$project` stage that explicitly specifies all existing
fields in the input documents and adds the new fields.

**Note:**

You can also use the `$set` stage, which is an alias for
`$addFields`.

## Compatibility

You can use `$addFields` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The stage has the following syntax:

```javascript
{ $addFields: { <newField>: <expression>, ... } }
```

Specify the name of each field to add and set its value to an
aggregation expression or an empty
object.

**Important:**

If the name of the new field is the same as an existing field name
(including `_id`), `$addFields` overwrites the existing value
of that field with the value of the specified expression.

## Behavior

- `$addFields` appends new fields to existing documents. You can
  include one or more `$addFields` stages in an aggregation operation.

- `$addFields` accepts the embedding of objects where you can set a value to
  an aggregation expression or to an empty object. For example, the following
  nested objects are accepted:

  ```javascript
  {$addFields: { a: { b: { } } } }
  ```

  To add a field or fields to embedded documents (including documents in
  arrays) use the dot notation. See example.

- To add an element to an existing array field with
  `$addFields`, use `$concatArrays`. See
  example.

## Examples

**shell:**

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Using Two `$addFields` Stages

The following operation uses two
`$addFields` stages to first convert runtime to
hours, then compute a licensing fee at $0.50 per hour:

```javascript
```

Output:

```javascript
```

### Adding Fields to an Embedded Document

Use dot notation to add new fields to embedded documents.

The following aggregation operation
adds a `certified` field to the embedded `imdb` document
in each movie:

```javascript
```

Output:

```javascript
```

### Overwriting an Existing Field

Specifying an existing field name in an `$addFields` operation
causes the original field to be replaced.

The following
`$addFields` operation overwrites the `runtime` field
to add 15 minutes:

```javascript
```

Output:

```javascript
```

You can also replace one field with another. The following operation sets
`_id` to the movie's title and replaces the `title` field with the
movie's primary genre:

```javascript
```

Output:

```javascript
```

### Add Element to an Array

You can use `$addFields` with a
`$concatArrays` expression to add an element to an
existing array field. The following operation appends `Epic` to the
`genres` array of movies with the title `Centennial`:

```javascript
```

Output:

```javascript
```

### Remove Fields

You can use `$addFields` with the `$$REMOVE`
variable to remove document fields.

The following operation uses `$addFields` to
remove the `plot` field with the `$$REMOVE` variable:

```javascript
```

Output:

```javascript
```

You can also use `$$REMOVE` to conditionally remove fields. For
example, the following aggregation removes the `rated` field from
documents where `rated` is `null`:

```javascript
```

Output:

```javascript
```

**nodejs:**

The Node.js examples on this page use the `sample_mflix` database from the
Atlas sample datasets. To learn how to create a free
MongoDB Atlas cluster and load the sample datasets, see `Get Started` in the MongoDB Node.js driver documentation.

To use the MongoDB Node.js driver to add a `$addFields` stage to an aggregation
pipeline, use the `$addFields` operator in a pipeline object.

The following example creates a pipeline stage that adds a `totalReviews` field to each movie document, which
contains the movie's total number of reviews. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [
  {
    $addFields: {
      totalReviews: {
        $add: ["$imdb.votes", "$tomatoes.viewer.numReviews"]
      }
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

**Tip:** Comparison with $project

You can use either the `$addFields` or `$project` stage to remove
document fields. The best approach depends on your pipeline and how much
of the original document you want to retain.

For an example using `$$REMOVE` in a `$project` stage, see
remove-example.

## Learn More

To learn more about related pipeline stages, see the `$project` and
`$set` guides.
