<!-- Converted from inference/service-voyageai.asciidoc (AsciiDoc). Includes are inlined. -->

### VoyageAI inference integration

**New API reference**
For the most up-to-date API details, refer to [Create a VoyageAI inference endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put-voyageai).

Creates an inference endpoint to perform an inference task with the `voyageai` service.

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

* `text_embedding`,
* `rerank`.

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
`voyageai`.

`service_settings`::
(Required, object)
Settings used to install the inference model.
These settings are specific to the `voyageai` service.

`dimensions`:::
(Optional, integer)
The number of dimensions the resulting output embeddings should have.
This setting maps to `output_dimension` in the [VoyageAI documentation](https://docs.voyageai.com/docs/embeddings).
Only for the `text_embedding` task type.

`embedding_type`:::
(Optional, string)
The data type for the embeddings to be returned.
This setting maps to `output_dtype` in the [VoyageAI documentation](https://docs.voyageai.com/docs/embeddings).
Permitted values: `float`, `int8`, `bit`.
`int8` is a synonym of `byte` in the VoyageAI documentation.
`bit` is a synonym of `binary` in the VoyageAI documentation.
Only for the `text_embedding` task type.

`model_id`:::
(Required, string)
The name of the model to use for the inference task.
Refer to the VoyageAI documentation for the list of available [text embedding](https://docs.voyageai.com/docs/embeddings) and [rerank](https://docs.voyageai.com/docs/reranker) models.

`rate_limit`:::
(Optional, object)
This setting helps to minimize the number of rate limit errors returned from VoyageAI.
The `voyageai` service sets a default number of requests allowed per minute depending on the task type.
For both `text_embedding` and `rerank`, it is set to `2000`.
To modify this, set the `requests_per_minute` setting of this object in your service settings:
```text
"rate_limit": {
    "requests_per_minute": <<number_of_requests>>
}
```
More information about the rate limits for OpenAI can be found in your [Account limits](https://platform.openai.com/account/limits).

`task_settings`::
(Optional, object)
Settings to configure the inference task.
These settings are specific to the `<task_type>` you specified.
.`task_settings` for the `text_embedding` task type
=====
`input_type`:::
(Optional, string)
Type of the input text.
Permitted values: `ingest` (maps to `document` in the VoyageAI documentation), `search` (maps to `query` in the VoyageAI documentation).

`truncation`:::
(Optional, boolean)
Whether to truncate the input texts to fit within the context length.
Defaults to `false`.
=====
.`task_settings` for the `rerank` task type
=====
`return_documents`:::
(Optional, boolean)
Whether to return the source documents in the response.
Defaults to `false`.

`top_k`:::
(Optional, integer)
The number of most relevant documents to return.
If not specified, the reranking results of all documents will be returned.

`truncation`:::
(Optional, boolean)
Whether to truncate the input texts to fit within the context length.
Defaults to `false`.
=====

#### VoyageAI service example

The following example shows how to create an inference endpoint called `voyageai-embeddings` to perform a `text_embedding` task type.
The embeddings created by requests to this endpoint will have 512 dimensions.

```console
PUT _inference/text_embedding/voyageai-embeddings
{
    "service": "voyageai",
    "service_settings": {
        "model_id": "voyage-3-large",
        "dimensions": 512
    }
}
```

The next example shows how to create an inference endpoint called `voyageai-rerank` to perform a `rerank` task type.

```console
PUT _inference/rerank/voyageai-rerank
{
    "service": "voyageai",
    "service_settings": {
        "model_id": "rerank-2"
    }
}
```
