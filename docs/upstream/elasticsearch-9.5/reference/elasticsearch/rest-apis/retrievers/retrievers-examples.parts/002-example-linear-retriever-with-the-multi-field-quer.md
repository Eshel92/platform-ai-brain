<!-- Part 2 of 4 of reference/elasticsearch/rest-apis/retrievers/retrievers-examples.md (split because the page is big). -->

## Example: Linear retriever with the multi-field query format [retrievers-examples-linear-multi-field-query-format]
```yaml {applies_to}
stack: ga 9.1
```

We can also use the [multi-field query format](/reference/elasticsearch/rest-apis/retrievers.md#multi-field-query-format) with the `linear` retriever.
It works much the same way as [on the `rrf` retriever](#retrievers-examples-rrf-multi-field-query-format), with a couple key differences:

- We can use `^` notation to specify a [per-field boost](/reference/elasticsearch/rest-apis/retrievers.md#multi-field-field-boosting)
- We must set the `normalizer` parameter to specify the normalization method used to combine [field group scores](/reference/elasticsearch/rest-apis/retrievers.md#multi-field-field-grouping)

The following example uses the `linear` retriever to query the `text`, `text_semantic`, and `topic` fields, with a boost of 2 on the `topic` field:

```console
GET /retrievers_example/_search
{
    "retriever": {
        "linear": {
            "query": "artificial intelligence",
            "fields": ["text", "text_semantic", "topic^2"],
            "normalizer": "minmax"
        }
    }
}
```
% TEST[continued]

This returns the following response based on the normalized score for each result:

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
        "max_score": 2.0,
        "hits": [
            {
                "_index": "retrievers_example",
                "_id": "2",
                "_score": 2.0
            },
            {
                "_index": "retrievers_example",
                "_id": "1",
                "_score": 1.2
            },
            {
                "_index": "retrievers_example",
                "_id": "3",
                "_score": 0.1
            }
        ]
    }
}
```
% TESTRESPONSE[s/"took": 42/"took": $body.took/]
% TESTRESPONSE[s/"value": 3/"value": $body.hits.total.value/]
% TESTRESPONSE[s/"max_score": 2.0/"max_score": $body.hits.max_score/]
::::


## Example: Grouping results by year with `collapse` [retrievers-examples-collapsing-retriever-results]

In our result set, we have many documents with the same `year` value. We can clean this up using the `collapse` parameter with our retriever. This, as with the standard [collapse](/reference/elasticsearch/rest-apis/collapse-search-results.md) feature,
enables grouping results by any field and returns only the highest-scoring document from each group. In this example we’ll collapse our results based on the `year` field.

```console
GET /retrievers_example/_search
{
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
    "collapse": {
        "field": "year",
        "inner_hits": {
            "name": "topic related documents",
            "_source": [
                "year"
            ]
        }
    },
    "_source": false
}
```
% TEST[continued]

This returns the following response with collapsed results.

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
        "max_score": 0.8333334,
        "hits": [
            {
                "_index": "retrievers_example",
                "_id": "1",
                "_score": 0.8333334,
                "fields": {
                    "year": [
                        2024
                    ]
                },
                "inner_hits": {
                    "topic related documents": {
                        "hits": {
                            "total": {
                                "value": 2,
                                "relation": "eq"
                            },
                            "max_score": 0.8333334,
                            "hits": [
                                {
                                    "_index": "retrievers_example",
                                    "_id": "1",
                                    "_score": 0.8333334,
                                    "_source": {
                                        "year": 2024
                                    }
                                },
                                {
                                    "_index": "retrievers_example",
                                    "_id": "3",
                                    "_score": 0.25,
                                    "_source": {
                                        "year": 2024
                                    }
                                }
                            ]
                        }
                    }
                }
            },
            {
                "_index": "retrievers_example",
                "_id": "2",
                "_score": 0.8333334,
                "fields": {
                    "year": [
                        2023
                    ]
                },
                "inner_hits": {
                    "topic related documents": {
                        "hits": {
                            "total": {
                                "value": 1,
                                "relation": "eq"
                            },
                            "max_score": 0.8333334,
                            "hits": [
                                {
                                    "_index": "retrievers_example",
                                    "_id": "2",
                                    "_score": 0.8333334,
                                    "_source": {
                                        "year": 2023
                                    }
                                }
                            ]
                        }
                    }
                }
            }
        ]
    }
}
```
% TESTRESPONSE[s/"took": 42/"took": $body.took/]
% TESTRESPONSE[s/"value": 3/"value": $body.hits.total.value/]
% TESTRESPONSE[s/"max_score": 0.8333334/"max_score": $body.hits.max_score/]
::::




## Example: Highlighting results based on nested sub-retrievers [retrievers-examples-highlighting-retriever-results]

Highlighting is now also available for nested sub-retrievers matches. For example, consider the same `rrf` retriever as above, with a `knn` and `standard` retriever as its sub-retrievers. We can specify a `highlight` section, as defined in the [highlighting](/reference/elasticsearch/rest-apis/highlighting.md) documentation, and compute highlights for the top results.

```console
GET /retrievers_example/_search
{
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
    "highlight": {
        "fields": {
            "text": {
                "fragment_size": 150,
                "number_of_fragments": 3
            }
        }
    },
    "_source": false
}
```
% TEST[continued]

This would highlight the `text` field, based on the matches produced by the `standard` retriever. The highlighted snippets would then be included in the response as usual, i.e. under each search hit.

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
        "max_score": 0.8333334,
        "hits": [
            {
                "_index": "retrievers_example",
                "_id": "1",
                "_score": 0.8333334,
                "highlight": {
                    "text": [
                        "Large language models are revolutionizing <em>information</em> <em>retrieval</em> by boosting search precision, deepening contextual understanding, and reshaping user experiences"
                    ]
                }
            },
            {
                "_index": "retrievers_example",
                "_id": "2",
                "_score": 0.8333334,
                "highlight": {
                    "text": [
                        "<em>Artificial</em> <em>intelligence</em> is transforming medicine, from advancing diagnostics and tailoring treatment plans to empowering predictive patient care for improved"
                    ]
                }
            },
            {
                "_index": "retrievers_example",
                "_id": "3",
                "_score": 0.25
            }
        ]
    }
}
```
% TESTRESPONSE[s/"took": 42/"took": $body.took/]
% TESTRESPONSE[s/"value": 3/"value": $body.hits.total.value/]
% TESTRESPONSE[s/"max_score": 0.8333334/"max_score": $body.hits.max_score/]
::::
