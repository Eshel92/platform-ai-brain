<!-- Converted from ml/trained-models/apis/start-trained-model-deployment.asciidoc (AsciiDoc). Includes are inlined. -->

# Start trained model deployment API

**New API reference**
For the most up-to-date API details, refer to [Machine learning trained model APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-trained-model).

Starts a new trained model deployment.

## Request

`POST _ml/trained_models/<model_id>/deployment/_start`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the
`machine_learning_admin` built-in role.

## Description

Currently only `pytorch` models are supported for deployment. Once deployed
the model can be used by the {infer-cap} processor
in an ingest pipeline or directly in the infer-trained-model API.

A model can be deployed multiple times by using deployment IDs. A deployment ID
must be unique and should not match any other deployment ID or model ID, unless
it is the same as the ID of the model being deployed. If `deployment_id` is not
set, it defaults to the `model_id`.

You can enable adaptive allocations to automatically scale model allocations up
and down based on the actual resource requirement of the processes.

Manually scaling inference performance can be achieved by setting the parameters
`number_of_allocations` and `threads_per_allocation`.

Increasing `threads_per_allocation` means more threads are used when an
inference request is processed on a node. This can improve inference speed for
certain models. It may also result in improvement to throughput.

Increasing `number_of_allocations` means more threads are used to process
multiple inference requests in parallel resulting in throughput improvement.
Each model allocation uses a number of threads defined by
`threads_per_allocation`.

Model allocations are distributed across machine learning nodes. All allocations assigned to
a node share the same copy of the model in memory. To avoid thread
oversubscription which is detrimental to performance, model allocations are
distributed in such a way that the total number of used threads does not surpass
the node's allocated processors.

## Path parameters

`<model_id>`::
(Required, string)
The unique identifier of the trained model.

## Query parameters

`deployment_id`::
(Optional, string)
A unique identifier for the deployment of the model.
Defaults to `model_id`.

`timeout`::
(Optional, time)
Controls the amount of time to wait for the model to deploy. Defaults to 30
seconds.

`wait_for`::
(Optional, string)
Specifies the allocation status to wait for before returning. Defaults to
`started`. The value `starting` indicates deployment is starting but not yet on
any node. The value `started` indicates the model has started on at least one
node. The value `fully_allocated` indicates the deployment has started on all
valid nodes.

## Request body

`adaptive_allocations`::
(Optional, object)
Adaptive allocations configuration object.
If enabled, the number of allocations of the model is set based on the current load the process gets.
When the load is high, a new model allocation is automatically created (respecting the value of `max_number_of_allocations` if it's set).
When the load is low, a model allocation is automatically removed (respecting the value of `min_number_of_allocations` if it's set).
If `adaptive_allocations` is enabled, do not set the number of allocations manually.
`enabled`:::
(Optional, Boolean)
If `true`, `adaptive_allocations` is enabled.
Defaults to `false`.
`max_number_of_allocations`:::
(Optional, integer)
Specifies the maximum number of allocations to scale to.
If set, it must be greater than or equal to `min_number_of_allocations`.
`min_number_of_allocations`:::
(Optional, integer)
Specifies the minimum number of allocations to scale to.
If set, it must be greater than or equal to `0`.
If not defined, the deployment scales to `0`.
`cache_size`::
(Optional, byte value)
The inference cache size (in memory outside the JVM heap) per node for the
model. In serverless, the cache is disabled by default. Otherwise, the default value is the size of the model as reported by the
`model_size_bytes` field in the get-trained-models-stats. To disable the
cache, `0b` can be provided.

`number_of_allocations`::
(Optional, integer)
The total number of allocations this model is assigned across machine learning nodes.
Increasing this value generally increases the throughput. Defaults to `1`.
If `adaptive_allocations` is enabled, do not set this value, because it's automatically set.

`priority`::
(Optional, string)
The priority of the deployment. The default value is `normal`.
There are two priority settings:
* `normal`: Use this for deployments in production. The deployment allocations
are distributed so that node processors are not oversubscribed.
* `low`: Use this for testing model functionality. The intention is that these
deployments are not sent a high volume of input. The deployment is required to
have a single allocation with just one thread. Low priority deployments may be
assigned on nodes that already utilize all their processors but will be given a
lower CPU priority than normal deployments. Low priority deployments may be
unassigned in order to satisfy more allocations of normal priority deployments.

**Warning:** Heavy usage of low priority deployments may impact performance of
normal priority deployments.

`queue_capacity`::
(Optional, integer)
Controls how many inference requests are allowed in the queue at a time.
Every machine learning node in the cluster where the model can be allocated
has a queue of this size; when the number of requests exceeds the total value,
new requests are rejected with a 429 error. Defaults to 10000. Max allowed value
is 100000.

`threads_per_allocation`::
(Optional, integer)
Sets the number of threads used by each model allocation during inference. This
generally increases the speed per inference request. The inference process is a
compute-bound process; `threads_per_allocations` must not exceed the number of
available allocated processors per node. Defaults to 1. Must be a power of 2.
Max allowed value is 32.

## Examples

The following example starts a new deployment for a
`elastic__distilbert-base-uncased-finetuned-conll03-english` trained model:

```console
POST _ml/trained_models/elastic__distilbert-base-uncased-finetuned-conll03-english/deployment/_start?wait_for=started&timeout=1m
```

The API returns the following results:

```console-result
{
    "assignment": {
        "task_parameters": {
            "model_id": "elastic__distilbert-base-uncased-finetuned-conll03-english",
            "model_bytes": 265632637,
            "threads_per_allocation" : 1,
            "number_of_allocations" : 1,
            "queue_capacity" : 10000,
            "priority": "normal"
        },
        "routing_table": {
            "uckeG3R8TLe2MMNBQ6AGrw": {
                "routing_state": "started",
                "reason": ""
            }
        },
        "assignment_state": "started",
        "start_time": "2022-11-02T11:50:34.766591Z"
    }
}
```

### Using deployment IDs

The following example starts a new deployment for the `my_model` trained model
with the ID `my_model_for_ingest`. The deployment ID an be used in inference API
calls or in inference processors.

```console
POST _ml/trained_models/my_model/deployment/_start?deployment_id=my_model_for_ingest
```

The `my_model` trained model can be deployed again with a different ID:

```console
POST _ml/trained_models/my_model/deployment/_start?deployment_id=my_model_for_search
```

### Setting adaptive allocations

The following example starts a new deployment of the `my_model` trained model
with the ID `my_model_for_search` and enables adaptive allocations with the
minimum number of 3 allocations and the maximum number of 10. 

```console
POST _ml/trained_models/my_model/deployment/_start?deployment_id=my_model_for_search
{
  "adaptive_allocations": {
    "enabled": true,
    "min_number_of_allocations": 3,
    "max_number_of_allocations": 10
  }
}
```
