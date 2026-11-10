<!-- Converted from eql/eql-search-api.asciidoc (AsciiDoc). Includes are inlined. -->

### EQL search API

**New API reference**
For the most up-to-date API details, refer to [EQL APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-eql).

Returns search results for an Event Query Language (EQL) query.

EQL assumes each document in a data stream or index corresponds to an
event.

```console
GET /my-data-stream/_eql/search
{
  "query": """
    process where process.name == "regsvr32.exe"
  """
}
```

#### Request

`GET /<target>/_eql/search`

`POST /<target>/_eql/search`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the `read`
index privilege for the target data stream, index,
or alias.

* See eql-required-fields.

* experimental:[] For cross-cluster search, the local and remote clusters must
use the same Elasticsearch version if they have versions prior to 7.17.7 (included) or prior to 8.5.1 (included). For security, see remote-clusters.

##### Limitations

See EQL limitations.

#### Path parameters

`<target>`::
(Required, string) Comma-separated list of data streams, indices, or aliases
used to limit the request. Supports wildcards (`*`). To search all data streams
and indices, use `*` or `_all`.
experimental:[] To search a remote cluster, use the `<cluster>:<target>` syntax.
See run-eql-search-across-clusters.

#### Query parameters

`allow_no_indices`::
(Optional, Boolean)
**Note:** This parameter's behavior differs from the `allow_no_indices` parameter
used in other multi-target APIs.
If `false`, the request returns an error if any wildcard pattern, alias, or
`_all` value targets only missing or closed indices. This behavior applies even
if the request targets other open indices. For example, a request targeting
`foo*,bar*` returns an error if an index starts with `foo` but no index starts
with `bar`.
If `true`, only requests that exclusively target missing or closed indices
return an error. For example, a request targeting `foo*,bar*` does not return an
error if an index starts with `foo` but no index starts with `bar`. However, a
request that targets only `bar*` still returns an error.
Defaults to `true`.

`allow_partial_search_results`::
(Optional, Boolean)

If `false`, the request returns an error if one or more shards involved in the query are unavailable.
If `true`, the query is executed only on the available shards, ignoring shard request timeouts and
shard failures.
Defaults to `true`.
To override the default for this field, set the
`xpack.eql.default_allow_partial_results` cluster setting to `false`.

**Important:**
You can also specify this value using the `allow_partial_search_results` request body parameter.
If both parameters are specified, only the query parameter is used.

`allow_partial_sequence_results`::
(Optional, Boolean)

Used together with `allow_partial_search_results=true`, controls the behavior of sequence queries specifically
(if `allow_partial_search_results=false`, this setting has no effect).
If `true` and if some shards are unavailable, the sequences are calculated on available shards only.
If `false` and if some shards are unavailable, the query only returns information about the shard failures,
but no further results.
Defaults to `false`.
Consider that sequences calculated with `allow_partial_search_results=true` can return incorrect results
(eg. if a missing event clause matches records in unavailable shards)
To override the default for this field, set the
`xpack.eql.default_allow_partial_sequence_results` cluster setting to `true`.

**Important:**
You can also specify this value using the `allow_partial_sequence_results` request body parameter.
If both parameters are specified, only the query parameter is used.

`ccs_minimize_roundtrips`::
(Optional, Boolean) If `true`, network round-trips between the local and the
remote cluster are minimized when running cross-cluster search (CCS) requests.
This option is effective for requests that target data fully contained in one
remote cluster; when data is spread across multiple clusters, the setting is
ignored.
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

`filter_path`::
(Optional, string)
Comma-separated list of filters for the API response. See
common-options-response-filtering.

`ignore_unavailable`::
(Optional, Boolean) If `false`, the request returns an error if it targets a
missing or closed index. Defaults to `true`.

`keep_alive`::
(Optional, time value)
Period for which the search and its results are stored on the cluster. Defaults
to `5d` (five days).

When this period expires, the search and its results are deleted, even if the
search is still ongoing.

If the `keep_on_completion` parameter is
`false`, Elasticsearch only stores async searches that do not
complete within the period set by the
`wait_for_completion_timeout`
parameter, regardless of this value.

**Important:**
You can also specify this value using the `keep_alive` request body parameter.
If both parameters are specified, only the query parameter is used.

`keep_on_completion`::
(Optional, Boolean)
If `true`, the search and its results are stored on the cluster.

If `false`, the search and its results are stored on the cluster only if the
request does not complete during the period set by the
`wait_for_completion_timeout`
parameter. Defaults to `false`.

**Important:**
You can also specify this value using the `keep_on_completion` request body
parameter. If both parameters are specified, only the query parameter is used.

