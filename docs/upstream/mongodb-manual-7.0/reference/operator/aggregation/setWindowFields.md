<!-- Converted from reference/operator/aggregation/setWindowFields.txt (reStructuredText). Includes are inlined. -->

# $setWindowFields (aggregation stage)

## Definition

**`$setWindowFields`**

**New in version:** 5.0

Performs operations on a specified span of documents in a collection,
known as a *window*, and returns the results based on the chosen
window operator.

For example, you can use the `$setWindowFields` stage to
output the:

- Difference in sales between two documents in a collection.

- Sales rankings.

- Cumulative sales totals.

- Analysis of complex time series information without exporting the
  data to an external database.

## Syntax

The `$setWindowFields` stage syntax:

```none
{
   $setWindowFields: {
      partitionBy: <expression>,
      sortBy: {
         <sort field 1>: <sort order>,
         <sort field 2>: <sort order>,
         ...,
         <sort field n>: <sort order>
      },
      output: {
         <output field 1>: {
            <window operator>: <window operator parameters>,
            window: {
               documents: [ <lower boundary>, <upper boundary> ],
               range: [ <lower boundary>, <upper boundary> ],
               unit: <time unit>
            }
         },
         <output field 2>: { ... },
         ...
         <output field n>: { ... }
      }
   }
}
```

The `$setWindowFields` stage takes a document with these
fields:

* - Field
  - Necessity
  - Description

* - partitionBy

  - Optional

  - .. _setWindowFields-partitionBy:

    Specifies an expression to group
    the documents. In the `$setWindowFields` stage, the
    group of documents is known as a *partition*. Default is one
    partition for the entire collection.

* - sortBy

  - Required for some operators (see
    setWindowFields-restrictions)

  - .. _setWindowFields-sortBy:

    Specifies the field(s) to sort the documents by in the partition.
    Uses the same syntax as the `$sort` stage. Default is
    no sorting.

* - output

  - Required

  - .. _setWindowFields-output:

    Specifies the field(s) to append to the documents in the output
    returned by the `$setWindowFields` stage. Each field is
    set to the result returned by the window operator.

    A field can contain dots to
    specify embedded document fields and array fields. The semantics
    for the embedded document dotted notation in the
    `$setWindowFields` stage are the same as the
    `$addFields` and `$set` stages. See
    embedded document $addFields example and embedded document $set example.

    - The `window operator` is the window operator name to use in the
      `$setWindowFields` stage.

    - The `window operator parameters` are the parameters to pass
      to the window operator.

* - window

  - Optional

  - .. _setWindowFields-window:

    Specifies the window boundaries and parameters. Window boundaries
    are inclusive. Default is an unbounded window, which includes all
    documents in the partition.

    Specify either a documents or
    range window.

* - documents

  - Optional

  - .. _setWindowFields-documents:

    A window where the lower and upper boundaries are specified
    relative to the position of the current document read from the
    collection.

    The window boundaries are specified using a two element array
    containing a lower and upper limit string or integer. Use:

    - The `"current"` string for the current document position in
      the output.

    - The `"unbounded"` string for the first or last document
      position in the partition.

    - An integer for a position relative to the current document. Use
      a negative integer for a position before the current
      document. Use a positive integer for a position after the
      current document. `0` is the current document position.

    See setWindowFields-documents-window-examples.

* - range

  - Optional

  - .. _setWindowFields-range:

    A window where the lower and upper boundaries are defined using
    a range of values based on the sortBy field in the current document.

    The window boundaries are specified using a two element array
    containing a lower and upper limit string or number. Use:

    - The `"current"` string for the current document position in
      the output.

    - The `"unbounded"` string for the first or last document
      position in the partition.

    - A number to add to the value of the sortBy field for the current document. A
      document is in the window if the sortBy field value is inclusively within the
      lower and upper boundaries.

    See setWindowFields-range-window-example.

* - unit

  - Optional

  - .. _setWindowFields-unit:

    Specifies the units for time range
    window boundaries. Can be set to one of these strings:

    - `"year"`

    - `"quarter"`

    - `"month"`

    - `"week"`

    - `"day"`

    - `"hour"`

    - `"minute"`

    - `"second"`

    - `"millisecond"`

    If omitted, default numeric range
    window boundaries are used.

    See setWindowFields-time-range-window-examples.

**See also:**

setWindowFields-examples

## Behavior

The `$setWindowFields` stage appends new fields to existing
documents. You can include one or more `$setWindowFields`
stages in an aggregation operation.

