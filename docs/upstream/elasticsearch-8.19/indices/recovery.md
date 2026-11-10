<!-- Converted from indices/recovery.asciidoc (AsciiDoc). Includes are inlined. -->

### Index recovery API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Returns information about ongoing and completed shard recoveries for one or
more indices. For data streams, the API returns information for the stream's
backing indices.

```console
GET /my-index-000001/_recovery
```

#### Request

`GET /<target>/_recovery`

`GET /_recovery`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` index privilege for the target data stream,
index, or alias.

#### Description

Use the index recovery API to get information about ongoing and completed shard
recoveries.

Shard recovery is the process of initializing a shard copy, such as restoring a
primary shard from a snapshot or creating a replica shard from a primary shard.
When a shard recovery completes, the recovered shard is available for search
and indexing.

Recovery automatically occurs during the following processes:

* When creating an index for the first time.
* When a node rejoins the cluster and starts up any missing primary shard copies using the data that it holds in its data path.
* Creation of new replica shard copies from the primary.
* Relocation of a shard copy to a different node in the same cluster.
* A snapshot restore operation.
* A clone, shrink, or
split operation.

You can determine the cause of a shard recovery using the recovery or  cat recovery APIs.
The index recovery API reports information about completed recoveries only for
shard copies that currently exist in the cluster. It only reports the last
recovery for each shard copy and does not report historical information about
earlier recoveries, nor does it report information about the recoveries of
shard copies that no longer exist. This means that if a shard copy completes a
recovery and then Elasticsearch relocates it onto a different node then the information
about the original recovery will not be shown in the recovery API.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, omit this parameter or use `*` or `_all`.

#### Query parameters

`active_only`::
(Optional, Boolean)
If `true`,
the response only includes ongoing shard recoveries.
Defaults to `false`.
`detailed`::
(Optional, Boolean)
If `true`,
the response includes detailed information about shard recoveries.
Defaults to `false`.
`index`::
(Optional, string)
Comma-separated list or wildcard expression of index names
used to limit the request.

#### Response body

`id`::
(Integer)
ID of the shard.

`type`::
(String) Recovery source for the shard. Returned values include:

`EMPTY_STORE`::
An empty store. Indicates a new primary shard or the forced allocation of an
empty primary shard using the cluster reroute API.

`EXISTING_STORE`::
The store of an existing primary shard. Indicates recovery is related
to node startup or the allocation of an existing primary shard.

`LOCAL_SHARDS`::
Shards of another index on the same node. Indicates recovery is related to a
clone, shrink, or
split operation.

`PEER`::
A primary shard on another node. Indicates recovery is related to shard
replication.

`SNAPSHOT`::
A snapshot. Indicates recovery is related to a
snapshot restore operation.

`STAGE`::
(String)
Recovery stage.
Returned values can include:

`INIT`::
Recovery has not started.

`INDEX`::
Reading index metadata and copying bytes from source to destination.

`VERIFY_INDEX`::
Verifying the integrity of the index.

`TRANSLOG`::
Replaying transaction log.

`FINALIZE`::
Cleanup.

`DONE`::
Complete.

`primary`::
(Boolean)
If `true`,
the shard is a primary shard.

`start_time`::
(String)
Timestamp of recovery start.

`stop_time`::
(String)
Timestamp of recovery finish.

`total_time_in_millis`::
(String)
Total time to recover shard in milliseconds.

`source`::
(Object)
Recovery source.
This can include:

  * A repository description if recovery is from a snapshot
  * A description of source node

`target`::
(Object)
Destination node.

`index`::
(Object)
Statistics about physical index recovery.

`translog`::
(Object)
Statistics about translog recovery.

`start`::
(Object)
Statistics about time to open and start the index.

#### Examples

##### Get recovery information for several data streams and indices

```console
GET index1,index2/_recovery?human
```

##### Get segment information for all data streams and indices in a cluster

Here we create a repository and snapshot index1 in
order to restore it right after and prints out the
index recovery result.

```console
# create the index
PUT index1
{"settings": {"index.number_of_shards": 1}}

# create the repository
PUT /_snapshot/my_repository
{"type": "fs","settings": {"location": "recovery_asciidoc" }}

# snapshot the index
PUT /_snapshot/my_repository/snap_1?wait_for_completion=true
{"indices": "index1"}

# delete the index
DELETE index1

# and restore the snapshot
POST /_snapshot/my_repository/snap_1/_restore?wait_for_completion=true

