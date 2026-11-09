<!-- Converted from reference/mql/accumulators.txt (reStructuredText). Includes are inlined. -->

# Accumulators

Accumulators calculate aggregated values like sums, maxima, and minima
across a variable number of input values.

You can use accumulators in the aggregation pipeline stages that perform
grouping operations:

- `$bucket`

- `$bucketAuto`

- `$group`

The following table lists the accumulator operators available in
MongoDB:

* - Name
  - Description

* - `$accumulator`

  - Returns the result of a user-defined accumulator function.

* - `$addToSet`

  - Returns an array of *unique* expression values for each group.
    Order of the array elements is undefined.

* - `$avg`

  - Returns an average of numerical values.

* - `$bottom`

  - .. include:: /includes/accumulators/bottom-definition.rst

* - `$bottomN`

  - Returns an aggregation of the bottom `n` fields within a group,
    according to the specified sort order.

* - `$count`

  - Returns the number of documents in a group.

    Distinct from the `$count` pipeline stage.

* - `$first`

  - Returns the result of an expression for the first document in a group.

* - `$firstN`

  - Returns an aggregation of the first `n` elements within a group.
    Only meaningful when documents are in a defined order.
    Distinct from the `$firstN` array operator.

* - `$last`

  - Returns the result of an expression for the last document in a group.

* - `$lastN`

  - Returns the result of evaluating a specified expression over
    the last n elements in a group.

* - `$max`

  - Returns the highest expression value for each group.

* - `$maxN`

  - Returns an aggregation of the `n` maximum valued elements in
    a group.
    Distinct from the `$maxN` array operator.

* - `$median`
  - .. include:: /includes/aggregation/fact-return-median-accumulator.rst

    **New in version:** 7.0

* - `$mergeObjects`

  - Returns a document created by combining the input documents
    for each group.

* - `$min`

  - Returns the lowest expression value for each group.

* - `$minN`

  - Returns an aggregation of the `n` minimum valued elements
    in a group.
    Distinct from the `$minN` array operator.

* - `$percentile`
  - .. include:: /includes/aggregation/fact-return-percentile.rst

    **New in version:** 7.0

* - `$push`

  - Returns an array of expression values for documents in each
    group.

* - `$stdDevPop`

  - Returns the population standard deviation of values from
    documents in a group.

* - `$stdDevSamp`

  - Returns the sample standard deviation of values from documents
    in a group.

* - `$sum`

  - Returns a sum of numerical values. Ignores non-numeric values.

* - `$top`

  - Returns the top element within a group according to the
    specified sort order.

* - `$topN`

  - Returns an aggregation of the top `n` fields within a group,
    according to the specified sort order.
