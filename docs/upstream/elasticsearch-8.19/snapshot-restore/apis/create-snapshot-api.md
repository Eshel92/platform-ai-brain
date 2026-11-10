<!-- Converted from snapshot-restore/apis/create-snapshot-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Create snapshot API

**New API reference**
For the most up-to-date API details, refer to [Snapshot and restore APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-snapshot).

Takes a snapshot of a cluster or specified data
streams and indices.

```console
PUT /_snapshot/my_repository/my_snapshot
```

#### Request

`PUT /_snapshot/<repository>/<snapshot>`

`POST /_snapshot/<repository>/<snapshot>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`create_snapshot` or `manage` cluster privilege to
use this API.

#### Path parameters

`<repository>`::
(Required, string)
Name of the snapshot repository.

`<snapshot>`::
(Required, string)
Name of the snapshot. Supports date math. Must be
unique within the snapshot repository.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`wait_for_completion`::
(Optional, Boolean) If `true`, the request returns a response when the snapshot
is complete. If `false`, the request returns a response when the snapshot
initializes. Defaults to `false`.

#### Request body

`expand_wildcards`::
(Optional, string) Determines how wildcard patterns in the `indices` parameter
match data streams and indices. Supports comma-separated values, such as
`open,hidden`. Defaults to `all`. Valid values are:

`all`:::
Match any data stream or index, including closed and hidden ones.

`open`:::
Match open indices and data streams.

`closed`:::
Match closed indices and data streams.

`hidden`:::
Match hidden data streams and indices. Must be combined with `open`, `closed`,
or both.

`none`:::
Don't expand wildcard patterns.

`ignore_unavailable`::
(Optional, Boolean)
If `false`, the snapshot fails if any data stream or index in `indices` is
missing. If `true`, the snapshot ignores missing data
streams and indices. Defaults to `false`.

`include_global_state`::
(Optional, Boolean)
If `true`, include the cluster state in the snapshot. Defaults to `true`.
The cluster state includes:

* Persistent cluster settings
* Index templates
* Legacy index templates
* Ingest pipelines
* ILM policies
* Stored scripts
* For snapshots taken after 7.12.0, feature states

`indices`::
(Optional, string or array of strings)
Comma-separated list of data streams and indices to include in the snapshot.
Supports multi-target syntax. Defaults to an empty array
(`[]`), which includes all regular data streams and regular indices. To exclude
all data streams and indices, use `-*`.
You can't use this parameter to include or exclude <<system-indices,system
indices or system data streams>> from a snapshot. Use
`feature_states` instead.

`feature_states`::
(Optional, array of strings)
Feature states to include in the snapshot. To get a list of
possible values and their descriptions, use the <<get-features-api,get features
API>>.
If `include_global_state` is `true`, the snapshot includes all feature states by
default. If `include_global_state` is `false`, the snapshot includes no feature
states by default.
Note that specifying an empty array will result in the default behavior. To
exclude all feature states, regardless of the `include_global_state` value,
specify an array with only the value `none` (`["none"]`).

`metadata`::
(Optional, object)
Attaches arbitrary metadata to the snapshot, such as a record of who took the snapshot, why it was taken, or any other useful data. Metadata must be less than 1024 bytes.

`partial`::
(Optional, Boolean)
If `false`, the entire snapshot will fail if one or more indices included in the snapshot do not have all primary shards available. Defaults to `false`.
If `true`, allows taking a partial snapshot of indices with unavailable shards.

:!page-id:

#### Examples

The following request takes a snapshot of `index_1` and `index_2`.

```console
PUT /_snapshot/my_repository/snapshot_2?wait_for_completion=true
{
  "indices": "index_1,index_2",
  "ignore_unavailable": true,
  "include_global_state": false,
  "metadata": {
    "taken_by": "user123",
    "taken_because": "backup before upgrading"
  }
}
```

The API returns the following response:

```console-result
{
  "snapshot": {
    "snapshot": "snapshot_2",
    "uuid": "vdRctLCxSketdKb54xw67g",
    "repository": "my_repository",
    "version_id": <version_id>,
    "version": <version>,
    "indices": [],
    "data_streams": [],
    "feature_states": [],
    "include_global_state": false,
    "metadata": {
      "taken_by": "user123",
      "taken_because": "backup before upgrading"
    },
    "state": "SUCCESS",
    "start_time": "2020-06-25T14:00:28.850Z",
    "start_time_in_millis": 1593093628850,
    "end_time": "2020-06-25T14:00:28.850Z",
    "end_time_in_millis": 1593094752018,
    "duration_in_millis": 0,
    "failures": [],
    "shards": {
      "total": 0,
      "failed": 0,
      "successful": 0
    }
  }
}
```
