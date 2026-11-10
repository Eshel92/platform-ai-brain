<!-- Converted from ml/trained-models/apis/put-trained-model-definition-part.asciidoc (AsciiDoc). Includes are inlined. -->

# Create trained model definition part API

**New API reference**
For the most up-to-date API details, refer to [Machine learning trained model APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ml-trained-model).

Creates part of a trained model definition.

## Request

`PUT _ml/trained_models/<model_id>/definition/<part_num>`

## Prerequisites

Requires the `manage_ml` cluster privilege. This privilege is included in the
`machine_learning_admin` built-in role.

## Path parameters

`<model_id>`::
(Required, string)
The unique identifier of the trained model.
`<part>`::
(Required, number)
The definition part number. When the definition is loaded for inference
the definition parts will be streamed in order of their `part_num`.
The first part must be `0` and the final part must be `total_parts - 1`.

## Request body

`definition`::
(Required, string)
The definition part for the model. Must be a base64 encoded string.

`total_definition_length`::
(Required, number)
The total uncompressed definition length in bytes. Not base64 encoded.

`total_parts`::
(Required, number)
The total number of parts that will be uploaded. Must be greater than 0.

## Examples

The following example creates a model definition part for a previously
stored model configuration. The definition part is stored in the index
that is configured by the `location.index.name`.

**Note:** The value of the `definition` object is elided from the example
as it is a very large base64 encoded string.

```console
PUT _ml/trained_models/elastic__distilbert-base-uncased-finetuned-conll03-english/definition/0
{
    "definition": "...",
    "total_definition_length": 265632637,
    "total_parts": 64
}
```

The API returns the following results:

```console-result
{
    "acknowledged": true
}
```
