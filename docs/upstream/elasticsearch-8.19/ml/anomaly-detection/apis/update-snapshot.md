<!-- Converted from ml/anomaly-detection/apis/update-snapshot.asciidoc (AsciiDoc). Includes are inlined. -->

# Update model snapshots API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Updates certain properties of a snapshot.

## Request

`POST _ml/anomaly_detectors/<job_id>/model_snapshots/<snapshot_id>/_update`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Path parameters

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job.
`<snapshot_id>`::
(Required, string)
Identifier for the model snapshot.

## Request body

The following properties can be updated after the model snapshot is created:

`description`::
(Optional, string) A description of the model snapshot.

`retain`::
(Optional, Boolean)
If `true`, this snapshot will not be deleted during automatic cleanup of
snapshots older than `model_snapshot_retention_days`. However, this snapshot
will be deleted when the job is deleted. The default value is `false`.

## Examples

```console
POST
_ml/anomaly_detectors/it_ops_new_logs/model_snapshots/1491852978/_update
{
  "description": "Snapshot 1",
  "retain": true
}
```

When the snapshot is updated, you receive the following results:
```js
{
  "acknowledged": true,
  "model": {
    "job_id": "it_ops_new_logs",
    "timestamp": 1491852978000,
    "description": "Snapshot 1",
...
    "retain": true
  }
}
```
