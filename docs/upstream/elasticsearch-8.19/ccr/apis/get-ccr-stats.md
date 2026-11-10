<!-- Converted from ccr/apis/get-ccr-stats.asciidoc (AsciiDoc). Includes are inlined. -->

### Get cross-cluster replication stats API

**New API reference**
For the most up-to-date API details, refer to [Cross-cluster replication APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ccr).

Get cross-cluster replication stats.

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
GET /_ccr/stats
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `monitor` cluster
privileges on the cluster that contains the follower index. For more information,
see security-privileges.

#### Description

This API gets cross-cluster replication stats. This API will return all stats related to cross-cluster replication. In
particular, this API returns stats about auto-following, and returns the same
shard-level stats as in the get follower stats API.

#### Query parameters

`timeout`::
(Optional, time) Controls the amount of time to wait for results. Defaults to unlimited.

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Response body

`auto_follow_stats`::
(object) An object representing stats for the auto-follow coordinator.
**Properties of `auto_follow_stats`**
`number_of_failed_follow_indices`::
(long) The number of indices that the auto-follow coordinator failed to
automatically follow. The causes of recent failures are captured in the logs
of the elected master node and in the
`auto_follow_stats.recent_auto_follow_errors` field.

`number_of_failed_remote_cluster_state_requests`::
(long) The number of times that the auto-follow coordinator failed to retrieve
the cluster state from a remote cluster registered in a collection of
auto-follow patterns.

`number_of_successful_follow_indices`::
(long) The number of indices that the auto-follow coordinator successfully
followed.

`recent_auto_follow_errors`::
(array) An array of objects representing failures by the auto-follow coordinator.

`follow_stats`::
(object) An object representing shard-level stats for follower indices; refer to
the details of the response in the
get follower stats API.

#### Examples

This example retrieves cross-cluster replication stats:

```console
GET /_ccr/stats
```

The API returns the following results:

```console-result
{
  "auto_follow_stats" : {
    "number_of_failed_follow_indices" : 0,
    "number_of_failed_remote_cluster_state_requests" : 0,
    "number_of_successful_follow_indices" : 1,
    "recent_auto_follow_errors" : [],
    "auto_followed_clusters" : []
  },
  "follow_stats" : {
    "indices" : [
      {
        "index" : "follower_index",
        "total_global_checkpoint_lag" : 256,
        "shards" : [
          {
            "remote_cluster" : "remote_cluster",
            "leader_index" : "leader_index",
            "follower_index" : "follower_index",
            "shard_id" : 0,
            "leader_global_checkpoint" : 1024,
            "leader_max_seq_no" : 1536,
            "follower_global_checkpoint" : 768,
            "follower_max_seq_no" : 896,
            "last_requested_seq_no" : 897,
            "outstanding_read_requests" : 8,
            "outstanding_write_requests" : 2,
            "write_buffer_operation_count" : 64,
            "follower_mapping_version" : 4,
            "follower_settings_version" : 2,
            "follower_aliases_version" : 8,
            "total_read_time_millis" : 32768,
            "total_read_remote_exec_time_millis" : 16384,
            "successful_read_requests" : 32,
            "failed_read_requests" : 0,
            "operations_read" : 896,
            "bytes_read" : 32768,
            "total_write_time_millis" : 16384,
            "write_buffer_size_in_bytes" : 1536,
            "successful_write_requests" : 16,
            "failed_write_requests" : 0,
            "operations_written" : 832,
            "read_exceptions" : [ ],
            "time_since_last_read_millis" : 8
          }
        ]
      }
    ]
  }
}
```
