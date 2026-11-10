<!-- Converted from ilm/apis/retry-policy.asciidoc (AsciiDoc). Includes are inlined. -->

### Retry policy execution API

**New API reference**
For the most up-to-date API details, refer to [Index lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ilm).

Retry executing the lifecycle policy for an index that is in the ERROR step.

#### Request

`POST <index>/_ilm/retry`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage_ilm`
privileges on the indices being managed to use this API. For more information,
see security-privileges.

#### Description

Sets the policy back to the step where the error occurred and executes the step.
Use the ILM Explain API to determine if an index is in the ERROR
step.

#### Path parameters

`<index>`::
  (Required, string) Identifier for the indices to retry in comma-separated format.

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

The following example retries the policy for `my-index-000001`.

```js
POST my-index-000001/_ilm/retry
```

If the request succeeds, you receive the following result:

```js
{
  "acknowledged": true
}
```
