<!-- Converted from modules/cassandra/pages/developing/cql/indexing/indexing-concepts.adoc (AsciiDoc). Includes are inlined. -->

# Indexing concepts

The data stored in CQL tables can be queried by a variety of methods.
The main method uses the partition key defined for a table, and is called primary indexing.
Often, however, a query must use another column of a table to select the rows desired, and secondary indexing is required.
Secondary indexing use fast, efficient lookup of data that matches a given condition.
After any index is created, data can be queried using that index.

{product} has the following types of indexing available:

|===
| Indexing type 
| Versions

a| Primary indexing
| All

a| Storage-attached indexing (SAI)
| 5.0

a| Secondary indexing (2i)
| All
|===

## Primary indexing

The primary index is the partition key in {product}. The storage engine of {product} uses the partition key to store rows of data, and the most efficient and fast lookup of data matches the partition key.

## Storage-attached indexing (SAI)

SAI uses indexes for non-partition columns, and attaches the indexing information to the SSTables that store the rows of data.
The indexes are located on the same node as the SSTable, and are updated when the SSTable is updated.
SAI is the most appropriate indexing method for most use cases.

## Secondary indexing (2i)

Secondary indexing is the original built-in indexing written for {product}.
These indexes are all local indexes, stored in a hidden table on each node of a {product} cluster, separate from the table that contains the values being indexed.
The index must be read from the node.
This indexing method is only recommended when used in conjunction with a partition key.
