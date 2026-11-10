<!-- Converted from ml/anomaly-detection/functions/ml-geo-functions.asciidoc (AsciiDoc). Includes are inlined. -->

# Geographic functions

The geographic functions detect anomalies in the geographic location of the
input data.

The {ml-features} include the following geographic function: `lat_long`.

**Note:** You cannot create forecasts for anomaly detection jobs that contain geographic
functions. You also cannot add rules with conditions to detectors that use
geographic functions. 

## Lat_long

The `lat_long` function detects anomalies in the geographic location of the
input data.

This function supports the following properties:

* `field_name` (required)
* `by_field_name` (optional)
* `over_field_name` (optional)
* `partition_field_name` (optional)

For more information about those properties, see the
[create anomaly detection jobs API](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/ml-put-job.html#ml-put-job-request-body).

**Example 1: Analyzing transactions with the lat_long function**
```console
PUT _ml/anomaly_detectors/example1
{
  "analysis_config": {
    "detectors": [{
      "function" : "lat_long",
      "field_name" : "transaction_coordinates",
      "by_field_name" : "credit_card_number"
    }]
  },
  "data_description": {
    "time_field":"timestamp",
    "time_format": "epoch_ms"
  }
}
```

If you use this `lat_long` function in a detector in your anomaly detection job, it
detects anomalies where the geographic location of a credit card transaction is
unusual for a particular customer’s credit card. An anomaly might indicate 
fraud.

A "typical" value indicates a centroid of a cluster of previously observed 
locations that is closest to the "actual" location at that time. For example, 
there may be one centroid near the person's home that is associated with the 
cluster of local grocery stores and restaurants, and another centroid near the 
person's work associated with the cluster of lunch and coffee places.   

**Important:** The `field_name` that you supply must be a single string that 
contains two comma-separated numbers of the form `latitude,longitude`, a 
`geo_point` field, a `geo_shape` field that contains point values, or a 
`geo_centroid` aggregation. The `latitude` and `longitude` must be in the range 
-180 to 180 and represent a point on the surface of the Earth.

For example, JSON data might contain the following transaction coordinates:

```js
{
  "time": 1460464275,
  "transaction_coordinates": "40.7,-74.0",
  "credit_card_number": "1234123412341234"
}
```

In Elasticsearch, location data is likely to be stored in `geo_point` fields. For more
information, see [`geo_point` data type](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/geo-point.html). This data type is
supported natively in {ml-features}. Specifically, when pulling data from a
`geo_point` field, a datafeed will transform the data into the appropriate
`lat,lon` string format before sending to the anomaly detection job.

For more information, see ml-configuring-transform.
