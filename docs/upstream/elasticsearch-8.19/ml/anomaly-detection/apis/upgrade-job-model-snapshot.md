<!-- Converted from ml/anomaly-detection/apis/upgrade-job-model-snapshot.asciidoc (AsciiDoc). Includes are inlined. -->

# Upgrade model snapshots API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Upgrades an anomaly detection model snapshot to the latest major version.

**Note:** From Elasticsearch 8.10.0,  a new version number is used to
track the configuration and state changes in the machine learning plugin. This new
version number is decoupled from the product version and will increment
independently.

## Request

`POST _ml/anomaly_detectors/<job_id>/model_snapshots/<snapshot_id>/_upgrade`

## Prerequisites

* Requires the `manage_ml` cluster privilege. This privilege is included in the
`machine_learning_admin` built-in role.
* The upgraded snapshot must have a version matching the previous major version.
* The upgraded snapshot must NOT be the current anomaly detection job snapshot.

## Description

Over time, older snapshot formats are deprecated and removed. {anomaly-jobs-cap}
support only snapshots that are from the current or previous major version.

This API provides a means to upgrade a snapshot to the current major version.
This aids in preparing the cluster for an upgrade to the next major version.

Only one snapshot per anomaly detection job can be upgraded at a time and the upgraded
snapshot cannot be the current snapshot of the anomaly detection job.

## Path parameters

`<job_id>`::
(Required, string)
Identifier for the anomaly detection job.
`<snapshot_id>`::
(Required, string)
Identifier for the model snapshot.

## Query parameters

`timeout`::
(Optional, time) Controls the time to wait for the request to complete. The
default value is 30 minutes.

`wait_for_completion`::
(Optional, boolean) When true, the API won't respond until the upgrade is
complete. Otherwise, it responds as soon as the upgrade task is assigned to a
node. Default is false.

## Response body

`node`::
  (string) The ID of the assigned node for the upgrade task if it is still running.

`completed`::
  (boolean) When true, this means the task is complete. When false, it is still running.

## Examples

```console
POST _ml/anomaly_detectors/low_request_rate/model_snapshots/1828371/_upgrade?timeout=45m&wait_for_completion=true
```

When the snapshot upgrade starts, you receive the following results:

```console-result
{
  "completed" : false,
  "node" : "node-1"
}
```
