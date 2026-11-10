<!-- Converted from ccr/apis/auto-follow/put-auto-follow-pattern.asciidoc (AsciiDoc). Includes are inlined. -->

### Create auto-follow pattern API

**New API reference**
For the most up-to-date API details, refer to [Cross-cluster replication APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ccr).

Creates a cross-cluster replication auto-follow pattern.

#### Request

```console
PUT /_ccr/auto_follow/<auto_follow_pattern_name>
{
  "remote_cluster" : "<remote_cluster>",
  "leader_index_patterns" :
  [
    "<leader_index_pattern>"
  ],
  "leader_index_exclusion_patterns":
  [
    "<leader_index_exclusion_pattern>"
  ],
  "follow_index_pattern" : "<follow_index_pattern>"
}
```

```console
DELETE /_ccr/auto_follow/auto_follow_pattern_name
```

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `read` and `monitor`
index privileges for the leader index patterns. You must also have `manage_ccr`
cluster privileges on the cluster that contains the follower index. For more
information, see security-privileges.

#### Description

This API creates a new named collection of
auto-follow patterns against the remote cluster
specified in the request body. Newly created indices on the remote cluster
matching any of the specified patterns will be automatically configured as follower
indices. Indices on the remote cluster that were created before the auto-follow
pattern is created won't be auto-followed even if they match the pattern.

This API can also be used to update existing
auto-follow patterns. Note that follower indices that were configured automatically
before updating an auto-follow pattern will remain unchanged even if they don't match against
the new patterns.

#### Path parameters

`<auto_follow_pattern_name>`::
  (Required, string) The name of the collection of auto-follow patterns.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Request body

`remote_cluster`::
  (Required, string) The remote cluster containing
  the leader indices to match against.

`leader_index_patterns`::
  (Optional, array) An array of simple index patterns to match against indices
  in the remote cluster specified by the `remote_cluster` field.

`leader_index_exclusion_patterns`::
  (Optional, array) An array of simple index patterns that can be used to exclude indices
  from being auto-followed. Indices in the remote cluster whose names are matching one or
  more `leader_index_patterns` and one or more `leader_index_exclusion_patterns` won't be followed.

`follow_index_pattern`::
  (Optional, string) The name of follower index. The template `{{leader_index}}` can be used to
  derive the name of the follower index from the name of the leader index. When following a data
  stream, the `follow_index_pattern` will be used for renaming not only the leader index, but also
  the data stream containing the leader index. For example, a data stream called
  `logs-mysql-default` with a backing index of `.ds-logs-mysql-default-2022-01-01-000001` and a
  `follow_index_pattern` of `{{leader_index}}_copy` will replicate the data stream as
  `logs-mysql-default_copy` and the backing index as
  `.ds-logs-mysql-default_copy-2022-01-01-000001`.

(See `ccr/apis/auto-follow/../follow-request-body.md`)

#### Examples

This example creates an auto-follow pattern named `my_auto_follow_pattern`:

```console
PUT /_ccr/auto_follow/my_auto_follow_pattern
{
  "remote_cluster" : "remote_cluster",
  "leader_index_patterns" :
  [
    "leader_index*"
  ],
  "follow_index_pattern" : "{{leader_index}}-follower",
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
  "acknowledged" : true
}
```

```console
DELETE /_ccr/auto_follow/my_auto_follow_pattern
```
