<!-- Converted from snapshot-restore/apis/put-repo-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Create or update snapshot repository API

**New API reference**
For the most up-to-date API details, refer to [Snapshot and restore APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-snapshot).

Registers or updates a snapshot repository.

```console
PUT /_snapshot/my_repository
{
  "type": "fs",
  "settings": {
    "location": "my_backup_location"
  }
}
```

**Important:** If you're migrating [searchable snapshots](https://www.elastic.co/guide/en/elasticsearch/reference/8.19/searchable-snapshots.html), the repository's name must be identical in the source and destination clusters.

#### Request

`PUT /_snapshot/<repository>`

`POST /_snapshot/<repository>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

* To register a snapshot repository, the cluster's global metadata must be
writeable. Ensure there aren't any cluster blocks that
prevent write access.

#### Path parameters

`<repository>`::
(Required, string)
Name of the snapshot repository to register or update.

#### Query parameters

**Important:** Several options for this API can be specified using a query parameter
or a request body parameter. If both parameters are specified, only the query
parameter is used.

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

`timeout`::
(Optional, time units) Period to wait for a response from all relevant nodes in the cluster after updating the cluster metadata.
If no response is received before the timeout expires, the cluster metadata update still applies but the response will indicate that it was not completely acknowledged.
Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`verify`::
(Optional, Boolean)
If `true`, the request verifies the repository is functional on all master and
data nodes in the cluster. If `false`, this verification is skipped. Defaults to
`true`.
You can manually perform this verification using the
verify snapshot repository API.

#### Request body

`type`::
(Required, string)
Repository type.
**Valid values for `type`**

`azure`:: repository-azure
`gcs`:: repository-gcs
`s3`:: repository-s3
`fs`:: snapshots-filesystem-repository
`source`:: snapshots-source-only-repository
`url`:: snapshots-read-only-repository

Other repository types are available through official plugins:

`hdfs`:: {plugins}/repository-hdfs.html[Hadoop Distributed File System (HDFS) repository]

`settings`::
(Required, object)
Settings for the repository. Supported settings vary based on the repository
type:
* repository-azure
* repository-gcs
* repository-s3
* snapshots-filesystem-repository
* snapshots-read-only-repository
* snapshots-source-only-repository

Other repository types are available through official plugins:

* {plugins}/repository-hdfs.html[Hadoop Distributed File System (HDFS) repository]

`verify`::
(Optional, Boolean)
If `true`, the request verifies the repository is functional on all master and
data nodes in the cluster. If `false`, this verification is skipped. Defaults to
`true`.
You can manually perform this verification using the
verify snapshot repository API.
