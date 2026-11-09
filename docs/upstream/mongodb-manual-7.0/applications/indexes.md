<!-- Converted from applications/indexes.txt (reStructuredText). Includes are inlined. -->

# Indexing Strategies

The best indexes for your application depend on several factors,
including the kinds of queries you expect, the ratio of reads to
writes, and the amount of free memory on your system.

Before building indexes, map out your application's queries and the
fields they access. Indexes have a performance cost, but are worth it
for frequent queries on large data sets. Consider the frequency of
each query and whether it justifies an index.

Profile multiple index configurations against production-representative
data to find which performs best. Inspect existing indexes to confirm
they support your current and planned queries. Drop indexes that are
no longer used.

Generally, MongoDB only uses *one* index to fulfill most queries.
However, each clause of an `$or` query may use a different
index.

The following documents introduce indexing strategies:

Use the ESR (Equality, Sort, Range) Guideline
   Arrange compound index keys to optimize equality, sort, and range
   operations.

create-indexes-to-support-queries
   An index supports a query when it contains all the fields the query
   scans, greatly improving performance.

sorting-with-indexes
   Use these strategies to specify index field order and support
   efficient sort queries.

index-selectivity
   Understand how index selectivity affects query performance and
   design indexes that answer queries efficiently.

unique-indexes-schema-validation
   Combine index properties and schema validation to implement your
   application design.
