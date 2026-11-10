<!-- Converted from ml/anomaly-detection/apis/flush-job.asciidoc (AsciiDoc). Includes are inlined. -->

# Flush jobs API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Forces any buffered data to be processed by the job.

## Request

`POST _ml/anomaly_detectors/<job_id>/_flush`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

The flush jobs API is only applicable when sending data for analysis using the
post data API. Depending on the content of the buffer, then it
might additionally calculate new results.

Both flush and close operations are similar, however the flush is more efficient
if you are expecting to send more data for analysis. When flushing, the job
remains open and is available to continue analyzing data. A close operation
additionally prunes and persists the model state to disk and the job must be
opened again before analyzing further data.

## Path parameters

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job.

## Query parameters

`advance_time`::
  (string) Optional. Specifies to advance to a particular time value. Results are
  generated and the model is updated for data from the specified time interval.

`calc_interim`::
  (Boolean) Optional. If true, calculates the interim results for the most
  recent bucket or all buckets within the latency period.

`end`::
  (string) Optional. When used in conjunction with `calc_interim` and `start`,
  specifies the range of buckets on which to calculate interim results.

`skip_time`::
  (string) Optional. Specifies to skip to a particular time value. Results are
  not generated and the model is not updated for data from the specified time
  interval.

`start`::
  (string) Optional. When used in conjunction with `calc_interim`, specifies the
  range of buckets on which to calculate interim results.

## Request body

You can also specify the query parameters (such as `advance_time` and
`calc_interim`) in the request body.

## Examples

```console
POST _ml/anomaly_detectors/low_request_rate/_flush
{
  "calc_interim": true
}
```

When the operation succeeds, you receive the following results:

```console-result
{
  "flushed": true,
  "last_finalized_bucket_end": 1455234900000
}
```

The `last_finalized_bucket_end` provides the timestamp (in
milliseconds-since-the-epoch) of the end of the last bucket that was processed.

If you want to flush the job to a specific timestamp, you can use the
`advance_time` or `skip_time` parameters. For example, to advance to 11 AM GMT
on January 1, 2018:

```console
POST _ml/anomaly_detectors/total-requests/_flush
{
  "advance_time": "1514804400000"
}
```

When the operation succeeds, you receive the following results:

```console-result
{
  "flushed": true,
  "last_finalized_bucket_end": 1514804400000
}
```
