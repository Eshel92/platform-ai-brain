<!-- Converted from cat/segments.asciidoc (AsciiDoc). Includes are inlined. -->

### cat segments API

**New API reference**
For the most up-to-date API details, refer to [Compact and aligned text (CAT) APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-cat)..

**Important:**
cat APIs are only intended for human consumption using the command line or Kibana 
console. They are _not_ intended for use by applications. For application 
consumption, use the index segments API.

Returns low-level information about the [Lucene](https://lucene.apache.org/core/)
segments in index shards, similar to the indices segments
API.

For data streams, the API returns information about the stream's backing
indices.

#### Request

`GET /_cat/segments/<target>`

`GET /_cat/segments`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` cluster privilege to use this API. You must
also have the `monitor` or `manage` index privilege
for any data stream, index, or alias you retrieve.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, omit this parameter or use `*` or `_all`.

#### Query parameters

`bytes`::
(Optional, byte size units) Unit used to display byte values.
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

`prirep`, `p`, `pr`, `primaryOrReplica`::
(Default) Shard type. Returned values are `primary` or `replica`.

`ip`::
(Default) IP address of the segment's shard, such as `127.0.1.1`.

`segment`::
(Default)
Name of the segment, such as `_0`. The segment name is derived from
the segment generation and used internally to create file names in the directory
of the shard.
`generation`::
(Default)
Generation number, such as `0`. Elasticsearch increments this generation number
for each segment written. Elasticsearch then uses this number to derive the segment name.
`docs.count`::
(Default)
The number of documents as reported by Lucene. This excludes deleted documents
and counts any nested documents separately from their parents. It
also excludes documents which were indexed recently and do not yet belong to a
segment.
`docs.deleted`::
(Default)
The number of deleted documents as reported by Lucene, which may be higher or
lower than the number of delete operations you have performed. This number
excludes deletes that were performed recently and do not yet belong to a
segment. Deleted documents are cleaned up by the
automatic merge process if it makes sense to do so.
Also, Elasticsearch creates extra deleted documents to internally track the recent
history of operations on a shard.
`size`::
(Default)
Disk space used by the segment, such as `50kb`.
`size.memory`::
(Default)
Bytes of segment data stored in memory for efficient search,
such as `1264`.
A value of `-1` indicates Elasticsearch was unable to compute this number.
`committed`::
(Default)
If `true`,
the segments is synced to disk. Segments that are synced can survive a hard reboot.
If `false`,
the data from uncommitted segments is also stored in
the transaction log so that Elasticsearch is able to replay
changes on the next start.
`searchable`::
(Default)
If `true`,
the segment is searchable.
If `false`,
the segment has most likely been written to disk
but needs a refresh to be searchable.
`version`::
(Default)
Version of Lucene used to write the segment.
`compound`::
(Default) If `true`, the segment is stored in a compound file. This means Lucene
merged all files from the segment in a single file to save file descriptors.

`id`::
ID of the node, such as `k0zy`.

`help`::
(Optional, Boolean) If `true`, the response includes help information. Defaults
to `false`.
`s`::
(Optional, string) Comma-separated list of column names or column aliases used
to sort the response.
`v`::
(Optional, Boolean) If `true`, the response includes column headings.
Defaults to `false`.

#### Examples

```console
GET /_cat/segments?v=true
```

The API returns the following response:

```
index shard prirep ip        segment generation docs.count docs.deleted size size.memory committed searchable version compound
test  0     p      127.0.0.1 _0               0          1            0  3kb           0 false     true       {lucene_version}   true
test1 0     p      127.0.0.1 _0               0          1            0  3kb           0 false     true       {lucene_version}   true
```
