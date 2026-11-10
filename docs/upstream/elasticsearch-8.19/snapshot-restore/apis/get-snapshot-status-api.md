<!-- Converted from snapshot-restore/apis/get-snapshot-status-api.asciidoc (AsciiDoc). Includes are inlined. -->

### Get snapshot status API

**New API reference**
For the most up-to-date API details, refer to [Snapshot and restore APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-snapshot).

Retrieves a detailed description of the current state for each shard participating in the snapshot. Note that this API should only be used to obtain detailed shard-level information for ongoing snapshots. If this detail is not needed, or you want to obtain information about one or more existing snapshots, use the get snapshot API.

```console
GET _snapshot/_status
```

#### Request

`GET _snapshot/_status`

`GET _snapshot/<repository>/_status`

`GET _snapshot/<repository>/<snapshot>/_status`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`monitor_snapshot`, `create_snapshot`, or `manage`
cluster privilege to use this API.

#### Description

Use the get snapshot status API to get detailed information about the shards
participating in a snapshot.

If you omit the `<snapshot>` request path parameter, the request only retrieves
information for currently running snapshots. This usage is preferred.

If needed, you can specify `<repository>` and `<snapshot>` to retrieve
information for specific snapshots, even if they're not currently running.

**Warning:**
Using the API to return the status of any snapshots other than currently running
snapshots can be expensive. The API requires a read from the repository for each
shard in each snapshot. For example, if you have 100 snapshots with 1,000 shards
each, an API request that includes all snapshots will require 100,000 reads (100
snapshots * 1,000 shards).

Depending on the latency of your storage, such requests can take an extremely
long time to return results. These requests can also tax machine resources
and, when using cloud storage, incur high processing costs.

#### Path parameters

`<repository>`::
(Optional, string)
Snapshot repository name used to limit the request. Supports wildcards (`*`) if
`<snapshot>` isn't specified.

`<snapshot>`::
(Optional, string)
Comma-separated list of snapshots to retrieve status for. Defaults to
currently running snapshots. Wildcards (`*`) are not supported.

#### Query parameters

`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.
`ignore_unavailable`::
(Optional, Boolean)
If `false`, the request returns an error for any snapshots that are unavailable. Defaults to `false`.
If `true`, the request ignores snapshots that are unavailable, such as those that are corrupted or temporarily cannot be returned.

#### Response body

`repository`::
(string)
Name of the repository that includes the snapshot.

`snapshot`::
(string)
Name of the snapshot.

`uuid`::
(string)
Universally unique identifier (UUID) of the snapshot.

`state`::
(string)
Indicates the current snapshot state.

**Values for `state`**
`FAILED`::
  The snapshot finished with an error and failed to store any data.

`STARTED`::
  The snapshot is currently running.

`SUCCESS`::
  The snapshot completed.

`include_global_state`::
(Boolean)
Indicates whether the current cluster state is included in the snapshot.

`shards_stats`::
(object)
Contains a count of shards in the snapshot.
**Properties of `shards_stats`**
`initializing`::
(integer)
Number of shards that are still initializing.

`started`::
(integer)
Number of shards that have started but are not finalized.

`finalizing`::
(integer)
Number of shards that are finalizing but are not done.

`done`::
(integer)
Number of shards that initialized, started, and finalized successfully.

`failed`::
(integer)
Number of shards that failed to be included in the snapshot.

`total`::
(integer)
Total number of shards included in the snapshot.

`stats`::
(object)
Provides details on the number (`file_count`) and size (`size_in_bytes`) of files included in the snapshot.
**Properties of `stats`**
`incremental`::
(object)
Number and size of files that still need to be copied as part of the incremental snapshot.
For completed snapshots, this property indicates the number and size
of files that were not already in the repository and were copied as
part of the incremental snapshot.

`processed`::
(object)
Number and size of files that have already been uploaded to the snapshot. After a file is uploaded, the processed `file_count` and `size_in_bytes` are incremented in `stats`.

`total`::
(object)
Total number and size of files that are referenced by the snapshot.

`start_time_in_millis`::
(long)
The time, in milliseconds, when the snapshot creation process started.

`time_in_millis`::
(long)
The total time, in milliseconds, that it took for the snapshot process
to complete.

`<index>`::
(list of objects)
List of objects containing information about the
indices included in the snapshot.
**Properties of `<index>`**
`shards_stats`::
(object)
See `shards_stats`.

`stats`::
(object)
See `stats`.

`shards`::
(list of objects)
List of objects containing information about the
shards that include the snapshot.
**Properties of `shards`**
=====
`stage`::
(string)
Indicates the current state of the shards that include the snapshot.
**Properties of `stage`**
======
`DONE`::
Number of shards in the snapshot that were successfully stored in the repository.

`FAILURE`::
Number of shards in the snapshot that were not successfully stored in
the repository.

`FINALIZE`::
Number of shards in the snapshot that are in the finalizing stage
of being stored in the repository.

`INIT`::
Number of shards in the snapshot that are in the initializing stage
of being stored in the repository.

`STARTED`::
Number of shards in the snapshot that are in the started stage
of being stored in the repository.
======
`stats`::
(object)
See `stats`.

`total`::
(object)
Total number and size of files that are referenced by the snapshot.

`start_time_in_millis`::
(long)
See `start_time_in_millis`.

`time_in_millis`::
(long)
See `time_in_millis`.
=====

#### {api-example-title}

The following request returns detailed status information for `snapshot_2` in the `my_repository` repository. This response includes additional information beyond the Get snapshot API, such as shard status and file statistics.

```console
GET _snapshot/my_repository/snapshot_2/_status
```

```console-result
{
  "snapshots" : [
    {
      "snapshot" : "snapshot_2",
      "repository" : "my_repository",
      "uuid" : "lNeQD1SvTQCqqJUMQSwmGg",
      "state" : "SUCCESS",
      "include_global_state" : false,
      "shards_stats" : {
        "initializing" : 0,
        "started" : 0,
        "finalizing" : 0,
        "done" : 1,
        "failed" : 0,
        "total" : 1
      },
      "stats" : {
        "incremental" : {
          "file_count" : 3,
          "size_in_bytes" : 5969
        },
        "total" : {
          "file_count" : 4,
          "size_in_bytes" : 6024
        },
        "start_time_in_millis" : 1594829326691,
        "time_in_millis" : 205
      },
      "indices" : {
        "index_1" : {
          "shards_stats" : {
            "initializing" : 0,
            "started" : 0,
            "finalizing" : 0,
            "done" : 1,
            "failed" : 0,
            "total" : 1
          },
          "stats" : {
            "incremental" : {
              "file_count" : 3,
              "size_in_bytes" : 5969
            },
            "total" : {
              "file_count" : 4,
              "size_in_bytes" : 6024
            },
            "start_time_in_millis" : 1594829326896,
            "time_in_millis" : 0
          },
          "shards" : {
            "0" : {
              "stage" : "DONE",
              "stats" : {
                "incremental" : {
                  "file_count" : 3,
                  "size_in_bytes" : 5969
                },
                "total" : {
                  "file_count" : 4,
                  "size_in_bytes" : 6024
                },
                "start_time_in_millis" : 1594829326896,
                "time_in_millis" : 0
              }
            }
          }
        }
      }
    }
  ]
}
```
