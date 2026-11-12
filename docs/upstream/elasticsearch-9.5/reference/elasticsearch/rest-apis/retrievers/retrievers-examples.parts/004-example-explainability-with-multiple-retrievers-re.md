<!-- Part 4 of 4 of reference/elasticsearch/rest-apis/retrievers/retrievers-examples.md (split because the page is big). -->

## Example: Explainability with multiple retrievers [retrievers-examples-explain-multiple-rrf]

By adding `explain: true` to the request, each retriever will now provide a detailed explanation of all the steps and calculations required to compute the final score. Composability is fully supported in the context of `explain`, and each retriever will provide its own explanation, as shown in the example below.

```console
GET /retrievers_example/_search
{
    "retriever": {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "term": {
                                "topic": "elastic"
                            }
                        }
                    }
                },
                {
                    "rrf": {
                        "retrievers": [
                            {
                                "standard": {
                                    "query": {
                                        "query_string": {
                                            "query": "(information retrieval) OR (artificial intelligence)",
                                            "default_field": "text"
                                        }
                                    }
                                }
                            },
                            {
                                "knn": {
                                    "field": "vector",
                                    "query_vector": [
                                        0.23,
                                        0.67,
                                        0.89
                                    ],
                                    "k": 3,
                                    "num_candidates": 5
                                }
                            }
                        ],
                        "rank_window_size": 10,
                        "rank_constant": 1
                    }
                }
            ],
            "rank_window_size": 10,
            "rank_constant": 1
        }
    },
    "_source": false,
    "size": 1,
    "explain": true
}
```
% TEST[continued]

The output of which, albeit a bit verbose, will provide all the necessary info to assist in debugging and reason with ranking.

::::{dropdown} Example response
```console-result
{
    "took": 42,
    "timed_out": false,
    "_shards": {
        "total": 1,
        "successful": 1,
        "skipped": 0,
        "failed": 0
    },
    "hits": {
        "total": {
            "value": 5,
            "relation": "eq"
        },
        "max_score": 0.5,
        "hits": [
            {
                "_shard": "[retrievers_example][0]",
                "_node": "jnrdZFKS3abUgWVsVdj2Vg",
                "_index": "retrievers_example",
                "_id": "1",
                "_score": 0.5,
                "_explanation": {
                    "value": 0.5,
                    "description": "rrf score: [0.5] computed for initial ranks [0, 1] with rankConstant: [1] as sum of [1 / (rank + rankConstant)] for each query",
                    "details": [
                        {
                            "value": 0.0,
                            "description": "rrf score: [0], result not found in query at index [0]",
                            "details": []
                        },
                        {
                            "value": 1,
                            "description": "rrf score: [0.5], for rank [1] in query at index [1] computed as [1 / (1 + 1)], for matching query with score",
                            "details": [
                                {
                                    "value": 0.8333334,
                                    "description": "rrf score: [0.8333334] computed for initial ranks [2, 1] with rankConstant: [1] as sum of [1 / (rank + rankConstant)] for each query",
                                    "details": [
                                        {
                                            "value": 2,
                                            "description": "rrf score: [0.33333334], for rank [2] in query at index [0] computed as [1 / (2 + 1)], for matching query with score",
                                            "details": [
                                                {
                                                    "value": 2.8129659,
                                                    "description": "sum of:",
                                                    "details": [
                                                        {
                                                            "value": 1.4064829,
                                                            "description": "weight(text:information in 0) [PerFieldSimilarity], result of:",
                                                            "details": [...]
                                                        },
                                                        {
                                                            "value": 1.4064829,
                                                            "description": "weight(text:retrieval in 0) [PerFieldSimilarity], result of:",
                                                            "details": [...]
                                                        }
                                                    ]
                                                }
                                            ]
                                        },
                                        {
                                            "value": 1,
                                            "description": "rrf score: [0.5], for rank [1] in query at index [1] computed as [1 / (1 + 1)], for matching query with score",
                                            "details": [
                                                {
                                                    "value": 1,
                                                    "description": "doc [0] with an original score of [1.0] is at rank [1] from the following source queries.",
                                                    "details": [
                                                        {
                                                            "value": 1.0,
                                                            "description": "found vector with calculated similarity: 1.0",
                                                            "details": []
                                                        }
                                                    ]
                                                }
                                            ]
                                        }
                                    ]
                                }
                            ]
                        }
                    ]
                }
            }
        ]
    }
}
```
% TESTRESPONSE[s/"took": 42/"took": $body.took/]
% TESTRESPONSE[s/\.\.\./$body.hits.hits.0._explanation.details.0.details.1.details.0.details.0.details.0.details.1.details.0/]
% TESTRESPONSE[s/jnrdZFKS3abUgWVsVdj2Vg/$body.hits.hits.0._node/]
::::




