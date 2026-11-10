<!-- Converted from slm/apis/slm-get-status.asciidoc (AsciiDoc). Includes are inlined. -->

### Get snapshot lifecycle management status API

**New API reference**
For the most up-to-date API details, refer to [Snapshot lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-slm).

Retrieves the status of snapshot lifecycle management (SLM).

#### Request

`GET /_slm/status`

#### Description

Returns the status of the SLM plugin. 
The `operation_mode` field in the response shows one of three states: 
`RUNNING`, `STOPPING`, or `STOPPED`. 
You halt and restart the SLM plugin with the
stop and start  APIs.

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

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the 
`manage_slm` or `read_slm` cluster privileges to use this API. 
For more information, see security-privileges.

#### Examples

```console
GET _slm/status
```

The API returns the following result:

```console-result
{
  "operation_mode": "RUNNING"
}
```
