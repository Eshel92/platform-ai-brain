<!-- Converted from core/aggregation-pipeline-sharded-collections.txt (reStructuredText). Includes are inlined. -->

# Aggregation Pipeline and Sharded Collections

The aggregation pipeline supports operations on sharded collections. This section describes behaviors
specific to the aggregation pipeline and
sharded collections.

## Behavior

If the pipeline starts with an exact `$match` on a
shard key, and the pipeline does not contain `$out` or
`$lookup` stages, the entire pipeline runs on the matching
shard only.

When aggregation operations run on multiple shards, the results are 
routed to the `mongos` to be merged, except in the
following cases:

- If the pipeline includes the `$out` or
  `$lookup` stages, the merge runs on the
  primary shard.

- If the pipeline includes a sorting or grouping stage, and the
  allowDiskUse setting is enabled,
  the merge runs on a randomly-selected shard.

## Optimization

When splitting the aggregation pipeline into two parts, the pipeline is
split to ensure that the shards perform as many stages as possible with
consideration for optimization.

To see how the pipeline was split, include the `explain` option in the
`db.collection.aggregate()` method.

Optimizations are subject to change between releases.
