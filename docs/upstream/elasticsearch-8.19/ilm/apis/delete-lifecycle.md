<!-- Converted from ilm/apis/delete-lifecycle.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete lifecycle policy API

**New API reference**
For the most up-to-date API details, refer to [Index lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ilm).

Deletes an index lifecycle policy.

#### Request

`DELETE _ilm/policy/<policy_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage_ilm`
cluster privilege to use this API. For more information, see
security-privileges.

#### Description

Deletes the specified lifecycle policy definition. You cannot delete policies
that are currently in use. If the policy is being used to manage any indices,
the request fails and returns an error.

#### Path parameters

`<policy_id>`::
  (Required, string) Identifier for the policy.

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

The following example deletes `my_policy`:

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
```

```console
DELETE _ilm/policy/my_policy
```

When the policy is successfully deleted, you receive the following result:

```console-result
{
  "acknowledged": true
}
```
