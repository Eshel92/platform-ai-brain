<!-- Converted from indices/delete-alias.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete alias API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Removes a data stream or index from an alias.

```console
DELETE my-data-stream/_alias/my-alias
```

#### Request

`DELETE <target>/_alias/<alias>`

`DELETE <target>/_aliases/<alias>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the alias and it data streams or
indices.

#### Path parameters

`<alias>`::
(Required, string) Comma-separated list of aliases to remove. Supports wildcards
(`*`). To remove all aliases, use `*` or `_all`.

`<target>`::
(Required, string) Comma-separated list of data streams or indices used to limit
the request. Supports wildcards (`*`).

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
