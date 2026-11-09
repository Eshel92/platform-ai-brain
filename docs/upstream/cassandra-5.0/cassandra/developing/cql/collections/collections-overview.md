<!-- Converted from modules/cassandra/pages/developing/cql/collections/collections-overview.adoc (AsciiDoc). Includes are inlined. -->

# Collection data types overview

{product} provides collection data types as a way to group and store data together in a column.
For example, in a relational database, a grouping such as a user's multiple email addresses is related with a many-to-one joined relationship between a user table and an email table.
 
{product} avoids joins between two tables by storing the user's email addresses in a collection column in the user table.
Each collection specifies the data type of the data held.

A collection is appropriate if the data for collection storage is limited.
If the data has unbounded growth potential, like messages sent or sensor events registered every second, do not use collections.
Instead, use a table with a compound primary key where data is stored in the clustering columns.
