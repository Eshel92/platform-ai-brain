<!-- Converted from ml/trained-models/apis/clear-trained-model-deployment-cache.asciidoc (AsciiDoc). Includes are inlined. -->

# Clear trained model deployment cache API

**New API reference**
For the most up-to-date API details, refer to [Machine learning trained model APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-trained-model).

Clears the inference cache on all nodes where the deployment is assigned.

## Request

`POST _ml/trained_models/<deployment_id>/deployment/cache/_clear`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the
`machine_learning_admin` built-in role.

## Description

A trained model deployment may have an inference cache enabled. As requests are 
handled by each allocated node, their responses may be cached on that individual 
node. Calling this API clears the caches without restarting the deployment.

## Path parameters

`deployment_id`::
(Required, string)
A unique identifier for the deployment of the model.

## Examples

The following example clears the cache for the new deployment for the
`elastic__distilbert-base-uncased-finetuned-conll03-english` trained model:

```console
POST _ml/trained_models/elastic__distilbert-base-uncased-finetuned-conll03-english/deployment/cache/_clear
```

The API returns the following results:

```console-result
{
   "cleared": true
}
```
