<!-- Converted from ml/anomaly-detection/apis/close-job.asciidoc (AsciiDoc). Includes are inlined. -->

# Close anomaly detection jobs API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Closes one or more anomaly detection jobs.

## Request

`POST _ml/anomaly_detectors/<job_id>/_close` +

`POST _ml/anomaly_detectors/<job_id>,<job_id>/_close` +

`POST _ml/anomaly_detectors/_all/_close` +

## Prerequisites

* Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

A job can be opened and closed multiple times throughout its lifecycle.

A closed job cannot receive data or perform analysis operations, but you can
still explore and navigate results.

If you close an anomaly detection job whose datafeed is running, the request first tries
to stop the datafeed. This behavior is equivalent to calling
stop datafeed with the same `timeout` and `force` parameters
as the close job request.

When you close a job, it runs housekeeping tasks such as pruning the model history,
flushing buffers, calculating final results and persisting the model snapshots.
Depending upon the size of the job, it could take several minutes to close and
the equivalent time to re-open.

After it is closed, the job has a minimal overhead on the cluster except for
maintaining its metadata. Therefore it is a best practice to close jobs that
are no longer required to process data.

When a datafeed that has a specified end date stops, it automatically closes
its associated job.

**Note:** If you use the `force` query parameter, the request returns without performing
the associated actions such as flushing buffers and persisting the model snapshots.
Therefore, do not use this parameter if you want the job to be in a consistent state
after the close job API returns. The `force` query parameter should only be used in
situations where the job has already failed, or where you are not interested in
results the job might have recently produced or might produce in the future.

## Path parameters

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job. It can be a job identifier, a group name, or a
wildcard expression.
You can close all jobs by using `_all` or by specifying `*` as the job
identifier.

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
`force`::
  (Optional, Boolean) Use to close a failed job, or to forcefully close a job
  which has not responded to its initial close request.

`timeout`::
  (Optional, time units) Controls the time to wait until a job 
  has closed. The default value is 30 minutes.

## Request body

You can also specify the query parameters (such as `allow_no_match` and `force`)
in the request body.

## Response codes

`404` (Missing resources)::
  If `allow_no_match` is `false`, this code indicates that there are no 
  resources that match the request or only partial matches for the request.

## Examples

```console
POST _ml/anomaly_detectors/low_request_rate/_close
```

When the job is closed, you receive the following results:

```console-result
{
  "closed": true
}
```