Starting in MongoDB 5.3, you can use the `$setWindowFields`
stage with transactions and the
`"snapshot"` read concern.

The `$setWindowFields` stage doesn't guarantee the order of the
returned documents.

## Window Operators

These operators can be used with the `$setWindowFields` stage:

- Accumulator operators: `$addToSet`, `$avg`, 
  `$bottom`, `$bottomN`, `$count`, 
  `$covariancePop`, `$covarianceSamp`, 
  `$derivative`, `$expMovingAvg`, `$firstN`, 
  `$integral`, `$lastN`, `$max`, `$maxN`,
  `$median`, `$min`, `$minN`, `$percentile`,
  `$push`, `$stdDevSamp`, `$stdDevPop`,
  `$sum`, `$top`, `$topN`.

- Gap filling operators: `$linearFill` and `$locf`.

- Order operators: `$first`, `$last`, and `$shift`.

- Rank operators: `$denseRank`, `$documentNumber`, and
  `$rank`.

## Restrictions

Restrictions for the `$setWindowFields` stage:

- Before MongoDB 5.3, the `$setWindowFields`
  stage cannot be used:

  - Within transactions.
  - With `"snapshot"` read concern.

- sortBy is required for:

  - Rank and order window operators.

  - Bounded windows (either a documents window or a range window).

  - `$linearFill` operator.

- Range windows require all sortBy values to be numbers.

- Time range windows require all
  sortBy values to be dates.

- Range and time range windows can only contain one sortBy field and the sort must be ascending.

- You cannot specify both a documents
  window and a range window.

- These operators use an implicit window and return an error if you
  specify a window option:

  - Rank operators.

  - `$shift` operator.

- For range windows, only numbers in
  the specified range are included in the window. Missing, undefined,
  and `null` values are excluded.

- For time range windows:

  - Only date and time types are included in the window.

  - Numeric boundary values must be integers. For example, you can use 2
    hours as a boundary but you cannot use 1.5 hours.

- For empty windows or windows with incompatible values (for example,
  using `$sum` on strings), the returned value depends on the
  operator:

  - For `$count` and `$sum`, the returned value is `0`.

  - For `$addToSet` and `$push`, the returned value is an
    empty array.

  - For all other operators, the returned value is `null`.

## Examples

**shell:**

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Documents Window Examples

#### Use Documents Window to Obtain Cumulative Runtime for Each Rating

This example uses a documents
window in `$setWindowFields` to output the cumulative
`runtime` for each `rated` value. In the example output, the
`cumulativeRuntimeForRating` field shows the cumulative
`runtime` for each rating.

```javascript
```

Output:

```javascript
```

In the example:

- `partitionBy: "$rated"` partitions the documents in the collection by
  `rated`. The partitions are `G`, `PG`, `PG-13`, and `R`.

- `sortBy: { released: 1 }` sorts the documents in each partition by
  `released` in ascending order (`1`), so the earliest
  `released` date is first.

- `output`:

  - Sets the `cumulativeRuntimeForRating` field to the
    cumulative `runtime` for each `rated` value, which
    increases by successive additions to the previous value in
    the partition.

  - Calculates the cumulative `runtime` using the `$sum`
    operator run in a documents
    window.

    The window contains documents
    between an `unbounded` lower limit and the `current`
    document. This means `$sum` returns the cumulative
    `runtime` for the documents between the beginning of the
    partition and the current document.

#### Use Documents Window to Obtain Cumulative Runtime for Each Year

This example uses a documents
window in `$setWindowFields` to output the cumulative
`runtime` for each `$year` in `released`. In the
example output, the `cumulativeRuntimeForYear` field shows the
cumulative `runtime` for each year.

```javascript
```

Output:

```javascript
```

In the example:

- `partitionBy: { $year: "$released" }` partitions the documents in the collection
  by `$year` in `released`. There are partitions
  for `1993`, `1994`, and `1995`.

- `sortBy: { released: 1 }` sorts the documents in each partition by
  `released` in ascending order (`1`), so the earliest
  `released` date is first.

- `output`:

  - Sets the `cumulativeRuntimeForYear` field to the cumulative
    `runtime` for each year, which increases by successive
    additions to the previous value in the partition.

  - Calculates the cumulative `runtime` using the `$sum`
    operator run in a documents
    window.

    The window contains documents
    between an `unbounded` lower limit and the `current`
    document. This means `$sum` returns the cumulative
    `runtime` for the documents between the beginning of the
    partition and the current document.

