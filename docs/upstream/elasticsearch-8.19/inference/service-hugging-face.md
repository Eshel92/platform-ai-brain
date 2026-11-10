<!-- Converted from inference/service-hugging-face.asciidoc (AsciiDoc). Includes are inlined. -->

### HuggingFace inference integration

**New API reference**
For the most up-to-date API details, refer to [Create a Hugging Face inference endpoint](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-inference-put-hugging-face).

Creates an inference endpoint to perform an inference task with the `hugging_face` service.

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
`hugging_face`.

`service_settings`::
(Required, object)
Settings used to install the inference model.
These settings are specific to the `hugging_face` service.

`api_key`:::
(Required, string)
A valid access token of your Hugging Face account.
You can find your Hugging Face access tokens or you can create a new one
[on the settings page](https://huggingface.co/settings/tokens).
**Important:** You need to provide the API key only once, during the inference model creation.
The get-inference-api does not retrieve your API key.
After creating the inference model, you cannot change the associated API key.
If you want to use a different API key, delete the inference model and recreate it with the same name and the updated API key.

`url`:::
(Required, string)
The URL endpoint to use for the requests.

`rate_limit`:::
(Optional, object)
By default, the `huggingface` service sets the number of requests allowed per minute to `3000`.
This helps to minimize the number of rate limit errors returned from Hugging Face.
To modify this, set the `requests_per_minute` setting of this object in your service settings:
```text
"rate_limit": {
    "requests_per_minute": <<number_of_requests>>
}
```

#### Hugging Face service example

The following example shows how to create an inference endpoint called
`hugging-face-embeddings` to perform a `text_embedding` task type.

```console
PUT _inference/text_embedding/hugging-face-embeddings
{
  "service": "hugging_face",
  "service_settings": {
    "api_key": "<access_token>", <1>
    "url": "<url_endpoint>" <2>
  }
}
```
<1> A valid Hugging Face access token.
You can find on the
[settings page of your account](https://huggingface.co/settings/tokens).
<2> The inference endpoint URL you created on Hugging Face.

Create a new inference endpoint on
[the Hugging Face endpoint page](https://ui.endpoints.huggingface.co/) to get an endpoint URL.
Select the model you want to use on the new endpoint creation page - for example `intfloat/e5-small-v2` - then select the `Sentence Embeddings`
task under the Advanced configuration section.
Create the endpoint.
Copy the URL after the endpoint initialization has been finished.

The list of recommended models for the Hugging Face service:

* [all-MiniLM-L6-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L6-v2)
* [all-MiniLM-L12-v2](https://huggingface.co/sentence-transformers/all-MiniLM-L12-v2)
* [all-mpnet-base-v2](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)
* [e5-base-v2](https://huggingface.co/intfloat/e5-base-v2)
* [e5-small-v2](https://huggingface.co/intfloat/e5-small-v2)
* [multilingual-e5-base](https://huggingface.co/intfloat/multilingual-e5-base)
* [multilingual-e5-small](https://huggingface.co/intfloat/multilingual-e5-small)
