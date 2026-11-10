<!-- Converted from snapshot-restore/apis/delete-snapshot-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Delete snapshot API

**New API reference**
For the most up-to-date API details, refer to [Snapshot and restore APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-snapshot).

Deletes a snapshot.

```console
DELETE /_snapshot/my_repository/my_snapshot
```

#### Request

`DELETE /_snapshot/<repository>/<snapshot>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
cluster privilege to use this API.

#### Path parameters

`<repository>`::
(Required, string)
Name of the repository to delete a snapshot from.

`<snapshot>`::
(Required, string)
Comma-separated list of snapshot names to delete. Also accepts wildcards (`*`).

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`wait_for_completion`::
(Optional, Boolean) If `true`, the request returns a response when the matching
snapshots are all deleted. If `false`, the request returns a response as soon as
the deletes are scheduled. Defaults to `true`.

#### {api-example-title}

The following request deletes `snapshot_2` and `snapshot_3` from the repository named `my_repository`.

```console
DELETE /_snapshot/my_repository/snapshot_2,snapshot_3
```

The API returns the following response:

```console-result
{
  "acknowledged" : true
}
```
