<!-- Converted from inference/stream-inference.asciidoc (AsciiDoc). Includes are inlined. -->

### Stream inference API

**New API reference**
For the most up-to-date API details, refer to https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-stream-completion[Perform streaming inference
].

Streams a chat completion response.

**Important:** The inference APIs enable you to use certain services, such as built-in machine learning models (ELSER, E5), models uploaded through Eland, Cohere, OpenAI, Azure, Google AI Studio, Google Vertex AI, Anthropic, Watsonx.ai, or Hugging Face.
For built-in models and models uploaded through Eland, the inference APIs offer an alternative way to use and manage trained models.
However, if you do not plan to use the inference APIs to use these models or if you want to use non-NLP models, use the ml-df-trained-models-apis.

#### Request

`POST /_inference/<inference_id>/_stream`

`POST /_inference/<task_type>/<inference_id>/_stream`

#### Prerequisites

* Requires the `monitor_inference` cluster privilege
(the built-in `inference_admin` and `inference_user` roles grant this privilege)
* You must use a client that supports streaming.

#### Description

The stream inference API enables real-time responses for completion tasks by delivering answers incrementally, reducing response times during computation.
It only works with the `completion` and `chat_completion` task types.

The Chat completion inference API and the Stream inference API differ in their response structure and capabilities.
The Chat completion inference API provides more comprehensive customization options through more fields and function calling support.
If you use the `openai` service or the `elastic` service, use the Chat completion inference API.

**Note:**
For more information on how to use the `chat_completion` task type, please refer to the chat completion documentation.

#### Path parameters

`<inference_id>`::
(Required, string)
The unique identifier of the inference endpoint.

`<task_type>`::
(Optional, string)
The type of inference task that the model performs.

#### Request body

`input`::
(Required, string or array of strings)
The text on which you want to perform the inference task.
`input` can be a single string or an array.

**Note:**
Inference endpoints for the `completion` task type currently only support a
single string as input.

#### Examples

The following example performs a completion on the example question with streaming.

```console
POST _inference/completion/openai-completion/_stream
{
  "input": "What is Elastic?"
}
```

The API returns the following response:

```txt
event: message
data: {
  "completion":[{
    "delta":"Elastic"
  }]
}

event: message
data: {
  "completion":[{
    "delta":" is"
    },
    {
    "delta":" a"
    }
  ]
}

event: message
data: {
  "completion":[{
    "delta":" software"
  },
  {
    "delta":" company"
  }]
}

(...)
```
