<!-- Converted from indices/shrink-index.asciidoc (AsciiDoc). Includes are inlined. -->

### Shrink index API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Shrinks an existing index into a new index with fewer primary shards.

```console
POST /my-index-000001/_shrink/shrunk-my-index-000001
```

#### Request

`POST /<index>/_shrink/<target-index>`

`PUT /<index>/_shrink/<target-index>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the index.

* Before you can shrink an index:

** The index must be read-only.
** A copy of every shard in the index must reside on the same node.
** The index must have a `green` health status.

To make shard allocation easier, we recommend you also remove the index's
replica shards. You can later re-add replica shards as part of the shrink
operation.

You can use the following update index settings API
request to remove an index's replica shards, and relocate the index's remaining
shards to the same node.

```console
PUT /my_source_index/_settings
{
  "settings": {
    "index.number_of_replicas": 0,                                <1>
    "index.routing.allocation.require._name": "shrink_node_name"  <2>
  }
}
```

<1> Removes replica shards for the index.
<2> Relocates the index's shards to the `shrink_node_name` node.
    See shard-allocation-filtering.

It can take a while to relocate the source index. Progress can be tracked
with the `_cat recovery` API, or the <<cluster-health,
`cluster health` API>> can be used to wait until all shards have relocated
with the `wait_for_no_relocating_shards` parameter.

You can then make the index read-only with the following request using the
add index block API:

```console
PUT /my_source_index/_block/write
```

#### Description

The shrink index API allows you to shrink an existing index into a new index
with fewer primary shards. The requested number of primary shards in the target index
must be a factor of the number of shards in the source index. For example an index with
`8` primary shards can be shrunk into `4`, `2` or `1` primary shards or an index
with `15` primary shards can be shrunk into `5`, `3` or `1`. If the number
of shards in the index is a prime number it can only be shrunk into a single
primary shard. Before shrinking, a (primary or replica) copy of every shard
in the index must be present on the same node.

The current write index on a data stream cannot be shrunk. In order to shrink
the current write index, the data stream must first be
rolled over so that a new write index is created
and then the previous write index can be shrunk.

##### How shrinking works

A shrink operation:

. Creates a new target index with the same definition as the source
  index, but with a smaller number of primary shards.

. Hard-links segments from the source index into the target index. (If
  the file system doesn't support hard-linking, then all segments are copied
  into the new index, which is a much more time consuming process. Also if using
  multiple data paths, shards on different data paths require a full copy of
  segment files if they are not on the same disk since hardlinks don’t work across
  disks)

. Recovers the target index as though it were a closed index which
  had just been re-opened. Recovers shards to Index Setting 
  `.routing.allocation.initial_recovery._id`.

##### Shrink an index

To shrink `my_source_index` into a new index called `my_target_index`, issue
the following request:

```console
POST /my_source_index/_shrink/my_target_index
{
  "settings": {
    "index.routing.allocation.require._name": null, <1>
    "index.blocks.write": null <2>
  }
}
```

<1> Clear the allocation requirement copied from the source index.
<2> Clear the index write block copied from the source index.

The above request returns immediately once the target index has been added to
the cluster state -- it doesn't wait for the shrink operation to start.

=====================================

Indices can only be shrunk if they satisfy the following requirements:

* The target index must not exist.

* The source index must have more primary shards than the target index.

* The number of primary shards in the target index must be a factor of the
  number of primary shards in the source index. The source index must have
  more primary shards than the target index.

* The index must not contain more than `2,147,483,519` documents in total
  across all shards that will be shrunk into a single shard on the target index
  as this is the maximum number of docs that can fit into a single shard.

* The node handling the shrink process must have sufficient free disk space to
  accommodate a second copy of the existing index.

=====================================

The `_shrink` API is similar to the `create index` API
and accepts `settings` and `aliases` parameters for the target index:

```console
POST /my_source_index/_shrink/my_target_index
{
  "settings": {
    "index.number_of_replicas": 1,
    "index.number_of_shards": 1, <1>
    "index.codec": "best_compression" <2>
  },
  "aliases": {
    "my_search_indices": {}
  }
}
```

<1> The number of shards in the target index. This must be a factor of the
    number of shards in the source index.
<2> Best compression will only take effect when new writes are made to the
    index, such as when force-merging the shard to a single
    segment.

**Note:** Mappings may not be specified in the `_shrink` request.

##### Monitor the shrink process

The shrink process can be monitored with the <<cat-recovery,`_cat recovery`
API>>, or the `cluster health` API can be used to wait
until all primary shards have been allocated by setting the  `wait_for_status`
parameter to `yellow`.

The `_shrink` API returns as soon as the target index has been added to the
cluster state, before any shards have been allocated. At this point, all
shards are in the state `unassigned`. If, for any reason, the target index
can't be allocated on the shrink node, its primary shard will remain
`unassigned` until it can be allocated on that node.

Once the primary shard is allocated, it moves to state `initializing`, and the
shrink process begins. When the shrink operation completes, the shard will
become `active`. At that point, Elasticsearch will try to allocate any
replicas and may decide to relocate the primary shard to another node.

##### Wait for active shards

Because the shrink operation creates a new index to shrink the shards to,
the wait for active shards setting
on index creation applies to the shrink index action as well.

#### Path parameters

`<index>`::
(Required, string)
Name of the source index to shrink.

`<target-index>`::
(Required, string)
Name of the target index to create.

Index names must meet the following criteria:

- Lowercase only
- Cannot include `\`, `/`, `*`, `?`, `"`, `<`, `>`, `|`, ` ` (space character), `,`, `#`
- Indices prior to 7.0 could contain a colon (`:`), but that's been deprecated and won't be supported in 7.0+
- Cannot start with `-`, `_`, `+`
- Cannot be `.` or `..`
- Cannot be longer than 255 bytes (note it is bytes, so multi-byte characters will count towards the 255 limit faster)
- Names starting with `.` are deprecated, except for hidden indices and internal indices managed by plugins