`wait_for_completion_timeout`::
(Optional, time value)
Timeout duration to wait for the request to finish. Defaults to no
timeout, meaning the request waits for complete search results.

If this parameter is specified and the request completes during this period,
complete search results are returned.

If the request does not complete during this period, the search becomes an
async search.

**Important:**
You can also specify this value using the `wait_for_completion_timeout` request
body parameter. If both parameters are specified, only the query parameter is
used.

#### Request body

`event_category_field`::
(Required*, string)
Field containing the event classification, such as `process`, `file`, or
`network`.
Defaults to `event.category`, as defined in the {ecs-ref}/ecs-event.html[Elastic
Common Schema (ECS)]. If a data stream or index does not contain the
`event.category` field, this value is required.
The event category field must be mapped as a field type in the
`keyword` family.

`fetch_size`::
(Optional, integer)
Maximum number of events to search at a time for sequence queries. Defaults to
`1000`.
This value must be greater than `2` but cannot exceed the value of the
`index.max_result_window` setting, which defaults to
`10000`.
Internally, a sequence query fetches and paginates sets of events to search for
matches. This parameter controls the size of those sets. This parameter does not
limit the total number of events searched or the number of matching events
returned.
A greater `fetch_size` value often increases search speed but uses more memory.

`fields`::
(Optional, array of strings and objects)
Array of field patterns. The request returns values for field names matching
these patterns in the `hits.fields` property of the response.
You can specify items in the array as a string or object. See
the `fields` option.
**Properties of `fields` objects**
`field`::
(Required, string) Field to return. Supports wildcards (`*`).

`format`::
(Optional, string)
Format for date and geospatial fields. Other field data types do not support
this parameter.
`date` and `date_nanos` fields accept a
date format. `geo_point` and
`geo_shape` fields accept:

`geojson` (default):::
[GeoJSON](http://www.geojson.org)

`wkt`:::
[Well Known Text](https://en.wikipedia.org/wiki/Well-known_text_representation_of_geometry)

`mvt(<spec>)`:::
Binary
[Mapbox vector tile](https://docs.mapbox.com/vector-tiles/specification). The API
returns the tile as a base64-encoded string.
The `<spec>` has the format `<zoom>/<x>/<y>` with two optional suffixes: `@<extent>` and/or `:<buffer>`. For example, `2/0/1` or `2/0/1@4096:5`.
.`mvt` parameters
========
`<zoom>`::
(Required, integer) Zoom level for the tile. Accepts `0`-`29`.

`<x>`::
(Required, integer) X coordinate for the tile.

`<y>`::
(Required, integer) Y coordinate for the tile.

`<extent>`::
(Optional, integer) Size, in pixels, of a side of the tile. Vector tiles are
square with equal sides. Defaults to `4096`.

`<buffer>`::
(Optional, integer) Size, in pixels, of a clipping buffer outside the tile.
This allows renderers to avoid outline artifacts from geometries that extend past the extent of the tile. Defaults to `5`.
========
`filter`::
(Optional, Query DSL object)
Query, written in Query DSL, used to filter the events on which the EQL query
runs.

`keep_alive`::
(Optional, time value)
Period for which the search and its results are stored on the cluster. Defaults
to `5d` (five days).

When this period expires, the search and its results are deleted, even if the
search is still ongoing.

If the `keep_on_completion` parameter is
`false`, Elasticsearch only stores async searches that do not
complete within the period set by the
`wait_for_completion_timeout`
parameter, regardless of this value.

**Important:**
You can also specify this value using the `keep_alive` query parameter.
If both parameters are specified, only the query parameter is used.

`keep_on_completion`::
(Optional, Boolean)
If `true`, the search and its results are stored on the cluster.

If `false`, the search and its results are stored on the cluster only if the
request does not complete during the period set by the
`wait_for_completion_timeout`
parameter. Defaults to `false`.

**Important:**
You can also specify this value using the `keep_on_completion` query parameter.
If both parameters are specified, only the query parameter is used.

`query`::
(Required, string)
EQL query you wish to run.

`result_position`::
(Optional, enum)
Set of matching events or sequences to return.
**Valid values for `result_position`**
`tail`::
(Default)
Return the most recent matches, similar to the https://en.wikipedia.org/wiki/Tail_(Unix)[Unix tail
command].

`head`::
Return the earliest matches, similar to the https://en.wikipedia.org/wiki/Head_(Unix)[Unix head
command].
**Note:** This parameter may change the set of returned hits. However, it does not
change the sort order of hits in the response.

`runtime_mappings`::
(Optional, object of objects)
Defines one or more runtime fields in the search
request. These fields take precedence over mapped fields with the same name.
**Properties of `runtime_mappings` objects**

`<field-name>`::
(Required, object)
Configuration for the runtime field. The key is the field name.
**Properties of `<field-name>`**
=====

`type`::
(Required, string)
Field type, which can be any of the following:
* `boolean`
* `composite`
* `date`
* `double`
* `geo_point`
* `ip`
* `keyword`
* `long`
* `lookup`
`script`::
(Optional, string)
Painless script executed at query time. The
script has access to the entire context of a document, including the original
`_source` and any mapped fields plus their values.
This script must include `emit` to return calculated values. For example:
```js
      "script": "emit(doc['@timestamp'].value.dayOfWeekEnum.toString())"
```

=====
`size`::
(Optional, integer or float)
For basic queries, the maximum number of matching events to
return.
For sequence queries, the maximum number of matching sequences
to return.
Defaults to `10`. This value must be greater than `0`.
**Note:** You cannot use pipes, such as `head` or `tail`, to exceed
this value.

`tiebreaker_field`::
(Optional, string)
Field used to sort hits with the same
timestamp in ascending order. See
eql-search-specify-a-sort-tiebreaker.

`timestamp_field`::
(Required*, string)
Field containing event timestamp.

Defaults to `@timestamp`, as defined in the
{ecs-ref}/ecs-event.html[Elastic Common Schema (ECS)]. If a data stream or index
does not contain the `@timestamp` field, this value is required.

Events in the API response are sorted by this field's value, converted to
milliseconds since the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time), in
ascending order.

