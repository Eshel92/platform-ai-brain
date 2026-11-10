<!-- Converted from cat/snapshots.asciidoc (AsciiDoc). Includes are inlined. -->

### cat snapshots API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the get snapshot API.

Returns information about the snapshots stored in one or
more repositories. A snapshot is a backup of an index or running Elasticsearch cluster.

#### Request

`GET /_cat/snapshots/<repository>`

`GET /_cat/snapshots`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`monitor_snapshot`, `create_snapshot`, or `manage`
cluster privilege to use this API.

#### Path parameters

`<repository>`::
(Optional, string) Comma-separated list of snapshot repositories used to limit
the request. Accepts wildcard expressions. `_all` returns all repositories.

If any repository fails during the request, Elasticsearch returns an error.

#### Query parameters

`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`h`::
(Optional, string) Comma-separated list of column names to display.
If you do not specify which columns to include, the API returns the default
columns in the order listed below. If you explicitly specify one or more
columns, it only returns the specified columns.

Valid columns are:

`id`, `snapshot`::
(Default) ID of the snapshot, such as `snap1`.

`repository`, `re`, `repo`::
(Default) Name of the repository, such as `repo1`.

`status`, `s`::
(Default) State of the snapshot process. Returned values are:
* `FAILED`: The snapshot process failed.
* `INCOMPATIBLE`: The snapshot process is incompatible with the current cluster
version.
* `IN_PROGRESS`: The snapshot process started but has not completed.
* `PARTIAL`: The snapshot process completed with a partial success.
* `SUCCESS`: The snapshot process completed with a full success.

`start_epoch`, `ste`, `startEpoch`::
(Default) [Unix `epoch` time](https://en.wikipedia.org/wiki/Unix_time) at which
the snapshot process started.

`start_time`, `sti`, `startTime`::
(Default) `HH:MM:SS` time at which the snapshot process started.

`end_epoch`, `ete`, `endEpoch`::
(Default) [Unix `epoch` time](https://en.wikipedia.org/wiki/Unix_time) at which
the snapshot process ended.

`end_time`, `eti`, `endTime`::
(Default) `HH:MM:SS` time at which the snapshot process ended.

`duration`, `dur`::
(Default) Time it took the snapshot process to complete in <<time-units,time
units>>.

`indices`, `i`::
(Default) Number of indices in the snapshot.

`successful_shards`, `ss`::
(Default) Number of successful shards in the snapshot.

`failed_shards`, `fs`::
(Default) Number of failed shards in the snapshot.

`total_shards`, `ts`::
(Default) Total number of shards in the snapshot.

`reason`, `r`::
Reason for any snapshot failures.

`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
`ignore_unavailable`::
(Optional, Boolean) If `true`, the response does not include information from
unavailable snapshots. Defaults to `false`.

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`time`::
(Optional, time units)
Unit used to display time values.
`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.

#### Examples

```console
GET /_cat/snapshots/repo1?v=true&s=id
```

The API returns the following response:

```txt
id     repository status start_epoch start_time end_epoch  end_time duration indices successful_shards failed_shards total_shards
snap1  repo1      FAILED 1445616705  18:11:45   1445616978 18:16:18     4.6m       1                 4             1            5
snap2  repo1      SUCCESS 1445634298  23:04:58   1445634672 23:11:12     6.2m       2                10             0           10
```
