<!-- Converted from ccr/apis/follow/post-resume-follow.asciidoc (AsciiDoc). Includes are inlined. -->

### Resume follower API

**New API reference**
For the most up-to-date API details, refer to [Cross-cluster replication APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ccr).

Resumes a cross-cluster replication follower index.

#### Request

```console
PUT /follower_index/_ccr/follow?wait_for_active_shards=1
{
  "remote_cluster" : "remote_cluster",
  "leader_index" : "leader_index"
}

POST /follower_index/_ccr/pause_follow
```

```console
POST /follower_index/_ccr/pause_follow
```

```console
POST /<follower_index>/_ccr/resume_follow
{
}
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `write` and `monitor`
index privileges for the follower index. You must have `read` and `monitor`
index privileges for the leader index. You must also have `manage_ccr` cluster
privileges on the cluster that contains the follower index. For more information,
see security-privileges.

#### Description

This API resumes a follower index that has been paused either explicitly with
the pause follower API or implicitly due to
execution that can not be retried due to failure during following. When this API
returns, the follower index will resume fetching operations from the leader index.

#### Path parameters

`<follower_index>`::
  (Required, string) The name of the follower index.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Request body

(See `ccr/apis/follow/../follow-request-body.md`)

#### Examples

This example resumes a follower index named `follower_index`:

```console
POST /follower_index/_ccr/resume_follow
{
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
  "acknowledged" : true
}
```
