<!-- Converted from reference/operator/aggregation/sortByCount.txt (reStructuredText). Includes are inlined. -->

# $sortByCount (aggregation)

## Definition

**`$sortByCount`**

Groups incoming documents based on the value of a specified
expression, then computes the count of documents in each distinct
group.

Each output document contains two fields: an `_id` field
containing the distinct grouping value, and a `count` field
containing the number of documents belonging to that grouping or
category.

The documents are sorted by `count` in descending order.

The `$sortByCount` stage has the following prototype form:

```javascript
{ $sortByCount:  <expression> }
```

* - Field
  - Description

* - `expression`

  - Expression to group by. You
    can specify any expression except for a document literal.

    To specify a field path,
    prefix the field name with a dollar sign `$` and enclose it
    in quotes. For example, to group by the field `employee`,
    specify `"$employee"` as the expression.

    ```javascript
    { $sortByCount:  "$employee" }
    ```

    Although you cannot specify a document literal for the group
    by expression, you can, however, specify a field or an
    expression that evaluates to a document. For example, if
    `employee` and `business` fields are document fields,
    then the following `$mergeObjects` expression,
    which evaluates to a document, is a valid argument to
    `$sortByCount`:

    ```javascript
    { $sortByCount: { $mergeObjects: [ "$employee", "$business" ] } }
    ```

    However, the following example with the document literal
    expression is invalid:

    ```javascript
    { $sortByCount: { lname: "$employee.last", fname: "$employee.first" } }
    ```

**See also:**

/reference/bson-type-comparison-order/

## Considerations

### `$sortByCount` and Memory Restrictions

Starting in MongoDB 6.0, pipeline stages that require more than 100 
megabytes of memory to execute write temporary files to disk by 
default. These temporary files last for the duration of the pipeline 
execution and can influence storage space on your instance. In earlier 
versions of MongoDB, you must pass  `{ allowDiskUse: true }` to 
individual `find` and `aggregate` commands to enable this 
behavior.

Individual `find` and `aggregate` commands can override the 
`allowDiskUseByDefault` parameter by either:

- Using `{ allowDiskUse: true }` to allow writing temporary files out 
  to disk when `allowDiskUseByDefault` is set to `false`

- Using `{ allowDiskUse: false }` to prohibit writing temporary files
  out to disk when `allowDiskUseByDefault` is set to `true`

**Note:**

For MongoDB Atlas, it is recommended to
configure storage auto-scaling to prevent 
long-running queries from filling up storage with temporary files.

If your Atlas cluster uses storage auto-scaling, the temporary files 
may cause your cluster to scale to the next storage tier.

For additional details, see agg-pipeline-limits.

## Behavior

The `$sortByCount` stage is equivalent to the
following `$group` + `$sort` sequence:

```javascript
{ $group: { _id: <expression>, count: { $sum: 1 } } },
{ $sort: { count: -1 } }
```

## Examples

**shell:**

Consider a collection `exhibits` with the following documents:

```javascript
db.exhibits.insertMany(
   [
      { _id: 1, title: "The Pillars of Society", artist: "Grosz", year: 1926, tags: [ "painting", "satire", "Expressionism", "caricature" ] },
      { _id: 2, title: "Melancholy III", artist: "Munch", year: 1902, tags: [ "woodcut", "Expressionism" ] },
      { _id: 3, title: "Dancer", artist: "Miro", year: 1925, tags: [ "oil", "Surrealism", "painting" ] },
      { _id: 4, title: "The Great Wave off Kanagawa", artist: "Hokusai", tags: [ "woodblock", "ukiyo-e" ] },
      { _id: 5, title: "The Persistence of Memory", artist: "Dali", year: 1931, tags: [ "Surrealism", "painting", "oil" ] },
      { _id: 6, title: "Composition VII", artist: "Kandinsky", year: 1913, tags: [ "oil", "painting", "abstract" ] },
      { _id: 7, title: "The Scream", artist: "Munch", year: 1893, tags: [ "Expressionism", "painting", "oil" ] },
      { _id: 8, title: "Blue Flower", artist: "O'Keefe", year: 1918, tags: [ "abstract", "painting" ] }
   ]
)
```

The following operation `unwinds` the `tags`
array and uses the `$sortByCount` stage to count the
number of documents associated with each tag:

```javascript
db.exhibits.aggregate( [ { $unwind: "$tags" },  { $sortByCount: "$tags" } ] )
```

The operation returns the following documents, sorted in descending
order by count:

```javascript
[
   { _id: "painting", count: 6 },
   { _id: "oil", count: 4 },
   { _id: "Expressionism", count: 3 },
   { _id: "Surrealism", count: 2 },
   { _id: "abstract", count: 2 },
   { _id: "woodblock", count: 1 },
   { _id: "woodcut", count: 1 },
   { _id: "ukiyo-e", count: 1 },
   { _id: "satire", count: 1 },
   { _id: "caricature", count: 1 }
]
```

**csharp:**

The C# examples on this page use the `sample_mflix` database
from the Atlas sample datasets. To learn how to create a
free MongoDB Atlas cluster and load the sample datasets, see
`Get Started` in the MongoDB .NET/C#
Driver documentation.

The following `Movie` class models the documents in the `sample_mflix.movies`
collection:

```csharp
public class Movie
{
    public string Id { get; set; }

    public int Runtime { get; set; }

    public string Title { get; set; }

    public string Rated { get; set; }

    public List<string> Genres { get; set; }

    public string Plot { get; set; }

    public ImdbData Imdb { get; set; }

    public int Year { get; set; }

    public int Index { get; set; }

    public string[] Comments { get; set; }

    [BsonElement("lastupdated")]
    public DateTime LastUpdated { get; set; }
}
```

To use the MongoDB {+csharp-driver-short+} to add a `$sortByCount` stage to an aggregation
pipeline, call the [SortByCount()](https://mongodb.github.io/mongo-csharp-driver/3.3.0/api/MongoDB.Driver/MongoDB.Driver.PipelineStageDefinitionBuilder.SortByCount.html) method on a `PipelineDefinition` object.

The following example creates a pipeline stage that groups the incoming `Movie` documents by the value of their `Rated` field,
and then returns the number of documents in each group:

```csharp
var pipeline = new EmptyPipelineDefinition<Movie>()
    .SortByCount(m => m.Rated);
```
