<!-- Converted from indices/shard-stores.asciidoc (AsciiDoc). Includes are inlined. -->

### Index shard stores API

**New API reference**
For the most up-to-date API details, refer to [Index APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-indices).

Retrieves store information
about replica shards in one or more indices.
For data streams, the API retrieves store
information for the stream's backing indices.

```console
GET /my-index-000001/_shard_stores
```

#### Request

`GET /<target>/_shard_stores`

`GET /_shard_stores`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `monitor` or
`manage` index privilege for the target data stream,
index, or alias.

#### Description

The index shard stores API returns the following information:

* The node on which each replica shard exists
* Allocation ID for each replica shard
* Unique ID for each replica shard
* Any errors encountered
  while opening the shard index
  or from an earlier failure

By default, the API only returns store information
for primary shards that are unassigned
or have one or more unassigned replica shards.

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

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `false`.
`status`::
(Optional, string)
Comma-separated list of shard health statuses
used to limit the request.

Valid values include:

`green`::
The primary shard and all replica shards are assigned.

`yellow`::
One or more replica shards are unassigned.

`red`::
The primary shard is unassigned.

`all`::
Return all shards,
regardless of health status.

Defaults to `yellow,red`.

`max_concurrent_shard_requests`::
(Optional, integer)
Maximum number of concurrent shard-level requests sent by the coordinating
node. Defaults to `100`. Larger values may yield a quicker response to requests
that target many shards, but may also cause a larger impact on other cluster
operations.

#### Examples

##### Get shard store information for a specific data stream or index

```console
GET /test/_shard_stores
```

##### Get shard store information for several data streams and indices

```console
GET /test1,test2/_shard_stores
```

##### Get shard store information for all data streams and indices

```console
GET /_shard_stores
```

##### Get shard store information based on cluster health

You can use the `status` query parameter
to limit returned information based on shard health.

The following request only returns information
for assigned primary and replica shards.

```console
GET /_shard_stores?status=green
```

The API returns the following response:

```console-result
{
   "indices": {
       "my-index-000001": {
           "shards": {
              "0": { <1>
                "stores": [ <2>
                    {
                        "sPa3OgxLSYGvQ4oPs-Tajw": { <3>
                            "name": "node_t0",
                            "ephemeral_id" : "9NlXRFGCT1m8tkvYCMK-8A",
                            "transport_address": "local[1]",
                            "external_id": "node_t0",
                            "attributes": {},
                            "roles": [...],
                            "version": "8.10.0",
                            "min_index_version": 7000099,
                            "max_index_version": 8100099
                        },
                        "allocation_id": "2iNySv_OQVePRX-yaRH_lQ", <4>
                        "allocation" : "primary|replica|unused" <5>
                        "store_exception": ... <6>
                    }
                ]
              }
           }
       }
   }
}
```

<1> The key is the corresponding shard id for the store information
<2> A list of store information for all copies of the shard
<3> The node information that hosts a copy of the store, the key
    is the unique node id.
<4> The allocation id of the store copy
<5> The status of the store copy, whether it is used as a
    primary, replica or not used at all
<6> Any exception encountered while opening the shard index or
    from earlier engine failure
