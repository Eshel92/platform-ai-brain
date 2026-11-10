<!-- Converted from ml/anomaly-detection/apis/delete-job.asciidoc (AsciiDoc). Includes are inlined. -->

# Delete anomaly detection jobs API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Deletes an existing anomaly detection job.

## Request

`DELETE _ml/anomaly_detectors/<job_id>`

## Prerequisites

* Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.
* Before you can delete a job, you must close it (unless you specify the `force` 
parameter). See ml-close-job.

## Description

All job configuration, model state and results are deleted.

**Important:** Deleting an anomaly detection job must be done via this API only. Do not
delete the job directly from the `.ml-*` indices using the Elasticsearch delete document
API. When Elasticsearch security features are enabled, make sure no `write` privileges
are granted to anyone over the `.ml-*` indices.

It is not currently possible to delete multiple jobs using wildcards or a comma
separated list.

If you delete a job that has a datafeed, the request first tries to delete the
datafeed. This behavior is equivalent to calling
delete datafeed with the same `timeout` and `force`
parameters as the delete job request.

## Path parameters

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job.

## Query parameters

`force`::
  (Optional, Boolean) Use to forcefully delete an opened job; this method is
  quicker than closing and deleting the job.

`wait_for_completion`::
  (Optional, Boolean) Specifies whether the request should return immediately or
  wait until the job deletion completes. Defaults to `true`.

`delete_user_annotations`::
  (Optional, Boolean) Specifies whether annotations that have been added by the 
  user should be deleted along with any auto-generated annotations when the job is
  reset. Defaults to `false`.

## Examples

```console
DELETE _ml/anomaly_detectors/total-requests
```

When the job is deleted, you receive the following results:

```console-result
{
  "acknowledged": true
}
```

In the next example we delete the `total-requests` job asynchronously:

```console
DELETE _ml/anomaly_detectors/total-requests?wait_for_completion=false
```

When `wait_for_completion` is set to `false`, the response contains the id
of the job deletion task:

```console-result
{
  "task": "oTUltX4IQMOUUVeiohTt8A:39"
}
```
