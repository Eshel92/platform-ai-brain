<!-- Converted from indices/rollover-index.asciidoc (AsciiDoc). Includes are inlined. -->

### Rollover API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Creates a new index for a data stream or index alias.

```console
POST my-data-stream/_rollover
```

#### Request

`POST /<rollover-target>/_rollover/`

`POST /<rollover-target>/_rollover/<target-index>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `manage`
index privilege for the rollover target.

#### Description

**Tip:** We recommend using ILM's `rollover` action to
automate rollovers. See ilm-index-lifecycle.

The rollover API creates a new index for a data stream or index alias.
The API's behavior depends on the rollover target.

**Roll over a data stream**

If you roll over a data stream, the API creates a new write index for the
stream. The stream's previous write index becomes a regular backing index. A
rollover also increments the data stream's generation. See
data-streams-rollover.

**Roll over an index alias with a write index**

**Tip:**
Prior to Elasticsearch 7.9, you'd typically use an
index alias with a write index
to manage time series data. Data streams replace this functionality, require
less maintenance, and automatically integrate with data tiers.
See convert-index-alias-to-data-stream.

If an index alias points to multiple indices, one of the indices must be a
write index. The rollover API creates a new write index
for the alias with `is_write_index` set to `true`. The API also sets
`is_write_index` to `false` for the previous write index.

**Roll over an index alias with one index**

If you roll over an index alias that points to only one index, the API creates a
new index for the alias and removes the original index from the alias.

##### Increment index names for an alias

When you roll over an index alias, you can specify a name for the new index. If
you don't specify a name and the current index ends with `-` and a number, such
as `my-index-000001` or `my-index-3`, the new index name increments that number.
For example, if you roll over an alias with a current index of
`my-index-000001`, the rollover creates a new index named `my-index-000002`.
This number is always 6 characters and zero-padded, regardless of the previous
index's name.

**Use date math with index alias rollovers**
****
If you use an index alias for time series data, you can use
date math in the index name to track the rollover
date. For example, you can create an alias that points to an index named
`<my-index-{now/d}-000001>`. If you create the index on May 6, 2099, the index's
name is `my-index-2099.05.06-000001`. If you roll over the alias on May 7, 2099,
the new index's name is `my-index-2099.05.07-000002`. For an example, see
roll-over-index-alias-with-write-index.
****

##### Wait for active shards

A rollover creates a new index and is subject to the
`wait_for_active_shards` setting.

#### Path parameters

`<rollover-target>`::
(Required, string)
Name of the data stream or index alias to roll over.

`<target-index>`::
(Optional, string)
Name of the index to create. Supports date math. Data
streams do not support this parameter.
If the name of the alias's current write index does not end with `-` and a
number, such as `my-index-000001` or `my-index-3`, this parameter is required.
Index names must meet the following criteria:

- Lowercase only
- Cannot include `\`, `/`, `*`, `?`, `"`, `<`, `>`, `|`, ` ` (space character), `,`, `#`
- Indices prior to 7.0 could contain a colon (`:`), but that's been deprecated and won't be supported in 7.0+
- Cannot start with `-`, `_`, `+`
- Cannot be `.` or `..`
- Cannot be longer than 255 bytes (note it is bytes, so multi-byte characters will count towards the 255 limit faster)
- Names starting with `.` are deprecated, except for hidden indices and internal indices managed by plugins

#### Query parameters

`dry_run`::
(Optional, Boolean)
If `true`, checks whether the current index satisfies the specified
`conditions` but does not perform a rollover. Defaults to `false`.

`lazy`::
(Optional, Boolean)
If `true`, signals that the data stream will be rolled over when the next
indexing operation occurs. Applies only to data streams. Defaults to `false`.

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
(Optional, object of objects) Aliases for the target index. Data streams do not
support this parameter.
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
`conditions`::
(Optional, object)
Conditions for the rollover. If specified, Elasticsearch only performs the rollover if
the current index satisfies these conditions. If this parameter is
not specified, Elasticsearch performs the rollover unconditionally.
If conditions are specified, at least one of them must be a max_* condition.
The index will rollover if any max_* condition is satisfied and all
min_* conditions are satisfied.
**Important:** To trigger a rollover, the current index must satisfy these conditions
at the time of the request. Elasticsearch does not monitor the index after the API
response. To automate rollover, use ILM's `rollover`
instead.
**Properties of `conditions`**
`max_age`::
(Optional,  time units)
Triggers rollover after the maximum elapsed time from index creation is reached.
The elapsed time is always calculated since the index creation time, even if the
index origination date is configured to a custom date, such as when using the
index.lifecycle.parse_origination_date or
index.lifecycle.origination_date settings.

