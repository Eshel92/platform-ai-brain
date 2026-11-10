<!-- Converted from search/retriever.asciidoc (AsciiDoc). Includes are inlined. -->

### Retriever

A retriever is a specification to describe top documents returned from a search.
A retriever replaces other elements of the search API
that also return top documents such as `query` and
`knn`.
A retriever may have child retrievers where a retriever with two or more children is considered a compound retriever.
This allows for complex behavior to be depicted in a tree-like structure, called the retriever tree, which clarifies the order of operations that occur during a search.

**Tip:**
Refer to retrievers-overview for a high level overview of the retrievers abstraction.
Refer to Retrievers examples for additional examples.

**New API reference**
For the most up-to-date API details, refer to [Search APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search).

The following retrievers are available:

`standard`::
A retriever that replaces the functionality of a traditional query.

`knn`::
A retriever that replaces the functionality of a knn search.

`linear`::
A retriever that linearly combines the scores of other retrievers for the top documents.

`rescorer`::
A retriever that replaces the functionality of the query rescorer.

`rrf`::
A retriever that produces top documents from reciprocal rank fusion (RRF).

`text_similarity_reranker`::
A retriever that enhances search results by re-ranking documents based on semantic similarity to a specified inference text, using a machine learning model.

`rule`::
A retriever that applies contextual query-rules to pin or exclude documents for specific queries.

`pinned`::
A retriever that always places specified documents at the top of the results, with the remaining hits provided by a secondary retriever.

#### Standard Retriever

A standard retriever returns top documents from a traditional query.

##### Parameters:

`query`::
(Optional, query object)
Defines a query to retrieve a set of top documents.

`filter`::
(Optional, query object or list of query objects)
Applies a boolean query filter to this retriever, where all documents must match this query but do not contribute to the score.

`search_after`::
(Optional, search after object)
Defines a search after object parameter used for pagination.

`terminate_after`::
(Optional, integer) Maximum number of documents to collect for each shard. If a
query reaches this limit, Elasticsearch terminates the query early. Elasticsearch collects
documents before sorting.
**Important:** Use with caution. Elasticsearch applies this parameter to each shard handling
the request. When possible, let Elasticsearch perform early termination automatically.
Avoid specifying this parameter for requests that target data streams with
backing indices across multiple data tiers.
`sort`::
(Optional, sort object) A sort object that specifies the order of matching documents.

`min_score`::
(Optional, `float`)
Minimum `_score` for matching documents.
Documents with a lower `_score` are not included in the top documents.

`collapse`::
(Optional, collapse object)
Collapses the top documents by a specified key into a single top document per key.

##### Restrictions

When a retriever tree contains a compound retriever (a retriever with two or more child retrievers) the search after parameter is not supported.

#### Example

```console
GET /restaurants/_search
{
  "retriever": { <1>
    "standard": { <2>
      "query": { <3>
        "bool": { <4>
          "should": [ <5>
            {
              "match": { <6>
                "region": "Austria"
              }
            }
          ],
          "filter": [ <7>
            {
              "term": { <8>
                "year": "2019" <9>
              }
            }
          ]
        }
      }
    }
  }
}
```

<1> Opens the `retriever` object.
<2> The `standard` retriever is used for defining traditional Elasticsearch queries.
<3> The entry point for defining the search query.
<4> The `bool` object allows for combining multiple query clauses logically.
<5> The `should` array indicates conditions under which a document will match.
Documents matching these conditions will have increased relevancy scores.
<6> The `match` object finds documents where the `region` field contains the word "Austria."
<7> The `filter` array provides filtering conditions that must be met but do not contribute to the relevancy score.
<8> The `term` object is used for exact matches, in this case, filtering documents by the `year` field.
<9> The exact value to match in the `year` field.

#### kNN Retriever

A kNN retriever returns top documents from a k-nearest neighbor search (kNN).

##### Parameters

`field`::
(Required, string)
The name of the vector field to search against. Must be a
`dense_vector` field with indexing enabled.
`query_vector`::
(Required if `query_vector_builder` is not defined, array of `float`)
Query vector. Must have the same number of dimensions as the vector field you
are searching against. Must be either an array of floats or a hex-encoded byte vector.
`query_vector_builder`::
(Required if `query_vector` is not defined, query vector builder object)
Defines a model to build a query vector.

