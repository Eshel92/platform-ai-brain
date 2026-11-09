<!-- Converted from reference/operator/aggregation/project.txt (reStructuredText). Includes are inlined. -->

# $project (aggregation)

## Definition

**`$project`**

Passes along the documents with the requested fields to the
next stage in the pipeline. The specified fields can be existing
fields from the input documents or newly computed fields.

## Compatibility

You can use `$project` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

The `$project` stage has the following prototype form:

```javascript
{ $project: { <specification(s)> } }
```

The `$project` takes a document that can specify the
inclusion of fields, the suppression of the `_id` field,
the addition of new fields, and the resetting of the values of existing
fields. Alternatively, you may specify the *exclusion*
of fields.

The `$project` specifications have the following forms:

| Form | Description |
|---|---|
| `<field>: <1 or true>` | Specifies the inclusion of a field. Non-zero integers are also treated as `true`. |
| `_id: <0 or false>` | Specifies the suppression of the `_id` field. To exclude a field conditionally, use the `REMOVE` variable instead. For details, see remove-var. |
| `<field>: <expression>` | Adds a new field or resets the value of an existing field. If the expression evaluates to `$$REMOVE`, the field is excluded in the output. For details, see remove-var. |
| `<field>: <0 or false>` | Specifies the exclusion of a field. To exclude a field conditionally, use the `REMOVE` variable instead. For details, see remove-var. If you specify the exclusion of a field other than `_id`, you **cannot** employ any other `$project` specification forms. This restriction does not apply to conditionally exclusion of a field using the `REMOVE` variable. See also the `$unset` stage to exclude fields. |

## Behavior

### Include Fields

- The `_id` field is, by default, included in the output documents.
  To include any other fields from the input documents in the output
  documents, you must explicitly specify the inclusion in
  `$project`.

- If you specify an inclusion of a field that does not exist in the
  document, `$project` ignores that field inclusion and
  does not add the field to the document.

### `_id` Field

By default, the `_id` field is included in the output documents.
To exclude the `_id` field from the output documents, you
must explicitly specify the suppression of the `_id` field in
`$project`.

### Exclude Fields

If you specify the exclusion of a field or fields, all other fields are
returned in the output documents.

```javascript
{ $project: { "<field1>": 0, "<field2>": 0, ... } } // Return all but the specified fields
```

If you specify the exclusion of a field other than `_id`, you cannot
employ any other `$project` specification forms: i.e. if you
exclude fields, you cannot also specify the inclusion of fields, reset
the value of existing fields, or add new fields. This restriction does
not apply to conditional exclusion of a field using the
`REMOVE` variable.

See also the `$unset` stage to exclude fields.

#### Exclude Fields Conditionally

You can use the variable `REMOVE` in aggregation expressions
to conditionally suppress a field. For an example, see
remove-example.

### Add New Fields or Reset Existing Fields

**Note:**

MongoDB also provides `$addFields` to add new fields to
the documents.

To add a new field or to reset the value of an existing field, specify
the field name and set its value to some expression. For more
information on expressions, see aggregation-expressions.

#### Literal Values

To set a field value directly to a numeric or boolean literal, as
opposed to setting the field to an expression that resolves to a
literal, use the `$literal` operator. Otherwise,
`$project` treats the numeric or boolean literal as a flag
for including or excluding the field.

#### Field Rename

By specifying a new field and setting its value to the field path of an
existing field, you can effectively rename a field.

#### New Array Fields

The `$project` stage supports using the square brackets `[]`
to directly create new array fields. If you specify array fields that do
not exist in a document, the operation substitutes `null` as the value
for that field. For an example, see
example-project-new-array-fields.

You cannot use an array index with the `$project` stage.
For more information, see example-project-array-indexes.

### Embedded Document Fields

When projecting or adding/resetting a field within an embedded
document, you can either use dot notation, as in

```javascript
"contact.address.country": <1 or 0 or expression>
```

Or you can nest the fields:

```javascript
contact: { address: { country: <1 or 0 or expression> } }
```

When nesting the fields, you *cannot* use dot notation inside the
embedded document to specify the field, e.g. ``contact: {
"address.country": <1 or 0 or expression> }`` is *invalid*.

#### Path Collision Errors in Embedded Fields

You cannot specify both an embedded document and a field within that
embedded document in the same projection.

The following `$project` stage fails with a `Path collision`
error because it attempts to project both the embedded `contact`
document and the `contact.address.country` field:

```javascript
{ $project: { contact: 1, "contact.address.country": 1 } }
```

The error occurs regardless of the order in which the parent document
and embedded field are specified. The following `$project`
fails with the same error:

```javascript
{ $project: { "contact.address.country": 1, contact: 1 } }
```

### `$project` Stage Placement

When you use a |$project| stage it should typically be the last stage in
your pipeline, used to specify which fields to return to the client.

Using a `$project` stage at the beginning or middle of a pipeline to
reduce the number of fields passed to subsequent pipeline stages is
unlikely to improve performance, as the database performs this
optimization automatically.

## Considerations

### Empty Specification

