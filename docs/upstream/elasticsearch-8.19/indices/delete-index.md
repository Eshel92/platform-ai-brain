<!-- Converted from indices/delete-index.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete index API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Deletes one or more indices.

```console
DELETE /my-index-000001
```

#### Request

`DELETE /<index>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `delete_index`
or `manage` index privilege for the target index.

#### Description

Deleting an index deletes its documents, shards, and metadata. It does not
delete related Kibana components, such as {data-sources}, visualizations, or
dashboards.

You cannot delete the current write index of a data stream. To delete the
index, you must roll over the data stream so a new
write index is created. You can then use the delete index API to delete the
previous write index.

#### Path parameters

`<index>`::
(Required, string) Comma-separated list of indices to delete. You cannot specify
index aliases.
By default, this parameter does not support wildcards (`*`) or `_all`. To use
wildcards or `_all`, set the
`action.destructive_requires_name` cluster
setting to `false`.

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
Defaults to `open,closed`.

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
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
