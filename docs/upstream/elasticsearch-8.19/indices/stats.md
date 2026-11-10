<!-- Converted from indices/stats.asciidoc (AsciiDoc). Includes are inlined. -->

### Index stats API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Returns statistics for one or more indices. For data streams, the API retrieves
statistics for the stream's backing indices.

```console
GET /my-index-000001/_stats
```

#### Request

`GET /<target>/_stats/<index-metric>`

`GET /<target>/_stats`

`GET /_stats`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` index privilege for the target data stream,
index, or alias.

#### Description

Use the index stats API to get high-level aggregation and statistics for one or
more data streams and indices.

By default,
the returned statistics are index-level
with `primaries` and `total` aggregations.
`primaries` are the values for only the primary shards.
`total` are the accumulated values for both primary and replica shards.

To get shard-level statistics,
set the `level` parameter to `shards`.

**Note:**
When moving to another node,
the shard-level statistics for a shard are cleared.
Although the shard
is no longer part of the node,
that node retains any node-level statistics
to which the shard contributed.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, omit this parameter or use `*` or `_all`.

`<index-metric>`::
(Optional, string)
Comma-separated list of metrics used to limit the request.
Supported metrics are:

`_all`::
Return all statistics.

`completion`::
Completion suggester statistics.

`dense_vector`::
Total number of dense vectors indexed.
Index refreshes can affect this statistic.

`docs`::
Number of documents, number of deleted docs which have not yet merged out, and total size in bytes.
Index refreshes can affect this statistic.

`fielddata`::
Fielddata statistics.

`flush`::
Flush statistics.

`get`::
Get statistics,
including missing stats.

`indexing`::
Indexing statistics.

`merge`::
Merge statistics.

`query_cache`::
Query cache statistics.

`refresh`::
Refresh statistics.

`request_cache`::
Shard request cache statistics.

`search`::
Search statistics including suggest statistics.
You can include statistics for custom groups
by adding an extra `groups` parameter
(search operations can be associated with one or more groups).
The `groups` parameter accepts a comma separated list of group names.
Use `_all` to return statistics for all groups.

`segments`::
Memory use of all open segments.
If the `include_segment_file_sizes` parameter is `true`,
this metric includes the aggregated disk usage
of each Lucene index file.

`sparse_vector`::
Total number of sparse vectors indexed.

Index refreshes can affect this statistic.

`store`::
Size of the index in byte units.

`translog`::
Translog statistics.

#### Query parameters

`expand_wildcards`::
(Optional, string)
Type of index that wildcard patterns can match. If the request can target data
streams, this argument determines whether wildcard expressions match hidden data
streams. Supports comma-separated values, such as `open,hidden`. Valid values
are:

`all`::
Match any data stream or index, including hidden ones.

`open`::
Match open, non-hidden indices. Also matches any non-hidden data stream.

`closed`::
Match closed, non-hidden indices. Also matches any non-hidden data stream. Data
streams cannot be closed.

`hidden`::
Match hidden data streams and hidden indices. Must be combined with `open`,
`closed`, or both.

`none`::
Wildcard patterns are not accepted.
Defaults to `open`.

`fields`::
(Optional, string)
Comma-separated list or wildcard expressions of fields
to include in the statistics.

Used as the default list
unless a specific field list is provided
in the `completion_fields` or `fielddata_fields` parameters.
`completion_fields`::
(Optional, string)
Comma-separated list or wildcard expressions of fields
to include in `fielddata` and `suggest` statistics.
`fielddata_fields`::
(Optional, string)
Comma-separated list or wildcard expressions of fields
to include in `fielddata` statistics.
`forbid_closed_indices`::
(Optional, Boolean)
If `true`, statistics are *not* collected from closed indices.
Defaults to `true`.

`groups`::
(Optional, string)
Comma-separated list of search groups
to include in the `search` statistics.
`level`::
(Optional, string)
Indicates whether statistics are aggregated at the cluster, index, or shard level.
If the shards level is requested, some additional
shard-specific statistics are shown.

Valid values are:

*   `cluster`
*   `indices`
*   `shards`
`include_segment_file_sizes`::
(Optional, Boolean)
If `true`, the call reports the aggregated disk usage of
each one of the Lucene index files (only applies if segment stats are
requested). Defaults to `false`.
`include_unloaded_segments`::
(Optional, Boolean) If `true`, the response includes information from segments
that are **not** loaded into memory. Defaults to `false`.

#### Examples

##### Get statistics for multiple data streams and indices

```console
GET /index1,index2/_stats
```

##### Get statistics for all data streams and indices in a cluster

```console
GET /_stats
```

##### Get specific statistics

The following request returns
only the `merge` and `refresh` statistics
for all indices.

```console
GET /_stats/merge,refresh
```

##### Get statistics for specific search groups

The following request returns
only search statistics
for the `group1` and `group2` search groups.

```console
GET /_stats/search?groups=group1,group2
```
