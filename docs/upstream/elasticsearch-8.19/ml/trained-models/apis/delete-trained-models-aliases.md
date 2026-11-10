<!-- Converted from ml/trained-models/apis/delete-trained-models-aliases.asciidoc (AsciiDoc). Includes are inlined. -->

# Delete trained model aliases API

**New API reference**
For the most up-to-date API details, refer to [Machine learning trained model APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-trained-model).

Deletes a trained model alias.

## Request

`DELETE _ml/trained_models/<model_id>/model_aliases/<model_alias>`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the 
`machine_learning_admin` built-in role.

## Description

This API deletes an existing model alias that refers to a trained model.

If the model alias is missing or refers to a model other than the one identified
by the `model_id`, this API returns an error.

## Path parameters

`model_alias`::
(Required, string)
The model alias to delete.

`model_id`::
(Required, string)
The trained model ID to which the model alias refers.

## Examples

The following example shows how to delete a model alias (`flight_delay_model`)
for a trained model ID (`flight-delay-prediction-1574775339910`):

```console
DELETE _ml/trained_models/flight-delay-prediction-1574775339910/model_aliases/flight_delay_model
```
