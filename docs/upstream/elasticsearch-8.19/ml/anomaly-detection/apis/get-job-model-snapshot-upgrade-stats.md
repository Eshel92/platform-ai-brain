<!-- Converted from ml/anomaly-detection/apis/get-job-model-snapshot-upgrade-stats.asciidoc (AsciiDoc). Includes are inlined. -->

# Get anomaly detection job model snapshot upgrade statistics API

**New API reference**
For the most up-to-date API details, refer to [Machine learning  anomaly detection APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-anomaly).

Retrieves usage information for anomaly detection job model snapshot upgrades.

## Request

`GET _ml/anomaly_detectors/<job_id>/model_snapshots/<snapshot_id>/_upgrade/_stats` +

`GET _ml/anomaly_detectors/<job_id>,<job_id>/model_snapshots/_all/_upgrade/_stats` +

`GET _ml/anomaly_detectors/_all/model_snapshots/_all/_upgrade/_stats`

## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the
`machine_learning_user` built-in role.

## Description

{anomaly-detect-cap} job model snapshot upgrades are ephemeral. Only
upgrades that are in progress at the time this API is called will be
returned.

## Path parameters

`<job_id>`::
(string)
Identifier for the anomaly detection job. It can be a job identifier, a group name, or a
wildcard expression.
`<snapshot_id>`::
(string)
Identifier for the model snapshot.
You can get statistics for multiple anomaly detection job model snapshot upgrades in a
single API request by using a comma-separated list of snapshot IDs. You can also
use wildcard expressions or `_all`.

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

## Response body

The API returns an array of anomaly detection job model snapshot upgrade status objects.
All of these properties are informational; you cannot update their values.

`assignment_explanation`::
(string)
For started datafeeds only, contains messages relating to the selection of a
node.
`job_id`::
(string)
Identifier for the anomaly detection job.
`node`::
(object)
Contains properties for the node that runs the upgrade task. This information is
available only for upgrade tasks that are assigned to a node.
`attributes`:::
(object)
Lists node attributes such as `ml.machine_memory` or `ml.max_open_jobs` settings.
`ephemeral_id`:::
(string)
The ephemeral ID of the node.
`id`:::
(string)
The unique identifier of the node.
`name`:::
(string)
The node name. For example, `0-o0tOo`.

`transport_address`:::
(string)
The host and port where transport HTTP connections are accepted.

`snapshot_id`::
(string)
A numerical character string that uniquely identifies the model snapshot. For
example, `1575402236000`.
`state`::
(string)
One of `loading_old_state`, `saving_new_state`, `stopped` or `failed`.

## Response codes

`404` (Missing resources)::
  If `allow_no_match` is `false`, this code indicates that there are no
  resources that match the request or only partial matches for the request.

## Examples

```console
GET _ml/anomaly_detectors/low_request_rate/model_snapshots/_all/_upgrade/_stats
```

The API returns the following results:

```console-result
{
  "count" : 1,
  "model_snapshot_upgrades" : [
    {
      "job_id" : "low_request_rate",
      "snapshot_id" : "1828371",
      "state" : "saving_new_state",
      "node" : {
        "id" : "7bmMXyWCRs-TuPfGJJ_yMw",
        "name" : "node-0",
        "ephemeral_id" : "hoXMLZB0RWKfR9UPPUCxXX",
        "transport_address" : "127.0.0.1:9300",
        "attributes" : {
          "ml.machine_memory" : "17179869184",
          "ml.max_open_jobs" : "512"
        }
      },
      "assignment_explanation" : ""
    }
  ]
}
```
