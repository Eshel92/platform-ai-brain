<!-- Converted from ilm/apis/get-status.asciidoc (AsciiDoc). Includes are inlined. -->

### Get index lifecycle management status API

**New API reference**
For the most up-to-date API details, refer to [Index lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ilm).

Retrieves the current index lifecycle management (ILM) status.

You can start or stop ILM with the start ILM and
stop ILM APIs.

#### Request

`GET /_ilm/status`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage_ilm` or
`read_ilm` or both cluster privileges to use this API. For more information, see
security-privileges.

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

#### Response body

`operation_mode`::
(string) Current operation mode for ILM.
**Possible values for `operation_mode`**
`RUNNING`::
ILM is running.

`STOPPING`::
ILM is finishing sensitive actions, such as shrink, that
are in progress. When these actions finish, ILM will move to `STOPPED`.

`STOPPED`::
ILM is not running.

#### Examples

The following example gets the ILM plugin status.

```console
GET _ilm/status
```

If the request succeeds, the body of the response shows the operation mode:

```console-result
{
  "operation_mode": "RUNNING"
}
```
