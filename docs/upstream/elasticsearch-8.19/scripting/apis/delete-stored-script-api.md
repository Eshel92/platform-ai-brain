<!-- Converted from scripting/apis/delete-stored-script-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete stored script API

**New API reference**
For the most up-to-date API details, refer to [Script APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-script).

Deletes a stored script or <<search-template,search
template>>.

```console
DELETE _scripts/my-stored-script
```

#### Request

`DELETE _scripts/<script-id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

#### Path parameters

`<script-id>`::
(Required, string)
Identifier for the stored script or search template.

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
