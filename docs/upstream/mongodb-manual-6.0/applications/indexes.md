<!-- Converted from applications/indexes.txt (reStructuredText). Includes are inlined. -->

# Indexing Strategies

The best indexes for your application must take a number
of factors into account, including the kinds of queries you expect,
the ratio of reads to writes, and the amount of free memory on your
system.

When developing your indexing strategy you should have a deep
understanding of your application's queries. Before you build indexes,
map out the types of queries you will run so that you can build
indexes that reference those fields. Indexes come with a performance
cost, but are more than worth the cost for frequent queries on large
data sets. Consider the relative frequency of each query in the
application and whether the query justifies an index.

The best overall strategy for designing indexes is to profile a
variety of index configurations with data sets similar to the ones
you'll be running in production to see which configurations perform
best. Inspect the current indexes created for your collections to
ensure they are supporting your current and planned queries. If an
index is no longer used, drop the index.

Generally, MongoDB only uses *one* index to fulfill most queries.
However, each clause of an `$or` query may use a different
index, and in addition, MongoDB can use an intersection of multiple indexes.

The following documents introduce indexing strategies:

Use the ESR (Equality, Sort, Range) Guideline
   The ESR (Equality, Sort, Range) Guideline is a guide to creating indexes
   that support your queries efficiently.

create-indexes-to-support-queries
   An index supports a query when the index contains all the fields
   scanned by the query. Creating indexes that support queries
   results in greatly increased query performance.

sorting-with-indexes
   To support efficient queries, use the strategies here when you
   specify the sequential order and sort order of index fields.

index-selectivity
   Understand how index selectivity plays a role in query performance
   and learn to design indexes to answer a given query most efficiently.