#### Query parameters

`wait_for_active_shards`::
(Optional, string) The number of copies of each shard that must be active
before proceeding with the operation. Set to `all` or any non-negative integer
up to the total number of copies of each shard in the index
(`number_of_replicas+1`). Defaults to `1`, meaning to wait just for each
primary shard to be active.

See index-wait-for-active-shards.
`master_timeout`::
(Optional, time units)
Period to wait for the master node. If the master node is not available before
the timeout expires, the request fails and returns an error. Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

`timeout`::
(Optional, time units) Period to wait for a response from all relevant nodes in the cluster after updating the cluster metadata.
If no response is received before the timeout expires, the cluster metadata update still applies but the response will indicate that it was not completely acknowledged.
Defaults to `30s`.
Can also be set to `-1` to indicate that the request should never timeout.

#### Request body

`aliases`::
(Optional, object of objects) Aliases for the resulting index.
**Properties of `aliases` objects**
=======
`<alias>`::
(Required, object) The key is the alias name. Index alias names support
date math.
The object body contains options for the alias. Supports an empty object.
**Properties of `<alias>`**
======
`filter`::
(Optional, Query DSL object) Query used to limit documents the
alias can access.

`index_routing`::
(Optional, string) Value used to route indexing operations to a specific shard.
If specified, this overwrites the `routing` value for indexing operations.

`is_hidden`::
(Optional, Boolean) If `true`, the alias is hidden. Defaults to
`false`. All indices for the alias must have the same `is_hidden` value.

`is_write_index`::
(Optional, Boolean) If `true`, the index is the write index for
the alias. Defaults to `false`.

`routing`::
(Optional, string) Value used to route indexing and search operations to a
specific shard.

`search_routing`::
(Optional, string) Value used to route search operations to a specific shard. If
specified, this overwrites the `routing` value for search operations.
======
=======
`settings`::
(Optional, index setting object)
Configuration options for the target index.
See index-modules-settings.
`max_primary_shard_size`::
(Optional, byte units)
The max primary shard size for the target index. Used to find the optimum number of shards for the target index.
When this parameter is set, each shard's storage in the target index will not be greater than the parameter.
The shards count of the target index will still be a factor of the source index's shards count, but if the parameter
is less than the single shard size in the source index, the shards count for the target index will be equal to the source index's shards count.
For example, when this parameter is set to 50gb, if the source index has 60 primary shards with totaling 100gb, then the
target index will have 2 primary shards, with each shard size of 50gb; if the source index has 60 primary shards
with totaling 1000gb, then the target index will have 20 primary shards; if the source index has 60 primary shards
with totaling 4000gb, then the target index will still have 60 primary shards. This parameter conflicts
with `number_of_shards` in the `settings`, only one of them may be set.
