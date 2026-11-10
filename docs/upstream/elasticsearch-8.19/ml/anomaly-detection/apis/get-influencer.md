<!-- Converted from ml/anomaly-detection/apis/get-influencer.asciidoc (AsciiDoc). Includes are inlined. -->

# Get influencers API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Retrieves anomaly detection job results for one or more influencers.

## Request

`GET _ml/anomaly_detectors/<job_id>/results/influencers`

## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the 
`machine_learning_user` built-in role.`

## Description

Influencers are the entities that have contributed to, or are to blame for,
the anomalies. Influencer results are available only if an
`influencer_field_name` is specified in the job configuration.

## Path parameters

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job.

## Query parameters

`desc`::
(Optional, Boolean)
If true, the results are sorted in descending order.
`end`::
(Optional, string) Returns influencers with timestamps earlier than this time.
Defaults to `-1`, which means it is unset and results are not limited to 
specific timestamps.

`exclude_interim`::
(Optional, Boolean)
If `true`, the output excludes interim results. Defaults to `false`, which means interim results are included.
`from`::
(Optional, integer)
Skips the specified number of influencers. Defaults to `0`.

`influencer_score`::
(Optional, double) Returns influencers with anomaly scores greater than or
equal to this value. Defaults to `0.0`.

`size`::
(Optional, integer)
Specifies the maximum number of influencers to obtain. Defaults to `100`.

`sort`::
(Optional, string) Specifies the sort field for the requested influencers. By
default, the influencers are sorted by the `influencer_score` value.

`start`::
(Optional, string) Returns influencers with timestamps after this time. Defaults 
to `-1`, which means it is unset and results are not limited to specific 
timestamps.

## Request body

You can also specify the query parameters in the request body; the exception are
`from` and `size`, use `page` instead:

`page`::
**Properties of `page`**

`from`:::
(Optional, integer) Skips the specified number of influencers. Defaults to `0`.

`size`:::
(Optional, integer) Specifies the maximum number of influencers to obtain. 
Defaults to `100`.

## Response body

The API returns an array of influencer objects, which have the following
properties:

`bucket_span`::
(number)
The length of the bucket in seconds. This value matches the `bucket_span`
that is specified in the job.
`influencer_score`::
(number) A normalized score between 0-100, which is based on the probability of
the influencer in this bucket aggregated across detectors. Unlike
`initial_influencer_score`, this value will be updated by a re-normalization
process as new data is analyzed.

`influencer_field_name`::
(string) The field name of the influencer.

`influencer_field_value`::
(string) The entity that influenced, contributed to, or was to blame for the
anomaly.

`initial_influencer_score`::
(number) A normalized score between 0-100, which is based on the probability of
the influencer aggregated across detectors. This is the initial value that was
calculated at the time the bucket was processed.

`is_interim`::
(Boolean)
If `true`, this is an interim result. In other words, the results are calculated
based on partial input data.
`job_id`::
(string)
Identifier for the anomaly detection job.
`probability`::
(number) The probability that the influencer has this behavior, in the range 0
to 1. For example, 0.0000109783. This value can be held to a high precision of
over 300 decimal places, so the `influencer_score` is provided as a
human-readable and friendly interpretation of this.

`result_type`::
(string) Internal. This value is always set to `influencer`.

`timestamp`::
(date)
The start time of the bucket for which these results were calculated.
**Note:** Additional influencer properties are added, depending on the fields being
analyzed. For example, if it's analyzing `user_name` as an influencer, then a
field `user_name` is added to the result document. This information enables you to
filter the anomaly results more easily.

## Examples

```console
GET _ml/anomaly_detectors/high_sum_total_sales/results/influencers
{
  "sort": "influencer_score",
  "desc": true
}
```

In this example, the API returns the following information, sorted based on the
influencer score in descending order:
```js
{
  "count": 189,
  "influencers": [
    {
      "job_id": "high_sum_total_sales",
      "result_type": "influencer",
      "influencer_field_name": "customer_full_name.keyword",
      "influencer_field_value": "Wagdi Shaw",
      "customer_full_name.keyword" : "Wagdi Shaw",
      "influencer_score": 99.02493,
      "initial_influencer_score" : 94.67233079580171,
      "probability" : 1.4784807245686567E-10,
      "bucket_span" : 3600,
      "is_interim" : false,
      "timestamp" : 1574661600000
    },
  ...
  ]
}
```
