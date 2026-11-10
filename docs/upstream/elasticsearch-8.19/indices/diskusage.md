<!-- Converted from indices/diskusage.asciidoc (AsciiDoc). Includes are inlined. -->

### Analyze index disk usage API

experimental[]

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Analyzes the disk usage of each field of an index or data stream.
This API might not support indices created in previous Elasticsearch versions.
The result of a small index can be inaccurate as some parts of an index
might not be analyzed by the API.

```console
POST /my-index-000001/_disk_usage?run_expensive_tasks=true
```

#### Request

`POST /<target>/_disk_usage`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the target index, data stream,
or alias.

#### Path parameters

`<target>`::
(Required, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. It's recommended to execute this API with a single
index (or the latest backing index of a data stream) as the API consumes
resources significantly.

#### Query parameters

`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
Defaults to `true`.

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
Defaults to `open`.

`flush`::
(Optional, Boolean) If `true`, the API performs a flush before analysis. If
`false`, the response may not include uncommitted data. Defaults to `true`.

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`run_expensive_tasks`::
(Required, Boolean) Analyzing field disk usage is resource-intensive. To use the
API, this parameter must be set to `true`. Defaults to `false`.

`wait_for_active_shards`::
(Optional, string) The number of copies of each shard that must be active
before proceeding with the operation. Set to `all` or any non-negative integer
up to the total number of copies of each shard in the index
(`number_of_replicas+1`). Defaults to `1`, meaning to wait just for each
primary shard to be active.

See index-wait-for-active-shards.

#### Examples

```console
POST /my-index-000001/_disk_usage?run_expensive_tasks=true
```

The API returns:

```console-response
{
    "_shards": {
        "total": 1,
        "successful": 1,
        "failed": 0
    },
    "my-index-000001": {
        "store_size": "929mb", <1>
        "store_size_in_bytes": 974192723,
        "all_fields": {
            "total": "928.9mb", <2>
            "total_in_bytes": 973977084,
            "inverted_index": {
                "total": "107.8mb",
                "total_in_bytes": 113128526
            },
            "stored_fields": "623.5mb",
            "stored_fields_in_bytes": 653819143,
            "doc_values": "125.7mb",
            "doc_values_in_bytes": 131885142,
            "points": "59.9mb",
            "points_in_bytes": 62885773,
            "norms": "2.3kb",
            "norms_in_bytes": 2356,
            "term_vectors": "2.2kb",
            "term_vectors_in_bytes": 2310,
            "knn_vectors": "0b",
            "knn_vectors_in_bytes": 0
        },
        "fields": {
            "_id": {
                "total": "49.3mb",
                "total_in_bytes": 51709993,
                "inverted_index": {
                    "total": "29.7mb",
                    "total_in_bytes": 31172745
                },
                "stored_fields": "19.5mb", <3>
                "stored_fields_in_bytes": 20537248,
                "doc_values": "0b",
                "doc_values_in_bytes": 0,
                "points": "0b",
                "points_in_bytes": 0,
                "norms": "0b",
                "norms_in_bytes": 0,
                "term_vectors": "0b",
                "term_vectors_in_bytes": 0,
                "knn_vectors": "0b",
                "knn_vectors_in_bytes": 0
            },
            "_primary_term": {...},
            "_seq_no": {...},
            "_version": {...},
            "_source": {
                "total": "603.9mb",
                "total_in_bytes": 633281895,
                "inverted_index": {...},
                "stored_fields": "603.9mb", <4>
                "stored_fields_in_bytes": 633281895,
                "doc_values": "0b",
                "doc_values_in_bytes": 0,
                "points": "0b",
                "points_in_bytes": 0,
                "norms": "0b",
                "norms_in_bytes": 0,
                "term_vectors": "0b",
                "term_vectors_in_bytes": 0,
                "knn_vectors": "0b",
                "knn_vectors_in_bytes": 0
            },
            "context": {
                "total": "28.6mb",
                "total_in_bytes": 30060405,
                "inverted_index": {
                    "total": "22mb",
                    "total_in_bytes": 23090908
                },
                "stored_fields": "0b",
                "stored_fields_in_bytes": 0,
                "doc_values": "0b",
                "doc_values_in_bytes": 0,
                "points": "0b",
                "points_in_bytes": 0,
                "norms": "2.3kb",
                "norms_in_bytes": 2356,
                "term_vectors": "2.2kb",
                "term_vectors_in_bytes": 2310,
                "knn_vectors": "0b",
                "knn_vectors_in_bytes": 0
            },
            "context.keyword": {...},
            "message": {...},
            "message.keyword": {...}
        }
    }
}
```

<1> The store size of only analyzed shards of the index.

<2> The total size of fields of the analyzed shards of the index. This total
is usually smaller than the index size specified in <1> as some small metadata
files are ignored and some parts of data files might not be scanned by the API.

<3> The stored size of the `_id` field

<4> The stored size of the `_source` field. As stored fields are stored
together in a compressed format, the sizes of stored fields are
estimates and can be inaccurate. The stored size of the `_id` field
is likely underestimated while the `_source` field is overestimated.