MongoDB returns an error if the `$project` stage is passed an
empty document.

For example, running the following pipeline produces an error:

```javascript
db.myCollection.aggregate( [ {
   $project: { }
} ] )
```

### Array Index

You cannot use an array index with the `$project` stage.
For more information, see example-project-array-indexes.

## Examples

**shell:**

### Include Specific Fields in Output Documents

Consider a `books` collection with the following document:

```javascript
{
  "_id" : 1,
  title: "abc123",
  isbn: "0001122223334",
  author: { last: "zzz", first: "aaa" },
  copies: 5
}
```

The following `$project` stage includes only the `_id`,
`title`, and the `author` fields in its output documents:

```javascript
db.books.aggregate( [ { $project : { title : 1 , author : 1 } } ] )
```

The operation results in the following document:

```javascript
{ "_id" : 1, "title" : "abc123", "author" : { "last" : "zzz", "first" : "aaa" } }
```

### Suppress `_id` Field in the Output Documents

The `_id` field is always included by default. To exclude the `_id`
field from the output documents of the `$project` stage,
specify the exclusion of the `_id` field by setting it to `0` in
the projection document.

Consider a `books` collection with the following document:

```javascript
{
  "_id" : 1,
  title: "abc123",
  isbn: "0001122223334",
  author: { last: "zzz", first: "aaa" },
  copies: 5
}
```

The following `$project` stage excludes the `_id` field but
includes the `title`, and the `author` fields in its output
documents:

```javascript
db.books.aggregate( [ { $project : { _id: 0, title : 1 , author : 1 } } ] )
```

The operation results in the following document:

```javascript
{ "title" : "abc123", "author" : { "last" : "zzz", "first" : "aaa" } }
```

### Exclude Fields from Output Documents

Consider a `books` collection with the following document:

```javascript
{
  "_id" : 1,
  title: "abc123",
  isbn: "0001122223334",
  author: { last: "zzz", first: "aaa" },
  copies: 5,
  lastModified: "2016-07-28"
}
```

The following `$project` stage excludes the `lastModified`
field from the output:

```javascript
db.books.aggregate( [ { $project : { "lastModified": 0 } } ] )
```

See also the `$unset` stage to exclude fields.

### Exclude Fields from Embedded Documents

Consider a `books` collection with the following document:

```javascript
{
  "_id" : 1,
  title: "abc123",
  isbn: "0001122223334",
  author: { last: "zzz", first: "aaa" },
  copies: 5,
  lastModified: "2016-07-28"
}
```

The following `$project` stage excludes the `author.first`
and `lastModified` fields from the output:

```javascript
db.books.aggregate( [ { $project : { "author.first" : 0, "lastModified" : 0 } } ] )
```

Alternatively, you can nest the exclusion specification in a document:

```javascript
db.bookmarks.aggregate( [ { $project: { "author": { "first": 0}, "lastModified" : 0 } } ] )
```

Both specifications result in the same output:

```javascript
{
   "_id" : 1,
   "title" : "abc123",
   "isbn" : "0001122223334",
   "author" : {
      "last" : "zzz"
   },
   "copies" : 5,
}
```

See also the `$unset` stage to exclude fields.

### Conditionally Exclude Fields

You can use the variable `REMOVE` in aggregation expressions
to conditionally suppress a field.

Consider a `books` collection with the following document:

```javascript
{
  "_id" : 1,
  title: "abc123",
  isbn: "0001122223334",
  author: { last: "zzz", first: "aaa" },
  copies: 5,
  lastModified: "2016-07-28"
}
{
  "_id" : 2,
  title: "Baked Goods",
  isbn: "9999999999999",
  author: { last: "xyz", first: "abc", middle: "" },
  copies: 2,
  lastModified: "2017-07-21"
}
{
  "_id" : 3,
  title: "Ice Cream Cakes",
  isbn: "8888888888888",
  author: { last: "xyz", first: "abc", middle: "mmm" },
  copies: 5,
  lastModified: "2017-07-22"
}
```

The following `$project` stage uses the `REMOVE`
variable to excludes the `author.middle` field only if it equals `""`:

```javascript
db.books.aggregate( [
   {
      $project: {
         title: 1,
         "author.first": 1,
         "author.last" : 1,
         "author.middle": {
            $cond: {
               if: { $eq: [ "", "$author.middle" ] },
               then: "$$REMOVE",
               else: "$author.middle"
            }
         }
      }
   }
] )
```

The aggregation operation results in the following output:

```javascript
{ "_id" : 1, "title" : "abc123", "author" : { "last" : "zzz", "first" : "aaa" } }
{ "_id" : 2, "title" : "Baked Goods", "author" : { "last" : "xyz", "first" : "abc" } }
{ "_id" : 3, "title" : "Ice Cream Cakes", "author" : { "last" : "xyz", "first" : "abc", "middle" : "mmm" } }
```

**Tip:** Comparison with $addFields

You can use either the `$addFields` or `$project` stage to remove
document fields. The best approach depends on your pipeline and how much
of the original document you want to retain.

