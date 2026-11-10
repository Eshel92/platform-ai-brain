<!-- Converted from indices/apis/reload-analyzers.asciidoc (AsciiDoc). Includes are inlined. -->

## Reload search analyzers API

**New API reference**
For the most up-to-date API details, refer to [Reload search analyzers](https://www.elastic.co/docs/api/doc/elasticsearch/operation/operation-indices-reload-search-analyzers).

Reloads an index's search analyzers and their resources.
For data streams, the API reloads search analyzers and resources for the
stream's backing indices.

```console
POST /my-index-000001/_reload_search_analyzers
POST /my-index-000001/_cache/clear?request=true
```

**Important:** After reloading the search analyzers you should clear the request
           cache to make sure it doesn't contain responses derived from the
           previous versions of the analyzer.

### Request

`POST /<target>/_reload_search_analyzers`

`GET /<target>/_reload_search_analyzers`

### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the target data stream, index,
or alias.

### Description

You can use the reload search analyzers API
to pick up changes to synonym files
used in the `synonym_graph`
or `synonym` token filter
of a search analyzer.
To be eligible,
the token filter must have an `updateable` flag of `true`
and only be used in search analyzers.

**Note:**
This API does not perform a reload
for each shard of an index.
Instead,
it performs a reload for each node
containing index shards.
As a result,
the total shard count returned by the API
can differ from the number of index shards.

Because reloading affects every node with an index shard,
its important to update the synonym file
on every data node in the cluster,
including nodes that don't contain a shard replica,
before using this API.
This ensures the synonym file is updated
everywhere in the cluster
in case shards are relocated
in the future.

### Path parameters

`<target>`::
(Required, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, use `*` or `_all`.

### Query parameters

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

### Examples

Use the create index API
to create an index with a search analyzer
that contains an updateable synonym filter.

**Note:** Using the following analyzer as an index analyzer results in an error.

```console
PUT /my-index-000001
{
  "settings": {
    "index": {
      "analysis": {
        "analyzer": {
          "my_synonyms": {
            "tokenizer": "whitespace",
            "filter": [ "synonym" ]
          }
        },
        "filter": {
          "synonym": {
            "type": "synonym_graph",
            "synonyms_path": "analysis/synonym.txt",  <1>
            "updateable": true                        <2>
          }
        }
      }
    }
  },
  "mappings": {
    "properties": {
      "text": {
        "type": "text",
        "analyzer": "standard",
        "search_analyzer": "my_synonyms"              <3>
      }
    }
  }
}
```

<1> Includes a synonym file.
<2> Marks the token filter as updateable.
<3> Marks the analyzer as a search analyzer.

After updating the synonym file,
use the analyzer reload API
to reload the search analyzer
and pick up the file changes.

```console
POST /my-index-000001/_reload_search_analyzers
```

The API returns the following response.

```console-result
{
  "_shards": {
    "total": 2,
    "successful": 2,
    "failed": 0
  },
  "reload_details": [
    {
      "index": "my-index-000001",
      "reloaded_analyzers": [
        "my_synonyms"
      ],
      "reloaded_node_ids": [
        "mfdqTXn_T7SGr2Ho2KT8uw"
      ]
    }
  ]
}
```
