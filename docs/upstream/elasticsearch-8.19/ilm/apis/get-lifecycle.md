<!-- Converted from ilm/apis/get-lifecycle.asciidoc (AsciiDoc). Includes are inlined. -->

### Get lifecycle policy API

**New API reference**
For the most up-to-date API details, refer to [Index lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ilm).

Retrieves a lifecycle policy.

#### Request

`GET _ilm/policy`

`GET _ilm/policy/<policy_id>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage_ilm` or
`read_ilm` or both cluster privileges to use this API. For more information, see
security-privileges.

#### Description

Returns the specified policy definition. Includes the policy version and last
modified date. If no policy is specified, returns all defined policies.

#### Path parameters

`<policy_id>`::
  (Optional, string) Identifier for the policy.

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

The following example retrieves `my_policy`:

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
GET _ilm/policy/my_policy
```

If the request succeeds, the body of the response contains the policy definition:

```console-result
{
  "my_policy": {
    "version": 1, <1>
    "modified_date": 82392349, <2>
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
            "delete": {
              "delete_searchable_snapshot": true
            }
          }
        }
      }
    },
    "in_use_by" : { <3>
      "indices" : [],
      "data_streams" : [],
      "composable_templates" : []
    }
  }
}
```

<1> The policy version is incremented whenever the policy is updated
<2> When this policy was last modified
<3> Which indices, data streams, or templates currently use this policy
