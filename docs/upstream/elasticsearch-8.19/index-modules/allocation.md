<!-- Converted from index-modules/allocation.asciidoc (AsciiDoc). Includes are inlined. -->

## Index Shard Allocation

This module provides per-index settings to control the allocation of shards to
nodes:

* Shard allocation filtering: Controlling which shards are allocated to which nodes.
* Delayed allocation: Delaying allocation of unassigned shards caused by a node leaving.
* Total shards per node: A hard limit on the number of shards from the same index per node.
* Data tier allocation: Controls the allocation of indices to data tiers.

(See `index-modules/allocation/filtering.md`)
(See `index-modules/allocation/delayed.md`)
(See `index-modules/allocation/prioritization.md`)
(See `index-modules/allocation/total_shards.md`)
(See `index-modules/allocation/data_tier_allocation.md`)
