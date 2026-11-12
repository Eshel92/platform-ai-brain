<!-- Part 2 of 2 of core/timeseries/timeseries-quick-start.md (split because the page is big). -->

## Sample Data

The following example shows the `stocks` time series collection
structure used in this quick start.

```javascript
{
   _id: ObjectId(...),
   ticker: <string>,
   date: ISODate(...),
   close: <double>,
   volume: <double>
}
```


## Learning Summary

Time series collections are optimized for time data, so performance
depends heavily on how you configure them at creation. For more
information, see Time Series Collection Considerations.


## Next Steps

* To migrate existing data into a time series collection, see Migrate
  Data into a Time Series Collection.

* To shard a time series collection, see Shard a Time Series Collection.

* For aggregation and query behaviors specific to time series
  collections, see Aggregation and Operator Considerations.


## Learn More

* To learn how MongoDB stores time series data internally, see
  About Time Series Data.

* To learn about custom bucketing parameters in MongoDB 6.3 and later,
  see Using Custom Bucketing Parameters.
