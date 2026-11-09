<!-- Converted from core/timeseries/timeseries-best-practices.txt (reStructuredText). Includes are inlined. -->

# Best Practices for Time Series Collections

This page describes best practices to improve performance and data usage
for time series collections.

## Optimize Inserts

To optimize insert performance for time series collections, perform the
following actions.

### Batch Document Writes

When inserting multiple documents:

- To avoid network roundtrips, use a single
  `insertMany()` statement as opposed to
  multiple `insertOne()` statements.

- If possible, construct batches to contain multiple measurements per series 
  (as defined by metadata).
 
- To improve performance, set the `ordered` parameter to `false`.

For example, if you have two sensors, `sensor A` and `sensor B`, a
batch containing multiple measurements from a single sensor incurs the
cost of one insert, rather than one insert per measurement.

The following operation inserts six documents, but only incurs the cost
of two inserts (one per batch), because the documents are ordered by
sensor. The `ordered` parameter is set to `false` to improve performance:

```javascript
db.temperatures.insertMany( [
   {
      "metadata": {
         "sensor": "sensorA"
      },
      "timestamp": ISODate("2021-05-18T00:00:00.000Z"),
      temperature: 10
   },
   {
      "metadata": {
         "sensor": "sensorA"
      },
      "timestamp": ISODate("2021-05-19T00:00:00.000Z"),
      temperature: 12
   },
   {
      "metadata": {
         "sensor": "sensorA"
      },
      "timestamp": ISODate("2021-05-20T00:00:00.000Z"),
      temperature: 13
   },
   {
      "metadata": {
         "sensor": "sensorB"
      },
      "timestamp": ISODate("2021-05-18T00:00:00.000Z"),
      temperature: 20
   },
   {
      "metadata": {
         "sensor": "sensorB"
      },
      "timestamp": ISODate("2021-05-19T00:00:00.000Z"),
      temperature: 25
   },
   {
      "metadata": {
         "sensor": "sensorB"
      },
      "timestamp": ISODate("2021-05-20T00:00:00.000Z"),
      temperature: 26
   }
], {
   "ordered": false
})
```

### Use Consistent Field Order in Documents

Using a consistent field order in your documents improves insert
performance. 

For example, inserting these documents achieves optimal insert
performance:

```javascript
{ 
   _id: ObjectId("6250a0ef02a1877734a9df57"),
   timestamp: 2020-01-23T00:00:00.441Z,
   name: 'sensor1',
   range: 1 
}, 
{
   _id: ObjectId("6560a0ef02a1877734a9df66")
   timestamp: 2020-01-23T01:00:00.441Z,
   name: 'sensor1',
   range: 5
} 
```

In contrast, these documents *do not* achieve optimal insert
performance, because their field orders differ:

```javascript
{ 
   range: 1,
   _id: ObjectId("6250a0ef02a1877734a9df57"),
   name: 'sensor1',
   timestamp: 2020-01-23T00:00:00.441Z
}, 
{
   _id: ObjectId("6560a0ef02a1877734a9df66")
   name: 'sensor1',
   timestamp: 2020-01-23T01:00:00.441Z,
   range: 5
} 
```

### Increase the Number of Clients

Increasing the number of clients writing data to your collections can
improve performance.

## Optimize Compression

To optimize data compression for time series collections, perform the
following actions.

### Omit Fields Containing Empty Objects and Arrays from Documents

To optimize compression, if your data contains empty objects or arrays,
omit the empty fields from your documents.

For example, consider the following documents:

```javascript
{
 time: 2020-01-23T00:00:00.441Z,
 coordinates: [1.0, 2.0]
},
{
   time: 2020-01-23T00:00:10.441Z,
   coordinates: []
},
{
   time: 2020-01-23T00:00:20.441Z,
   coordinates: [3.0, 5.0]
}
```

The alternation between `coordinates` fields with populated values and
an empty array result in a schema change for the compressor. The schema
change causes the second and third documents in the sequence remain
uncompressed.

In contrast, the following documents where the empty array is omitted
receive the benefit of optimal compression:

```javascript
{
   time: 2020-01-23T00:00:00.441Z,
   coordinates: [1.0, 2.0]
},
{
   time: 2020-01-23T00:00:10.441Z
},
{
   time: 2020-01-23T00:00:20.441Z,
   coordinates: [3.0, 5.0]
}
```

### Round Numeric Data to Few Decimal Places

Round numeric data to the precision required for your application.
Rounding numeric data to fewer decimal places improves the compression
ratio.

## Optimize Query Performance

To improve query performance, 
create one or more secondary indexes 
on your `timeField` and `metaField` to support common query 
patterns. 

### Use $group Instead of Distinct()

Due to the unique data structure of time series collections, MongoDB can't
efficiently index them for distinct values. Avoid using the
`distinct` command or `db.collection.distinct()` helper
method on time series collections. Instead, use a `$group` 
aggregation to group documents by distinct values. 

For example, to query for distinct `meta.type` values on documents
where `meta.project = 10`, instead of:

```javascript
db.foo.distinct("meta.type", {"meta.project": 10})
```

Use:

```javascript
db.foo.createIndex({"meta.project":1, "meta.type":1})
db.foo.aggregate([{$match: {"meta.project": 10}},
                  {$group: {_id: "$meta.type"}}])
```

This works as follows:

#. Creating a compound index on `meta.project`
   and `meta.type` and supports the aggregation. 

#. The `$match` stage filters for documents where `meta.project = 10`.

#. The `$group` stage uses `meta.type` as the group key to output
   one document per unique value.
