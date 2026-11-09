<!-- Converted from reference/operator/aggregation/replaceRoot.txt (reStructuredText). Includes are inlined. -->

# $replaceRoot (aggregation stage)

## Definition

**`$replaceRoot`**

Replaces the input document with the specified document. The
operation replaces all existing fields in the input document,
including the `_id` field. You can promote an existing
embedded document to the top level, or create a new document
for promotion (see
example).

**Note:**

You can also use the `$replaceWith` stage. The
`$replaceWith` stage peforms the same action as the
`$replaceRoot` stage, but the stages have different forms.

The `$replaceRoot` stage has the following form:

```javascript
{ $replaceRoot: { newRoot: <replacementDocument> } }
```

The replacement document can be any valid expression that resolves to a document. The stage
errors and fails if `<replacementDocument>` is not a document. For
more information on expressions, see aggregation-expressions.

## Behavior

If the `<replacementDocument>` is not a document,
`$replaceRoot` errors and fails.

If the `<replacementDocument>` resolves to a missing document (i.e.
the document does not exist), `$replaceRoot` errors and
fails. For example, create a collection with the following
documents:

```javascript
db.collection.insertMany([
   { "_id": 1, "name" : { "first" : "John", "last" : "Backus" } },
   { "_id": 2, "name" : { "first" : "John", "last" : "McCarthy" } },
   { "_id": 3, "name": { "first" : "Grace", "last" : "Hopper" } },
   { "_id": 4, "firstname": "Ole-Johan", "lastname" : "Dahl" },
])
```

Then the following `$replaceRoot` operation fails because one
of the documents does not have the `name` field:

```javascript
db.collection.aggregate([
   { $replaceRoot: { newRoot: "$name" } }
])
```

To avoid the error, you can use `$mergeObjects` to merge
the `name` document into some default document; for example:

```javascript
```

Output:

```javascript
```

Alternatively, you can skip the documents that are missing the `name` field by
including a `$match` stage to check for existence of the
document field before passing documents to the `$replaceRoot`
stage:

```javascript
```

Output:

```javascript
```

Or, you can use `$ifNull` expression to specify some other
document to be root; for example:

```javascript
```

Output:

```javascript
```

## Examples

**shell:**

### `$replaceRoot` with an Embedded Document Field

A collection named `people` contains the following documents:

```javascript
db.people.insertMany([
   { "_id" : 1, "name" : "Arlene", "age" : 34, "pets" : { "dogs" : 2, "cats" : 1 } },
   { "_id" : 2, "name" : "Sam", "age" : 41, "pets" : { "cats" : 1, "fish" : 3 } },
   { "_id" : 3, "name" : "Maria", "age" : 25 }
])
```

The following operation uses the `$replaceRoot` stage to
replace each input document with the result of a
`$mergeObjects` operation. The `$mergeObjects`
expression merges the specified default document with the `pets`
document.

```javascript
```

Output:

```javascript
```

### `$replaceRoot` with a Document Nested in an Array

A collection named `students` contains the following documents:

```javascript
db.students.insertMany([
   {
      "_id" : 1,
      "grades" : [
         { "test": 1, "grade" : 80, "mean" : 75, "std" : 6 },
         { "test": 2, "grade" : 85, "mean" : 90, "std" : 4 },
         { "test": 3, "grade" : 95, "mean" : 85, "std" : 6 }
      ]
   },
   {
      "_id" : 2,
      "grades" : [
         { "test": 1, "grade" : 90, "mean" : 75, "std" : 6 },
         { "test": 2, "grade" : 87, "mean" : 90, "std" : 3 },
         { "test": 3, "grade" : 91, "mean" : 85, "std" : 4 }
      ]
   }
])
```

The following operation promotes the embedded document(s) with the
`grade` field greater than or equal to `90` to the top level:

```javascript
```

Output:

```javascript
```

### `$replaceRoot` with a newly created document

You can also create new documents as part of the
`$replaceRoot` stage and use them to replace all the other fields.

A collection named `contacts` contains the following documents:

```javascript
db.contacts.insertMany([
   { "_id" : 1, "first_name" : "Gary", "last_name" : "Sheffield", "city" : "New York" },
   { "_id" : 2, "first_name" : "Nancy", "last_name" : "Walker", "city" : "Anaheim" },
   { "_id" : 3, "first_name" : "Peter", "last_name" : "Sumner", "city" : "Toledo" }
])
```

The following operation creates a new document out of the
`first_name` and `last_name` fields.

```javascript
```

Output:

```javascript
```

### `$replaceRoot` with a New Document Created from `$$ROOT` and a Default Document

A collection named `contacts` contains the following documents:

```javascript
db.contacts.insertMany( [
   { "_id" : 1, name: "Fred", email: "fred@example.net" },
   { "_id" : 2, name: "Frank N. Stine", cell: "012-345-9999" },
   { "_id" : 3, name: "Gren Dell", home: "987-654-3210", email: "beo@example.net" }
] )
```

The following operation uses `$replaceRoot` with
`$mergeObjects` to output current documents with default
values for missing fields:

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

The following `ImdbData` class models the embedded
`imdb` document:

```csharp
[BsonIgnoreExtraElements]
public class ImdbData
{
    [BsonElement("id")]
    public int? ImdbId { get; set; }
    [BsonElement("rating")]
    public double? Rating { get; set; }
    [BsonElement("votes")]
    public int? Votes { get; set; }
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

To use the MongoDB Node.js driver to add a `$replaceRoot` stage to an aggregation
pipeline, use the `$replaceRoot` operator in a pipeline object.

The following example creates a pipeline stage that replaces each input `movie` document with the document stored
in its `imdb` property. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [{ $replaceRoot: { newRoot: "$imdb" } }];

const cursor = collection.aggregate(pipeline);
return cursor;
```

## Learn More

To learn more about related pipeline stages, see the `$replaceRoot` guide.
