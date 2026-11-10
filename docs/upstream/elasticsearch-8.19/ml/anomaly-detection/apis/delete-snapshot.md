<!-- Converted from ml/anomaly-detection/apis/delete-snapshot.asciidoc (AsciiDoc). Includes are inlined. -->

# Delete model snapshots API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Deletes an existing model snapshot.

## Request

`DELETE _ml/anomaly_detectors/<job_id>/model_snapshots/<snapshot_id>`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

**Important:** You cannot delete the active model snapshot. To delete that snapshot,
first revert to a different one. To identify the active model snapshot, refer to
the `model_snapshot_id` in the results from the get jobs API.

## Path parameters

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job.
`<snapshot_id>`::
(Required, string)
Identifier for the model snapshot.

## Examples

```console
DELETE _ml/anomaly_detectors/farequote/model_snapshots/1491948163
```

When the snapshot is deleted, you receive the following results:

```console-result
{
  "acknowledged": true
}
```
