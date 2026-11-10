<!-- Converted from ml/trained-models/apis/get-trained-models-stats.asciidoc (AsciiDoc). Includes are inlined. -->

# Get trained models statistics API

**New API reference**
For the most up-to-date API details, refer to [Machine learning trained model APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-trained-model).

Retrieves usage information for trained models.

## Request

`GET _ml/trained_models/_stats` +

`GET _ml/trained_models/_all/_stats` +

`GET _ml/trained_models/<model_id_or_deployment_id>/_stats` +

`GET _ml/trained_models/<model_id_or_deployment_id>,<model_id_2_or_deployment_id_2>/_stats` +

`GET _ml/trained_models/<model_id_pattern*_or_deployment_id_pattern*>,<model_id_2_or_deployment_id_2>/_stats`

## Prerequisites

Requires the `monitor_ml` cluster privilege. This privilege is included in the
`machine_learning_user` built-in role.

## Description

You can get usage information for multiple trained models or trained model 
deployments in a single API request by using a comma-separated list of model 
IDs, deployment IDs, or a wildcard expression.

## Path parameters

`<model_id_or_deployment_id>`::
(Optional, string)
The unique identifier of the model or the deployment. If a model has multiple 
deployments, and the ID of one of the deployments matches the model ID, then the 
model ID takes precedence; the results are returned for all deployments of the 
model.

## Query parameters

`allow_no_match`::
(Optional, Boolean)
Specifies what to do when the request:
* Contains wildcard expressions and there are no models that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty array when there are no
matches and the subset of results when there are partial matches. If this
parameter is `false`, the request returns a `404` status code when there are no
matches or only partial matches.
`from`::
(Optional, integer)
Skips the specified number of models. The default value is `0`.
`size`::
(Optional, integer)
Specifies the maximum number of models to obtain. The default value
is `100`.

## Response body

`count`::
(integer)
The total number of trained model statistics that matched the requested ID
patterns. Could be higher than the number of items in the `trained_model_stats`
array as the size of the array is restricted by the supplied `size` parameter.

`trained_model_stats`::
(array)
An array of trained model statistics, which are sorted by the `model_id` value
in ascending order.
**Properties of trained model stats**
`deployment_stats`:::
(list)
A collection of deployment stats if one of the provided `model_id` values
is deployed
**Properties of deployment stats**
=====
`allocation_status`:::
(object)
The detailed allocation status given the deployment configuration.
**Properties of allocation stats**
======
`allocation_count`:::
(integer)
The current number of nodes where the model is allocated.

`cache_size`:::
(byte value)
The inference cache size (in memory outside the JVM heap) per node for the model.

`state`:::
(string)
The detailed allocation state related to the nodes.
* `starting`: Allocations are being attempted but no node currently has the model allocated.
* `started`: At least one node has the model allocated.
* `fully_allocated`: The deployment is fully allocated and satisfies the `target_allocation_count`.

`target_allocation_count`:::
(integer)
The desired number of nodes for model allocation.
======

`deployment_id`:::
A unique identifier for the deployment of the model.
`error_count`:::
(integer)
The sum of `error_count` for all nodes in the deployment.

`inference_count`:::
(integer)
The sum of `inference_count` for all nodes in the deployment.

`model_id`:::
(string)
The unique identifier of the trained model.
`nodes`:::
(array of objects)
The deployment stats for each node that currently has the model allocated.
**Properties of node stats**
======
`average_inference_time_ms`:::
(double)
The average time for each inference call to complete on this node.
The average is calculated over the lifetime of the deployment.

`average_inference_time_ms_excluding_cache_hits`:::
(double)
The average time to perform inference on the trained model excluding
occasions where the response comes from the cache. Cached inference
calls return very quickly as the model is not evaluated, by excluding
cache hits this value is an accurate measure of the average time taken
to evaluate the model.

`average_inference_time_ms_last_minute`:::
(double)
The average time for each inference call to complete on this node
in the last minute.

`error_count`:::
(integer)
The number of errors when evaluating the trained model.

`inference_cache_hit_count`:::
(integer)
The total number of inference calls made against this node for this
model that were served from the inference cache.

`inference_cache_hit_count_last_minute`:::
(integer)
The number of inference calls made against this node for this model
in the last minute that were served from the inference cache.

`inference_count`:::
(integer)
The total number of inference calls made against this node for this model.

`last_access`:::
(long)
The epoch time stamp of the last inference call for the model on this node.

`node`:::
(object)
Information pertaining to the node.
**Properties of node**
========
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
(string) The node name.

`transport_address`:::
(string)
The host and port where transport HTTP connections are accepted.
========

`number_of_allocations`:::
(integer)
The number of allocations assigned to this node.

`number_of_pending_requests`:::
(integer)
The number of inference requests queued to be processed.

`peak_throughput_per_minute`:::
(integer)
The peak number of requests processed in a 1 minute period.

`routing_state`:::
(object)
The current routing state and reason for the current routing state for this allocation.
**Properties of routing_state**
========
`reason`:::
(string)
The reason for the current state. Usually only populated when the `routing_state` is `failed`.

