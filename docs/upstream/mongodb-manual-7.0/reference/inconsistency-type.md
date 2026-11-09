<!-- Converted from reference/inconsistency-type.txt (reStructuredText). Includes are inlined. -->

# Inconsistency Types

**New in version:** 7.0

The `checkMetadataConsistency` command performs a series of consistency 
checks on sharding metadata and indexes and returns an array of inconsistency
documents.

| Inconsistency Type | Description |
|---|---|
| `CollectionOptionsMismatch` | .. include:: /includes/inconsistency-type/CollectionOptionsMismatch |
| `CollectionUUIDMismatch` | .. include:: /includes/inconsistency-type/CollectionUUIDMismatch |
| `CorruptedChunkShardKey` | .. include:: /includes/inconsistency-type/CorruptedChunkShardKey |
| `CorruptedZoneShardKey` | .. include:: /includes/inconsistency-type/CorruptedZoneShardKey |
| `HiddenShardedCollection` | .. include:: /includes/inconsistency-type/HiddenShardedCollection |
| `InconsistentIndex` | .. include:: /includes/inconsistency-type/InconsistentIndex |
| `MisplacedCollection` | .. include:: /includes/inconsistency-type/MisplacedCollection |
| `MissingRoutingTable` | .. include:: /includes/inconsistency-type/MissingRoutingTable |
| `MissingShardKeyIndex` | .. include:: /includes/inconsistency-type/MissingShardKeyIndex |
| `RoutingTableMissingMaxKey` | .. include:: /includes/inconsistency-type/RoutingTableMissingMaxKey |
| `RoutingTableMissingMinKey` | .. include:: /includes/inconsistency-type/RoutingTableMissingMinKey |
| `RoutingTableRangeGap` | .. include:: /includes/inconsistency-type/RoutingTableRangeGap |
| `RoutingTableRangeOverlap` | .. include:: /includes/inconsistency-type/RoutingTableRangeOverlap |
| `ShardThinksCollectionIsUnsharded` | .. include:: /includes/inconsistency-type/ShardThinksCollectionIsUnsharded |
| `ZonesRangeOverlap` | .. include:: /includes/inconsistency-type/ZonesRangeOverlap |
