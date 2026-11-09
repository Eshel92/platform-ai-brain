<!-- Converted from reference/operator/aggregation/unwind.txt (reStructuredText). Includes are inlined. -->

# $unwind (aggregation)

## Definition

**`$unwind`**

Deconstructs an array field from the input documents to output a
document for *each* element. Each output document is the input
document with the value of the array field replaced by the element.

## Compatibility

You can use `$unwind` for deployments hosted in the following
environments:

- [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server): The fully
  managed service for MongoDB deployments in the cloud
- MongoDB Enterprise: The
  subscription-based, self-managed version of MongoDB
- MongoDB Community: The
  source-available, free-to-use, and self-managed version of MongoDB

## Syntax

You can pass a field path operand or a document operand to unwind an
array field.

### Field Path Operand

You can pass the array field path to `$unwind`. When using
this syntax, `$unwind` does not output a document if the field
value is null, missing, or an empty array.

```javascript
{ $unwind: <field path> }
```

When you specify the field path, prefix the
field name with a dollar sign `$` and enclose in quotes.

### Document Operand with Options

You can pass a document to `$unwind` to specify various
behavior options.

```javascript
{
  $unwind:
    {
      path: <field path>,
      includeArrayIndex: <string>,
      preserveNullAndEmptyArrays: <boolean>
    }
}
```

* - Field

  - Type

  - Description

* - path

  - string

  - .. _unwind-path:

    Field path to an array field. To specify a field path, prefix
    the field name with a dollar sign `$` and enclose in quotes.

* - includeArrayIndex

  - string

  - .. _unwind-includeArrayIndex:

    Optional. The name of a new field to hold the array index of the
    element. The name cannot start with a dollar sign `$`.

* - preserveNullAndEmptyArrays

  - boolean

  - .. _unwind-preserveNullAndEmptyArrays:

    Optional.

    - If `true`, if the `path` is null, missing, or an empty
      array, `$unwind` outputs the document.

    - If `false`, if `path` is null, missing, or an empty
      array, `$unwind` does not output a document.

    The default value is `false`.

## Behaviors

### Non-Array Field Path

* When the operand does not resolve to an array, but is not missing, `null`,
  or an empty array, `$unwind` treats the operand as a single element array.

* When the operand is `null`, missing, or an empty array `$unwind` follows
  the behavior set for the
  preserveNullAndEmptyArrays option.

### Missing Field

If you specify a path for a field that does not exist in an input
document or the field is an empty array, `$unwind`, by
default, ignores the input document and will not output documents for
that input document.

To output documents where the array field is missing, null or an
empty array, use the
preserveNullAndEmptyArrays
option.

## Examples

**shell:**

### Unwind Array

In `mongosh`, create a sample collection named
`inventory` with the following document:

```javascript
db.inventory.insertOne({ _id: 1, item: "ABC1", sizes: [ "S", "M", "L"] })
```

The following aggregation uses the `$unwind` stage to output
a document for each element in the `sizes` array:

```javascript
db.inventory.aggregate( [ { $unwind : "$sizes" } ] )
```

The operation returns the following results:

```javascript
{ _id: 1, item: "ABC1", sizes: "S" }
{ _id: 1, item: "ABC1", sizes: "M" }
{ _id: 1, item: "ABC1", sizes: "L" }
```

Each document is identical to the input document except for the value
of the `sizes` field which now holds a value from the original
`sizes` array.

### Missing or Non-array Values

Consider the `clothing` collection:

```javascript
db.clothing.insertMany([
  { _id: 1, item: "Shirt", sizes: [ "S", "M", "L"] },
  { _id: 2, item: "Shorts", sizes: [ ] },
  { _id: 3, item: "Hat", sizes: "M" },
  { _id: 4, item: "Gloves" },
  { _id: 5, item: "Scarf", sizes: null }
])
```

`$unwind` treats the `sizes` field as a single element
array if:

- the field is present,
- the value is not null, and
- the value is not an empty array.

Expand the `sizes` arrays with `$unwind`:

```javascript
db.clothing.aggregate( [ { $unwind: { path: "$sizes" } } ] )
```

The `$unwind` operation returns:

