<!-- Converted from core/indexes/index-types.txt (reStructuredText). Includes are inlined. -->

# Index Types

This page describes the types of indexes you can create in MongoDB.
Different index types support different types of data and queries.

## Single Field Index

Single field indexes collect and sort data from a single field in each
document in a collection.

This image shows an index on a single field, `score`:

(Figure: /images/index-ascending.bakedsvg.svg)

To learn more, see indexes-single-field.

## Compound Index

Compound indexes collect and sort data from multiple field values from each
document in a collection. You can use the compound index to query the first 
field or any prefix fields of the index. 
The order of fields in a compound index is very important. The B-tree created
by a compound index stores the sorted data in the order that the index specifies
the fields. 

For example, the following image shows a compound index where documents
are first sorted by `userid` in ascending order (alphabetically).
Then, the `scores` for each `userid` are sorted in descending order:

(Figure: /images/index-compound-key.bakedsvg.svg)

To learn more, see index-type-compound.

## Multikey Index

Multikey indexes collect and sort data stored in arrays.

This image shows a multikey index on the `addr.zip` field:

(Figure: /images/index-multikey.bakedsvg.svg)

To learn more, see index-type-multikey.

## Wildcard Index

Wildcard indexes apply to collections with flexible schemas,
where document field names may differ. Use wildcard indexes to support
queries against arbitrary or unknown field names.

To learn more, see wildcard-index-core.

## Geospatial Index

Geospatial indexes improve performance for queries on geospatial
coordinate data. To learn more, see geospatial-index.

## Hashed Index

Hashed indexes support hashed sharding. Hashed indexes index the hash of a field's value.

To learn more, see index-type-hashed.

## Text Index

Text indexes support text search queries on fields containing string content. 

To learn more, see index-type-text.

**Note:** Use Atlas Search or Atlas Vector Search on Atlas Deployments

For data hosted on MongoDB Atlas, MongoDB offers the
following text search solutions:

- Atlas Search provides improved performance
  and functionality compared to on-premises text search.
- Atlas Vector Search 
  provides vector search capabilities to perform semantic, hybrid, and generative
  search.

## Clustered Index

Clustered indexes specify the order in which clustered collections store data. Collections created with a
clustered index are called clustered collections.

To learn how to create a collection with a clustered index, see
clustered-collections-index-example.
