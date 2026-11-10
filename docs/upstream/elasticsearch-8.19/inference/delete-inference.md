<!-- Converted from inference/delete-inference.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete inference API

**New API reference**
For the most up-to-date API details, refer to [Delete an inference endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-delete).

Deletes an inference endpoint.

**Important:** The inference APIs enable you to use certain services, such as built-in machine learning models (ELSER, E5), models uploaded through Eland, Cohere, OpenAI, Azure, Google AI Studio, Google Vertex AI, Anthropic, Watsonx.ai, or Hugging Face.
For built-in models and models uploaded through Eland, the inference APIs offer an alternative way to use and manage trained models.
However, if you do not plan to use the inference APIs to use these models or if you want to use non-NLP models, use the ml-df-trained-models-apis.

#### Request

`DELETE /_inference/<inference_id>`

`DELETE /_inference/<task_type>/<inference_id>`

#### Prerequisites

* Requires the `manage_inference` cluster privilege
(the built-in `inference_admin` role grants this privilege)

#### Path parameters

<inference_id>::
(Required, string)
The unique identifier of the inference endpoint to delete.

<task_type>::
(Optional, string)
The type of inference task that the model performs.

## Query parameters

`dry_run`::
(Optional, Boolean)
When `true`, checks the `semantic_text` fields and  inference processors that reference the endpoint and returns them in a list, but does not delete the endpoint.
Defaults to `false`.

`force`::
(Optional, Boolean)
Deletes the endpoint regardless if it's used in a `semantic_text` field or in an inference pipeline.

#### Examples

The following API call deletes the `my-elser-model` inference model that can
perform `sparse_embedding` tasks.

```console
DELETE /_inference/sparse_embedding/my-elser-model
```

The API returns the following response:

```console-result
{
  "acknowledged": true
}
```
