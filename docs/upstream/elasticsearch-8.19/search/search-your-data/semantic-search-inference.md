<!-- Converted from search/search-your-data/semantic-search-inference.asciidoc (AsciiDoc). Includes are inlined. -->

### Tutorial: semantic search with the inference API

The instructions in this tutorial shows you how to use the inference API workflow with various services to perform semantic search on your data.

**Important:** For the easiest way to perform semantic search in the Elastic Stack, refer to the `semantic_text` end-to-end tutorial.

The following examples use the:

* `embed-english-v3.0` model for [Cohere](https://docs.cohere.com/docs/cohere-embed)
* `all-mpnet-base-v2` model from [HuggingFace](https://huggingface.co/sentence-transformers/all-mpnet-base-v2)
* `text-embedding-ada-002` second generation embedding model for OpenAI
* models available through [Azure AI Studio](https://ai.azure.com/explore/models?selectedTask=embeddings) or [Azure OpenAI](https://learn.microsoft.com/en-us/azure/ai-services/openai/concepts/models)
* `text-embedding-004` model for [Google Vertex AI](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/text-embeddings-api)
* `mistral-embed` model for [Mistral](https://docs.mistral.ai/getting-started/models/)
* `amazon.titan-embed-text-v1` model for [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/model-ids.html)
* `ops-text-embedding-zh-001` model for [AlibabaCloud AI](https://help.aliyun.com/zh/open-search/search-platform/developer-reference/text-embedding-api-details)

You can use any Cohere and OpenAI models, they are all supported by the inference API.
For a list of recommended models available on HuggingFace, refer to the supported model list.

Click the name of the service you want to use on any of the widgets below to review the corresponding instructions.

<!-- This page was over 60 KB, so its sections are separate files. -->

## Sections (in `semantic-search-inference.parts/`)

- `001-requirements-create-an-inference-endpoint.md`: Requirements … Create an inference endpoint
- `002-create-the-index-mapping-load-data.md`: Create the index mapping … Load data
- `003-ingest-the-data-through-the-inference-ingest-pipel.md`: Ingest the data through the inference ingest pipeline
- `004-semantic-search.md`: Semantic search
- `005-interactive-tutorials.md`: Interactive tutorials
