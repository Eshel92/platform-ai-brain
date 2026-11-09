<!-- Converted from reference/operator/aggregation/project.txt (reStructuredText). Includes are inlined. -->

# $project (aggregation stage)

## Definition

**`$project`**

Passes along the documents with the requested fields to the
next stage in the pipeline. The specified fields can be existing
fields from the input documents or newly computed fields.

## Compatibility

You can use `$project` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas): The fully
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
| `<field>: <0 or false>` | Specifies the exclusion of a field. To exclude a field conditionally, use the `REMOVE` variable instead. For details, see remove-var. If you specify the exclusion of a field other than `_id`, you **cannot** employ any other `$project` specification forms. This restriction does not apply to conditionally exclusion of a field using the `REMOVE` variable. To exclude fields, you can also use the `$unset` stage. |

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
unlikely to improve performance, because the database performs this
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

## Examples

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

**shell:**

### Include Specific Fields in Output Documents

The following `$project` stage includes only the
`_id`, `title`, and `rated` fields:

```javascript
```

Output:

```javascript
```

### Suppress `_id` Field in the Output Documents

MongoDB includes the `_id` field by default. To exclude the
`_id` field from the `$project` stage, set the
`_id` field to `0` in the projection document.

The following `$project` stage excludes the `_id`
field but includes the `title` and `rated` fields:

```javascript
```

Output:

```javascript
```

### Exclude Fields from Output Documents

The following `$project` stage excludes the `rated`
field from the output:

```javascript
db.movies.aggregate( [
   { $match: { title: "The Great Train Robbery" } },
   { $project : { "rated": 0 } },
   { $limit: 1 }
] )
```

Alternatively, use the `$unset` stage to exclude
fields.

### Exclude Fields from Embedded Documents

The following `$project` stage excludes the `imdb.id` and `type`
fields from the output:

```javascript
```

Output:

```javascript
```

Alternatively, you can nest the exclusion specification in a
document:

```javascript
```

Output:

```javascript
```

Alternatively, use the `$unset` stage to exclude
fields.

### Conditionally Exclude Fields

You can use the variable `REMOVE` in aggregation expressions
to conditionally suppress a field.

The following `$project` stage uses the
`REMOVE` variable to exclude the `imdb.votes` field
if it equals `null` or is an empty string:

```javascript
```

Output:

```javascript
```

Because `imdb.votes` is an empty string for this document,
MongoDB excludes the field from the output.

**Tip:** Comparison with $addFields

You can use either the `$addFields` or `$project` stage to remove
document fields. The best approach depends on your pipeline and how much
of the original document you want to retain.

To see an example using `$$REMOVE` in an `$addFields` stage, see
addFields-remove-example.

### Include Specific Fields from Embedded Documents

Documents in the `movies` collection contain an embedded
`imdb` document with the `rating`, `votes`, and
`id` fields. To include only the `rating` field from the
`imdb` document, use dot notation:

```javascript
```

Output:

```javascript
```

Or, nest the inclusion specification in a document:

```javascript
```

Output:

```javascript
```

### Include Computed Fields

The following `$project` stage adds the
`leadActor` and `releaseYear` fields:

```javascript
```

Output:

```javascript
```

### Project New Array Fields

The following operation projects the `year` and
`runtime` fields as elements in a new `myArray` field:

```javascript
```

Output:

```javascript
```

If the array specification includes fields that are non-existent
in a document, the operation substitutes `null` as the value
for that field.

For example, given the same document as above, the following
operation projects the fields `year`, `runtime`, and a
non-existing field `$someField` as elements in a new field
`myArray`:

```javascript
```

Output:

```javascript
```

**csharp:**

(Text shared from another MongoDB docs repo, not available offline: dbx/csharp/aggregation/rst-files/sample-data-mflix-intro.rst)

To use the MongoDB {+csharp-driver-short+} to add a `$project` stage to an aggregation
pipeline, call the `Project()` method on a `PipelineDefinition` object and
pass a `ProjectionDefinitionBuilder<TDocument>` object. `TDocument`
is the class that represents the documents in your collection.

The following sections show the different ways that you can customize the output
documents of the `$project` stage.

### Include Specific Fields in Output Documents

To include specific fields when using the .NET/C# driver, call the
`Include()` method on the projection builder. You can chain `Include()` calls
to include multiple fields.

The following code example produces a document that includes only the `_id`,
`plot`, and `title` fields:

```csharp
```

Output:

```json
```

### Exclude Fields from Output Documents

