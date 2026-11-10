<!-- Converted from tab-widgets/semantic-search/search.asciidoc (AsciiDoc). Includes are inlined. -->

ELSER text embeddings can be queried using a
sparse vector query. The sparse vector
query enables you to query a sparse vector field, by
providing the inference ID associated with the NLP model you want to use, and the query text:

```console
GET my-index/_search
{
   "query":{
    "sparse_vector": {
        "field": "my_tokens",
        "inference_id": "my-elser-endpoint",
        "query": "the query string"
      }
   }
}
```

Text embeddings produced by dense vector models can be queried using a
kNN search. In the `knn` clause, provide the name of the
dense vector field, and a `query_vector_builder` clause with the model ID and
the query text.

```console
GET my-index/_search
{
  "knn": {
    "field": "my_embeddings.predicted_value",
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
```
