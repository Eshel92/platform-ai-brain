<!-- Converted from indices/flush.asciidoc (AsciiDoc). Includes are inlined. -->

### Flush API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Flushes one or more data streams or indices.

```console
POST /my-index-000001/_flush
```

#### Request

`POST /<target>/_flush`

`GET /<target>/_flush`

`POST /_flush`

`GET /_flush`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `maintenance`
or `manage` index privilege for the target data
stream, index, or alias.

#### Description

Flushing a data stream or index is the process of making sure that any data that is currently
only stored in the transaction log is also
permanently stored in the Lucene index. When restarting, Elasticsearch replays any
unflushed operations from the transaction log in to the Lucene index to bring it
back into the state that it was in before the restart. Elasticsearch automatically
triggers flushes as needed, using heuristics that trade off the size of the
unflushed transaction log against the cost of performing each flush.

Once each operation has been flushed it is permanently stored in the Lucene
index. This may mean that there is no need to maintain an additional copy of it
in the transaction log. The transaction log is made up of multiple files,
called _generations_, and Elasticsearch will delete any generation files once they are no
longer needed, freeing up disk space.

It is also possible to trigger a flush on one or more indices using the flush
API, although it is rare for users to need to call this API directly. If you
call the flush API after indexing some documents then a successful response
indicates that Elasticsearch has flushed all the documents that were indexed before the
flush API was called.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases to
flush. Supports wildcards (`*`). To flush all data streams and indices, omit
this parameter or use `*` or `_all`.

#### Query parameters

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

`force`::
(Optional, Boolean)
If `true`,
the request forces a flush
even if there are no changes to commit to the index.
Defaults to `false`.

You can use this parameter
to increment the generation number of the transaction log.

This parameter is considered internal.

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`wait_if_ongoing`::
(Optional, Boolean)
If `true`,
the flush operation blocks until execution
when another flush operation is running.

If `false`,
Elasticsearch returns an error
if you request a flush
when another flush operation is running.

Defaults to `true`.

#### Examples

##### Flush a specific data stream or index

```console
POST /my-index-000001/_flush
```

##### Flush several data streams and indices

```console
POST /my-index-000001,my-index-000002/_flush
```

##### Flush all data streams and indices in a cluster

```console
POST /_flush
```
