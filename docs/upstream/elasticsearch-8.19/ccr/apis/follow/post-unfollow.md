<!-- Converted from ccr/apis/follow/post-unfollow.asciidoc (AsciiDoc). Includes are inlined. -->

### Unfollow API

**New API reference**
For the most up-to-date API details, refer to [Cross-cluster replication APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ccr).

Converts a cross-cluster replication follower index to a regular index.

#### Request

```console
PUT /follower_index/_ccr/follow?wait_for_active_shards=1
{
  "remote_cluster" : "remote_cluster",
  "leader_index" : "leader_index"
}

POST /follower_index/_ccr/pause_follow

POST /follower_index/_close
```

```console
POST /<follower_index>/_ccr/unfollow
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `manage_follow_index`
index privileges for the follower index. For more information, see
security-privileges.

#### Description

This API stops the following task associated with a follower index and removes
index metadata and settings associated with cross-cluster replication. This enables the index to
treated as a regular index. The follower index must be paused and closed before
invoking the unfollow API.

**Note:** Currently cross-cluster replication does not support converting an existing regular index to a
follower index. Converting a follower index to a regular index is an
irreversible operation.

#### Path parameters

`<follower_index>`::
  (Required, string) The name of the follower index.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

This example converts `follower_index` from a follower index to a regular index:

```console
POST /follower_index/_ccr/unfollow
```

The API returns the following result:

```console-result
{
  "acknowledged" : true
}
```