```javascript
{ _id: 1, item: 'Shirt', sizes: 'S' },
{ _id: 1, item: 'Shirt', sizes: 'M' },
{ _id: 1, item: 'Shirt', sizes: 'L' },
{ _id: 3, item: 'Hat', sizes: 'M' }
```

- In document `"_id": 1`, `sizes` is a populated array.
  `$unwind` returns a document for each element in the
  `sizes` field.
- In document `"_id": 3`, `sizes` resolves to a single element
  array.
- Documents `"_id": 2, "_id": 4`, and `"_id": 5` do not return
  anything because the `sizes` field cannot be reduced to a single
  element array.

**Note:**

The `{ path: <FIELD> }` syntax is optional. The following
`$unwind` operations are equivalent.

```javascript
db.clothing.aggregate( [ { $unwind: "$sizes" } ] )
db.clothing.aggregate( [ { $unwind: { path: "$sizes" } } ] )
```

### `preserveNullAndEmptyArrays` and `includeArrayIndex`

The ex-preservedNull and ex-includeArrayIndex examples
use the following collection:

```javascript
db.inventory2.insertMany([
   { _id: 1, item: "ABC", price: NumberDecimal("80"), sizes: [ "S", "M", "L"] },
   { _id: 2, item: "EFG", price: NumberDecimal("120"), sizes: [ ] },
   { _id: 3, item: "IJK", price: NumberDecimal("160"), sizes: "M" },
   { _id: 4, item: "LMN" , price: NumberDecimal("10") },
   { _id: 5, item: "XYZ", price: NumberDecimal("5.75"), sizes: null }
])
```

#### `preserveNullAndEmptyArrays`

The following `$unwind` operation uses the
preserveNullAndEmptyArrays
option to include documents whose `sizes` field is null, missing,
or an empty array.

```javascript
db.inventory2.aggregate( [
   { $unwind: { path: "$sizes", preserveNullAndEmptyArrays: true } }
] )
```

The output includes those documents where the `sizes` field is
null, missing, or an empty array:

```javascript
{ _id: 1, item: "ABC", price: NumberDecimal("80"), sizes: "S" }
{ _id: 1, item: "ABC", price: NumberDecimal("80"), sizes: "M" }
{ _id: 1, item: "ABC", price: NumberDecimal("80"), sizes: "L" }
{ _id: 2, item: "EFG", price: NumberDecimal("120") }
{ _id: 3, item: "IJK", price: NumberDecimal("160"), sizes: "M" }
{ _id: 4, item: "LMN", price: NumberDecimal("10") }
{ _id: 5, item: "XYZ", price: NumberDecimal("5.75"), sizes: null }
```

#### `includeArrayIndex`

The following `$unwind` operation uses the
includeArrayIndex option to include
the array index in the output.

```javascript
db.inventory2.aggregate( [
  {
    $unwind:
      {
        path: "$sizes",
        includeArrayIndex: "arrayIndex"
      }
   }])
```

The operation unwinds the `sizes` array and includes the array index
in the new `arrayIndex` field. If the `sizes` field does not
resolve to a populated array but is not missing, null, or an empty
array, the `arrayIndex` field is `null`.

```javascript
{ _id: 1, item: "ABC", price: NumberDecimal("80"), sizes: "S", arrayIndex: NumberLong(0) }
{ _id: 1, item: "ABC", price: NumberDecimal("80"), sizes: "M", arrayIndex: NumberLong(1) }
{ _id: 1, item: "ABC", price: NumberDecimal("80"), sizes: "L", arrayIndex: NumberLong(2) }
{ _id: 3, item: "IJK", price: NumberDecimal("160"), sizes: "M", arrayIndex: null }
```

### Group by Unwound Values

In `mongosh`, create a sample collection named
`inventory2` with the following documents:

```javascript
db.inventory2.insertMany([
  { _id: 1, item: "ABC", price: NumberDecimal("80"), sizes: [ "S", "M", "L"] },
  { _id: 2, item: "EFG", price: NumberDecimal("120"), sizes: [ ] },
  { _id: 3, item: "IJK", price: NumberDecimal("160"), sizes: "M" },
  { _id: 4, item: "LMN" , price: NumberDecimal("10") },
  { _id: 5, item: "XYZ", price: NumberDecimal("5.75"), sizes: null }
])
```

