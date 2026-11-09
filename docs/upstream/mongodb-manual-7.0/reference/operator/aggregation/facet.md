<!-- Converted from reference/operator/aggregation/facet.txt (reStructuredText). Includes are inlined. -->

# $facet (aggregation stage)

## Definition

**`$facet`**

Processes multiple aggregation pipelines within a single stage on the same set of
input documents. Each sub-pipeline has its own field in the output
document where its results are stored as an array of documents.

The `$facet` stage allows you to create multi-faceted aggregations
which characterize data across multiple dimensions, or facets,
within a single aggregation stage. Multi-faceted aggregations
provide multiple filters and categorizations to guide data browsing
and analysis. Retailers commonly use faceting to narrow search results
by creating filters on product price, manufacturer, size, etc.

Input documents are passed to the `$facet` stage only once,
enabling various aggregations on the same set of input documents.

## Compatibility

You can use `$facet` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$facet` stage has the following form:

```javascript
{ $facet:
    {
      <outputField1>: [ <stage1>, <stage2>, ... ],
      <outputField2>: [ <stage1>, <stage2>, ... ],
      ...

    }
}
```

Specify the output field name for each specified pipeline.

## Considerations

As each stage in a `$facet` executes, the resulting document is
limited to 100 megabytes. Note the allowDiskUse flag doesn't affect the 100 megabyte size
limit, since `$facet` can't spill to disk.

The final output document is subject to the 16 mebibyte `BSON
document size limit`. If it exceeds 16 mebibytes,
the aggregation produces an error.

**See also:**

agg-pipeline-limits

## Behavior

Facet-related aggregation stages categorize and group incoming
documents. Specify any of the following facet-related stages within
different `$facet` sub-pipeline's `<stage>` to perform a
multi-faceted aggregation:

- `$bucket`
- `$bucketAuto`
- `$sortByCount`

Other aggregation stages can also be used with
`$facet` with the following exceptions:

- `$collStats`
- `$facet`
- `$geoNear`
- `$indexStats`
- `$out`
- `$merge`
- `$planCacheStats`
- `$search`
- `$searchMeta`
- `$vectorSearch`

Each sub-pipeline within `$facet` is passed the exact same set of
input documents. These sub-pipelines are completely independent of one
another and the document array output by each is stored in separate
fields in the output document. The output of one sub-pipeline can not
be used as the input for a different sub-pipeline within the same
`$facet` stage. If further aggregations are required, add additional
stages after `$facet` and specify the field name, `<outputField>`,
of the desired sub-pipeline output.

### Index Use

Pipeline order determines how the `$facet` stage uses indexes.

- If the `$facet` stage is the first stage in a pipeline, the stage
  will perform a `COLLSCAN`. The `$facet` stage does not make use of
  indexes if it is the first stage in the pipeline.

- If the `$facet` stage comes later in the pipeline and earlier stages
  have used indexes, `$facet` will not trigger a `COLLSCAN` during
  execution.

For example, `$match` or `$sort` stages that come
before a `$facet` stage can make use of indexes and the `$facet`
will not trigger a `COLLSCAN`.

For optimization suggestions, see: agg-pipeline-optimization.

## Examples

**shell:**

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following aggregation pipeline uses the `movies` collection to
categorize films across multiple dimensions. A `$match` stage
limits the input to movies with a runtime greater than 1,000 minutes. The
`$facet` stage runs three sub-pipelines in parallel using
`$sortByCount`, `$bucket`, and
`$bucketAuto`. MongoDB fetches input documents from the
`movies` collection only once, at the beginning of the operation:

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

To use the MongoDB Node.js driver to add a `$facet` stage to an aggregation
pipeline, use the `$facet` operator in a pipeline object.

The following example creates a pipeline stage that executes two parallel aggregations. The first aggregation distributes
incoming documents into five groups by the value of their `runtime`
field by using the `$bucketAuto` stage. The second
aggregation counts each value in the `rated` field and returns the
count of the top five values by using the `$sortByCount`
and `$limit` stages. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [
  {
    $facet: {
      bucketPipeline: [
        {
          $bucketAuto: {
            groupBy: "$runtime",
            buckets: 5
          }
        }
      ],
      countLimit: [
        { $sortByCount: "$rated" },
        { $limit: 5 }
      ]
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

## Learn More

To learn more about related pipeline stages, see the `$bucketAuto`,
`$sortByCount`, and `$limit` guides.
