<!-- Converted from snapshot-restore/apis/restore-snapshot-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Restore snapshot API

**New API reference**
For the most up-to-date API details, refer to [Snapshot and restore APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-snapshot).

Restores a snapshot of a cluster or specified data streams and indices.

```console
POST /_snapshot/my_repository/my_snapshot/_restore
```

#### Request

`POST /_snapshot/<repository>/<snapshot>/_restore`

#### Prerequisites

* If you use Elasticsearch security features, you must have the `manage` or
`cluster:admin/snapshot/*` cluster privilege to use this API.

* You can only restore a snapshot to a running cluster with an elected
master node. The snapshot's repository must be
registered and available to the cluster.

* The snapshot and cluster versions must be compatible. See
snapshot-restore-version-compatibility.

* To restore a snapshot, the cluster's global metadata must be writable. Ensure
there aren't any cluster blocks that prevent writes. The
restore operation ignores index blocks.

* Before you restore a data stream, ensure the cluster contains a
matching index template with data stream enabled. To
check, use Kibana's **Index Management** feature or
the get index template API:
```console
GET _index_template/*?filter_path=index_templates.name,index_templates.index_template.index_patterns,index_templates.index_template.data_stream
```
If no such template exists, you can create one or
restore a cluster state that
contains one. Without a matching index template, a data stream can't roll over
or create backing indices.

* If your snapshot contains data from App Search or Workplace Search, ensure
you've restored the {enterprise-search-ref}/encryption-keys.html[Enterprise
Search encryption key] before restoring the snapshot.

#### Path parameters

`<repository>`::
(Required, string)
Name of the repository to restore a snapshot from.

`<snapshot>`::
(Required, string)
Name of the snapshot to restore.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`wait_for_completion`::
(Optional, Boolean) If `true`, the request returns a response when the restore
operation completes. The operation is complete when it finishes all attempts to
recover primary shards for restored indices.
This applies even if one or more of the recovery attempts fail.
If `false`, the request returns a response when the restore
operation initializes. Defaults to `false`.

#### Request body

`ignore_unavailable`::
(Optional, Boolean) If `true`, the request ignores any index or data stream in
`indices` that's missing from the snapshot. If `false`, the request returns an
error for any missing index or data stream. Defaults to `false`.

`ignore_index_settings`::
(Optional, string or array of strings) Index settings to not restore from the snapshot. You can't use this option to ignore `index.number_of_shards`.
For data streams, this option only applies to restored backing indices. New
backing indices are configured using the data stream's matching index template.

`include_aliases`::
(Optional, Boolean)
If `true`, the request restores aliases for any restored data streams and
indices. If `false`, the request doesn't restore aliases. Defaults to `true`.

`include_global_state`::
(Optional, Boolean)
If `true`, restore the cluster state. Defaults to `false`.

The cluster state includes:

* Persistent cluster settings
* Index templates
* Legacy index templates
* Ingest pipelines
* ILM policies
* Stored scripts
* For snapshots taken after 7.12.0, feature states

If `include_global_state` is `true` then the restore operation merges the
legacy index templates in your cluster with the templates contained in the
snapshot, replacing any existing ones whose name matches one in the snapshot.
It completely removes all persistent settings, non-legacy index templates,
ingest pipelines and ILM lifecycle policies that exist in your cluster
and replaces them with the corresponding items from the snapshot.

Use the `feature_states` parameter to configure how feature states are restored.

If `include_global_state` is `true` and a snapshot was created without a global
state then the restore request will fail.

`feature_states`::
(Optional, array of strings)
Feature states to restore.
If `include_global_state` is `true`, the request restores all feature states
in the snapshot by default. If `include_global_state` is `false`, the request
restores no feature states by default. Note that specifying an empty array
will result in the default behavior. To restore no feature states, regardless
of the `include_global_state` value, specify an array containing only the value
`none` (`["none"]`).

`index_settings`::
(Optional, object) Index settings to add or change in restored indices,
including backing indices. You can't use this option to change
`index.number_of_shards`.
For data streams, this option only applies to restored backing indices. New
backing indices are configured using the data stream's matching index template.

`indices`::
(Optional, string or array of strings) Comma-separated list of indices and data
streams to restore. Supports multi-target syntax. Defaults
to all regular indices and regular data streams in the snapshot.
You can't use this parameter to restore <<system-indices,system indices or
system data streams>>. Use
`feature_states` instead.

`partial`::
(Optional, Boolean)
If `false`, the entire restore operation will fail if one or more indices included in the snapshot do not have all primary shards available. Defaults to `false`.
If `true`, allows restoring a partial snapshot of indices with unavailable shards. Only shards that were successfully included in the snapshot
will be restored. All missing shards will be recreated as empty.

`rename_pattern`::
(Optional, string)
Defines a rename pattern to apply to restored data streams and indices. Data streams and indices matching the rename pattern will be renamed according to
`rename_replacement`.
The rename pattern is applied as defined by the regular expression that
supports referencing the original text, according to the [`appendReplacement`](https://docs.oracle.com/javase/8/docs/api/java/util/regex/Matcher.html#appendReplacement-java.lang.StringBuffer-java.lang.String-) logic.

`rename_replacement`::
(Optional, string)
Defines the rename replacement string. See `rename_pattern` for more information.

#### Examples

##### Restore renamed

The following request restores `index_1` and `index_2` from `snapshot_2`. The `rename_pattern` and `rename_replacement` parameters indicate any index matching the regular expression `index_(.+)` will be renamed using the pattern `restored_index_$1` when restored.

For example, `index_1` will be renamed to `restored_index_1`. `index_2` will be renamed to `restored_index_2`.

```console
POST /_snapshot/my_repository/snapshot_2/_restore?wait_for_completion=true
{
  "indices": "index_1,index_2",
  "ignore_unavailable": true,
  "include_global_state": false,
  "rename_pattern": "index_(.+)",
  "rename_replacement": "restored_index_$1",
  "include_aliases": false
}
```

The API returns an acknowledgement if the request succeeds. If the request encounters errors, the response indicates any issues found, such as
open indices that are blocking the restore operation from completing.

##### Restore in-place

You may want to restore an index in-place, for example when no alternative
options surface after the cluster-allocation-explain API reports
`no_valid_shard_copy`.

The following request closes `index_1` and then restores it
in-place from the `snapshot_2` snapshot in the `my_repository` repository.

```console
POST index_1/_close

POST /_snapshot/my_repository/snapshot_2/_restore?wait_for_completion=true
{
  "indices": "index_1"
}
```