`k`::
(Required, integer)
Number of nearest neighbors to return as top hits.
This value must be fewer than or equal to `num_candidates`.

`num_candidates`::
(Required, integer)
The number of nearest neighbor candidates to consider per shard.
Needs to be greater than `k`, or `size` if `k` is omitted, and cannot exceed 10,000.
Elasticsearch collects `num_candidates` results from each shard, then merges them
to find the top `k` results. Increasing `num_candidates` tends to improve the
accuracy of the final `k` results. Defaults to `Math.min(1.5 * k, 10_000)`.
`filter`::
(Optional, query object or list of query objects)
Query to filter the documents that can match. The kNN search will return the top
`k` documents that also match this filter. The value can be a single query or a
list of queries. If `filter` is not provided, all documents are allowed to
match.
`similarity`::
(Optional, float)
The minimum similarity required for a document to be considered a match. The similarity
value calculated relates to the raw `similarity` used. Not the
document score. The matched documents are then scored according to `similarity`
and the provided `boost` is applied.

The `similarity` parameter is the direct vector similarity calculation.

* `l2_norm`: also known as Euclidean, will include documents where the vector is within
the `dims` dimensional hypersphere with radius `similarity` with origin at `query_vector`.
* `cosine`, `dot_product`, and `max_inner_product`: Only return vectors where the cosine similarity or dot-product are at least the provided
`similarity`.
Read more here: knn similarity search

`rescore_vector`::
(Optional, object) Functionality in preview:[]. Apply oversampling and rescoring to quantized vectors.

**Note:** Rescoring only makes sense for quantized vectors; when quantization is not used, the original vectors are used for scoring.
Rescore option will be ignored for non-quantized `dense_vector` fields.

`oversample`::
(Required, float)
Applies the specified oversample factor to `k` on the approximate kNN search.
The approximate kNN search will:

* Retrieve `num_candidates` candidates per shard.
* From these candidates, the top `k * oversample` candidates per shard will be rescored using the original vectors.
* The top `k` rescored candidates will be returned.

See oversampling and rescoring quantized vectors for details.

##### Restrictions

The parameters `query_vector` and `query_vector_builder` cannot be used together.

#### Example

```console
GET /restaurants/_search
{
  "retriever": {
    "knn": { <1>
      "field": "vector", <2>
      "query_vector": [10, 22, 77], <3>
      "k": 10, <4>
      "num_candidates": 10 <5>
    }
  }
}
```
<1> Configuration for k-nearest neighbor (knn) search, which is based on vector similarity.
<2> Specifies the field name that contains the vectors.
<3> The query vector against which document vectors are compared in the `knn` search.
<4> The number of nearest neighbors to return as top hits.
This value must be fewer than or equal to `num_candidates`.
<5> The size of the initial candidate set from which the final `k` nearest neighbors are selected.

#### Linear Retriever

A retriever that normalizes and linearly combines the scores of other retrievers.

##### Parameters

**Note:**
Either `query` or `retrievers` must be specified.
Combining `query` and `retrievers` is not supported.

`query`::
(Optional, String)
The query to use when using the multi-field query format.

`fields`::
(Optional, array of strings)
The fields to query when using the multi-field query format.
Fields can include boost values using the `^` notation (e.g., `"field^2"`).
If not specified, uses the index's default fields from the `index.query.default_field` index setting, which is `*` by default.

`normalizer`::
(Optional, String)
The normalizer to use when using the multi-field query format.
See normalizers for supported values.
Required when `query` is specified.

**Warning:**
Avoid using `none` as that will disable normalization and may bias the result set towards lexical matches.
See field grouping for more information.

`retrievers`::
(Optional, array of objects)
A list of the sub-retrievers' configuration, that we will take into account and whose result sets
we will merge through a weighted sum. Each configuration can have a different weight and normalization depending
on the specified retriever.