`routing_state`:::
(string)
The current routing state.
* `starting`: The model is attempting to allocate on this model, inference calls are not yet accepted.
* `started`: The model is allocated and ready to accept inference requests.
* `stopping`: The model is being deallocated from this node.
* `stopped`: The model is fully deallocated from this node.
* `failed`: The allocation attempt failed, see `reason` field for the potential cause.
========

`rejected_execution_count`:::
(integer)
The number of inference requests that were not processed because the
queue was full.

`start_time`:::
(long)
The epoch timestamp when the allocation started.

`threads_per_allocation`:::
(integer)
The number of threads for each allocation during inference.
This value is limited by the number of hardware threads on the node;
it might therefore differ from the `threads_per_allocation` value in the start-trained-model-deployment API.

`timeout_count`:::
(integer)
The number of inference requests that timed out before being processed.

`throughput_last_minute`:::
(integer)
The number of requests processed in the last 1 minute.
======

`number_of_allocations`:::
(integer)
The requested number of allocations for the trained model deployment.

`peak_throughput_per_minute`:::
(integer)
The peak number of requests processed in a 1 minute period for
all nodes in the deployment. This is calculated as the sum of
each node's `peak_throughput_per_minute` value.

`priority`:::
(string)
The deployment priority.

`rejected_execution_count`:::
(integer)
The sum of `rejected_execution_count` for all nodes in the deployment.
Individual nodes reject an inference request if the inference queue is full.
The queue size is controlled by the `queue_capacity` setting in the
start-trained-model-deployment API.

`reason`:::
(string)
The reason for the current deployment state.
Usually only populated when the model is not deployed to a node.

`start_time`:::
(long)
The epoch timestamp when the deployment started.

`state`:::
(string)
The overall state of the deployment. The values may be:
* `starting`: The deployment has recently started but is not yet usable as the model is not allocated on any nodes.
* `started`: The deployment is usable as at least one node has the model allocated.
* `stopping`: The deployment is preparing to stop and deallocate the model from the relevant nodes.

`threads_per_allocation`:::
(integer)
The number of threads per allocation used by the inference process.

`timeout_count`:::
(integer)
The sum of `timeout_count` for all nodes in the deployment.

`queue_capacity`:::
(integer)
The number of inference requests that may be queued before new requests are
rejected.

=====

`inference_stats`:::
(object)
A collection of inference stats fields.
**Properties of inference stats**
=====

`missing_all_fields_count`:::
(integer)
The number of inference calls where all the training features for the model
were missing.

`inference_count`:::
(integer)
The total number of times the model has been called for inference.
This is across all inference contexts, including all pipelines.

`cache_miss_count`:::
(integer)
The number of times the model was loaded for inference and was not retrieved
from the cache. If this number is close to the `inference_count`, then the cache
is not being appropriately used. This can be solved by increasing the cache size
or its time-to-live (TTL). See general-ml-settings for the appropriate
settings.

`failure_count`:::
(integer)
The number of failures when using the model for inference.

`timestamp`:::
(time units)
The time when the statistics were last updated.
=====

`ingest`:::
(object)
A collection of ingest stats for the model across all nodes. The values are
summations of the individual node statistics. The format matches the `ingest`
section in cluster-nodes-stats.

`model_id`:::
(string)
The unique identifier of the trained model.
`model_size_stats`:::
(object)
A collection of model size stats fields.
**Properties of model size stats**
=====

`model_size_bytes`:::
(integer)
The size of the model in bytes.
This parameter applies only to PyTorch models.

`required_native_memory_bytes`:::
(integer)
The amount of memory required to load the model in bytes.
=====

`pipeline_count`:::
(integer)
The number of ingest pipelines that currently refer to the model.

## Response codes

`404` (Missing resources)::
  If `allow_no_match` is `false`, this code indicates that there are no
  resources that match the request or only partial matches for the request.

## Examples

The following example gets usage information for all the trained models:

```console
GET _ml/trained_models/_stats
```

The API returns the following results:

```console-result
{
  "count": 2,
  "trained_model_stats": [
    {
      "model_id": "flight-delay-prediction-1574775339910",
      "pipeline_count": 0,
      "inference_stats": {
        "failure_count": 0,
        "inference_count": 4,
        "cache_miss_count": 3,
        "missing_all_fields_count": 0,
        "timestamp": 1592399986979
      }
    },
    {
      "model_id": "regression-job-one-1574775307356",
      "pipeline_count": 1,
      "inference_stats": {
        "failure_count": 0,
        "inference_count": 178,
        "cache_miss_count": 3,
        "missing_all_fields_count": 0,
        "timestamp": 1592399986979
      },
      "ingest": {
        "total": {
          "count": 178,
          "time_in_millis": 8,
          "current": 0,
          "failed": 0
        },
        "pipelines": {
          "flight-delay": {
            "count": 178,
            "time_in_millis": 8,
            "current": 0,
            "failed": 0,
            "processors": [
              {
                "inference": {
                  "type": "inference",
                  "stats": {
                    "count": 178,
                    "time_in_millis": 7,
                    "current": 0,
                    "failed": 0
                  }
                }
              }
            ]
          }
        }
      }
    }
  ]
}
```
