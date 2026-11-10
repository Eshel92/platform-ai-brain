<!-- Converted from ilm/apis/remove-policy-from-index.asciidoc (AsciiDoc). Includes are inlined. -->

### Remove policy from index API

**New API reference**
For the most up-to-date API details, refer to [Index lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ilm).

Removes assigned lifecycle policies from an index or a data stream's backing
indices.

#### Request

`POST <target>/_ilm/remove`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage_ilm`
privileges on the indices being managed to use this API. For more information,
see security-privileges.

#### Description

For indices, the remove lifecycle policy API removes the assigned lifecycle
policy and stops managing the specified index.

For data streams, the API removes any assigned lifecycle policies from 
the stream's backing indices and stops managing the indices.

#### Path parameters

`<target>`::
(Required, string) Comma-separated list of data streams, indices, and aliases to
target. Supports wildcards (`*`). To target all data streams and indices, use
`*` or `_all`.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

The following example removes the assigned policy from `my-index-000001`.

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
{
  "settings": {
    "index.lifecycle.name": "my_policy"
  }
}
```

```console
POST my-index-000001/_ilm/remove
```

If the request succeeds, you receive the following result:

```console-result
{
  "has_failures" : false,
  "failed_indexes" : []
}
```
