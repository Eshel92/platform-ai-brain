<!-- Converted from inference/service-google-vertex-ai.asciidoc (AsciiDoc). Includes are inlined. -->

### Google Vertex AI inference integration

**New API reference**
For the most up-to-date API details, refer to https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put-googlevertexai[Create a Google Vertex AI inference endpoint
].

Creates an inference endpoint to perform an inference task with the `googlevertexai` service.

#### Request

`PUT /_inference/<task_type>/<inference_id>`

#### Path parameters

`<inference_id>`::
(Required, string)
The unique identifier of the inference endpoint.
`<task_type>`::
(Required, string)
The type of the inference task that the model will perform.
Available task types:

* `rerank`
* `text_embedding`.

#### Request body

`chunking_settings`::
(Optional, object)
Chunking configuration object.
Refer to infer-chunking-config to learn more about chunking.
`max_chunk_size`:::
(Optional, integer)
Specifies the maximum size of a chunk in words.
Defaults to `250`.
This value cannot be higher than `300` or lower than `20` (for `sentence` strategy) or `10` (for `word` strategy).
`overlap`:::
(Optional, integer)
Only for `word` chunking strategy.
Specifies the number of overlapping words for chunks.
Defaults to `100`.
This value cannot be higher than the half of `max_chunk_size`.
`sentence_overlap`:::
(Optional, integer)
Only for `sentence` chunking strategy.
Specifies the numnber of overlapping sentences for chunks.
It can be either `1` or `0`.
Defaults to `1`.
`strategy`:::
(Optional, string)
Specifies the chunking strategy.
It could be either `sentence` or `word`.
`service`::
(Required, string)
The type of service supported for the specified task type. In this case,
`googlevertexai`.

`service_settings`::
(Required, object)
Settings used to install the inference model.
These settings are specific to the `googlevertexai` service.

`service_account_json`:::
(Required, string)
A valid service account in json format for the Google Vertex AI API.

`model_id`:::
(Required, string)
The name of the model to use for the inference task.
You can find the supported models at [Text embeddings API](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api).

`location`:::
(Required, string)
The name of the location to use for the inference task.
You find the supported locations at [Generative AI on Vertex AI locations](https://cloud.google.com/vertex-ai/generative-ai/docs/learn/locations).

`project_id`:::
(Required, string)
The name of the project to use for the inference task.

`rate_limit`:::
(Optional, object)
By default, the `googlevertexai` service sets the number of requests allowed per minute to `30.000`.
This helps to minimize the number of rate limit errors returned from Google Vertex AI.
To modify this, set the `requests_per_minute` setting of this object in your service settings:
```text
"rate_limit": {
    "requests_per_minute": <<number_of_requests>>
}
```
More information about the rate limits for Google Vertex AI can be found in the [Google Vertex AI Quotas docs](https://cloud.google.com/vertex-ai/docs/quotas).

`task_settings`::
(Optional, object)
Settings to configure the inference task.
These settings are specific to the `<task_type>` you specified.
.`task_settings` for the `rerank` task type
=====
`top_n`:::
(optional, boolean)
Specifies the number of the top n documents, which should be returned.
=====
.`task_settings` for the `text_embedding` task type
=====
`auto_truncate`:::
(optional, boolean)
Specifies if the API truncates inputs longer than the maximum token length automatically.
=====

#### Google Vertex AI service example

The following example shows how to create an inference endpoint called
`google_vertex_ai_embeddings` to perform a `text_embedding` task type.

```console
PUT _inference/text_embedding/google_vertex_ai_embeddings
{
    "service": "googlevertexai",
    "service_settings": {
        "service_account_json": "<service_account_json>",
        "model_id": "<model_id>",
        "location": "<location>",
        "project_id": "<project_id>"
    }
}
```

The next example shows how to create an inference endpoint called
`google_vertex_ai_rerank` to perform a `rerank` task type.

```console
PUT _inference/rerank/google_vertex_ai_rerank
{
    "service": "googlevertexai",
    "service_settings": {
        "service_account_json": "<service_account_json>",
        "project_id": "<project_id>"
    }
}
```
