<!-- Converted from slm/apis/slm-stats.asciidoc (AsciiDoc). Includes are inlined. -->

### Get snapshot lifecycle stats API

**New API reference**
For the most up-to-date API details, refer to [Snapshot lifecycle management APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-slm).

Returns global and policy-level statistics about actions taken by snapshot lifecycle management.

#### Request

`GET /_slm/stats`

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the `manage_slm`
cluster privilege to use this API. For more information, see
security-privileges.

#### Examples

```console
GET /_slm/stats
```

The API returns the following response:

```js
{
  "retention_runs": 13,
  "retention_failed": 0,
  "retention_timed_out": 0,
  "retention_deletion_time": "1.4s",
  "retention_deletion_time_millis": 1404,
  "policy_stats": [ ],
  "total_snapshots_taken": 1,
  "total_snapshots_failed": 1,
  "total_snapshots_deleted": 0,
  "total_snapshot_deletion_failures": 0
}
```