`max_docs`::
(Optional, integer)
Triggers rollover after the specified maximum number of documents is reached.
Documents added since the last refresh are not included in the document count.
The document count does *not* include documents in replica shards.

`max_size`::
(Optional, byte units)
Triggers rollover when the index reaches a certain size.
This is the total size of all primary shards in the index.
Replicas are not counted toward the maximum index size.
**Tip:** To see the current index size, use the _cat indices API.
The `pri.store.size` value shows the combined size of all primary shards.

`max_primary_shard_size`::
(Optional, byte units)
Triggers rollover when the largest primary shard in the index reaches a certain size.
This is the maximum size of the primary shards in the index. As with `max_size`,
replicas are ignored.
**Tip:** To see the current shard size, use the _cat shards API.
The `store` value shows the size each shard, and `prirep` indicates whether a
shard is a primary (`p`) or a replica (`r`).

`max_primary_shard_docs`::
(Optional, integer)
Triggers rollover when the largest primary shard in the index reaches a certain number of documents.
This is the maximum docs of the primary shards in the index. As with `max_docs`,
replicas are ignored.
**Tip:** To see the current shard docs, use the _cat shards API.
The `docs` value shows the number of documents each shard.

`min_age`::
(Optional,  time units)
Prevents rollover until after the minimum elapsed time from index creation is reached.
See notes on `max_age`.

`min_docs`::
(Optional, integer)
Prevents rollover until after the specified minimum number of documents is reached.
See notes on `max_docs`.

`min_size`::
(Optional, byte units)
Prevents rollover until the index reaches a certain size.
See notes on `max_size`.

`min_primary_shard_size`::
(Optional, byte units)
Prevents rollover until the largest primary shard in the index reaches a certain size.
See notes on `max_primary_shard_size`.

`min_primary_shard_docs`::
(Optional, integer)
Prevents rollover until the largest primary shard in the index reaches a certain number of documents.
See notes on `max_primary_shard_docs`.

`mappings`::
(Optional, mapping object) Mapping for fields in the index. If
specified, this mapping can include:

* Field names
* Field data types
* Mapping parameters

See mapping.
Data streams do not support this parameter.

`settings`::
(Optional, index setting object) Configuration
options for the index. See index-modules-settings.
Data streams do not support this parameter.

#### Response body

`acknowledged`::
(Boolean)
If `true`, the request received a response from the master node within the
`timeout` period.

`shards_acknowledged`::
(Boolean)
If `true`, the request received a response from
active shards within the `master_timeout`
period.

`old_index`::
(string)
Previous index for the data stream or index alias. For data streams and index
aliases with a write index, this is the previous write index.

`new_index`::
(string)
Index created by the rollover. For data streams and index aliases with a write
index, this is the current write index.

`rolled_over`::
(Boolean)
If `true`, the data stream or index alias rolled over.

`dry_run`::
(Boolean)
If `true`, Elasticsearch did not perform the rollover.

`condition`::
(object)
Result of each condition specified in the request's `conditions`. If no
conditions were specified, this is an empty object.
**Properties of `condition`**
`<condition>`::
(Boolean) The key is each condition. The value is its result. If `true`, the
index met the condition.

`lazy`::
(Boolean)
If `true`, Elasticsearch did not perform the rollover, but successfully marked the data stream to be rolled
over at the next indexing event.

#### Examples

##### Roll over a data stream

The following request rolls over a data stream unconditionally.

```console
POST my-data-stream/_rollover
```

The following request rolls over a data stream lazily, meaning that the data stream
will roll over at the next indexing event. This ensures that mapping and setting changes
will be applied to the coming data, but it will avoid creating extra backing indices for
data streams with slow ingestion.

```console
POST my-data-stream/_rollover?lazy
```

The following request only rolls over the data stream if the current write index
meets one or more of the following conditions:

