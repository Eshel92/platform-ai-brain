<!-- Converted from inference/inference-apis.asciidoc (AsciiDoc). Includes are inlined. -->

## {infer-cap} APIs

**Important:** The inference APIs enable you to use certain services, such as built-in
machine learning models (ELSER, E5), models uploaded through Eland, Cohere, OpenAI, Azure,
Google AI Studio or Hugging Face. For built-in models and models uploaded
through Eland, the inference APIs offer an alternative way to use and manage
trained models. However, if you do not plan to use the inference APIs to use these
models or if you want to use non-NLP models, use the
ml-df-trained-models-apis.

**New API reference**
For the most up-to-date API details, refer to [{infer-cap} APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-inference).

The inference APIs enable you to create inference endpoints and integrate with machine learning models of different services - such as Amazon Bedrock, Anthropic, Azure AI Studio, Cohere, Google AI, Mistral, OpenAI, or HuggingFace.
Use the following APIs to manage inference models and perform inference:

* delete-inference-api
* get-inference-api
* post-inference-api
* put-inference-api
* stream-inference-api
* chat-completion-inference-api
* update-inference-api

**A representation of the Elastic inference landscape**
(Figure: images/inference-landscape.jpg)

An inference endpoint enables you to use the corresponding machine learning model without
manual deployment and apply it to your data at ingestion time through
semantic text.

Choose a model from your service or use ELSER – a retrieval model trained by Elastic –, then create an inference endpoint by the put-inference-api.
Now use semantic text to perform semantic search on your data.

### Adaptive allocations

Adaptive allocations allow inference services to dynamically adjust the number of model allocations based on the current load.

When adaptive allocations are enabled:

* The number of allocations scales up automatically when the load increases.
- Allocations scale down to a minimum of 0 when the load decreases, saving resources.

For more information about adaptive allocations and resources, refer to the {ml-docs}/ml-nlp-auto-scale.html[trained model autoscaling] documentation.

### Default inference endpoints

Your Elasticsearch deployment contains preconfigured inference endpoints which makes them easier to use when defining `semantic_text` fields or using inference processors.
The following list contains the default inference endpoints listed by `inference_id`:

* `.elser-2-elasticsearch`: uses the {ml-docs}/ml-nlp-elser.html[ELSER] built-in trained model for `sparse_embedding` tasks (recommended for English language texts)
* `.multilingual-e5-small-elasticsearch`: uses the {ml-docs}/ml-nlp-e5.html[E5] built-in trained model for `text_embedding` tasks (recommended for non-English language texts)

Use the `inference_id` of the endpoint in a `semantic_text` field definition or when creating an inference processor.
The API call will automatically download and deploy the model which might take a couple of minutes.
Default inference enpoints have {ml-docs}/ml-nlp-auto-scale.html#nlp-model-adaptive-allocations[adaptive allocations] enabled.
For these models, the minimum number of allocations is `0`.
If there is no inference activity that uses the endpoint, the number of allocations will scale down to `0` automatically after 15 minutes.

### Configuring chunking

{infer-cap} endpoints have a limit on the amount of text they can process at once, determined by the model's input capacity.
Chunking is the process of splitting the input text into pieces that remain within these limits.
It occurs when ingesting documents into `semantic_text` fields.
Chunking also helps produce sections that are digestible for humans.
Returning a long document in search results is less useful than providing the most relevant chunk of text.

Each chunk will include the text subpassage and the corresponding embedding generated from it.

By default, documents are split into sentences and grouped in sections up to 250 words with 1 sentence overlap so that each chunk shares a sentence with the previous chunk.
Overlapping ensures continuity and prevents vital contextual information in the input text from being lost by a hard break.

Elasticsearch uses the [ICU4J](https://unicode-org.github.io/icu-docs/) library to detect word and sentence boundaries for chunking.
[Word boundaries](https://unicode-org.github.io/icu/userguide/boundaryanalysis/#word-boundary) are identified by following a series of rules, not just the presence of a whitespace character.
For written languages that do use whitespace such as Chinese or Japanese dictionary lookups are used to detect word boundaries.

#### Chunking strategies

Two strategies are available for chunking: `sentence` and `word`.

The `sentence` strategy splits the input text at sentence boundaries.
Each chunk contains one or more complete sentences ensuring that the integrity of sentence-level context is preserved, except when a sentence causes a chunk to exceed a word count of `max_chunk_size`, in which case it will be split across chunks.
The `sentence_overlap` option defines the number of sentences from the previous chunk to include in the current chunk which is either `0` or `1`.

The `word` strategy splits the input text on individual words up to the `max_chunk_size` limit.
The `overlap` option is the number of words from the previous chunk to include in the current chunk.

The default chunking strategy is `sentence`.

**Note:** The default chunking strategy for inference endpoints created before 8.16 is `word`.

#### Example of configuring the chunking behavior

The following example creates an inference endpoint with the `elasticsearch` service that deploys the ELSER model by default and configures the chunking behavior.

```console
PUT _inference/sparse_embedding/small_chunk_size
{
  "service": "elasticsearch",
  "service_settings": {
    "num_allocations": 1,
    "num_threads": 1
  },
  "chunking_settings": {
    "strategy": "sentence",
    "max_chunk_size": 100,
    "sentence_overlap": 0
  }
}
```

(See `inference/delete-inference.md`)
(See `inference/get-inference.md`)
(See `inference/post-inference.md`)
(See `inference/chat-completion-inference.md`)
(See `inference/put-inference.md`)
(See `inference/stream-inference.md`)
(See `inference/update-inference.md`)
(See `inference/service-alibabacloud-ai-search.md`)
(See `inference/service-amazon-bedrock.md`)
(See `inference/service-anthropic.md`)
(See `inference/service-azure-ai-studio.md`)
(See `inference/service-azure-openai.md`)
(See `inference/service-cohere.md`)
(See `inference/service-elasticsearch.md`)
(See `inference/service-elser.md`)
(See `inference/service-google-ai-studio.md`)
(See `inference/service-google-vertex-ai.md`)
(See `inference/service-hugging-face.md`)
(See `inference/service-jinaai.md`)
(See `inference/service-mistral.md`)
(See `inference/service-openai.md`)
(See `inference/service-voyageai.md`)
(See `inference/service-watsonx-ai.md`)
