<!-- Converted from modules/cassandra/pages/developing/cql/indexing/2i/2i-concepts.adoc (AsciiDoc). Includes are inlined. -->

# Secondary index (2i) concepts

Secondary indexing (2i) is a globally-distributed index for {cassandra} databases.

2i is the original secondary indexing of {product}, but today, it suffers from poor performance and latency. 
If you are building new indexing, use SAI indexing instead.

2i adds column-level indexes to any CQL table column of any CQL data type, except for a counter column.
However, the indexes are locally built on each {product} node in a cluster, so using 2i for queries results in poor performance.
A number of [techniques](https://www.datastax.com/dev/blog/improving-secondary-index-write-performance-in-1-2) exist for guarding against the undesirable scenario where data might be incorrectly retrieved during a query based on stale values in an index.

There are distinct conditions about when and when not to use a 2i index.
