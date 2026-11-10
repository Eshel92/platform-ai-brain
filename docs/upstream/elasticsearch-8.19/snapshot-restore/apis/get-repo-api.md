<!-- Converted from snapshot-restore/apis/get-repo-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Get snapshot repository API

**New API reference**
For the most up-to-date API details, refer to [Snapshot and restore APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-snapshot).

Gets information about one or more registered
snapshot repositories.

```console
GET /_snapshot/my_repository
```

#### Request

`GET /_snapshot/<repository>`

`GET /_snapshot`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`monitor_snapshot`, `create_snapshot`, or `manage`
cluster privilege to use this API.

#### Path parameters

`<repository>`::
(Optional, string)
Comma-separated list of snapshot repository names used to limit the request.
Wildcard (`*`) expressions are supported including combining wildcards with exclude patterns starting with `-`.
To get information about all snapshot repositories registered in the
cluster, omit this parameter or use `*` or `_all`.

#### Query parameters

`local`::
(Optional, Boolean) If `true`, the request gets information from the local node
only. If `false`, the request gets information from the master node. Defaults to
`false`.

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Response body

`<repository>`::
(object)
Contains information about the snapshot repository. Key is the name of the
snapshot repository.
**Properties of `<repository>`**
`type`::
(string)
Repository type.

**Values for `type`**
=====
`fs`::
Shared file system repository. See snapshots-filesystem-repository.

[xpack]#`source`#::
Source-only repository. See snapshots-source-only-repository.

`url`::
URL repository. See snapshots-read-only-repository.
=====

More repository types are available through these official plugins:

* repository-s3 for S3 repository support
* {plugins}/repository-hdfs.html[repository-hdfs] for HDFS repository support in
  Hadoop environments
* repository-azure for Azure storage repositories
* repository-gcs for Google Cloud Storage repositories

`settings`::
(object)
Contains settings for the repository. Valid properties for the `settings` object
depend on the repository type, set using the
`type` parameter.
For properties, see the <<put-snapshot-repo-api,create or update snapshot
repository API>>'s <<put-snapshot-repo-api-settings-param,`settings`
parameter>>.

#### Examples

```console
GET /_snapshot/my_repository
```

The API returns the following response:

```console-result
{
  "my_repository" : {
    "type" : "fs",
    "uuid" : "0JLknrXbSUiVPuLakHjBrQ",
    "settings" : {
      "location" : "my_backup_location"
    }
  }
}
```
