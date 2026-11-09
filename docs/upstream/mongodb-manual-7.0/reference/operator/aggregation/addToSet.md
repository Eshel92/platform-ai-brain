<!-- Converted from reference/operator/aggregation/addToSet.txt (reStructuredText). Includes are inlined. -->

# $addToSet (accumulator operator)

## Definition

**`$addToSet`**

Returns an array of unique values for an expression
evaluated across documents in a group. The order of elements in the array
is unspecified.

`$addToSet` is available in these stages:
  
- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Disambiguation

This page describes `$addToSet` when used as an **accumulator**.
Accumulators return a single aggregated value like sum, maximum, or
minimum across a group of input documents.

You can also use `$addToSet` in these other contexts:

- `$addToSet (window function)`, which is used in the
  `$setWindowFields` stage to return an array of unique values
  from documents in a particular window.
- `$addToSet (update operator)`, which adds
  unique elements to an array field in a document.

## Syntax

```none
{ $addToSet: <expression> }
```

For more information on expressions, see aggregation-expressions.

## Behavior

If the value of the expression is an array, `$addToSet` appends the
whole array as a single element.

If the value of the expression is a document, MongoDB determines that
the document is a duplicate if another document in the array matches the
to-be-added document exactly. Specifically, the existing document has
the exact same fields and values in the exact same order.

`$addToSet` cannot write temporary files to disk. The
`internalQueryMaxAddToSetBytes` server parameter controls the `$addToSet`
memory limit and if the accumulated array exceeds that limit, MongoDB returns an
error even when allowDiskUse is `true`.
By default, the parameter is 104857600 bytes (100 megabytes). You can raise the
limit at runtime with the `setParameter` command.

For more information about aggregation memory restrictions, see
agg-pipeline-limits.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following operation groups movies by director and uses the
`$addToSet` accumulator to collect the unique genres each director has
worked in. To improve readability, the pipeline limits the results to the
first five directors in alphabetical order.

```javascript
db.movies.aggregate( [
   {
      $unwind: "$directors"
   },
   {
      $unwind: "$genres"
   },
   {
      $group: {
         _id: "$directors",
         genres: { $addToSet: "$genres" }
      }
   },
   {
      $sort: { _id: 1 }
   },
   {
      $limit: 5
   }
] )
```

This pipeline returns these results:

```javascript
[
  { _id: 'A. Dean Bell', genres: [ 'Crime', 'Drama' ] },
  { _id: 'A. Karunakaran', genres: [ 'Romance' ] },
  { _id: 'A. Vanichkin', genres: [ 'Animation', 'Fantasy' ] },
  { _id: 'A.J. Edwards', genres: [ 'Biography', 'Drama', 'History' ] },
  {
    _id: 'A.R. Murugadoss',
    genres: [ 'Drama', 'Sci-Fi', 'Thriller', 'Action', 'Mystery' ]
  }
]
```
