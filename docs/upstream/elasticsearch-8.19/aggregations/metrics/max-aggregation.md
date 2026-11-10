<!-- Converted from aggregations/metrics/max-aggregation.asciidoc (AsciiDoc). Includes are inlined. -->

### Max aggregation

A `single-value` metrics aggregation that keeps track and returns the maximum
value among the numeric values extracted from the aggregated documents.

**Note:** The `min` and `max` aggregation operate on the `double` representation of
the data. As a consequence, the result may be approximate when running on longs
whose absolute value is greater than 2^53.

Computing the max price value across all documents

```console
POST /sales/_search?size=0
{
  "aggs": {
    "max_price": { "max": { "field": "price" } }
  }
}
```

Response:

```console-result
{
  ...
  "aggregations": {
      "max_price": {
          "value": 200.0
      }
  }
}
```

As can be seen, the name of the aggregation (`max_price` above) also serves as
the key by which the aggregation result can be retrieved from the returned
response.

#### Script

If you need to get the `max` of something more complex than a single field,
run an aggregation on a runtime field.

```console
POST /sales/_search
{
  "size": 0,
  "runtime_mappings": {
    "price.adjusted": {
      "type": "double",
      "script": """
        double price = doc['price'].value;
        if (doc['promoted'].value) {
          price *= 0.8;
        }
        emit(price);
      """
    }
  },
  "aggs": {
    "max_price": {
      "max": { "field": "price.adjusted" }
    }
  }
}
```

#### Missing value

The `missing` parameter defines how documents that are missing a value should
be treated. By default they will be ignored but it is also possible to treat
them as if they had a value.

```console
POST /sales/_search
{
  "aggs" : {
      "grade_max" : {
          "max" : {
              "field" : "grade",
              "missing": 10       <1>
          }
      }
  }
}
```

<1> Documents without a value in the `grade` field will fall into the same
bucket as documents that have the value `10`.

#### Histogram fields

When `max` is computed on histogram fields, the result of the aggregation is the maximum
of all elements in the `values` array. Note, that the `counts` array of the histogram is ignored.

For example, for the following index that stores pre-aggregated histograms with latency metrics for different networks:

```console
PUT metrics_index
{
  "mappings": {
    "properties": {
      "latency_histo": { "type": "histogram" }
    }
  }
}

PUT metrics_index/_doc/1?refresh
{
  "network.name" : "net-1",
  "latency_histo" : {
      "values" : [0.1, 0.2, 0.3, 0.4, 0.5],
      "counts" : [3, 7, 23, 12, 6]
   }
}

PUT metrics_index/_doc/2?refresh
{
  "network.name" : "net-2",
  "latency_histo" : {
      "values" :  [0.1, 0.2, 0.3, 0.4, 0.5],
      "counts" : [8, 17, 8, 7, 6]
   }
}

POST /metrics_index/_search?size=0&filter_path=aggregations
{
  "aggs" : {
    "max_latency" : { "max" : { "field" : "latency_histo" } }
  }
}
```

The `max` aggregation will return the maximum value of all histogram fields:

```console-result
{
  "aggregations": {
    "max_latency": {
      "value": 0.5
    }
  }
}
```
