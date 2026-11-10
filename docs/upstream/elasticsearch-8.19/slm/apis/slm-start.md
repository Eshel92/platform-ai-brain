<!-- Converted from slm/apis/slm-start.asciidoc (AsciiDoc). Includes are inlined. -->

### Start snapshot lifecycle management API

**New API reference**
For the most up-to-date API details, refer to [Snapshot lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-slm).

Turns on snapshot lifecycle management (SLM).

#### Request

`POST /_slm/start`

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the `manage_slm`
cluster privilege to use this API. For more information, see
security-privileges.

#### Description

Starts the SLM plugin if it's not running. 
SLM starts automatically when a cluster is formed. 
Manually starting SLM is only necessary if it has been stopped using the slm-api-stop.

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

#### Examples

Start the SLM plugin:

```console
POST _slm/start
```

If successful, this request returns:

```console-result
{
  "acknowledged": true
}
```
