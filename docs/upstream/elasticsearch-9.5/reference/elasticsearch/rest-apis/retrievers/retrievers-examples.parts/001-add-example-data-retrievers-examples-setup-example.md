<!-- Part 1 of 4 of reference/elasticsearch/rest-apis/retrievers/retrievers-examples.md (split because the page is big). -->

## Add example data [retrievers-examples-setup]

To begin with, let's create the `retrievers_example` index, and add some documents to it.
We will set `number_of_shards=1` for our examples to ensure consistent and reproducible ordering.

```console
PUT retrievers_example
{
    "settings": {
        "number_of_shards": 1
    },
   "mappings": {
       "properties": {
           "vector": {
               "type": "dense_vector",
               "dims": 3,
               "similarity": "l2_norm",
               "index": true,
               "index_options": {
                    "type": "flat"
               }
           },
           "text": {
               "type": "text",
               "copy_to": "text_semantic"
           },
           "text_semantic": {
               "type": "semantic_text"
           },
           "year": {
               "type": "integer"
           },
           "topic": {
               "type": "keyword"
           },
           "timestamp": {
               "type": "date"
           }
       }
   }
}

POST /retrievers_example/_doc/1
{
 "vector": [0.23, 0.67, 0.89],
 "text": "Large language models are revolutionizing information retrieval by boosting search precision, deepening contextual understanding, and reshaping user experiences in data-rich environments.",
 "year": 2024,
 "topic": ["llm", "ai", "information_retrieval"],
 "timestamp": "2021-01-01T12:10:30"
}

POST /retrievers_example/_doc/2
{
 "vector": [0.12, 0.56, 0.78],
 "text": "Artificial intelligence is transforming medicine, from advancing diagnostics and tailoring treatment plans to empowering predictive patient care for improved health outcomes.",
 "year": 2023,
 "topic": ["ai", "medicine"],
 "timestamp": "2022-01-01T12:10:30"
}

POST /retrievers_example/_doc/3
{
 "vector": [0.45, 0.32, 0.91],
  "text": "AI is redefining security by enabling advanced threat detection, proactive risk analysis, and dynamic defenses against increasingly sophisticated cyber threats.",
 "year": 2024,
 "topic": ["ai", "security"],
 "timestamp": "2023-01-01T12:10:30"
}

POST /retrievers_example/_doc/4
{
 "vector": [0.34, 0.21, 0.98],
 "text": "Elastic introduces Elastic AI Assistant, the open, generative AI sidekick powered by ESRE to democratize cybersecurity and enable users of every skill level.",
 "year": 2023,
 "topic": ["ai", "elastic", "assistant"],
 "timestamp": "2024-01-01T12:10:30"
}

POST /retrievers_example/_doc/5
{
 "vector": [0.11, 0.65, 0.47],
 "text": "Learn how to spin up a deployment on Elastic Cloud and use Elastic Observability to gain deeper insight into the behavior of your applications and systems.",
 "year": 2024,
 "topic": ["documentation", "observability", "elastic"],
 "timestamp": "2025-01-01T12:10:30"
}

POST /retrievers_example/_refresh
```

Now that we have our documents in place, let’s try to run some queries using retrievers.



## Example: Combining query and kNN with RRF [retrievers-examples-combining-standard-knn-retrievers-with-rrf]

First, let’s examine how to combine two different types of queries: a `kNN` query and a `query_string` query.
While these queries may produce scores in different ranges, we can use Reciprocal Rank Fusion (`rrf`) to combine the results and generate a merged final result list.

