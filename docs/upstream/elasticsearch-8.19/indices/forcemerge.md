<!-- Converted from indices/forcemerge.asciidoc (AsciiDoc). Includes are inlined. -->

### Force merge API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Forces a merge on the shards of one or more indices.
For data streams, the API forces a merge on the shards of the stream's backing
indices.

```console
POST /my-index-000001/_forcemerge
```

#### Request

`POST /<target>/_forcemerge`

`POST /_forcemerge`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `maintenance`
or `manage` index privilege for the target data
stream, index, or alias.

#### Description

Use the force merge API to force a merge on the
shards of one or more indices. Merging reduces the number of segments in each
shard by merging some of them together, and also frees up the space used by
deleted documents. Merging normally happens automatically, but sometimes it is
useful to trigger a merge manually.

**Warning:** **We recommend only force merging a read-only index (meaning the index
is no longer receiving writes).**  When documents are updated or deleted, the
old version is not immediately removed, but instead soft-deleted and marked
with a "tombstone". These soft-deleted documents are automatically cleaned up
during regular segment merges. But force merge can cause very large (> 5GB)
segments to be produced, which are not eligible for regular merges. So the
number of soft-deleted documents can then grow rapidly, resulting in higher
disk usage and worse search performance. If you regularly force merge an index
receiving writes, this can also make snapshots more expensive, since the new
documents can't be backed up incrementally.

##### Blocks during a force merge

Calls to this API block until the merge is complete (unless request contains
wait_for_completion=false, which is default true). If the client connection
is lost before completion then the force merge process will continue in the
background. Any new requests to force merge the same indices will also block
until the ongoing force merge is complete.

##### Running force merge asynchronously

If the request contains `wait_for_completion=false`, Elasticsearch
performs some preflight checks, launches the request, and returns a
`task` you can use to get the status of the task. However, you can
not cancel this task as the force merge task is not cancelable. Elasticsearch
creates a record of this task as a document at `_tasks/<task_id>`. When you
are done with a task, you should delete the task document so Elasticsearch
can reclaim the space.

##### Force merging multiple indices

You can force merge multiple indices with a single request by targeting:

* One or more data streams that contain multiple backing indices
* Multiple indices
* One or more aliases
* All data streams and indices in a cluster

Each targeted shard is force-merged separately using <<modules-threadpool,the
`force_merge` threadpool>>. By default each node only has a single
`force_merge` thread which means that the shards on that node are force-merged
one at a time. If you expand the `force_merge` threadpool on a node then it
will force merge its shards in parallel.

Force merge makes the storage for the shard being merged temporarily
increase, as it may require free space up to triple its size in case
`max_num_segments` parameter is set to `1`, to rewrite all segments into a new
one.

#### Path parameters

`<target>`::
(Optional, string) Comma-separated list of data streams, indices, and aliases
used to limit the request. Supports wildcards (`*`). To target all data streams
and indices, omit this parameter or use `*` or `_all`.

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

`flush`::
(Optional, Boolean)
If `true`,
Elasticsearch performs a flush on the indices
after the force merge.
Defaults to `true`.

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`max_num_segments`::
(Optional, integer)
The number of segments to merge to.
To fully merge indices,
set it to `1`.

Defaults to checking if a merge needs to execute.
If so, executes it.

You can't specify this parameter and `only_expunge_deletes` in the same request.

`only_expunge_deletes`::
(Optional, Boolean)
If `true`,
expunge all segments containing more than `index.merge.policy.expunge_deletes_allowed`
 (default to 10) percents of deleted documents.
Defaults to `false`.

In Lucene,
a document is not deleted from a segment;
just marked as deleted.
During a merge,
a new segment is created
that does not contain those document deletions.

You can't specify this parameter and `max_num_segments` in the same request.

`wait_for_completion`::
(Optional, Boolean)
If `true`, the request blocks until the operation is complete.
Defaults to `true`.

#### Examples

##### Force merge a specific data stream or index

```console
POST /my-index-000001/_forcemerge
```

##### Force merge several data streams or indices

```console
POST /my-index-000001,my-index-000002/_forcemerge
```

##### Force merge all indices

```console
POST /_forcemerge
```

##### Data streams and time-based indices

Force-merging is useful for managing a data stream's older backing indices and
other time-based indices, particularly after a
rollover.
In these cases,
each index only receives indexing traffic for a certain period of time.
Once an index receive no more writes,
its shards can be force-merged to a single segment.

```console
POST /.ds-my-data-stream-2099.03.07-000001/_forcemerge?max_num_segments=1
```

This can be a good idea because single-segment shards can sometimes use simpler
and more efficient data structures to perform searches.
