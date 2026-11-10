<!-- Converted from inference/post-inference.asciidoc (AsciiDoc). Includes are inlined. -->

### Perform inference API

**New API reference**
For the most up-to-date API details, refer to [Perform completion inference on the service](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-completion).

Performs an inference task on an input text by using an inference endpoint.

**Important:** The inference APIs enable you to use certain services, such as built-in machine learning models (ELSER, E5), models uploaded through Eland, Cohere, OpenAI, Azure, Google AI Studio, Google Vertex AI, Anthropic, Watsonx.ai, or Hugging Face.
For built-in models and models uploaded through Eland, the inference APIs offer an alternative way to use and manage trained models.
However, if you do not plan to use the inference APIs to use these models or if you want to use non-NLP models, use the ml-df-trained-models-apis.

#### Request

`POST /_inference/<inference_id>`

`POST /_inference/<task_type>/<inference_id>`

#### Prerequisites

* Requires the `monitor_inference` cluster privilege
(the built-in `inference_admin` and `inference_user` roles grant this privilege)

#### Description

The perform inference API enables you to use machine learning models to perform specific tasks
on data that you provide as an input. The API returns a response with the
results of the tasks. The inference endpoint you use can perform one specific task
that has been defined when the endpoint was created with the
put-inference-api.

#### Path parameters

`<inference_id>`::
(Required, string)
The unique identifier of the inference endpoint.

`<task_type>`::
(Optional, string)
The type of inference task that the model performs.

#### Query parameters

`timeout`::
(Optional, timeout)
Controls the amount of time to wait for the inference to complete. Defaults to 30
seconds.

#### Request body

`input`::
(Required, string or array of strings)
The text on which you want to perform the inference task.
`input` can be a single string or an array.

**Note:**
Inference endpoints for the `completion` task type currently only support a
single string as input.

`query`::
(Required, string)
Only for `rerank` inference endpoints. The search query text.

`task_settings`::
(Optional, object)
Task settings for the individual inference request.
These settings are specific to the `<task_type>` you specified and override the task settings specified when initializing the service.

#### Examples

##### Completion example

The following example performs a completion on the example question.

```console
POST _inference/completion/openai_chat_completions
{
  "input": "What is Elastic?"
}
```

The API returns the following response:

```console-result
{
  "completion": [
    {
      "result": "Elastic is a company that provides a range of software solutions for search, logging, security, and analytics. Their flagship product is Elasticsearch, an open-source, distributed search engine that allows users to search, analyze, and visualize large volumes of data in real-time. Elastic also offers products such as Kibana, a data visualization tool, and Logstash, a log management and pipeline tool, as well as various other tools and solutions for data analysis and management."
    }
  ]
}
```

##### Rerank example

The following example performs reranking on the example input.

```console
POST _inference/rerank/cohere_rerank
{
  "input": ["luke", "like", "leia", "chewy","r2d2", "star", "wars"],
  "query": "star wars main character"
}
```

The API returns the following response:

```console-result
{
  "rerank": [
    {
      "index": "2",
      "relevance_score": "0.011597361",
      "text": "leia"
    },
    {
      "index": "0",
      "relevance_score": "0.006338922",
      "text": "luke"
    },
    {
      "index": "5",
      "relevance_score": "0.0016166499",
      "text": "star"
    },
    {
      "index": "4",
      "relevance_score": "0.0011695103",
      "text": "r2d2"
    },
    {
      "index": "1",
      "relevance_score": "5.614787E-4",
      "text": "like"
    },
    {
      "index": "6",
      "relevance_score": "3.7850367E-4",
      "text": "wars"
    },
    {
      "index": "3",
      "relevance_score": "1.2508839E-5",
      "text": "chewy"
    }
  ]
}
```

##### Sparse embedding example

The following example performs sparse embedding on the example sentence.

```console
POST _inference/sparse_embedding/my-elser-model
{
  "input": "The sky above the port was the color of television tuned to a dead channel."
}
```

The API returns the following response:

```console-result
{
  "sparse_embedding": [
    {
      "port": 2.1259406,
      "sky": 1.7073475,
      "color": 1.6922266,
      "dead": 1.6247464,
      "television": 1.3525393,
      "above": 1.2425821,
      "tuned": 1.1440028,
      "colors": 1.1218185,
      "tv": 1.0111054,
      "ports": 1.0067928,
      "poem": 1.0042328,
      "channel": 0.99471164,
      "tune": 0.96235967,
      "scene": 0.9020516,
      (...)
    },
    (...)
  ]
}
```

##### Text embedding example

The following example performs text embedding on the example sentence using the Cohere integration.

```console
POST _inference/text_embedding/my-cohere-endpoint
{
  "input": "The sky above the port was the color of television tuned to a dead channel.",
  "task_settings": {
    "input_type": "ingest"
  }
}
```

The API returns the following response:

```console-result
{
  "text_embedding": [
    {
      "embedding": [
        {
          0.018569946,
          -0.036895752,
          0.01486969,
          -0.0045204163,
          -0.04385376,
          0.0075950623,
          0.04260254,
          -0.004005432,
          0.007865906,
          0.030792236,
          -0.050476074,
          0.011795044,
          -0.011642456,
          -0.010070801,
          (...)
        },
        (...)
      ]
    }
  ]
}
```
