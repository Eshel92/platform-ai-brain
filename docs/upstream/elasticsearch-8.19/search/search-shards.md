<!-- Converted from search/search-shards.asciidoc (AsciiDoc). Includes are inlined. -->

### Search shards API

**New API reference**
For the most up-to-date API details, refer to [Search APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-search).

Returns the indices and shards that a search request would be executed against.

```console
GET /my-index-000001/_search_shards
```

#### Request

`GET /<target>/_search_shards`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`view_index_metadata` or `manage` index privilege
for the target data stream, index, or alias.

#### Description

The search shards api returns the indices and shards that a search request would
be executed against. This can give useful feedback for working out issues or
planning optimizations with routing and shard preferences. When filtered aliases
are used, the filter is returned as part of the `indices` section.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases to
search. Supports wildcards (`*`). To search all data streams and indices, omit
this parameter or use `*` or `_all`.

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

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`local`::
(Optional, Boolean) If `true`, the request retrieves information from the local
node only. Defaults to `false`, which means information is retrieved from
the master node.
`preference`::
(Optional, string) Specifies the node or shard the operation should be
performed on. Random by default.
`routing`::
(Optional, string)
Custom value used to route operations to a specific shard.
`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

```console
GET /my-index-000001/_search_shards
```

The API returns the following result:

```console-result
{
  "nodes": ...,
  "indices" : {
    "my-index-000001": { }
  },
  "shards": [
    [
      {
        "index": "my-index-000001",
        "node": "JklnKbD7Tyqi9TP3_Q_tBg",
        "relocating_node": null,
        "primary": true,
        "shard": 0,
        "state": "STARTED",
        "allocation_id": {"id":"0TvkCyF7TAmM1wHP4a42-A"},
        "relocation_failure_info" : {
          "failed_attempts" : 0
        }
      }
    ],
    [
      {
        "index": "my-index-000001",
        "node": "JklnKbD7Tyqi9TP3_Q_tBg",
        "relocating_node": null,
        "primary": true,
        "shard": 1,
        "state": "STARTED",
        "allocation_id": {"id":"fMju3hd1QHWmWrIgFnI4Ww"},
        "relocation_failure_info" : {
          "failed_attempts" : 0
        }
      }
    ],
    [
      {
        "index": "my-index-000001",
        "node": "JklnKbD7Tyqi9TP3_Q_tBg",
        "relocating_node": null,
        "primary": true,
        "shard": 2,
        "state": "STARTED",
        "allocation_id": {"id":"Nwl0wbMBTHCWjEEbGYGapg"},
        "relocation_failure_info" : {
          "failed_attempts" : 0
        }
      }
    ],
    [
      {
        "index": "my-index-000001",
        "node": "JklnKbD7Tyqi9TP3_Q_tBg",
        "relocating_node": null,
        "primary": true,
        "shard": 3,
        "state": "STARTED",
        "allocation_id": {"id":"bU_KLGJISbW0RejwnwDPKw"},
        "relocation_failure_info" : {
          "failed_attempts" : 0
        }
      }
    ],
    [
      {
        "index": "my-index-000001",
        "node": "JklnKbD7Tyqi9TP3_Q_tBg",
        "relocating_node": null,
        "primary": true,
        "shard": 4,
        "state": "STARTED",
        "allocation_id": {"id":"DMs7_giNSwmdqVukF7UydA"},
        "relocation_failure_info" : {
          "failed_attempts" : 0
        }
      }
    ]
  ]
}
```

Specifying the same request, this time with a routing value:

```console
GET /my-index-000001/_search_shards?routing=foo,bar
```

The API returns the following result:

```console-result
{
  "nodes": ...,
  "indices" : {
      "my-index-000001": { }
  },
  "shards": [
    [
      {
        "index": "my-index-000001",
        "node": "JklnKbD7Tyqi9TP3_Q_tBg",
        "relocating_node": null,
        "primary": true,
        "shard": 2,
        "state": "STARTED",
        "allocation_id": {"id":"fMju3hd1QHWmWrIgFnI4Ww"},
        "relocation_failure_info" : {
          "failed_attempts" : 0
        }
      }
    ],
    [
      {
        "index": "my-index-000001",
        "node": "JklnKbD7Tyqi9TP3_Q_tBg",
        "relocating_node": null,
        "primary": true,
        "shard": 3,
        "state": "STARTED",
        "allocation_id": {"id":"0TvkCyF7TAmM1wHP4a42-A"},
        "relocation_failure_info" : {
          "failed_attempts" : 0
        }
      }
    ]
  ]
}
```

Because of the specified routing values,
the search is only executed against two of the shards.
