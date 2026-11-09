<!-- Converted from core/timeseries/timeseries-migrate-with-aggregation.txt (reStructuredText). Includes are inlined. -->

# Migrate Data into a Time Series Collection with Aggregation

Starting in MongoDB version 7.0, you can use the `$out`
aggregation stage to migrate data from an existing collection into a
time series collection.

**Note:**

MongoDB does not guarantee output order when you use `$out` to
migrate data into a times series collection. To maintain order, sort
your data before you migrate with an aggregation pipeline. 

## Before you Begin

Consider a `weatherdata` collection that contains time and metadata information:

```javascript
db.weatherdata.insertOne(
   {
      _id: ObjectId("5553a998e4b02cf7151190b8"),
      st: "x+47600-047900",
      ts: ISODate("1984-03-05T13:00:00Z"),
      position: {
         type: "Point",
         coordinates: [ -47.9, 47.6 ]
      },
      elevation: 9999,
      callLetters: "VCSZ",
      qualityControlProcess: "V020",
      dataSource: "4",
      type: "FM-13",
      airTemperature: { value: -3.1, quality: "1" },
      dewPoint: { value: 999.9, quality : "9" },
      pressure: { value: 1015.3, quality: "1" },
      wind: {
         direction: { angle: 999, quality: "9" },
         type: "9",
         speed: { rate: 999.9, quality: "9" }
      },
      visibility: {
         distance: { value: 999999, quality : "9" },
         variability: { value: "N", quality: "9" }
      },
      skyCondition: {
         ceilingHeight: { value: 99999, quality: "9", determination: "9" },
         cavok: "N"
      },
      sections: [ "AG1" ],
      precipitationEstimatedObservation: { 
         discrepancy: "2",
         estimatedWaterDepth: 999 
      }
   }
)
```

## Steps

**Step 1: Create a metadata field.**

If your collection doesn't include a field you can use to identify each
series, transform your data to define one. In this example, the
`metaData` field becomes the `metaField` of the time series collection
that you create.  

**Note:**

Choosing the right field as your time series `metaField` and
`granularity` optimizes both storage and query performance. For more
information on field selection and best practices, see metaField and
Granularity Best Practices. 

The pipline below performs the following operations:

- Uses `$addFields` to add a `metaData` field to the
  `weather_data` collection.
- Uses `$project` to include or exclude the remaining fields in the
  document. 

```javascript
db.weather_data.aggregate([
{
   $addFields: {
      metaData: {
         "st": "$st",
         "position": "$position",
         "elevation": "$elevation",
         "callLetters": "$callLetters",
         "qualityControlProcess": "$qualityControlProcess",
         "type": "$type"
      }
   },
}, 
{
   $project: {
      _id: 1,
      ts: 1,
      metaData: 1,
      dataSource: 1,
      airTemperature: 1,
      dewPoint: 1,
      pressure: 1,
      wind: 1,
      visibility: 1,
      skyCondition: 1,
      sections: 1,
      precipitationEstimatedObservation: 1
   }
}
])
```

**Step 2: Create your time series collection and insert your data.**

Add an `$out` aggregation stage to your pipeline to create a
time series collection and insert your data into it. The pipeline below
performs the following operations:

- Uses `$out` with the
  `timeseries` option to create a `weathernew` time series collection
  in the `mydatabase` database. 
- Defines the `metaData` field as the `metaField` of 
  the `weathernew` collection.
- Defines the `ts` field as the `timeField` of the
  `weathernew` collection.

  **Note:**

  The `timeField` of a time series collection must be a date type. 

```javascript
{
   $out: {
      db: "mydatabase",
      coll: "weathernew",
      timeseries: {
         timeField: "ts",
         metaField: "metaData",
         granularity: "seconds"
      }
   }
}
```

For the aggregation stage syntax, see
`$out`. For a full explanation of the time series
options, see the Time Series Field Reference.

**Step 3: Review your data.**

After you run this aggregation pipeline, you can use
`findOne()` to view a document in your
`weathernew` time series collection:

```javascript
db.weathernew.findOne()
```

The operation returns the following document: 

```javascript
   {
      _id: ObjectId("5553a998e4b02cf7151190b8"),
      ts: ISODate("1984-03-05T13:00:00Z"),
      metaData: {
         st: "x+47600-047900",
         position: {
            type: "Point",
            coordinates: [ -47.9, 47.6 ]
         },
         elevation: 9999,
         callLetters: "VCSZ",
         qualityControlProcess: "V020",
         type: "FM-13"
      },
      dataSource: "4",
      airTemperature: { value: -3.1, quality: "1" },
      dewPoint: { value: 999.9, quality: "9" },
      pressure: { value: 1015.3, quality: "1" },
      wind: {
         direction: { angle: 999, quality: "9" },
         type: "9",
         speed: { rate: 999.9, quality: "9" }
      },
      visibility: {
         distance: { value: 999999, quality: "9" },
         variability: { value: "N", quality: "9" }
      },
      skyCondition: {
         ceilingHeight: { value: 99999, quality: "9", determination: "9" },
         cavok: "N"
      },
      sections: [ "AG1" ],
      precipitationEstimatedObservation: { discrepancy: "2", estimatedWaterDepth: 999 }
   }
```

For more information on additional considerations for migrating your data, see
timeseries-best-practices. 

## Next Steps

If your original collection had secondary indexes, manually recreate 
them now. 

If your time series collection includes `timeField` values before
`1970-01-01T00:00:00.000Z` or after `2038-01-19T03:14:07.000Z`,
MongoDB logs a warning and disables some query optimizations that make
use of the internal clustered index. To regain query performance and
resolve the log warning, create a secondary index on the `timeField`.

**See also:**

timeseries-add-secondary-index
