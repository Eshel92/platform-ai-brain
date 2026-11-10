<!-- Converted from search/search-your-data/semantic-search.asciidoc (AsciiDoc). Includes are inlined. -->

## Semantic search

Semantic search is a search method that helps you find data based on the intent and contextual meaning of a search query, instead of a match on query terms (lexical search).

Elasticsearch provides various semantic search capabilities using {ml-docs}/ml-nlp.html[natural language processing (NLP)] and vector search.
Using an NLP model enables you to extract text embeddings out of text.
Embeddings are vectors that provide a numeric representation of a text.
Pieces of content with similar meaning have similar representations.

(Figure: images/semantic-options.svg)

You have several options for using NLP models in the Elastic Stack:

* use the `semantic_text` workflow (recommended)
* use the inference API workflow
* deploy models directly in Elasticsearch

Refer to this section to choose your workflow.

You can also store your own embeddings in Elasticsearch as vectors.
Refer to this section for guidance on which query type to use for semantic search.

At query time, Elasticsearch can use the same NLP model to convert a query into embeddings, enabling you to find documents with similar text embeddings.

### Choose a semantic search workflow

#### `semantic_text` workflow

The simplest way to use NLP models in the Elastic Stack is through the `semantic_text` workflow.
We recommend using this approach because it abstracts away a lot of manual work.
All you need to do is create an inference endpoint and an index mapping to start ingesting, embedding, and querying data.
There is no need to define model-related settings and parameters, or to create inference ingest pipelines.
Refer to the Create an inference endpoint API documentation for a list of supported services.

The Semantic search with `semantic_text` tutorial shows you the process end-to-end.

#### inference API workflow

The inference API workflow is more complex but offers greater control over the inference endpoint configuration.
You need to create an inference endpoint, provide various model-related settings and parameters, define an index mapping, and set up an inference ingest pipeline with the appropriate settings.

The Semantic search with the inference API tutorial shows you the process end-to-end.

#### Model deployment workflow

You can also deploy NLP in Elasticsearch manually, without using an inference endpoint.
This is the most complex and labor intensive workflow for performing semantic search in the Elastic Stack.
You need to select an NLP model from the {ml-docs}/ml-nlp-model-ref.html#ml-nlp-model-ref-text-embedding[list of supported dense and sparse vector models], deploy it using the Eland client, create an index mapping, and set up a suitable ingest pipeline to start ingesting and querying data.

The Semantic search with a model deployed in Elasticsearch tutorial shows you the process end-to-end.

### Using the right query

Crafting the right query is crucial for semantic search.
Which query you use and which field you target in your queries depends on your chosen workflow.
If you're using the `semantic_text` workflow it's quite simple.
If not, it depends on which type of embeddings you're working with.

|=======================================================================================================================================================================================================
| Field type to query                    | Query to use                                      | Notes                                                                                                                                                             
| `semantic_text`      | `semantic`           | The `semantic_text` field handles generating embeddings for you at index time and query time.                                                               
| `sparse_vector`      | `sparse_vector` | The `sparse_vector` query can generate query embeddings for you, but you can also provide your own. You must provide embeddings at index time.
| `dense_vector`        | `knn`                     | The `knn` query can generate query embeddings for you, but you can also provide your own. You must provide embeddings at index time.
|=======================================================================================================================================================================================================

If you want Elasticsearch to generate embeddings at both index and query time, use the `semantic_text` field and the `semantic` query.
If you want to bring your own embeddings, use the `sparse_vector` or `dense_vector` field type and the associated query depending on the NLP model you used to generate the embeddings.

**Important:** For the easiest way to perform semantic search in the Elastic Stack, refer to the `semantic_text` end-to-end tutorial.

### Read more

* Tutorials:
** Semantic search with `semantic_text`
** Semantic search with the inference API
** Semantic search with ELSER using the model deployment workflow
** Semantic search with a model deployed in Elasticsearch
** {ml-docs}/ml-nlp-text-emb-vector-search-example.html[Semantic search with the msmarco-MiniLM-L-12-v3 sentence-transformer model]
* Interactive examples:
** The [`elasticsearch-labs`](https://github.com/elastic/elasticsearch-labs) repo contains a number of interactive semantic search examples in the form of executable Python notebooks, using the Elasticsearch Python client
** [Semantic search with ELSER using the model deployment workflow](https://github.com/elastic/elasticsearch-labs/blob/main/notebooks/search/03-ELSER.ipynb)
** [Semantic search with `semantic_text`](https://github.com/elastic/elasticsearch-labs/blob/main/notebooks/search/09-semantic-text.ipynb)
* Blogs:
** [Elasticsearch new semantic_text mapping: Simplifying semantic search](https://www.elastic.co/search-labs/blog/semantic-search-simplified-semantic-text)
** [`semantic_text` format changes and new features in 8.18](https://www.elastic.co/search-labs/blog/semantic-text-ga)
** {blog-ref}may-2023-launch-sparse-encoder-ai-model[Introducing Elastic Learned Sparse Encoder: Elastic's AI model for semantic search]
** {blog-ref}lexical-ai-powered-search-elastic-vector-database[How to get the best of lexical and AI-powered search with Elastic's vector database]
** Information retrieval blog series:
*** {blog-ref}improving-information-retrieval-elastic-stack-search-relevance[Part 1: Steps to improve search relevance]
*** {blog-ref}improving-information-retrieval-elastic-stack-benchmarking-passage-retrieval[Part 2: Benchmarking passage retrieval]
*** {blog-ref}may-2023-launch-information-retrieval-elasticsearch-ai-model[Part 3: Introducing Elastic Learned Sparse Encoder, our new retrieval model]
*** {blog-ref}improving-information-retrieval-elastic-stack-hybrid[Part 4: Hybrid retrieval]

(See `search/search-your-data/semantic-search-semantic-text.md`)
(See `search/search-your-data/semantic-text-hybrid-search.md`)
(See `search/search-your-data/semantic-search-inference.md`)
(See `search/search-your-data/semantic-search-elser.md`)
(See `search/search-your-data/cohere-es.md`)
(See `search/search-your-data/semantic-search-deploy-model.md`)
(See `search/search-your-data/ingest-vectors.md`)
