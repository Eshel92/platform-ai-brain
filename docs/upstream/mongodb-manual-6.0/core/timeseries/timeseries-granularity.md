<!-- Converted from core/timeseries/timeseries-granularity.txt (reStructuredText). Includes are inlined. -->

# Set Granularity for Time Series Data

**Note:**

You must be running MongoDB 5.0.1 or later in order to change a
time series collection's granularity after the collection has been
created. See MongoDB 5.0 known issues.

When you create a time series collection, set the granularity to the value that
is the closest match to the time span between consecutive incoming
measurements that have the same unique value for the `metaField`
field:

```javascript
db.createCollection(
    "weather24h",
    {
       timeseries: {
          timeField: "timestamp",
          metaField: "metadata",
          granularity: "minutes"
       },
       expireAfterSeconds: 86400
    }
)
```

Setting the `granularity` parameter accurately improves performance by
optimizing how data in the time series collection is stored internally.

To set the parameter accurately, choose a `granularity` value that is
closest to the ingestion rate for a unique data source as specified by
the value for the `metaField` field.

For example, if your `metaField` data identifies weather sensors and
you ingest data from each individual sensor once every 5 minutes, you
should choose `"minutes"`. Even if you have thousands of sensors and
the data coming in from different sensors is only seconds apart, the
`granularity` should still be based on the ingestion rate for one
sensor that is uniquely identified by its metadata.

In the following table, you can see the max time span of data that is
stored together for each `granularity` value:

| `granularity` | Covered Time Span |
|---|---|
| `"seconds"` (default) | one hour |
| `"minutes"` | 24 hours |
| `"hours"` | 30 days |

**See also:**

Timing of Automatic Removal

## Retrieve the `granularity` of a Time Series Collection

To retrieve the current value of `granularity`, use the
`listCollections` command:

```javascript
db.runCommand( { listCollections: 1 } )
```

The result document contains a document for the time series collection
which contains the `options.timeseries.granularity` field.

```javascript
{
    cursor: {
       id: <number>,
       ns: 'test.$cmd.listCollections',
       firstBatch: [
         {
            name: <string>,
            type: 'timeseries',
            options: {
               expireAfterSeconds: <number>,
               timeseries: {
                  timeField: <string>,
                  metaField: <string>,
                  granularity: <string>,
                  bucketMaxSpanSeconds: <number>
               }
            },
            ...
         },
         ...
       ]
    }
 }
```

## Change the `granularity` of a Time Series Collection

To change the `granularity` parameter value, issue the following
`collMod` command:

```javascript
db.runCommand({
   collMod: "weather24h",
   timeseries: { granularity: "hours" }
})
```

Once the `granularity` is set it can only be increased by one level at
a time. From `"seconds"` to `"minutes"` or from `"minutes"` to
`"hours"`. Other changes are not allowed. If you need to change the
`granularity` from `"seconds"` to `"hours"`, first increase the
`granularity` to `"minutes"` and then to `"hours"`.

**Note:**

You cannot modify the `granularity` of a sharded time series
collection.
