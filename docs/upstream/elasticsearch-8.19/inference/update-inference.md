<!-- Converted from inference/update-inference.asciidoc (AsciiDoc). Includes are inlined. -->

### Update inference API

**New API reference**
For the most up-to-date API details, refer to [Update an inference endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-update).

Updates an inference endpoint.

**Important:** The inference APIs enable you to use certain services, such as built-in machine learning models (ELSER, E5), models uploaded through Eland, Cohere, OpenAI, Azure, Google AI Studio, Google Vertex AI, Anthropic, Watsonx.ai, or Hugging Face.
For built-in models and models uploaded through Eland, the inference APIs offer an alternative way to use and manage trained models.
However, if you do not plan to use the inference APIs to use these models or if you want to use non-NLP models, use the ml-df-trained-models-apis.

#### Request

`PUT _inference/<inference_id>/_update`

`PUT _inference/<task_type>/<inference_id>/_update`

#### Prerequisites

* Requires the `manage_inference` cluster privilege (the built-in inference_admin role grants this privilege)
* Requires an existing inference endpoint, created by using the put-inference-api

#### Description

The update inference API enables you to update the task_settings, secrets, and/or num_allocations of an existing inference endpoint.

To use the update API, you can modify `task_settings`, secrets (within `service_settings`), or `num_allocations`, depending on the specific endpoint service and task_type you've created.
To view the updatable `task_settings`, the field names of secrets (specific to each service), and the services where `num_allocations` is applicable (only for the `elasticsearch` service), refer to the following list of services available through the inference API.
You will find the available task types next to each service name.
Click the links to review the service configuration details:

* AlibabaCloud AI Search (`completion`, `rerank`, `sparse_embedding`, `text_embedding`)
* Amazon Bedrock (`completion`, `text_embedding`)
* Anthropic (`completion`)
* Azure AI Studio (`completion`, `text_embedding`)
* Azure OpenAI (`completion`, `text_embedding`)
* Cohere (`completion`, `rerank`, `text_embedding`)
* Elasticsearch (`rerank`, `sparse_embedding`, `text_embedding` - this service is for built-in models and models uploaded through Eland)
* ELSER (`sparse_embedding`)
* Google AI Studio (`completion`, `text_embedding`)
* Google Vertex AI (`rerank`, `text_embedding`)
* Hugging Face (`text_embedding`)
* Mistral (`text_embedding`)
* OpenAI (`completion`, `text_embedding`)

#### Path parameters

`<inference_id>`::
(Required, string)
The unique identifier of the inference endpoint.

`<task_type>`::
(Optional, string)
The type of inference task that the model performs.
Refer to the service list in the API description section for the available task types.

#### Examples

The following example shows how to update an API key of an inference endpoint called `my-inference-endpoint`:

```console
PUT _inference/my-inference-endpoint/_update
{
 "service_settings": {
   "api_key": "<API_KEY>"
 }
}
```
