<!-- Converted from modules/cassandra/pages/developing/cql/indexing/2i/operations/2i-build.adoc (AsciiDoc). Includes are inlined. -->

# Rebuilding and maintaining secondary indexes (2i)

An advantage of indexes is the operational ease of populating and maintaining the index.
Indexes are built in the background automatically, without blocking reads or writes.
Client-maintained _tables as indexes_ must be created manually;
for example, if the artists column had been indexed by creating a table such as `songs_by_artist`, your client application would have to populate the table with data from the songs table.

To perform a hot rebuild of an index, use the nodetool rebuild_index command.
