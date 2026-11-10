<!-- Converted from ccr/apis/auto-follow/get-auto-follow-pattern.asciidoc (AsciiDoc). Includes are inlined. -->

### Get auto-follow pattern API

**New API reference**
For the most up-to-date API details, refer to [Cross-cluster replication APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ccr).

Get cross-cluster replication auto-follow patterns.

#### Request

```console
PUT /_ccr/auto_follow/my_auto_follow_pattern
{
  "remote_cluster" : "remote_cluster",
  "leader_index_patterns" :
  [
    "leader_index*"
  ],
  "leader_index_exclusion_patterns":
  [
    "leader_index_001"
  ],
  "follow_index_pattern" : "{{leader_index}}-follower"
}
```

```console
DELETE /_ccr/auto_follow/my_auto_follow_pattern
```

```console
GET /_ccr/auto_follow/
```

```console
GET /_ccr/auto_follow/<auto_follow_pattern_name>
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `manage_ccr` cluster
privileges on the cluster that contains the follower index. For more information,
see security-privileges.

#### Description

This API gets configured auto-follow patterns.
This API will return the specified auto-follow pattern collection.

#### Path parameters

`<auto_follow_pattern_name>`::
  (Optional, string) Specifies the auto-follow pattern collection that you want
  to retrieve. If you do not specify a name, the API returns information for all
  collections.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

This example retrieves information about an auto-follow pattern collection
named `my_auto_follow_pattern`:

```console
GET /_ccr/auto_follow/my_auto_follow_pattern
```

The API returns the following result:

```console-result
{
  "patterns": [
    {
      "name": "my_auto_follow_pattern",
      "pattern": {
        "active": true,
        "remote_cluster" : "remote_cluster",
        "leader_index_patterns" :
        [
          "leader_index*"
        ],
        "leader_index_exclusion_patterns":
        [
          "leader_index_001"
        ],
        "follow_index_pattern" : "{{leader_index}}-follower"
      }
    }
  ]
}
```