```

```console-result
{
  "snapshot": {
    "snapshot": "snap_1",
    "indices": [
      "index1"
    ],
    "shards": {
      "total": 1,
      "failed": 0,
      "successful": 1
    }
  }
}
```

```console
GET /_recovery?human
```

The API returns the following response:

```console-result
{
  "index1" : {
    "shards" : [ {
      "id" : 0,
      "type" : "SNAPSHOT",
      "stage" : "INDEX",
      "primary" : true,
      "start_time" : "2014-02-24T12:15:59.716",
      "start_time_in_millis": 1393244159716,
      "stop_time" : "0s",
      "stop_time_in_millis" : 0,
      "total_time" : "2.9m",
      "total_time_in_millis" : 175576,
      "source" : {
        "repository" : "my_repository",
        "snapshot" : "my_snapshot",
        "index" : "index1",
        "version" : "{version}",
        "restoreUUID": "PDh1ZAOaRbiGIVtCvZOMww"
      },
      "target" : {
        "id" : "ryqJ5lO5S4-lSFbGntkEkg",
        "host" : "my.fqdn",
        "transport_address" : "my.fqdn",
        "ip" : "10.0.1.7",
        "name" : "my_es_node"
      },
      "index" : {
        "size" : {
          "total" : "75.4mb",
          "total_in_bytes" : 79063092,
          "reused" : "0b",
          "reused_in_bytes" : 0,
          "recovered" : "65.7mb",
          "recovered_in_bytes" : 68891939,
          "recovered_from_snapshot" : "0b",
          "recovered_from_snapshot_in_bytes" : 0,
          "percent" : "87.1%"
        },
        "files" : {
          "total" : 73,
          "reused" : 0,
          "recovered" : 69,
          "percent" : "94.5%"
        },
        "total_time" : "0s",
        "total_time_in_millis" : 0,
        "source_throttle_time" : "0s",
        "source_throttle_time_in_millis" : 0,
        "target_throttle_time" : "0s",
        "target_throttle_time_in_millis" : 0
      },
      "translog" : {
        "recovered" : 0,
        "total" : 0,
        "percent" : "100.0%",
        "total_on_start" : 0,
        "total_time" : "0s",
        "total_time_in_millis" : 0
      },
      "verify_index" : {
        "check_index_time" : "0s",
        "check_index_time_in_millis" : 0,
        "total_time" : "0s",
        "total_time_in_millis" : 0
      }
    } ]
  }
}
```

This response includes information
about a single index recovering a single shard.
The source of the recovery is a snapshot repository
and the target of the recovery is the `my_es_node` node.

The response also includes the number
and percentage of files and bytes recovered.

##### Get detailed recovery information

To get a list of physical files in recovery,
set the `detailed` query parameter to `true`.

```console
GET _recovery?human&detailed=true
```

The API returns the following response:

```console-result
{
  "index1" : {
    "shards" : [ {
      "id" : 0,
      "type" : "EXISTING_STORE",
      "stage" : "DONE",
      "primary" : true,
      "start_time" : "2014-02-24T12:38:06.349",
      "start_time_in_millis" : "1393245486349",
      "stop_time" : "2014-02-24T12:38:08.464",
      "stop_time_in_millis" : "1393245488464",
      "total_time" : "2.1s",
      "total_time_in_millis" : 2115,
      "source" : {
        "id" : "RGMdRc-yQWWKIBM4DGvwqQ",
        "host" : "my.fqdn",
        "transport_address" : "my.fqdn",
        "ip" : "10.0.1.7",
        "name" : "my_es_node"
      },
      "target" : {
        "id" : "RGMdRc-yQWWKIBM4DGvwqQ",
        "host" : "my.fqdn",
        "transport_address" : "my.fqdn",
        "ip" : "10.0.1.7",
        "name" : "my_es_node"
      },
      "index" : {
        "size" : {
          "total" : "24.7mb",
          "total_in_bytes" : 26001617,
          "reused" : "24.7mb",
          "reused_in_bytes" : 26001617,
          "recovered" : "0b",
          "recovered_in_bytes" : 0,
          "recovered_from_snapshot" : "0b",
          "recovered_from_snapshot_in_bytes" : 0,
          "percent" : "100.0%"
        },
        "files" : {
          "total" : 26,
          "reused" : 26,
          "recovered" : 0,
          "percent" : "100.0%",
          "details" : [ {
            "name" : "segments.gen",
            "length" : 20,
            "recovered" : 20
          }, {
            "name" : "_0.cfs",
            "length" : 135306,
            "recovered" : 135306,
            "recovered_from_snapshot": 0
          }, {
            "name" : "segments_2",
            "length" : 251,
            "recovered" : 251,
            "recovered_from_snapshot": 0
          }
          ]
        },
        "total_time" : "2ms",
        "total_time_in_millis" : 2,
        "source_throttle_time" : "0s",
        "source_throttle_time_in_millis" : 0,
        "target_throttle_time" : "0s",
        "target_throttle_time_in_millis" : 0
      },
      "translog" : {
        "recovered" : 71,
        "total" : 0,
        "percent" : "100.0%",
        "total_on_start" : 0,
        "total_time" : "2.0s",
        "total_time_in_millis" : 2025
      },
      "verify_index" : {
        "check_index_time" : 0,
        "check_index_time_in_millis" : 0,
        "total_time" : "88ms",
        "total_time_in_millis" : 88
      }
    } ]
  }
}
```

The response includes a listing
of any physical files recovered
and their sizes.

The response also includes timings in milliseconds
of the various stages of recovery:

* Index retrieval
* Translog replay
* Index start time

This response indicates the recovery is `done`.
All recoveries,
whether ongoing or complete,
are kept in the cluster state
and may be reported on at any time.

To only return information about ongoing recoveries,
set the `active_only` query parameter to `true`.
