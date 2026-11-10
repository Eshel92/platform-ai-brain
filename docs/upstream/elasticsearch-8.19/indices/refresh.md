<!-- Converted from indices/refresh.asciidoc (AsciiDoc). Includes are inlined. -->

### Refresh API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

A refresh makes recent operations performed on one or more indices available for
search. For data streams, the API runs the refresh operation on the stream's
backing indices. For more information about the refresh operation, see
near-real-time.

```console
POST /my-index-000001/_refresh
```

#### Request

`POST <target>/_refresh`

`GET <target>/_refresh`

`POST /_refresh`

`GET /_refresh`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `maintenance`
or `manage` index privilege for the target data
stream, index, or alias.

#### Description

Use the refresh API to explicitly make all operations performed on one or more
indices since the last refresh available for search.
If the request targets a data stream, it refreshes the stream's backing indices.

By default, Elasticsearch periodically refreshes indices every second, but only on
indices that have received one search request or more in the last 30 seconds.
You can change this default interval
using the `index.refresh_interval` setting.

Refresh requests are synchronous and do not return a response until the
refresh operation completes.

**Important:**
Refreshes are resource-intensive.
To ensure good cluster performance,
we recommend waiting for Elasticsearch's periodic refresh
rather than performing an explicit refresh
when possible.

If your application workflow
indexes documents and then runs a search
to retrieve the indexed document,
we recommend using the index API's
`refresh=wait_for` query parameter option.
This option ensures the indexing operation waits
for a periodic refresh
before running the search.

#### Path parameters

`<target>`::
(Optional, string)
Comma-separated list of data streams, indices, and aliases used to limit
the request. Supports wildcards (`*`). To target all data streams and indices,
omit this parameter or use `*` or `_all`.

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

#### Examples

##### Refresh several data streams and indices

```console
POST /my-index-000001,my-index-000002/_refresh
```

##### Refresh all data streams and indices in a cluster

```console
POST /_refresh
```
