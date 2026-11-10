<!-- Converted from indices/close.asciidoc (AsciiDoc). Includes are inlined. -->

### Close index API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Closes an index.

```console
POST /my-index-000001/_close
```

#### Request

`POST /<index>/_close`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the target index or index alias.

#### Description

You use the close index API to close open indices.

A closed index is blocked for read/write operations and does not allow
all operations that opened indices allow. It is not possible to index
documents or to search for documents in a closed index. This allows
closed indices to not have to maintain internal data structures for
indexing or searching documents, resulting in a smaller overhead on
the cluster.

When opening or closing an index, the master is responsible for
restarting the index shards to reflect the new state of the index.
The shards will then go through the normal recovery process. The
data of opened/closed indices is automatically replicated by the
cluster to ensure that enough shard copies are safely kept around
at all times.

You can open and close multiple indices. An error is thrown
if the request explicitly refers to a missing index. This behaviour can be
disabled using the `ignore_unavailable=true` parameter.

By default, you must explicitly name the indices you are opening or closing.
To open or close indices with `_all`, `*`, or other wildcard
expressions, change the `action.destructive_requires_name` setting to `false`.
This setting can also be changed via the cluster update settings api.

Closed indices consume a significant amount of disk-space which can cause
problems in managed environments. Closing indices can be disabled via the cluster settings
API by setting `cluster.indices.close.enable` to `false`. The default is `true`.

#### Path parameters

`<index>`::
(Optional, string) Comma-separated list or wildcard expression of index names
used to limit the request.
To close all indices, use `_all` or `*`.
By default, you must explicitly name the indices you are closing.
To specify indices to close with `_all`, `*`, or other wildcard
expressions, change the `action.destructive_requires_name` setting to `false`.
You can update this setting in the `elasticsearch.yml` file
or using the cluster update settings API.

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
`wait_for_active_shards`::
(Optional, string) The number of copies of each shard that must be active
before proceeding with the operation. Set to `all` or any non-negative integer
up to the total number of copies of each shard in the index
(`number_of_replicas+1`). Defaults to `1`, meaning to wait just for each
primary shard to be active.

See index-wait-for-active-shards.
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

#### Examples

The following example shows how to close an index:

```console
POST /my-index-000001/_close
```

The API returns following response:

```console-result
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "indices": {
    "my-index-000001": {
      "closed": true
    }
  }
}
```
