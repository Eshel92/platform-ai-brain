<!-- Converted from ccr/apis/follow/post-pause-follow.asciidoc (AsciiDoc). Includes are inlined. -->

### Pause follower API

**New API reference**
For the most up-to-date API details, refer to [Cross-cluster replication APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ccr).

Pauses a cross-cluster replication follower index.

#### Request

```console
PUT /follower_index/_ccr/follow?wait_for_active_shards=1
{
  "remote_cluster" : "remote_cluster",
  "leader_index" : "leader_index"
}
```

```console
POST /<follower_index>/_ccr/pause_follow
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `manage_ccr` cluster
privileges on the cluster that contains the follower index. For more information,
see security-privileges.

#### Description

This API pauses a follower index. When this API returns, the follower index will
not fetch any additional operations from the leader index. You can resume
following with the resume follower API. Pausing and
resuming a follower index can be used to change the configuration of the
following task.

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

This example pauses a follower index named `follower_index`:

```console
POST /follower_index/_ccr/pause_follow
```

The API returns the following result:

```console-result
{
  "acknowledged" : true
}
```
