<!-- Converted from ilm/apis/stop.asciidoc (AsciiDoc). Includes are inlined. -->

### Stop index lifecycle management API

**New API reference**
For the most up-to-date API details, refer to [Index lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ilm).

Stop the index lifecycle management (ILM) plugin.

#### Request

`POST /_ilm/stop`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage_ilm`
cluster privilege to use this API. For more information, see
security-privileges.

#### Description

Halts all lifecycle management operations and stops the ILM plugin. This
is useful when you are performing maintenance on the cluster and need to prevent
ILM from performing any actions on your indices.

The API returns as soon as the stop request has been acknowledged, but the
plugin might continue to run until in-progress operations complete and the plugin
can be safely stopped. Use the  Get ILM Status API to see
if ILM is running.

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

The following example stops the ILM plugin.

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "phases": {
      "warm": {
        "min_age": "10d",
        "actions": {
          "forcemerge": {
            "max_num_segments": 1
          }
        }
      },
      "delete": {
        "min_age": "30d",
        "actions": {
          "delete": {}
        }
      }
    }
  }
}

PUT my-index-000001
```

```console
POST _ilm/stop
```

If the request does not encounter errors, you receive the following result:

```console-result
{
  "acknowledged": true
}
```

```console
POST _ilm/start
```
