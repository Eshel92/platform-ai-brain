<!-- Converted from indices/create-index.asciidoc (AsciiDoc). Includes are inlined. -->

### Create index API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Creates a new index.

```console
PUT /my-index-000001
```

#### Request

`PUT /<index>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `create_index`
or `manage` index privilege for the target index. To
add the index to an alias, you must have the `manage` index privilege for the
alias.

#### Description

You can use the create index API to add a new index to an Elasticsearch cluster. When
creating an index, you can specify the following:

* Settings for the index
* Mappings for fields in the index
* Index aliases

#### Path parameters

`<index>`::
(Required, string) Name of the index you wish to create.

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
(Optional, object of objects) Aliases for the index.
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

`mappings`::
(Optional, mapping object) Mapping for fields in the index. If
specified, this mapping can include:

* Field names
* Field data types
* Mapping parameters

See mapping.
`settings`::
(Optional, index setting object) Configuration
options for the index. See index-modules-settings.

#### Examples

##### Index settings

Each index created can have specific settings
associated with it, defined in the body:

```console
PUT /my-index-000001
{
  "settings": {
    "index": {
      "number_of_shards": 3,  <1>
      "number_of_replicas": 2 <2>
    }
  }
}
```

<1> Default for `number_of_shards` is 1
<2> Default for `number_of_replicas` is 1 (ie one replica for each primary shard)

or more simplified

```console
PUT /my-index-000001
{
  "settings": {
    "number_of_shards": 3,
    "number_of_replicas": 2
  }
}
```

You do not have to explicitly specify `index` section inside the
`settings` section.

For more information regarding all the different index level settings
that can be set when creating an index, please check the
index modules section.

##### Mappings

The create index API allows for providing a mapping definition:

```console
PUT /test
{
  "settings": {
    "number_of_shards": 1
  },
  "mappings": {
    "properties": {
      "field1": { "type": "text" }
    }
  }
}
```

##### Aliases

The create index API allows also to provide a set of aliases:

```console
PUT /test
{
  "aliases": {
    "alias_1": {},
    "alias_2": {
      "filter": {
        "term": { "user.id": "kimchy" }
      },
      "routing": "shard-1"
    }
  }
}
```

Index alias names also support date math.

```console
PUT /logs
{
  "aliases": {
    "<logs_{now/M}>": {}
  }
}
```

##### Wait for active shards

By default, index creation will only return a response to the client when the primary copies of
each shard have been started, or the request times out. The index creation response will indicate
what happened:

```console-result
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "index": "logs"
}
```

`acknowledged` indicates whether the index was successfully created in the cluster, while
`shards_acknowledged` indicates whether the requisite number of shard copies were started for
each shard in the index before timing out. Note that it is still possible for either
`acknowledged` or `shards_acknowledged` to be `false`, but the index creation was successful.
These values simply indicate whether the operation completed before the timeout. If
`acknowledged` is `false`, then we timed out before the cluster state was updated with the
newly created index, but it probably will be created sometime soon. If `shards_acknowledged`
is `false`, then we timed out before the requisite number of shards were started (by default
just the primaries), even if the cluster state was successfully updated to reflect the newly
created index (i.e. `acknowledged=true`).

We can change the default of only waiting for the primary shards to start through the index
setting `index.write.wait_for_active_shards` (note that changing this setting will also affect
the `wait_for_active_shards` value on all subsequent write operations):

```console
PUT /test
{
  "settings": {
    "index.write.wait_for_active_shards": "2"
  }
}
```

or through the request parameter `wait_for_active_shards`:

```console
PUT /test?wait_for_active_shards=2
```

A detailed explanation of `wait_for_active_shards` and its possible values can be found
here.
