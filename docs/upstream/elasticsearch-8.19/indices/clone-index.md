<!-- Converted from indices/clone-index.asciidoc (AsciiDoc). Includes are inlined. -->

### Clone index API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Clones an existing index.

```console
POST /my-index-000001/_clone/cloned-my-index-000001
```

#### Request

`POST /<index>/_clone/<target-index>`

`PUT /<index>/_clone/<target-index>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the index you want to clone.

* To clone an index, the index must be marked as read-only and have a
cluster health status of `green`.

For example,
the following request prevents write operations on `my_source_index`
so it can be cloned using the
add index block API.
Metadata changes like deleting the index are still allowed.

```console
PUT /my_source_index/_block/write
```

The current write index on a data stream cannot be cloned. In order to clone
the current write index, the data stream must first be
rolled over so that a new write index is created
and then the previous write index can be cloned.

#### Description

Use the clone index API to clone an existing index into a new index, where each
original primary shard is cloned into a new primary shard in the new index.

**Important:**
Elasticsearch doesn't apply index templates to the resulting index. The API
also doesn't copy index metadata from the original index. Index metadata
includes aliases, ILM phase definitions, and CCR follower
information. For example, if you clone a CCR follower index, the
resulting clone won't be a follower index.

The clone API copies most index settings from the source index to the resulting
index, with the exception of `index.number_of_replicas` and
`index.auto_expand_replicas`. To set the number of replicas in the resulting
index, configure these settings in the clone request.

##### How cloning works

Cloning works as follows:

* First, it creates a new target index with the same definition as the source
  index.

* Then it hard-links segments from the source index into the target index. (If
  the file system doesn't support hard-linking, then all segments are copied
  into the new index, which is a much more time consuming process.)

* Finally, it recovers the target index as though it were a closed index which
  had just been re-opened.

##### Clone an index

To clone `my_source_index` into a new index called `my_target_index`, issue
the following request:

```console
POST /my_source_index/_clone/my_target_index
```

The above request returns immediately once the target index has been added to
the cluster state -- it doesn't wait for the clone operation to start.

=====================================

Indices can only be cloned if they meet the following requirements:

* The target index must not exist.

* The source index must have the same number of primary shards as the target index.

* The node handling the clone process must have sufficient free disk space to
  accommodate a second copy of the existing index.

=====================================

The `_clone` API is similar to the `create index` API
and accepts `settings` and `aliases` parameters for the target index:

```console
POST /my_source_index/_clone/my_target_index
{
  "settings": {
    "index.number_of_shards": 5 <1>
  },
  "aliases": {
    "my_search_indices": {}
  }
}
```

<1> The number of shards in the target index. This must be equal to the
    number of shards in the source index.

**Note:** Mappings may not be specified in the `_clone` request. The mappings of
the source index will be used for the target index.

##### Monitor the cloning process

The cloning process can be monitored with the <<cat-recovery,`_cat recovery`
API>>, or the `cluster health` API can be used to wait
until all primary shards have been allocated by setting the  `wait_for_status`
parameter to `yellow`.

The `_clone` API returns as soon as the target index has been added to the
cluster state, before any shards have been allocated. At this point, all
shards are in the state `unassigned`. If, for any reason, the target index
can't be allocated, its primary shard will remain `unassigned` until it
can be allocated on that node.

Once the primary shard is allocated, it moves to state `initializing`, and the
clone process begins. When the clone operation completes, the shard will
become `active`. At that point, Elasticsearch will try to allocate any
replicas and may decide to relocate the primary shard to another node.

##### Wait for active shards

Because the clone operation creates a new index to clone the shards to,
the wait for active shards setting
on index creation applies to the clone index action as well.

#### Path parameters

`<index>`::
(Required, string)
Name of the source index to clone.

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
