<!-- Converted from cat/shards.asciidoc (AsciiDoc). Includes are inlined. -->

### cat shards API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana
console.
They are _not_ intended for use by applications.

The `shards` command is the detailed view of what nodes contain which shards.
It will tell you if it's a primary or replica, the number of docs, the bytes it takes on disk, and the node where it's located.

For data streams, the API returns information about the stream's backing indices.

#### Request

`GET /_cat/shards/<target>`

`GET /_cat/shards`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API.
You must also have the `monitor` or `manage` index privilege
to view the full information for any data stream, index, or alias you retrieve.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases used to limit the request.
Supports wildcards (`*`).
To target all data streams and indices, omit this parameter or use `*` or `_all`.

#### Query parameters

`bytes`::
(Optional, byte size units) Unit used to display byte values.
`format`::
(Optional, string) Short version of the
[HTTP accept header](https://www.w3.org/Protocols/rfc2616/rfc2616-sec14.html).
Valid values include JSON, YAML, etc.
`h`::
(Optional, string) Comma-separated list of column names to display.
If you do not specify which columns to include, the API returns the default columns in the order listed below.
If you explicitly specify one or more columns, it only returns the specified columns.

Valid columns are:

`index`, `i`, `idx`::
(Default) Name of the index.

`shard`, `s`, `sh`::
(Default) Name of the shard.

`prirep`, `p`, `pr`, `primaryOrReplica`::
(Default) Shard type.
Returned values are `primary` or `replica`.

`state`, `st`::
(Default) State of the shard.
Returned values are:
* `INITIALIZING`: The shard is recovering from a peer shard or gateway.
* `RELOCATING`: The shard is relocating.
* `STARTED`: The shard has started.
* `UNASSIGNED`: The shard is not assigned to any node.

`docs`, `d`, `dc`::
(Default) Number of documents in shard, such as `25`.

`store`, `sto`::
(Default) Disk space used by the shard, such as `5kb`.

`dataset.size`::
(Default) Disk space used by the shard's dataset, which may or may not be the size on disk, but includes space used by the shard on object storage.
Reported as a size value such as `5kb`.

`ip`::
(Default) IP address of the node, such as `127.0.1.1`.

`id`::
(Default) ID of the node, such as `k0zy`.

`node`, `n`::
(Default) Node name, such as `I8hydUG`.

`completion.size`, `cs`, `completionSize`::
Size of completion, such as `0b`.

`dense_vector.value_count`, `dvc`, `denseVectorCount`::
Number of indexed dense vectors.

`fielddata.memory_size`, `fm`, `fielddataMemory`::
Used fielddata cache memory, such as `0b`.

`fielddata.evictions`, `fe`, `fielddataEvictions`::
Fielddata cache evictions, such as `0`.

`flush.total`, `ft`, `flushTotal`::
Number of flushes, such as `1`.

`flush.total_time`, `ftt`, `flushTotalTime`::
Time spent in flush, such as `1`.

`get.current`, `gc`, `getCurrent`::
Number of current get operations, such as `0`.

`get.time`, `gti`, `getTime`::
Time spent in get, such as `14ms`.

`get.total`, `gto`, `getTotal`::
Number of get operations, such as `2`.

`get.exists_time`, `geti`, `getExistsTime`::
Time spent in successful gets, such as `14ms`.

`get.exists_total`, `geto`, `getExistsTotal`::
Number of successful get operations, such as `2`.

`get.missing_time`, `gmti`, `getMissingTime`::
Time spent in failed gets, such as `0s`.

`get.missing_total`, `gmto`, `getMissingTotal`::
Number of failed get operations, such as `1`.

`indexing.delete_current`, `idc`, `indexingDeleteCurrent`::
Number of current deletion operations, such as `0`.

`indexing.delete_time`, `idti`, `indexingDeleteTime`::
Time spent in deletions, such as `2ms`.

`indexing.delete_total`, `idto`, `indexingDeleteTotal`::
Number of deletion operations, such as `2`.

`indexing.index_current`, `iic`, `indexingIndexCurrent`::
Number of current indexing operations, such as `0`.

`indexing.index_time`, `iiti`, `indexingIndexTime`::
Time spent in indexing, such as `134ms`.

`indexing.index_total`, `iito`, `indexingIndexTotal`::
Number of indexing operations, such as `1`.

`indexing.index_failed`, `iif`, `indexingIndexFailed`::
Number of failed indexing operations, such as `0`.

`indexing.index_failed_due_to_version_conflict`, `iifvc`, `indexingIndexFailedDueToVersionConflict`::
Number of failed indexing operations due to version conflict, such as `0`.

`merges.current`, `mc`, `mergesCurrent`::
Number of current merge operations, such as `0`.

`merges.current_docs`, `mcd`, `mergesCurrentDocs`::
Number of current merging documents, such as `0`.

`merges.current_size`, `mcs`, `mergesCurrentSize`::
Size of current merges, such as `0b`.

`merges.total`, `mt`, `mergesTotal`::
Number of completed merge operations, such as `0`.

`merges.total_docs`, `mtd`, `mergesTotalDocs`::
Number of merged documents, such as `0`.

`merges.total_size`, `mts`, `mergesTotalSize`::
Size of current merges, such as `0b`.

`merges.total_time`, `mtt`, `mergesTotalTime`::
Time spent merging documents, such as `0s`.

`query_cache.memory_size`, `qcm`, `queryCacheMemory`::
Used query cache memory, such as `0b`.

`query_cache.evictions`, `qce`, `queryCacheEvictions`::
Query cache evictions, such as `0`.

`recoverysource.type`, `rs`::
Type of recovery source.

`refresh.total`, `rto`, `refreshTotal`::
Number of refreshes, such as `16`.

`refresh.time`, `rti`, `refreshTime`::
Time spent in refreshes, such as `91ms`.

`search.fetch_current`, `sfc`, `searchFetchCurrent`::
Current fetch phase operations, such as `0`.

`search.fetch_time`, `sfti`, `searchFetchTime`::
Time spent in fetch phase, such as `37ms`.

`search.fetch_total`, `sfto`, `searchFetchTotal`::
Number of fetch operations, such as `7`.

`search.open_contexts`, `so`, `searchOpenContexts`::
Open search contexts, such as `0`.

`search.query_current`, `sqc`, `searchQueryCurrent`::
Current query phase operations, such as `0`.

`search.query_time`, `sqti`, `searchQueryTime`::
Time spent in query phase, such as `43ms`.

`search.query_total`, `sqto`, `searchQueryTotal`::
Number of query operations, such as `9`.

`search.scroll_current`, `scc`, `searchScrollCurrent`::
Open scroll contexts, such as `2`.

`search.scroll_time`, `scti`, `searchScrollTime`::
Time scroll contexts held open, such as `2m`.

`search.scroll_total`, `scto`, `searchScrollTotal`::
Completed scroll contexts, such as `1`.

`segments.count`, `sc`, `segmentsCount`::
Number of segments, such as `4`.

`segments.memory`, `sm`, `segmentsMemory`::
Memory used by segments, such as `1.4kb`.

`segments.index_writer_memory`, `siwm`, `segmentsIndexWriterMemory`::
Memory used by index writer, such as `18mb`.

`segments.version_map_memory`, `svmm`, `segmentsVersionMapMemory`::
Memory used by version map, such as `1.0kb`.

`segments.fixed_bitset_memory`, `sfbm`, `fixedBitsetMemory`::
Memory used by fixed bit sets for nested object field types and type filters for types referred in `join` fields, such as `1.0kb`.

`seq_no.global_checkpoint`, `sqg`, `globalCheckpoint`::
Global checkpoint.

`seq_no.local_checkpoint`, `sql`, `localCheckpoint`::
Local checkpoint.

`seq_no.max`, `sqm`, `maxSeqNo`::
Maximum sequence number.

`sparse_vector.value_count`, `svc`, `sparseVectorCount`::
Number of indexed sparse vectors.

`suggest.current`, `suc`, `suggestCurrent`::
Number of current suggest operations, such as `0`.

`suggest.time`, `suti`, `suggestTime`::
Time spent in suggest, such as `0`.

`suggest.total`, `suto`, `suggestTotal`::
Number of suggest operations, such as `0`.

`sync_id`::
Sync ID of the shard.

`unassigned.at`, `ua`::
Time at which the shard became unassigned in
[Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/List_of_UTC_time_offsets).

`unassigned.details`, `ud`::
Details about why the shard became unassigned.
This does not explain why the shard is currently unassigned.
To understand why a shard is not assigned, use the cluster-allocation-explain API.

`unassigned.for`, `uf`::
Time at which the shard was requested to be unassigned in
[Coordinated Universal Time (UTC)](https://en.wikipedia.org/wiki/List_of_UTC_time_offsets).

`unassigned.reason`, `ur`::
Indicates the reason for the last change to the state of this unassigned shard.
This does not explain why the shard is currently unassigned.
To understand why a shard is not assigned, use the cluster-allocation-explain API.
Returned values include:
* `ALLOCATION_FAILED`: Unassigned as a result of a failed allocation of the shard.
* `CLUSTER_RECOVERED`: Unassigned as a result of a full cluster recovery.
* `DANGLING_INDEX_IMPORTED`: Unassigned as a result of importing a dangling index.
* `EXISTING_INDEX_RESTORED`: Unassigned as a result of restoring into a closed index.
* `FORCED_EMPTY_PRIMARY`: The shard's allocation was last modified by forcing an empty primary using the cluster-reroute API.
* `INDEX_CLOSED`: Unassigned because the index was closed.
* `INDEX_CREATED`: Unassigned as a result of an API creation of an index.
* `INDEX_REOPENED`: Unassigned as a result of opening a closed index.
* `MANUAL_ALLOCATION`: The shard's allocation was last modified by the cluster-reroute API.
* `NEW_INDEX_RESTORED`: Unassigned as a result of restoring into a new index.
* `NODE_LEFT`: Unassigned as a result of the node hosting it leaving the cluster.
* `NODE_RESTARTING`: Similar to `NODE_LEFT`, except that the node was registered as restarting using the Node shutdown API.
* `PRIMARY_FAILED`: The shard was initializing as a replica, but the primary shard failed before the initialization completed.
* `REALLOCATED_REPLICA`: A better replica location is identified and causes the existing replica allocation to be cancelled.
* `REINITIALIZED`: When a shard moves from started back to initializing.
* `REPLICA_ADDED`: Unassigned as a result of explicit addition of a replica.
* `REROUTE_CANCELLED`: Unassigned as a result of explicit cancel reroute command.

`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
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

##### Example with a single data stream or index

```console
GET _cat/shards
```

The API returns the following response:

```txt
my-index-000001 0 p STARTED 3014 31.1mb 192.168.56.10 H5dfFeA
```

##### Example with a wildcard pattern

If your cluster has many shards, you can use a wildcard pattern in the
`<target>` path parameter to limit the API request.

The following request returns information for any data streams or indices beginning with `my-index-`.

```console
GET _cat/shards/my-index-*
```

The API returns the following response:

```txt
my-index-000001 0 p STARTED 3014 31.1mb 192.168.56.10 H5dfFeA
```

##### Example with a relocating shard

```console
GET _cat/shards
```

The API returns the following response:

```txt
my-index-000001 0 p RELOCATING 3014 31.1mb 192.168.56.10 H5dfFeA -> -> 192.168.56.30 bGG90GE
```

The `RELOCATING` value in `state` column indicates the index shard is relocating.

##### Example with a shard states

Before a shard is available for use, it goes through an `INITIALIZING` state.
You can use the cat shards API to see which shards are initializing.

```console
GET _cat/shards
```

The API returns the following response:

```txt
my-index-000001 0 p STARTED      3014 31.1mb 192.168.56.10 H5dfFeA
my-index-000001 0 r INITIALIZING    0 14.3mb 192.168.56.30 bGG90GE
```

##### Example with reasons for unassigned shards

The following request returns the `unassigned.reason` column, which indicates why a shard is unassigned.

```console
GET _cat/shards?h=index,shard,prirep,state,unassigned.reason
```

The API returns the following response:

```txt
my-index-000001 0 p STARTED    3014 31.1mb 192.168.56.10 H5dfFeA
my-index-000001 0 r STARTED    3014 31.1mb 192.168.56.30 bGG90GE
my-index-000001 0 r STARTED    3014 31.1mb 192.168.56.20 I8hydUG
my-index-000001 0 r UNASSIGNED ALLOCATION_FAILED
```
