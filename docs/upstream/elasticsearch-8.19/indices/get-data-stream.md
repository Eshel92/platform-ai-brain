<!-- Converted from indices/get-data-stream.asciidoc (AsciiDoc). Includes are inlined. -->

### Get data stream API

**New API reference**
For the most up-to-date API details, refer to [Data stream APIs](https://www.elastic.co/docs/api/doc/elasticsearch/group/endpoint-data-stream).

Retrieves information about one or more data streams.
See get-info-about-data-stream.

```console
GET /_data_stream/my-data-stream
```

#### Request

`GET /_data_stream/<data-stream>`

#### Prerequisites

* If the Elasticsearch security features are enabled, you must have the
`view_index_metadata` or `manage` index privilege
for the data stream.

#### Path parameters

`<data-stream>`::
(Optional, string)
Comma-separated list of data stream names used to limit the request. Wildcard
(`*`) expressions are supported. If omitted, all data streams will be
returned.

#### Query parameters

`expand_wildcards`::
(Optional, string)
Type of data stream that wildcard patterns can match. Supports
comma-separated values, such as `open,hidden`. Valid values are:

`all`, `hidden`::
Match any data stream, including hidden ones.

`open`, `closed`::
Matches any non-hidden data stream. Data streams cannot be closed.

`none`::
Wildcard patterns are not accepted.
Defaults to `open`.

`include_defaults`::
(Optional, Boolean) Functionality in preview:[]. If `true`, return all default settings in the response.
Defaults to `false`.

`verbose`::
(Optional, Boolean). If `true`, Returns the `maximum_timestamp` corresponding to the `@timestamp` field for documents in the data stream.
Defaults to `false`.

#### Response body

`data_streams`::
(array of objects)
Contains information about retrieved data streams.
**Properties of objects in `data_streams`**
`name`::
(string)
Name of the data stream.

`timestamp_field`::
(object)
Contains information about the data stream's `@timestamp` field.
**Properties of `timestamp_field`**
=====
`name`::
(string)
Name of the data stream's timestamp field, which must be `@timestamp`. The
`@timestamp` field must be included in every document indexed to the data
stream.
=====

`indices`::
(array of objects)
Array of objects containing information about the data stream's backing
indices.
The last item in this array contains information about the stream's current
write index.
**Properties of `indices` objects**
=====
`index_name`::
(string)
Name of the backing index. For naming conventions, see
data-streams-generation.

`index_uuid`::
(string)
Universally unique identifier (UUID) for the index.

`prefer_ilm`::
(boolean)
Functionality in preview:[]. Indicates if this index is configured to prefer index lifecycle management
when both Index lifecycle management and Data stream lifecycle are configured to
manage this index.

`managed_by`::
(string)
Functionality in preview:[]. Indicates the system that managed this index.
=====

`generation`::
(integer)
Current generation for the data stream. This number
acts as a cumulative count of the stream's rollovers, starting at `1`.

`_meta`::
(object)
Custom metadata for the stream, copied from the `_meta` object of the
stream's matching index template. If empty,
the response omits this property.

`status`::
(string)
Health status of the data stream.
This health status is based on the state of the primary and replica shards of
the stream's backing indices.
**Values for `status`**
=====
`GREEN`:::
All shards are assigned.

`YELLOW`:::
All primary shards are assigned, but one or more replica shards are
unassigned.

`RED`:::
One or more primary shards are unassigned, so some data is unavailable.
=====

`template`::
(string)
Name of the index template used to create the data stream's backing indices.
The template's index pattern must match the name of this data stream. See
create an index template.

`ilm_policy`::
(string)
Name of the current ILM lifecycle policy in the stream's matching index
template. This lifecycle policy is set in the `index.lifecycle.name` setting.
If the template does not include a lifecycle policy, this property is not
included in the response.
**Note:** A data stream's backing indices may be assigned different lifecycle
policies. To retrieve the lifecycle policy for individual backing indices,
use the get index settings API.

`next_generation_managed_by`::
(string)
Functionality in preview:[]. Indicates the system that will managed the next generation index
(i.e. the next data stream write index).

`prefer_ilm`::
(boolean)
Functionality in preview:[]. Indicates if the index template used to create the data
stream's backing indices is configured to prefer Index lifecycle management when both Index lifecycle management and
Data stream lifecycle are configured to manage this index.

`hidden`::
(Boolean) If `true`, the data stream is hidden.

`system`::
(Boolean)
If `true`, the data stream is created and managed by an Elastic stack component
and cannot be modified through normal user interaction.

`allow_custom_routing`::
(Boolean)
If `true`, the data stream this data stream allows custom routing on write request.

`replicated`::
(Boolean)
If `true`, the data stream is created and managed by cross-cluster replication and the local
cluster can not write into this data stream or change its mappings.

`lifecycle`::
(object)
Functionality in preview:[]. Contains the configuration for the data stream lifecycle management of this data stream.
**Properties of `lifecycle`**
=====
`data_retention`::
(string)
If defined, every document added to this data stream will be stored at least for this time frame. Any time after this
duration the document could be deleted. When empty, every document in this data stream will be stored indefinitely.

`rollover`::
(object)
The conditions which will trigger the rollover of a backing index as configured by the cluster setting
`cluster.lifecycle.default.rollover`. This property is an implementation detail and it will only be retrieved when the query
param `include_defaults` is set to `true`. The contents of this field are subject to change.
=====

`rollover_on_write`::
(Boolean)
If `true`, the next write to this data stream will trigger a rollover first and the document will be
indexed in the new backing index. If the rollover fails the indexing request will fail too.

#### Examples

```console
GET _data_stream/my-data-stream*
```

The API returns the following response:

```console-result
{
  "data_streams": [
    {
      "name": "my-data-stream",
      "timestamp_field": {
        "name": "@timestamp"
      },
      "indices": [
        {
          "index_name": ".ds-my-data-stream-2099.03.07-000001",
          "index_uuid": "xCEhwsp8Tey0-FLNFYVwSg",
          "prefer_ilm": true,
          "ilm_policy": "my-lifecycle-policy",
          "managed_by": "Index Lifecycle Management",
          "index_mode": "standard"
        },
        {
          "index_name": ".ds-my-data-stream-2099.03.08-000002",
          "index_uuid": "PA_JquKGSiKcAKBA8DJ5gw",
          "prefer_ilm": true,
          "ilm_policy": "my-lifecycle-policy",
          "managed_by": "Index Lifecycle Management",
          "index_mode": "standard"
        }
      ],
      "generation": 2,
      "_meta": {
        "my-meta-field": "foo"
      },
      "status": "GREEN",
      "index_mode": "standard",
      "next_generation_managed_by": "Index Lifecycle Management",
      "prefer_ilm": true,
      "template": "my-index-template",
      "ilm_policy": "my-lifecycle-policy",
      "hidden": false,
      "system": false,
      "allow_custom_routing": false,
      "replicated": false,
      "rollover_on_write": false,
      "settings": {}
    },
    {
      "name": "my-data-stream-two",
      "timestamp_field": {
        "name": "@timestamp"
      },
      "indices": [
        {
          "index_name": ".ds-my-data-stream-two-2099.03.08-000001",
          "index_uuid": "3liBu2SYS5axasRt6fUIpA",
          "prefer_ilm": true,
          "ilm_policy": "my-lifecycle-policy",
          "managed_by": "Index Lifecycle Management",
          "index_mode": "standard"
        }
      ],
      "generation": 1,
      "_meta": {
        "my-meta-field": "foo"
      },
      "status": "YELLOW",
      "index_mode": "standard",
      "next_generation_managed_by": "Index Lifecycle Management",
      "prefer_ilm": true,
      "template": "my-index-template",
      "ilm_policy": "my-lifecycle-policy",
      "hidden": false,
      "system": false,
      "allow_custom_routing": false,
      "replicated": false,
      "rollover_on_write": false,
      "settings": {}
    }
  ]
}
```