`rank_window_size`::
(Optional, integer)
This value determines the size of the individual result sets per
query. A higher value will improve result relevance at the cost of performance. The final
ranked result set is pruned down to the search request's size.
`rank_window_size` must be greater than or equal to `size` and greater than or equal to `1`.
Defaults to 10.
`filter`::
(Optional, query object or list of query objects)
Applies the specified boolean query filter to all of the specified sub-retrievers,
according to each retriever's specifications.
Each entry in the `retrievers` array specifies the following parameters:

`retriever`::
(Required, a retriever object)
Specifies the retriever for which we will compute the top documents for. The retriever will produce `rank_window_size`
results, which will later be merged based on the specified `weight` and `normalizer`.

`weight`::
(Optional, float)
The weight that each score of this retriever's top docs will be multiplied with. Must be greater or equal to 0. Defaults to 1.0.

`normalizer`::
(Optional, String)
Specifies how the retriever’s score will be normalized before applying the specified `weight`.
See normalizers for supported values.
Defaults to `none`.

See also this hybrid search example using a linear retriever on how to
independently configure and apply normalizers to retrievers.

##### Normalizers

The `linear` retriever supports the following normalizers:

* `none`: No normalization
* `minmax`: Normalizes scores based on the following formula:
```
score = (score - min) / (max - min)
```

* `l2_norm`: Normalizes scores using the L2 norm of the score values

#### RRF Retriever

An RRF retriever returns top documents based on the RRF formula, equally weighting two or more child retrievers.
Reciprocal rank fusion (RRF) is a method for combining multiple result sets with different relevance indicators into a single result set.

##### Parameters

**Note:**
Either `query` or `retrievers` must be specified.
Combining `query` and `retrievers` is not supported.

`query`::
(Optional, String)
The query to use when using the multi-field query format.

`fields`::
(Optional, array of strings)
The fields to query when using the multi-field query format.
If not specified, uses the index's default fields from the `index.query.default_field` index setting, which is `*` by default.

`retrievers`::
(Optional, array of retriever objects)
A list of child retrievers to specify which sets of returned top documents
will have the RRF formula applied to them. Each child retriever carries an
equal weight as part of the RRF formula. Two or more child retrievers are
required.
`rank_constant`::
(Optional, integer)
This value determines how much influence documents in individual
result sets per query have over the final ranked result set. A higher value indicates
that lower ranked documents have more influence. This value must be greater than or
equal to `1`. Defaults to `60`.
`rank_window_size`::
(Optional, integer)
This value determines the size of the individual result sets per
query. A higher value will improve result relevance at the cost of performance. The final
ranked result set is pruned down to the search request's size.
`rank_window_size` must be greater than or equal to `size` and greater than or equal to `1`.
Defaults to 10.
`filter`::
(Optional, query object or list of query objects)
Applies the specified boolean query filter to all of the specified sub-retrievers,
according to each retriever's specifications.

#### Example: Hybrid search

A simple hybrid search example (lexical search + dense vector search) combining a `standard` retriever with a `knn` retriever using RRF:

```console
GET /restaurants/_search
{
  "retriever": {
    "rrf": { <1>
      "retrievers": [ <2>
        {
          "standard": { <3>
            "query": {
              "multi_match": {
                "query": "Austria",
                "fields": [
                  "city",
                  "region"
                ]
              }
            }
          }
        },
        {
          "knn": { <4>
            "field": "vector",
            "query_vector": [10, 22, 77],
            "k": 10,
            "num_candidates": 10
          }
        }
      ],
      "rank_constant": 1, <5>
      "rank_window_size": 50  <6>
    }
  }
}
```
<1> Defines a retriever tree with an RRF retriever.
<2> The sub-retriever array.
<3> The first sub-retriever is a `standard` retriever.
<4> The second sub-retriever is a `knn` retriever.
<5> The rank constant for the RRF retriever.
<6> The rank window size for the RRF retriever.

#### Example: Hybrid search with sparse vectors

A more complex hybrid search example (lexical search  ELSER sparse vector search  dense vector search) using RRF:

