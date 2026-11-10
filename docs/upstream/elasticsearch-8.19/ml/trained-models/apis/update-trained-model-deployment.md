<!-- Converted from ml/trained-models/apis/update-trained-model-deployment.asciidoc (AsciiDoc). Includes are inlined. -->

# Update trained model deployment API

**New API reference**
For the most up-to-date API details, refer to [Machine learning trained model APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-trained-model).

Updates certain properties of a trained model deployment.

## Request

`POST _ml/trained_models/<deployment_id>/deployment/_update`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the
`machine_learning_admin` built-in role.

## Description

You can update a trained model deployment whose `assignment_state` is `started`.
You can enable adaptive allocations to automatically scale model allocations up
and down based on the actual resource requirement of the processes.
Or you can manually increase or decrease the number of allocations of a model
deployment.

## Path parameters

`<deployment_id>`::
(Required, string)
A unique identifier for the deployment of the model.

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
`number_of_allocations`::
(Optional, integer)
The total number of allocations this model is assigned across machine learning nodes.
Increasing this value generally increases the throughput.
If `adaptive_allocations` is enabled, do not set this value, because it's automatically set.

## Examples

The following example updates the deployment for a
`elastic__distilbert-base-uncased-finetuned-conll03-english` trained model to have 4 allocations:

```console
POST _ml/trained_models/elastic__distilbert-base-uncased-finetuned-conll03-english/deployment/_update
{
  "number_of_allocations": 4
}
```

The API returns the following results:

```console-result
{
    "assignment": {
        "task_parameters": {
            "model_id": "elastic__distilbert-base-uncased-finetuned-conll03-english",
            "model_bytes": 265632637,
            "threads_per_allocation" : 1,
            "number_of_allocations" : 4,
            "queue_capacity" : 1024
        },
        "routing_table": {
            "uckeG3R8TLe2MMNBQ6AGrw": {
                "current_allocations": 1,
                "target_allocations": 4,
                "routing_state": "started",
                "reason": ""
            }
        },
        "assignment_state": "started",
        "start_time": "2022-11-02T11:50:34.766591Z"
    }
}
```

The following example updates the deployment for a
`elastic__distilbert-base-uncased-finetuned-conll03-english` trained model to
enable adaptive allocations with the minimum number of 3 allocations and the
maximum number of 10:

```console
POST _ml/trained_models/elastic__distilbert-base-uncased-finetuned-conll03-english/deployment/_update
{
  "adaptive_allocations": {
    "enabled": true,
    "min_number_of_allocations": 3,
    "max_number_of_allocations": 10
  }
}
```
