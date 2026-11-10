<!-- Converted from ml/anomaly-detection/apis/reset-job.asciidoc (AsciiDoc). Includes are inlined. -->

# Reset anomaly detection jobs API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Resets an existing anomaly detection job.

## Request

`POST _ml/anomaly_detectors/<job_id>/_reset`

## Prerequisites

* Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.
* Before you can reset a job, you must close it. You can set `force` to `true`
when closing the job to avoid waiting for the job to complete. See 
ml-close-job.

## Description

All model state and results are deleted.
The job is ready to start over as if it had just been created.

It is not currently possible to reset multiple jobs using wildcards or a comma
separated list.

## Path parameters

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job.

## Query parameters

`wait_for_completion`::
  (Optional, Boolean) Specifies whether the request should return immediately or
  wait until the job reset completes. Defaults to `true`.

`delete_user_annotations`::
  (Optional, Boolean) Specifies whether annotations that have been added by the 
  user should be deleted along with any auto-generated annotations when the job is
  reset. Defaults to `false`.

## Examples

```console
POST _ml/anomaly_detectors/total-requests/_reset
```

When the job is reset, you receive the following results:

```console-result
{
  "acknowledged": true
}
```

In the next example we reset the `total-requests` job asynchronously:

```console
POST _ml/anomaly_detectors/total-requests/_reset?wait_for_completion=false
```

When `wait_for_completion` is set to `false`, the response contains the id
of the job reset task:

```console-result
{
  "task": "oTUltX4IQMOUUVeiohTt8A:39"
}
```

If you want to check the status of the reset task, use the tasks by referencing 
the task ID.
