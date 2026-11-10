<!-- Converted from ccr/apis/follow/put-follow.asciidoc (AsciiDoc). Includes are inlined. -->

### Create follower API

**New API reference**
For the most up-to-date API details, refer to [Cross-cluster replication APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ccr).

Creates a cross-cluster replication follower index.

#### Request

```console
POST /follower_index/_ccr/pause_follow
```

```console
PUT /<follower_index>/_ccr/follow?wait_for_active_shards=1
{
  "remote_cluster" : "<remote_cluster>",
  "leader_index" : "<leader_index>"
}
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `write`, `monitor`,
and `manage_follow_index` index privileges for the follower index. You must have
`read` and `monitor` index privileges for the leader index. You must also have
`manage_ccr` cluster privileges on the cluster that contains the follower index.
For more information, see security-privileges.

#### Description

This API creates a new follower index that is configured to follow the
referenced leader index. When this API returns, the follower index exists, and
cross-cluster replication starts replicating operations from the leader index to the follower index.

#### Path parameters

`<follower_index>`::
  (Required, string) The name of the follower index.

#### Query parameters

`wait_for_active_shards`::
  (Optional, integer) Specifies the number of shards to wait on being active before
  responding. This defaults to waiting on none of the shards to be active. A
  shard must be restored from the leader index before being active. Restoring a
  follower shard requires transferring all the remote Lucene segment files to
  the follower index.

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Request body

[[ccr-put-follow-request-body-leader_index]]`leader_index`::
  (Required, string) The name of the index in the leader cluster to follow.

[[ccr-put-follow-request-body-remote_cluster]]`remote_cluster`::
  (Required, string) The remote cluster containing
  the leader index.

[[ccr-put-follow-request-body-data_stream_name]]`data_stream_name`::
  (Optional, string) If the leader index is part of a data stream, the name to
  which the local data stream for the followed index should be renamed. For example, A request like:

```console
PUT /.ds-logs-mysql-default_copy-2022-01-01-000001/_ccr/follow
{
  "remote_cluster" : "remote_cluster",
  "leader_index" : ".ds-logs-mysql-default-2022-01-01-000001",
  "data_stream_name": "logs-mysql-default_copy"
}
```

Replicates the leader index `.ds-logs-mysql-default-2022-01-01-000001` into the follower index
`.ds-logs-mysql-default_copy-2022-01-01-000001` and will do so using the data stream
`logs-mysql-default_copy`, as opposed to the original leader data stream name of
`logs-mysql-default`.

(See `ccr/apis/follow/../follow-request-body.md`)

#### Examples

This example creates a follower index named `follower_index`:

```console
PUT /follower_index/_ccr/follow?wait_for_active_shards=1
{
  "remote_cluster" : "remote_cluster",
  "leader_index" : "leader_index",
  "settings": {
    "index.number_of_replicas": 0
  },
  "max_read_request_operation_count" : 1024,
  "max_outstanding_read_requests" : 16,
  "max_read_request_size" : "1024k",
  "max_write_request_operation_count" : 32768,
  "max_write_request_size" : "16k",
  "max_outstanding_write_requests" : 8,
  "max_write_buffer_count" : 512,
  "max_write_buffer_size" : "512k",
  "max_retry_delay" : "10s",
  "read_poll_timeout" : "30s"
}
```

The API returns the following result:

```console-result
{
  "follow_index_created" : true,
  "follow_index_shards_acked" : true,
  "index_following_started" : true
}
```
