<!-- Converted from ilm/apis/start.asciidoc (AsciiDoc). Includes are inlined. -->

### Start index lifecycle management API

**New API reference**
For the most up-to-date API details, refer to [Index lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ilm).

Start the index lifecycle management (ILM) plugin.

#### Request

`POST /_ilm/start`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage_ilm`
cluster privilege to use this API. For more information, see
security-privileges.

#### Description

Starts the ILM plugin if it is currently stopped. ILM is started
automatically when the cluster is formed. Restarting ILM is only
necessary if it has been stopped using the Stop ILM API.

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

The following example starts the ILM plugin.

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

POST _ilm/stop
```

```console
POST _ilm/start
```

If the request succeeds, you receive the following result:

```console-result
{
  "acknowledged": true
}
```