The timestamp field should be mapped as a `date`. The
`date_nanos` field type is not supported.

`wait_for_completion_timeout`::
(Optional, time value)
Timeout duration to wait for the request to finish. Defaults to no
timeout, meaning the request waits for complete search results.

If this parameter is specified and the request completes during this period,
complete search results are returned.

If the request does not complete during this period, the search becomes an
async search.

**Important:**
You can also specify this value using the `wait_for_completion_timeout` query
parameter. If both parameters are specified, only the query parameter is used.

#### Response body

`id`::
(string)
Identifier for the search.

This search ID is only provided if one of the following conditions is met:

* A search request does not return complete results during the
  `wait_for_completion_timeout`
  parameter's timeout period, becoming an async search.

* The search request's `keep_on_completion`
  parameter is `true`.

You can use this ID with the <<get-async-eql-search-api,get async EQL search
API>> to get the current status and available results for the search or
get async EQL status API to get only
the current status.

`is_partial`::
(Boolean)
If `true`, the response does not contain complete search results.

`is_running`::
(Boolean)
If `true`, the search request is still executing.

**Important:**
If this parameter and the `is_partial` parameter are `true`, the search is an
ongoing async search. If the `keep_alive` period does not
pass, the complete search results will be available when the search completes.

If `is_partial` is `true` but `is_running` is `false`, the search returned
partial results due to a failure. Only some shards returned results or the node
coordinating the search failed.

`took`::
(integer)
Milliseconds it took Elasticsearch to execute the request.

This value is calculated by measuring the time elapsed
between receipt of a request on the coordinating node
and the time at which the coordinating node is ready to send the response.

Took time includes:

* Communication time between the coordinating node and data nodes
* Time the request spends in the `search` thread pool,
  queued for execution
* Actual execution time

Took time does *not* include:

* Time needed to send the request to Elasticsearch
* Time needed to serialize the JSON response
* Time needed to send the response to a client

`timed_out`::
(Boolean)
If `true`, the request timed out before completion.

`hits`::
(object)
Contains matching events and sequences. Also contains related metadata.
**Properties of `hits`**

`total`::
(object)
Metadata about the number of matching events or sequences.
**Properties of `total`**
=====

`value`::
(integer)
For basic queries, the total number of matching events.
For sequence queries, the total number of matching sequences.

`relation`::
(string)
Indicates whether the number of events or sequences returned is accurate or a
lower bound.

Returned values are:

`eq`::: Accurate
`gte`::: Lower bound, including returned events or sequences
=====

`sequences`::
(array of objects)
Contains event sequences matching the query. Each object represents a
matching sequence. This parameter is only returned for EQL queries containing
a sequence.
**Properties of `sequences` objects**
=====
`join_keys`::
(array of values)
Shared field values used to constrain matches in the sequence. These are defined
using the `by` keyword in the EQL query syntax.

`events`::
(array of objects)
Contains events matching the query. Each object represents a
matching event.
**Properties of `events` objects**
======
`_index`::
(string)
Name of the index containing the event.

`_id`::
(string)
Unique identifier for the event.
This ID is only unique within the index.

`_source`::
(object)
Original JSON body passed for the event at index time.
======
=====

