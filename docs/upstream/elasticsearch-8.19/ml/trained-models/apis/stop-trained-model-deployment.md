<!-- Converted from ml/trained-models/apis/stop-trained-model-deployment.asciidoc (AsciiDoc). Includes are inlined. -->

# Stop trained model deployment API

**New API reference**
For the most up-to-date API details, refer to [Machine learning trained model APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-trained-model).

Stops a trained model deployment.

## Request

`POST _ml/trained_models/<deployment_id>/deployment/_stop`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the
`machine_learning_admin` built-in role.

## Description

Deployment is required only for trained models that have a PyTorch `model_type`.

## Path parameters

`<deployment_id>`::
(Required, string)
A unique identifier for the deployment of the model.

## Query parameters

`allow_no_match`::
(Optional, Boolean)
Specifies what to do when the request:
* Contains wildcard expressions and there are no deployments that match.
* Contains the `_all` string or no identifiers and there are no matches.
* Contains wildcard expressions and there are only partial matches.

The default value is `true`, which returns an empty array when there are no
matches and the subset of results when there are partial matches. If this
parameter is `false`, the request returns a `404` status code when there are no
matches or only partial matches.
`force`::
(Optional, Boolean) If true, the deployment is stopped even if it or one of its
model aliases is referenced by ingest pipelines. You can't use these pipelines
until you restart the model deployment.

`finish_pending_work`::
(Optional, Boolean) If true, the deployment is stopped after any queued work is completed. Defaults to `false`.

## Examples

The following example stops the `my_model_for_search` deployment:

```console
POST _ml/trained_models/my_model_for_search/deployment/_stop
```
