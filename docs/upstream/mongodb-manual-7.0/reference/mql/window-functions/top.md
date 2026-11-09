<!-- Converted from reference/mql/window-functions/top.txt (reStructuredText). Includes are inlined. -->

# $top (window function)

## Definition

**`$top`**

Returns the top element within a window according to the specified sort order.

**Note:** Disambiguation

This page describes `$top` when used as a **window function**.
You can also use the `$top (accumulator)`, which
returns the top element within a group according to the specified
sort order.

## Syntax

```none
{
   $setWindowFields: {
      ...
      output: {
         <field>: {
            $top: {
               sortBy: { <field1>: <sort order>, <field2>: <sort order> ... },
               output: <expression>
            }
         }
      }
   }
}
```

| Field | Necessity | Description |
|---|---|---|
| sortBy | Required | Defines the ranking order of elements within the window, with syntax similar to `$sort`. Does not affect the order of documents in pipeline output. |
| output | Required | Specifies the output for each element in the window. Can be any expression. |

## Behavior

The `$top` window function has the following behaviors for null and missing values:

- `$top` does not filter out null values.
- `$top` converts missing values to null.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

### Find the Highest-Rated Movie Per Year Over a Window

This example uses `$top` as a window function to identify
the highest-rated movie in the same year for each movie document.
The dataset is filtered to include only PG-rated Family movies
from 1980–1982.

```javascript
```

Output:

```javascript
```

In this example:

- The `$match` stage filters for PG-rated Family movies
  from 1980-1982 to produce a small, focused result set.
- `$setWindowFields` partitions the documents by `year`.
- The window spans from
  `unbounded` to `unbounded`, meaning `$top` considers all
  documents in the partition when determining the highest-rated
  movie.
- `$top` returns the highest-rated movie in each partition as an
  embedded document containing the `title` and `rating` fields.
- `$project` includes only the `title`, `year`,
  `rating`, and `highestRatedInYear` fields in the output.
- `$limit` limits the output to 10 documents.

This approach preserves all individual movie documents and includes
a reference to the top performer in each year.