To exclude a field from the result documents when using the .NET/C# driver, call the
`Exclude()` method on the projection builder. You can chain `Exclude()` calls
to exclude multiple fields.

The following code example produces a document that excludes the `Type` field:

```csharp
```

Output:

```json
```

By default, result documents always include the `_id` field. The following code
example produces a document that excludes the `_id` field but includes the `plot`
and `title` fields:

```csharp
```

Output:

```json
```

### Exclude Fields from Embedded Documents

To exclude a field in an embedded document when using the .NET/C# driver, call the
`Exclude()` method on the projection builder and pass the path to the corresponding
class property. You can chain `Exclude()` calls to exclude multiple fields.

The following code example produces a document that excludes the `imdb.id`
and `type` fields:

```csharp
```

Output:

```json
```

**Note:** Use Strings for Embedded ID Fields

To project an ID field in an embedded document, specify the field
name as a string, not a lambda expression.

### Conditionally Exclude Fields

You can use the variable `REMOVE` in aggregation expressions
to conditionally suppress a field:

```csharp
```

Output:

```json
```

**Note:** No Builder for Conditional Exclusion

The preceding example uses `BsonDocument` objects because the .NET/C# driver
doesn't provide a builder to conditionally exclude fields. Other MongoDB
language drivers might support this feature. See the
[MongoDB driver documentation](https://www.mongodb.com/docs/drivers/) for more
information.

### Include Computed Fields

To include computed fields in the result documents when using the .NET/C# driver,
call the `Expression()` method on the projection builder and pass an expression
that includes the computed fields. For added type safety, you can define a model
class for the result documents, like the following `ProjectedMovie` class:

```csharp
[BsonIgnoreExtraElements]
public class ProjectedMovie
{
    [BsonId]
    public ObjectId Id { get; set; }

    public string Title { get; set; } = null!;

    public string? LeadActor { get; set; }

    public List<string>? Crew { get; set; }
}
```

The following code example produces a document that includes multiple computed
fields:

```csharp
```

Output:

```json
```

### Project New Array Fields

To project new array fields in the result documents when using the .NET/C# driver,
call the `Expression()` method on the projection builder and pass an expression
that includes the new array fields. For added type safety, you can define a model
class for the result documents, like the following `ProjectedMovie` class:

```csharp
[BsonIgnoreExtraElements]
public class ProjectedMovie
{
    [BsonId]
    public ObjectId Id { get; set; }

    public string Title { get; set; } = null!;

    public string? LeadActor { get; set; }

    public List<string>? Crew { get; set; }
}
```

The following code example produces documents that include a new array field,
`crew`, which contains values from the `directors` and `writers` fields:

```csharp
```

Output:

```json
```

If the array specification includes fields that are non-existent in a
document, the pipeline substitutes `null` as the value for that
field. For example, the following code example projects the fields `directors`, `writers`,
and a non-existent field, `makeupArtists`, as elements in a new field named `crew`:

```csharp
```

Output:

```json
```

**Note:** Builders Class Prevents Missing Fields

The preceding example uses `BsonDocument` objects because the .NET/C# driver
raises a compile-time error if you try to use builders to add a missing field to
an array. Other MongoDB language drivers might support this feature. See the
[MongoDB driver documentation](https://www.mongodb.com/docs/drivers/) for more
information.

**nodejs:**

The Node.js examples on this page use the `sample_mflix` database from the
Atlas sample datasets. To learn how to create a free
MongoDB Atlas cluster and load the sample datasets, see `Get Started` in the MongoDB Node.js driver documentation.

To use the MongoDB Node.js driver to add a `$project` stage to an
aggregation pipeline, use the `$project` operator in a pipeline object.

The following sections show how to customize the output documents of the
`$project` stage.

### Include Specific Fields in Output Documents

To include specific fields, set the value of the field to `1` in the
`$project` stage.

The following example returns documents that include only the `_id`,
`plot`, and `title` fields:

```javascript
const pipeline = [
  {
    $project: {
      title: 1, 
      plot: 1
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

The output documents resemble the following example:

```javascript
{
  _id: new ObjectId('573a1390f29313caabcd42e8'),
  plot: 'A group of bandits stage a brazen train hold-up, only to find a
            determined posse hot on their heels.',
  title: 'The Great Train Robbery'
}
```

### Exclude Fields from Output Documents

To exclude specific fields, set the value of the field to `0` in the
`$project` stage.

The following example returns documents that exclude the `type` field:

```javascript
const pipeline = [
  {
    $project: {
      type: 0
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

By default, result documents always include the `_id` field. The
following example returns documents that exclude the `_id` field
but include the `plot` and `title` fields:

```javascript
const pipeline = [
  {
    $project: {
      _id: 0, 
      title: 1,
      plot: 1 
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

The output documents resemble the following example:

```javascript
{
  plot: 'A group of bandits stage a brazen train hold-up, only to find a
            determined posse hot on their heels.',
  title: 'The Great Train Robbery'
}
```

### Exclude Fields from Embedded Documents

To exclude a field in an embedded document, set value of the field path to
`0` in the `$project` stage.

**Note:** Use Strings for Embedded Fields

To project a field in an embedded document, specify the field
path as a string.

The following example returns documents that exclude the `imdb.id`
and `type` fields:

```javascript
const pipeline = [
  {
    $project: {
      "imdb.id": 0, 
      type: 0
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

The output documents resemble the following example:

```javascript
{
  plot: 'A group of bandits stage a brazen train hold-up, only to find a
            determined posse hot on their heels.',
  title: 'The Great Train Robbery',
  imdb: { rating: 7.4000000000000004, votes: 9847 }
}
```

### Conditionally Exclude Fields

To conditionally exclude a field, assign conditional logic that includes
the variable `REMOVE` to the field name.

```javascript
const pipeline = [
  {
    $project: {
      title: 1,
      "imdb.id": 1, 
      "imdb.rating": 1,
      "imdb.votes": {
        $cond: {
          if: { $eq: ["$imdb.votes", ""] },
          then: "$REMOVE",
          else: "$imdb.votes"
        }
      }
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

If a document contains the `imdb.votes` field, the pipeline returns
documents that resemble the following example output:

```javascript
{
  _id: new ObjectId('573a1390f29313caabcd42e8'),
  title: 'The Great Train Robbery',
  imdb: { rating : 7.4000000000000004, id: 439, votes: 9847 }
}
```

If a document doesn't contain the `imdb.votes` field, the pipeline
returns documents that resemble the following example output:

```javascript
{
  _id: new ObjectId('573a1390f29313caabcd42e8'), 
  title: 'This Is Spinal Tap',
  imdb: { rating: 8.0, id: 88258 }
}
```

### Include Computed Fields

To include computed fields in the result documents, assign an expression
to the field that stores the results.

The following example projects the `_id` and `title` fields into new
fields of the same name and computes the new field `leadActor`. The
example then returns documents that include these fields:

```javascript
const pipeline = [
  {
    $project: {
      _id: "$_id",
      title: "$title",
      leadActor: { $arrayElemAt: ["$cast", 0] }
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

The output documents resemble the following example:

```javascript
{
  _id: new ObjectId('573a1390f29313caabcd42e8'),
  title: 'The Great Train Robbery',
  leadActor: 'A.C. Abadie'
}
```

### Project New Array Fields

To project new array fields in the result documents, assign an expression
that computes the new array field to the field that stores the array.

The following example returns documents that include a new array
field, `crew`, which combines values from the `directors` and
`writers` fields:

```javascript
const pipeline = [
  {
    $project: {
      _id: "$_id",
      title: "$title",
      leadActor: { $arrayElemAt: ["$cast", 0] },
      crew: { $concatArrays: ["$directors", "$writers"] }
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

The output documents resemble the following example:

```javascript
{
  _id: new ObjectId('573a1395f29313caabce2297'),
  title: 'The Chalk Garden',
  leadActor: 'Deborah Kerr',
  crew: ['Ronald Neame', 'John Michael Hayes (screenplay)', 'Enid Bagnold (from the play by)']
}
```

If the array specification includes fields that aren't in a document, the
pipeline substitutes `null` as the value for that field. For example,
the following example projects the fields `directors`, `writers`,
and a non-existent field, `makeupArtists`, as elements in a new field
named `crew`:

```javascript
const pipeline = [
  {
    $project: {
      crew: ["$directors", "$writers", "$makeupArtists"]
    }
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

The output documents resemble the following example:

```javascript
{
  _id: new ObjectId('573a1399f29313caabced0d9'),
  crew: [['Bill Kroyer'], ['Jim Cox (screenplay)', 'Diana Young (original stories)'], null]
}
```

## Learn More

For more information and detailed explanations of common aggregation tasks, see
the aggregation-complete-examples.

To learn more about the methods on this page, see the following guides:

- `$eq`
- `$cond`
- `$arrayElemAt`
- `$concatArrays`
- `REMOVE`
