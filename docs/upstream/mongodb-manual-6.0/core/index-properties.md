<!-- Converted from core/index-properties.txt (reStructuredText). Includes are inlined. -->

# Index Properties

In addition to the numerous index types
MongoDB supports, indexes can also have various properties. The
following documents detail the index properties that you can select
when building an index.

/core/index-ttl
   The TTL index is used for TTL collections, which expire data after
   a period of time.

/core/index-unique
   A unique index causes MongoDB to reject all documents that contain
   a duplicate value for the indexed field.

/core/index-partial
   A partial index indexes only documents that meet specified filter
   criteria.

/core/index-case-insensitive
   A case insensitive index disregards the case of the index key
   values.

/core/index-hidden
   A hidden index is not visible to the query planner.

/core/index-sparse
   A sparse index does not index documents that do not have the
   indexed field.
