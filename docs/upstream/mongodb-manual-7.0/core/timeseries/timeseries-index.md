<!-- Converted from core/timeseries/timeseries-index.txt (reStructuredText). Includes are inlined. -->

# Time Series Indexes

Indexes on time series collections generally behave like indexes on
regular collections, but with several additional considerations and
limitations. 

If there are secondary indexes on time
series collections and you need to
downgrade the feature compatibility version (FCV), you must first drop
any secondary indexes that are incompatible with the downgraded FCV.
For more information, see `setFeatureCompatibilityVersion`.

Starting in version 6.0, you can add a secondary index to any field in a
time series collection. MongoDB indexes time series collections by
buckets of documents as opposed to individual
documents. Time series buckets contain documents with shared metaField values,
ordered by timeField values that are close together. MongoDB indexes the
minimum and maximum values of all fields, except the metaField. Indexing
buckets instead of individual documents reduces index size and improves query
efficiency.

**Tip:**

To improve query performance, you can manually add secondary
indexes to any field in your time
series collection.

## Clustered Collection

By default, MongoDB clusters time series collections based on bucket
time. 

## Compound Indexes

**New in version:** 6.3

Starting in MongoDB 6.3, MongoDB creates a default  compound index on both the metaField and timeField of a time
series collection. MongoDB uses this index to improve query performance
and speed. 

You can add a compound index on the
`timeField`, `metaField`, or measurement fields.

## Partial Indexes

**New in version:** 6.0

Starting in MongoDB 6.0, you can use the `$or`, `$in`, and
`$geoWithin` operators with partial indexes on a time series collection.

You cannot create partial indexes on the
metaField and timeField. 

## TTL Indexes

**New in version:** 7.0

Starting in MongoDB 7.0, you can create a TTL
index with a `partialFilterExpression` that relies only on the
metaField. In versions prior to 6.3, you can only create TTL indexes
based on the `expireAfterSeconds` parameter. 

If your time series collection doesn't use the `expireAfterSeconds`
option to expire documents, creating a partial TTL index sets an
expiration time for matching documents only. If the collection uses
`expireAfterSeconds` for all documents, you can use a partial TTL
index to expire matching documents sooner.

## Prohibited Indexes

MongoDB does not allow the following index types on time series
collections:

- Text indexes
- 2d indexes
- Unique indexes

You cannot create sparse indexes on the metaField. 

## Indexing Best Practices

- Use the metaField index for filtering and equality.
- Use the timeField and other indexed fields for range queries. 
- General indexing strategies also apply to time series collections. For
  more information, see indexing-strategies.

For more information and examples, see
timeseries-add-secondary-index.
