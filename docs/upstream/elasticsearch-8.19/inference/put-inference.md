<!-- Converted from inference/put-inference.asciidoc (AsciiDoc). Includes are inlined. -->

### Create inference API

**New API reference**
For the most up-to-date API details, refer to [Create an inference endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put).

Creates an inference endpoint to perform an inference task.

**Important:**
* The inference APIs enable you to use certain services, such as built-in machine learning models (ELSER, E5), models uploaded through Eland, Cohere, OpenAI, Mistral, Azure OpenAI, Google AI Studio, Google Vertex AI, Anthropic, Watsonx.ai, or Hugging Face.
* For built-in models and models uploaded through Eland, the inference APIs offer an alternative way to use and manage trained models. However, if you do not plan to use the inference APIs to use these models or if you want to use non-NLP models, use the ml-df-trained-models-apis.

#### Request

`PUT /_inference/<task_type>/<inference_id>`

#### Prerequisites

* Requires the `manage_inference` cluster privilege
(the built-in `inference_admin` role grants this privilege)

#### Path parameters

`<inference_id>`::
(Required, string)
The unique identifier of the inference endpoint.
`<task_type>`::
(Required, string)
The type of the inference task that the model will perform.
Refer to the integration list in the API description section for the available task types.

#### Description

The create inference API enables you to create an inference endpoint and configure a machine learning model to perform a specific inference task.

**Important:**
* When creating an inference endpoint, the associated machine learning model is automatically deployed if it is not already running.
* After creating the endpoint, wait for the model deployment to complete before using it. You can verify the deployment status by using the Get trained model statistics API. In the response, look for `"state": "fully_allocated"` and ensure the `"allocation_count"` matches the `"target_allocation_count"`.
* Avoid creating multiple endpoints for the same model unless required, as each endpoint consumes significant resources.

The following integrations are available through the inference API.
You can find the available task types next to the integration name.
Click the links to review the configuration details of the integrations:

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
* OpenAI (`chat_completion`, `completion`, `text_embedding`)
* VoyageAI (`text_embedding`, `rerank`)
* infer-service-watsonx-ai (`text_embedding`)
* JinaAI (`text_embedding`, `rerank`)

The Elasticsearch and ELSER services run on a machine learning node in your Elasticsearch cluster.
The rest of the integrations connect to external services.

#### Adaptive allocations

Adaptive allocations allow inference endpoints to dynamically adjust the number of model allocations based on the current load.

When adaptive allocations are enabled:

- The number of allocations scales up automatically when the load increases.
- Allocations scale down to a minimum of 0 when the load decreases, saving resources.

For more information about adaptive allocations and resources, refer to the {ml-docs}/ml-nlp-auto-scale.html[trained model autoscaling] documentation.
