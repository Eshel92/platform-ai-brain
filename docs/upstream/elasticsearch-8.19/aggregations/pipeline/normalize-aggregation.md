<!-- Converted from aggregations/pipeline/normalize-aggregation.asciidoc (AsciiDoc). Includes are inlined. -->

### Normalize aggregation

A parent pipeline aggregation which calculates the specific normalized/rescaled value for a specific bucket value.
Values that cannot be normalized, will be skipped using the skip gap policy.

#### Syntax

A `normalize` aggregation looks like this in isolation:

```js
{
  "normalize": {
    "buckets_path": "normalized",
    "method": "percent_of_sum"
  }
}
```

.`normalize_pipeline` Parameters
|===
|Parameter Name |Description |Required |Default Value
|`buckets_path` |The path to the buckets we wish to normalize (see `buckets_path` syntax for more details) |Required |
|`method` | The specific method to apply | Required |
|`format` |{javadoc}/java.base/java/text/DecimalFormat.html[DecimalFormat pattern] for the
output value. If specified, the formatted value is returned in the aggregation's
`value_as_string` property |Optional |`null`
|===

#### Methods

The Normalize Aggregation supports multiple methods to transform the bucket values. Each method definition will use
the following original set of bucket values as examples: `[5, 5, 10, 50, 10, 20]`.

_rescale_0_1_::
                This method rescales the data such that the minimum number is zero, and the maximum number is 1, with the rest normalized
                linearly in-between.

                x' = (x - min_x) / (max_x - min_x)

_rescale_0_100_::
                This method rescales the data such that the minimum number is zero, and the maximum number is 100, with the rest normalized
                linearly in-between.

                x' = 100 * (x - min_x) / (max_x - min_x)

_percent_of_sum_::
                This method normalizes each value so that it represents a percentage of the total sum it attributes to.

                x' = x / sum_x

_mean_::
                This method normalizes such that each value is normalized by how much it differs from the average.

                x' = (x - mean_x) / (max_x - min_x)

_z-score_::
                This method normalizes such that each value represents how far it is from the mean relative to the standard deviation

                x' = (x - mean_x) / stdev_x

_softmax_::
                This method normalizes such that each value is exponentiated and relative to the sum of the exponents of the original values.

                x' = e^x / sum_e_x

#### Example

The following snippet calculates the percent of total sales for each month:

```console
POST /sales/_search
{
  "size": 0,
  "aggs": {
    "sales_per_month": {
      "date_histogram": {
        "field": "date",
        "calendar_interval": "month"
      },
      "aggs": {
        "sales": {
          "sum": {
            "field": "price"
          }
        },
        "percent_of_total_sales": {
          "normalize": {
            "buckets_path": "sales",          <1>
            "method": "percent_of_sum",       <2>
            "format": "00.00%"                <3>
          }
        }
      }
    }
  }
}
```

<1> `buckets_path` instructs this normalize aggregation to use the output of the `sales` aggregation for rescaling
<2> `method` sets which rescaling to apply. In this case, `percent_of_sum` will calculate the sales value as a percent of all sales
    in the parent bucket
<3> `format` influences how to format the metric as a string using Java's `DecimalFormat` pattern. In this case, multiplying by 100
    and adding a '%'

And the following may be the response:

```console-result
{
   "took": 11,
   "timed_out": false,
   "_shards": ...,
   "hits": ...,
   "aggregations": {
      "sales_per_month": {
         "buckets": [
            {
               "key_as_string": "2015/01/01 00:00:00",
               "key": 1420070400000,
               "doc_count": 3,
               "sales": {
                  "value": 550.0
               },
               "percent_of_total_sales": {
                  "value": 0.5583756345177665,
                  "value_as_string": "55.84%"
               }
            },
            {
               "key_as_string": "2015/02/01 00:00:00",
               "key": 1422748800000,
               "doc_count": 2,
               "sales": {
                  "value": 60.0
               },
               "percent_of_total_sales": {
                  "value": 0.06091370558375635,
                  "value_as_string": "06.09%"
               }
            },
            {
               "key_as_string": "2015/03/01 00:00:00",
               "key": 1425168000000,
               "doc_count": 2,
               "sales": {
                  "value": 375.0
               },
               "percent_of_total_sales": {
                  "value": 0.38071065989847713,
                  "value_as_string": "38.07%"
               }
            }
         ]
      }
   }
}
```
