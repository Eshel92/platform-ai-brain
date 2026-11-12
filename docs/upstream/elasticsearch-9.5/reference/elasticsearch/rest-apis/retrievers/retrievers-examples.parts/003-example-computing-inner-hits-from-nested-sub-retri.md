<!-- Part 3 of 4 of reference/elasticsearch/rest-apis/retrievers/retrievers-examples.md (split because the page is big). -->

## Example: Computing inner hits from nested sub-retrievers [retrievers-examples-inner-hits-retriever-results]

We can also define `inner_hits` to be computed on any of the sub-retrievers, and propagate those computations to the top level compound retriever. For example, let’s create a new index with a `knn` field, nested under the `nested_field` field, and index a couple of documents.

```console
PUT retrievers_example_nested
{
    "settings": {
         "number_of_shards": 1
     },
    "mappings": {
        "properties": {
            "nested_field": {
                "type": "nested",
                "properties": {
                    "paragraph_id": {
                        "type": "keyword"
                    },
                    "nested_vector": {
                        "type": "dense_vector",
                        "dims": 3,
                        "similarity": "l2_norm",
                        "index": true,
                        "index_options": {
                            "type": "flat"
                        }
                    }
                }
            },
            "topic": {
                "type": "keyword"
            }
        }
    }
}

POST /retrievers_example_nested/_doc/1
{
    "nested_field": [
        {
            "paragraph_id": "1a",
            "nested_vector": [
                -1.12,
                -0.59,
                0.78
            ]
        },
        {
            "paragraph_id": "1b",
            "nested_vector": [
                -0.12,
                1.56,
                0.42
            ]
        },
        {
            "paragraph_id": "1c",
            "nested_vector": [
                1,
                -1,
                0
            ]
        }
    ],
    "topic": [
        "ai"
    ]
}

POST /retrievers_example_nested/_doc/2
{
    "nested_field": [
        {
            "paragraph_id": "2a",
            "nested_vector": [
                0.23,
                1.24,
                0.65
            ]
        }
    ],
    "topic": [
        "information_retrieval"
    ]
}

POST /retrievers_example_nested/_doc/3
{
    "topic": [
        "ai"
    ]
}

POST /retrievers_example_nested/_refresh
```
% TEST[continued]

Now we can run an `rrf` retriever query and also compute [inner hits](/reference/elasticsearch/rest-apis/retrieve-inner-hits.md) for the `nested_field.nested_vector` field, based on the `knn` query specified.

```console
GET /retrievers_example_nested/_search
{
    "retriever": {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "nested": {
                                "path": "nested_field",
                                "inner_hits": {
                                    "name": "nested_vector",
                                    "_source": false,
                                    "fields": [
                                        "nested_field.paragraph_id"
                                    ]
                                },
                                "query": {
                                    "knn": {
                                        "field": "nested_field.nested_vector",
                                        "query_vector": [
                                            1,
                                            0,
                                            0.5
                                        ],
                                        "k": 10
                                    }
                                }
                            }
                        }
                    }
                },
                {
                    "standard": {
                        "query": {
                            "term": {
                                "topic": "ai"
                            }
                        }
                    }
                }
            ],
            "rank_window_size": 10,
            "rank_constant": 1
        }
    },
    "_source": [
        "topic"
    ]
}
```
% TEST[continued]