The following pipeline unwinds the `sizes` array and groups the
resulting documents by the unwound size values:

```javascript
db.inventory2.aggregate( [
   // First Stage
   {
     $unwind: { path: "$sizes", preserveNullAndEmptyArrays: true }
   },
   // Second Stage
   {
     $group:
       {
         _id: "$sizes",
         averagePrice: { $avg: "$price" }
       }
   },
   // Third Stage
   {
     $sort: { "averagePrice": -1 }
   }
] )
```

First Stage:
  The `$unwind` stage outputs a new document for each element
  in the `sizes` array. The stage uses the
  preserveNullAndEmptyArrays
  option to include in the output those documents where `sizes` field
  is missing, null or an empty array. This stage passes the following
  documents to the next stage:

  ```javascript
  { _id: 1, item: "ABC", price: NumberDecimal("80"), sizes: "S" }
  { _id: 1, item: "ABC", price: NumberDecimal("80"), sizes: "M" }
  { _id: 1, item: "ABC", price: NumberDecimal("80"), sizes: "L" }
  { _id: 2, item: "EFG", price: NumberDecimal("120") }
  { _id: 3, item: "IJK", price: NumberDecimal("160"), sizes: "M" }
  { _id: 4, item: "LMN", price: NumberDecimal("10") }
  { _id: 5, item: "XYZ", price: NumberDecimal("5.75"), sizes: null }
  ```

Second Stage:
  The `$group` stage groups the documents by `sizes`
  and calculates the average price of each size. This stage
  passes the following documents to the next stage:

  ```javascript
  { _id: "S", averagePrice: NumberDecimal("80") }
  { _id: "L", averagePrice: NumberDecimal("80") }
  { _id: "M", averagePrice: NumberDecimal("120") }
  { _id: null, averagePrice: NumberDecimal("45.25") }
  ```

Third Stage:
  The `$sort` stage sorts the documents by `averagePrice` in
  descending order. The operation returns the following result:

  ```javascript
  { _id" : "M", averagePrice: NumberDecimal("120") }
  { _id" : "L", averagePrice: NumberDecimal("80") }
  { _id" : "S", averagePrice: NumberDecimal("80") }
  { _id" : null, averagePrice: NumberDecimal("45.25") }
  ```

**See also:**

- `$group`
- `$sort`

### Unwind Embedded Arrays

In `mongosh`, create a sample collection named
`sales` with the following documents:

```javascript
db.sales.insertMany( [
  {
   _id: "1",
   items: [
     {
      name: "pens",
      tags: [ "writing", "office", "school", "stationary" ],
      price: NumberDecimal("12.00"),
      quantity: NumberInt("5")
     },
     {
      name: "envelopes",
      tags: [ "stationary", "office" ],
      price: NumberDecimal("19.95"),
      quantity: NumberInt("8")
     }
    ]
  },
  {
   _id: "2",
   items: [
     {
      name: "laptop",
      tags: [ "office", "electronics" ],
      price: NumberDecimal("800.00"),
      quantity: NumberInt("1")
     },
     {
      name: "notepad",
      tags: [ "stationary", "school" ],
      price: NumberDecimal("14.95"),
      quantity: NumberInt("3")
     }
    ]
  }
])
```

The following operation groups the items sold by their tags and
calculates the total sales amount per each tag.

```javascript
db.sales.aggregate([
  // First Stage
  { $unwind: "$items" },

  // Second Stage
  { $unwind: "$items.tags" },

  // Third Stage
  {
    $group:
      {
        _id: "$items.tags",
        totalSalesAmount:
          {
            $sum: { $multiply: [ "$items.price", "$items.quantity" ] }
          }
      }
  }
])
```

