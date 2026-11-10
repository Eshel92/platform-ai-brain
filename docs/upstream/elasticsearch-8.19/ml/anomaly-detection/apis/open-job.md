<!-- Converted from ml/anomaly-detection/apis/open-job.asciidoc (AsciiDoc). Includes are inlined. -->

# Open anomaly detection jobs API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Opens one or more anomaly detection jobs.

## Request

`POST _ml/anomaly_detectors/{job_id}/_open`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

An anomaly detection job must be opened in order for it to be ready to receive and
analyze data. It can be opened and closed multiple times throughout its
lifecycle.

When you open a new job, it starts with an empty model.

When you open an existing job, the most recent model state is automatically
loaded. The job is ready to resume its analysis from where it left off, once new
data is received.

## Path parameters

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job.

## Query parameters

`timeout`::
(Optional, time) Controls the time to wait until a job has opened. The default
value is 30 minutes.

## Request body

You can also specify the `timeout` query parameter in the request body.

## Response body

`node`::
  (string) The ID of the node that the job was opened on. If the job is allowed to 
open lazily and has not yet been assigned to a node, this value is an empty string.

`opened`::
  (Boolean) For a successful response, this value is always `true`. On failure, an
  exception is returned instead.

## Examples

```console
POST _ml/anomaly_detectors/low_request_rate/_open
{
  "timeout": "35m"
}
```

When the job opens, you receive the following results:

```console-result
{
  "opened" : true,
  "node" : "node-1"
}
```