This would propagate the `inner_hits` defined for the `knn` query to the `rrf` retriever, and compute inner hits for `rrf`'s top results.

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
            "value": 3,
            "relation": "eq"
        },
        "max_score": 1.0,
        "hits": [
            {
                "_index": "retrievers_example_nested",
                "_id": "1",
                "_score": 1.0,
                "_source": {
                    "topic": [
                        "ai"
                    ]
                },
                "inner_hits": {
                    "nested_vector": {
                        "hits": {
                            "total": {
                                "value": 3,
                                "relation": "eq"
                            },
                            "max_score": 0.44444445,
                            "hits": [
                                {
                                    "_index": "retrievers_example_nested",
                                    "_id": "1",
                                    "_nested": {
                                        "field": "nested_field",
                                        "offset": 2
                                    },
                                    "_score": 0.44444445,
                                    "fields": {
                                        "nested_field": [
                                            {
                                                "paragraph_id": [
                                                    "1c"
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "_index": "retrievers_example_nested",
                                    "_id": "1",
                                    "_nested": {
                                        "field": "nested_field",
                                        "offset": 1
                                    },
                                    "_score": 0.21301977,
                                    "fields": {
                                        "nested_field": [
                                            {
                                                "paragraph_id": [
                                                    "1b"
                                                ]
                                            }
                                        ]
                                    }
                                },
                                {
                                    "_index": "retrievers_example_nested",
                                    "_id": "1",
                                    "_nested": {
                                        "field": "nested_field",
                                        "offset": 0
                                    },
                                    "_score": 0.16889325,
                                    "fields": {
                                        "nested_field": [
                                            {
                                                "paragraph_id": [
                                                    "1a"
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                }
            },
            {
                "_index": "retrievers_example_nested",
                "_id": "2",
                "_score": 0.33333334,
                "_source": {
                    "topic": [
                        "information_retrieval"
                    ]
                },
                "inner_hits": {
                    "nested_vector": {
                        "hits": {
                            "total": {
                                "value": 1,
                                "relation": "eq"
                            },
                            "max_score": 0.31715825,
                            "hits": [
                                {
                                    "_index": "retrievers_example_nested",
                                    "_id": "2",
                                    "_nested": {
                                        "field": "nested_field",
                                        "offset": 0
                                    },
                                    "_score": 0.31715825,
                                    "fields": {
                                        "nested_field": [
                                            {
                                                "paragraph_id": [
                                                    "2a"
                                                ]
                                            }
                                        ]
                                    }
                                }
                            ]
                        }
                    }
                }
            },
            {
                "_index": "retrievers_example_nested",
                "_id": "3",
                "_score": 0.33333334,
                "_source": {
                    "topic": [
                        "ai"
                    ]
                },
                "inner_hits": {
                    "nested_vector": {
                        "hits": {
                            "total": {
                                "value": 0,
                                "relation": "eq"
                            },
                            "max_score": null,
                            "hits": []
                        }
                    }
                }
            }
        ]
    }
}
```
% TESTRESPONSE[s/"took": 42/"took" : $body.took/]
% TESTRESPONSE[s/"value": 3/"value": $body.hits.total.value/]
::::


Note: if using more than one `inner_hits` we need to provide custom names for each `inner_hits` so that they are unique across all retrievers within the request.



## Example: Combine RRF with aggregations [retrievers-examples-rrf-and-aggregations]

Retrievers support both composability and most of the standard `_search` functionality. For instance, we can compute aggregations with the `rrf` retriever. When using a compound retriever, the aggregations are computed based on its nested retrievers. In the following example, the `terms` aggregation for the `topic` field will include all results, not just the top `rank_window_size`, from the 2 nested retrievers, i.e. all documents whose `year` field is greater than 2023, and whose `topic` field matches the term `elastic`.

```console
GET retrievers_example/_search
{
    "retriever": {
        "rrf": {
            "retrievers": [
                {
                    "standard": {
                        "query": {
                            "range": {
                                "year": {
                                    "gt": 2023
                                }
                            }
                        }
                    }
                },
                {
                    "standard": {
                        "query": {
                            "term": {
                                "topic": "elastic"
                            }
                        }
                    }
                }
            ],
            "rank_window_size": 10,
            "rank_constant": 1
        }
    },
    "_source": false,
    "aggs": {
        "topics": {
            "terms": {
                "field": "topic"
            }
        }
    }
}
```
% TEST[continued]

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
            "value": 4,
            "relation": "eq"
        },
        "max_score": 0.5833334,
        "hits": [
            {
                "_index": "retrievers_example",
                "_id": "5",
                "_score": 0.5833334
            },
            {
                "_index": "retrievers_example",
                "_id": "1",
                "_score": 0.5
            },
            {
                "_index": "retrievers_example",
                "_id": "4",
                "_score": 0.5
            },
            {
                "_index": "retrievers_example",
                "_id": "3",
                "_score": 0.33333334
            }
        ]
    },
    "aggregations": {
        "topics": {
            "doc_count_error_upper_bound": 0,
            "sum_other_doc_count": 0,
            "buckets": [
                {
                    "key": "ai",
                    "doc_count": 3
                },
                {
                    "key": "elastic",
                    "doc_count": 2
                },
                {
                    "key": "assistant",
                    "doc_count": 1
                },
                {
                    "key": "documentation",
                    "doc_count": 1
                },
                {
                    "key": "information_retrieval",
                    "doc_count": 1
                },
                {
                    "key": "llm",
                    "doc_count": 1
                },
                {
                    "key": "observability",
                    "doc_count": 1
                },
                {
                    "key": "security",
                    "doc_count": 1
                }
            ]
        }
    }
}
```
% TESTRESPONSE[s/"took": 42/"took" : $body.took/]
::::




## Example: Multi-level nested retrievers with min_score [retrievers-examples-nested-retrievers-min-score]

This example demonstrates how `min_score` works with deeply nested compound retrievers. The retriever tree structure is:

- **Outer RRF** (rank_window_size: 20)
  - **Inner RRF** (rank_window_size: 50)
    - **Linear** (rank_window_size: 100, minmax normalizer, min_score: 0.5)
      - **Standard** (query_string query)

Documents are first matched by the innermost `standard` retriever using a query_string query. The `linear` retriever then normalizes these scores using the minmax normalizer and filters based on the specified `min_score`. Then, the inner `rrf` retriever computes the scores for the subset of documents that pass `min_score`, and finally the outer `rrf` retriever produces the final ranking.

The `total_hits` value in this scenario is constrained by the `rank_window_size` parameters, as parent retrievers only have access to the top documents from their children.

**Pagination behavior**: When using `from` and `size` at the top level of the search request, pagination is limited to the documents available at the outermost retriever's `rank_window_size`. In this example, even though the inner retrievers process more documents (100 for `linear`, 50 for inner `rrf`), the outer `rrf` only receives 50 documents and produces a final set of 20 documents. Therefore, `from` and `size` can only paginate through these top 20 documents.

```console
GET /retrievers_example/_search
{
    "retriever": {
        "rrf": {
            "retrievers": [
                {
                    "rrf": {
                        "retrievers": [
                            {
                                "linear": {
                                    "min_score": 0.5,
                                    "retrievers": [
                                        {
                                            "retriever": {
                                                "standard": {
                                                    "query": {
                                                        "query_string": {
                                                            "query": "artificial intelligence",
                                                            "default_field": "text"
                                                        }
                                                    }
                                                }
                                            }
                                        }
                                    ],
                                    "rank_window_size": 100,
                                    "normalizer": "minmax"
                                }
                            }
                        ],
                        "rank_window_size": 50
                    }
                }
            ],
            "rank_window_size": 20
        }
    },
    "size": 10
}
```
% TEST[continued]

In this example:
1. The `standard` retriever matches documents containing "artificial intelligence" in the text field.
2. The `linear` retriever normalizes these scores to a 0-1 range using minmax normalization and filters documents with score less than 0.5.
3. The inner `rrf` computes RRF scores based on document ranks.
4. The outer `rrf` produces the final RRF scores.
5. The `total_hits` value reflects only the documents passing the inner `min_score` threshold.

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
            "value": 1,
            "relation": "eq"
        },
        "max_score": 0.016393442,
        "hits": [
            {
                "_index": "retrievers_example",
                "_id": "2",
                "_score": 0.016393442,
                "_source": {
                    "vector": [0.12, 0.56, 0.78],
                    "text": "Artificial intelligence is transforming medicine, from advancing diagnostics and tailoring treatment plans to empowering predictive patient care for improved health outcomes.",
                    "year": 2023,
                    "topic": ["ai", "medicine"],
                    "timestamp": "2022-01-01T12:10:30"
                }
            }
        ]
    }
}
```
% TESTRESPONSE[s/"took": 42/"took" : $body.took/]
::::
