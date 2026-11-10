<!-- Converted from inference/get-inference.asciidoc (AsciiDoc). Includes are inlined. -->

### Get inference API

**New API reference**
For the most up-to-date API details, refer to [Get an inference endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-get).

Retrieves inference endpoint information.

**Important:** The inference APIs enable you to use certain services, such as built-in machine learning models (ELSER, E5), models uploaded through Eland, Cohere, OpenAI, Azure, Google AI Studio, Google Vertex AI, Anthropic, Watsonx.ai, or Hugging Face.
For built-in models and models uploaded through Eland, the inference APIs offer an alternative way to use and manage trained models.
However, if you do not plan to use the inference APIs to use these models or if you want to use non-NLP models, use the ml-df-trained-models-apis.

#### Request

`GET /_inference`

`GET /_inference/_all`

`GET /_inference/<inference_id>`

`GET /_inference/<task_type>/_all`

`GET /_inference/<task_type>/<inference_id>`

#### Prerequisites

* Requires the `monitor_inference` cluster privilege
(the built-in `inference_admin` and `inference_user` roles grant this privilege)

#### Description

You can get information in a single API request for:

* a single inference endpoint by providing the task type and the inference ID,
* all of the inference endpoints for a certain task type by providing the task
type and a wildcard expression,
* all of the inference endpoints by using a wildcard expression.

#### Path parameters

`<inference_id>`::
(Optional, string)
The unique identifier of the inference endpoint.

`<task_type>`::
(Optional, string)
The type of inference task that the model performs.

#### Examples

The following API call retrieves information about the `my-elser-model` inference
model that can perform `sparse_embedding` tasks.

```console
GET _inference/sparse_embedding/my-elser-model
```

The API returns the following response:

```console-result
{
  "inference_id": "my-elser-model",
  "task_type": "sparse_embedding",
  "service": "elasticsearch",
  "service_settings": {
    "num_allocations": 1,
    "num_threads": 1,
    "model_id": ".elser_model_2"
  },
  "chunking_settings": {
    "strategy": "sentence",
    "max_chunk_size": 250,
    "sentence_overlap": 1
  }
}
```
