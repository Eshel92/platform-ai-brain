<!-- Converted from core/timeseries/timeseries-procedures.txt (reStructuredText). Includes are inlined. -->

# Create and Query a Time Series Collection

This page shows how to create and query a time series collection, with
code examples.

**Important:** Feature Compatibility Version Requirement

You can only create time series collections on a system with
featureCompatibilityVersion set to 5.0 or greater.

## Create a Time Series Collection

**Step 1: **

Define the `timeField` as the field that contains time data and
the `metaField` as the field that contains metadata: 

```javascript
{
   timeField: "timestamp",
   metaField: "metadata"
}
```

In this example, `timestamp` is the name of the
`timeField` and `metadata` is the name of the `metaField`.
The value of the `timestamp` field must be a date type. 

**Important:**

Choosing the right `metaField` for your collection optimizes
both storage and query performance. For more information on
`metaField` selection and best practices, see
timeseries-collections-metafield. 

**Step 2: **

Define the time interval for each bucket of data using one 
of the two approaches below:

**Important:** Changing Time Series Intervals

After creation, you can modify granularity or bucket
definitions using the `collMod` method. However,
you can only increase the time span covered by each bucket. You
cannot decrease it.

A. Define a `granularity` field:

   ```javascript
   {
      granularity: "seconds"
   }
   ```

   For more detailed information on selecting a `granularity`
   value, see Granularity Considerations.

**OR**

B. Define the `bucketMaxSpanSeconds` and `bucketRoundingSeconds` 
   fields. Both values must be the same:

   ```javascript
   {
      bucketMaxSpanSeconds: 300,
      bucketRoundingSeconds: 300
   }
   ```

**Step 3: **

Optionally, set `expireAfterSeconds` to expire documents 
when the value of the `timeField` is at least that old:

```javascript
{
   expireAfterSeconds: 86400
}
```

**Step 4: **

Create the collection using either the
`db.createCollection()` method or the `create`
command. The follow example uses the
`db.createCollection()` method to create a `weather`
time series collection:

```javascript
db.createCollection(
   "weather",
   {
      timeseries: {
         timeField: "timestamp",
         metaField: "metadata",
         granularity: "seconds"
      },
      expireAfterSeconds: 86400
   }
)
```

### Time Series Field Reference

A time series collection includes the following fields:

| Field | Type | Description |
|---|---|---|
| `timeseries.timeField` | string | .. include:: /includes/time-series/fact-time-field-description.rst |
| `timeseries.metaField` | string | .. include:: /includes/time-series/fact-meta-field-description.rst |
| `timeseries.granularity` | integer | .. include:: /includes/time-series/fact-granularity-field-description.rst |
| `timeseries.bucketMaxSpanSeconds` | integer | .. include:: /includes/time-series/fact-bucketmaxspanseconds-field-description.rst |
| `timeseries.bucketRoundingSeconds` | integer | .. include:: /includes/time-series/fact-bucketroundingseconds-field-description.rst |
| `expireAfterSeconds` | integer | Optional. Enable the automatic deletion of documents in a time series collection by specifying the number of seconds after which documents expire. MongoDB deletes expired documents automatically. See manual-timeseries-automatic-removal for more information. |

Other allowed options that are not specific to time series collections are:

- `storageEngine`
- `indexOptionDefaults`
- `collation`
- `writeConcern`
- `comment`

**See also:**

`db.createCollection()` and `create`.

## Insert Measurements into a Time Series Collection

Each document you insert should contain a single measurement. To insert
multiple documents at once, issue the following command:

```javascript
db.weather.insertMany( [
   {
      metadata: { sensorId: 5578, type: "temperature" },
      timestamp: ISODate("2021-05-18T00:00:00.000Z"),
      temp: 12
   },
   {
      metadata: { sensorId: 5578, type: "temperature" },
      timestamp: ISODate("2021-05-18T04:00:00.000Z"),
      temp: 11
   },
   {
      metadata: { sensorId: 5578, type: "temperature" },
      timestamp: ISODate("2021-05-18T08:00:00.000Z"),
      temp: 11
   },
   {
      metadata: { sensorId: 5578, type: "temperature" },
      timestamp: ISODate("2021-05-18T12:00:00.000Z"),
      temp: 12
   },
   {
      metadata: { sensorId: 5578, type: "temperature" },
      timestamp: ISODate("2021-05-18T16:00:00.000Z"),
      temp: 16
   },
   {
      metadata: { sensorId: 5578, type: "temperature" },
      timestamp: ISODate("2021-05-18T20:00:00.000Z"),
      temp: 15
   }, 
   {
      metadata: { sensorId: 5578, type: "temperature" },
      timestamp: ISODate("2021-05-19T00:00:00.000Z"),
      temp: 13
   },
   {
      metadata: { sensorId: 5578, type: "temperature" },
      timestamp: ISODate("2021-05-19T04:00:00.000Z"),
      temp: 12
   },
   {
      metadata: { sensorId: 5578, type: "temperature" },
      timestamp: ISODate("2021-05-19T08:00:00.000Z"),
      temp: 11
   },
   {
      metadata: { sensorId: 5578, type: "temperature" },
      timestamp: ISODate("2021-05-19T12:00:00.000Z"),
      temp: 12
   },
   {
      metadata: { sensorId: 5578, type: "temperature" },
      timestamp: ISODate("2021-05-19T16:00:00.000Z"),
      temp: 17
   },
   {
      metadata: { sensorId: 5578, type: "temperature" },
      timestamp: ISODate("2021-05-19T20:00:00.000Z"),
      temp: 12
   }
] )
```

To insert a single document, use the `db.collection.insertOne()`
method.

**Tip:** Optimize Insert Performance

To learn how to optimize inserts for large operations, see
tsc-best-practice-optimize-inserts.

## Query a Time Series Collection

You query a time series collection the same way you query a standard MongoDB collection.

To return one document from a time series collection, run:

```javascript
db.weather.findOne( {
   timestamp: ISODate("2021-05-18T00:00:00.000Z")
} )
```

Example output:

```javascript
{
   timestamp: ISODate("2021-05-18T00:00:00.000Z"),
   metadata: { sensorId: 5578, type: 'temperature' },
   temp: 12,
   _id: ObjectId("62f11bbf1e52f124b84479ad")
}
```

For more information on time series queries, see
tsc-best-practice-optimize-query-performance.

## Run Aggregations on a Time Series Collection

For additional query functionality, use an aggregation pipeline such as:

```javascript
db.weather.aggregate( [
   {
      $project: {
         date: {
            $dateToParts: { date: "$timestamp" }
         },
         temp: 1
      }
   },
   {
      $group: {
         _id: {
            date: {
               year: "$date.year",
               month: "$date.month",
               day: "$date.day"
            }
         },
         avgTmp: { $avg: "$temp" }
      }
   }
] )
```

The example aggregation pipeline groups all documents by the date of the
measurement and then returns the average of all temperature measurements
that day:

```javascript
 :copyable: false

 {
  "_id" : {
    "date" : {
      "year" : 2021,
      "month" : 5,
      "day" : 18
    }
  },
  "avgTmp" : 12.714285714285714
}
{
  "_id" : {
    "date" : {
      "year" : 2021,
      "month" : 5,
      "day" : 19
    }
  },
  "avgTmp" : 13
}
```