#### Use Documents Window to Obtain Moving Average Runtime for Each Year

This example uses a documents
window in `$setWindowFields` to output the moving
average `runtime`. In the example output, the `averageRuntime`
field shows the moving average `runtime`.

```javascript
```

Output:

```javascript
```

In the example:

- `partitionBy: { $year: "$released" }` partitions the documents in the collection
  by `$year` in `released`. There are partitions
  for `1993`, `1994`, and `1995`.

- `sortBy: { released: 1 }` sorts the documents in each partition by
  `released` in ascending order (`1`), so the earliest
  `released` date is first.

- `output`:

  - Sets the `averageRuntime` field to the moving average
    `runtime` for each year.

  - Calculates the moving average `runtime` using the
    `$avg` operator run in a documents window.

    The window contains documents
    between `-1` and `0`. This means `$avg` returns the
    moving average `runtime` between the document before the
    current document (`-1`) and the current document (`0`) in
    the partition.

#### Use Documents Window to Obtain Cumulative and Maximum Runtime for Each Year

This example uses a documents
window in `$setWindowFields` to output the cumulative
and maximum `runtime` values for each `$year` in
`released`. In the example output, the
`cumulativeRuntimeForYear` field shows the cumulative
`runtime` and the `maximumRuntimeForYear` field shows the
maximum `runtime`.

```javascript
```

Output:

```javascript
```

In the example:

- `partitionBy: { $year: "$released" }` partitions the documents in the collection
  by `$year` in `released`. There are partitions
  for `1993`, `1994`, and `1995`.

- `sortBy: { released: 1 }` sorts the documents in each partition by
  `released` in ascending order (`1`), so the earliest
  `released` date is first.

- `output`:

  - Sets the `cumulativeRuntimeForYear` field to the cumulative
    `runtime` for each year.

  - Calculates the cumulative `runtime` using the `$sum`
    operator run in a documents
    window.

    The window contains documents
    between an `unbounded` lower limit and the `current`
    document. This means `$sum` returns the cumulative
    `runtime` for the documents between the beginning of the
    partition and the current document.

  - Sets the `maximumRuntimeForYear` field to the maximum
    `runtime` for each year.

  - Calculates the maximum `runtime` of all the documents using
    the `$max` operator run in a documents window.

    The window contains documents
    between an `unbounded` lower and `upper` limit. This means
    `$max` returns the maximum `runtime` for the
    documents in the partition.

### Range Window Example

This example uses a range window in
`$setWindowFields` to return the sum of the `runtime`
values of movies released within plus or minus 10 minutes of the
current document's `runtime` value. In the example output, the
`runtimeFromSimilarMovies` field shows the sum of the
`runtime` values for documents in the window.

```javascript
```

Output:

```javascript
```

In the example:

- `partitionBy: "$rated"` partitions the documents in the collection
  by `rated`. The partitions are `G`, `PG`, `PG-13`, and
  `R`.

- `sortBy: { runtime: 1 }` sorts the documents in each partition by
  `runtime` in ascending order (`1`), so the shortest
  `runtime` is first.

- `output` sets the `runtimeFromSimilarMovies` field to the
  sum of the `runtime` values from the documents in a
  range window.

  - The window contains documents
    between a lower limit of `-10` and an upper limit of `10`.
    The range is inclusive.

  - `$sum` returns the sum of `runtime` values contained
    in a range of plus or minus 10 minutes of the current
    document's `runtime` value.

### Time Range Window Examples

#### Use a Time Range Window with a Positive Upper Bound

The following example uses a
window with a positive upper bound
time range unit in
`$setWindowFields`. The pipeline outputs an array of
`released` values for each `rated` value that match the
specified time range. In the example output, the
`recentReleases` field shows the array of `released` values.

```javascript
```

Output:

```javascript
```

In the example:

- `partitionBy: "$rated"` partitions the documents in the collection by
  `rated`. The partitions are `G`, `PG`, `PG-13`, and `R`.

- `sortBy: { released: 1 }` sorts the documents in each partition by
  `released` in ascending order (`1`), so the earliest
  `released` date is first.

- `output`:

  - Sets the `recentReleases` field to an array of `released`
    values for the documents in each `rated` partition. The array
    elements are expanded with additions to the previous elements in
    the array.

  - Uses `$push` to return an array of `released`
    values from the documents in a range
    window.

