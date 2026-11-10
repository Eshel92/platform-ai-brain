<!-- Converted from indices/field-usage-stats.asciidoc (AsciiDoc). Includes are inlined. -->

### Field usage stats API

experimental[]

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Returns field usage information for each shard and field
of an index.
Field usage statistics are automatically captured when
queries are running on a cluster. A shard-level search
request that accesses a given field, even if multiple times
during that request, is counted as a single use.

```console
GET /my-index-000001/_field_usage_stats
```

#### Request

`GET /<index>/_field_usage_stats`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the target index or index alias.

#### Path parameters

`<index>`::
(Optional, string) Comma-separated list or wildcard expression of index names
used to limit the request.

#### Query parameters

`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
`expand_wildcards`::
(Optional, string)
Type of index that wildcard patterns can match. If the request can target data
streams, this argument determines whether wildcard expressions match hidden data
streams. Supports comma-separated values, such as `open,hidden`. Valid values
are:

`all`::
Match any data stream or index, including hidden ones.

`open`::
Match open, non-hidden indices. Also matches any non-hidden data stream.

`closed`::
Match closed, non-hidden indices. Also matches any non-hidden data stream. Data
streams cannot be closed.

`hidden`::
Match hidden data streams and hidden indices. Must be combined with `open`,
`closed`, or both.

`none`::
Wildcard patterns are not accepted.
`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`wait_for_active_shards`::
(Optional, string) The number of copies of each shard that must be active
before proceeding with the operation. Set to `all` or any non-negative integer
up to the total number of copies of each shard in the index
(`number_of_replicas+1`). Defaults to `1`, meaning to wait just for each
primary shard to be active.

See index-wait-for-active-shards.
`fields`::
(Optional, string)
Comma-separated list or wildcard expressions of fields
to include in the statistics.

#### Response body

The response body reports the per-shard usage count of the data structures that back the fields in the index.
A given request will increment each count by a maximum value of 1, even if the request accesses the same field multiple times.

`any`::
(integer)
Denotes any kind of use of the field (e.g. via the _inverted index_, _stored fields_, _doc values_, etc.)
such that any usage is counted once for a given search request.

`inverted_index`::
(object)
The _inverted index_ is enabled by the `index` mapping parameter and configured by setting the `index_options` for the field.
**Properties of `inverted_index`:**
`terms`::
(integer)
Denotes the usages of _terms_ in the _inverted index_, answering the question "Is this field's inverted index used?".

`postings`::
(integer)
Denotes the usage of the _posting list_ which contains the document ids for a given term.

`proximity`::
(integer)
Denotes any kind of usage of either _positions_, _offsets_ or _payloads_ in the _inverted index_
such that any usage is counted once for a given search request.

`positions`::
(integer)
Denotes the usage of _position_ data (order of the term) in the _inverted index_.

`term_frequencies`::
(integer)
Denotes the usage of the _term frequencies_ in the _inverted index_ which are used to calculate scores.

`offsets`::
(integer)
Denotes the usage of the _offsets_ in the _inverted index_ which store the start and end character offsets of the terms.

`payloads`::
(integer)
Denotes the usage of _payloads_ in the _inverted index_,
e.g. via the delimited payload token filter, or by user-defined analysis components and plugins.

`stored_fields`::
(integer)
Denotes the usage of _stored fields_. These are enabled via the `store` mapping option,
and accessed by specifying the `stored_fields` query option.
Note that the `_source` and `_id` fields are stored by default and their usage is counted here.

`doc_values`::
(integer)
Denotes the usage of _doc values_, which are primarily used for sorting and aggregations. These are enabled via the `doc_values` mapping parameter.

`points`::
(integer)
Denotes the usage of the Lucene _PointValues_ which are the basis of most numeric _field data types_, including spacial data types, numbers, dates, and more.
These are used by queries/aggregations for ranges, counts, bucketing, min/max, histograms, spacial, etc.

`norms`::
(integer)
Denotes the usage of _norms_ which contain index-time boost values used for scoring.

`term_vectors`::
(integer)
Denotes the usage of _term vectors_ which allow for a document's terms to be retrieved at search time.
Usages include highlighting and the More Like This Query.

`knn_vectors`::
(integer)
Denotes the usage of the _knn_vectors_ field type,
primarily used for k-nearest neighbor (kNN) search.

#### Examples

```console
POST /my-index-000001/_search
{
  "query" : {
    "match" : { "context" : "bar" }
  },
  "aggs": {
    "message_stats": {
      "string_stats": {
        "field": "message.keyword",
        "show_distribution": true
      }
    }
  }
}
```

The following request retrieves field usage information of index `my-index-000001`
on the currently available shards.

```console
GET /my-index-000001/_field_usage_stats
```

The API returns the following response:

```console-response
{
    "_shards": {
        "total": 1,
        "successful": 1,
        "failed": 0
    },
    "my-index-000001": {
        "shards": [
            {
                "tracking_id": "MpOl0QlTQ4SYYhEe6KgJoQ",
                "tracking_started_at_millis": 1625558985010,
                "routing": {
                    "state": "STARTED",
                    "primary": true,
                    "node": "gA6KeeVzQkGURFCUyV-e8Q",
                    "relocating_node": null
                },
                "stats" : {
                    "all_fields": { <1>
                        "any": "6",
                        "inverted_index": {
                            "terms" : 1,
                            "postings" : 1,
                            "proximity" : 1,
                            "positions" : 0,
                            "term_frequencies" : 1,
                            "offsets" : 0,
                            "payloads" : 0
                        },
                        "stored_fields" : 2,
                        "doc_values" : 1,
                        "points" : 0,
                        "norms" : 1,
                        "term_vectors" : 0,
                        "knn_vectors" : 0
                    },
                    "fields": {
                        "_id": { <2>
                            "any" : 1,
                            "inverted_index": {
                                "terms" : 1,
                                "postings" : 1,
                                "proximity" : 1,
                                "positions" : 0,
                                "term_frequencies" : 1,
                                "offsets" : 0,
                                "payloads" : 0
                            },
                            "stored_fields" : 1,
                            "doc_values" : 0,
                            "points" : 0,
                            "norms" : 0,
                            "term_vectors" : 0,
                            "knn_vectors" : 0
                        },
                        "_source": {...},
                        "context": {...},
                        "message.keyword": {...}
                    }
                }
            }
        ]
    }
}
```
<1> Reports the sums of the usage-counts for all fields in the index (on the listed shard).
<2> The field name for which the following usage-counts are reported (on the listed shard).