To implement this in the retriever framework, we start with the top-level element: our `rrf` retriever.
This retriever operates on top of two other retrievers: a `knn` retriever and a `standard` retriever.
We can specify weights to adjust the influence of each retriever on the final ranking.
In this example, we're giving the `standard` retriever twice the influence of the `knn` retriever:

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
    "_source": false
}
```
% TEST[continued]

This returns the following response based on the final rrf score for each result.

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
                "_score": 0.8333334
            },
            {
                "_index": "retrievers_example",
                "_id": "2",
                "_score": 0.8333334
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
::::


### Using the expanded format with weights
```{applies_to}
stack: ga 9.2
```

The same query can be written using the expanded format, which allows you to specify custom weights to adjust the influence of each retriever on the final ranking.
In this example, we're giving the `standard` retriever twice the influence of the `knn` retriever:

```console
GET /retrievers_example/_search
{
    "retriever": {
        "rrf": {
            "retrievers": [
                {
                    "retriever": {
                        "standard": {
                            "query": {
                                "query_string": {
                                    "query": "(information retrieval) OR (artificial intelligence)",
                                    "default_field": "text"
                                }
                            }
                        }
                    },
                    "weight": 2.0
                },
                {
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
                    "weight": 1.0
                }
            ],
            "rank_window_size": 10,
            "rank_constant": 1
        }
    },
    "_source": false
}
```



## Example: Hybrid search with linear retriever [retrievers-examples-linear-retriever]

A different, and more intuitive, way to provide hybrid search, is to linearly combine the top documents of different retrievers using a weighted sum of the original scores.
Since, as above, the scores could lie in different ranges, we can also specify a `normalizer` that would ensure that all scores for the top ranked documents of a retriever lie in a specific range.

To implement this, we define a `linear` retriever, and along with a set of retrievers that will generate the heterogeneous results sets that we will combine.
We will solve a problem similar to the above, by merging the results of a `standard` and a `knn` retriever.
As the `standard` retriever’s scores are based on BM25 and are not strictly bounded, we will also define a `minmax` normalizer to ensure that the scores lie in the [0, 1] range.
We will apply the same normalizer to `knn` as well to ensure that we capture the importance of each document within the result set.

So, let’s now specify the `linear` retriever whose final score is computed as follows:

```text
score = weight(standard) * score(standard) + weight(knn) * score(knn)
score = 2 * score(standard) + 1.5 * score(knn)
```
% NOTCONSOLE

```console
GET /retrievers_example/_search
{
    "retriever": {
        "linear": {
            "retrievers": [
                {
                    "retriever": {
                        "standard": {
                            "query": {
                                "query_string": {
                                    "query": "(information retrieval) OR (artificial intelligence)",
                                    "default_field": "text"
                                }
                            }
                        }
                    },
                    "weight": 2,
                    "normalizer": "minmax"
                },
                {
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
                    "weight": 1.5,
                    "normalizer": "minmax"
                }
            ],
            "rank_window_size": 10
        }
    },
    "_source": false
}
```
% TEST[continued]

This returns the following response based on the normalized weighted score for each result.

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
        "max_score": 3.5,
        "hits": [
            {
                "_index": "retrievers_example",
                "_id": "2",
                "_score": 3.5
            },
            {
                "_index": "retrievers_example",
                "_id": "1",
                "_score": 2.3
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
% TESTRESPONSE[s/"took": 26/"took": $body.took/]
% TESTRESPONSE[s/"value": 3/"value": $body.hits.total.value/]

::::


By normalizing scores and leveraging `function_score` queries, we can also implement more complex ranking strategies, such as sorting results based on their timestamps, assign the timestamp as a score, and then normalizing this score to [0, 1].
Then, we can easily combine the above with a `knn` retriever as follows:

```console
GET /retrievers_example/_search
{
    "retriever": {
        "linear": {
            "retrievers": [
                {
                    "retriever": {
                        "standard": {
                            "query": {
                                "function_score": {
                                    "query": {
                                        "term": {
                                            "topic": "ai"
                                        }
                                    },
                                    "functions": [
                                        {
                                            "script_score": {
                                                "script": {
                                                    "source": "doc['timestamp'].value.millis"
                                                }
                                            }
                                        }
                                    ],
                                    "boost_mode": "replace"
                                }
                            },
                            "sort": {
                                "timestamp": {
                                    "order": "asc"
                                }
                            }
                        }
                    },
                    "weight": 2,
                    "normalizer": "minmax"
                },
                {
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
                    "weight": 1.5
                }
            ],
            "rank_window_size": 10
        }
    },
    "_source": false
}
```
% TEST[continued]

Which would return the following results:

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
        "max_score": 3.5,
        "hits": [
            {
                "_index": "retrievers_example",
                "_id": "3",
                "_score": 3.5
            },
            {
                "_index": "retrievers_example",
                "_id": "2",
                "_score": 2.0
            },
            {
                "_index": "retrievers_example",
                "_id": "4",
                "_score": 1.1
            },
            {
                "_index": "retrievers_example",
                "_id": "1",
                "_score": 0.1
            }
        ]
    }
}
```
% TESTRESPONSE[s/"took": 42/"took": $body.took/]
% TESTRESPONSE[s/"value": 4/"value": $body.hits.total.value/]
% TESTRESPONSE[s/"max_score": 3.5/"max_score": $body.hits.max_score/]
% TESTRESPONSE[s/\.\.\./$body.hits.hits/]
::::



## Example: RRF with the multi-field query format [retrievers-examples-rrf-multi-field-query-format]
```yaml {applies_to}
stack: ga 9.1
```

There's an even simpler way to execute a hybrid search though: We can use the [multi-field query format](/reference/elasticsearch/rest-apis/retrievers.md#multi-field-query-format), which allows us to query multiple fields without explicitly specifying inner retrievers.

One of the major challenges with hybrid search is normalizing the scores across matches on all field types.
Scores from [`text`](/reference/elasticsearch/mapping-reference/text.md) and [`semantic_text`](/reference/elasticsearch/mapping-reference/semantic-text.md) fields don't always fall in the same range, so we need to normalize the ranks across matches on these fields to generate a result set.
For example, BM25 scores from `text` fields are unbounded, while vector similarity scores from `text_embedding` models are bounded between [0, 1].
The multi-field query format [handles this normalization for us automatically](/reference/elasticsearch/rest-apis/retrievers.md#multi-field-field-grouping).

The following example uses the multi-field query format to query every field specified in the `index.query.default_field` index setting, which is set to `*` by default.
This default value will cause the retriever to query every field that either:

- Supports term queries, such as `keyword` and `text` fields
- Is a `semantic_text` field

In this example, that would translate to the `text`, `text_semantic`, `year`, `topic`, and `timestamp` fields.

```console
GET /retrievers_example/_search
{
    "retriever": {
        "rrf": {
            "query": "artificial intelligence"
        }
    }
}
```
% TEST[continued]

This returns the following response based on the final rrf score for each result.

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
                "_score": 0.8333334
            },
            {
                "_index": "retrievers_example",
                "_id": "2",
                "_score": 0.8333334
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

We can also use the `fields` parameter to explicitly specify the fields to query.
The following example uses the multi-field query format to query the `text` and `text_semantic` fields.

```console
GET /retrievers_example/_search
{
    "retriever": {
        "rrf": {
            "query": "artificial intelligence",
            "fields": ["text", "text_semantic"]
        }
    }
}
```
% TEST[continued]

::::{note}
The `fields` parameter also accepts [wildcard field patterns](/reference/elasticsearch/rest-apis/retrievers.md#multi-field-wildcard-field-patterns).
::::

This returns the following response based on the final rrf score for each result.

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
                "_score": 0.8333334
            },
            {
                "_index": "retrievers_example",
                "_id": "2",
                "_score": 0.8333334
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
