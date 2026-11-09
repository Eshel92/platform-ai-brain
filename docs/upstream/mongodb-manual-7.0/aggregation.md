<!-- Converted from aggregation.txt (reStructuredText). Includes are inlined. -->

# Aggregation Operations

Aggregation operations process multiple documents and return computed
results. You can use aggregation operations to:

- Group values from multiple documents.
- Compute a single result from the grouped data.
- Analyze data changes over time.
- Query the most up-to-date version of your data. 

The aggregation operators in MongoDB let you run analytics on your
cluster without moving data to another platform.

## Get Started

To perform aggregation operations, you can use:

- Aggregation pipelines, the
  preferred method.
- Single purpose aggregation methods, which have less functionality than an
  aggregation pipeline.

You can run aggregation pipelines in the UI for deployments hosted in [MongoDB Atlas](https://www.mongodb.com/docs/atlas).

## Aggregation Pipelines

An aggregation pipeline consists of one or more stages that process documents:

- Each stage performs an operation on the input documents.
  For example, a stage can filter documents, group documents, and
  calculate values.

- The documents that are output from a stage are passed to the next
  stage.

- An aggregation pipeline can return results for groups of documents.
  For example, return the total, average, maximum, and minimum values.

You can update documents with an aggregation pipeline if you use the stages 
shown in updates-agg-pipeline.

**Note:**

Aggregation pipelines run with the
`db.collection.aggregate()` method do not modify documents in
a collection, unless the pipeline contains a `$merge` or
`$out` stage.

### Aggregation Pipeline Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following pipeline finds the top three directors who have directed
the most movies in the database.

Use a `$match` stage to filter to movies that have directors
listed (excluding documents where the directors field is null or empty):

```javascript
{
    $match : {
        "directors" : { $exists: true, $ne: null, $not: {$size: 0} }
    }
},
```

The `$match` stage reduces the number of documents in our pipeline by 
filtering out movies without director information. Next, use
`$unwind` to deconstruct the directors array so you can
count movies per individual director:

```javascript
{
    $unwind : "$directors"
},
```

Use `$group` to group documents by director name and count
each director's movies:

```javascript
{
    $group : {
    _id : "$directors",
    movieCount : {
        $sum: 1
        }
    }
},
```

Use `$sort` to order the remaining documents in descending
order by movie count:

```javascript
{
    $sort : {
        movieCount : -1
    }
},
```

Use `$limit` to return the top three directors:

```javascript
{
    $limit : 3
}
```

The full pipeline:

```javascript
db.movies.aggregate(
  [
    {
        $match : {
            "directors" : { $exists: true, $ne: null, $not: {$size: 0} }
        }
    },
    {
        $unwind : "$directors"
    },
    {
        $group : {
        _id : "$directors",
        movieCount : {
            $sum: 1
            }
        }
    },
    {
        $sort : {
            movieCount : -1
        }
    },
    {
        $limit : 3
    }
  ]
)
```

The pipeline returns these results:

```javascript
[
  { _id: 'Woody Allen', movieCount: 40 },
  { _id: 'Martin Scorsese', movieCount: 32 },
  { _id: 'Takashi Miike', movieCount: 31 }
]
```

For runnable examples containing sample input documents, see
aggregation-pipeline-examples.

To learn more about aggregation pipelines, see
aggregation-pipeline.

## Single Purpose Aggregation Methods

Single purpose aggregation methods aggregate documents from a single
collection. These methods have less functionality than an aggregation
pipeline.

| Method | Description |
|---|---|
| `db.collection.estimatedDocumentCount()` | Returns an approximate count of the documents in a collection or a view. |
| `db.collection.count()` | Returns a count of the number of documents in a collection or a view. |
| `db.collection.distinct()` | Returns an array of documents that have distinct values for the specified field. |
