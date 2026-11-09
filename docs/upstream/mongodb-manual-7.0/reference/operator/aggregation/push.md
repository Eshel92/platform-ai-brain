<!-- Converted from reference/operator/aggregation/push.txt (reStructuredText). Includes are inlined. -->

# $push (accumulator operator)

## Definition

**`$push`**

Returns an array of all values that result from applying an
expression to each document in a
group.

The `$push` accumulator is available in these stages:

- `$bucket`
- `$bucketAuto`
- `$group`

**Note:** Disambiguation

This page describes `$push` when used as an **accumulator**.
Accumulators return an aggregated value across a group of input
documents.

You can also use `$push` in these other contexts:

- `$push (window function)`, which is used in the
  `$setWindowFields` stage to return an array of all
  values from documents in a particular window.
- `$push (update operator)`, which appends a value
  to an array field in a document.

## Syntax

```none
{ $push: <expression> }
```

For more information on expressions, see aggregation-expressions.

## Behavior

When you use `$push` as an accumulator, the order of the documents
coming into the pipeline determines the order of the documents in the
output array. To guarantee a defined order, place a `$sort` stage
before the `$group` stage.

## Limitations

The `$push` accumulator cannot write temporary files to disk. The
`internalQueryMaxPushBytes` server parameter controls the `$push` memory
limit and if the accumulated array exceeds that limit, MongoDB returns an error
even when allowDiskUse is `true`. By
default, the parameter is 104857600 bytes (100 megabytes). You can raise the
limit at runtime with the `setParameter` command, up to a maximum of
2147483647 bytes.

For more information about aggregation memory restrictions, see
agg-pipeline-limits.

## Example

The examples on this page use data from the sample_mflix dataset. For details on how to load this dataset into your self-managed
MongoDB deployment, see Load the Sample Dataset.
If you made any modifications to the sample databases, you may need to drop and
recreate the databases to run the examples on this page. 

The following operation groups movies by director and uses the `$push`
accumulator to collect the primary genre of each film directed by that
director.

```javascript
```

Output:

```javascript
```

The preceding pipeline:

- Uses `$match` to filter to movies from 2010-2015 that
  have genre and director information.
- Uses `$unwind` to create a separate document for each
  director in the `directors` array.
- Groups the resulting documents by director and uses `$push` to
  collect the primary genre of each film.
- Sorts the results by director name in alphabetical order.
- Limits the output to five directors.

In the output, `A.R. Murugadoss` has `Action` listed twice because
they directed two films with `Action` as the primary genre. This
demonstrates that `$push` includes duplicate values, unlike
`$addToSet`, which returns an array of unique values.

## Learn More

- accumulators-ref
- `$addToSet`
- agg-pipeline-limits
