<!-- Converted from ccr/apis/follow/get-follow-stats.asciidoc (AsciiDoc). Includes are inlined. -->

### Get follower stats API

**New API reference**
For the most up-to-date API details, refer to [Cross-cluster replication APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ccr).

Get cross-cluster replication follower stats.

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
GET /<index>/_ccr/stats
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `monitor` cluster
privileges on the cluster that contains the follower index. For more information,
see security-privileges.

#### Description

This API gets follower stats. This API will return shard-level stats about the
following tasks associated with each shard for the specified indices.

#### Path parameters

`<index>`::
  (Required, string) A comma-delimited list of index patterns.

#### Query parameters

`timeout`::
(Optional, time) Controls the amount of time to wait for results. Defaults to unlimited.

#### Response body

`indices`::
(array) An array of follower index statistics.
**Properties of `indices`**
`fatal_exception`::
(object) An object representing a fatal exception that cancelled the following
task. In this situation, the following task must be resumed manually with the
resume follower API.

`index`::
(string) The name of the follower index.

`total_global_checkpoint_lag`::
(long) Indication of how much the follower is lagging the leader. This is the sum of the difference between the `leader_global_checkpoint` and the `follower_global_checkpoint` for all shards.

`shards`::
(array) An array of shard-level following task statistics.
**Properties of objects in `shards`**
=====
`bytes_read`::
(long) The total of transferred bytes read from the leader.
**Note:** This is only an estimate and does not account for compression if enabled.

`failed_read_requests`::
(long) The number of failed reads.

`failed_write_requests`::
(long) The number of failed bulk write requests executed on the follower.

`follower_aliases_version`::
(long) The index aliases version the follower is synced up to.

`follower_global_checkpoint`::
(long) The current global checkpoint on the follower. The difference between the
`leader_global_checkpoint` and the `follower_global_checkpoint` is an
indication of how much the follower is lagging the leader.

`follower_index`::
(string) The name of the follower index.

`follower_mapping_version`::
(long) The mapping version the follower is synced up to.

`follower_max_seq_no`::
(long) The current maximum sequence number on the follower.

`follower_settings_version`::
(long) The index settings version the follower is synced up to.

`last_requested_seq_no`::
(long) The starting sequence number of the last batch of operations requested
from the leader.

`leader_global_checkpoint`::
(long) The current global checkpoint on the leader known to the follower task.

`leader_index`::
(string) The name of the index in the leader cluster being followed.

`leader_max_seq_no`::
(long) The current maximum sequence number on the leader known to the follower
task.

`operations_read`::
(long) The total number of operations read from the leader.

`operations_written`::
(long) The number of operations written on the follower.

`outstanding_read_requests`::
(integer) The number of active read requests from the follower.

`outstanding_write_requests`::
(integer) The number of active bulk write requests on the follower.

`read_exceptions`::
(array) An array of objects representing failed reads.
**Properties of objects in `read_exceptions`**
======
`exception`::
(object) Represents the exception that caused the read to fail.

`from_seq_no`::
(long) The starting sequence number of the batch requested from the leader.

`retries`::
(integer) The number of times the batch has been retried.
======

`remote_cluster`::
(string) The remote cluster containing the leader
index.

`shard_id`::
(integer) The numerical shard ID, with values from 0 to one less than the
number of replicas.

`successful_read_requests`::
(long) The number of successful fetches.

`successful_write_requests`::
(long) The number of bulk write requests executed on the follower.

`time_since_last_read_millis`::
(long) The number of milliseconds since a read request was sent to the leader.
**Note:** When the follower is caught up to the leader, this number will increase up
to the configured `read_poll_timeout` at which point another read request will
be sent to the leader.

`total_read_remote_exec_time_millis`::
(long) The total time reads spent executing on the remote cluster.

`total_read_time_millis`::
(long) The total time reads were outstanding, measured from the time a read was
sent to the leader to the time a reply was returned to the follower.

`total_write_time_millis`::
(long) The total time spent writing on the follower.

`write_buffer_operation_count`::
(integer) The number of write operations queued on the follower.

`write_buffer_size_in_bytes`::
(long) The total number of bytes of operations currently queued for writing.
=====

#### Examples

This example retrieves follower stats:

```console
GET /follower_index/_ccr/stats
```

The API returns the following results:

```console-result
{
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
```
