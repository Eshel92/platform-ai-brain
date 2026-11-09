<!-- Converted from reference/operator/aggregation/set.txt (reStructuredText). Includes are inlined. -->

# $set (aggregation)

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

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
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
aggregation expression. For more
information on expressions, see aggregation-expressions.
   

**Important:**

If the name of the new field is the same as an existing field name
(including `_id`), `$set` overwrites the existing value
of that field with the value of the specified expression.

## Behavior

`$set` appends new fields to existing documents. You can
include one or more `$set` stages in an aggregation operation.

To add field or fields to embedded documents (including documents in
arrays) use the dot notation. See example.

To add an element to an existing array field with `$set`, use
with `$concatArrays`. See example.

## Examples

**shell:**

### Using Two `$set` Stages

Create a sample `scores` collection with the following:

```javascript
db.scores.insertMany( [
   { _id: 1, student: "Maya", homework: [ 10, 5, 10 ], quiz: [ 10, 8 ], extraCredit: 0 },
   { _id: 2, student: "Ryan", homework: [ 5, 6, 5 ], quiz: [ 8, 8 ], extraCredit: 8 }
] )
```

The following operation uses two `$set` stages to
include three new fields in the output documents:

```javascript
db.scores.aggregate( [
   {
     $set: {
        totalHomework: { $sum: "$homework" },
        totalQuiz: { $sum: "$quiz" }
     }
   },
   {
     $set: {
        totalScore: { $add: [ "$totalHomework", "$totalQuiz", "$extraCredit" ] } }
   }
] )
```

The operation returns the following documents:

```javascript
[
   {
      _id: 1,
      student: "Maya",
      homework: [ 10, 5, 10 ],
      quiz: [ 10, 8 ],
      extraCredit: 0,
      totalHomework: 25,
      totalQuiz: 18,
      totalScore: 43
   },
   {
      _id: 2,
      student: "Ryan",
      homework: [ 5, 6, 5 ],
      quiz: [ 8, 8 ],
      extraCredit: 8,
      totalHomework: 16,
      totalQuiz: 16,
      totalScore: 40
   }
]
```

### Adding Fields to an Embedded Document

Use dot notation to add new fields to embedded documents.

Create a sample collection `vehicles` with the following:

```javascript
db.vehicles.insertMany( [
   { _id: 1, type: "car", specs: { doors: 4, wheels: 4 } },
   { _id: 2, type: "motorcycle", specs: { doors: 0, wheels: 2 } },
   { _id: 3, type: "jet ski" }
] )
```

The following aggregation operation adds a new field `fuel_type` to
the embedded document `specs`.

```javascript
db.vehicles.aggregate( [
   { $set: { "specs.fuel_type": "unleaded" } }
] )
```

The operation returns the following results:

```javascript
[
   { _id: 1, type: "car", specs: { doors: 4, wheels: 4, fuel_type: "unleaded" } },
   { _id: 2, type: "motorcycle", specs: { doors: 0, wheels: 2, fuel_type: "unleaded" } },
   { _id: 3, type: "jet ski", specs: { fuel_type: "unleaded" } }
]
```

### Overwriting an existing field

Specifying an existing field name in a `$set` operation
causes the original field to be replaced.

Create a sample collection called `animals` with the following:

```javascript
db.animals.insertOne( { _id: 1, dogs: 10, cats: 15 } )
```

The following `$set` operation overrides the `cats` field:

```javascript
db.animals.aggregate( [
  { $set: { cats: 20 } }
] )
```

The operation returns the following document:

```javascript
[ { _id: 1, dogs: 10, cats: 20 } ]
```

It is possible to replace one field with another. In the following
example the `item` field substitutes for the `_id` field.

Create a sample collection called `fruits` contains the following
documents:

```javascript
db.fruits.insertMany( [
   { _id: 1, item: "tangerine", type: "citrus" },
   { _id: 2, item: "lemon", type: "citrus" },
   { _id: 3, item: "grapefruit", type: "citrus" }
] )
```

The following aggregration operation uses `$set` to replace the
`_id` field of each document with the value of the `item` field,
and replaces the `item` field with a string `"fruit"`.

```javascript
db.fruits.aggregate( [
  { $set: { _id: "$item", item: "fruit" } }
] )
```

The operation returns the following:

```javascript
[
   { _id: "tangerine", item: "fruit", type: "citrus" },
   { _id: "lemon", item: "fruit", type: "citrus" },
   { _id: "grapefruit", item: "fruit", type: "citrus" }
]
```

### Add Element to an Array

Create a sample `scores` collection with the following:

```javascript
db.scores.insertMany( [
   { _id: 1, student: "Maya", homework: [ 10, 5, 10 ], quiz: [ 10, 8 ], extraCredit: 0 },
   { _id: 2, student: "Ryan", homework: [ 5, 6, 5 ], quiz: [ 8, 8 ], extraCredit: 8 }
] )
```

You can use `$set` with a `$concatArrays`
expression to add an element to an existing array field. For example,
the following operation uses `$set` to replace the
`homework` field with a new array whose elements are the current
`homework` array concatenated with another array containing a new
score `[ 7 ]`.

```javascript
db.scores.aggregate( [
   { $match: { _id: 1 } },
   { $set: { homework: { $concatArrays: [ "$homework", [ 7 ] ] } } }
] )
```

The operation returns the following:

```javascript
[ { _id: 1, student: "Maya", homework: [ 10, 5, 10, 7 ], quiz: [ 10, 8 ], extraCredit: 0 } ]
```

### Creating a New Field with Existing Fields

Create a sample `scores` collection with the following:

```javascript
db.scores.insertMany( [
   { _id: 1, student: "Maya", homework: [ 10, 5, 10 ], quiz: [ 10, 8 ], extraCredit: 0 },
   { _id: 2, student: "Ryan", homework: [ 5, 6, 5 ], quiz: [ 8, 8 ], extraCredit: 8 }
] )
```

The following aggregation operation adds a new field `quizAverage`
to each document that contains the average of the `quiz` array.

```javascript
db.scores.aggregate( [
   {
      $set: {
         quizAverage: { $avg: "$quiz" }
      }
   }
] )
```

The operation returns the following documents:

```javascript
[
   {
      _id: 1,
      student: 'Maya',
      homework: [ 10, 5, 10 ],
      quiz: [ 10, 8 ],
      extraCredit: 0,
      quizAverage: 9
   },
   {
      _id: 2,
      student: 'Ryan',
      homework: [ 5, 6, 5 ],
      quiz: [ 8, 8 ],
      extraCredit: 8,
      quizAverage: 8
   }
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

To use the MongoDB {+csharp-driver-short+} to add a `$set` stage to an aggregation
pipeline, call the [Set()](https://mongodb.github.io/mongo-csharp-driver/3.3.0/api/MongoDB.Driver/MongoDB.Driver.PipelineStageDefinitionBuilder.Set.html) method on a `PipelineDefinition` object.

The following example creates a pipeline stage that sets the value of the `LastUpdated` field in each `Movie`
document to the value of `DateTime.Now`:

```csharp
var pipeline = new EmptyPipelineDefinition<Movie>()
    .Set(Builders<Movie>.SetFields.Set(m => m.LastUpdated, DateTime.Now));
```