```console
GET movies/_search
{
  "retriever": {
    "rrf": {
      "retrievers": [
        {
          "standard": {
            "query": {
              "sparse_vector": {
                "field": "plot_embedding",
                "inference_id": "my-elser-model",
                "query": "films that explore psychological depths"
              }
            }
          }
        },
        {
          "standard": {
            "query": {
              "multi_match": {
                "query": "crime",
                "fields": [
                  "plot",
                  "title"
                ]
              }
            }
          }
        },
        {
          "knn": {
            "field": "vector",
            "query_vector": [10, 22, 77],
            "k": 10,
            "num_candidates": 10
          }
        }
      ]
    }
  }
}
```

#### Rescorer Retriever

The `rescorer` retriever re-scores only the results produced by its child retriever.
For the `standard` and `knn` retrievers, the `window_size` parameter specifies the number of documents examined per shard.

For compound retrievers like `rrf`, the `window_size` parameter defines the total number of documents examined globally.

When using the `rescorer`, an error is returned if the following conditions are not met:

* The minimum configured rescore's `window_size` is:
** Greater than or equal to the `size` of the parent retriever for nested `rescorer` setups.
** Greater than or equal to the `size` of the search request when used as the primary retriever in the tree.

* And the maximum rescore's `window_size` is:
** Smaller than or equal to the `size` or `rank_window_size` of the child retriever.

##### Parameters

`rescore`::
(Required. A rescorer definition or an array of rescorer definitions)
Defines the rescorers applied sequentially to the top documents returned by the child retriever.

`retriever`::
(Required. retriever)
Specifies the child retriever responsible for generating the initial set of top documents to be re-ranked.

`filter`::
(Optional. query object or list of query objects)
Applies a boolean query filter to the retriever, ensuring that all documents match the filter criteria without affecting their scores.

#### Example

The `rescorer` retriever can be placed at any level within the retriever tree.
The following example demonstrates a `rescorer` applied to the results produced by an `rrf` retriever:

```console
GET movies/_search
{
  "size": 10, <1>
  "retriever": {
    "rescorer": { <2>
      "rescore": {
        "window_size": 50, <3>
        "query": { <4>
          "rescore_query": {
            "script_score": {
              "query": {
                "match_all": {}
              },
              "script": {
                "source": "cosineSimilarity(params.queryVector, 'product-vector_final_stage') + 1.0",
                "params": {
                  "queryVector": [-0.5, 90.0, -10, 14.8, -156.0]
                }
              }
            }
          }
        }
      },
      "retriever": { <5>
        "rrf": {
          "rank_window_size": 100, <6>
          "retrievers": [
            {
              "standard": {
                "query": {
                  "sparse_vector": {
                    "field": "plot_embedding",
                    "inference_id": "my-elser-model",
                    "query": "films that explore psychological depths"
                  }
                }
              }
            },
            {
              "standard": {
                "query": {
                  "multi_match": {
                    "query": "crime",
                    "fields": [
                      "plot",
                      "title"
                    ]
                  }
                }
              }
            },
            {
              "knn": {
                "field": "vector",
                "query_vector": [10, 22, 77],
                "k": 10,
                "num_candidates": 10
              }
            }
          ]
        }
      }
    }
  }
}
```
<1> Specifies the number of top documents to return in the final response.
<2> A `rescorer` retriever applied as the final step.
<3> Defines the number of documents to rescore from the child retriever.
<4> The definition of the `query` rescorer.
<5> Specifies the child retriever definition.
<6> Defines the number of documents returned by the `rrf` retriever, which limits the available documents to

#### Text Similarity Re-ranker Retriever

The `text_similarity_reranker` retriever uses an NLP model to improve search results by reordering the top-k documents based on their semantic similarity to the query.

**Tip:**
Refer to semantic-reranking for a high level overview of semantic re-ranking.

##### Prerequisites

To use `text_similarity_reranker`, you can rely on the preconfigured `.rerank-v1-elasticsearch` inference endpoint, which uses the Elastic Rerank model and serves as the default if no `inference_id` is provided.
This model is optimized for reranking based on text similarity. If you'd like to use a different model, you can set up a custom inference endpoint for the `rerank` task using the Create inference API.
The endpoint should be configured with a machine learning model capable of computing text similarity.
Refer to {ml-docs}/ml-nlp-model-ref.html#ml-nlp-model-ref-text-similarity[the Elastic NLP model reference] for a list of third-party text similarity models supported by {Elasticsearch}.

