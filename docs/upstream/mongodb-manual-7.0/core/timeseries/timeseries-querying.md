<!-- Converted from core/timeseries/timeseries-querying.txt (reStructuredText). Includes are inlined. -->

# About Querying Time Series Data

   

MongoDB groups documents with matching metaFields to optimize the storage and query
latency of time series data. Your choice of `metaField` has the biggest 
impact on optimizing queries in your application.

## Querying the metaField

You query a time series collection the same way you query a standard MongoDB
collection. For an example query and example aggregation pipeline, see
timeseries-query-example. For a list of querying best practices, see 
tsc-best-practice-optimize-query-performance.

Queries against time series data typically focus on a single time series in the
collection. For example, consider a time series collection that tracks stock
data using the following schema:

```javascript
{
   _id: 573a1397f29313caabce8347,

   "ticker": "MDB",
   "timestamp": ISODate("2024-07-24T13:45:00.000Z"),
   "price": 248.21,
   "volume": 6930
}
```

The collection has the following settings:

```javascript
timeseries: {
   timeField: "timestamp",
   metaField: "ticker",
   granularity: "seconds"
}
```

MongoDB groups documents with matching `ticker` values. Instead of having to
check for matches across all fields in all documents, the server only has to
check against the `metaField`, in this case `ticker`, to narrow down
the search range to a unique time series. This fits the expected use
case, which is searching for activity on a single stock. A user searching for
information on MongoDB stock (MDB) doesn't need to consider results for Amazon
(AMZN).

## Querying the timeField

The second major dimension for querying time series data is time. Since MongoDB
groups documents that have both an identical `metaField` value and close
`timeField` values, this further narrows the scope of a query to a range of
buckets. Recent transactions are kept in memory, so it's easy to stream data in
real time.