First Stage
  The first `$unwind` stage outputs a new document for
  each element in the `items` array:

  ```javascript
  { _id: "1", items: { name: "pens", tags: [ "writing", "office", "school", "stationary" ], price: NumberDecimal("12.00"), quantity: 5 } }
  { _id: "1", items: { name: "envelopes", tags: [ "stationary", "office" ], price: NumberDecimal("19.95"), quantity: 8 } }
  { _id: "2", items: { name: "laptop", tags: [ "office", "electronics" ], price: NumberDecimal("800.00"), quantity": 1 } }
  { _id: "2", items: { name: "notepad", tags: [ "stationary", "school" ], price: NumberDecimal("14.95"), quantity: 3 } }
  ```

Second Stage
  The second `$unwind` stage outputs a new document for each
  element in the `items.tags` arrays:

  ```javascript
  { _id: "1", items: { name: "pens", tags: "writing", price: NumberDecimal("12.00"), quantity: 5 } }
  { _id: "1", items: { name: "pens", tags: "office", price: NumberDecimal("12.00"), quantity: 5 } }
  { _id: "1", items: { name: "pens", tags: "school", price: NumberDecimal("12.00"), quantity: 5 } }
  { _id: "1", items: { name: "pens", tags: "stationary", price: NumberDecimal("12.00"), quantity: 5 } }
  { _id: "1", items: { name: "envelopes", tags: "stationary", price: NumberDecimal("19.95"), quantity: 8 } }
  { _id: "1", items: { name: "envelopes", tags: "office", "price" : NumberDecimal("19.95"), quantity: 8 } }
  { _id: "2", items: { name: "laptop", tags: "office", price: NumberDecimal("800.00"), quantity: 1 } }
  { _id: "2", items: { name: "laptop", tags: "electronics", price: NumberDecimal("800.00"), quantity: 1 } }
  { _id: "2", items: { name: "notepad", tags: "stationary", price: NumberDecimal("14.95"), quantity: 3 } }
  { _id: "2", items: { name: "notepad", "ags: "school", price: NumberDecimal("14.95"), quantity: 3 } }
  ```

Third Stage
  The `$group` stage groups the documents by the tag and
  calculates the total sales amount of items with each tag:

  ```javascript
  { _id: "writing", totalSalesAmount: NumberDecimal("60.00") }
  { _id: "stationary", totalSalesAmount: NumberDecimal("264.45") }
  { _id: "electronics", totalSalesAmount: NumberDecimal("800.00") }
  { _id: "school", totalSalesAmount: NumberDecimal("104.85") }
  { _id: "office", totalSalesAmount: NumberDecimal("1019.60") }
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

To use the MongoDB {+csharp-driver-short+} to add a `$unwind` stage to an aggregation
pipeline, call the [Unwind()](https://mongodb.github.io/mongo-csharp-driver/3.3.0/api/MongoDB.Driver/MongoDB.Driver.PipelineStageDefinitionBuilder.Unwind.html) method on a `PipelineDefinition` object.

The following example creates a pipeline stage that iterates over the `Genres` field in each input `Movie` document. For each
value in the `Genres` field, the stage creates a new `Movie` document and
populates its `Genres` field with the `Genres` value from the input document.

```csharp
var pipeline = new EmptyPipelineDefinition<Movie>()
    .Unwind(m => m.Genres);
```

You can use an [AggregateUnwindOptions](https://mongodb.github.io/mongo-csharp-driver/3.3.0/api/MongoDB.Driver/MongoDB.Driver.AggregateUnwindOptions.html)
object to customize the behavior of the `Unwind()` method.
The following example performs the same operation as the previous
example, but also includes the following options:

- `PreserveNullAndEmptyArrays` ensures that documents that contain an empty
  array in the `Genres` field are included in the output.
- The `IncludeArrayIndex` option adds a new field named `Index` to each output
  document. The value of this field is the array index of the `Genres` field's value
  in the input document's `Genres` array.

```csharp
var pipeline = new EmptyPipelineDefinition<Movie>()
    .Unwind(m => m.Genres,
        new AggregateUnwindOptions<Movie>()
        {
           PreserveNullAndEmptyArrays = true,
           IncludeArrayIndex = new ExpressionFieldDefinition<Movie, int>(
               m => m.Index) 
        });
```

**See also:**

- `$group`
- `$sum`
- `$multiply`

## Additional Resources

- /tutorial/aggregation-zip-code-data-set,
- /tutorial/aggregation-with-user-preference-data
