<!-- Converted from indices/update-settings.asciidoc (AsciiDoc). Includes are inlined. -->

### Update index settings API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Changes a dynamic index setting in real time.

For data streams, index setting changes are applied to all backing indices by
default.

```console
PUT /my-index-000001/_settings
{
  "index" : {
    "number_of_replicas" : 2
  }
}
```

#### Request

`PUT /<target>/_settings`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the target data stream, index,
or alias.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, omit this parameter or use `*` or `_all`.

#### Query parameters

`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
Defaults to `false`.

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

`flat_settings`::
(Optional, Boolean) If `true`, returns settings in flat format. Defaults to
`false`.
`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`preserve_existing`::
(Optional, Boolean) If `true`, existing index settings remain unchanged.
Defaults to `false`.

`reopen`::
(Optional, Boolean) If `true`, then any static settings that would ordinarily only
be updated on closed indices will be updated by automatically closing and reopening
the affected indices. If `false`, attempts to update static settings on open indices
will fail. Defaults to `false`.

**Note:** Changing index settings on an automatically closed index using the `reopen`
parameter will result in the index becoming unavailable momentarily while the index
is in the process of reopening.

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

`timeout`::
(Optional, time units) Period to wait for a response from all relevant nodes in the cluster after updating the cluster metadata.
If no response is received before the timeout expires, the cluster metadata update still applies but the response will indicate that it was not completely acknowledged.
Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Request body

`settings`::
(Optional, index setting object) Configuration
options for the index. See index-modules-settings.

#### Examples

##### Reset an index setting

To revert a setting to the default value, use `null`. For example:

```console
PUT /my-index-000001/_settings
{
  "index" : {
    "refresh_interval" : null
  }
}
```

The list of per-index settings which can be updated dynamically on live
indices can be found in index-modules.
To preserve existing settings from being updated, the `preserve_existing`
request parameter can be set to `true`.

##### Bulk indexing usage

For example, the update settings API can be used to dynamically change
the index from being more performant for bulk indexing, and then move it
to more real time indexing state. Before the bulk indexing is started,
use:

```console
PUT /my-index-000001/_settings
{
  "index" : {
    "refresh_interval" : "-1"
  }
}
```

(Another optimization option is to start the index without any replicas,
and only later adding them, but that really depends on the use case).

Then, once bulk indexing is done, the settings can be updated (back to
the defaults for example):

```console
PUT /my-index-000001/_settings
{
  "index" : {
    "refresh_interval" : "1s"
  }
}
```

And, a force merge should be called:

```console
POST /my-index-000001/_forcemerge?max_num_segments=5
```

##### Update index analysis

You can only define new analyzers on closed indices.

To add an analyzer,
you must close the index,
define the analyzer,
and reopen the index.

**Note:**
You cannot close the write index of a data stream.

To update the analyzer for a data stream's write index and future backing
indices, update the analyzer in the <<create-index-template,index
template used by the stream>>. Then <<manually-roll-over-a-data-stream,roll over
the data stream>> to apply the new analyzer to the stream’s write index and
future backing indices. This affects searches and any new data added to the
stream after the rollover. However, it does not affect the data stream's backing
indices or their existing data.

To change the analyzer for existing backing indices, you must create a
new data stream and reindex your data into it. See
data-streams-use-reindex-to-change-mappings-settings.

For example,
the following commands add the `content` analyzer to the `my-index-000001` index:

```console
POST /my-index-000001/_close

PUT /my-index-000001/_settings
{
  "analysis" : {
    "analyzer":{
      "content":{
        "type":"custom",
        "tokenizer":"whitespace"
      }
    }
  }
}

POST /my-index-000001/_open
```