- The window contains documents
  between an `unbounded` lower limit and an upper limit set to
  `10` (10 months after the current document's `released`
  value) using a time range unit.

- `$push` returns the array of `released` values
  for the documents between the beginning of the partition and the
  documents with `released` values inclusively in a range of the
  current document's `released` value plus `10` months.

#### Use a Time Range Window with a Negative Upper Bound

The following example uses a
window with a negative upper bound
time range unit in
`$setWindowFields`. The pipeline outputs an array of
`released` values for each `rated` value that match the
specified time range. In the example output, the
`recentReleases` field shows the array of `released` values.

```javascript
```

Output:

```javascript
```

In the example:

- `partitionBy: "$rated"` partitions the documents in the collection by
  `rated`. The partitions are `G`, `PG`, `PG-13`, and `R`.

- `sortBy: { released: 1 }` sorts the documents in each partition by
  `released` in ascending order (`1`), so the earliest
  `released` date is first.

- `output`:

  - Sets the `recentReleases` field to an array of `released`
    values for the documents in each `rated` partition. The array
    elements are expanded with additions to the previous elements in
    the array.

  - Uses `$push` to return an array of `released`
    values from the documents in a range
    window.

- The window contains documents
  between an `unbounded` lower limit and an upper limit set to
  `-10` (10 months before the current document's `released`
  value) using a time range unit.

- `$push` returns the array of `released` values
  for the documents between the beginning of the partition and the
  documents with `released` values inclusively in a range of the
  current document's `released` value minus `10` months.

### Comparison with Previous Values Example

The following example uses `$setWindowFields` with the
`$shift` operator and the `$set` stage to compare
fields in a collection. In the example output, the
`runtimeComparison` field shows the comparison result.

```javascript
```

Output:

```javascript
```

In the example:

- `partitionBy: "$rated"` partitions the documents in the collection
  by `rated` so each rating's calculations are kept separate.

- `sortBy: { released: 1 }` sorts the documents in each partition by
  `released` in ascending order (`1`).

- `output.previousRuntime` uses the `$shift` operator to
  capture the `runtime` from the immediately preceding movie
  within the same rating.

- `$set` adds a new field called
  `runtimeComparison`, and sets that field's value to
  `longer`, `shorter`, or `same` based on the comparison to
  `previousRuntime`.

**csharp:**

The following `WeatherMeasurement` class represents documents in a
collection of weather measurements:

```csharp
[BsonIgnoreExtraElements]
public class WeatherMeasurement
{
    [BsonId]
    public ObjectId Id { get; set; }
    [BsonElement("localityId")]
    public string LocalityId { get; set; } = null!;
    [BsonElement("measurementDateTime")]
    public DateTime MeasurementDateTime { get; set; }
    [BsonElement("rainfall")]
    public float Rainfall { get; set; }
    [BsonElement("temperature")]
    public float Temperature { get; set; }
}
```

(Text shared from another MongoDB docs repo, not available offline: dbx/csharp/aggregation/rst-files/method-intro.rst)

```csharp
```

Output:

```json
```

**nodejs:**

The Node.js examples on this page use the `sample_weatherdata.data` collection
from the Atlas sample datasets. To learn how to create a
free MongoDB Atlas cluster and load the sample datasets, see `Get
Started` in the MongoDB Node.js driver documentation.

To use the MongoDB Node.js driver to add a `$setWindowFields` stage to an aggregation
pipeline, use the `$setWindowFields` operator in a pipeline object.

The following example creates a pipeline stage that calculates the average `airTemperature.value` and the total
`waveMeasurement.waves.height` for each unique value of
`callLetters` over the past month. The
example then runs the aggregation pipeline:

```javascript
const pipeline = [
  {
    $setWindowFields: {
      partitionBy: "$callLetters",
      sortBy: { ts: 1 },
      output: {
        temperatureAvg: {
          $avg: "$airTemperature.value",
          window: {
            range: [-1, "current"],
            unit: "month"
          }
        },
        totalWaveHeight: {
          $sum: "$waveMeasurement.waves.height",
          window: {
            range: [-1, "current"],
            unit: "month"
          }
        }
      }
    }
  },
];

const cursor = collection.aggregate(pipeline);
return cursor;
```

**See also:**

For an additional example about IOT (Internet of Things)
Power Consumption, see the [Practical MongoDB Aggregations](https://www.practical-mongodb-aggregations.com/examples/time-series/iot-power-consumption.html)
e-book.
