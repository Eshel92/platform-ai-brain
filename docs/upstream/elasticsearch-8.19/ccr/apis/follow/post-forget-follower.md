<!-- Converted from ccr/apis/follow/post-forget-follower.asciidoc (AsciiDoc). Includes are inlined. -->

### Forget follower API

**New API reference**
For the most up-to-date API details, refer to [Cross-cluster replication APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ccr).

Removes the cross-cluster replication follower retention leases from the leader.

#### Request

```console
PUT /follower_index/_ccr/follow?wait_for_active_shards=1
{
  "remote_cluster" : "remote_cluster",
  "leader_index" : "leader_index"
}
```

```console
POST /follower_index/_ccr/pause_follow
```

```console
POST /<leader_index>/_ccr/forget_follower
{
  "follower_cluster" : "<follower_cluster>",
  "follower_index" : "<follower_index>",
  "follower_index_uuid" : "<follower_index_uuid>",
  "leader_remote_cluster" : "<leader_remote_cluster>"
}
```

```console-result
{
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "failed" : 0,
    "failures" : [ ]
  }
}
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `manage_leader_index`
index privileges for the leader index. For more information, see
security-privileges.

#### Description

A following index takes out retention leases on its leader index. These
retention leases are used to increase the likelihood that the shards of the
leader index retain the history of operations that the shards of the following
index need to execute replication. When a follower index is converted to a
regular index via the unfollow API (either via explicit
execution of this API, or implicitly via index lifecycle management), these retention leases are
removed. However, removing these retention leases can fail (e.g., if the remote
cluster containing the leader index is unavailable). While these retention
leases will eventually expire on their own, their extended existence can cause
the leader index to hold more history than necessary, and prevent index lifecycle management from
performing some operations on the leader index. This API exists to enable
manually removing these retention leases when the unfollow API was unable to do
so.

**Note:** This API does not stop replication by a following index. If you use this
API targeting a follower index that is still actively following, the following
index will add back retention leases on the leader. The only purpose of this API
is to handle the case of failure to remove the following retention leases after
the unfollow API is invoked.

#### Path parameters

`<leader_index>`::
  (Required, string) The name of the leader index.

#### Query parameters

`timeout`::
(Optional, time) Controls the amount of time to wait for results. Defaults to unlimited.

#### Request body

`follower_cluster`::
  (Required, string) The name of the cluster containing the follower index.

`follower_index`::
  (Required, string) The name of the follower index.

`follower_index_uuid`::
  (Required, string) The UUID of the follower index.

`leader_remote_cluster`::
  (Required, string) The alias (from the perspective of the cluster containing
  the follower index) of the remote cluster
  containing the leader index.

#### Examples

This example removes the follower retention leases for `follower_index` from
`leader_index`.

```console
POST /leader_index/_ccr/forget_follower
{
  "follower_cluster" : "follower_cluster",
  "follower_index" : "follower_index",
  "follower_index_uuid" : "vYpnaWPRQB6mNspmoCeYyA",
  "leader_remote_cluster" : "leader_cluster"
}
```

The API returns the following result:

```console-result
{
  "_shards" : {
    "total" : 1,
    "successful" : 1,
    "failed" : 0,
    "failures" : [ ]
  }
}
```
