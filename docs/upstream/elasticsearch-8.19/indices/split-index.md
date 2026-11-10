<!-- Converted from indices/split-index.asciidoc (AsciiDoc). Includes are inlined. -->

### Split index API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Splits an existing index into a new index with more primary shards.

```console
POST /my-index-000001/_split/split-my-index-000001
{
  "settings": {
    "index.number_of_shards": 2
  }
}
```

#### Request

`POST /<index>/_split/<target-index>`

`PUT /<index>/_split/<target-index>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the index.

* Before you can split an index:

** The index must be read-only.
** The cluster health status must be green.

You can do make an index read-only with the following request using the
add index block API:

```console
PUT /my_source_index/_block/write
```

The current write index on a data stream cannot be split. In order to split
the current write index, the data stream must first be
rolled over so that a new write index is created
and then the previous write index can be split.

#### Description

The split index API allows you to split an existing index into a new index,
where each original primary shard is split into two or more primary shards in
the new index.

The number of times the index can be split (and the number of shards that each
original shard can be split into) is determined by the
`index.number_of_routing_shards` setting. The number of routing shards
specifies the hashing space that is used internally to distribute documents
across shards with consistent hashing. For instance, a 5 shard index with
`number_of_routing_shards` set to `30` (`5 x 2 x 3`) could be split by a
factor of `2` or `3`. In other words, it could be split as follows:

* `5` -> `10` -> `30`  (split by 2, then by 3)
* `5` -> `15` -> `30` (split by 3, then by 2)
* `5` -> `30` (split by 6)

`index.number_of_routing_shards` is a <<index-modules-settings,static index
setting>>. You can only set `index.number_of_routing_shards` at index creation
time or on a closed index.

.*Index creation example*
The following create index API creates the
`my-index-000001` index with an `index.number_of_routing_shards` setting of `30`.

```console
PUT /my-index-000001
{
  "settings": {
    "index": {
      "number_of_routing_shards": 30
    }
  }
}
```

The `index.number_of_routing_shards` setting's default value depends 
on the number of primary shards in the original index.
The default is designed to allow you to split
by factors of 2 up to a maximum of 1024 shards. However, the original number
of primary shards must taken into account. For instance, an index created
with 5 primary shards could be split into 10, 20, 40, 80, 160, 320, or a
maximum of 640 shards (with a single split action or multiple split actions).

If the original index contains one primary shard (or a multi-shard index has
been shrunk down to a single primary shard), then the
index may by split into an arbitrary number of shards greater than 1. The
properties of the default number of routing shards will then apply to the
newly split index.

##### How splitting works

A split operation:

. Creates a new target index with the same definition as the source
  index, but with a larger number of primary shards.

. Hard-links segments from the source index into the target index. (If
  the file system doesn't support hard-linking, then all segments are copied
  into the new index, which is a much more time consuming process.)

. Hashes all documents again, after low level files are created, to delete
  documents that belong to a different shard.

. Recovers the target index as though it were a closed index which
  had just been re-opened.

##### Why doesn't Elasticsearch support incremental resharding?

Going from `N` shards to `N+1` shards, aka. incremental resharding, is indeed a
feature that is supported by many key-value stores. Adding a new shard and
pushing new data to this new shard only is not an option: this would likely be
an indexing bottleneck, and figuring out which shard a document belongs to
given its `_id`, which is necessary for get, delete and update requests, would
become quite complex. This means that we need to rebalance existing data using
a different hashing scheme.

The most common way that key-value stores do this efficiently is by using
consistent hashing. Consistent hashing only requires `1/N`-th of the keys to
be relocated when growing the number of shards from `N` to `N+1`. However
Elasticsearch's unit of storage, shards, are Lucene indices. Because of their
search-oriented data structure, taking a significant portion of a Lucene index,
be it only 5% of documents, deleting them and indexing them on another shard
typically comes with a much higher cost than with a key-value store. This cost
is kept reasonable when growing the number of shards by a multiplicative factor
as described in the above section: this allows Elasticsearch to perform the
split locally, which in-turn allows to perform the split at the index level
rather than reindexing documents that need to move, as well as using hard links
for efficient file copying.

In the case of append-only data, it is possible to get more flexibility by
creating a new index and pushing new data to it, while adding an alias that
covers both the old and the new index for read operations. Assuming that the
old and new indices have respectively M and N shards, this has no overhead
compared to searching an index that would have MN+ shards.

##### Split an index

To split `my_source_index` into a new index called `my_target_index`, issue
the following request:

```console
POST /my_source_index/_split/my_target_index
{
  "settings": {
    "index.number_of_shards": 2
  }
}
```

The above request returns immediately once the target index has been added to
the cluster state -- it doesn't wait for the split operation to start.

=====================================

Indices can only be split if they satisfy the following requirements:

* The target index must not exist

* The source index must have fewer primary shards than the target index.

* The number of primary shards in the target index must be a multiple of the
  number of primary shards in the source index.

* The node handling the split process must have sufficient free disk space to
  accommodate a second copy of the existing index.

=====================================

The `_split` API is similar to the `create index` API
and accepts `settings` and `aliases` parameters for the target index:

```console
POST /my_source_index/_split/my_target_index
{
  "settings": {
    "index.number_of_shards": 5 <1>
  },
  "aliases": {
    "my_search_indices": {}
  }
}
```

<1> The number of shards in the target index. This must be a multiple of the
    number of shards in the source index.

**Note:** Mappings may not be specified in the `_split` request.

##### Monitor the split process

The split process can be monitored with the <<cat-recovery,`_cat recovery`
API>>, or the `cluster health` API can be used to wait
until all primary shards have been allocated by setting the  `wait_for_status`
parameter to `yellow`.

The `_split` API returns as soon as the target index has been added to the
cluster state, before any shards have been allocated. At this point, all
shards are in the state `unassigned`. If, for any reason, the target index
can't be allocated, its primary shard will remain `unassigned` until it
can be allocated on that node.

Once the primary shard is allocated, it moves to state `initializing`, and the
split process begins. When the split operation completes, the shard will
become `active`. At that point, Elasticsearch will try to allocate any
replicas and may decide to relocate the primary shard to another node.

##### Wait for active shards

Because the split operation creates a new index to split the shards to,
the wait for active shards setting
on index creation applies to the split index action as well.

#### Path parameters

`<index>`::
(Required, string)
Name of the source index to split.

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
