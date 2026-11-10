<!-- Converted from slm/apis/slm-stop.asciidoc (AsciiDoc). Includes are inlined. -->

### Stop snapshot lifecycle management API

**New API reference**
For the most up-to-date API details, refer to [Snapshot lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-slm).

Turn off snapshot lifecycle management (SLM).

#### Request

`POST /_slm/stop`

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the `manage_slm`
cluster privilege to use this API. For more information, see
security-privileges.

#### Description

Halts all snapshot lifecycle management (SLM) operations and stops the SLM plugin.
This is useful when you are performing maintenance on a cluster and need to
prevent SLM from performing any actions on your data streams or indices. 
Stopping SLM does not stop any snapshots that are in progress.
You can manually trigger snapshots with the slm-api-execute-lifecycle even if SLM is stopped.

The API returns a response as soon as the request is acknowledged, but 
the plugin might continue to run until in-progress operations complete and it can be safely stopped. 

Use the  slm-api-get-status to see if SLM is running. 

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

```console
POST _slm/stop
```
