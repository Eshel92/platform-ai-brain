<!-- Converted from snapshot-restore/apis/clone-snapshot-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Clone snapshot API

**New API reference**
For the most up-to-date API details, refer to [Snapshot and restore APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-snapshot).

Clones part or all of a snapshot into a new snapshot.

```console
PUT /_snapshot/my_repository/source_snapshot/_clone/target_snapshot
{
  "indices": "index_a,index_b"
}
```

#### Request

`PUT /_snapshot/<repository>/<source_snapshot>/_clone/<target_snapshot>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

#### Description

The clone snapshot API allows creating a copy of all or part of an existing snapshot
within the same repository.

#### Path parameters

`<repository>`::
(Required, string)
Name of the snapshot repository that both source and target snapshot belong to.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`timeout`::
(Optional, time units) Specifies the period of time to wait for
a response. If no response is received before the timeout expires, the request
fails and returns an error. Defaults to `30s`.

`indices`::
(Required, string)
A comma-separated list of indices to include in the snapshot.
multi-target syntax is supported.
