<!-- Converted from ilm/apis/put-lifecycle.asciidoc (AsciiDoc). Includes are inlined. -->

### Create or update lifecycle policy API

**New API reference**
For the most up-to-date API details, refer to [Index lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ilm).

Creates or updates lifecycle policy. See ilm-index-lifecycle for
definitions of policy components.

#### Request

`PUT _ilm/policy/<policy_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage_ilm`
cluster privilege to use this API. You must also have the `manage` index
privilege on all indices being managed by `policy`. ILM performs
operations as the user who last updated the policy. ILM only has the
roles assigned to the user at the time of the last policy
update.

#### Description

Creates a lifecycle policy. If the specified policy exists, the policy is
replaced and the policy version is incremented.

**Note:** Only the latest version of the policy is stored, you cannot revert to
previous versions.

#### Path parameters

`<policy_id>`::
  (Required, string) Identifier for the policy.

**Important:**
To avoid naming collisions with built-in and Fleet-managed ILM policies, avoid using `@` as part of the id of your own ILM policies.

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

The following example creates a new policy named `my_policy`. In addition, you can use the
`_meta` parameter to add arbitrary metadata to the policy, the `_meta` parameter is optional
and not automatically generated or used by Elasticsearch. To unset `_meta`, replace the policy
without specifying one. To check the `_meta`, you can use the Get lifecycle policy API.

```console
PUT _ilm/policy/my_policy
{
  "policy": {
    "_meta": {
      "description": "used for nginx log",
      "project": {
        "name": "myProject",
        "department": "myDepartment"
      }
    },
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

If the request succeeds, you receive the following result:

```console-result
{
  "acknowledged": true
}
```
