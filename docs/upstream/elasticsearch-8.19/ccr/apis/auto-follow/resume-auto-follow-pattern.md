<!-- Converted from ccr/apis/auto-follow/resume-auto-follow-pattern.asciidoc (AsciiDoc). Includes are inlined. -->

### Resume auto-follow pattern API

**New API reference**
For the most up-to-date API details, refer to [Cross-cluster replication APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-ccr).

Resumes a cross-cluster replication auto-follow pattern.

#### Request

`POST /_ccr/auto_follow/<auto_follow_pattern_name>/resume`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have `manage_ccr` cluster
privileges on the cluster that contains the follower index. For more information,
see security-privileges.

#### Description

This API resumes an auto-follow pattern that has been paused with the
pause auto-follow pattern API. When this API
returns, the auto-follow pattern will resume configuring following indices for
newly created indices on the remote cluster that match its patterns. Remote
indices created while the pattern was paused will also be followed, unless they
have been deleted or closed in the meantime.

#### Path parameters

`<auto_follow_pattern_name>`::
  (Required, string) Specifies the name of the auto-follow pattern to resume.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Examples

This example resumes the activity of a paused auto-follow pattern
named `my_auto_follow_pattern`:

```console
PUT /_ccr/auto_follow/my_auto_follow_pattern
{
  "remote_cluster" : "remote_cluster",
  "leader_index_patterns" :
  [
    "leader_index"
  ],
  "follow_index_pattern" : "{{leader_index}}-follower"
}
```

```console
DELETE /_ccr/auto_follow/my_auto_follow_pattern
```

```console
POST /_ccr/auto_follow/my_auto_follow_pattern/pause
```

```console
POST /_ccr/auto_follow/my_auto_follow_pattern/resume
```

The API returns the following result:

```console-result
{
  "acknowledged" : true
}
```