To see an example using `$$REMOVE` in an `$addFields` stage, see
addFields-remove-example.

### Include Specific Fields from Embedded Documents

Consider a `bookmarks` collection with the following documents:

```javascript
{ _id: 1, user: "1234", stop: { title: "book1", author: "xyz", page: 32 } }
{ _id: 2, user: "7890", stop: [ { title: "book2", author: "abc", page: 5 }, { title: "book3", author: "ijk", page: 100 } ] }
```

To include only the `title` field in the embedded document in the
`stop` field, you can use  the dot notation:

```javascript
db.bookmarks.aggregate( [ { $project: { "stop.title": 1 } } ] )
```

Or, you can nest the inclusion specification in a document:

```javascript
db.bookmarks.aggregate( [ { $project: { stop: { title: 1 } } } ] )
```

Both specifications result in the following documents:

```javascript
{ "_id" : 1, "stop" : { "title" : "book1" } }
{ "_id" : 2, "stop" : [ { "title" : "book2" }, { "title" : "book3" } ] }
```

### Include Computed Fields

Consider a `books` collection with the following document:

```javascript
{
  "_id" : 1,
  title: "abc123",
  isbn: "0001122223334",
  author: { last: "zzz", first: "aaa" },
  copies: 5
}
```

The following `$project` stage adds the new fields
`isbn`, `lastName`, and `copiesSold`:

```javascript
db.books.aggregate(
   [
      {
         $project: {
            title: 1,
            isbn: {
               prefix: { $substr: [ "$isbn", 0, 3 ] },
               group: { $substr: [ "$isbn", 3, 2 ] },
               publisher: { $substr: [ "$isbn", 5, 4 ] },
               title: { $substr: [ "$isbn", 9, 3 ] },
               checkDigit: { $substr: [ "$isbn", 12, 1] }
            },
            lastName: "$author.last",
            copiesSold: "$copies"
         }
      }
   ]
)
```

The operation results in the following document:

```javascript
{
   "_id" : 1,
   "title" : "abc123",
   "isbn" : {
      "prefix" : "000",
      "group" : "11",
      "publisher" : "2222",
      "title" : "333",
      "checkDigit" : "4"
   },
   "lastName" : "zzz",
   "copiesSold" : 5
}
```

### Project New Array Fields

For example, if a collection includes the following document:

```javascript
{ "_id" : ObjectId("55ad167f320c6be244eb3b95"), "x" : 1, "y" : 1 }
```

The following operation projects the fields `x` and `y` as elements
in a new field `myArray`:

```javascript
db.collection.aggregate( [ { $project: { myArray: [ "$x", "$y" ] } } ] )
```

The operation returns the following document:

```javascript
{ "_id" : ObjectId("55ad167f320c6be244eb3b95"), "myArray" : [ 1, 1 ] }
```

If array specification includes fields that are non-existent in a
document, the operation substitutes `null` as the value for that
field.

For example, given the same document as above, the following operation
projects the fields `x`, `y`, and a non-existing field
`$someField` as elements in a new field `myArray`:

```javascript
db.collection.aggregate( [ { $project: { myArray: [ "$x", "$y", "$someField" ] } } ] )
```

The operation returns the following document:

```javascript
{ "_id" : ObjectId("55ad167f320c6be244eb3b95"), "myArray" : [ 1, 1, null ] }
```

### Array Indexes are Unsupported

You cannot use an array index with the `$project` stage. This
section shows an example.

Create the following `pizzas` collection:

```javascript
db.pizzas.insert( [
   { _id: 0, name: [ 'Pepperoni' ] },
] )
```

The following example returns the pizza:

```javascript
db.pizzas.aggregate( [
   { $project: { x: '$name', _id: 0 } },
] )
```

The pizza is returned in the example output:

```javascript
[ { x: [ 'Pepperoni' ] } ]
```

The following example uses an array index (`$name.0`) to attempt to
return the pizza:

```javascript
db.pizzas.aggregate( [
   { $project: { x: '$name.0', _id: 0 } },
] )
```

The pizza is not returned in the example output:

```javascript
[ { x: [] } ]
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

To use the MongoDB {+csharp-driver-short+} to add a `$project` stage to an aggregation
pipeline, call the [Project()](https://mongodb.github.io/mongo-csharp-driver/3.3.0/api/MongoDB.Driver/MongoDB.Driver.PipelineStageDefinitionBuilder.Project.html) method on a `PipelineDefinition` object.

The following example creates a pipeline stage that includes only the `Title` and `Plot` fields:

```csharp
var pipeline = new EmptyPipelineDefinition<Movie>()
    .Project(m => new { m.Title, m.Plot });
```

### Projecting Computed Fields

The following example creates a pipeline stage that projects the `Rated` field
into a new field called `Rating`, effectively renaming the field:

```csharp
var pipeline = new EmptyPipelineDefinition<Movie> ()
    .Project(
        Builders<Movie>
            .Projection
            .Expression(m => new { Rating = m.Rated, })
    );
```

**See also:**

- /tutorial/aggregation-zip-code-data-set
- /tutorial/aggregation-with-user-preference-data
