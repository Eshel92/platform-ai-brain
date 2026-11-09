<!-- Converted from core/timeseries/timeseries-aggregations-operators.txt (reStructuredText). Includes are inlined. -->

# Aggregation and Operator Considerations

Some aggregation stages and operators require special considerations
when you use them with time series collections. 

## $geoNear

Time series collections only support the `$geoNear`
aggregation stage for sorting geospatial data from queries against 2dsphere indexes. You can't use the `$near` and
`$nearSphere` operators on time series collections.

You can't use the `query` field for `$geoNear` on a 
time series collection.

You must specify the `key` field for `$geoNear` on a 
time series collection.

## $merge

You cannot use the `$merge` aggregation stage to add data from
another collection to a time series collection.

## $out

Starting in MongoDB 7.0, you can use the `$out` aggregation stage to write
documents to a time series collection. For more information, see
migrate-data-into-a-timeseries-collection. 

## Frequently Used Operations

The following aggregation pipeline operators and stages are often used to analyze
time series data:

- `$dateAdd`: Adds a specified amount of time to a Date
  object.
- `$dateDiff`: Returns the time difference between two dates.
- `$dateTrunc`: Returns a date that has been truncated to
  the specific unit.
- `$setWindowFields`: Runs calculations on documents in a
  given window.

## Examples

### Calculate Average Price per Month

Consider a `dowJonesTickerData` collection that contains
documents with the following structure:

```javascript
{
   date: ISODate("2020-01-03T05:00:00.000Z"),
   symbol: 'AAPL',
   volume: 146322800,
   open: 74.287498,
   adjClose: 73.486023,
   high: 75.144997,
   low: 74.125,
   close: 74.357498
}
```

This aggregation pipeline performs the following actions:

- Uses `$dateTrunc` to truncate each document's `date` to the
  appropriate month.
- Uses `$group` to group the documents by month and symbol. 
- Uses `$avg` to calculate the average price per month. 

```javascript
db.dowJonesTickerData.aggregate( [ {
   $group: {
      _id: {
         firstDayOfMonth: {
            $dateTrunc: {
               date: "$date",
               unit: "month"
            }
         },
         symbol: "$symbol"
      },
      avgMonthClose: {
         $avg: "$close"
      }
   }
} ] )
```

The pipeline returns a set of documents where each document contains the
average closing price per month for a particular stock. 

```javascript
{
   _id: {
      firstDayOfMonth: ISODate("2020-06-01T00:00:00.000Z"),
      symbol: 'GOOG'
   },
   avgMonthClose: 1431.0477184545455
},
{
   _id: {
      firstDayOfMonth: ISODate("2021-07-01T00:00:00.000Z"),
      symbol: 'MDB'
   },
   avgMonthClose: 352.7314293333333
},
{
   _id: {
      firstDayOfMonth: ISODate("2021-06-01T00:00:00.000Z"),
      symbol: 'MSFT'
   },
   avgMonthClose: 259.01818086363636
}
```

### Calculate a Rolling Average Over 30 Days

Consider a `dowJonesTickerData` collection that contains
documents with the following structure:

```javascript
{
   date: ISODate("2020-01-03T05:00:00.000Z"),
   symbol: 'AAPL',
   volume: 146322800,
   open: 74.287498,
   adjClose: 73.486023,
   high: 75.144997,
   low: 74.125,
   close: 74.357498
}
```

This aggregation pipeline performs the following operations:

- Uses `$setWindowFields` to specify a window of 30 days.
- Calculates a rolling average of the closing price over the last 30
  days for each stock.

```javascript
db.dowJonesTickerData.aggregate( [
   { $setWindowFields: {
      partitionBy: { symbol : "$symbol" } ,
      sortBy: { date: 1 },
      output: {
         averageMonthClosingPrice: {
            $avg : "$close",
            window : { range : [-1, "current"], unit : "month" }

         } 
      } 
   } }
] )
```

The pipeline returns a set of documents where each document includes a
`$averageMonthClosingPrice` field that contains the average of the
previous month's closing price for that stock symbol. 

```javascript
{
   date: ISODate("2020-01-29T05:00:00.000Z"),
   symbol: 'AAPL',
   volume: 216229200,
   adjClose: 80.014801,
   low: 80.345001,
   high: 81.962502,
   open: 81.112503,
   close: 81.084999,
   averageMonthClosingPrice: 77.63137520000001
}
```