You have the following options:

* Use the built-in Elastic Rerank cross-encoder model via the inference API’s {Elasticsearch} service. See this example for creating an endpoint using the Elastic Rerank model.
* Use the Cohere Rerank inference endpoint with the `rerank` task type.
* Use the Google Vertex AI inference endpoint with the `rerank` task type.
* Upload a model to Elasticsearch with {eland-docs}/machine-learning.html#ml-nlp-pytorch[Eland] using the `text_similarity` NLP task type.
** Then set up an Elasticsearch service inference endpoint with the `rerank` task type.
** Refer to the example on this page for a step-by-step guide.

**Important:**
Scores from the re-ranking process are normalized using the following formula before returned to the user,
to avoid having negative scores.
```text
score = max(score, 0) + min(exp(score), 1)
```
Using the above, any initially negative scores are projected to (0, 1) and positive scores to [1, infinity).
To revert back if needed, one can use:
```text
score = score - 1, if score >= 0
score = ln(score), if score < 0
```

##### Parameters

`retriever`::
(Required, retriever)
The child retriever that generates the initial set of top documents to be re-ranked.

`field`::
(Required, `string`)
The document field to be used for text similarity comparisons.
This field should contain the text that will be evaluated against the `inferenceText`.

`inference_id`::
(Optional, `string`)
Unique identifier of the inference endpoint created using the inference API. If you don’t specify an inference endpoint, the `inference_id` field defaults to `.rerank-v1-elasticsearch`, a preconfigured endpoint for the elasticsearch `.rerank-v1` model.

`inference_text`::
(Required, `string`)
The text snippet used as the basis for similarity comparison.

`rank_window_size`::
(Optional, `int`)
The number of top documents to consider in the re-ranking process.
Defaults to `10`.

`min_score`::
(Optional, `float`)
Sets a minimum threshold score for including documents in the re-ranked results.
Documents with similarity scores below this threshold will be excluded.
Note that score calculations vary depending on the model used.

`filter`::
(Optional, query object or list of query objects)
Applies the specified boolean query filter to the child  retriever.
If the child retriever already specifies any filters, then this top-level filter is applied in conjuction with the filter defined in the child retriever.

#### Example: Elastic Rerank

This examples demonstrates how to deploy the Elastic Rerank model and use it to re-rank search results using the `text_similarity_reranker` retriever.

Follow these steps:

. Create an inference endpoint for the `rerank` task using the Create inference API.
```console
PUT _inference/rerank/my-elastic-rerank
{
  "service": "elasticsearch",
  "service_settings": {
    "model_id": ".rerank-v1",
    "num_threads": 1,
    "adaptive_allocations": { <1>
      "enabled": true,
      "min_number_of_allocations": 1,
      "max_number_of_allocations": 10
    }
  }
}
```
<1> {ml-docs}/ml-nlp-auto-scale.html#nlp-model-adaptive-allocations[Adaptive allocations] will be enabled with the minimum of 1 and the maximum of 10 allocations.
. Define a `text_similarity_rerank` retriever:
```console
POST _search
{
  "retriever": {
    "text_similarity_reranker": {
      "retriever": {
        "standard": {
          "query": {
            "match": {
              "text": "How often does the moon hide the sun?"
            }
          }
        }
      },
      "field": "text",
      "inference_id": "my-elastic-rerank",
      "inference_text": "How often does the moon hide the sun?",
      "rank_window_size": 100,
      "min_score": 0.5
    }
  }
}
```

#### Example: Cohere Rerank

This example enables out-of-the-box semantic search by re-ranking top documents using the Cohere Rerank API.
This approach eliminates the need to generate and store embeddings for all indexed documents.
This requires a Cohere Rerank inference endpoint that is set up for the `rerank` task type.