`events`::
(array of objects)
Contains events matching the query. Each object represents a
matching event.
**Properties of `events` objects**
=====
`_index`::
(string)
Name of the index containing the event.

`_id`::
(string)
(string)
Unique identifier for the event.
This ID is only unique within the index.

`_source`::
(object)
Original JSON body passed for the event at index time.
=====

#### Examples

##### Basic query example

The following EQL search request searches for events with an `event.category` of
`process` that meet the following conditions:

* A `process.name` of `cmd.exe`
* An `process.pid` other than `2013`

```console
GET /my-data-stream/_eql/search
{
  "query": """
    process where (process.name == "cmd.exe" and process.pid != 2013)
  """
}
```

The API returns the following response. Matching events in the `hits.events`
property are sorted by timestamp, converted
to milliseconds since the [Unix epoch](https://en.wikipedia.org/wiki/Unix_time),
in ascending order.

If two or more events share the same timestamp, the
`tiebreaker_field` field is used to sort
the events in ascending order.

```console-result
{
  "is_partial": false,
  "is_running": false,
  "took": 6,
  "timed_out": false,
  "hits": {
    "total": {
      "value": 2,
      "relation": "eq"
    },
    "events": [
      {
        "_index": ".ds-my-data-stream-2099.12.07-000001",
        "_id": "babI3XMBI9IjHuIqU0S_",
        "_source": {
          "@timestamp": "2099-12-06T11:04:05.000Z",
          "event": {
            "category": "process",
            "id": "edwCRnyD",
            "sequence": 1
          },
          "process": {
            "pid": 2012,
            "name": "cmd.exe",
            "executable": "C:\\Windows\\System32\\cmd.exe"
          }
        }
      },
      {
        "_index": ".ds-my-data-stream-2099.12.07-000001",
        "_id": "b6bI3XMBI9IjHuIqU0S_",
        "_source": {
          "@timestamp": "2099-12-07T11:06:07.000Z",
          "event": {
            "category": "process",
            "id": "cMyt5SZ2",
            "sequence": 3
          },
          "process": {
            "pid": 2012,
            "name": "cmd.exe",
            "executable": "C:\\Windows\\System32\\cmd.exe"
          }
        }
      }
    ]
  }
}
```

##### Sequence query example

The following EQL search request matches a sequence of events
that:

. Start with an event with:
* An `event.category` of `file`
* A `file.name` of `cmd.exe`
* An `process.pid` other than `2013`
. Followed by an event with:
* An `event.category` of `process`
* A `process.executable` that contains the substring `regsvr32`

These events must also share the same `process.pid` value.

```console
GET /my-data-stream/_eql/search
{
  "query": """
    sequence by process.pid
      [ file where file.name == "cmd.exe" and process.pid != 2013 ]
      [ process where stringContains(process.executable, "regsvr32") ]
  """
}
```

The API returns the following response. Matching sequences are included in the
`hits.sequences` property. The `hits.sequences.join_keys` property contains the
shared `process.pid` value for each matching event.

```console-result
{
  "is_partial": false,
  "is_running": false,
  "took": 6,
  "timed_out": false,
  "hits": {
    "total": {
      "value": 1,
      "relation": "eq"
    },
    "sequences": [
      {
        "join_keys": [
          2012
        ],
        "events": [
          {
            "_index": ".ds-my-data-stream-2099.12.07-000001",
            "_id": "AtOJ4UjUBAAx3XR5kcCM",
            "_source": {
              "@timestamp": "2099-12-06T11:04:07.000Z",
              "event": {
                "category": "file",
                "id": "dGCHwoeS",
                "sequence": 2
              },
              "file": {
                "accessed": "2099-12-07T11:07:08.000Z",
                "name": "cmd.exe",
                "path": "C:\\Windows\\System32\\cmd.exe",
                "type": "file",
                "size": 16384
              },
              "process": {
                "pid": 2012,
                "name": "cmd.exe",
                "executable": "C:\\Windows\\System32\\cmd.exe"
              }
            }
          },
          {
            "_index": ".ds-my-data-stream-2099.12.07-000001",
            "_id": "OQmfCaduce8zoHT93o4H",
            "_source": {
              "@timestamp": "2099-12-07T11:07:09.000Z",
              "event": {
                "category": "process",
                "id": "aR3NWVOs",
                "sequence": 4
              },
              "process": {
                "pid": 2012,
                "name": "regsvr32.exe",
                "command_line": "regsvr32.exe  /s /u /i:https://...RegSvr32.sct scrobj.dll",
                "executable": "C:\\Windows\\System32\\regsvr32.exe"
              }
            }
          }
        ]
      }
    ]
  }
}
```
