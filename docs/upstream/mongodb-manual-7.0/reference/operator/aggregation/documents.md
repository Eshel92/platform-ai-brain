<!-- Converted from reference/operator/aggregation/documents.txt (reStructuredText). Includes are inlined. -->

# $documents (aggregation stage)

## Definition

**`$documents`**

**New in version:** 6.0

Returns literal documents from input values.

## Syntax

The `$documents` stage has the following form:

```
{ $documents: <expression> }
```

## Limitations

- You can only use `$documents` in a database-level aggregation
  pipeline.

- You must use `$documents` as the first stage of an aggregation
  pipeline.

See below for usage examples.

## Behavior

`$documents` accepts any valid expression that resolves to an
array of objects. This includes:

- system variables, such as `$$NOW` or
  `$$SEARCH_META`
- `$let` expressions
- variables in scope from `$lookup` expressions

Expressions that do not resolve to a current document, like
`$myField` or `$$ROOT`, will result in an error.

## Examples

**shell:**

### Test a Pipeline Stage

Create testing and debugging data for a pipeline stage without creating
test collections.

```javascript
db.aggregate(
   [
      { $documents: [ { x: 10 }, { x: 2 }, { x: 5 } ] },
      { $bucketAuto: { groupBy: "$x", buckets: 4 } }
   ]
)
```

The aggregation expression does not
specify a collection. It uses the input data in the highlighted
`$documents` stage as input to the `$bucketAuto`
stage.

```javascript
[
  { _id: { min: 2, max: 5 }, count: 1 },
  { _id: { min: 5, max: 10 }, count: 1 },
  { _id: { min: 10, max: 10 }, count: 1 }
]
```

### Use a `$documents` Stage in a `$lookup` Stage

Correlate documents in a collection with other data using
`$documents` to modify `$lookup` output.

Create the `locations` collection.

```javascript
db.locations.insertMany(
   [
      { zip: 94301, name: "Palo Alto" },
      { zip: 10019, name: "New York" }
   ]
 )
```

Use `$documents` as a data source to transform the documents.

```javascript
db.locations.aggregate(
   [
      { $match: {} },
      { $lookup:
         {
            localField: "zip",
            foreignField: "zip_id",
            as: "city_state",
            pipeline:
              [
                 { $documents:
                    [
                       { zip_id: 94301, name: "Palo Alto, CA" },
                       { zip_id: 10019, name: "New York, NY" }
                    ]
                 }
              ]
         }
      }
   ]
 )
```

The output correlates the data in the `locations` collection with the
values in the `$documents` pipeline stage.

```javascript
[
   {
      _id: ObjectId("618949d60f7bfd5f5689490d"),
      zip: 94301,
      name: 'Palo Alto',
      city_state: [ { zip_id: 94301, name: 'Palo Alto, CA' } ]
   },
   {
      _id: ObjectId("618949d60f7bfd5f5689490e"),
      zip: 10019,
      name: 'New York',
      city_state: [ { zip_id: 10019, name: 'New York, NY' } ]
   }
]
```

- The `zip` field corresponds to the `zip_id` field
- The `as` parameter creates a new output field

**csharp:**

(Text shared from another MongoDB docs repo, not available offline: dbx/csharp/aggregation/rst-files/method-intro.rst)

```csharp
```

Output:

```json
```

**nodejs:**

To use the MongoDB Node.js driver to add a `$documents` stage to an aggregation
pipeline, use the `$documents` operator in a pipeline object.

The following example creates a pipeline stage that creates three documents. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [
  {
    $documents: [
      { "title": "The Shawshank Redemption" },
      { "title": "Back to the Future" },
      { "title": "Jurassic Park" }
    ]
  }
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

      

## Learn More

For details on subqueries using the `$lookup` syntax, see
lookup-syntax-concise-correlated-subquery.
