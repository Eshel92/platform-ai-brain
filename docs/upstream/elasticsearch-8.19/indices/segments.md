<!-- Converted from indices/segments.asciidoc (AsciiDoc). Includes are inlined. -->

### Index segments API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Returns low-level information about the [Lucene](https://lucene.apache.org/core/)
segments in index shards. For data streams, the API returns information about
the stream's backing indices.

```console
GET /my-index-000001/_segments
```

#### Request

`GET /<target>/_segments`

`GET /_segments`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` index privilege for the target data stream,
index, or alias.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, omit this parameter or use `*` or `_all`.

#### Query parameters

`<vector_formats>`::
(Optional, Boolean)
If `true`, the list of vector formats used by fields in each segment is
included in the output `attributes`. Defaults to `false`.

`allow_no_indices`::
(Optional, Boolean)
If `false`, the request returns an error if any wildcard expression,
index alias, or `_all` value targets only missing or closed indices.
This behavior applies even if the request targets other open indices. For
example, a request targeting `foo*,bar*` returns an error if an index starts
with `foo` but no index starts with `bar`.
Defaults to `true`.

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

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.

#### Response body

`<segment>`::
(String)
Name of the segment, such as `_0`. The segment name is derived from
the segment generation and used internally to create file names in the directory
of the shard.
`generation`::
(Integer)
Generation number, such as `0`. Elasticsearch increments this generation number
for each segment written. Elasticsearch then uses this number to derive the segment name.
`num_docs`::
(Integer)
The number of documents as reported by Lucene. This excludes deleted documents
and counts any nested documents separately from their parents. It
also excludes documents which were indexed recently and do not yet belong to a
segment.
`deleted_docs`::
(Integer)
The number of deleted documents as reported by Lucene, which may be higher or
lower than the number of delete operations you have performed. This number
excludes deletes that were performed recently and do not yet belong to a
segment. Deleted documents are cleaned up by the
automatic merge process if it makes sense to do so.
Also, Elasticsearch creates extra deleted documents to internally track the recent
history of operations on a shard.
`size_in_bytes`::
(Integer)
Disk space used by the segment, such as `50kb`.
`committed`::
(Boolean)
If `true`,
the segments is synced to disk. Segments that are synced can survive a hard reboot.
If `false`,
the data from uncommitted segments is also stored in
the transaction log so that Elasticsearch is able to replay
changes on the next start.
`search`::
(Boolean)
If `true`,
the segment is searchable.
If `false`,
the segment has most likely been written to disk
but needs a refresh to be searchable.
`version`::
(String)
Version of Lucene used to write the segment.
`compound`::
(Boolean)
If `true`, Lucene merged all files from the segment
into a single file to save file descriptors.

`attributes`::
(Object)
Contains information about (i) whether high compression was enabled, (ii) per-field vector formats.

#### Examples

##### Get segment information for a specific data stream or index

```console
GET /test/_segments
```

##### Get segment information for several data streams and indices

```console
GET /test1,test2/_segments
```

##### Get segment information for all data streams and indices in a cluster

```console
GET /_segments
```

The API returns the following response:

```console-response
{
  "_shards": ...
  "indices": {
    "test": {
      "shards": {
        "0": [
          {
            "routing": {
              "state": "STARTED",
              "primary": true,
              "node": "zDC_RorJQCao9xf9pg3Fvw"
            },
            "num_committed_segments": 0,
            "num_search_segments": 1,
            "segments": {
              "_0": {
                "generation": 0,
                "num_docs": 1,
                "deleted_docs": 0,
                "size_in_bytes": 3800,
                "committed": false,
                "search": true,
                "version": "7.0.0",
                "compound": true,
                "attributes": {
                }
              }
            }
          }
        ]
      }
    }
  }
}
```