## Example: Rerank results of an RRF retriever [retrievers-examples-text-similarity-reranker-on-top-of-rrf]

To demonstrate the full functionality of retrievers, the following examples also require access to a [semantic reranking model](docs-content://solutions/search/ranking/semantic-reranking.md) set up using the [Elastic inference APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-inference).

In this example we’ll set up a reranking service and use it with the `text_similarity_reranker` retriever to rerank our top results.

```console
PUT _inference/rerank/my-rerank-model
{
 "service": "cohere",
 "service_settings": {
   "model_id": "rerank-english-v3.0",
   "api_key": "{{COHERE_API_KEY}}"
 }
}
```
% TEST[skip: no_access_to_ml]

Let’s start by reranking the results of the `rrf` retriever in our previous example.
We'll also apply a `chunk_rescorer` to ensure that we only consider the best scoring chunks when sending information to the reranker.

```console
GET retrievers_example/_search
{
    "retriever": {
        "text_similarity_reranker": {
            "retriever": {
                "rrf": {
                    "retrievers": [
                        {
                            "standard": {
                                "query": {
                                    "query_string": {
                                        "query": "(information retrieval) OR (artificial intelligence)",
                                        "default_field": "text"
                                    }
                                }
                            }
                        },
                        {
                            "knn": {
                                "field": "vector",
                                "query_vector": [
                                    0.23,
                                    0.67,
                                    0.89
                                ],
                                "k": 3,
                                "num_candidates": 5
                            }
                        }
                    ],
                    "rank_window_size": 10,
                    "rank_constant": 1
                }
            },
            "field": "text",
            "inference_id": "my-rerank-model",
            "inference_text": "What are the state of the art applications of AI in information retrieval?",
            "chunk_rescorer": {
                "size": 1,
                "chunking_settings": {
                    "strategy": "sentence",
                    "max_chunk_size": 300,
                    "sentence_overlap": 0
                }
            }
        }
    },
    "_source": false
}
```
% TEST[skip: no_access_to_ml]


## Example: RRF with semantic reranker [retrievers-examples-rrf-ranking-on-text-similarity-reranker-results]

For this example, we’ll replace the rrf’s `standard` retriever with the `text_similarity_reranker` retriever, using the `my-rerank-model` reranker we previously configured. Since this is a reranker, it needs an initial pool of documents to work with. In this case, we’ll rerank the top `rank_window_size` documents matching the  `ai` topic.

```console
GET /retrievers_example/_search
{
    "retriever": {
        "rrf": {
            "retrievers": [
                {
                    "knn": {
                        "field": "vector",
                        "query_vector": [
                            0.23,
                            0.67,
                            0.89
                        ],
                        "k": 3,
                        "num_candidates": 5
                    }
                },
                {
                    "text_similarity_reranker": {
                        "retriever": {
                            "standard": {
                                "query": {
                                    "term": {
                                        "topic": "ai"
                                    }
                                }
                            }
                        },
                        "field": "text",
                        "inference_id": "my-rerank-model",
                        "inference_text": "Can I use generative AI to identify user intent and improve search relevance?"
                    }
                }
            ],
            "rank_window_size": 10,
            "rank_constant": 1
        }
    },
    "_source": false
}
```
% TEST[skip: no_access_to_ml]


## Example: Chaining multiple semantic rerankers [retrievers-examples-chaining-text-similarity-reranker-retrievers]

Full composability means we can chain together multiple retrievers of the same type. For instance, imagine we have a computationally expensive reranker that’s specialized for AI content. We can rerank the results of a `text_similarity_reranker` using another `text_similarity_reranker` retriever. Each reranker can operate on different fields and/or use different inference services.

```console
GET retrievers_example/_search
{
    "retriever": {
        "text_similarity_reranker": {
            "retriever": {
                "text_similarity_reranker": {
                    "retriever": {
                        "knn": {
                            "field": "vector",
                            "query_vector": [
                                0.23,
                                0.67,
                                0.89
                            ],
                            "k": 3,
                            "num_candidates": 5
                        }
                    },
                    "rank_window_size": 100,
                    "field": "text",
                    "inference_id": "my-rerank-model",
                    "inference_text": "What are the state of the art applications of AI in information retrieval?"
                }
            },
            "rank_window_size": 10,
            "field": "text",
            "inference_id": "my-other-more-expensive-rerank-model",
            "inference_text": "Applications of Large Language Models in technology and their impact on user satisfaction"
        }
    },
    "_source": false
}
```
% TEST[skip: no_access_to_ml]

Note that our example applies two reranking steps. First, we rerank the top 100 documents from the `knn` search using the `my-rerank-model` reranker. Then we pick the top 10 results and rerank them using the more fine-grained `my-other-more-expensive-rerank-model`.