```console
GET /index/_search
{
   "retriever": {
      "text_similarity_reranker": {
         "retriever": {
            "standard": {
               "query": {
                  "match_phrase": {
                     "text": "landmark in Paris"
                  }
               }
            }
         },
         "field": "text",
         "inference_id": "my-cohere-rerank-model",
         "inference_text": "Most famous landmark in Paris",
         "rank_window_size": 100,
         "min_score": 0.5
      }
   }
}
```

#### Example: Semantic re-ranking with a Hugging Face model

The following example uses the `cross-encoder/ms-marco-MiniLM-L-6-v2` model from Hugging Face to rerank search results based on semantic similarity.
The model must be uploaded to Elasticsearch using [Eland](https://www.elastic.co/guide/en/elasticsearch/client/eland/current/machine-learning.html#ml-nlp-pytorch).

**Tip:**
Refer to {ml-docs}/ml-nlp-model-ref.html#ml-nlp-model-ref-text-similarity[the Elastic NLP model reference] for a list of third party text similarity models supported by Elasticsearch.

Follow these steps to load the model and create a semantic re-ranker.

. Install Eland using `pip`
```sh
python -m pip install eland[pytorch]
```
. Upload the model to Elasticsearch using Eland.
This example assumes you have an Elastic Cloud deployment and an API key.
Refer to the [Eland documentation](https://www.elastic.co/guide/en/elasticsearch/client/eland/current/machine-learning.html#ml-nlp-pytorch-auth) for more authentication options.
```sh
eland_import_hub_model \
  --cloud-id $CLOUD_ID \
  --es-api-key $ES_API_KEY \
  --hub-model-id cross-encoder/ms-marco-MiniLM-L-6-v2 \
  --task-type text_similarity \
  --clear-previous \
  --start
```
. Create an inference endpoint for the `rerank` task
```console
PUT _inference/rerank/my-msmarco-minilm-model
{
  "service": "elasticsearch",
  "service_settings": {
    "num_allocations": 1,
    "num_threads": 1,
    "model_id": "cross-encoder__ms-marco-minilm-l-6-v2"
  }
}
```
. Define a `text_similarity_rerank` retriever.
```console
POST movies/_search
{
  "retriever": {
    "text_similarity_reranker": {
      "retriever": {
        "standard": {
          "query": {
            "match": {
              "genre": "drama"
            }
          }
        }
      },
      "field": "plot",
      "inference_id": "my-msmarco-minilm-model",
      "inference_text": "films that explore psychological depths"
    }
  }
}
```
This retriever uses a standard `match` query to search the `movie` index for films tagged with the genre "drama".
It then re-ranks the results based on semantic similarity to the text in the `inference_text` parameter, using the model we uploaded to Elasticsearch.

#### Query Rules Retriever

The `rule` retriever enables fine-grained control over search results by applying contextual query rules to pin or exclude documents for specific queries.
This retriever has similar functionality to the rule query, but works out of the box with other retrievers.

##### Prerequisites

To use the `rule` retriever you must first create one or more query rulesets using the query rules management APIs.

##### Parameters

`retriever`::
(Required, retriever)
The child retriever that returns the results to apply query rules on top of.
This can be a standalone retriever such as the standard or knn retriever, or it can be a compound retriever.

`ruleset_ids`::
(Required, `array`)
An array of one or more unique query ruleset IDs with query-based rules to match and apply as applicable.
Rulesets and their associated rules are evaluated in the order in which they are specified in the query and ruleset.
The maximum number of rulesets to specify is 10.

`match_criteria`::
(Required, `object`)
Defines the match criteria to apply to rules in the given query ruleset(s).
Match criteria should match the keys defined in the `criteria.metadata` field of the rule.

`rank_window_size`::
(Optional, `int`)
The number of top documents to return from the `rule` retriever.
Defaults to `10`.

#### Example: Rule retriever

This example shows the rule retriever executed without any additional retrievers.
It runs the query defined by the `retriever` and applies the rules from `my-ruleset` on top of the returned results.

```console
GET movies/_search
{
  "retriever": {
    "rule": {
      "match_criteria": {
        "query_string": "harry potter"
      },
      "ruleset_ids": [
        "my-ruleset"
      ],
      "retriever": {
        "standard": {
          "query": {
            "query_string": {
              "query": "harry potter"
            }
          }
        }
      }
    }
  }
}
```

#### Example: Rule retriever combined with RRF

This example shows how to combine the `rule` retriever with other rerank retrievers such as rrf or text_similarity_reranker.

**Warning:**
The `rule` retriever will apply rules to any documents returned from its defined `retriever` or any of its sub-retrievers.
This means that for the best results, the `rule` retriever should be the outermost defined retriever.
Nesting a `rule` retriever as a sub-retriever under a reranker such as `rrf` or `text_similarity_reranker` may not produce the expected results.

```console
GET movies/_search
{
  "retriever": {
    "rule": { <1>
      "match_criteria": {
        "query_string": "harry potter"
      },
      "ruleset_ids": [
        "my-ruleset"
      ],
      "retriever": {
        "rrf": { <2>
          "retrievers": [
            {
              "standard": {
                "query": {
                  "query_string": {
                    "query": "sorcerer's stone"
                  }
                }
              }
            },
            {
              "standard": {
                "query": {
                  "query_string": {
                    "query": "chamber of secrets"
                  }
                }
              }
            }
          ]
        }
      }
    }
  }
}
```

<1> The `rule` retriever is the outermost retriever, applying rules to the search results that were previously reranked using the `rrf` retriever.
<2> The `rrf` retriever returns results from all of its sub-retrievers, and the output of the `rrf` retriever is used as input to the `rule` retriever.

#### Pinned retriever

A `pinned` retriever returns top documents by always placing specific documents at the top of the results, with the remaining hits provided by a secondary retriever. This retriever offers similar functionality to the pinned query, but works seamlessly with other retrievers. This is useful for promoting certain documents for particular queries, regardless of their relevance score.

##### Parameters

`ids`::
(Optional, array of strings)
A list of document IDs to pin at the top of the results, in the order provided.

`docs`::
(Optional, array of objects)
List of objects specifying documents to pin. Each object must contain at least an `_id` field, and may also specify `_index` if pinning documents across multiple indices.

`retriever`::
(Optional, retriever object)
A retriever (for example a `standard` retriever or a specialized retriever such as `rrf` retriever) used to retrieve the remaining documents after the pinned ones.

Either `ids` or `docs` must be specified.

#### Example: Pinned retriever using `docs

```console
GET /restaurants/_search
{
  "retriever": {
    "pinned": {
      "docs": [
        { "_id": "doc1", "_index": "my-index" },
        { "_id": "doc2" }
      ],
      "retriever": {
        "standard": {
          "query": {
            "match": {
              "title": "elasticsearch"
            }
          }
        }
      }
    }
  }
}
```

### Multi-field query format

The `linear` and `rrf` retrievers support a multi-field query format that provides a simplified way to define searches across multiple fields without explicitly specifying inner retrievers.
This format automatically generates appropriate inner retrievers based on the field types and query parameters.
This is a great way to search an index, knowing little to nothing about its schema, while also handling normalization across lexical and semantic matches.

#### Field grouping

The multi-field query format groups queried fields into two categories:

- **Lexical fields**: fields that support term queries, such as `keyword` and `text` fields.
- **Semantic fields**: `semantic_text` fields.

Each field group is queried separately and the scores/ranks are normalized such that each contributes 50% to the final score/rank.
This balances the importance of lexical and semantic fields.
Most indices contain more lexical than semantic fields, and without this grouping the results would often bias towards lexical field matches.

**Warning:**
In the `linear` retriever, this grouping relies on using a normalizer other than `none` (i.e., `minmax` or `l2_norm`).
If you use the `none` normalizer, the scores across field groups will not be normalized and the results may be biased towards lexical field matches.

#### Linear retriever field boosting

When using the `linear` retriever, fields can be boosted using the `^` notation:

```console
GET books/_search
{
  "retriever": {
    "linear": {
      "query": "elasticsearch",
      "fields": [
        "title^3",                <1>
        "description^2",          <2>
        "title_semantic",         <3>
        "description_semantic^2"
      ],
      "normalizer": "minmax"
    }
  }
}
```

<1> 3x weight
<2> 2x weight
<3> 1x weight (default)

Due to how the field group scores are normalized, per-field boosts have no effect on the range of the final score.
Instead, they affect the importance of the field's score within its group.

For example, if the schema looks like:

```console
PUT /books
{
  "mappings": {
    "properties": {
      "title": {
        "type": "text",
        "copy_to": "title_semantic"
      },
      "description": {
        "type": "text",
        "copy_to": "description_semantic"
      },
      "title_semantic": {
        "type": "semantic_text"
      },
      "description_semantic": {
        "type": "semantic_text"
      }
    }
  }
}
```

And we run this query:

```console
GET books/_search
{
  "retriever": {
    "linear": {
      "query": "elasticsearch",
      "fields": [
        "title",
        "description",
        "title_semantic",
        "description_semantic"
      ],
      "normalizer": "minmax"
    }
  }
}
```

The score breakdown would be:

* Lexical fields (50% of score):
  ** `title`: 50% of lexical fields group score, 25% of final score
  ** `description`: 50% of lexical fields group score, 25% of final score
* Semantic fields (50% of score):
  ** `title_semantic`: 50% of semantic fields group score, 25% of final score
  ** `description_semantic`: 50% of semantic fields group score, 25% of final score

If we apply per-field boosts like so:

```console
GET books/_search
{
  "retriever": {
    "linear": {
      "query": "elasticsearch",
      "fields": [
        "title^3",
        "description^2",
        "title_semantic",
        "description_semantic^2"
      ],
      "normalizer": "minmax"
    }
  }
}
```

The score breakdown would change to:

* Lexical fields (50% of score):
  ** `title`: 60% of lexical fields group score, 30% of final score
  ** `description`: 40% of lexical fields group score, 20% of final score
* Semantic fields (50% of score):
  ** `title_semantic`: 33% of semantic fields group score, 16.5% of final score
  ** `description_semantic`: 66% of semantic fields group score, 33% of final score

#### Wildcard field patterns

Field names support the `*` wildcard character to match multiple fields:

```console
GET books/_search
{
  "retriever": {
    "rrf": {
      "query": "machine learning",
      "fields": [
        "title*",    <1>
        "*_text"     <2>
      ]
    }
  }
}
```

<1> Match fields that start with `title`
<2> Match fields that end with `_text`

Note, however, that wildcard field patterns will only resolve to fields that either:

- Support term queries, such as `keyword` and `text` fields
- Are `semantic_text` fields

#### Limitations

- **Single index**: Multi-field queries currently work with single index searches only
- **CCS (Cross Cluster Search)**: Multi-field queries do not support remote cluster searches

#### Examples

- RRF with the multi-field query format
- Linear retriever with the multi-field query format

### Common usage guidelines

#### Using `from` and `size` with a retriever tree

The `from` and `size`
parameters are provided globally as part of the general
search API.
They are applied to all retrievers in a retriever tree, unless a specific retriever overrides the `size` parameter using a different parameter such as `rank_window_size`.
Though, the final search hits are always limited to `size`.

#### Using aggregations with a retriever tree

Aggregations are globally specified as part of a search request.
The query used for an aggregation is the combination of all leaf retrievers as `should`
clauses in a boolean query.

#### Using `min_score` with compound retrievers

When using `min_score` with compound retrievers (such as [`rrf`](retrievers/rrf-retriever.md) or [`linear`](retrievers/linear-retriever.md)), documents are filtered **after** the compound scoring has been applied. This is important to understand because:

1. **Document collection**: Each child retriever collects documents up to its `rank_window_size` limit.
2. **Score computation**: The compound retriever computes final scores (e.g., RRF ranking, linear combination with normalization).
3. **Threshold filtering**: Documents with a final score below `min_score` are excluded from the results.

Because `min_score` is applied after score normalization or RRF computation, the `total_hits` value reflects only the documents that pass the threshold after the compound scoring, not the total number of documents matched by the child retrievers.

#### Restrictions on search parameters when specifying a retriever

When a retriever is specified as part of a search, the following elements are not allowed at the top-level:

* `query`
* `knn`
* `search_after`
* `terminate_after`
* `sort`
* `rescore` use a rescorer retriever instead
