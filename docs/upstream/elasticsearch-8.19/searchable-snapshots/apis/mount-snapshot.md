<!-- Converted from searchable-snapshots/apis/mount-snapshot.asciidoc (AsciiDoc). Includes are inlined. -->

### Mount snapshot API

**New API reference**
For the most up-to-date API details, refer to [Searchable snapshots APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-searchable_snapshots).

Mount a snapshot as a searchable snapshot index.

#### Request

`POST /_snapshot/<repository>/<snapshot>/_mount`

#### Prerequisites

If the Elasticsearch security features are enabled, you must have the
`manage` cluster privilege and the `manage` index privilege
for any included indices to use this API.
For more information, see security-privileges.

#### Description

This API mounts a snapshot as a searchable snapshot index. 

Don't use this API for snapshots managed by ILM. Manually mounting
ILM-managed snapshots can interfere with
ILM processes.

#### Path parameters

`<repository>`::
(Required, string)
The name of the repository containing
the snapshot of the index to mount.

`<snapshot>`::
(Required, string)
The name of the snapshot of the index
to mount.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`wait_for_completion`::
(Optional, Boolean) If `true`, the request blocks until the operation is complete.
Defaults to `false`.

`storage`::
(Optional, string)
Mount option for the
{search-snap} index. Possible values are:

`full_copy` (Default):::
Fully mounted index.

`shared_cache`:::
Partially mounted index.

#### Request body

`index`::
(Required, string)
Name of the index contained in the snapshot
whose data is to be mounted.

If no `renamed_index` is specified this name
will also be used to create the new index.

`renamed_index`::
(Optional, string)
Name of the index that will be created.

`index_settings`::
(Optional, object)
Settings that should be added to the index when it is mounted.

`ignore_index_settings`::
(Optional, array of strings)
Names of settings that should be removed from the index when it is mounted.

#### Examples

Mounts the index `my_docs` from an existing snapshot named `my_snapshot` stored
in the `my_repository` as a new index `docs`:

```console
POST /_snapshot/my_repository/my_snapshot/_mount?wait_for_completion=true
{
  "index": "my_docs", <1>
  "renamed_index": "docs", <2>
  "index_settings": { <3>
    "index.number_of_replicas": 0
  },
  "ignore_index_settings": [ "index.refresh_interval" ] <4>
}
```

<1> The name of the index in the snapshot to mount
<2> The name of the index to create
<3> Any index settings to add to the new index
<4> List of index settings to ignore when mounting the snapshotted index
