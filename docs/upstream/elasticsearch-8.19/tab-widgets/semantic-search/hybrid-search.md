<!-- Converted from tab-widgets/semantic-search/hybrid-search.asciidoc (AsciiDoc). Includes are inlined. -->

Hybrid search between a semantic and lexical query can be achieved by using an
`rrf` retriever as part of your search request. Provide a
`sparse_vector` query and a full-text query as
`standard` retrievers for the `rrf` retriever. The `rrf`
retriever uses reciprocal rank fusion to rank the top documents.

```console
GET my-index/_search
{
  "retriever": {
    "rrf": {
      "retrievers": [
        {
          "standard": {
            "query": {
              "match": {
                "my_text_field": "the query string"
              }
            }
          }
        },
        {
          "standard": {
            "query": {
             "sparse_vector": {
                "field": "my_tokens",
                "inference_id": "my-elser-endpoint",
                "query": "the query string"
              }
            }
          }
        }
      ]
    }
  }
}
```

Hybrid search between a semantic and lexical query can be achieved by providing:

* an `rrf` retriever to rank top documents using reciprocal rank fusion
* a `standard` retriever as a child retriever with `query` clause for the full-text query
* a `knn` retriever as a child retriever with the kNN search that queries the dense vector field

```console
GET my-index/_search
{
  "retriever": {
    "rrf": {
      "retrievers": [
        {
          "standard": {
            "query": {
              "match": {
                "my_text_field": "the query string"
              }
            }
          }
        },
        {
          "knn": {
            "field": "text_embedding.predicted_value",
            "k": 10,
            "num_candidates": 100,
            "query_vector_builder": {
              "text_embedding": {
                "model_id": "sentence-transformers__msmarco-minilm-l-12-v3",
                "model_text": "the query string"
              }
            }
          }
        }
      ]
    }
  }
}
```
