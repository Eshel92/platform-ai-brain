<!-- Converted from core/timeseries-collections.txt (reStructuredText). Includes are inlined. -->

# Time Series

Time series data is a sequence of data points in which insights are
gained by analyzing changes over time.

Time series data is generally composed of these components:

- **Time** when the data point was recorded.

- **Metadata** (sometimes referred to as source), which is a label or tag
  that uniquely identifies a series and rarely changes.

- **Measurements** (sometimes referred to as metrics or values), which
  are the data points tracked at increments in time. Generally these are
  key-value pairs that change over time.

This table shows examples of time series data:

| **Example** | **Measurement** | **Metadata** |
|---|---|---|
| Stock data | Stock price | Stock ticker, exchange |
| Weather data | Temperature | Sensor identifier, location |
| Website visitors | View count | URL |

For efficient time series data storage, MongoDB provides time series
collections.

## Time Series Collections

**New in version:** 5.0

Time series collections efficiently store time series data. In time
series collections, writes are organized so that data from the same
source is stored alongside other data points from a similar point in
time.

You can create time series collections in the UI for deployments hosted in [MongoDB Atlas](https://www.mongodb.com/docs/atlas?tck=docs_server).

### Benefits

Compared to normal collections, storing time series data in time series
collections improves query efficiency and reduces the disk usage for
time series data and secondary indexes.

Time series collections use an underlying columnar storage format and
store data in time-order with an automatically created clustered
index. The columnar storage format provides the
following benefits:

- Reduced complexity for working with time series data
- Improved query efficiency
- Reduced disk usage
- Reduced I/O for read operations
- Increased WiredTiger cache usage

### Behavior

Time series collections behave like normal collections. You can insert
and query your data as you normally would.

MongoDB treats time series collections as writable non-materialized
views backed by an internal collection. When
you insert data, the internal collection automatically organizes time
series data into an optimized storage format.

When you query time series collections, you operate on one document per
measurement. Queries on time series collections take advantage of the
optimized internal storage format and return results faster.

**Tip:**

To improve query performance, you can manually add secondary
indexes on measurement fields or
any field in your time series collection.

**Important:** Backward-Incompatible Feature

You must drop time series collections before downgrading:

- MongoDB 6.0 or later to MongoDB 5.0.7 or earlier.

- MongoDB 5.3 to MongoDB 5.0.5 or earlier.

**Warning:**

Do not attempt to create a time series collection or view with the
name `system.profile` because the MongoDB server will crash.

### Zone Sharding

Zone sharding does not support time series collections. The
balancer always distributes data in sharded time series
collections evenly across all shards in the cluster.

#### Internal Index

When you create a time series collection, MongoDB automatically creates
an internal clustered index on the time
field. This index improves query efficiency and reduces disk 
usage. To learn more about the performance benefits of clustered 
indexes, see Clustered Collections.

The internal index is not listed when you run `listIndexes`.

**Note:**

If you insert a document into a collection with a `timeField` 
value before `1970-01-01T00:00:00.000Z` or after 
`2038-01-19T03:14:07.000Z`, 
MongoDB logs a warning and prevents some query optimizations from 
using the internal index. Create a secondary index 
on the `timeField` to regain query performance and resolve the log 
warning.

## Get Started

To get started with time series collections, see
timeseries-create-query-procedures.