* The index was created 7 or more days ago.
* The index contains 1,000 or more documents.
* The index's largest primary shard is 50GB or larger.

```console
POST my-data-stream/_rollover
{
  "conditions": {
    "max_age": "7d",
    "max_docs": 1000,
    "max_primary_shard_size": "50gb",
    "max_primary_shard_docs": "2000"
  }
}
```

The API returns:

```console-result
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "old_index": ".ds-my-data-stream-2099.05.06-000001",
  "new_index": ".ds-my-data-stream-2099.05.07-000002",
  "rolled_over": true,
  "dry_run": false,
  "lazy": false,
  "conditions": {
    "[max_age: 7d]": false,
    "[max_docs: 1000]": true,
    "[max_primary_shard_size: 50gb]": false,
    "[max_primary_shard_docs: 2000]": false
  }
}
```

##### Roll over an index alias with a write index

The following request creates `<my-index-{now/d}-000001>` and sets it as the
write index for `my-alias`.

```console
# PUT <my-index-{now/d}-000001>
PUT %3Cmy-index-%7Bnow%2Fd%7D-000001%3E
{
  "aliases": {
    "my-alias": {
      "is_write_index": true
    }
  }
}
```

The following request only rolls over the alias if the current write index
meets one or more of the following conditions:

* The index was created 7 or more days ago.
* The index contains 1,000 or more documents.
* The index's largest primary shard is 50GB or larger.
```console
POST my-alias/_rollover
{
  "conditions": {
    "max_age": "7d",
    "max_docs": 1000,
    "max_primary_shard_size": "50gb",
    "max_primary_shard_docs": "2000"
  }
}
```

The API returns:

```console-result
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "old_index": "my-index-2099.05.06-000001",
  "new_index": "my-index-2099.05.07-000002",
  "rolled_over": true,
  "dry_run": false,
  "lazy": false,
  "conditions": {
    "[max_age: 7d]": false,
    "[max_docs: 1000]": true,
    "[max_primary_shard_size: 50gb]": false,
    "[max_primary_shard_docs: 2000]": false
  }
}
```

If the alias's index names use date math and you roll over indices at a regular
interval, you can use date math to narrow your searches. For example, the
following search targets indices created in the last three days.

```console
# GET /<my-index-{now/d}-*>,<my-index-{now/d-1d}-*>,<my-index-{now/d-2d}-*>/_search
GET /%3Cmy-index-%7Bnow%2Fd%7D-*%3E%2C%3Cmy-index-%7Bnow%2Fd-1d%7D-*%3E%2C%3Cmy-index-%7Bnow%2Fd-2d%7D-*%3E/_search
```

##### Roll over an index alias with one index

The following request creates `<my-index-{now/d}-000001>` and its alias, `my-write-alias`.

```console
# PUT <my-index-{now/d}-000001>
PUT %3Cmy-index-%7Bnow%2Fd%7D-000001%3E
{
  "aliases": {
    "my-write-alias": { }
  }
}
```

The following request only rolls over the alias if the current index
meets one or more of the following conditions:

* The index was created 7 or more days ago.
* The index contains 1,000 or more documents.
* The index's largest primary shard is 50GB or larger.
:target!:
:index!:

```console
POST my-write-alias/_rollover
{
  "conditions": {
    "max_age": "7d",
    "max_docs": 1000,
    "max_primary_shard_size": "50gb",
    "max_primary_shard_docs": "2000"
  }
}
```

The API returns:

```console-result
{
  "acknowledged": true,
  "shards_acknowledged": true,
  "old_index": "my-index-2099.05.06-000001",
  "new_index": "my-index-2099.05.07-000002",
  "rolled_over": true,
  "dry_run": false,
  "lazy": false,
  "conditions": {
    "[max_age: 7d]": false,
    "[max_docs: 1000]": true,
    "[max_primary_shard_size: 50gb]": false,
    "[max_primary_shard_docs: 2000]": false
  }
}
```

##### Specify settings during a rollover

Typically, you use an index template to automatically
configure indices created during a rollover. If you roll over an index alias,
you use the rollover API to add additional index settings or overwrite settings
in the template. Data streams do not support the `settings` parameter.

```console
POST my-alias/_rollover
{
  "settings": {
    "index.number_of_shards": 2
  }
}
```
