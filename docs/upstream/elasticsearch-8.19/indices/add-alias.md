<!-- Converted from indices/add-alias.asciidoc (AsciiDoc). Includes are inlined. -->

### Create or update alias API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Adds a data stream or index to an alias.

```console
PUT my-data-stream/_alias/my-alias
```

#### Request

`POST <target>/_alias/<alias>`

`POST <target>/_aliases/<alias>`

`PUT <target>/_alias/<alias>`

`PUT <target>/_aliases/<alias>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the alias and its data streams
or indices.

#### Path parameters

`<alias>`::
(Required, string) Alias to update. If the alias doesn't exist, the request
creates it. Index alias names support date math.

`<target>`::
(Required, string) Comma-separated list of data streams or indices to add.
Supports wildcards (`*`). Wildcard patterns that match both data streams and
indices return an error.

#### Query parameters

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

`filter`::
(Optional, Query DSL object Query used to limit documents the
alias can access.
