<!-- Converted from cat/recovery.asciidoc (AsciiDoc). Includes are inlined. -->

### cat recovery API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the index recovery API.

Returns information about ongoing and completed shard recoveries,
similar to the index recovery API.

For data streams, the API returns information about the stream's backing
indices.

#### Request

`GET /_cat/recovery/<target>`

`GET /_cat/recovery`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API. You must
also have the `monitor` or `manage` index privilege
for any data stream, index, or alias you retrieve.

#### Description

The cat recovery API returns information about shard recoveries, both
ongoing and completed. It is a more compact view of the JSON
index recovery API.

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
`bytes`::
(Optional, byte size units) Unit used to display byte values.
`detailed`::
(Optional, Boolean)
If `true`,
the response includes detailed information about shard recoveries.
Defaults to `false`.
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

`index`, `i`, `idx`::
(Default) Name of the index.

`shard`, `s`, `sh`::
(Default) Name of the shard.

`time`, `t`, `ti`, `primaryOrReplica`::
(Default) Recovery time elasped.

`type`, `ty`::
(Default) Type of recovery, from a `peer` or a `snapshot`.

`stage`, `st`::
(Default) Stage of the recovery. 
Returned values are:
* `INIT`
* `INDEX` recovery of lucene files, either reusing local ones are copying new ones
* `VERIFY_INDEX` potentially running check index
* `TRANSLOG` starting up the engine, replaying the translog
* `FINALIZE` performing final task after all translog ops have been done
* `DONE`

`source_host`, `shost`::
(Default) Host address the index is moving from.

`source_node`, `snode`::
(Default) Node name the index is moving from.

`target_host`, `thost`::
(Default) Host address the index is moving to.

`target_node`, `tnode`::
(Default) Node name the index is moving to.

`repository`, `rep`::
(Default) Name of the repository being used. if not relevant `n/a`.

`snapshot`, `snap`::
(Default) Name of the snapshot being used. if not relevant `n/a`.
                
`files`, `f`::
(Default) Total number of files to recover.

`files_recovered`, `fr`::
(Default) Number of files currently recovered.

`files_percent`, `fp`::
(Default) Percentage of files currently recovered.

`files_total`, `tf`::
(Default) Total number of files.

`bytes`, `b`::
(Default) Total number of bytes to recover.

`bytes_recovered`, `br`::
(Default) Total number of bytes currently recovered.

`bytes_percent`, `bp`::
(Default) Percentage of bytes currently recovered.

`bytes_total`, `tb`::
(Default) Total number of bytes.

`translog_ops`, `to`::
(Default) Total number of translog ops to recover.

`translog_ops_recovered`, `tor`::
(Default) Total number of translog ops currently recovered.

`translog_ops_percent`, `top`::
(Default) Percentage of translog ops currently recovered.

`start_time`, `start`::
Start time of the recovery operation.

`start_time_millis`, `start_millis`::
Start time of the recovery operation in eopch milliseconds.

`stop_time`, `stop`::
End time of the recovery operation. If ongoing `1970-01-01T00:00:00.000Z`

`stop_time_millis`, `stop_millis`::
End time of the recovery operation in eopch milliseconds. If ongoing `0`

`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
`index`::
(Optional, string)
Comma-separated list or wildcard expression of index names
used to limit the request.
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

##### Example with no ongoing recoveries

```console
GET _cat/recovery?v=true
```

The API returns the following response:

```txt
index             shard time type  stage source_host source_node target_host target_node repository snapshot files files_recovered files_percent files_total bytes bytes_recovered bytes_percent bytes_total translog_ops translog_ops_recovered translog_ops_percent
my-index-000001   0     13ms store done  n/a         n/a         127.0.0.1   node-0      n/a        n/a      0     0               100%          13          0b    0b              100%          9928b       0            0                      100.0%
```

In this example response, the source and target nodes are the same because the
recovery type is `store`, meaning they were read from local storage on node
start.

##### Example with a live shard recovery

By increasing the replica count of an index and bringing another node online to
host the replicas, you can retrieve information about an ongoing recovery.

```console
GET _cat/recovery?v=true&h=i,s,t,ty,st,shost,thost,f,fp,b,bp
```

The API returns the following response:

```txt
i               s t      ty   st    shost       thost       f     fp      b  bp
my-index-000001 0 1252ms peer done  192.168.1.1 192.168.1.2 0     100.0%  0b 100.0%
```

In this example response, the recovery type is `peer`, meaning the shard
recovered from another node. The returned files and bytes are real-time
measurements.

##### Example with a snapshot recovery

You can restore backups of an index using the <<snapshot-restore,snapshot and
restore>> API. You can use the cat recovery API retrieve information about a
snapshot recovery.

```console
GET _cat/recovery?v=true&h=i,s,t,ty,st,rep,snap,f,fp,b,bp
```

The API returns the following response with a recovery type of `snapshot`:

```txt
i               s t      ty       st    rep     snap   f  fp   b     bp
my-index-000001 0 1978ms snapshot done  my-repo snap-1 79 8.0% 12086 9.0%
```
