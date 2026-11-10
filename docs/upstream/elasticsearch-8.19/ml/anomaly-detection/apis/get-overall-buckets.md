<!-- Converted from ml/anomaly-detection/apis/get-overall-buckets.asciidoc (AsciiDoc). Includes are inlined. -->

# Get overall buckets API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Retrieves overall bucket results that summarize the bucket results of multiple
anomaly detection jobs.

## Request

`GET _ml/anomaly_detectors/<job_id>/results/overall_buckets` +

`GET _ml/anomaly_detectors/<job_id>,<job_id>/results/overall_buckets` +

`GET _ml/anomaly_detectors/_all/results/overall_buckets`

## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the 
`machine_learning_user` built-in role.

## Description

By default, an overall bucket has a span equal to the largest bucket span of the
specified anomaly detection jobs. To override that behavior, use the optional
`bucket_span` parameter. To learn more about the concept of buckets, see
{ml-docs}/ml-buckets.html[Buckets].

The `overall_score` is calculated by combining the scores of all the buckets
within the overall bucket span. First, the maximum `anomaly_score` per
anomaly detection job in the overall bucket is calculated. Then the `top_n` of those
scores are averaged to result in the `overall_score`. This means that you can
fine-tune the `overall_score` so that it is more or less sensitive to the number
of jobs that detect an anomaly at the same time. For example, if you set `top_n`
to `1`, the `overall_score` is the maximum bucket score in the overall bucket.
Alternatively, if you set `top_n` to the number of jobs, the `overall_score` is
high only when all jobs detect anomalies in that overall bucket. If you set
the `bucket_span` parameter (to a value greater than its default), the
`overall_score` is the maximum `overall_score` of the overall buckets that have
a span equal to the jobs' largest bucket span.

## Path parameters

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job. It can be a job identifier, a group name, a
comma-separated list of jobs or groups, or a wildcard expression.
You can summarize the bucket results for all anomaly detection jobs by using `_all` or
by specifying `*` as the job identifier.

## Query parameters

`allow_no_match`::
(Optional, Boolean)
Specifies what to do when the request:
* Contains wildcard expressions and there are no jobs that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty `jobs` array
when there are no matches and the subset of results when there are partial
matches. If this parameter is `false`, the request returns a `404` status code
when there are no matches or only partial matches.
`bucket_span`::
(Optional, string) The span of the overall buckets. Must be greater or equal to
the largest bucket span of the specified anomaly detection jobs, which is the default
value.

`end`::
(Optional, string) Returns overall buckets with timestamps earlier than this
time. Defaults to `-1`, which means it is unset and results are not limited to 
specific timestamps.

`exclude_interim`::
(Optional, Boolean) If `true`, the output excludes interim overall buckets.
Overall buckets are interim if any of the job buckets within the overall bucket
interval are interim. Defaults to `false`, which means interim results are
included.

`overall_score`::
(Optional, double) Returns overall buckets with overall scores greater or equal
than this value. Defaults to `0.0`.

`start`::
(Optional, string) Returns overall buckets with timestamps after this time. 
Defaults to `-1`, which means it is unset and results are not limited to 
specific timestamps.

`top_n`::
(Optional, integer) The number of top anomaly detection job bucket scores to be used in
the `overall_score` calculation. Defaults to `1`.

## Request body

You can also specify the query parameters (such as `allow_no_match` and
`bucket_span`) in the request body.

## Response body

The API returns an array of overall bucket objects, which have the following
properties:

`bucket_span`::
(number) The length of the bucket in seconds. Matches the `bucket_span`
of the job with the longest one.

`is_interim`::
(Boolean)
If `true`, this is an interim result. In other words, the results are calculated
based on partial input data.
`jobs`::
(array) An array of objects that contain the `max_anomaly_score` per `job_id`.

`overall_score`::
(number) The `top_n` average of the max bucket `anomaly_score` per job.

`result_type`::
(string) Internal. This is always set to `overall_bucket`.

`timestamp`::
(date)
The start time of the bucket for which these results were calculated.

## Examples

```console
GET _ml/anomaly_detectors/job-*/results/overall_buckets
{
  "overall_score": 80,
  "start": "1403532000000"
}
```

In this example, the API returns a single result that matches the specified
score and time constraints. The `overall_score` is the max job score as
`top_n` defaults to 1 when not specified:
```js
{
  "count": 1,
  "overall_buckets": [
    {
      "timestamp" : 1403532000000,
      "bucket_span" : 3600,
      "overall_score" : 80.0,
      "jobs" : [
        {
          "job_id" : "job-1",
          "max_anomaly_score" : 30.0
        },
        {
          "job_id" : "job-2",
          "max_anomaly_score" : 10.0
        },
        {
          "job_id" : "job-3",
          "max_anomaly_score" : 80.0
        }
      ],
      "is_interim" : false,
      "result_type" : "overall_bucket"
    }
  ]
}
```

The next example is similar but this time `top_n` is set to `2`:

```console
GET _ml/anomaly_detectors/job-*/results/overall_buckets
{
  "top_n": 2,
  "overall_score": 50.0,
  "start": "1403532000000"
}
```

Note how the `overall_score` is now the average of the top 2 job scores:
```js
{
  "count": 1,
  "overall_buckets": [
    {
      "timestamp" : 1403532000000,
      "bucket_span" : 3600,
      "overall_score" : 55.0,
      "jobs" : [
        {
          "job_id" : "job-1",
          "max_anomaly_score" : 30.0
        },
        {
          "job_id" : "job-2",
          "max_anomaly_score" : 10.0
        },
        {
          "job_id" : "job-3",
          "max_anomaly_score" : 80.0
        }
      ],
      "is_interim" : false,
      "result_type" : "overall_bucket"
    }
  ]
}
```
